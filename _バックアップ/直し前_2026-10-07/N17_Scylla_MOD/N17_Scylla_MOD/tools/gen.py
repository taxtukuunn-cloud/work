#!/usr/bin/env python3
"""N17 スキュラの海底神殿（Scylla）カード一式の生成スクリプト（企画書v4対応・2026-09-24）

v4の要点
- ★得意技だけが累積スタック「深海度」を積む（マスター・上級+3、下級+2）。
- スタックは受けた側が個別に持つ：主人公＝相手プレイヤー.$深海度（上限12で敗北）、
  男モンスター＝相手.$深海度（上限6で海の眷属として敵側へ）。
- 攻撃時のセリフは、受けた側のスタック段階で変わる（主人公向け4段階・男モンスター向け4段階）。
- クラーケのふたなり挿入は、受けた側の $ほぐし が2未満なら「深淵の指ほぐし」に置き換わる。
- バトルはクエスト（EventList/Quest）。回想バトルでは敵のターン開始ごとに
  「特殊召喚させる／手札に加えさせる／ドローさせる／進める」を選べる。
- 敗北シナリオはマスターに28本集約し、クエストイベントの バトル開始 直後の if,is敗北 で流す（N12で実機確認済みの形）。
- 画像はすべて @初期設定 の & 変数（直接パスは使わない）。敗北CGの直後に フェードイン,1。

使い方：python3 gen.py  → out/N17_Scylla_MOD/ に Card/ と EventList/ を作る（UTF-8・CRLF）。
"""
import os, json, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCEN = os.path.join(BASE, "scen")
LINES = os.path.join(BASE, "lines")
OUT = os.path.join(BASE, "out", "N17_Scylla_MOD")
C = "Scylla"
P = f"#{C}/{C}_"
ST = "$深海度"
PMAX, MMAX = 12, 6

ROUTES = [("btl", 1), ("onani", 2), ("inochi", 3), ("onedari", 4)]
ATTACKERS = [("m1", 1), ("m2", 2), ("m3", 3), ("e1", 4), ("e2", 5), ("e3", 6), ("boss", 7)]
SPK = {"e1": "%セイレ", "e2": "%アネモ", "e3": "%メドゥ", "boss": "%クラーケ"}
G_LAST = f"$${C}_最後の責め手"
G_ROUTE = f"$${C}_敗北経路"
G_RECALL = f"$${C}_回想中"


def J(k):
    return json.load(open(os.path.join(LINES, k + ".json"), encoding="utf-8"))


def ind(lines, n=1):
    return [(" " * n) + l if l else l for l in lines]


def block(cond, body):
    return [f"if,{cond}", "{"] + ind(body) + ["}"]


def ifelse(cond, a, b):
    return [f"if,{cond}", "{"] + ind(a) + ["}else{"] + ind(b) + ["}"]


def write(rel, lines, trailing=True):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines) + ("\r\n" if trailing else ""))


def record(aid=None, route=None):
    """最後の責め手・負け方をカード変数と $$ の両方に記録"""
    out = []
    if aid is not None:
        out += [f"自分プレイヤー.$最後の責め手,=,{aid}", f"{G_LAST},=,{aid}"]
    if route is not None:
        out += [f"自分プレイヤー.$敗北経路,=,{route}", f"{G_ROUTE},=,{route}"]
    return out


# ---------------------------------------------------------------- スタック
def stage_calc():
    """受けた側のスタックから $段階（1〜4）と $主人公（1/0）を決める"""
    pl = ["$主人公,=,1", f"$値,=,相手プレイヤー.{ST}", "$段階,=,1"] + \
        block("$値,>=,4", ["$段階,=,2"]) + block("$値,>=,7", ["$段階,=,3"]) + block("$値,>=,10", ["$段階,=,4"])
    mo = ["$主人公,=,0", f"$値,=,相手.{ST}", "$段階,=,1"] + \
        block("$値,>=,2", ["$段階,=,2"]) + block("$値,>=,4", ["$段階,=,3"]) + block("$値,>=,5", ["$段階,=,4"])
    return ifelse("相手,==,相手プレイヤー", pl, mo)


def player_stage_only():
    return [f"$値,=,相手プレイヤー.{ST}", "$段階,=,1"] + \
        block("$値,>=,4", ["$段階,=,2"]) + block("$値,>=,7", ["$段階,=,3"]) + block("$値,>=,10", ["$段階,=,4"])


