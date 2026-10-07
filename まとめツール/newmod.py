# -*- coding: utf-8 -*-
"""新しいMODの骨組み（cfg.py・brief.md）を、入力画面の内容から作る。
決まりは kit の SETUP_TASK.md（N106〜）と同じ：強さ master＞boss＞e1＞e2＞e3、累積スタックは主人公用と男モンスター用の2つ、
攻撃タイプは1キャラ2種以上、得意技は1キャラ1つ、挿入は指ほぐしの後、登場人物は全員20歳以上。"""
import re

TYPES = ["本番", "キス", "手コキ", "乳首責め", "ハグ", "耳責め", "ぱふぱふ", "足コキ", "ふとももコキ", "魔法責め", "おっぱい", "息",
         "膝コキ", "パイズリ", "尻コキ", "触手", "スマタ"]
STATUSES = ["", "発情", "発情強", "魅了", "メロメロ", "見惚れ", "拘束", "寸止め", "攻撃指示不能", "洗脳", "麻痺"]
ATTRS = ["闇属性", "光属性", "地属性", "水属性", "火属性", "風属性"]
RACES = ["ローグ", "戦士", "獣"]
GENDERS = ["女", "ふたなり", "ニューハーフ", "男の娘"]
CKEYS = ["master", "e1", "e2", "e3", "boss"]
CLABEL = {"master": "マスター", "e1": "下級1（e1）", "e2": "下級2（e2）", "e3": "下級3（e3）", "boss": "上級（boss）"}
STATS = {"e1": (4, 4, 550, 1600, "R"), "e2": (5, 4, 500, 1500, "R"), "e3": (6, 4, 450, 1400, "R"), "boss": (7, 7, 1200, 6000, "SR")}
BAD_CH = set("$%&#{}<>;")
SWAP = {",": "、", "!": "！", "?": "？", "(": "（", ")": "）"}
BAD_WORDS = ["小柄", "華奢", "すっぽり", "ボウヤ", "坊や", "少年", "少女", "いい子", "赤ちゃん", "幼", "♪", "♡"]


def clean(s):
    s = (s or "").strip().replace("\r", "")
    for a, b in SWAP.items():
        s = s.replace(a, b)
    return s


def walk_text(b):
    for k in ("title", "stack", "mstack", "world", "stack_desc", "lose_title", "player_full_desc", "conv_desc", "magic_conv"):
        yield k, b.get(k, "")
    for ck in CKEYS:
        c = (b.get("chars") or {}).get(ck) or {}
        for k in ("title", "name", "look", "persona", "first", "call", "tone"):
            yield "%s の %s" % (CLABEL[ck], k), c.get(k, "")
        for i, t in enumerate(c.get("techs") or []):
            yield "%s の技%d の名前" % (CLABEL[ck], i + 1), t.get("name", "")
            yield "%s の技%d の内容" % (CLABEL[ck], i + 1), t.get("desc", "")
    for k, v in (b.get("magic") or {}).items():
        if k in ("add", "search", "trap", "target", "persist"):
            yield "魔法・罠（%s）" % k, v


