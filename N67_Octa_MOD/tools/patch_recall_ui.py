# -*- coding: utf-8 -*-
"""
回想バトル用「回想の栞」パッチ（全MOD共通）

使い方:  python patch_recall_ui.py <Cardフォルダ> <コード>
  例:    python patch_recall_ui.py "N26_Kitsune_MOD\\CSV\\Card" Kitsune

やること
 1. <コード>_recall.txt（永続魔法「回想の栞」）を作る。
    回想バトル中だけ主人公の手札に配られ、場に出すと／場にある間いつでも、
    相手のデッキ一覧 → カード詳細（特殊召喚・ドロー・閉じる）を開ける。
 2. <コード>_master.txt の @回想メニュー を「栞を手札に配るだけ」に置き換え、
    @回想バトル の デッキ設定 の直前に $回想栞配布,=,0 を入れる。
    （毎ターンの選択肢メニューは出なくなる）
build.py / gen.py でカードを作り直したら、もう一度このスクリプトを実行する。
何度実行しても同じ結果になる（二重に入らない）。
"""
import os, re, sys

MARK = "//回想の栞パッチ"


def read(p):
    with open(p, "rb") as f:
        b = f.read()
    if b.startswith(b"\xef\xbb\xbf"):
        b = b[3:]
    return b.decode("utf-8")


def write(p, text):
    text = text.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(p, "wb") as f:
        f.write(text.encode("utf-8"))


def sections(text):
    """[(name, start_line_idx, end_line_idx_exclusive)]"""
    lines = text.replace("\r\n", "\n").split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("@")]
    out = []
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        out.append((lines[i][1:].strip(), i, j))
    return lines, out


def parse_card(path):
    t = read(path)
    lines, secs = sections(t)
    init = []
    for n, a, b in secs:
        if n == "初期設定":
            init = lines[a + 1:b]
    info = {"file": os.path.splitext(os.path.basename(path))[0], "effects": {}}
    for l in init:
        s = l.strip()
        if not s:
            continue
        parts = s.split(",")
        k = parts[0]
        if k == "&カード名":
            info["name"] = ",".join(parts[1:]).strip()
        elif k == "&カード画像":
            info["img"] = parts[1].strip()
        elif k == "&背景":
            info["bg"] = parts[1].strip()
        elif k == "レベル設定":
            info["lv"] = parts[1].strip()
        elif k == "攻撃力設定":
            info["atk"] = parts[1].strip()
        elif k == "最大HP設定":
            info["hp"] = parts[1].strip()
        elif k == "属性設定":
            info["attr"] = parts[1].strip()
        elif k == "タイプ設定":
            info["type"] = parts[1].strip()
        elif k == "効果設定" and len(parts) >= 4:
            eid = parts[1].strip()
            txt = ",".join(parts[3:]).strip()
            if txt:
                info["effects"][eid] = txt
    info["is_mon"] = "lv" in info and "魔法" not in info.get("type", "") and "罠" not in info.get("type", "")
    return info


def safe(s):
    s = s.replace(",", "、").replace("<", "＜").replace(">", "＞")
    s = s.replace("{", "（").replace("}", "）").replace("$", "＄").replace("%", "％").replace("&", "＆").replace("#", "＃")
    return s


def detail_text(c):
    if c["is_mon"]:
        head = f'{c["name"]}★{c.get("lv","")} Atk{c.get("atk","")} HP{c.get("hp","")}\\n{c.get("attr","")}／{c.get("type","")} ID {c["file"]}'
    else:
        head = f'{c["name"]}\\n{c.get("attr","")}／{c.get("type","")} ID {c["file"]}'
    body = []
    n = 1
    for eid in sorted((e for e in c["effects"] if e != "0"), key=lambda x: int(x) if x.isdigit() else 99):
        body.append(f"[{n}].{c['effects'][eid]}")
        n += 1
    flav = c["effects"].get("0", "")
    txt = "\\n".join(body)
    if flav:
        txt += "\\n\\n" + flav
    return safe(head), safe(txt)


def deck_from_master(mlines, msecs):
    for n, a, b in msecs:
        if n == "回想バトル":
            for l in mlines[a:b]:
                if l.strip().startswith("デッキ設定,"):
                    ids = [x.strip() for x in l.strip().split(",")[1:] if x.strip()]
                    uniq = []
                    for x in ids:
                        if x not in uniq:
                            uniq.append(x)
                    return uniq
    return []


