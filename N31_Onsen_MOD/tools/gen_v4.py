#!/usr/bin/env python3
"""v4 カード一式の汎用生成スクリプト（N27 騎士団用。N4 v4 のものに固有効果の1試合1回（once）を追加。2026-09-24）

使い方：python3 gen_v4.py <MODフォルダ>
 MODフォルダに cfg.py（CFG 辞書）・scen/<経路>_<責め手>.txt（28本）・lines/<m|e1|e2|e3|boss>.json を置く。
 出力：<MODフォルダ>/out/<出力名>/Card/*.txt・Eventlist/Quest/<コード>.txt（UTF-8・CRLF）

v4の決まり（MOD制作_進捗とルールまとめ.md 0章）：
- 得意技だけが累積スタックを積む。スタックは受けた側が個別に持つ（主人公 相手プレイヤー.$<名>／男モンスター 相手.$<名>）
- セリフは受けた側のスタック段階（4段階）で変わる。主人公向け・モンスター向けの2組
- 挿入技（insert=True）は受けた側の $ほぐし が2未満なら「指ほぐし」に置き換わる
- 街には出さずクエスト登録。回想バトル（敵デッキから特殊召喚・手札・ドロー）
- 敗北シナリオは バトル開始 直後で流す（N12で実機確認済みの形）。画像は @初期設定 の変数経由
"""
import os, re, sys, json, importlib.util

MOD = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("cfg", os.path.join(MOD, "cfg.py"))
cfgmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cfgmod)
CFG = cfgmod.CFG

C = CFG["code"]
P = f"#{C}/{C}_"
S = CFG["stack"]
PMAX, MMAX = CFG.get("pmax", 12), CFG.get("mmax", 6)
OUT = os.path.join(MOD, "out", CFG["outdir"])
ROUTES = [("btl", 1), ("onani", 2), ("inochi", 3), ("onedari", 4)]
ATT = [("m1", 1), ("m2", 2), ("m3", 3), ("e1", 4), ("e2", 5), ("e3", 6), ("boss", 7)]
L_ = {k: json.load(open(os.path.join(MOD, "lines", f"{k}.json"), encoding="utf-8")) for k in ["m", "e1", "e2", "e3", "boss"]}
G = f"$${C}_"   # グローバル変数の頭
BG = CFG.get("bg", f"{P}bg.png")   # 背景（#… の画像 または &&素材）


def ind(lines, n=1):
    return [(" " * n) + l if l else l for l in lines]


def block(cond, body):
    return [f"if,{cond}", "{"] + ind(body) + ["}"]


def ifelse(cond, a, b):
    return [f"if,{cond}", "{"] + ind(a) + ["}else{"] + ind(b) + ["}"]


def txt(s):
    return s.replace("\n", "\\n")


# ---------------------------------------------------------------- スタック
def stage_from(var, player=True):
    th = CFG.get("pstage", [4, 7, 10]) if player else CFG.get("mstage", [2, 4, 5])
    return ["$段階,=,1"] + block(f"{var},>=,{th[0]}", ["$段階,=,2"]) + block(f"{var},>=,{th[1]}", ["$段階,=,3"]) + \
        block(f"{var},>=,{th[2]}", ["$段階,=,4"])


def target_calc():
    L = ["$主,=,0"] + block("相手,==,相手プレイヤー", ["$主,=,1"])
    L += ifelse("$主,==,1",
                [f"$値,=,相手プレイヤー.${S}", "$ほ,=,相手プレイヤー.$ほぐし"] + stage_from("$値", True),
                [f"$値,=,相手.${S}", "$ほ,=,相手.$ほぐし"] + stage_from("$値", False))
    return L


def conv_monster(obj, line):
    how = CFG.get("mon_fate", "conv")
    L = ["話者,自分", f"セリフ,{txt(line)}", f"説明,{CFG['conv_desc']}"]
    if how == "destroy":
        return L + [f"効果破壊,{obj}"]
    return L + [f"コントロール変更,{obj},自分所属"]