def validate(b, used_codes):
    e = []
    try:
        n = int(b.get("n"))
        if n < 1:
            raise ValueError
    except Exception:
        e.append("番号は1以上の数字で入れてください")
    code = b.get("code") or ""
    if not re.match(r"^[A-Z][A-Za-z0-9]{2,15}$", code):
        e.append("コードは英字で始まる英数字3〜16文字（先頭は大文字）にしてください")
    elif code in used_codes:
        e.append("コード %s はもう使われています（カード名・画像フォルダが重なります）" % code)
    for k, lab in (("title", "MOD名"), ("stack", "主人公の累積スタック名"), ("mstack", "男モンスターの累積スタック名")):
        if not clean(b.get(k)):
            e.append("%s を入れてください" % lab)
    if clean(b.get("stack")) and clean(b.get("stack")) == clean(b.get("mstack")):
        e.append("累積スタックは主人公用と男モンスター用で別の名前にしてください")
    if b.get("attr") not in ATTRS:
        e.append("属性を選んでください")
    names = set()
    for ck in CKEYS:
        c = (b.get("chars") or {}).get(ck) or {}
        lab = CLABEL[ck]
        if not clean(c.get("name")):
            e.append("%s：名前を入れてください" % lab)
        if clean(c.get("name")) in names:
            e.append("%s：ほかのキャラと同じ名前です" % lab)
        names.add(clean(c.get("name")))
        try:
            if int(c.get("age")) < 20:
                e.append("%s：年齢は20歳以上にしてください（登場人物は全員20歳以上）" % lab)
        except Exception:
            e.append("%s：年齢を数字で入れてください（20歳以上）" % lab)
        for k, jl in (("height", "身長"), ("b", "バスト"), ("w", "ウエスト"), ("h", "ヒップ")):
            try:
                if not 40 <= int(c.get(k)) <= 260:
                    raise ValueError
            except Exception:
                e.append("%s：%s を数字で入れてください" % (lab, jl))
        if c.get("gender") not in GENDERS:
            e.append("%s：性別を選んでください" % lab)
        if c.get("race") not in RACES:
            e.append("%s：タイプを選んでください" % lab)
        if not clean(c.get("first")):
            e.append("%s：一人称を入れてください" % lab)
        techs = c.get("techs") or []
        want = 3 if ck == "master" else 2
        if len(techs) != want:
            e.append("%s：技は%dつです" % (lab, want))
            continue
        tt = [t.get("type") for t in techs]
        if any(t not in TYPES for t in tt):
            e.append("%s：攻撃タイプを選んでください" % lab)
        elif len(set(tt)) != len(tt):
            e.append("%s：同じカードの中で同じ攻撃タイプは使えません（2種以上・重複なし）" % lab)
        if len([t for t in techs if t.get("fav")]) != 1:
            e.append("%s：得意技（★）を1つだけ選んでください" % lab)
        for i, t in enumerate(techs):
            if not clean(t.get("name")) or not clean(t.get("desc")):
                e.append("%s：技%d の名前と内容を入れてください" % (lab, i + 1))
            if t.get("st") and t["st"] not in STATUSES:
                e.append("%s：技%d の状態異常が一覧にありません" % (lab, i + 1))
    mg = b.get("magic") or {}
    for k, jl in (("add", "累積を足す魔法"), ("search", "手札に加える魔法"), ("trap", "罠"), ("target", "状態異常の魔法"), ("persist", "永続魔法")):
        if not clean(mg.get(k)):
            e.append("魔法・罠：%s の名前を入れてください" % jl)
    for lab, s in walk_text(b):
        s = s or ""
        bad = sorted(set(s) & BAD_CH)
        if bad:
            e.append("「%s」に使えない半角記号があります: %s" % (lab, " ".join(bad)))
        for w in BAD_WORDS:
            if w in s:
                e.append("「%s」に使わない言葉があります: %s" % (lab, w))
    return e


def card_sex(c):
    return "女" if c.get("gender") == "女" else "その他"


def fullname(c):
    t, n = clean(c.get("title")), clean(c.get("name"))
    return (t + "　" + n) if t else n


def tech_src(t, fav_n):
    a = ["%r" % clean(t["name"]), "%r" % t["type"]]
    if t.get("fav"):
        a.append("fav=%d" % fav_n)
    if t.get("insert"):
        a.append("insert=True")
    if t.get("finger"):
        a.append("finger=True")
    if t.get("st"):
        a.append("st=(%r, %d)" % (t["st"], int(t.get("turns") or 1)))
    return "T(%s)" % ", ".join(a)