def add_player(n):
    return [f"相手プレイヤー.{ST},+=,{n}", f"$表示用,=,相手プレイヤー.{ST}",
            "説明,（あなたの深海度 {$表示用}／12）"] + \
        block(f"$表示用,>=,{PMAX}", ["説明,……深海度12。もう、陸には戻れない。", "とどめダメージ,相手プレイヤー,9999"])


def add_monster(n, conv_line):
    return [f"相手.{ST},+=,{n}", f"$表示用,=,相手.{ST}", "説明,（仲間の深海度 {$表示用}／6）"] + \
        block(f"$表示用,>=,{MMAX}", ["話者,自分", f"セリフ,{conv_line}",
                                    "説明,仲間の男は触手に抱かれ、とろんとした目で水底へ沈んでいき……海の眷属として敵側へ移った。",
                                    "コントロール変更,相手,自分所属"])


def add_target(n, conv_line):
    return ifelse("$主人公,==,1", add_player(n), add_monster(n, conv_line))


# ---------------------------------------------------------------- 攻撃
def staged(lines):
    out = []
    for i in range(4):
        out += block(f"$段階,==,{i+1}", [f"セリフ,{lines[i]}"])
    return out


def tech_body(t, cg, aid, gain, conv, extra=None):
    """技1つ分（攻撃タイプの if の中身）。gain=0 ならスタックを積まない"""
    b = ["話者,自分", f"技名表示,{t['name']}", f"画像,{cg},1"]
    b += ifelse("$主人公,==,1", staged(t["atk"]), staged(t["atk_mon"]))
    b += ["話者,相手"] + ifelse("$主人公,==,1", staged(t["rx"]), staged(t["rx_mon"]))
    eff = "&&キスエフェクト" if t["type"] == "キス" else "&&セクシーエフェクト"
    b += ["話者,自分", f"攻撃エフェクト変更,{eff}"] + record(aid) + ["$今回付与,=,1"]
    if extra:
        b += extra
    if gain:
        b += add_target(gain, conv)
    return b


def hogushi_body(h, cg, aid, conv):
    """深淵の指ほぐし：$ほぐし+1、得意技が挿入技なのでスタックも+1"""
    b = ["話者,自分", f"技名表示,{h['name']}", f"画像,{cg},1"]
    pl = ["$ほ,=,相手プレイヤー.$ほぐし"]
    mo = ["$ほ,=,相手.$ほぐし"]
    b += ifelse("$主人公,==,1", pl, mo)
    for side, atk, rx in (("1", h["atk"], h["rx"]), ("0", h["atk_mon"], h["rx_mon"])):
        seq = []
        seq += ifelse("$ほ,==,0", [f"セリフ,{atk[0]}", "話者,相手", f"セリフ,{rx[0]}"],
                      [f"セリフ,{atk[1]}", "話者,相手", f"セリフ,{rx[1]}"])
        b += block(f"$主人公,==,{side}", seq)
    b += ["話者,自分"] + ifelse("$主人公,==,1", ["相手プレイヤー.$ほぐし,+=,1"], ["相手.$ほぐし,+=,1"])
    b += ["説明,（指でほぐされた。二度ほぐされると、女王に貫かれてしまう）"] + record(aid) + ["$今回付与,=,1"]
    b += add_target(1, conv)
    return b


def battle_section(techs, aid, conv, star_idx, star_gain, hogushi=None, extras=None):
    """@戦闘。techs=[(tech, cg)]、star_idx=得意技の番号"""
    extras = extras or {}
    out = ["@戦闘", "攻撃タイプランダム変更," + ",".join(t["type"] for t, _ in techs), "$今回付与,=,0"] + stage_calc()
    for i, (t, cg) in enumerate(techs):
        gain = star_gain if i == star_idx else 0
        body = tech_body(t, cg, aid if isinstance(aid, int) else aid[i], gain, conv, extras.get(i))
        if hogushi is not None and i == star_idx:
            need = ifelse("$主人公,==,1", ["$ほ,=,相手プレイヤー.$ほぐし"], ["$ほ,=,相手.$ほぐし"])
            body = need + ifelse("$ほ,<,2", hogushi_body(hogushi, cg, aid if isinstance(aid, int) else aid[i], conv), body)
        out += block(f"攻撃タイプ,==,{t['type']}", body)
    out += block("$今回付与,==,0", record(aid if isinstance(aid, int) else aid[0]))
    return out + [""]