MENU_SECS = ("回想メニュー", "回想操作")


def _block_end(lines, i):
    """lines[i] is an if line; returns index of matching closing brace"""
    depth = 0
    j = i + 1
    while j < len(lines):
        t = lines[j].strip()
        if t == "{":
            depth += 1
        elif t == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return None


def menu_regions(lines, secs):
    """[(kind, start, end, secname)] kind=section: body lines[start:end]; inline: lines[start:end+1]"""
    out = []
    for n, a, b in secs:
        body = lines[a + 1:b]
        has_menu = any(l.strip().startswith("選択肢生成") for l in body) or any(MARK in l for l in body)
        if n in MENU_SECS:
            if has_menu:
                out.append(("section", a + 1, b, n))
            continue
        if n in ("試合開始", "ターン開始") and any(l.strip().startswith("選択肢生成") for l in body):
            i = a + 1
            while i < b:
                t = lines[i].strip()
                if re.match(r"if,\$\$\w+_回想\w*,==,1$", t) and not lines[i].startswith(" "):
                    e = _block_end(lines, i)
                    if e is not None and any(l.strip().startswith("選択肢生成") for l in lines[i:e]):
                        out.append(("inline", i, e, n))
                        i = e
                i += 1
    return out


def old_menu_lines(mlines, msecs):
    """旧メニューから責め手のセリフ（導入・召喚・手札）を拾う。パッチ済みなら None"""
    regs = menu_regions(mlines, msecs)
    if not regs:
        return None
    k, a, b, n = regs[0]
    body = mlines[a:b + (1 if k == "inline" else 0)]
    if any(MARK in l for l in body):
        return None
    intro = summon = search = None
    state = 0
    for l in body:
        s = l.strip()
        if s.startswith("選択肢生成"):
            state = 1
        m = re.match(r"if,選択肢,==,(\d)", s)
        if m:
            state = 10 + int(m.group(1))
        if s.startswith("セリフ,"):
            t = s[len("セリフ,"):]
            if state in (0, 1) and intro is None:
                intro = t
            elif state == 11 and summon is None:
                summon = t
            elif state == 12 and search is None:
                search = t
    return intro, summon, search


def name_key(name):
    segs = [x for x in re.split(r"[ 　・]", name) if x]
    return segs[-1] if segs else name


def lookup(f, name, indent, gen_cmd=None):
    """%対象 に相手デッキの該当カード（1枚以上）を入れる。IDで見つからなければ名前で探す"""
    k = safe(name_key(name))
    i = " " * indent
    # ?ID は実機で絞り込まれなかった（デッキ全体からランダムになった）ため、名前で探す
    L = [f"{i}%対象,=,相手デッキ.?NamePart:{k}"]
    return L


