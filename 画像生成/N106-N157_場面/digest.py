# -*- coding: utf-8 -*-
"""読む用シナリオ集を28本に分けて、各本の見出し＋冒頭（導入）＋終わり（クライマックス〜結末）だけを出す。
使い方: python3 digest.py <読む用シナリオ集.txt> [冒頭の字数=350] [終わりの字数=1300]"""
import re, sys
p = sys.argv[1]
h = int(sys.argv[2]) if len(sys.argv) > 2 else 350
t = int(sys.argv[3]) if len(sys.argv) > 3 else 1300
txt = open(p, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
lines = txt.split("\n")
heads = []
for i, L in enumerate(lines):
    m = re.match(r"^=+\s*(\S.*?)\s*=*\s*$", L)
    if m and not re.fullmatch(r"=+", L.strip()):
        heads.append((i, m.group(1)))
    elif re.match(r"^【.+】\s*$", L) and i > 0 and re.fullmatch(r"=+", lines[i - 1].strip() or "x"):
        heads.append((i, L.strip()))
n = 0
for k, (i, title) in enumerate(heads):
    end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
    body = "\n".join(x for x in lines[i + 1:end] if x.strip() and not re.fullmatch(r"=+", x.strip())).strip()
    n += 1
    print("\n##### %d %s（%d字）" % (n, title, len(body)))
    print("[冒頭] " + body[:h].replace("\n", " "))
    print("[終わり] " + body[-t:].replace("\n", " "))
if n == 0:
    print("見出し（=== と【】）が見つかりません。ファイルを直接読んでください。")