def tech_explain(t, fav_n, S, MS, end="。"):
    nm, ds = clean(t["name"]), clean(t["desc"])
    if t.get("fav"):
        s = "★得意技【%s】（%s%s）で受けた相手に+%d（主人公は%s、男モンスターは%s）" % (nm, ds, "。ほぐし+1" if t.get("finger") else "", fav_n, S, MS)
        if t.get("insert"):
            s += "。挿入技のため指で2回ほぐした後にだけ出せる（足りなければ指ほぐしになり、その間は+1）"
    else:
        s = "【%s】は%s" % (nm, ds)
        if t.get("finger"):
            s += "（ほぐし+1）"
        if t.get("insert"):
            s += "。指で2回ほぐした後にだけ出せる（足りなければ指ほぐしになる）"
    if t.get("st"):
        s += "、%s%dターン" % (t["st"], int(t.get("turns") or 1))
    return s + end


def defaults(b):
    S, MS, title = clean(b["stack"]), clean(b["mstack"]), clean(b["title"])
    m = b["chars"]["master"]
    fate = "破壊される" if b.get("fate") == "destroy" else "相手の側へ寝返る"
    d = dict(
        lose_title="―― %s　%sの虜 ――" % (title, clean(m["name"])),
        player_full_desc="%sが十二に届いた。もう数え直すことはできない。僕は%sのものになった。" % (S, clean(m["name"])),
        conv_desc="男モンスターの%sが六に届いた。彼は%s。" % (MS, "力を失って場を離れた" if b.get("fate") == "destroy" else "相手の側へ連れて行かれた"),
        magic_conv="六つ目。\nこの子も、もうこちらのものね。",
    )
    for k in d:
        if clean(b.get(k)):
            d[k] = clean(b[k])
    d["fate_word"] = fate
    return d