def build_recall(code, cards, master, lines):
    intro, summon, search = lines
    L = []
    a = L.append
    a("default")
    a("@初期設定")
    a("    &カード名,回想の栞")
    a(f"    &カード画像,{master.get('img', '#'+code+'/'+code+'_master.png')}")
    for i, c in enumerate(cards, 1):
        a(f"    &回想画像_{i},{c.get('img','')}")
    a("    &回想パネル,#RecallUI/recall_panel.png")
    a(f"    &戻り背景,{master.get('bg', '&&グレー背景')}")
    a("    属性設定,光属性")
    a("    タイプ設定,永続魔法")
    a("    レアリティ設定,UR")
    a("    効果設定,1,play,発動時：相手のデッキを開く。好きなカードを選んで、相手の場に特殊召喚させるか、相手の手札に加えさせる（ドロー）。")
    a("    効果設定,2,起動,場にある間、自分のターンに何度でも使える：相手のデッキを開き、好きなカードを選んで特殊召喚させるか、ドローさせる。デッキに残っていないカードは新しく生成される。")
    a(f"    効果設定,0,explain,回想バトル専用。あの夜の記憶に挟んでおいた栞。めくれば、{safe(master.get('name',''))}の手札も場も、思い出の中で好きなように並べ直せる。")
    a("")
    a("@効果")
    a("switch,効果ID")
    a("case,1")
    a("{")
    a(" イベント実行,回想デッキ")
    a("}")
    a("case,2")
    a("{")
    a(" イベント実行,回想デッキ")
    a("}")
    a("")
    # ---- deck list screen ----
    a("@回想デッキ")
    a("&一覧,(" + ",".join("%%" + c["file"] for c in cards) + ")")
    a(f"$一覧数,=,{len(cards)}")
    a("$画像id用プラス,=,100")
    a("$ソーターid,=,2")
    a("$配列位置,=,1")
    a("$ページ内項目数,=,10")
    a("$旧配列位置,=,0")
    a("$終了,=,0")
    a("$操作,=,0")
    a("$番号,=,0")
    a("イベント実行,回想一覧画面")
    a("while,$終了,==,0")
    a("{")
    a(" if,$旧配列位置,!=,$配列位置")
    a(" {")
    a("  $旧配列位置,=,$配列位置")
    a("  $count,=,0")
    a("  子画像全削除,$ソーターid")
    a("  while,$count,<,$ページ内項目数")
    a("  {")
    a("   括弧文字列抜き出し,&一覧,$配列位置+$count,&カード")
    a("   %カード,=,&カード")
    a("   $画像id,=,$配列位置+$count+$画像id用プラス")
    a("   画像,$画像id,%カード.&カード画像")
    a("   親子化,$ソーターid,$画像id")
    a("   $count,+=,1")
    a("   if,$配列位置+$count,>,$一覧数")
    a("   {")
    a("    break")
    a("   }")
    a("  }")
    a(" }")
    # 実機：先に作った画像ほど手前に出た（後から作った矢印や一覧が下敷きに隠れた）ため、下敷きは最後に作る
    a(" 画像,1000,&回想パネル")
    a(" 画像縦横比不保持,1000")
    a(" 画像アンカー,1000,(0,0),(1,1)")
    a(" ボタン付加,1001,1002,1003")
    a(" 全子供ボタン付加,$ソーターid")
    a(" ボタン待ち")
    a(" switch,選択肢")
    a(" case,1001")
    a(" {")
    a("  $配列位置,-=,$ページ内項目数")
    a("  if,$配列位置,<=,0")
    a("  {")
    a("   $配列位置,=,1")
    a("  }")
    a(" }")
    a(" case,1002")
    a(" {")
    a("  if,$一覧数,>=,$配列位置+$ページ内項目数")
    a("  {")
    a("   $配列位置,+=,$ページ内項目数")
    a("  }")
    a(" }")
    a(" case,1003")
    a(" {")
    a("  $終了,=,1")
    a(" }")
    a(" default")
    a(" {")
    a("  $番号,=,選択肢-$画像id用プラス")
    a("  画像全削除")
    a("  $操作,=,0")
    a("  イベント実行,回想詳細")
    a("  if,$操作,!=,0")
    a("  {")
    a("   $終了,=,1")
    a("  }else{")
    a("   イベント実行,回想一覧画面")
    a("   $旧配列位置,=,0")
    a("  }")
    a(" }")
    a("}")
    a("画像全削除")
    a("背景,&戻り背景")
    a("if,$操作,==,1")
    a("{")
    a(" イベント実行,回想召喚")
    a("}")
    a("if,$操作,==,2")
    a("{")
    a(" イベント実行,回想ドロー")
    a("}")
    a("")
    a("@回想一覧画面")
    a("背景,&&グレー背景")
    a('テキスト画像,1004,<align="center">相手のデッキ　カードを選ぶと「特殊召喚」「ドロー」を選べます')
    a("画像アンカー,1004,(0.12,0.84),(0.86,0.97)")
    a("ソーター,$ソーターid,グリッド,(0.15,0.12),(0.85,0.82)")
    a("ソーター一行グリッド数,$ソーターid,5")
    a("画像,1001,&&UI左矢印")
    a("画像,1002,&&UI右矢印")
    a("画像,1003,&&閉じるアイコン")
    a("画像アンカー,1001,(0.02,0.4),(0.1,0.6)")
    a("画像アンカー,1002,(0.9,0.4),(0.98,0.6)")
    a("画像アンカー,1003,(0.9,0.9),(0.98,0.98)")
    a("")
    # ---- detail window ----
    a("@回想詳細")
    a("背景,&&グレー背景")
    a("$モンスター,=,0")
    a("$残,=,0")
    a("switch,$番号")
    for i, c in enumerate(cards, 1):
        head, body = detail_text(c)
        a(f"case,{i}")
        a("{")
        a(f" 画像,1104,&回想画像_{i}")
        L += lookup(c["file"], c["name"], 1)
        a(" $残,=,%対象.Count")
        a(f' テキスト画像,1105,<align="left">{head}\\n相手デッキの残り：{{$残}}枚\\n<size=78%>{body}')
        if c["is_mon"]:
            a(" $モンスター,=,1")
        a("}")
    a("画像アンカー,1104,(0,0),(0.5,1)")
    a("画像アンカー,1105,(0.52,0.22),(0.97,0.97)")
    a("ソーター,1106,横型,(0.3,0.02),(0.99,0.19)")
    a("if,$モンスター,==,1")
    a("{")
    a(" 画像,1107,&&ボタン背景青")
    a(" 画像縦横比不保持,1107")
    a(" 親子化,1106,1107")
    a(" テキスト画像,1108,特殊召喚")
    a(" 親子化,1107,1108")
    a("}")
    a("画像,1109,&&ボタン背景赤")
    a("画像縦横比不保持,1109")
    a("親子化,1106,1109")
    a("テキスト画像,1110,ドロー")
    a("親子化,1109,1110")
    a("画像,1111,&&ボタン背景灰")
    a("画像縦横比不保持,1111")
    a("親子化,1106,1111")
    a("テキスト画像,1112,閉じる")
    a("親子化,1111,1112")
    a("画像,1000,&回想パネル")
    a("画像縦横比不保持,1000")
    a("画像アンカー,1000,(0,0),(1,1)")
    a("全子供ボタン付加,1106")
    a("ボタン待ち")
    a("$操作,=,0")
    a("if,選択肢,==,1107")
    a("{")
    a(" $操作,=,1")
    a("}")
    a("if,選択肢,==,1108")
    a("{")
    a(" $操作,=,1")
    a("}")
    a("if,選択肢,==,1109")
    a("{")
    a(" $操作,=,2")
    a("}")
    a("if,選択肢,==,1110")
    a("{")
    a(" $操作,=,2")
    a("}")
    a("画像全削除")
    a("")
    # ---- actions ----
    a("@回想召喚")
    a("switch,$番号")
    for i, c in enumerate(cards, 1):
        if not c["is_mon"]:
            continue
        f = c["file"]
        a(f"case,{i}")
        a("{")
        a(" if,相手モンスター.Count,>=,3")
        a(" {")
        a("  アラート,相手の場がいっぱいのため、特殊召喚できません。")
        a(" }else{")
        L += lookup(f, c["name"], 2)
        a("  if,%対象.Count,==,0")
        a("  {")
        a(f"   効果生成デッキ内,{f},相手所属")
        L += lookup(f, c["name"], 3)
        a("  }")
        a("  カードランダム抜き出し,%対象,1,%召喚")
        if summon:
            a("  話者,相手プレイヤー")
            a(f"  セリフ,{summon}")
        a("  特殊召喚,%召喚,相手所属")
        a(" }")
        a("}")
    a("")
    a("@回想ドロー")
    a("switch,$番号")
    for i, c in enumerate(cards, 1):
        f = c["file"]
        a(f"case,{i}")
        a("{")
        if search:
            a(" 話者,相手プレイヤー")
            a(f" セリフ,{search}")
        L += lookup(f, c["name"], 1)
        a(" if,%対象.Count,==,0")
        a(" {")
        a(f"  効果生成ドロー,{f},相手所属")
        a(" }else{")
        a("  カードランダム抜き出し,%対象,1,%召喚")
        a("  効果サーチ,%召喚,相手所属")
        a(" }")
        a("}")
    a("")
    return "\n".join(L) + "\n"


