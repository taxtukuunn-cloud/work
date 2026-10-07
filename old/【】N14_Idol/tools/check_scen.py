#!/usr/bin/env python3
"""N14 敗北シナリオ本文チェッカー。
使い方: python3 check_scen.py <file> [<file>...]
- 許可コマンドのみか / 本文の禁止文字 / 字数（セリフ・説明の本文のみ）を確認する。
"""
import sys, re

ALLOWED_EXACT = {"話者,自分", "話者,相手", "CG", "射精", "SE,&&怪しい光SE", "SE,&&注ぐSE",
                 "SE,&&キスエフェクト", "フラッシュ,ピンク", "フラッシュ,白"}
FORBIDDEN = set(",$%&#{}<>,")  # 半角カンマは本文先頭の区切り以外禁止
MIN_CHARS = 5200

def check(path):
    errs, n, cg, climax = [], 0, 0, 0
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\r\n") for l in f]
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            continue
        if s in ALLOWED_EXACT:
            if s == "CG":
                cg += 1
            if s == "射精":
                climax += 1
            continue
        m = re.match(r"^(セリフ|説明),(.*)$", s)
        if not m:
            errs.append(f"{i}: 許可されていない行: {s[:40]}")
            continue
        body = m.group(2)
        bad = [c for c in body if c in FORBIDDEN]
        if bad:
            errs.append(f"{i}: 本文に禁止文字 {''.join(sorted(set(bad)))}: {body[:30]}")
        if body.count("\\n") > 2:
            errs.append(f"{i}: 1行の改行が多すぎる（\\n は2つまで）")
        n += len(body.replace("\\n", ""))
    if cg != 1:
        errs.append(f"CG 行は1回だけ（現在 {cg}）")
    if climax < 2:
        errs.append(f"射精 行（絶頂）が2回未満（現在 {climax}）")
    if n < MIN_CHARS:
        errs.append(f"字数不足: {n} 字（{MIN_CHARS} 字以上必要）")
    return n, errs

if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        n, errs = check(p)
        status = "OK" if not errs else "NG"
        print(f"[{status}] {p}: {n} 字")
        for e in errs:
            print("   ", e)
        ok &= not errs
    sys.exit(0 if ok else 1)