def street_hooks(sections):
    out = []
    for s in sections:
        out += [f"@{s}_街バトル", f"    イベント実行,{s}", ""]
    return out


# ---------------------------------------------------------------- 敗北シナリオ
def read_scen(route, att):
    out = []
    for l in open(os.path.join(SCEN, f"{C}_lose_{route}_{att}.txt"), encoding="utf-8-sig"):
        s = l.rstrip("\r\n").strip()
        if s and s != "default" and not s.startswith("@"):
            out.append(s)
    return out


def scen_section(route, att):
    body = []
    for s in read_scen(route, att):
        if s.startswith("画像,#"):
            body += [f"画像,&敗北CG_{route}_{att},1", "フェードイン,1"]
            continue
        if s == "話者,自分" and att in SPK:
            s = "話者," + SPK[att]
        elif s == "話者,相手":
            s = "話者,相手プレイヤー"
        body.append(s)
    return [f"@敗北_{route}_{att}"] + ind(body, 4) + [""]


def replay_section():
    """@敗北再生：$経路・$責め手 に従って28本から1本を流す"""
    out = ["@敗北再生", "BGM,&&敗北BGM", "背景,&背景", "画像,&カード画像,1", "フェードイン,2"]
    out += [f"話者生成,{v},&画像_{k},女" for k, v in SPK.items()]
    for key, aid in ATTACKERS:
        inner = []
        for r, rid in ROUTES:
            inner += block(f"$経路,==,{rid}", [f"イベント実行,敗北_{r}_{key}"])
        out += block(f"$責め手,==,{aid}", inner)
    out += ["射精", "フェードアウト,2,true", "説明,GAME OVER"]
    return out + [""]


def resolve_route():
    return [f"$経路,=,{G_ROUTE}"] + block("死亡理由,==,オナニー", ["$経路,=,2"]) + \
        block("$経路,==,0", ["$経路,=,1"]) + [f"$責め手,=,{G_LAST}"] + block("$責め手,==,0", ["$責め手,=,1"])


# ---------------------------------------------------------------- 画像変数
def master_images():
    L = [f"    &カード画像,{P}master.png", f"    &背景,{P}bg.png"]
    for k in ("m1", "m2", "m3"):
        L.append(f"    &技CG_{k},{P}atk_{k}.png")
    for k in SPK:
        L.append(f"    &画像_{k},{P}{k}.png")
    for r, _ in ROUTES:
        for a, _ in ATTACKERS:
            L.append(f"    &敗北CG_{r}_{a},{P}lose_{r}_{a}.png")
    L += [f"    &オナニーCG,{P}onanie_m.png", f"    &命乞いCG,{P}inochigoi.png", f"    &おねだりCG,{P}onedari.png"]
    return L


# ---------------------------------------------------------------- マスター
def recall_menu():
    """回想バトル：プレイヤーが敵のデッキから選んで特殊召喚・手札に加える・ドローさせる"""
    loop = ["話者,自分",
            "説明,【回想バトル】メルティナにどう動いてほしいか選べます。",
            "選択肢生成,デッキから選んで特殊召喚させる,デッキから選んで手札に加えさせる,1枚ドローさせる,このまま進める"]
    loop += block("選択肢,==,1", ["%候補,=,自分デッキ.?isモンスター:true", "カード選択,%候補,1,1",
                                  "特殊召喚,選択カード,味方", "セリフ,ふふ、この子を呼んでほしいのね。いいわ。"])
    loop += block("選択肢,==,2", ["%候補,=,自分デッキ", "カード選択,%候補,1,1",
                                  "効果サーチ,選択カード,自分所属", "セリフ,これを使ってほしいの？　欲張りな陸の子。"])
    loop += block("選択肢,==,3", ["効果ドロー,自分プレイヤー", "セリフ,もう一枚、引いてあげる。"])
    loop += block("選択肢,==,4", ["$回想メニュー,=,0"])
    return block(f"{G_RECALL},==,1", ["$回想メニュー,=,1"] + ["while,$回想メニュー,==,1", "{"] + ind(loop) + ["}"])


