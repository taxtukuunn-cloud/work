#!/usr/bin/env python3
"""N1 男の娘ホストクラブ（Host）v4 カード一式の生成スクリプト（2026-09-24）

v4の決まり（MOD制作_進捗とルールまとめ.md 0章・新MOD企画書v4 4〜8章）：
- 得意技だけが累積スタック「指名度」を積む。スタックは受けた側が個別に持つ
  （主人公＝相手プレイヤー.$指名度 上限12で敗北／男モンスター＝相手.$指名度 上限6で店側へ寝返り）
- セリフは受けた側のスタック段階（4段階）で変わる。主人公向け・モンスター向けの2組
- 挿入技は受けた側の $ほぐし が2未満なら「指ほぐし」に置き換わる
- 街には出さずクエスト登録（Eventlist/Quest/Host.txt）。回想バトル（敵デッキから特殊召喚・手札・ドロー）
- 敗北シナリオは @クエストイベント／@回想バトル の バトル開始 直後で流す（N12で実機確認済みの形）

入力：scen/<経路>_<責め手>.txt（敗北シナリオ28本）、lines/<m|e1|e2|e3|boss>.json（セリフ）
出力：out/N1_Host_MOD/Card/*.txt、Eventlist/Quest/Host.txt（UTF-8・CRLF）
"""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
SCEN = os.path.join(BASE, "scen")
LINES = os.path.join(BASE, "lines")
OUT = os.path.join(BASE, "out", "N1_Host_MOD")
C = "Host"
P = f"#{C}/{C}_"
S = "指名度"          # スタック名
PMAX, MMAX = 12, 6     # 上限（主人公／男モンスター）

ROUTES = [("btl", 1), ("onani", 2), ("inochi", 3), ("onedari", 4)]
ATT = [("m1", 1), ("m2", 2), ("m3", 3), ("e1", 4), ("e2", 5), ("e3", 6), ("boss", 7)]
WEAK = {"m1": "キス", "m2": "乳首責め", "m3": "本番", "e1": "乳首責め", "e2": "耳責め", "e3": "魔法責め", "boss": "本番"}
SPEAKERS = [("%レン", "master"), ("%ヒナタ", "e1"), ("%ユウ", "e2"), ("%ソラ", "e3"), ("%暁", "boss")]

L_ = {k: json.load(open(os.path.join(LINES, f"{k}.json"), encoding="utf-8")) for k in ["m", "e1", "e2", "e3", "boss"]}


def ind(lines, n=1):
    return [(" " * n) + l if l else l for l in lines]


def block(cond, body):
    return [f"if,{cond}", "{"] + ind(body) + ["}"]


def ifelse(cond, a, b):
    return [f"if,{cond}", "{"] + ind(a) + ["}else{"] + ind(b) + ["}"]


def txt(s):
    return s.replace("\n", "\\n")


# ---------------------------------------------------------------- スタック（受けた側ごと）
def target_calc():
    """@戦闘 の頭：$主（主人公なら1）・$値（受けた側のスタック）・$ほ（ほぐし）・$段階"""
    L = ["$主,=,0"] + block("相手,==,相手プレイヤー", ["$主,=,1"])
    L += ifelse("$主,==,1",
                [f"$値,=,相手プレイヤー.${S}", "$ほ,=,相手プレイヤー.$ほぐし", "$段階,=,1"]
                + block("$値,>=,4", ["$段階,=,2"]) + block("$値,>=,7", ["$段階,=,3"]) + block("$値,>=,10", ["$段階,=,4"]),
                [f"$値,=,相手.${S}", "$ほ,=,相手.$ほぐし", "$段階,=,1"]
                + block("$値,>=,2", ["$段階,=,2"]) + block("$値,>=,4", ["$段階,=,3"]) + block("$値,>=,5", ["$段階,=,4"]))
    return L


def conv_monster(obj, line):
    """男モンスターがスタック上限に達した → 店側へ寝返り"""
    return ["話者,自分", f"セリフ,{txt(line)}",
            "説明,男モンスターはうっとりとした顔のまま、専属ホスト見習いとして店側の席へ移った。",
            f"コントロール変更,{obj},自分所属"]


def add_stack(n, conv_line):
    """$主 に応じて受けた側へ n 加算し、表示と上限の判定"""
    player = [f"相手プレイヤー.${S},+=,{n}", f"$表示,=,相手プレイヤー.${S}", f"説明,（あなたの{S} {{$表示}}／{PMAX}）"] + \
        block(f"相手プレイヤー.${S},>=,{PMAX}", ["説明,指名度が満ちた。……もう、この店の客ではいられない。", "とどめダメージ,相手プレイヤー,9999"])
    mon = [f"相手.${S},+=,{n}", f"$表示,=,相手.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"] + \
        block(f"相手.${S},>=,{MMAX}", conv_monster("相手", conv_line))
    return ifelse("$主,==,1", player, mon)


