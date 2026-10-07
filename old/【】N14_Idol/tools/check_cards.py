#!/usr/bin/env python3
"""カードtxtの構文チェック（N14用。他MODにも流用可）。"""
import sys, re, glob, os

OFFICIAL = set("通常攻撃 おっぱい パイズリ ぱふぱふ フェラ 手コキ 足コキ 脇コキ ハグ ふとももコキ 膝コキ 尻コキ 尻尾コキ 髪コキ キス スマタ 素股 魔法責め 触手 触手コキ 耳責め 乳首責め 強制自慰 パンチラ 息 本番".split())

def check(path):
    errs = []
    raw = open(path, "rb").read()
    if b"\n" in raw.replace(b"\r\n", b""):
        errs.append("LFのみの改行がある（CRLFに統一）")
    lines = raw.decode("utf-8").split("\r\n")
    if lines[0] != "default":
        errs.append("1行目が default でない")
    sections = set(l[1:] for l in lines if l.startswith("@"))
    depth = 0
    images = set()
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("@"):
            if depth != 0:
                errs.append(f"{i}: セクション開始時に括弧が閉じていない（depth={depth}）")
                depth = 0
            continue
        if s.startswith("if,"):
            nxt = lines[i].strip() if i < len(lines) else ""
            if nxt != "{":
                errs.append(f"{i}: if の次の行が {{ ではない")
        if s in ("else", "}else", "else{"):
            errs.append(f"{i}: else は }}else{{ の1行で書く")
        if s in ("{",):
            depth += 1
        elif s == "}":
            depth -= 1
        elif s == "}else{":
            pass
        if depth < 0:
            errs.append(f"{i}: 閉じ括弧が多い"); depth = 0
        m = re.match(r"^(セリフ|説明|アラート),(.*)$", s)
        if m:
            body = m.group(2).replace("{$表示用}", "")
            bad = set(c for c in body if c in ",$%&#{}<>")
            if bad:
                errs.append(f"{i}: 本文に禁止文字 {''.join(sorted(bad))}")
        for kw in ("攻撃タイプ,==,", "攻撃タイプ固定,", "主人公攻撃タイプ弱点付与,"):
            if s.startswith("if," + kw) or s.startswith(kw):
                t = s.split(kw, 1)[1].split(",")[0]
                if t not in OFFICIAL:
                    errs.append(f"{i}: 公式にない攻撃タイプ {t}")
        if s.startswith("攻撃タイプランダム変更,"):
            for t in s.split(",")[1:]:
                if t not in OFFICIAL:
                    errs.append(f"{i}: 公式にない攻撃タイプ {t}")
        if s.startswith("イベント実行,"):
            tgt = s.split(",", 1)[1]
            if tgt not in sections:
                errs.append(f"{i}: イベント実行 の先 @{tgt} がない")
        for img in re.findall(r"#Idol/[A-Za-z0-9_]+\.png", s):
            images.add(img)
        if s.startswith(("話者変更", "画像表示")):
            errs.append(f"{i}: 旧コマンド {s.split(',')[0]}")
    if depth != 0:
        errs.append(f"末尾で括弧が閉じていない（depth={depth}）")
    return errs, images

if __name__ == "__main__":
    allimg = set()
    ok = True
    for p in sorted(sys.argv[1:]):
        errs, imgs = check(p)
        allimg |= imgs
        print(f"[{'OK' if not errs else 'NG'}] {os.path.basename(p)}")
        for e in errs[:30]:
            print("   ", e)
        ok &= not errs
    print(f"参照画像 {len(allimg)} 枚")
    for i in sorted(allimg):
        print("  ", i)
    sys.exit(0 if ok else 1)