def master():
    m1, m2, m3 = J("m1"), J("m2"), J("m3")
    t1, t2, t3 = m1["tech"], m2["tech"], m3["tech"]
    conv = m3["convert"]
    L = ["default", "@初期設定",
         "    &カード名,海魔 メルティナ",
         "    レベル設定,8", "    攻撃力設定,1000", "    最大HP設定,10000",
         "    属性設定,水属性", "    タイプ設定,水棲", "    性別設定,女", "    レアリティ設定,UR",
         "    攻撃エフェクト設定,&&セクシーエフェクト"] + master_images() + [
         "    効果設定,1,explain,★得意技【吸盤の愛撫】が当たると、受けた相手の【深海度】+3。深海度は主人公と仲間の男モンスターが1人ずつ別々に持つ（減らない）。主人公は12で海の眷属（敗北）、男モンスターは6で海の眷属として敵側へ移る。ほかの技は深海度を積まないが、受けた相手の深海度に応じてセリフが変わる。ターン終了時、主人公の深海度に応じて　1〜3：魅了／4〜6：拘束／7〜9：魅了＋拘束／10〜11：拘束2ターン＋500ダメージ。",
         "    効果設定,0,explain," + m2["flavor_master"] + "（身長175cm・触手を広げると約4m／B98・W59）。得意技：吸盤の愛撫",
         ""]

    # クエストイベント
    first = ["背景,&背景"]
    shown = False
    for x in m1["field_first"]:
        if x["k"] == "セリフ" and not shown:
            first.append("画像,&カード画像,1")
            shown = True
        first.append(f"{x['k']},{x['t']}")
    won = ["画像,&カード画像,1"] + [f"セリフ,{s}" for s in m1["field_win"]]
    prev = ["画像,&カード画像,1"]
    for r, rid in ROUTES:
        prev += block(f"$${C}_前回敗北経路,==,{rid}", [f"セリフ,{s}" for s in m1["field_prev"][r]])
    prev += [f"アラート,{m1['continue_alert']}", "選択肢生成,勝負する,誘いに乗る,引き返す"]
    prev += block("選択肢,==,2", ["イベント実行,前回続き", "イベント終了"])
    prev += block("選択肢,==,3", ["セリフ,あら、帰ってしまうの？　ふふ、潮はまた満ちるわ。", "イベント終了"])
    deck = [f"{C}_mons_e1"] * 3 + [f"{C}_mons_e2"] * 3 + [f"{C}_mons_e3"] * 3 + [f"{C}_mons_boss"] + \
           [f"{C}_magic_{i}" for i in range(1, 6) for _ in range(2)]
    deckline = "デッキ設定," + ",".join(deck)
    reset = [f"{G_LAST},=,1", f"{G_ROUTE},=,0"]

    q = ["@クエストイベント", "話者,自分", f"{G_RECALL},=,0"]
    q += ifelse(f"$${C}_敗北回数,==,0", first, ifelse("is前回プレイヤー勝利,==,true", won, prev))
    q += [deckline, "デッキ報酬設定,300,300,0", f"$${C}_挑戦回数,+=,1"] + reset + ["バトル開始,&背景,&&戦闘BGM"]
    lose = resolve_route() + ["イベント実行,敗北再生",
                              f"$${C}_敗北回数,+=,1", f"$${C}_前回敗北経路,=,$経路", f"$${C}_前回最後の責め手,=,$責め手"]
    q += ifelse("is敗北,==,true", lose, ["話者,自分", "画像,&カード画像,1",
                                        "セリフ,……あら、負けてしまったわ。でも潮はまた満ちるの。次はもっと深いところで会いましょう、陸の子。"])
    L += q + [""]

    # 回想バトル
    r = ["@回想バトル", "話者,自分", "背景,&背景", "画像,&カード画像,1",
         "説明,【回想バトル】海底神殿の記憶。メルティナのデッキから好きなカードを呼ばせたり、引かせたりして戦える。勝敗の記録は残らない。",
         "セリフ,ふふ、また思い出しに来たの？　いいわ、あなたの好きな潮の満ち方で遊んであげる。",
         f"{G_RECALL},=,1", deckline] + reset + ["バトル開始,&背景,&&戦闘BGM"]
    r += block("is敗北,==,true", resolve_route() + ["イベント実行,敗北再生"])
    r += [f"{G_RECALL},=,0"]
    L += r + [""]

    L += ["@試合開始", "自分.$敗北経路,=,0", "自分.$最後の責め手,=,1", f"相手プレイヤー.{ST},=,0", "相手プレイヤー.$ほぐし,=,0",
          "話者,自分", f"セリフ,{m1['start']}",
          "説明,（★吸盤の愛撫を受けるたびに深海度が溜まる。あなたは12、仲間の男モンスターは6で海の眷属になる）"] + recall_menu() + [""]
    L += ["@ターン開始"] + recall_menu() + [""]

    L += ["@召喚宣言"] + player_stage_only() + ["話者,自分"]
    for i, s in enumerate(m3["summon_decl"]):
        L += block(f"$段階,==,{i+1}", [f"セリフ,{s}"])
    L += [""]

    L += battle_section([(t1, "&技CG_m1"), (t2, "&技CG_m2"), (t3, "&技CG_m3")], [1, 2, 3], conv, 0, 3)

    te = ["@ターン終了宣言"] + player_stage_only() + ["話者,自分"]
    eff = [["状態異常付与,相手プレイヤー,魅了,1"], ["状態異常付与,相手プレイヤー,拘束,1"],
           ["状態異常付与,相手プレイヤー,魅了,1", "状態異常付与,相手プレイヤー,拘束,1"],
           ["状態異常付与,相手プレイヤー,拘束,2", "イベントダメージ,相手プレイヤー,500"]]
    body = []
    for i in range(4):
        body += block(f"$段階,==,{i+1}", [f"セリフ,{m3['turnend'][i]}"] + eff[i])
    te += block("$値,>=,1", body)
    te += block(f"$値,>=,{PMAX}", ["セリフ,深海度、十二。……おかえりなさい、わたしの眷属。", "とどめダメージ,相手プレイヤー,9999"])
    L += te + [""]

    labels = ["吸盤で乳首を吸って", "甘い墨を吸わせて", "八本の脚で埋め尽くして"]
    types = [t1["type"], t2["type"], t3["type"]]
    L += ["@おねだり", "話者,自分", "画像,&おねだりCG,1", f"セリフ,{m2['onedari_open']}", "選択肢生成," + ",".join(labels)]
    for i in range(3):
        L += block(f"選択肢,==,{i+1}", ["話者,相手", f"セリフ,{m2['onedari_opts'][i]}", "話者,自分",
                                       "セリフ,ふふ、自分の口で言えたわね。いいわ、望みどおりに。",
                                       f"攻撃タイプ固定,{types[i]}", f"自分プレイヤー.$最後の技,=,{i+1}"] + record(i + 1))
    L += ["話者,相手", f"セリフ,{m2['onedari_rx']}"] + record(route=4) + ["状態異常付与,自分,弱点付与スキル,1", ""]
    L += ["@おねだり後", "攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル"] + \
        block("相手プレイヤー.HP,>,0", record(route=0)) + [""]

    ino = ["@命乞い", "話者,自分", "画像,&命乞いCG,1"] + [f"セリフ,{s}" for s in m3["inochi"]]
    ino += ["選択肢生成,とどめを刺す,手が止まる"]
    ino += block("選択肢,==,1", [f"セリフ,{m3['inochi_fail']}", "命乞い失敗", "イベント終了"])
    ino += record(route=3) + ["$技,=,自分プレイヤー.$最後の技"] + block("$技,==,0", ["$技,=,1"]) + \
        ["自分プレイヤー.$最後の責め手,=,$技", f"{G_LAST},=,$技"] + [f"セリフ,{s}" for s in m3["inochi_win"]] + \
        ["話者,相手", f"セリフ,{m3['inochi_rx']}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ino

    ona = ["@オナニー", "画像,&オナニーCG,1"] + record(route=2) + \
        ["$技,=,自分プレイヤー.$最後の技"] + block("$技,==,0", ["$技,=,1"]) + \
        ["自分プレイヤー.$最後の責め手,=,$技", f"{G_LAST},=,$技", "話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{s}" for s in m1["onani_second"]], [f"セリフ,{s}" for s in m1["onani_first"]])
    ona += ["話者,相手", f"セリフ,{m1['onani_rx']}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@瀕死時セリフ", "話者,自分", f"セリフ,{m1['dying']}", ""]
    L += ["@終了時一言"] + block("自分プレイヤー.$敗北経路,==,0", record(route=1)) + ["話者,自分", f"セリフ,{m1['end']}", ""]
    L += replay_section()
    L += ["@前回続き", f"$経路,=,$${C}_前回敗北経路", f"$責め手,=,$${C}_前回最後の責め手"] + \
        block("$経路,==,0", ["$経路,=,1"]) + block("$責め手,==,0", ["$責め手,=,1"]) + \
        ["話者,自分", "画像,&カード画像,1"] + [f"セリフ,{s}" for s in m1["continue_lines"]] + \
        ["イベント実行,敗北再生", f"$${C}_敗北回数,+=,1", ""]
    for rr, _ in ROUTES:
        for a, _ in ATTACKERS:
            L += scen_section(rr, a)
    L += street_hooks(["戦闘", "オナニー", "おねだり", "おねだり後", "命乞い", "終了時一言", "瀕死時セリフ"])
    write(f"Card/{C}_master.txt", L)


