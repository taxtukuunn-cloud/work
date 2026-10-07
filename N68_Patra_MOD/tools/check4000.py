#!/usr/bin/env python3
"""N61〜N75 敗北シナリオの書式・字数・割合チェック（本編の文体・1本 約4,000字）
使い方: python3 check4000.py scen/*.txt   （tools フォルダで実行。cfg.py の話者表を読む）
"""
import re, sys, os, importlib.util

ALLOWED = {"話者", "セリフ", "説明", "画像", "フラッシュ", "射精", "ウエイト", "ウェイト", "フェードイン", "フェードアウト"}
BAD_CHARS = set(",$%&#{}<>;!?()")
BAD_WORDS = ["少年", "子供", "子ども", "幼い", "幼げ", "ロリ", "少女", "ショタ", "童顔", "♪", "♡", "小柄", "華奢", "【未記入】"]
TOTAL = (3700, 4900)
RATIO = {"e": (0.55, 0.80), "h": (0.05, 0.18), "d": (0.12, 0.32)}

here = os.path.dirname(os.path.abspath(sys.argv[1])) if len(sys.argv) > 1 else "."
cfgp = os.path.join(os.path.dirname(here), "cfg.py")
spec = importlib.util.spec_from_file_location("cfg", cfgp)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
SPK = {s[0] for s in m.CFG["speakers"]} | {"相手プレイヤー"}
CODE = m.CFG["code"]


def check(path):
    ng = []
    route = os.path.basename(path)[:-4]
    lines = open(path, encoding="utf-8").read().splitlines()
    if not lines or lines[0] != "#導入":
        ng.append("1行目が #導入 ではない")
    if len(lines) < 2 or lines[1] != f"画像,#{CODE}/{CODE}_lose_{route}.png,1":
        ng.append(f"2行目は 画像,#{CODE}/{CODE}_lose_{route}.png,1")
    secs = [l for l in lines if l.startswith("#")]
    if secs != ["#導入", "#プレイ", "#結び"]:
        ng.append(f"区画が #導入/#プレイ/#結び でない: {secs}")
    c = {"e": 0, "h": 0, "d": 0}
    sp = None
    hero_lines = hero_heart = 0
    for i, l in enumerate(lines, 1):
        if l.startswith("#"):
            continue
        if not l.strip() or l != l.strip():
            ng.append(f"{i}行目: 空行か前後の空白")
            continue
        cmd, _, rest = l.partition(",")
        if cmd not in ALLOWED:
            ng.append(f"{i}行目: 使えないコマンド {cmd}")
            continue
        if cmd == "話者":
            if rest not in SPK:
                ng.append(f"{i}行目: 話者が話者表にない {rest}")
            sp = rest
        elif cmd in ("セリフ", "説明"):
            bad = sorted(set(ch for ch in rest if ch in BAD_CHARS))
            if bad:
                ng.append(f"{i}行目: 半角記号 {bad}")
            for w in BAD_WORDS:
                if w in rest:
                    ng.append(f"{i}行目: 使わない語 {w}")
            n = len(rest.replace("\\n", ""))
            if cmd == "説明":
                c["d"] += n
            elif sp == "相手プレイヤー":
                c["h"] += n
                hero_lines += 1
                hero_heart += "❤" in rest
            else:
                if sp is None:
                    ng.append(f"{i}行目: 話者の前のセリフ")
                c["e"] += n
    tot = sum(c.values())
    if not TOTAL[0] <= tot <= TOTAL[1]:
        ng.append(f"合計 {tot}字（{TOTAL[0]}〜{TOTAL[1]}）")
    for k, (a, b) in RATIO.items():
        r = c[k] / tot if tot else 0
        if not a <= r <= b:
            ng.append(f"割合 {k}={r:.0%}（{a:.0%}〜{b:.0%}）")
    if lines.count("射精") < 1:
        ng.append("射精の行がない")
    if hero_lines and hero_heart / hero_lines < 0.5:
        ng.append("主人公のセリフに❤が少ない")
    return tot, c, ng


if __name__ == "__main__":
    bad = 0
    for p in sys.argv[1:]:
        tot, c, ng = check(p)
        st = "OK" if not ng else "NG"
        bad += bool(ng)
        print(f"{st} {os.path.basename(p)} {tot}字 責め手{c['e']} 主人公{c['h']} 説明{c['d']}")
        for x in ng[:12]:
            print("   -", x)
    print("NG件数", bad)
    sys.exit(1 if bad else 0)
