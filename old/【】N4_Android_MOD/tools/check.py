#!/usr/bin/env python3
"""N4 Android MOD 用チェッカー
usage: python3 check.py <file.txt> [--min 5000]
- セクションごとの本文字数（セリフ・説明・技名表示・アラートの本文のみ）
- 本文中の禁止文字（半角カンマは引数区切りなので本文に2つ目以降の","があれば警告、$ % & # { } < > と半角括弧）
- if の直後が { か / 波括弧の対応 / 単独 else
"""
import re, sys

TEXT_CMDS = ("セリフ", "説明", "技名表示", "アラート")
FORBID = set("$%&#{}<>()")

def main():
    path = sys.argv[1]
    mn = 5000
    if "--min" in sys.argv:
        mn = int(sys.argv[sys.argv.index("--min") + 1])
    lines = open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    errs = []
    counts = {}
    cur = None
    depth = 0
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if not s or s.startswith("//"):
            continue
        if s.startswith("@"):
            cur = s[1:]
            counts[cur] = 0
            if depth != 0:
                errs.append(f"L{i}: セクション開始時に波括弧が閉じていない(depth={depth})")
                depth = 0
            continue
        if s == "{":
            depth += 1
            continue
        if s == "}":
            depth -= 1
            if depth < 0:
                errs.append(f"L{i}: 閉じ括弧が多い")
                depth = 0
            continue
        if s == "}else{":
            if depth <= 0:
                errs.append(f"L{i}: }}else{{ の位置が不正")
            continue
        if s.startswith("else"):
            errs.append(f"L{i}: 単独 else")
        if s.startswith("if,"):
            # 次の非空行が {
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or lines[j].strip() != "{":
                errs.append(f"L{i}: if の次の行が {{ ではない")
        cmd, _, arg = s.partition(",")
        if cmd in TEXT_CMDS:
            if "," in arg:
                errs.append(f"L{i}: 本文に半角カンマ: {s[:40]}")
            bad = [c for c in arg.replace("{$表示用}","") if c in FORBID]
            if bad:
                errs.append(f"L{i}: 本文に禁止文字 {''.join(sorted(set(bad)))}: {s[:40]}")
            body = arg.replace("\\n", "")
            if cur is not None:
                counts[cur] += len(body)
    if depth != 0:
        errs.append(f"EOF: 波括弧が閉じていない(depth={depth})")
    for k, v in counts.items():
        flag = ""
        if k.startswith("敗北_") and v < mn:
            flag = f"  <-- {mn}字未満"
        print(f"{k}: {v}字{flag}")
    if errs:
        print("---- ERRORS ----")
        for e in errs[:200]:
            print(e)
        sys.exit(1)
    print("OK")

if __name__ == "__main__":
    main()