def menu_body(code, intro):
    # 試合開始の時点では手札が配られる前で消える場合があるため、
    # 主人公の手札・魔法ゾーンに栞が無ければ、そのたびに1枚作って手札に入れる。
    out = [MARK,
           "$栞の数,=,相手手札.?NamePart:回想の栞.Count+相手スペル.?NamePart:回想の栞.Count",
           "if,$栞の数,==,0",
           "{"]
    out += ["if,$回想栞配布,==,0", "{"]
    if intro:
        out += [" 話者,自分", f" セリフ,{intro}"]
    out += [" 説明,【回想バトル】主人公の手札に「回想の栞」が加わる。自分のターンに場に出すと、相手のデッキを開いて好きなカードを選び、「特殊召喚」か「ドロー」をさせられる。場に置いたあとも、自分のターンなら何度でも効果を使える。",
            "}",
            " $回想栞配布,=,1",
            f" 効果生成ドロー,{code}_recall,相手所属",
            "}", ""]
    # indent fix: nested if needs its own braces already present
    return out


def patch_master(code, mtext, intro):
    lines, secs = sections(mtext)
    regs = menu_regions(lines, secs)
    repl = {}  # start -> (end_exclusive, new_lines)
    has_menu_sec = any(n in MENU_SECS for n, _, _ in secs)
    for k, a, b, n in regs:
        if k == "section":
            repl[a] = (b, menu_body(code, intro))
        else:
            cond = lines[a].strip()
            target = next((m for m in MENU_SECS if any(x == m for x, _, _ in secs)), "回想メニュー")
            repl[a] = (b + 1, [cond, "{", f" イベント実行,{target}", "}"])
    for n, a, b in secs:
        if n == "回想バトル":
            body = lines[a:b]
            if not any(l.strip() == "$回想栞配布,=,0" for l in body):
                for j in range(a, b):
                    if lines[j].strip().startswith("デッキ設定,"):
                        repl[j] = (j + 1, ["$回想栞配布,=,0", lines[j]])
                        break
    out = []
    i = 0
    while i < len(lines):
        if i in repl:
            e, nl = repl[i]
            out.extend(nl)
            i = e
            continue
        out.append(lines[i])
        i += 1
    if not has_menu_sec:
        out += ["", "@回想メニュー"] + menu_body(code, intro)
    if not any(n == "相手ターン開始" for n, _, _ in secs):
        flag = None
        for l in lines:
            m = re.match(r"if,(\$\$\w+_回想\w*),==,1$", l.strip())
            if m:
                flag = m.group(1)
                break
        target = next((m for m in MENU_SECS if any(x == m for x, _, _ in secs)), "回想メニュー")
        out += ["", "@相手ターン開始", MARK, f"if,{flag},==,1", "{", f" イベント実行,{target}", "}", ""]
    return "\n".join(out)