def add_hogushi():
    return ifelse("$主,==,1", ["相手プレイヤー.$ほぐし,+=,1"], ["相手.$ほぐし,+=,1"])


def effect_target_add(n, conv_line):
    """効果（召喚時・魔法）からの加算：男モンスターがいればランダムに1体、いなければ主人公"""
    L = ["$主,=,1"] + block("相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", "$主,=,0"])
    player = [f"相手プレイヤー.${S},+=,{n}", f"$表示,=,相手プレイヤー.${S}", f"説明,（あなたの{S} {{$表示}}／{PMAX}）"] + \
        block(f"相手プレイヤー.${S},>=,{PMAX}", ["とどめダメージ,相手プレイヤー,9999"])
    mon = [f"%対象.${S},+=,{n}", f"$表示,=,%対象.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"] + \
        block(f"%対象.${S},>=,{MMAX}", conv_monster("%対象", conv_line))
    return L + ifelse("$主,==,1", player, mon)


def stage_lines(pairs, idx):
    """pairs=[[責め,反応]×4] の idx 番目（0=責め,1=反応）を段階で分岐"""
    out = []
    for i in range(4):
        out += block(f"$段階,==,{i+1}", [f"セリフ,{txt(pairs[i][idx])}"])
    return out


def tech_body(name, cg, t, aid, fav_n=0, finger=False, extra=None, effect="&&セクシーエフェクト", conv="", master_tech=None):
    b = ["$今回,=,1", "話者,自分", f"技名表示,{name}", f"画像,{cg},1"]
    b += ifelse("$主,==,1", stage_lines(t["player"], 0), stage_lines(t["monster"], 0))
    b += ["話者,相手"]
    b += ifelse("$主,==,1", stage_lines(t["player"], 1), stage_lines(t["monster"], 1))
    b += ["話者,自分", f"攻撃エフェクト変更,{effect}"]
    rec = [f"自分プレイヤー.$最後の責め手,=,{aid}"]
    if master_tech:
        rec += [f"$$Host_最後のマスター技,=,{master_tech}"]
    b += block("$主,==,1", rec)
    if finger:
        b += ["説明,（指でほぐされた。）"] + add_hogushi()
    if extra:
        b += extra
    if fav_n:
        b += add_stack(fav_n, conv)
    return b


def prep_body(name, pr, aid, fav_insert, conv, master_tech=None):
    """挿入技の代わりの指ほぐし"""
    b = ["$今回,=,1", "話者,自分", f"技名表示,{name}の指ほぐし"]
    pl = ifelse("$ほ,==,0", [f"セリフ,{txt(pr['player'][0][0])}"], [f"セリフ,{txt(pr['player'][1][0])}"])
    b += ifelse("$主,==,1", pl, [f"セリフ,{txt(pr['monster'][0])}"])
    b += ["話者,相手"]
    pr_r = ifelse("$ほ,==,0", [f"セリフ,{txt(pr['player'][0][1])}"], [f"セリフ,{txt(pr['player'][1][1])}"])
    b += ifelse("$主,==,1", pr_r, [f"セリフ,{txt(pr['monster'][1])}"])
    b += ["話者,自分"]
    rec = [f"自分プレイヤー.$最後の責め手,=,{aid}"]
    if master_tech:
        rec += [f"$$Host_最後のマスター技,=,{master_tech}"]
    b += block("$主,==,1", rec)
    b += add_hogushi()
    b += ifelse("$主,==,1", ["$表示,=,相手プレイヤー.$ほぐし"], ["$表示,=,相手.$ほぐし"]) + ["説明,（ほぐし {$表示}／2）"]
    if fav_insert:
        b += add_stack(1, conv)
    return b


def mirror_globals(lines):
    """最後の責め手・負け方を $$ にも記録（戦闘が終わるとカード変数は読めないため）"""
    out = []
    for l in lines:
        out.append(l)
        m = re.match(r"^(\s*)自分プレイヤー\.\$(最後の責め手|敗北経路),=,(\S+)$", l)
        if m:
            out.append(f"{m.group(1)}$${C}_{m.group(2)},=,{m.group(3)}")
    return out


_IMG = re.compile(r"^(\s*)画像,(#[^,]+),(.*)$")
_SPK = re.compile(r"^(\s*)話者生成,(%[^,]+),(#[^,]+),(.*)$")