def lose_line():
    return f"説明,{CFG['player_full_desc']}"


def add_stack(n, conv_line):
    player = [f"相手プレイヤー.${S},+=,{n}", f"$表示,=,相手プレイヤー.${S}", f"説明,（あなたの{S} {{$表示}}／{PMAX}）"] + \
        block(f"相手プレイヤー.${S},>=,{PMAX}", [lose_line(), "とどめダメージ,相手プレイヤー,9999"])
    mon = [f"相手.${S},+=,{n}", f"$表示,=,相手.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"] + \
        block(f"相手.${S},>=,{MMAX}", conv_monster("相手", conv_line))
    return ifelse("$主,==,1", player, mon)


def add_hogushi():
    return ifelse("$主,==,1", ["相手プレイヤー.$ほぐし,+=,1"], ["相手.$ほぐし,+=,1"])


def pick_target():
    return ["$主,=,1"] + block("相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", "$主,=,0"])


def effect_add(n, conv_line):
    """効果からの加算：男モンスターがいればランダムに1体、いなければ主人公"""
    player = [f"相手プレイヤー.${S},+=,{n}", f"$表示,=,相手プレイヤー.${S}", f"説明,（あなたの{S} {{$表示}}／{PMAX}）"] + \
        block(f"相手プレイヤー.${S},>=,{PMAX}", ["とどめダメージ,相手プレイヤー,9999"])
    mon = [f"%対象.${S},+=,{n}", f"$表示,=,%対象.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"] + \
        block(f"%対象.${S},>=,{MMAX}", conv_monster("%対象", conv_line))
    return pick_target() + ifelse("$主,==,1", player, mon)


def ops(oplist, conv_line):
    """効果の命令リスト → スクリプト
    ("add", n) 男モンスター1体（いなければ主人公）に+n／("status_p", 名, T) 主人公に状態異常
    ("status_m", 名, T) 男モンスター1体（いなければ主人公）／("status_all_m", 名, T) 男モンスター全体
    ("status_target", 名, T) 効果対象に／("status_attacker", 名, T) 攻撃してきたカードに
    ("search",) 効果対象を手札へ／("draw", n)／("dmg_p", n)"""
    L = []
    for op in oplist:
        k = op[0]
        if k == "add":
            L += effect_add(op[1], conv_line)
        elif k == "status_p":
            L += [f"状態異常付与,相手プレイヤー,{op[1]},{op[2]}"]
        elif k == "status_m":
            L += ifelse("相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", f"状態異常付与,%対象,{op[1]},{op[2]}"],
                        [f"状態異常付与,相手プレイヤー,{op[1]},{op[2]}"])
        elif k == "m_status_add":   # 男モンスター1体だけ（いなければ何もしない）に状態異常と+n
            L += block("相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", f"状態異常付与,%対象,{op[1]},{op[2]}",
                                                  f"%対象.${S},+=,{op[3]}", f"$表示,=,%対象.${S}", f"説明,（男モンスターの{S} {{$表示}}／{MMAX}）"]
                       + block(f"%対象.${S},>=,{MMAX}", conv_monster("%対象", conv_line)))
        elif k == "status_m_only":   # 男モンスター1体だけ（いなければ何もしない）
            L += block("相手モンスター.Count,>,0", ["カードランダム抜き出し,相手モンスター,1,%対象", f"状態異常付与,%対象,{op[1]},{op[2]}"])
        elif k == "status_all_m":
            L += block("相手モンスター.Count,>,0", [f"状態異常付与,相手モンスター.?性別:男,{op[1]},{op[2]}"])
        elif k == "status_target":
            L += [f"状態異常付与,効果対象,{op[1]},{op[2]}"]
        elif k == "status_attacker":
            L += [f"状態異常付与,トリガー能動カード,{op[1]},{op[2]}"]
        elif k == "search":
            L += ["効果サーチ,効果対象,自分所属"]
        elif k == "draw":
            L += ["効果ドロー,自分プレイヤー"] * op[1]
        elif k == "dmg_p":
            L += [f"イベントダメージ,相手プレイヤー,{op[1]}"]
        else:
            raise ValueError(op)
    return L


