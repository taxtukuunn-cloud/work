#!/usr/bin/env python3
"""敗北シナリオ（N76〜N105・本編文体）の書式・字数・割合チェック
使い方: python3 check4000.py <file> [...]
- 本文（セリフ・説明。\\n は数えない）の合計 3,400〜4,900字（目標 約4,000字）
- 割合：責め手のセリフ 55〜80%／主人公のセリフ 5〜18%／説明 12〜32%
- ❤ で統一（♡ 禁止）。主人公のセリフの8割以上に❤
- 区画 #導入 #プレイ #結び の順（導入 150〜700字・結び 200〜900字）
"""
import re, sys, os

ALLOWED = {"話者", "セリフ", "説明", "画像", "フラッシュ", "射精", "ウェイト", "ウエイト", "画面色変化", "画面色解除",
           "フェードアウト", "フェードイン", "SE"}
SE_OK = {"&&おっぱいSE", "&&服を脱がすSE", "&&ドア閉まるSE"}
BAD_CHARS = set(",$%&#{}<>;!?")
BAD_WORDS = ["少年", "子供", "子ども", "幼い", "幼げ", "ロリ", "少女", "ショタ", "童顔", "♪", "小柄", "華奢", "すっぽり",
             "小さな体", "男の子", "よい子", "良い子", "♡", "アヘ", "いい子", "赤ちゃん", "おくるみ", "ボウヤ", "坊や"]

def count(b):
    return len(b.replace("\\n", ""))

def check(path, quiet=False):
    ng = []
    lines = open(path, encoding="utf-8-sig").read().splitlines()
    fname = os.path.basename(path)
    route = fname.rsplit(".", 1)[0]
    if not lines or lines[0] != "#導入":
        ng.append("1行目が #導入 ではない")
    if len(lines) < 2 or not lines[1].startswith("画像,"):
        ng.append("2行目が画像行ではない")
    sec, order = None, []
    cnt = {"導入": 0, "プレイ": 0, "結び": 0}
    who = {"責め手": 0, "主人公": 0, "説明": 0}
    pl, ph, speaker = 0, 0, None
    prev_protag = False
    shot = 0
    for i, l in enumerate(lines, 1):
        if l.startswith("#"):
            n = l[1:]
            if n not in cnt:
                ng.append(f"{i}行目: 不明な区画 {l}")
            sec = n; order.append(n); continue
        if not l.strip():
            ng.append(f"{i}行目: 空行"); continue
        if l != l.lstrip():
            ng.append(f"{i}行目: 行頭に空白")
        cmd, _, rest = l.partition(",")
        _pp = prev_protag
        prev_protag = False
        if cmd not in ALLOWED:
            ng.append(f"{i}行目: 使えないコマンド {cmd}"); continue
        if cmd == "射精":
            shot += 1
        if cmd == "SE" and rest.rstrip(",") not in SE_OK:
            ng.append(f"{i}行目: SE は {' '.join(sorted(SE_OK))} だけ")
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
            b = rest
            bad = sorted(set(c for c in b if c in BAD_CHARS))
            if bad:
                ng.append(f"{i}行目: 禁止文字 {' '.join(bad)}")
            for w in BAD_WORDS:
                if w in b:
                    ng.append(f"{i}行目: 禁止語 {w}")
            if cmd == "セリフ" and b.startswith("「"):
                ng.append(f"{i}行目: セリフに「」を付けない")
            if speaker is None and cmd == "セリフ":
                ng.append(f"{i}行目: 話者の前にセリフ")
            n = count(b)
            if sec in cnt:
                cnt[sec] += n
            if cmd == "説明":
                who["説明"] += n
            elif speaker == "相手プレイヤー":
                who["主人公"] += n; pl += 1; ph += ("❤" in b)
                if "\\n" in b and _pp:
                    ng.append(f"{i}行目: 主人公のセリフが続き、2つ目に \\n がある。話者行の抜けでは？（fix_speaker.py で直せる）")
                if n > 90:
                    ng.append(f"{i}行目: 主人公のセリフが長い（{n}字）。話者行の抜けでは？")
                prev_protag = (cmd == "セリフ")
            else:
                who["責め手"] += n
    if order != ["導入", "プレイ", "結び"]:
        ng.append(f"区画の順番が違う {order}")
    tot = sum(cnt.values())
    if not 3700 <= tot <= 4900:
        ng.append(f"合計 {tot}字（3,700〜4,900字。目標4,000）")
    if cnt["導入"] < 150 or cnt["導入"] > 700:
        ng.append(f"導入 {cnt['導入']}字（150〜700）")
    if cnt["結び"] < 200 or cnt["結び"] > 900:
        ng.append(f"結び {cnt['結び']}字（200〜900）")
    r = {k: (v * 100 // tot if tot else 0) for k, v in who.items()}
    for k, lo, hi in [("責め手", 55, 80), ("主人公", 5, 18), ("説明", 12, 32)]:
        if not lo <= r[k] <= hi:
            ng.append(f"{k}の割合 {r[k]}%（{lo}〜{hi}%）")
    if pl and ph < pl * 0.8:
        ng.append(f"主人公のセリフに❤が少ない（{ph}/{pl}）")
    if shot < 2:
        ng.append(f"射精 の行が {shot}（2回以上：カウントダウンの1回目＋得意技だけの2回目）")
    st = "OK" if not ng else "NG"
    print(f"{st} {fname} 合計{tot}（導入{cnt['導入']}/プレイ{cnt['プレイ']}/結び{cnt['結び']}） 責め手{r['責め手']}% 主人公{r['主人公']}% 説明{r['説明']}%")
    for n in ng[:30]:
        print("   -", n)
    return not ng

if __name__ == "__main__":
    ok = all([check(f) for f in sys.argv[1:]])
    sys.exit(0 if ok else 1)
