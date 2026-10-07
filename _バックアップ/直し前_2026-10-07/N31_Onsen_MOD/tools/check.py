#!/usr/bin/env python3
"""敗北シナリオの書式・字数チェック（N31〜N45 共通）
使い方: python3 check.py <file> [<file> ...]
"""
import re, sys, os

ALLOWED_CMD = {"話者", "セリフ", "説明", "画像", "フラッシュ", "射精", "ウェイト", "画面色変化", "画面色解除"}
BAD_CHARS = set(",$%&#{}<>;!?")
BAD_WORDS = ["少年", "子供", "子ども", "幼い", "幼げ", "ロリ", "少女", "ショタ", "童顔", "♪"]
MIN = {"導入": (350, 600), "プレイ": (6300, None), "結び": (300, 650)}

def count(body):
    return len(body.replace("\\n", ""))

def check(path):
    ng = []
    lines = open(path, encoding="utf-8").read().splitlines()
    fname = os.path.basename(path)
    route = fname.rsplit(".", 1)[0]
    if not lines or lines[0] != "#導入":
        ng.append("1行目が #導入 ではない")
    if len(lines) < 2 or not lines[1].startswith("画像,"):
        ng.append("2行目が画像行ではない")
    sec = None
    counts = {"導入": 0, "プレイ": 0, "結び": 0}
    order = []
    protag_lines = 0
    protag_heart = 0
    speaker = None
    for i, l in enumerate(lines, 1):
        if l.startswith("#"):
            name = l[1:]
            if name not in counts:
                ng.append(f"{i}行目: 不明な区画 {l}")
            sec = name
            order.append(name)
            continue
        if not l.strip():
            ng.append(f"{i}行目: 空行")
            continue
        if l != l.lstrip():
            ng.append(f"{i}行目: 行頭に空白")
        cmd, _, rest = l.partition(",")
        if cmd not in ALLOWED_CMD:
            ng.append(f"{i}行目: 使えないコマンド {cmd}")
            continue
        if cmd == "画像":
            m = re.match(r"#(\w+)/(\w+)_lose_(\w+?)_(\w+)\.png,1$", rest)
            if not m or f"{m.group(3)}_{m.group(4)}" != route:
                ng.append(f"{i}行目: 画像行がファイル名と合わない {rest}")
            continue
        if cmd == "話者":
            speaker = rest
            if not (rest == "相手プレイヤー" or rest.startswith("%")):
                ng.append(f"{i}行目: 話者の書き方 {rest}")
            continue
        if cmd in ("セリフ", "説明"):
            body = rest
            bad = sorted(set(c for c in body if c in BAD_CHARS))
            if bad:
                ng.append(f"{i}行目: 禁止文字 {' '.join(bad)}")
            for w in BAD_WORDS:
                if w in body:
                    ng.append(f"{i}行目: 禁止語 {w}")
            if body.startswith("「") and cmd == "セリフ":
                ng.append(f"{i}行目: セリフに「」を付けない")
            if sec in counts:
                counts[sec] += count(body)
            if cmd == "セリフ" and speaker == "相手プレイヤー":
                protag_lines += 1
                if "♡" in body:
                    protag_heart += 1
    if order != ["導入", "プレイ", "結び"]:
        ng.append(f"区画の順番が違う {order}")
    for k, (lo, hi) in MIN.items():
        if counts[k] < lo:
            ng.append(f"{k}が短い {counts[k]}字（{lo}字以上）")
        if hi and counts[k] > hi:
            ng.append(f"{k}が長い {counts[k]}字（{hi}字まで）")
    if protag_lines and protag_heart < protag_lines * 0.8:
        ng.append(f"主人公のセリフに♡が少ない（{protag_heart}/{protag_lines}）")
    status = "OK" if not ng else "NG"
    print(f"{status} {fname} 導入{counts['導入']} プレイ{counts['プレイ']} 結び{counts['結び']} 合計{sum(counts.values())}")
    for n in ng[:30]:
        print("   -", n)
    return not ng

if __name__ == "__main__":
    files = sys.argv[1:]
    ok = all([check(f) for f in files])
    sys.exit(0 if ok else 1)