def stage_lines(pairs, idx):
    out = []
    for i in range(4):
        out += block(f"$段階,==,{i+1}", [f"セリフ,{txt(pairs[i][idx])}"])
    return out


def tech_body(tech, t, aid, conv, cg, master_tech=None):
    """tech: dict(name, type, fav(積む量), finger, insert, extra=[命令], effect)"""
    b = ["$今回,=,1", "話者,自分", f"技名表示,{tech['name']}", f"画像,{cg},1"]
    b += ifelse("$主,==,1", stage_lines(t["player"], 0), stage_lines(t["monster"], 0))
    b += ["話者,相手"]
    b += ifelse("$主,==,1", stage_lines(t["player"], 1), stage_lines(t["monster"], 1))
    eff = tech.get("effect") or ("&&キスエフェクト" if tech["type"] == "キス" else "&&セクシーエフェクト")
    b += ["話者,自分", f"攻撃エフェクト変更,{eff}"]
    rec = [f"自分プレイヤー.$最後の責め手,=,{aid}"]
    if master_tech:
        rec += [f"{G}最後のマスター技,=,{master_tech}"]
    b += block("$主,==,1", rec)
    if tech.get("finger"):
        b += ["説明,（指でほぐされた。）"] + add_hogushi()
    for st in tech.get("statuses", []):
        b += [f"状態異常付与,相手,{st[0]},{st[1]}"]
    if tech.get("fav"):
        b += add_stack(tech["fav"], conv)
    return b


def prep_body(tech, pr, aid, conv, master_tech=None):
    b = ["$今回,=,1", "話者,自分", f"技名表示,{tech['name']}の指ほぐし"]
    pl = ifelse("$ほ,==,0", [f"セリフ,{txt(pr['player'][0][0])}"], [f"セリフ,{txt(pr['player'][1][0])}"])
    b += ifelse("$主,==,1", pl, [f"セリフ,{txt(pr['monster'][0])}"])
    b += ["話者,相手"]
    pr_r = ifelse("$ほ,==,0", [f"セリフ,{txt(pr['player'][0][1])}"], [f"セリフ,{txt(pr['player'][1][1])}"])
    b += ifelse("$主,==,1", pr_r, [f"セリフ,{txt(pr['monster'][1])}"])
    b += ["話者,自分"]
    rec = [f"自分プレイヤー.$最後の責め手,=,{aid}"]
    if master_tech:
        rec += [f"{G}最後のマスター技,=,{master_tech}"]
    b += block("$主,==,1", rec)
    b += add_hogushi()
    b += ifelse("$主,==,1", ["$表示,=,相手プレイヤー.$ほぐし"], ["$表示,=,相手.$ほぐし"]) + ["説明,（ほぐし {$表示}／2）"]
    if tech.get("fav"):
        b += add_stack(1, conv)
    return b


def battle(techs, lines, aid, conv, cgs, master=False):
    L = ["@戦闘", "攻撃タイプランダム変更," + ",".join(t["type"] for t in techs), "$今回,=,0"] + target_calc()
    for i, tech in enumerate(techs):
        mt = (i + 1) if master else None
        a = aid[i] if isinstance(aid, list) else aid
        body = tech_body(tech, lines["techs"][i], a, conv, cgs[i], mt)
        if tech.get("insert"):
            body = ifelse("$ほ,<,2", prep_body(tech, lines["prep"], a, conv, mt), body)
        L += block(f"攻撃タイプ,==,{tech['type']}", body)
    L += block("$今回,==,0", ["話者,自分", f"セリフ,{txt(lines['techs'][0]['player'][0][0])}"])
    return L + [""]