def make_cfg(b):
    S, MS, code, n = clean(b["stack"]), clean(b["mstack"]), b["code"], int(b["n"])
    C, D = b["chars"], defaults(b)
    title = clean(b["title"])
    m = C["master"]
    both = "男モンスター1体の%s（いなければ主人公の%s）" % (MS, S)
    L = []
    w = L.append
    w("# N%d %s（%s）の設定（gen_v4.py 用）。登場人物は全員20歳以上。" % (n, title, code))
    w("# まとめツールの入力画面から作成。カード効果は N106〜 の共通の型（e1＝召喚時+1とターン終了時の攻撃指示不能／e2＝召喚時に男モンスターへ拘束／")
    w("# e3＝召喚時に主人公へ発情／boss＝召喚時+3と固有効果／魔法罠＝+2・サーチ・罠・状態異常・永続）。変えたい時はこのファイルを直す。")
    w("import os, sys")
    w("sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'kit', 'common'))")
    w("from cfgkit import T, std_magic")
    w("")
    w("S = %r       # 主人公の累積スタック（12で敗北）" % S)
    w("MS = %r      # 男モンスターの累積スタック（6で%s）" % (MS, D["fate_word"]))
    w('BOTH = f"男モンスター1体の{MS}（いなければ主人公の{S}）"')
    w("")
    w("CFG = dict(")
    w("    code=%r, outdir=%r, stack=S, mstack=MS, sex=%r, speaker_sex=\"女\", attr=%r," % (code, "N%d_%s_MOD" % (n, code), card_sex(m), b["attr"]))
    if b.get("fate") == "destroy":
        w('    mon_fate="destroy",')
    w("    bg=%r," % ("#%s/%s_bg.png" % (code, code)))
    w("    quest_name=%r, quest_name_kaisou=%r," % ("%s（%s）" % (title, fullname(m)), "%s【回想バトル】" % title))
    w("    lose_title=%r," % D["lose_title"])
    w("    player_full_desc=%r," % D["player_full_desc"])
    w("    conv_desc=%r," % D["conv_desc"])
    w("    magic_conv=%r," % D["magic_conv"])
    w("    speakers=[%s]," % ", ".join('(%r, %r, "女")' % ("%" + clean(C[k]["name"]), k) for k in CKEYS))
    weak = {"m%d" % (i + 1): t["type"] for i, t in enumerate(m["techs"])}
    for k in ("e1", "e2", "e3", "boss"):
        weak[k] = [t for t in C[k]["techs"] if t.get("fav")][0]["type"]
    w("    weak=%r," % weak)
    ex = "".join(tech_explain(t, 3, S, MS) for t in sorted(m["techs"], key=lambda t: not t.get("fav")))
    ex += "主人公は【%s】が12で敗北。男モンスターは【%s】が6で%s。主人公と男モンスターは別々に数える。ターン終了時、主人公の%sの段階に応じて 魅了／魅了／洗脳／洗脳＋500。" % (S, MS, D["fate_word"], S)
    w("    master=dict(")
    w("        name=%r, race=%r, sex=%r, atk=500," % (fullname(m), m["race"], card_sex(m)))
    w("        explain=%r," % ex)
    w("        techs=[%s]," % ",\n               ".join(tech_src(t, 3) for t in m["techs"]))
    w('        turn_end_ops=[[("status_p", "魅了", 1)], [("status_p", "魅了", 1)], [("status_p", "洗脳", 1)],')
    w('                      [("status_p", "洗脳", 1), ("dmg_p", 500)]]),')
    w("    mons={")
    head = {"e1": "召喚時：%s+1。" % both, "e2": "召喚時：男モンスター1体に拘束1ターン（男モンスターがいなければ何もしない）。",
            "e3": "召喚時：主人公に発情1ターン。", "boss": "召喚時：%s+3。" % both}
    tail = {"e1": "自分のターン終了時：男モンスター1体に攻撃指示不能1ターン（男モンスターがいなければ何もしない）。", "e2": "", "e3": "",
            "boss": "固有効果【%sの預かり】自分のターン終了時、主人公の%sが6以上なら1試合1回、男モンスター1体に拘束1ターンを与えて%s+6（男モンスターがいなければ何も起きない）。" % (clean(C["boss"]["name"]), S, MS)}
    ops = {"e1": 'summon_ops=[("add", 1)], end_ops=[("status_m_only", "攻撃指示不能", 1)]', "e2": 'summon_ops=[("status_m_only", "拘束", 1)]',
           "e3": 'summon_ops=[("status_p", "発情", 1)]',
           "boss": 'summon_ops=[("add", 3)],\n                     unique=dict(name=%r, min=6, once=True, ops=[("m_status_add", "拘束", 1, 6)])' % ("%sの預かり" % clean(C["boss"]["name"]))}
    for k in ("e1", "e2", "e3", "boss"):
        c = C[k]
        aid, lv, atk, hp, rare = STATS[k]
        fav_n = 3 if k == "boss" else 2
        ex = head[k] + "".join(tech_explain(t, fav_n, S, MS) for t in sorted(c["techs"], key=lambda t: not t.get("fav"))) + tail[k]
        w("        %r: dict(name=%r, aid=%d, lv=%d, atk=%d, hp=%d, rare=%r, race=%r, sex=%r," % (k, fullname(c), aid, lv, atk, hp, rare, c["race"], card_sex(c)))
        w("                   techs=[%s]," % ", ".join(tech_src(t, fav_n) for t in c["techs"]))
        w("                   explain=%r," % ex)
        w("                   %s)," % ops[k])
    w("    },")
    mg = b["magic"]
    w("    magic=std_magic(S, [(%r, \"add\", 2), (%r, \"search\", None), (%r, \"trap\", %r)," % (clean(mg["add"]), clean(mg["search"]), clean(mg["trap"]), mg.get("trap_st") or "魅了"))
    w("                        (%r, \"target\", (%r, 1)), (%r, \"persist\", None)])," % (clean(mg["target"]), mg.get("target_st") or "発情", clean(mg["persist"])))
    w(")")
    w("")
    w("# std_magic の説明文は主人公側の名前だけになるので、男モンスター側の名前と書き分ける。")
    w('_OLD = f"男モンスター1体（いなければ主人公）の{S}"')
    w('for _d in CFG["magic"]:')
    w('    for _k in ("explain", "persist_explain"):')
    w("        if _k in _d:")
    w("            _d[_k] = _d[_k].replace(_OLD, BOTH)")
    return "\n".join(L) + "\n"


