#!/usr/bin/env python3
"""N1 Host v4 シナリオ／カードのチェッカー
usage: check.py file [file...]
 シナリオ（/scen/ 内）: 導入300〜600字・プレイ6000字以上・結び600字以内・書式
 カード: CRLF・default・if括弧・禁止文字
"""
import sys, re

CODE = "Host"
ALLOWED = {"画像", "話者", "セリフ", "説明", "フラッシュ", "射精", "ウェイト", "##PLAY", "##END"}
SPEAKERS = {"%レン", "%ヒナタ", "%ユウ", "%ソラ", "%暁", "相手プレイヤー"}
BAD = set("$%&#{}<>;")


def body_len(l):
    return len(l.split(",", 1)[1].replace("\\n", "")) if "," in l else 0


def check_scen(path):
    errs = []
    lines = [l.rstrip("\r\n") for l in open(path, encoding="utf-8-sig")]
    lines = [l for l in lines if l.strip()]
    if not lines or not re.match(rf"^画像,#{CODE}/{CODE}_lose_(btl|onani|inochi|onedari)_(m1|m2|m3|e1|e2|e3|boss)\.png,1$", lines[0]):
        errs.append("1行目が画像行ではない")
    if lines.count("##PLAY") != 1 or lines.count("##END") != 1:
        errs.append("##PLAY / ##END がそれぞれ1回ではない")
    part = 0
    n = [0, 0, 0]
    for i, l in enumerate(lines, 1):
        if l == "##PLAY":
            part = 1; continue
        if l == "##END":
            part = 2; continue
        cmd = l.split(",", 1)[0].strip()
        if cmd not in ALLOWED:
            errs.append(f"{i}: 使えないコマンド: {l[:40]}")
            continue
        if cmd in ("セリフ", "説明"):
            body = l.split(",", 1)[1] if "," in l else ""
            if "," in body:
                errs.append(f"{i}: 本文に半角カンマ: {l[:40]}")
            bad = [c for c in body if c in BAD]
            if bad:
                errs.append(f"{i}: 禁止文字 {''.join(set(bad))}: {l[:40]}")
            if not body.strip():
                errs.append(f"{i}: 本文が空")
            n[part] += body_len(l)
        if cmd == "話者":
            sp = l.split(",", 1)[1].strip() if "," in l else ""
            if sp not in SPEAKERS:
                errs.append(f"{i}: 不明な話者 {sp}")
        if cmd == "画像" and not re.match(rf"^画像,#{CODE}/{CODE}_lose_(btl|onani|inochi|onedari)_(m1|m2|m3|e1|e2|e3|boss)\.png,1$", l):
            errs.append(f"{i}: 画像行の形式: {l}")
    if not (300 <= n[0] <= 650):
        errs.append(f"導入の字数 {n[0]}（300〜600字にする）")
    if n[1] < 6000:
        errs.append(f"プレイ描写の字数 {n[1]}（6,000字以上にする）")
    if n[2] > 700:
        errs.append(f"結びの字数 {n[2]}（600字以内にする）")
    return n, errs


def check_card(path):
    errs = []
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8-sig")
    if b"\r\n" not in raw or re.search(rb"[^\r]\n", raw):
        errs.append("改行がCRLFでない箇所あり")
    lines = txt.split("\r\n")
    if lines[0].strip() != "default":
        errs.append("1行目がdefaultでない")
    depth = 0
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith(("if,", "while,", "case,")):
            nxt = lines[i].strip() if i < len(lines) else ""
            if nxt != "{":
                errs.append(f"{i}: if/while/case の次が {{ でない: {s[:40]}")
        if s == "{":
            depth += 1
        elif s == "}":
            depth -= 1
        elif s == "}else{":
            if depth <= 0:
                errs.append(f"{i}: else の位置")
        elif s.startswith("else"):
            errs.append(f"{i}: 単独 else")
        if s.startswith("@"):
            if depth != 0:
                errs.append(f"{i}: セクション開始時に括弧が閉じていない (depth={depth})")
            depth = 0
        if depth < 0:
            errs.append(f"{i}: 閉じ括弧が多い"); depth = 0
        if s.startswith("##"):
            errs.append(f"{i}: 区切り行が残っている")
        for cmd in ("セリフ,", "説明,", "アラート,", "技名表示,"):
            if s.startswith(cmd):
                body = s[len(cmd):]
                if "," in body:
                    errs.append(f"{i}: 本文に半角カンマ: {s[:40]}")
                body2 = re.sub(r"\{\$[^{}]+\}", "", body)
                bad = [c for c in body2 if c in BAD]
                if bad:
                    errs.append(f"{i}: 禁止文字 {''.join(set(bad))}: {s[:40]}")
    if depth != 0:
        errs.append(f"末尾で括弧が閉じていない depth={depth}")
    return errs


if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        if "/scen/" in p:
            n, errs = check_scen(p)
            st = "OK" if not errs else "NG"
            ok &= not errs
            print(f"{st} {p} 導入={n[0]} プレイ={n[1]} 結び={n[2]} 合計={sum(n)}")
            for e in errs[:30]:
                print("   ", e)
        else:
            errs = check_card(p)
            ok &= not errs
            print(("OK " if not errs else "NG ") + p)
            for e in errs[:30]:
                print("   ", e)
    sys.exit(0 if ok else 1)