def mirror_globals(lines):
    out = []
    for l in lines:
        out.append(l)
        m = re.match(r"^(\s*)自分プレイヤー\.\$(最後の責め手|敗北経路),=,(\S+)$", l)
        if m:
            out.append(f"{m.group(1)}{G}{m.group(2)},=,{m.group(3)}")
    return out


_IMG = re.compile(r"^(\s*)画像,(#[^,]+),(.*)$")
_SPK = re.compile(r"^(\s*)話者生成,(%[^,]+),(#[^,]+),(.*)$")


def var_images(lines):
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


def write(rel, lines):
    lines = ["default"] + var_images(mirror_globals(lines))
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines) + "\r\n")


def hooks(sections):
    out = []
    for s in sections:
        out += [f"@{s}_街バトル", f"    イベント実行,{s}", ""]
    return out


def read_scen(route, att):
    lines = [l.rstrip("\r\n") for l in open(os.path.join(MOD, "scen", f"{route}_{att}.txt"), encoding="utf-8-sig")]
    return [l for l in lines if l.strip() and not l.startswith("##") and l not in ("#導入", "#プレイ", "#結び")]


def scen_section(route, att):
    return [f"@敗北_{route}_{att}"] + ind(read_scen(route, att), 4) + [
        "    フラッシュ,白", f"    説明,{CFG['lose_title']}",
        f"    主人公攻撃タイプ弱点付与,{CFG['weak'][att]},50", ""]


def lose_play(record):
    L = [f"{G}再生済,=,1", "BGM,&&敗北BGM", f"$経路,=,{G}敗北経路"] + block("$経路,==,0", ["$経路,=,1"]) + \
        block("死亡理由,==,オナニー", ["$経路,=,1"]) + [f"$責め手,=,{G}最後の責め手"] + block("$責め手,==,0", ["$責め手,=,1"]) + \
        ["イベント実行,敗北再生"]
    if record:
        L += [f"{G}敗北回数,+=,1", f"{G}前回敗北経路,=,$経路", f"{G}前回最後の責め手,=,$責め手"]
    return L + ["説明,GAME OVER"]


def bg_line():
    return "背景,&背景"