def make_brief(b):
    S, MS, code, n = clean(b["stack"]), clean(b["mstack"]), b["code"], int(b["n"])
    C, D, title = b["chars"], defaults(b), clean(b["title"])
    kinds = sorted({C[k]["gender"] for k in CKEYS})
    L = []
    w = L.append
    w("# N%d %s（%s） 設計書（brief）" % (n, title, code))
    w("")
    w("成人向け（M男向け）カードゲーム「サキュバスデュエル」の個人用MOD。登場人物は全員20歳以上。個人利用のみ。")
    w("型：%s。書き方は kit\\common\\STYLE.md（本編踏襲・1本約4,000字・❤）に従う。" % "・".join(kinds))
    w("敵上位が絶対条件。主人公側は快楽攻撃を使わない。逆転・痛み・凌辱なし。挿入は必ず指ほぐしの後。")
    w("")
    w("## 1. 世界観・勝負の形")
    w(clean(b.get("world")) or "（未記入：場所・相手は何者か・なぜ勝負になるかを400字ほどで）")
    w("")
    w("## 2. 累積スタック")
    w("- 主人公：**%s**（12で敗北）。男モンスター：**%s**（6で%s）。主人公と男モンスターは別々に数える。" % (S, MS, D["fate_word"]))
    w("- 見た目・数え方：" + (clean(b.get("stack_desc")) or "（未記入：何が1つずつ増えるのか。体のどこに、どう見えるか）"))
    w("- 段階（主人公 1-3／4-6／7-9／10-11／12、男モンスター 0-1／2-3／4／5／6）ごとの様子：（未記入）")
    w("- 攻撃時のセリフは受けた側の段階で変える（主人公向け4段階・男モンスター向け4段階）。")
    w("")
    w("## 3. 場所の一覧（12〜15か所・五感の特徴つき）")
    w("（未記入）")
    w("")
    w("## 4. 道具・用語")
    w("（未記入：痛みのないもの。挿入具のサイズ。ふたなり・ニューハーフのサイズ）")
    w("")
    w("## 5. 主人公")
    w("二十歳・160cm・B80／W64／H82・細身・非筋肉質・紺髪・色白。一人称「僕」。味方の男モンスターの一人称も「僕」。")
    w("")
    w("## 6. 登場人物")
    w("| key | 名前（年齢・性別） | 身長・スリーサイズ | 外見 | 性格 | 一人称／主人公の呼び方／話し方 | 話者名 |")
    w("|---|---|---|---|---|---|---|")
    for k in CKEYS:
        c = C[k]
        w("| %s | %s（%s歳・%s） | %scm・B%s／W%s／H%s | %s | %s | %s／%s／%s | %%%s |" % (
            k, fullname(c), c["age"], c["gender"], c["height"], c["b"], c["w"], c["h"], clean(c.get("look")) or "（未記入）",
            clean(c.get("persona")) or "（未記入）", clean(c["first"]), clean(c.get("call")) or "（未記入）", clean(c.get("tone")) or "（未記入）", clean(c["name"])))
    w("")
    w("## 7. 責め手ごとの言い方表（おちんちん／お尻の穴／前立腺。全本でそろえる）")
    w("（未記入）")
    w("")
    w("## 8. 得意技表")
    w("| key | 技（攻撃タイプ） | 内容 | 印 |")
    w("|---|---|---|---|")
    keymap = [("m1", "master", 0), ("m2", "master", 1), ("m3", "master", 2), ("e1", "e1", None), ("e2", "e2", None), ("e3", "e3", None), ("boss", "boss", None)]
    for key, ck, i in keymap:
        ts = [C[ck]["techs"][i]] if i is not None else C[ck]["techs"]
        for t in ts:
            mark = ("★得意技 " if t.get("fav") else "") + ("挿入（指ほぐしの後） " if t.get("insert") else "") + ("ほぐし+1 " if t.get("finger") else "") + (("%s%sターン" % (t["st"], t.get("turns") or 1)) if t.get("st") else "")
            w("| %s | %s（%s） | %s | %s |" % (key, clean(t["name"]), t["type"], clean(t["desc"]), mark.strip()))
    w("")
    w("m1・m3 の本は「その技＋マスターの★を厚く混ぜる」。下級・上級の本は★を主役にする。")
    w("")
    w("## 9. オナニー表（key ごと。相手の★に合わせた自慰。安易にペニスを使わない）")
    w("| key | 自慰の内容 |")
    w("|---|---|")
    for key, _, _ in keymap:
        w("| %s | （未記入） |" % key)
    w("")
    w("## 10. 28本のあらすじ（key × btl／onani／inochi／onedari）")
    w("敗北イベントは1本5,000字以上（プレイ描写4,000字以上、状況・責めの理由は400字ほど）。同じ責め手の4本は場所・流れ・印で別物にする。")
    for key, ck, i in keymap:
        t = C[ck]["techs"][i] if i is not None else [x for x in C[ck]["techs"] if x.get("fav")][0]
        w("")
        w("### %s %s・%s　結末：（未記入）" % (key, clean(C[ck]["name"]), clean(t["name"])))
        w("| 経路 | 場所 | あらすじ（100〜180字） | 寸止めで言わせる言葉（2つ） | ★だけの2回目 | 印 |")
        w("|---|---|---|---|---|---|")
        for r in ("btl", "onani", "inochi", "onedari"):
            w("| %s | （未記入） | （未記入） | （未記入） | （未記入） | （未記入） |" % r)
    w("")
    w("## 11. カード効果")
    w("- マスター（atk500）：ターン終了時、主人公の%sの段階に応じて 魅了／魅了／洗脳／洗脳＋500。★で+3。" % S)
    w("- e1（atk550・hp1600）：召喚時+1。ターン終了時、男モンスター1体に攻撃指示不能1ターン。★で+2。")
    w("- e2（atk500・hp1500）：召喚時、男モンスター1体に拘束1ターン。★で+2。")
    w("- e3（atk450・hp1400）：召喚時、主人公に発情1ターン。★で+2。")
    w("- boss（atk1200・hp6000）：召喚時+3。固有効果（主人公の%sが6以上・1試合1回・男モンスター1体に拘束1ターンと%s+6）。★で+3。" % (S, MS))
    mg = b["magic"]
    w("- 魔法・罠：%s（+2）／%s（サーチ）／%s（罠：攻撃したカードに%s1ターン）／%s（男モンスター1体に%s1ターン）／%s（永続+1・3回で自壊）。" % (
        clean(mg["add"]), clean(mg["search"]), clean(mg["trap"]), mg.get("trap_st") or "魅了", clean(mg["target"]), mg.get("target_st") or "発情", clean(mg["persist"])))
    w("")
    w("## 12. 話者名と画像")
    w("話者名：" + "／".join("%%%s" % clean(C[k]["name"]) for k in CKEYS) + "。主人公は 相手プレイヤー。")
    w("画像行の書き方：`画像,#%s/%s_lose_<経路>_<key>.png,1`。バトル中と敗北時のBGMは本編のものを使う。" % (code, code))
    w("")
    w("## 次にすること")
    w("1. この設計書の（未記入）を埋める　2. scen\\ に敗北シナリオ28本　3. lines\\ にセリフ5本（m・e1・e2・e3・boss）")
    w("4. まとめツールの「点検」→「組み立て」　5. 画像プロンプト → 撮影 → ゲームへ反映")
    return "\n".join(L) + "\n"