def var_images(lines):
    """画像は @初期設定 の & 変数経由で使う（直接パスでは敗北CGが出なかった。N12で確認）"""
    defs, out = {}, []

    def var(path):
        name = "&画像_" + os.path.splitext(os.path.basename(path))[0]
        defs[name] = path
        return name
    for l in lines:
        m = _IMG.match(l)
        if m:
            sp, path, rest = m.groups()
            out.append(f"{sp}画像,{var(path)},{rest}")
            continue
        m = _SPK.match(l)
        if m:
            sp, v, path, rest = m.groups()
            out.append(f"{sp}話者生成,{v},{var(path)},{rest}")
            continue
        out.append(l)
    if defs:
        i = out.index("@初期設定") + 1
        out[i:i] = [f"    {k},{p}" for k, p in sorted(defs.items())]
    return out


def write(rel, lines, raw=False):
    if not raw:
        lines = var_images(mirror_globals(lines))
        lines = ["default"] + lines
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines) + ("" if raw else "\r\n"))


def street_hooks(sections):
    out = []
    for s in sections:
        out += [f"@{s}_街バトル", f"    イベント実行,{s}", ""]
    return out


# ---------------------------------------------------------------- 敗北シナリオ
def read_scen(route, att):
    lines = [l.rstrip("\r\n") for l in open(os.path.join(SCEN, f"{route}_{att}.txt"), encoding="utf-8-sig")]
    return [l for l in lines if l.strip() and not l.startswith("##")]


def scen_section(route, att):
    weak = WEAK[att]
    return [f"@敗北_{route}_{att}"] + ind(read_scen(route, att), 4) + [
        "    フラッシュ,白",
        "    説明,―― クラブ・ルクス　専属契約 ――",
        f"    主人公攻撃タイプ弱点付与,{weak},50", ""]


def lose_play(record):
    """バトル開始直後の敗北処理。record=True ならクエスト（$$ の記録あり）"""
    L = ["$$Host_再生済,=,1", "BGM,&&敗北BGM",
         "$経路,=,$$Host_敗北経路"] + block("$経路,==,0", ["$経路,=,1"]) + block("死亡理由,==,オナニー", ["$経路,=,2"]) + [
        "$責め手,=,$$Host_最後の責め手"] + block("$責め手,==,0", ["$責め手,=,1"]) + ["イベント実行,敗北再生"]
    if record:
        L += ["$$Host_敗北回数,+=,1", "$$Host_前回敗北経路,=,$経路", "$$Host_前回最後の責め手,=,$責め手"]
    L += ["説明,GAME OVER"]
    return L