# ---------------------------------------------------------------- マスター
def master():
    m = L_["m"]
    q = m["quest"]
    M = CFG["master"]
    deck = [f"{C}_mons_e1"] * 3 + [f"{C}_mons_e2"] * 3 + [f"{C}_mons_e3"] * 3 + [f"{C}_mons_boss"] + \
        [f"{C}_magic_{i}" for i in range(1, 6) for _ in range(2)]
    L = ["@初期設定", f"    &カード名,{M['name']}", f"    &カード画像,{P}master.png",
         "    レベル設定,8", f"    攻撃力設定,{M.get('atk', 500)}", "    最大HP設定,10000",
         f"    属性設定,{CFG.get('attr', '闇属性')}", f"    タイプ設定,{M.get('race', '戦士')}", f"    性別設定,{M.get('sex', CFG['sex'])}", "    レアリティ設定,UR",
         f"    攻撃エフェクト設定,{M.get('effect', '&&セクシーエフェクト')}",
         f"    &技CG_1,{P}atk_m1.png", f"    &技CG_2,{P}atk_m2.png", f"    &技CG_3,{P}atk_m3.png",
         f"    &背景,{BG}",
         f"    効果設定,1,explain,{M['explain']}", f"    効果設定,0,explain,{txt(m['flavor'])}", ""]

    first = [bg_line(), f"説明,{txt(q['first'][0][3:])}", "画像,&カード画像,1"] + [f"セリフ,{txt(s)}" for s in q["first"][1:]]
    won_before = ["画像,&カード画像,1"] + [f"セリフ,{txt(s)}" for s in q["won_before"]]
    prev = ["画像,&カード画像,1"]
    for k in "1234":
        prev += block(f"{G}前回敗北経路,==,{k}", [f"セリフ,{txt(q['prev'][k])}"])
    prev += [f"アラート,{txt(q['prev_alert'])}", "選択肢生成," + ",".join(q["choices"])]
    prev += block("選択肢,==,2", ["イベント実行,前回続き", "イベント終了"])
    prev += block("選択肢,==,3", [f"セリフ,{txt(q['decline'])}", "イベント終了"])
    qe = ["@クエストイベント", "話者,自分", bg_line(), f"{G}回想中,=,0", f"{G}挑戦回数,+=,1"]
    qe += ifelse(f"{G}敗北回数,==,0", first, ifelse("is前回プレイヤー勝利,==,true", won_before, prev))
    start = [f"{G}最後の責め手,=,1", f"{G}敗北経路,=,0", f"{G}再生済,=,0", f"{G}最後のマスター技,=,1",
             "デッキ設定," + ",".join(deck)]
    reward = [f"デッキ報酬設定,{CFG.get('reward', '300,300,0')}"]
    bstart = [f"バトル開始,&背景,&&戦闘BGM"]
    qe += start + reward + bstart
    won = ["BGM,&&戦闘BGM", "画像,&カード画像,1", "話者,自分", f"セリフ,{txt(q['lost_line'])}"]
    qe += ifelse("is敗北,==,true", lose_play(True), won) + [""]
    L += qe

    ks = ["@回想バトル", "話者,自分", bg_line(), "画像,&カード画像,1", f"{G}回想中,=,1"]
    ks += [f"セリフ,{txt(s)}" for s in q["kaisou"]]
    ks += ["説明,【回想バトル】主人公の手札に「回想の栞」が配られる。自分のターンに場に出すと、相手のデッキから好きなカードを選んで特殊召喚させたり、ドローさせたりできる。負けても記録は残らない。"]
    ks += start + bstart
    ks += ifelse("is敗北,==,true", lose_play(False), won)
    ks += [f"{G}回想中,=,0", ""]
    L += ks

    menu = ["@回想メニュー", "$続ける,=,1", "while,$続ける,==,1", "{"]
    body = ["アラート,回想バトル：相手の手を選んでください",
            "選択肢生成,デッキからモンスターを特殊召喚させる,デッキからカードを手札に加えさせる,ドローさせる,このまま進める"]
    body += block("選択肢,==,1", ["%候補,=,自分デッキ.?isモンスター:true"] + ifelse(
        "%候補.Count,>,0", ["カード選択,%候補,1,1", "特殊召喚,選択カード,味方"], ["説明,デッキにモンスターが残っていない。"]))
    body += block("選択肢,==,2", ["%候補,=,自分デッキ"] + ifelse(
        "%候補.Count,>,0", ["カード選択,%候補,1,1", "効果サーチ,選択カード,自分所属"], ["説明,デッキにカードが残っていない。"]))
    body += block("選択肢,==,3", ["効果ドロー,自分プレイヤー"])
    body += block("選択肢,==,4", ["$続ける,=,0"])
    L += menu + ind(body) + ["}", ""]

    L += ["@試合開始", f"相手プレイヤー.${S},=,0", "相手プレイヤー.$ほぐし,=,0", "自分プレイヤー.$固有発動,=,0",
          "自分プレイヤー.$敗北経路,=,0", "自分プレイヤー.$最後の責め手,=,1", f"{G}再生済,=,0", "話者,自分"]
    L += [f"セリフ,{txt(s)}" for s in q["start"]]
    L += block(f"{G}回想中,==,1", ["イベント実行,回想メニュー"]) + [""]
    L += ["@ターン開始"] + block(f"{G}回想中,==,1", block("Now自分ターン,==,true", ["イベント実行,回想メニュー"])) + [""]

    L += ["@召喚宣言", f"$値,=,相手プレイヤー.${S}"] + stage_from("$値", True) + ["話者,自分"]
    summ = m["summon"]
    for i in range(4):
        L += block(f"$段階,==,{i+1}", [f"セリフ,{txt(summ[min(i, len(summ)-1)])}"])
    L += [""]

    L += battle(M["techs"], m, [1, 2, 3], m["conv"], ["&技CG_1", "&技CG_2", "&技CG_3"], master=True)
    te = ["@ターン終了宣言", f"$値,=,相手プレイヤー.${S}", "$段階,=,0"] + block("$値,>=,1", ["$段階,=,1"])
    th = CFG.get("pstage", [4, 7, 10])
    te += block(f"$値,>=,{th[0]}", ["$段階,=,2"]) + block(f"$値,>=,{th[1]}", ["$段階,=,3"]) + block(f"$値,>=,{th[2]}", ["$段階,=,4"]) + ["話者,自分"]
    for i in range(4):
        te += block(f"$段階,==,{i+1}", [f"セリフ,{txt(m['turn_end'][i])}"] + ops(M["turn_end_ops"][i], m["conv"]))
    te += block(f"$値,>=,{PMAX}", ["とどめダメージ,相手プレイヤー,9999"])
    L += te + [""]

    types = [t["type"] for t in M["techs"]]
    L += ["@おねだり", "話者,自分", "画像,&カード画像,1", f"セリフ,{txt(m['onedari_intro'])}",
          "選択肢生成," + ",".join(o[0] for o in m["onedari"])]
    for i, o in enumerate(m["onedari"]):
        L += block(f"選択肢,==,{i+1}", ["話者,相手", f"セリフ,{txt(o[1])}", "話者,自分", f"セリフ,{txt(o[2])}",
                                    f"攻撃タイプ固定,{types[i]}", f"{G}最後のマスター技,=,{i+1}"])
    L += block("相手,==,相手プレイヤー", ["自分プレイヤー.$敗北経路,=,4"]) + ["状態異常付与,自分,弱点付与スキル,1", ""]
    L += ["@おねだり後", "攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル"] + \
        block("相手プレイヤー.HP,>,0", ["自分プレイヤー.$敗北経路,=,0"]) + [""]

    ino = ["@命乞い", "話者,自分", "画像,&カード画像,1"]
    ino += ifelse("命乞い回数,>=,2", [f"セリフ,{txt(s)}" for s in m["inochi_again"]], [f"セリフ,{txt(s)}" for s in m["inochi_first"]])
    ino += ["選択肢生成,とどめを刺す,迷う"]
    ino += block("選択肢,==,1", [f"セリフ,{txt(m['inochi_fail'])}", "命乞い失敗", "イベント終了"])
    ino += [f"$技,=,{G}最後のマスター技"] + block("$技,==,0", ["$技,=,1"]) + [
        "自分プレイヤー.$最後の責め手,=,$技", "自分プレイヤー.$敗北経路,=,3",
        "説明,とどめを刺すはずの手が、ほんの一瞬止まった。", f"セリフ,{txt(m['inochi_trap'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ino

    ona = ["@オナニー", f"$技,=,{G}最後のマスター技"] + \
        block("$技,==,0", ["$技,=,1"]) + ["自分プレイヤー.$最後の責め手,=,$技", "自分プレイヤー.$敗北経路,=,1",
                                           f"説明,{txt(m['onani_desc'])}", "話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{txt(s)}" for s in m["onani_again"]], [f"セリフ,{txt(s)}" for s in m["onani_first"]])
    ona += ["話者,相手", f"セリフ,{txt(m['onani_player'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@終了時一言"] + block("自分プレイヤー.$敗北経路,==,0", ["自分プレイヤー.$敗北経路,=,1"]) + [
        "話者,自分", f"セリフ,{txt(m['end'])}", ""]

    disp = ["@敗北再生", bg_line(), "画像,&カード画像,1", "フェードイン,1"]
    disp += [f"話者生成,{sp[0]},{P}{sp[1]}.png,{sp[2] if len(sp) > 2 else CFG['speaker_sex']}" for sp in CFG["speakers"]]
    for key, aid in ATT:
        inner = []
        for r, rid in ROUTES:
            inner += block(f"$経路,==,{rid}", [f"イベント実行,敗北_{r}_{key}"])
        disp += block(f"$責め手,==,{aid}", inner)
    L += disp + [""]

    L += ["@前回続き", f"$経路,=,{G}前回敗北経路", f"$責め手,=,{G}前回最後の責め手"] + \
        block("$経路,==,0", ["$経路,=,1"]) + block("$責め手,==,0", ["$責め手,=,1"]) + [
        "話者,自分", f"セリフ,{txt(q['prev_continue'])}", "BGM,&&敗北BGM", "イベント実行,敗北再生",
        f"{G}敗北回数,+=,1", "説明,GAME OVER", ""]

    for r, _ in ROUTES:
        for a, _ in ATT:
            L += scen_section(r, a)
    L += hooks(["試合開始", "ターン開始", "召喚宣言", "戦闘", "ターン終了宣言", "おねだり", "おねだり後", "命乞い", "オナニー", "終了時一言"])
    write(f"Card/{C}_master.txt", L)