# ---------------------------------------------------------------- モンスター
MONS = {
    "e1": dict(name="人魚 セイレ", aid=4, lv=4, atk=1100, hp=1500, rare="R", star=0, gain=2,
               explain="★得意技【人魚の歌声】が当たると、受けた相手の深海度+2（主人公は12、男モンスターは6で海の眷属）。歌声が命中すると相手に【魅了】1ターン。召喚時：主人公の深海度+1。",
               size="身長168cm・尾を含む全長2.4m／B86・W56", special="得意技：人魚の歌声",
               flavor="入り江の洞に棲む金の髪の人魚。寂しがりで、気に入った相手には耳元で歌い、口移しで息を分け与える。その歌を一度聞いた者は、潮騒の中にいつまでも同じ旋律を探してしまう。",
               summon_gain=1, extra={0: ["状態異常付与,相手,魅了,1"]}),
    "e2": dict(name="イソギンチャク娘 アネモ", aid=5, lv=4, atk=1300, hp=1500, rare="R", star=0, gain=2,
               explain="★得意技【揺れる触手】が当たると、受けた相手の深海度+2（主人公は12、男モンスターは6で海の眷属）。自分のターン終了時：相手の男モンスター1体に【発情】2ターン。",
               size="身長160cm／B82・W55・H84", special="得意技：揺れる触手",
               flavor="神殿脇の温かい岩場に根付くイソギンチャク娘。桃色の髪に細い触手の房を揺らし、気に入った相手を触手のスカートに座らせて離さない。刺胞の毒は痛くない。ただ、甘く火照るだけ。",
               endturn=("自分のターン終了時：相手の男モンスター1体に【発情】2ターン", "発情", 2)),
    "e3": dict(name="クラゲ娘 メドゥ", aid=6, lv=4, atk=1000, hp=1700, rare="R", star=0, gain=2,
               explain="★得意技【透明な糸】が当たると、受けた相手の深海度+2（主人公は12、男モンスターは6で海の眷属）。召喚時：相手の男モンスター1体に【麻痺】1ターン。",
               size="身長164cm／B78・W54・H80", special="得意技：透明な糸",
               flavor="光るクラゲの群れの中を漂う、白く透ける髪のクラゲ娘。いつもぼんやりしていて言葉は途切れがち。傘のドレスの裾から垂れる透明な糸は、触れたところに甘い痺れを残していく。",
               summon_status=("麻痺", 1)),
    "boss": dict(name="深海の女王 クラーケ", aid=7, lv=7, atk=2500, hp=3200, rare="UR", star=0, gain=3,
                 explain="★得意技【深淵の交わり】（触手で乳首＋ふたなりで後ろ）が当たると、受けた相手の深海度+3。受けた相手が指でほぐされていない（ほぐし2未満）時は、代わりに【深淵の指ほぐし】（ほぐし+1・深海度+1）。召喚時：主人公の深海度+3。固有効果【深淵の抱擁】：主人公の深海度6以上の時、自分のターン終了時に相手の男モンスター1体に【拘束】2ターン。",
                 size="身長190cm・触手の全長約10m／B104・W64", special="得意技：深淵の交わり",
                 flavor="神殿のさらに下、光の届かない海溝の玉座に座す深海の暴君。深紅の髪と黒い鱗の装束をまとい、巨大な触手で獲物を抱いたまま深淵へ降りていく。その番（つがい）に選ばれた者は、二度と水面を見ない。",
                 summon_gain=3,
                 endturn=("深淵の抱擁：主人公の深海度6以上の時、相手の男モンスター1体に【拘束】2ターン", "拘束", 2)),
}


