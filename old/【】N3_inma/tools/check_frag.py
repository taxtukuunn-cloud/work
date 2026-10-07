#!/usr/bin/env python3
"""敗北シナリオ断片のチェッカー。使い方: python3 check_frag.py frag/Inma_lose_btl_m1.txt [...]"""
import sys, re

ALLOWED = [
    r"^話者変更,(自分|相手)$",
    r"^セリフ,.+$",
    r"^説明,.+$",
    r"^画像表示,#Inma/Inma_lose_(btl|onani|inochi|onedari)_(m1|m2|m3|e1|e2|e3|boss)\.png,1$",
    r"^画像全削除$",
    r"^フラッシュ,(白|ピンク)$",
    r"^SE,&&(怪しい光SE|注ぐSE)$",
    r"^射精$",
]
BAD_CHARS = set(",$%&#{}<>")

def body_len(lines):
    n = 0
    for l in lines:
        if l.startswith("セリフ,") or l.startswith("説明,"):
            t = l.split(",", 1)[1].replace("\\n", "")
            n += len(t)
    return n

ok_all = True
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\r\n") for l in f]
    errs = []
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if not s:
            continue
        if not any(re.match(p, s) for p in ALLOWED):
            errs.append(f"L{i}: 使えない行: {s[:40]}")
            continue
        if s.startswith("セリフ,") or s.startswith("説明,"):
            t = s.split(",", 1)[1]
            bad = [c for c in t if c in BAD_CHARS]
            if bad:
                errs.append(f"L{i}: 本文に禁止文字 {''.join(sorted(set(bad)))}: {t[:30]}")
    n = body_len(lines)
    if n < 5000:
        errs.append(f"文字数不足: {n}字（5000字以上必要。目標5800字）")
    status = "OK" if not errs else "NG"
    if errs:
        ok_all = False
    print(f"[{status}] {path} 本文 {n}字")
    for e in errs[:30]:
        print("   ", e)
sys.exit(0 if ok_all else 1)