# ---------------------------------------------------------------- モンスター
def monster(key):
    d = CFG["mons"][key]
    m = L_[key]
    img = f"{P}{key}.png"
    has_end = bool(d.get("end_ops") or d.get("unique"))
    L = ["@初期設定", f"    &カード名,{d['name']}", f"    &カード画像,{img}",
         f"    レベル設定,{d['lv']}", f"    攻撃力設定,{d['atk']}", f"    最大HP設定,{d['hp']}",
         f"    属性設定,{CFG.get('attr', '闇属性')}", f"    タイプ設定,{d.get('race', '戦士')}", f"    性別設定,{d.get('sex', CFG['sex'])}", f"    レアリティ設定,{d['rare']}",
         "    攻撃エフェクト設定,&&セクシーエフェクト", f"    &技CG,{P}atk_{key}.png",
         f"    効果設定,1,forceTrigger,{d['explain']}", "    誘発効果設定,1,場に出た時", "    効果条件設定,1,トリガー受動カード,==,自分"]
    if has_end:
        L += ["    効果設定,2,forceTrigger,自分のターン終了時の効果。", "    誘発効果設定,2,エンドフェイズ開始時",
              "    効果条件設定,2,Now自分ターン,==,true"]
    L += [f"    効果設定,0,explain,{txt(m['flavor'])}", ""]

    ef = ["@効果", "switch,効果ID", "case,1", "{", "    話者,自分", f"    画像,{img},1"] + [f"    セリフ,{txt(s)}" for s in m["summon"]]
    ef += ind(ops(d.get("summon_ops", []), m["conv"]), 4) + ["}"]
    if has_end:
        ef += ["case,2", "{"]
        body = []
        if d.get("end_ops"):
            body += ["話者,自分", f"セリフ,{txt(m['turn_end'][0])}"] + ops(d["end_ops"], m["conv"])
        if d.get("unique"):
            u = d["unique"]
            inner = ["話者,自分", f"セリフ,{txt(m['turn_end'][-1])}", f"説明,【{u['name']}】"] + ops(u["ops"], m["conv"])
            if u.get("once"):
                inner = block("自分プレイヤー.$固有発動,==,0", ["自分プレイヤー.$固有発動,=,1"] + inner)
            body += block(f"相手プレイヤー.${S},>=,{u['min']}", inner)
        ef += ind(body, 4) + ["}"]
    ef += ["endswitch", ""]
    L += ef

    L += battle(d["techs"], m, d["aid"], m["conv"], ["&技CG"] * len(d["techs"]))

    types = [t["type"] for t in d["techs"]]
    L += ["@おねだり", "話者,自分", "画像,&カード画像,1", f"セリフ,{txt(m['onedari_intro'])}",
          "選択肢生成," + ",".join(o[0] for o in m["onedari"])]
    for i, o in enumerate(m["onedari"]):
        L += block(f"選択肢,==,{i+1}", ["話者,相手", f"セリフ,{txt(o[1])}", "話者,自分", f"セリフ,{txt(o[2])}", f"攻撃タイプ固定,{types[i]}"])
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

    ona = ["@オナニー", f"自分プレイヤー.$最後の責め手,=,{d['aid']}", "自分プレイヤー.$敗北経路,=,1", f"説明,{txt(m['onani_desc'])}", "話者,自分"]
    ona += ifelse("オナニー回数,>=,2", [f"セリフ,{txt(s)}" for s in m["onani_again"]], [f"セリフ,{txt(s)}" for s in m["onani_first"]])
    ona += ["話者,相手", f"セリフ,{txt(m['onani_player'])}", "とどめダメージ,相手プレイヤー,9999", ""]
    L += ona

    L += ["@終了時一言"] + block("自分プレイヤー.$敗北経路,==,0", ["自分プレイヤー.$敗北経路,=,1"]) + [
        "話者,自分", f"セリフ,{txt(m['end'])}", ""]
    L += hooks(["戦闘", "おねだり", "おねだり後", "命乞い", "オナニー", "終了時一言", "効果"])
    write(f"Card/{C}_mons_{key}.txt", L)


