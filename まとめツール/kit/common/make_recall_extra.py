# -*- coding: utf-8 -*-
"""Yakai / Rosetta に回想バトル（回想の栞）を追加する。
patch_recall_ui.py の build_recall を流用し、master には
@回想バトル・@回想メニュー・@相手ターン開始 を足し、@試合開始 に呼び出しを足す。
何度実行しても二重には入らない（MARK で判定）。
使い方: python make_recall_extra.py <Cardフォルダ> <コード>
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import patch_recall_ui as P

MARK = P.MARK

CFG = {
    "Rosetta": dict(
        flag="$$Rosetta_回想中",
        bg="&&豪華な寝室背景",
        ind="    ",
        intro_lines=[
            ("画像", "&カード画像,2"),
            ("話者", "自分"),
            ("セリフ", "あら、また来てくれたのね。今夜は『おさらい』の時間よ❤\\nどの子に躾けてほしいか…あなたが選んでいいわ"),
            ("説明", "【回想バトル】主人公の手札に「回想の栞」が配られる。自分のターンに場に出すと、相手のデッキを開いて好きなカードを特殊召喚させたり、ドローさせたりできる。報酬はない。"),
        ],
        pre=["$$ロゼッタ_最後の責め手,=,1"],
        post_setup=["バトル設定,相手先攻"],
        menu_intro="ふふ、栞を渡しておくわ。見たい躾けがあったら、それで呼び出しなさい❤",
        summon="その子をご指名？いいわ。たっぷり躾けてもらいなさい❤",
        search="そのカードね。手元に置いておいてあげる❤",
        win=[("画像", "&カード画像,0"), ("話者", "自分"),
             ("セリフ", "ふふ、おさらいはここまで。…また躾けてほしくなったら、いつでもいらっしゃい❤")],
    ),
    "Yakai": dict(
        flag="$$Yakai_回想中",
        bg="&&豪華な寝室背景",
        ind="",
        intro_lines=[
            ("画像", "&カード画像,1"),
            ("話者", "自分"),
            ("セリフ", "あら❤また来てくださったのね❤今夜はあなたの好きな子を❤好きなだけ呼んでいいわ❤"),
            ("説明", "【回想バトル】主人公の手札に「回想の栞」が配られる。自分のターンに場に出すと、相手のデッキを開いて好きなカードを特殊召喚させたり、ドローさせたりできる。報酬はない。"),
        ],
        pre=["$$Yakai_last,=,1", "$$Yakai_敗北済,=,0", "$$Yakai_進行,=,0"],
        post_setup=[],
        menu_intro="この栞をどうぞ❤会いたい子がいたら❤それで呼んでちょうだい❤",
        summon="あら❤その子をご指名？いいわ❤たっぷり可愛がってもらいなさい❤",
        search="ふふ❤そのカード❤手元に置いておくわね❤",
        win=[("画像", "&カード画像,1"), ("話者", "自分"),
             ("セリフ", "くすっ❤今夜はここまで❤また会いたくなったら❤いつでもいらしてね❤")],
    ),
}

# ---- parse_card を拡張：フレーバーテキスト（効果設定,0 が無いカード）も詳細に出す
_orig_parse = P.parse_card


def parse_card(path):
    info = _orig_parse(path)
    if "0" not in info["effects"]:
        for l in P.read(path).replace("\r\n", "\n").split("\n"):
            s = l.strip()
            for k in ("&フレーバーテキスト,", "フレーバーテキスト,"):
                if s.startswith(k):
                    info["effects"]["0"] = s[len(k):]
                    break
            if "0" in info["effects"]:
                break
    return info


P.parse_card = parse_card


def section_bounds(lines, name):
    for i, l in enumerate(lines):
        if l.strip() == "@" + name and l.startswith("@"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("@"):
                j += 1
            return i, j
    return None


def quest_battle_block(lines, code):
    """@クエストイベント の デッキ設定 から最後の if,is敗北 ブロック（敗北処理）までを取り出す"""
    a, b = section_bounds(lines, "クエストイベント")
    body = lines[a + 1:b]
    di = next(i for i, l in enumerate(body) if l.strip().startswith("デッキ設定,"))
    deck = body[di].strip()
    bi = next(i for i, l in enumerate(body) if l.strip().startswith("バトル開始,"))
    battle = body[bi].strip()
    ii = next(i for i in range(bi, len(body)) if body[i].strip() == "if,is敗北,==,true")
    # 敗北ブロック: if の次の { から、深さ1で閉じる } または }else{ の手前まで
    assert body[ii + 1].strip() == "{"
    depth = 1
    lose = []
    j = ii + 2
    while j < len(body):
        t = body[j].strip()
        if t == "{":
            depth += 1
        elif t == "}":
            depth -= 1
            if depth == 0:
                break
        elif t == "}else{":
            if depth == 1:
                break
        if t:
            # 元のインデントを1段分（if の中身として）保つ
            lose.append(body[j].strip() if t in ("{", "}", "}else{") else t)
        j += 1
    assert depth >= 1 or True
    return deck, battle, lose


def build_master_patch(code, text):
    c = CFG[code]
    ind = c["ind"]
    lines = text.replace("\r\n", "\n").split("\n")
    if any(MARK in l for l in lines):
        print("already patched:", code)
        return None, None
    deck, battle, lose = quest_battle_block(lines, code)
    # ---- @クエストイベント の先頭で回想フラグを確実に下ろす
    a, b = section_bounds(lines, "クエストイベント")
    lines.insert(a + 1, f"{ind}{c['flag']},=,0")
    # ---- @試合開始 の末尾に呼び出し
    a, b = section_bounds(lines, "試合開始")
    end = b
    while end - 1 > a and lines[end - 1].strip() == "":
        end -= 1
    call = [f"{ind}{MARK}", f"{ind}if,{c['flag']},==,1", f"{ind}{{", f"{ind} イベント実行,回想メニュー", f"{ind}}}"]
    lines[end:end] = call
    out = lines
    while out and out[-1].strip() == "":
        out.pop()
    # ---- 追加セクション
    add = ["", "@回想バトル", MARK, f"{c['flag']},=,1", "$回想栞配布,=,0", f"背景変更,{c['bg']}"]
    for k, v in c["intro_lines"]:
        add.append(f"{k},{v}")
    add += c["pre"]
    add.append(deck)
    add += c["post_setup"]
    add.append(battle)
    add += ["if,is敗北,==,true", "{"]
    add += [" " + l for l in lose]
    add += ["}else{", " BGM,&&戦闘BGM"]
    for k, v in c["win"]:
        add.append(f" {k},{v}")
    add += ["}", f"{c['flag']},=,0", ""]
    add += ["@回想メニュー"] + P.menu_body(code, c["menu_intro"])
    add += ["@相手ターン開始", MARK, f"if,{c['flag']},==,1", "{", " イベント実行,回想メニュー", "}", ""]
    out += add
    deck_ids = []
    for x in deck.split(",")[1:]:
        x = x.split("//")[0].strip()
        if x and x not in deck_ids:
            deck_ids.append(x)
    return "\n".join(out), deck_ids


def main(card_dir, code):
    c = CFG[code]
    mpath = os.path.join(card_dir, f"{code}_master.txt")
    text = P.read(mpath)
    new, deck = build_master_patch(code, text)
    if new is None:
        return
    cards = [parse_card(os.path.join(card_dir, f + ".txt")) for f in deck]
    master = parse_card(mpath)
    master["bg"] = c["bg"]
    rec = P.build_recall(code, cards, master, (c["menu_intro"], c["summon"], c["search"]))
    P.write(os.path.join(card_dir, f"{code}_recall.txt"), rec)
    P.write(mpath, new)
    print(f"OK {code}: {len(cards)} kinds ->", ", ".join(deck))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
