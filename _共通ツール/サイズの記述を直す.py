# -*- coding: utf-8 -*-
"""MOD の本文の長さの記述を、サイズの記述_直す一覧.json のとおりに書き換える（2026-10-03）。
・書き換える前のファイルを MOD\\_バックアップ\\サイズ変更前_2026-10-03\\ に控える（すでに控えがあれば上書きしない）
・指定の行に元の語が無ければ、その行は触らない（結果の一覧に「見つからない」と出る）
・--dry を付けると書き換えずに数だけ出す
結果: サイズの記述_直した結果.csv"""
import os, sys, json, csv, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BK = os.path.join(ROOT, "_バックアップ", "サイズ変更前_2026-10-03")
DRY = "--dry" in sys.argv
with open(os.path.join(HERE, "サイズの記述_直す一覧.json"), encoding="utf-8") as f:
    edits = json.load(f)
by = {}
for mod, rel, line, old, new in edits:
    by.setdefault((mod, rel.replace("\\", os.sep).replace("/", os.sep)), []).append((int(line), old, new))
rows = []; nfile = 0
for (mod, rel), es in sorted(by.items()):
    p = os.path.join(ROOT, mod, rel)
    if not os.path.exists(p):
        rows += [[mod, rel, l, o, n, "ファイルが無い"] for l, o, n in es]; continue
    b = open(p, "rb").read()
    text = enc = None
    for e in (("utf-8-sig",) if b[:3] == b"\xef\xbb\xbf" else ("utf-8", "cp932", "utf-16")):
        try:
            text = b.decode(e); enc = e; break
        except Exception:
            pass
    if text is None:
        rows += [[mod, rel, l, o, n, "読めない"] for l, o, n in es]; continue
    L = text.splitlines(keepends=True)
    changed = False
    dst = os.path.join(BK, mod, rel)
    if os.path.exists(dst):   # 控えがある＝もう直したファイル。二重に書き換えない
        rows += [[mod, rel, l, o, n, "もう直っている"] for l, o, n in es]; continue
    perline = {}
    for line, old, new in es:
        perline.setdefault(line, {})[old] = new
    for line, d in sorted(perline.items()):
        i = line - 1
        if i >= len(L):
            rows += [[mod, rel, line, o, n, "行が無い"] for o, n in d.items()]; continue
        found = [o for o in d if o in L[i]]
        for o, n in d.items():
            rows.append([mod, rel, line, o, n, ("直した" if not DRY else "直せる") if o in found else "見つからない"])
        if found:   # 同じ行の置き換えは一度に行う（三十→四十 と 二十→三十 が重ならないように）
            rx = re.compile("(?<![0-9０-９〇一二三四五六七八九十百])(?:" + "|".join(re.escape(o) for o in sorted(found, key=len, reverse=True)) + ")")
            L[i] = rx.sub(lambda m: d[m.group(0)], L[i]); changed = True
    if changed and not DRY:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst):
            shutil.copy2(p, dst)
        with open(p, "wb") as f:
            f.write("".join(L).encode(enc))
        nfile += 1
# 長さを比べている文（「〜より少し長く」など）を拾っておく（数字の大小が逆になっていないか後で見る用）
import re
cmp_rows = []
RX = re.compile(r"[^。\\n]{0,40}(?:のものより|よりも?(?:少し|ずっと|ひとまわり)?(?:長|大き|短))[^。\\n]{0,40}")
for (mod, rel) in sorted(by):
    p = os.path.join(ROOT, mod, rel)
    if not os.path.exists(p):
        continue
    try:
        t = open(p, "rb").read().decode("utf-8-sig", "replace")
    except Exception:
        continue
    for i, line in enumerate(t.splitlines(), 1):
        for m in RX.finditer(line):
            cmp_rows.append([mod, rel, i, m.group(0)])
with open(os.path.join(HERE, "サイズの記述_比べている文.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f); w.writerow(["MOD", "ファイル", "行", "文"]); w.writerows(cmp_rows)
with open(os.path.join(HERE, "サイズの記述_直した結果.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f); w.writerow(["MOD", "ファイル", "行", "元", "新", "結果"]); w.writerows(rows)
import collections
c = collections.Counter(r[5] for r in rows)
print("結果:", dict(c), "／書き換えたファイル:", nfile)
if not DRY:
    print("控え:", BK)