# ---------------------------------------------------------------- 魔法・罠
def magic(d):
    img = f"{P}magic_{d['no']}.png"
    conv = CFG["magic_conv"]
    L = ["@初期設定", f"    &カード名,{d['name']}", f"    &カード画像,{img}",
         f"    属性設定,{CFG.get('attr', '闇属性')}", f"    タイプ設定,{d['type']}", f"    レアリティ設定,{d['rare']}"]
    if d["type"].endswith("罠"):
        L += [f"    効果設定,1,forceTrigger,{d['explain']}", "    誘発効果設定,1,onAttack",
              "    効果条件設定,1,トリガー能動カード.所属,!=,自分所属"]
    else:
        L += [f"    効果設定,1,play,{d['explain']}"]
    if d.get("target"):
        L += ["    " + d["target"]]
    if d.get("persist_ops"):
        L += [f"    効果設定,2,forceTrigger,{d['persist_explain']}",
              "    誘発効果設定,2,エンドフェイズ開始時", "    効果条件設定,2,Now自分ターン,==,true"]
    L += [f"    効果設定,0,explain,{d['flavor']}", ""]
    ef = ["@効果", "switch,効果ID", "case,1", "{", "    話者,自分プレイヤー", f"    画像,{img},1"]
    body = (["$回数,=,0"] if d.get("persist_ops") else []) + ops(d["ops"], conv)
    ef += [f"    セリフ,{txt(s)}" for s in d["lines"]] + ind(body, 4) + ["}"]
    if d.get("persist_ops"):
        ef += ["case,2", "{", "    話者,自分プレイヤー", f"    セリフ,{txt(d['persist_line'])}", "    $回数,+=,1"]
        ef += ind(ops(d["persist_ops"], conv), 4)
        ef += ind(block("$回数,>=,3", [f"セリフ,{txt(d['end_line'])}", "効果破壊,自分"]), 4) + ["}"]
    ef += ["endswitch", ""]
    L += ef + ["@効果_街バトル", "    イベント実行,効果", ""]
    write(f"Card/{C}_magic_{d['no']}.txt", L)


def quest():
    lines = [f"{CFG['quest_name']},Card/{C}_master,クエストイベント",
             f"{CFG['quest_name_kaisou']},Card/{C}_master,回想バトル,{G}挑戦回数,>=,1"]
    path = os.path.join(OUT, "Eventlist", "Quest", f"{C}.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines))


if __name__ == "__main__":
    import shutil
    shutil.rmtree(OUT, ignore_errors=True)
    master()
    for k in ["e1", "e2", "e3", "boss"]:
        monster(k)
    for d in CFG["magic"]:
        magic(d)
    quest()
    print("generated", OUT)