# ---------------------------------------------------------------- マスター
def master():
    m = L_["m"]
    q = m["quest"]
    deck = ["Host_mons_e1"] * 3 + ["Host_mons_e2"] * 3 + ["Host_mons_e3"] * 3 + ["Host_mons_boss"] + \
        [f"Host_magic_{i}" for i in range(1, 6) for _ in range(2)]
    L = ["@初期設定",
         "    &カード名,NO.1ホスト　レン",
         f"    &カード画像,{P}master.png",
         "    レベル設定,8", "    攻撃力設定,1000", "    最大HP設定,10000",
         "    属性設定,闇属性", "    タイプ設定,戦士", "    性別設定,男", "    レアリティ設定,UR",
         "    攻撃エフェクト設定,&&キスエフェクト",
         f"    &技CG_1,{P}atk_m1.png", f"    &技CG_2,{P}atk_m2.png", f"    &技CG_3,{P}atk_m3.png",
         f"    &背景,{P}room.png",
         f"    効果設定,1,explain,★得意技【ディープキス】で、受けた相手の【{S}】+3（主人公は12で敗北／男モンスターは6で専属ホスト見習いとして店側へ）。{S}は主人公とモンスターが別々に持つ。【VIPルームの指名】は指で2回ほぐした後にだけ出せる（足りなければ指ほぐし）。ターン終了時、主人公の{S}の段階に応じて 魅了／メロメロ／攻撃指示不能／魔法使用不能＋500。",
         f"    効果設定,0,explain,{txt(m['flavor'])}", ""]

    # ---- クエスト
    first = ["背景,&背景", f"説明,{txt(q['first'][0][3:])}", "画像,&カード画像,1"] + [f"セリフ,{txt(s)}" for s in q["first"][1:]]
    won_before = ["画像,&カード画像,1"] + [f"セリフ,{txt(s)}" for s in q["won_before"]]
    prev = ["画像,&カード画像,1"]
    for k in "1234":
        prev += block(f"$$Host_前回敗北経路,=={','}{k}".replace("=,,", "==,"), [f"セリフ,{txt(q['prev'][k])}"])
    prev += [f"アラート,{txt(q['prev_alert'])}", "選択肢生成," + ",".join(q["choices"])]
    prev += block("選択肢,==,2", ["イベント実行,前回続き", "イベント終了"])
    prev += block("選択肢,==,3", [f"セリフ,{txt(q['decline'])}", "イベント終了"])
    qe = ["@クエストイベント", "話者,自分", "背景,&背景", "$$Host_回想中,=,0", "$$Host_挑戦回数,+=,1"]
    qe += ifelse("$$Host_敗北回数,==,0", first, ifelse("is前回プレイヤー勝利,==,true", won_before, prev))
    start = ["$$Host_最後の責め手,=,1", "$$Host_敗北経路,=,0", "$$Host_再生済,=,0", "$$Host_最後のマスター技,=,1",
             "デッキ設定," + ",".join(deck), "デッキ報酬設定,300,300,0", "バトル開始,&背景,&&戦闘BGM"]
    qe += start
    won = ["BGM,&&戦闘BGM", "画像,&カード画像,1", "話者,自分", f"セリフ,{txt(q['lost_line'])}"]
    qe += ifelse("is敗北,==,true", lose_play(True), won) + [""]
    L += qe

    # ---- 回想バトル
    ks = ["@回想バトル", "話者,自分", "背景,&背景", "画像,&カード画像,1", "$$Host_回想中,=,1"]
    ks += [f"セリフ,{txt(s)}" for s in q["kaisou"]]
    ks += ["説明,【回想バトル】相手のターンが始まるたびに、相手のデッキから好きなカードを特殊召喚させる・手札に加えさせる・ドローさせることができる。負けても記録は残らない。"]
    ks += [x for x in start if not x.startswith("デッキ報酬設定")]
    ks += ifelse("is敗北,==,true", lose_play(False), ["BGM,&&戦闘BGM", "画像,&カード画像,1", "話者,自分", f"セリフ,{txt(q['lost_line'])}"])
    ks += ["$$Host_回想中,=,0", ""]
    L += ks

    # ---- 回想メニュー
    menu = ["@回想メニュー", "$続ける,=,1", "while,$続ける,==,1", "{"]
    body = ["アラート,回想バトル：相手の手を選んでください",
            "選択肢生成,デッキからモンスターを特殊召喚させる,デッキからカードを手札に加えさせる,ドローさせる,このまま進める"]
    body += block("選択肢,==,1", ["%候補,=,自分デッキ.?isモンスター:true"] + ifelse(
        "%候補.Count,>,0", ["カード選択,%候補,1,1", "特殊召喚,選択カード,味方"], ["説明,デッキにモンスターが残っていない。"]))
    body += block("選択肢,==,2", ["%候補,=,自分デッキ"] + ifelse(
        "%候補.Count,>,0", ["カード選択,%候補,1,1", "効果サーチ,選択カード,自分所属"], ["説明,デッキにカードが残っていない。"]))
    body += block("選択肢,==,3", ["効果ドロー,自分プレイヤー"])
    body += block("選択肢,==,4", ["$続ける,=,0"])
    menu += ind(body) + ["}", ""]
    L += menu

    # ---- 試合開始・ターン開始
    L += ["@試合開始", f"相手プレイヤー.${S},=,0", "相手プレイヤー.$ほぐし,=,0",
          "自分プレイヤー.$敗北経路,=,0", "自分プレイヤー.$最後の責め手,=,1", "$$Host_再生済,=,0", "話者,自分"]
    L += [f"セリフ,{txt(s)}" for s in q["start"]]
    L += block("$$Host_回想中,==,1", ["イベント実行,回想メニュー"]) + [""]
    L += ["@ターン開始"] + block("$$Host_回想中,==,1", block("Now自分ターン,==,true", ["イベント実行,回想メニュー"])) + [""]

    # ---- 召喚宣言（主人公の段階で）
    L += ["@召喚宣言", f"$値,=,相手プレイヤー.${S}", "$段階,=,1"] + block("$値,>=,4", ["$段階,=,2"]) + \
        block("$値,>=,7", ["$段階,=,3"]) + block("$値,>=,10", ["$段階,=,4"]) + ["話者,自分"]
    summ = m["summon"]
    for i in range(4):
        L += block(f"$段階,==,{i+1}", [f"セリフ,{txt(summ[min(i, len(summ)-1)])}"])
    L += [""]

    # ---- 戦闘
    conv = m["conv"]
    t = m["techs"]
    L += ["@戦闘", "攻撃タイプランダム変更,キス,乳首責め,本番", "$今回,=,0"] + target_calc()
    L += block("攻撃タイプ,==,キス", tech_body("ディープキス", "&技CG_1", t[0], 1, fav_n=3, effect="&&キスエフェクト", conv=conv, master_tech=1))
    L += block("攻撃タイプ,==,乳首責め", tech_body("乳首と耳の囁き", "&技CG_2", t[1], 2, conv=conv, master_tech=2))
    L += block("攻撃タイプ,==,本番", ifelse("$ほ,<,2",
                                          prep_body("VIPルームの指名", m["prep"], 3, False, conv, master_tech=3),
                                          tech_body("VIPルームの指名", "&技CG_3", t[2], 3, conv=conv, master_tech=3)))
    L += block("$今回,==,0", ["話者,自分", "セリフ,ほら、こっち向いて。……逃げようとしても、もう俺の席だよ。"])
    L += [""]

    # ---- ターン終了宣言（主人公の段階で状態異常）
    te = ["@ターン終了宣言", f"$値,=,相手プレイヤー.${S}", "$段階,=,0"] + block("$値,>=,1", ["$段階,=,1"]) + \
        block("$値,>=,4", ["$段階,=,2"]) + block("$値,>=,7", ["$段階,=,3"]) + block("$値,>=,10", ["$段階,=,4"]) + ["話者,自分"]
    effs = [["状態異常付与,相手プレイヤー,魅了,1"], ["状態異常付与,相手プレイヤー,メロメロ,1"],
            ["状態異常付与,相手プレイヤー,攻撃指示不能,1"], ["状態異常付与,相手プレイヤー,魔法使用不能,1", "イベントダメージ,相手プレイヤー,500"]]
    for i in range(4):
        te += block(f"$段階,==,{i+1}", [f"セリフ,{txt(m['turn_end'][i])}"] + effs[i])
    te += block(f"$値,>=,{PMAX}", ["とどめダメージ,相手プレイヤー,9999"])
    L += te + [""]

    # ---- おねだり
    types = ["キス", "乳首責め", "本番"]
    L += ["@おねだり", "話者,自分", "画像,&カード画像,1", f"セリフ,{txt(m['onedari_intro'])}",
          "選択肢生成," + ",".join(o[0] for o in m["onedari"])]
    for i, o in enumerate(m["onedari"]):
        L += block(f"選択肢,=={','}{i+1}".replace("=,,", "==,"),
                   ["話者,相手", f"セリフ,{txt(o[1])}", "話者,自分", f"セリフ,{txt(o[2])}", f"攻撃タイプ固定,{types[i]}",
                    f"$$Host_最後のマスター技,=,{i+1}"])
    L += block("相手,==,相手プレイヤー", ["自分プレイヤー.$敗北経路,=,4"]) + ["状態異常付与,自分,弱点付与スキル,1", ""]
    L += ["@おねだり後", "攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル"] + \
        block("相手プレイヤー.HP,>,0", ["自分プレイヤー.$敗北経路,=,0"]) + [""]

    # ---- 命乞い
    ino = ["@命乞い", "話者,自分", "画像,&カード画像,1"]
    ino += ifelse("命乞い回数,>=,2", [f"セリフ,{txt(s)}" for s in m["inochi_again"]], [f"セリフ,{txt(s)}" for s in m["inochi_first"]])
    ino += ["選択肢生成,とどめを刺す,迷う"]
    ino += block("選択肢,==,1", [f"セリフ,{txt(m['inochi_fail'])}", "命乞い失敗", "イベント終了"])
    ino += ["$技,=,$$Host_最後のマスター技"] + block("$技,==,0", ["$技,=,1"]) + [
        "自分プレイヤー.$最後の責め手,=,$技", "自分プレイヤー.$敗北経路,=,3",
        "説明,とどめを刺すはずの手が、ほんの一瞬止まった。",
        f"セリフ,{txt(m['inochi_trap'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ino

    # ---- オナニー（得意技＝キスの真似。直前に受けたレンの技があればそれに合わせる）
    ona = ["@オナニー", f"画像,{P}onanie_master.png,1", "フェードイン,1",
           "$技,=,$$Host_最後のマスター技"] + block("$技,==,0", ["$技,=,1"]) + [
        "自分プレイヤー.$最後の責め手,=,$技", "自分プレイヤー.$敗北経路,=,2",
        f"説明,{txt(m['onani_desc'])}", "話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{txt(s)}" for s in m["onani_again"]], [f"セリフ,{txt(s)}" for s in m["onani_first"]])
    ona += ["話者,相手", f"セリフ,{txt(m['onani_player'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@終了時一言"] + block("自分プレイヤー.$敗北経路,==,0", ["自分プレイヤー.$敗北経路,=,1"]) + [
        "話者,自分", f"セリフ,{txt(m['end'])}", ""]

    # ---- 敗北シナリオの振り分け
    disp = ["@敗北再生", "背景,&背景", "画像,&カード画像,1", "フェードイン,1"]
    disp += [f"話者生成,{v},{P}{img}.png,男" for v, img in SPEAKERS]
    for key, aid in ATT:
        inner = []
        for r, rid in ROUTES:
            inner += block(f"$経路,=={','}{rid}".replace("=,,", "==,"), [f"イベント実行,敗北_{r}_{key}"])
        disp += block(f"$責め手,=={','}{aid}".replace("=,,", "==,"), inner)
    L += disp + [""]

    L += ["@前回続き", "$経路,=,$$Host_前回敗北経路", "$責め手,=,$$Host_前回最後の責め手"] + \
        block("$経路,==,0", ["$経路,=,1"]) + block("$責め手,==,0", ["$責め手,=,1"]) + [
        "話者,自分", f"セリフ,{txt(q['prev_continue'])}", "BGM,&&敗北BGM", "イベント実行,敗北再生",
        "$$Host_敗北回数,+=,1", "説明,GAME OVER", ""]

    for r, _ in ROUTES:
        for a, _ in ATT:
            L += scen_section(r, a)
    L += street_hooks(["試合開始", "ターン開始", "召喚宣言", "戦闘", "ターン終了宣言", "おねだり", "おねだり後", "命乞い", "オナニー", "終了時一言"])
    write("Card/Host_master.txt", L)