def monster(key):
    m, d = MONS[key], J(key)
    L = ["default", "@初期設定",
         f"    &カード名,{m['name']}", f"    &カード画像,{P}{key}.png", f"    &技CG,{P}atk_{key}.png",
         f"    &オナニーCG,{P}onanie_{key}.png", f"    &命乞いCG,{P}inochigoi.png", f"    &おねだりCG,{P}onedari.png",
         f"    レベル設定,{m['lv']}", f"    攻撃力設定,{m['atk']}", f"    最大HP設定,{m['hp']}",
         "    属性設定,水属性", "    タイプ設定,水棲", "    性別設定,女", f"    レアリティ設定,{m['rare']}",
         "    攻撃エフェクト設定,&&セクシーエフェクト",
         f"    効果設定,9,explain,{m['explain']}"]
    has1 = m.get("summon_gain") or m.get("summon_status")
    if has1:
        L += ["    効果設定,1,forceTrigger,召喚時の効果", "    誘発効果設定,1,場に出た時", "    効果条件設定,1,トリガー受動カード,==,自分"]
        if m.get("summon_status"):
            L += ["    効果ターゲット設定,1,ランダム,相手モンスター.?性別:男,1"]
    if m.get("endturn"):
        L += [f"    効果設定,2,forceTrigger,{m['endturn'][0]}", "    誘発効果設定,2,エンドフェイズ開始時",
              "    効果条件設定,2,Now自分ターン,==,true", "    効果ターゲット設定,2,ランダム,相手モンスター.?性別:男,1"]
    L += [f"    効果設定,0,explain,{m['flavor']}（{m['size']}）。{m['special']}", ""]

    ef = ["@効果", "switch,効果ID"]
    if has1:
        c1 = ["話者,自分", "画像,&カード画像,1", f"セリフ,{d['summon']}"]
        if m.get("summon_status"):
            c1 += [f"状態異常付与,効果対象,{m['summon_status'][0]},{m['summon_status'][1]}"]
        if m.get("summon_gain"):
            c1 += add_player(m["summon_gain"])
        ef += ["case,1", "{"] + ind(c1, 4) + ["}"]
    if m.get("endturn"):
        c2 = ["話者,自分", f"セリフ,{d['turnend']}", f"状態異常付与,効果対象,{m['endturn'][1]},{m['endturn'][2]}"]
        if key == "boss":
            c2 = [f"$値,=,相手プレイヤー.{ST}"] + block("$値,>=,6", c2)
        ef += ["case,2", "{"] + ind(c2, 4) + ["}"]
    ef += ["endswitch", ""]
    L += ef

    techs = [(t, "&技CG") for t in d["techs"]]
    L += battle_section(techs, m["aid"], d["convert"], m["star"], m["gain"],
                        hogushi=d.get("hogushi") if key == "boss" else None, extras=m.get("extra"))

    t0, t1 = d["techs"]
    L += ["@おねだり", "話者,自分", "画像,&おねだりCG,1", f"セリフ,{d['onedari_open']}",
          f"選択肢生成,{d['onedari_opts'][0]},{d['onedari_opts'][1]}"]
    L += block("選択肢,==,1", [f"攻撃タイプ固定,{t0['type']}"]) + block("選択肢,==,2", [f"攻撃タイプ固定,{t1['type']}"])
    L += ["話者,相手", f"セリフ,{d['onedari_rx']}"] + record(m["aid"], 4) + ["状態異常付与,自分,弱点付与スキル,1", ""]
    L += ["@おねだり後", "攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル"] + \
        block("相手プレイヤー.HP,>,0", ["自分プレイヤー.$敗北経路,=,0", f"{G_ROUTE},=,0"]) + [""]

    ino = ["@命乞い", "話者,自分", "画像,&命乞いCG,1"] + [f"セリフ,{s}" for s in d["inochi"]]
    ino += ["選択肢生成,とどめを刺す,手が止まる"]
    ino += block("選択肢,==,1", [f"セリフ,{d['inochi_fail']}", "命乞い失敗", "イベント終了"])
    ino += record(m["aid"], 3) + [f"セリフ,{s}" for s in d["inochi_win"]] + \
        ["話者,相手", f"セリフ,{d['inochi_rx']}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ino

    ona = ["@オナニー", "画像,&オナニーCG,1"] + record(m["aid"], 2) + ["話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{s}" for s in d["onani_second"]], [f"セリフ,{s}" for s in d["onani_first"]])
    ona += ["話者,相手", f"セリフ,{d['onani_rx']}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@瀕死時セリフ", "話者,自分", f"セリフ,{d['dying']}", ""]
    L += ["@終了時一言", "話者,自分", f"セリフ,{d['end']}", ""]
    secs = ["効果", "戦闘", "オナニー", "おねだり", "おねだり後", "命乞い", "終了時一言", "瀕死時セリフ"]
    L += street_hooks(secs)
    write(f"Card/{C}_mons_{key}.txt", L)


