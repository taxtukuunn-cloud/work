# -*- coding: utf-8 -*-
"""MOD の本文（CSV の中の txt）から、長さの記述（◯cm・◯センチ）を探して一覧にする。書き換えはしない。
結果: 同じフォルダの サイズの記述_一覧.csv"""
import os, re, csv, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)   # C:\Users\...\Downloads\MOD
RX = re.compile(r"[0-9０-９〇一二三四五六七八九十]+\s*(?:cm|ｃｍ|センチ|㎝)", re.I)
SKIP = ("_バックアップ", "_プロジェクト復元", "old", "Zip", "画像生成", "claude", "_出張資料")

def read(p):
    b = open(p, "rb").read()
    for enc in ("utf-8-sig", "cp932", "utf-16"):
        try:
            return b.decode(enc), enc
        except Exception:
            pass
    return b.decode("utf-8", "replace"), "utf-8?"

rows = []
mods = 0
for d in sorted(os.listdir(ROOT)):
    base = os.path.join(ROOT, d)
    if not os.path.isdir(base) or d in SKIP or not os.path.isdir(os.path.join(base, "CSV")):
        continue
    mods += 1
    for dp, _, fs in os.walk(os.path.join(base, "CSV")):
        for fn in sorted(fs):
            if not fn.lower().endswith(".txt"):
                continue
            p = os.path.join(dp, fn)
            try:
                text, enc = read(p)
            except Exception as e:
                rows.append([d, os.path.relpath(p, base), "", "", "読めない: %s" % e, ""]); continue
            for i, line in enumerate(text.splitlines(), 1):
                for m in RX.finditer(line):
                    a, b = max(0, m.start() - 45), min(len(line), m.end() + 30)
                    rows.append([d, os.path.relpath(p, base), i, m.group(0), line[a:b].replace("\t", " "), enc])
out = os.path.join(HERE, "サイズの記述_一覧.csv")
with open(out, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["MOD", "ファイル", "行", "記述", "前後の文", "文字コード"])
    w.writerows(rows)
print("調べたMOD: %d ／ 見つかった記述: %d" % (mods, len(rows)))
print("結果:", out)