# ---------------------------------------------------------------- モンスター
MONS = {
    "e1": dict(name="見習いホスト　ヒナタ", aid=4, lv=3, atk=900, hp=2400, rare="R",
               techs=[("ディープキス", "キス", 0, False), ("舌での乳首責め", "乳首責め", 2, False)],
               explain=f"召喚時：男モンスター1体（いなければ主人公）の{S}+1。★得意技【舌での乳首責め】で受けた相手の{S}+2。"),
    "e2": dict(name="営業担当　ユウ", aid=5, lv=4, atk=1100, hp=2600, rare="R",
               techs=[("耳元の囁き", "耳責め", 2, False), ("乳首つまみ", "乳首責め", 0, False)],
               explain=f"★得意技【耳元の囁き】で受けた相手の{S}+2。自分のターン終了時：男モンスター1体（いなければ主人公）にメロメロ1ターン。"),
    "e3": dict(name="ボーイ　ソラ", aid=6, lv=4, atk=1200, hp=2200, rare="R",
               techs=[("貞操帯の焦らし", "魔法責め", 2, False), ("入口だけの指", "本番", 0, True)],
               explain=f"召喚時：主人公に魔法使用不能1ターン。★得意技【貞操帯の焦らし】で受けた相手の{S}+2と寸止め1ターン。【入口だけの指】で相手のほぐし+1。"),
    "boss": dict(name="オーナー　暁", aid=7, lv=7, atk=2500, hp=6000, rare="SR",
                 techs=[("指と器具のアナル開発", "魔法責め", 0, True), ("専属契約の夜", "本番", 3, False)],
                 explain=f"召喚時：男モンスター1体（いなければ主人公）の{S}+3。【指と器具のアナル開発】で相手のほぐし+1。★得意技【専属契約の夜】（指で2回ほぐした後だけ。足りなければ指ほぐし）で受けた相手の{S}+3。固有効果【専属契約】自分のターン終了時、主人公の{S}が6以上なら、男モンスター1体にメロメロ2ターンと{S}+2。"),
}