# ---------------------------------------------------------------- 魔法・罠
def magic_defs():
    return [
        dict(no=1, k="tide", type="永続魔法", rare="SR",
             explain="発動時と、自分のターン終了時に主人公の深海度+1。3回目のターン終了時に自壊する。", body=add_player(1)),
        dict(no=2, k="whirl", type="通常罠", rare="R", trap=True,
             explain="相手の攻撃時に発動。攻撃してきたカードに【拘束】1ターン、主人公の深海度+1。",
             body=["状態異常付与,トリガー能動カード,拘束,1"] + add_player(1)),
        dict(no=3, k="song", type="通常魔法", rare="R", explain="相手の男モンスター1体に【魅了】2ターン。",
             target="効果ターゲット設定,1,選択,相手モンスター.?性別:男,1", body=["状態異常付与,効果対象,魅了,2"]),
        dict(no=4, k="call", type="通常魔法", rare="N", explain="自分のデッキから海の娘（モンスター）1枚をランダムに手札に加える。",
             target="効果ターゲット設定,1,ランダム,自分デッキ.?isモンスター:true,1", body=["効果サーチ,効果対象,自分所属"]),
        dict(no=5, k="ink", type="通常魔法", rare="R", explain="主人公の深海度+2。", body=add_player(2)),
    ]