def main(card_dir, code):
    mpath = os.path.join(card_dir, f"{code}_master.txt")
    mtext = read(mpath)
    mlines, msecs = sections(mtext)
    names = [n for n, _, _ in msecs]
    assert "回想バトル" in names, "master に @回想バトル がない"
    assert menu_regions(mlines, msecs), "回想メニューの処理が見つからない"
    deck = deck_from_master(mlines, msecs)
    assert deck, "回想バトルのデッキ設定が見つからない"
    got = old_menu_lines(mlines, msecs)
    if got is None:  # already patched -> recover lines from previous output
        intro = summon = search = None
        for n, a, b in msecs:
            if n in MENU_SECS:
                for l in mlines[a:b]:
                    if l.strip().startswith("セリフ,"):
                        intro = l.strip()[4:]
                        break
        rp = os.path.join(card_dir, f"{code}_recall.txt")
        if os.path.exists(rp):
            rl, rs = sections(read(rp))
            for n, a, b in rs:
                for l in rl[a:b]:
                    if l.strip().startswith("セリフ,"):
                        if n == "回想召喚" and summon is None:
                            summon = l.strip()[4:]
                        if n == "回想ドロー" and search is None:
                            search = l.strip()[4:]
        got = (intro, summon, search)
    cards = [parse_card(os.path.join(card_dir, f + ".txt")) for f in deck]
    master = parse_card(mpath)
    write(os.path.join(card_dir, f"{code}_recall.txt"), build_recall(code, cards, master, got))
    write(mpath, patch_master(code, mtext, got[0]))
    print(f"OK {code}: deck {len(cards)} kinds, lines intro={bool(got[0])} summon={bool(got[1])} search={bool(got[2])}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