def monster(key):
    d = MONS[key]
    m = L_[key]
    img = f"{P}{key}.png"
    cg = f"{P}atk_{key}.png"
    has_end = key in ("e2", "boss")
    L = ["@初期設定", f"    &カード名,{d['name']}", f"    &カード画像,{img}",
         f"    レベル設定,{d['lv']}", f"    攻撃力設定,{d['atk']}", f"    最大HP設定,{d['hp']}",
         "    属性設定,闇属性", "    タイプ設定,戦士", "    性別設定,男", f"    レアリティ設定,{d['rare']}",
         "    攻撃エフェクト設定,&&セクシーエフェクト", f"    &技CG,{cg}",
         f"    効果設定,1,forceTrigger,{d['explain']}", "    誘発効果設定,1,場に出た時", "    効果条件設定,1,トリガー受動カード,==,自分"]
    if has_end:
        L += ["    効果設定,2,forceTrigger,自分のターン終了時の効果。", "    誘発効果設定,2,エンドフェイズ開始時",
              "    効果条件設定,2,Now自分ターン,==,true"]
    L += [f"    効果設定,0,explain,{txt(m['flavor'])}", ""]

    ef = ["@効果", "switch,効果ID", "case,1", "{", "    話者,自分", f"    画像,{img},1"] + [f"    セリフ,{txt(s)}" for s in m["summon"]]
    if key == "e1":
        ef += ind(effect_target_add(1, m["conv"]), 4)
    if key == "boss":
        ef += ind(effect_target_add(3, m["conv"]), 4)
    if key == "e3":
        ef += ["    状態異常付与,相手プレイヤー,魔法使用不能,1"]
    ef += ["}"]
    if key == "e2":
        ef += ["case,2", "{", "    話者,自分", f"    セリフ,{txt(m['turn_end'][0])}"]
        ef += ind(ifelse("相手モンスター.Count,>,0",
                         ["カードランダム抜き出し,相手モンスター,1,%対象", "状態異常付与,%対象,メロメロ,1"],
                         ["状態異常付与,相手プレイヤー,メロメロ,1"]), 4)
        ef += ["}"]
    if key == "boss":
        ef += ["case,2", "{"]
        body = block(f"相手プレイヤー.${S},>=,6", ["話者,自分", f"セリフ,{txt(m['turn_end'][0])}", "説明,【専属契約】"] + block(
            "相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", "状態異常付与,%対象,メロメロ,2", f"%対象.${S},+=,2",
                                        f"$表示,=,%対象.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"] +
            block(f"%対象.${S},>=,{MMAX}", conv_monster("%対象", m["conv"]))))
        ef += ind(body, 4) + ["}"]
    ef += ["endswitch", ""]
    L += ef

    # 戦闘
    types = [x[1] for x in d["techs"]]
    L += ["@戦闘", "攻撃タイプランダム変更," + ",".join(types), "$今回,=,0"] + target_calc()
    for i, (tn, tt, fav, finger) in enumerate(d["techs"]):
        extra = ["状態異常付与,相手,寸止め,1"] if (key == "e3" and i == 0) else None
        body = tech_body(tn, "&技CG", m["techs"][i], d["aid"], fav_n=fav, finger=finger, extra=extra,
                         effect="&&キスエフェクト" if tt == "キス" else "&&セクシーエフェクト", conv=m["conv"])
        if key == "boss" and i == 1:
            body = ifelse("$ほ,<,2", prep_body(tn, m["prep"], d["aid"], True, m["conv"]), body)
        L += block(f"攻撃タイプ,=={','}{tt}".replace("=,,", "==,"), body)
    L += block("$今回,==,0", ["話者,自分", f"セリフ,{txt(m['techs'][0]['player'][0][0])}"]) + [""]

    # おねだり
    L += ["@おねだり", "話者,自分", "画像,&カード画像,1", f"セリフ,{txt(m['onedari_intro'])}",
          "選択肢生成," + ",".join(o[0] for o in m["onedari"])]
    for i, o in enumerate(m["onedari"]):
        L += block(f"選択肢,=={','}{i+1}".replace("=,,", "==,"),
                   ["話者,相手", f"セリフ,{txt(o[1])}", "話者,自分", f"セリフ,{txt(o[2])}", f"攻撃タイプ固定,{types[i]}"])
    L += block("相手,==,相手プレイヤー", [f"自分プレイヤー.$最後の責め手,=,{d['aid']}", "自分プレイヤー.$敗北経路,=,4"]) + [
        "状態異常付与,自分,弱点付与スキル,1", ""]
    L += ["@おねだり後", "攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル"] + \
        block("相手プレイヤー.HP,>,0", ["自分プレイヤー.$敗北経路,=,0"]) + [""]

    ino = ["@命乞い", "話者,自分", "画像,&カード画像,1"]
    ino += ifelse("命乞い回数,>=,2", [f"セリフ,{txt(s)}" for s in m["inochi_again"]], [f"セリフ,{txt(s)}" for s in m["inochi_first"]])
    ino += ["選択肢生成,とどめを刺す,迷う"]
    ino += block("選択肢,==,1", [f"セリフ,{txt(m['inochi_fail'])}", "命乞い失敗", "イベント終了"])
    ino += [f"自分プレイヤー.$最後の責め手,=,{d['aid']}", "自分プレイヤー.$敗北経路,=,3",
            "説明,とどめを刺すはずの手が、ほんの一瞬止まった。", f"セリフ,{txt(m['inochi_trap'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ino

    ona = ["@オナニー", f"画像,{P}onanie_{key}.png,1", "フェードイン,1",
           f"自分プレイヤー.$最後の責め手,=,{d['aid']}", "自分プレイヤー.$敗北経路,=,2",
           f"説明,{txt(m['onani_desc'])}", "話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{txt(s)}" for s in m["onani_again"]], [f"セリフ,{txt(s)}" for s in m["onani_first"]])
    ona += ["話者,相手", f"セリフ,{txt(m['onani_player'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@終了時一言"] + block("自分プレイヤー.$敗北経路,==,0", ["自分プレイヤー.$敗北経路,=,1"]) + [
        "話者,自分", f"セリフ,{txt(m['end'])}", ""]
    L += street_hooks(["戦闘", "おねだり", "おねだり後", "命乞い", "オナニー", "終了時一言", "効果"])
    write(f"Card/Host_mons_{key}.txt", L)