def magic(m, mg):
    t = mg[m["k"]]
    L = ["default", "@初期設定", f"    &カード名,{t['name']}", f"    &カード画像,{P}magic_{m['no']}.png",
         "    属性設定,水属性", f"    タイプ設定,{m['type']}", f"    レアリティ設定,{m['rare']}"]
    if m.get("trap"):
        L += [f"    効果設定,1,forceTrigger,{m['explain']}", "    誘発効果設定,1,onAttack",
              "    効果条件設定,1,トリガー能動カード.所属,!=,自分所属"]
    else:
        L += [f"    効果設定,1,play,{m['explain']}"]
    if m.get("target"):
        L += ["    " + m["target"]]
    if m["no"] == 1:
        L += ["    効果設定,2,forceTrigger,自分のターン終了時：主人公の深海度+1。3回目で自壊。",
              "    誘発効果設定,2,エンドフェイズ開始時", "    効果条件設定,2,Now自分ターン,==,true"]
    L += [f"    効果設定,0,explain,{t['flavor']}", ""]
    ef = ["@効果", "switch,効果ID", "case,1", "{"] + \
        ind(["話者,自分プレイヤー", "画像,&カード画像,1", f"セリフ,{t['play']}"] + m["body"], 4) + ["}"]
    if m["no"] == 1:
        c2 = ["話者,自分プレイヤー", f"セリフ,{t['tick']}", "$回数,+=,1"] + add_player(1) + \
            block("$回数,>=,3", [f"セリフ,{t['end']}", "効果破壊,自分"])
        ef += ["case,2", "{"] + ind(c2, 4) + ["}"]
    ef += ["endswitch", ""]
    L += ef + ["@効果_街バトル", "    イベント実行,効果", ""]
    write(f"Card/{C}_magic_{m['no']}.txt", L)


def quest_files():
    q = [f"スキュラの海底神殿,Card/{C}_master,クエストイベント",
         f"スキュラの海底神殿【回想バトル】,Card/{C}_master,回想バトル,$${C}_挑戦回数,>=,1"]
    write(f"EventList/Quest/{C}.txt", q, trailing=False)
    write(f"EventList/Renoun/{C}.txt", [q[1]], trailing=False)


if __name__ == "__main__":
    master()
    for k in MONS:
        monster(k)
    mg = J("m2")["magic"]
    for m in magic_defs():
        magic(m, mg)
    quest_files()
    print("generated", OUT)