# ---------------------------------------------------------------- 魔法・罠
CONV_M = "指名、入ったね。……今日から君も、うちの専属ホスト見習いだ。"
MAGIC = [
    dict(no=1, name="指名入りました", type="通常魔法", rare="R",
         explain=f"男モンスター1体（いなければ主人公）の{S}+2。",
         flavor="店内に響くマイクの声と、指名ボードに引かれる金の線。名前を呼ばれた瞬間から、もう帰り道は細くなっていく。",
         lines=["指名入りましたー！　……ほら、みんな君のこと見てる。もう逃げられないよ。"],
         body=effect_target_add(2, CONV_M)),
    dict(no=2, name="シャンパンコール", type="通常魔法", rare="R",
         explain="男モンスター1体に魅了2ターン。",
         flavor="積み上げられたグラスの塔に、金色の泡が流れ落ちていく。ホストたちの掛け声に囲まれて、断る言葉は泡と一緒に消えた。",
         target="効果ターゲット設定,1,選択,相手モンスター.?性別:男,1",
         lines=["シャンパン入りまーす！　お連れさんも一緒に飲もうよ。……ほら、目がとろんとしてきた。"],
         body=["状態異常付与,効果対象,魅了,2"]),
    dict(no=3, name="VIPルーム", type="永続魔法", rare="SR",
         explain=f"発動時と、自分のターン終了時に、男モンスター1体（いなければ主人公）の{S}+1。3回目のターン終了時に自壊する。",
         flavor="店の奥、天蓋つきのソファと大きな姿見のある個室。扉が閉まると、フロアの音楽は遠い波音のようにしか聞こえない。",
         lines=["VIPルーム、開けておいたよ。……ここなら誰にも邪魔されない。"],
         body=["$回数,=,0"] + effect_target_add(1, CONV_M)),
    dict(no=4, name="ヘルプ要請", type="通常魔法", rare="N",
         explain="自分のデッキからホスト（モンスター）1枚をランダムに手札に加える。",
         flavor="ナンバーワンの席には、いつでも手の空いたホストが飛んでくる。客が一人で帰ることのないように。",
         target="効果ターゲット設定,1,ランダム,自分デッキ.?isモンスター:true,1",
         lines=["ヘルプお願い。……君の相手、もう一人増やしてあげる。"],
         body=["効果サーチ,効果対象,自分所属"]),
    dict(no=5, name="アフターの誘い", type="通常罠", rare="R",
         explain="相手の攻撃時に発動。攻撃してきたカードにメロメロ1ターン。",
         flavor="閉店後、裏口で待っているホスト。「このあと、少しだけ付き合ってよ」――その少しが朝まで続くことを、客はまだ知らない。",
         trap=True,
         lines=["ねえ、そんな怖い顔しないで。……このあと、アフター行こうよ。二人きりで、ね。"],
         body=["状態異常付与,トリガー能動カード,メロメロ,1"]),
]


def magic(d):
    img = f"{P}magic_{d['no']}.png"
    L = ["@初期設定", f"    &カード名,{d['name']}", f"    &カード画像,{img}",
         "    属性設定,闇属性", f"    タイプ設定,{d['type']}", f"    レアリティ設定,{d['rare']}"]
    if d.get("trap"):
        L += [f"    効果設定,1,forceTrigger,{d['explain']}", "    誘発効果設定,1,onAttack",
              "    効果条件設定,1,トリガー能動カード.所属,!=,自分所属"]
    else:
        L += [f"    効果設定,1,play,{d['explain']}"]
    if d.get("target"):
        L += ["    " + d["target"]]
    if d["no"] == 3:
        L += [f"    効果設定,2,forceTrigger,自分のターン終了時：男モンスター1体（いなければ主人公）の{S}+1。3回目で自壊。",
              "    誘発効果設定,2,エンドフェイズ開始時", "    効果条件設定,2,Now自分ターン,==,true"]
    L += [f"    効果設定,0,explain,{d['flavor']}", ""]
    ef = ["@効果", "switch,効果ID", "case,1", "{", "    話者,自分プレイヤー", f"    画像,{img},1"]
    ef += [f"    セリフ,{s}" for s in d["lines"]] + ind(d["body"], 4) + ["}"]
    if d["no"] == 3:
        ef += ["case,2", "{", "    話者,自分プレイヤー", "    セリフ,VIPルームの灯りは、まだ落とさないよ。", "    $回数,+=,1"]
        ef += ind(effect_target_add(1, CONV_M), 4)
        ef += ind(block("$回数,>=,3", ["セリフ,今夜のVIPルームはここまで。……また予約、入れておくね。", "効果破壊,自分"]), 4)
        ef += ["}"]
    ef += ["endswitch", ""]
    L += ef + ["@効果_街バトル", "    イベント実行,効果", ""]
    write(f"Card/Host_magic_{d['no']}.txt", L)


def quest():
    lines = ["クラブ・ルクス（NO.1ホスト　レン）,Card/Host_master,クエストイベント",
             "クラブ・ルクス【回想バトル】,Card/Host_master,回想バトル,$$Host_挑戦回数,>=,1"]
    path = os.path.join(OUT, "Eventlist", "Quest", "Host.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines))


if __name__ == "__main__":
    master()
    for k in MONS:
        monster(k)
    for d in MAGIC:
        magic(d)
    quest()
    print("generated", OUT)
