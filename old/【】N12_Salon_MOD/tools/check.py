#!/usr/bin/env python3
"""Scenario / card checker for Salon MOD.
usage: check.py file [file...]   (scenario body files or card txt)
"""
import sys, re

ALLOWED = {"画像", "話者", "セリフ", "説明", "フラッシュ", "射精", "ウェイト", "画面色変化", "画面色解除"}
SPEAKERS = {"%カレン", "%エマ", "%ココ", "%ルル", "%セラ", "相手プレイヤー", "自分", "相手", "自分プレイヤー"}
BAD = set("$%&#{}<>;")

def count_body(lines):
    n = 0
    for l in lines:
        if l.startswith("セリフ,") or l.startswith("説明,"):
            n += len(l.split(",", 1)[1].replace("\\n", ""))
    return n

def check_scen(path):
    errs = []
    lines = [l.rstrip("\r\n") for l in open(path, encoding="utf-8-sig")]
    lines = [l for l in lines if l.strip()]
    if not lines or not lines[0].startswith("画像,#Salon/Salon_lose_"):
        errs.append("1行目が画像行ではない")
    for i, l in enumerate(lines, 1):
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
        if cmd == "話者":
            sp = l.split(",", 1)[1].strip() if "," in l else ""
            if sp not in SPEAKERS:
                errs.append(f"{i}: 不明な話者 {sp}")
        if cmd == "画像" and not re.match(r"^画像,#Salon/Salon_lose_(btl|onani|inochi|onedari)_(m1|m2|m3|e1|e2|e3|boss)\.png,1$", l):
            errs.append(f"{i}: 画像行の形式: {l}")
    n = count_body(lines)
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
        if s.startswith("if,") or s.startswith("while,") or s.startswith("case,"):
            nxt = lines[i].strip() if i < len(lines) else ""
            if nxt != "{":
                errs.append(f"{i}: if/case の次が {{ でない: {s[:40]}")
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
            errs.append(f"{i}: 閉じ括弧が多い")
            depth = 0
        for cmd in ("セリフ,", "説明,", "アラート,", "技名表示,"):
            if s.startswith(cmd):
                body = s[len(cmd):]
                if "," in body:
                    errs.append(f"{i}: 本文に半角カンマ: {s[:40]}")
                body2 = re.sub(r"\{\$[^{}]+\}", "", body)
                bad = [c for c in body2 if c in BAD]
                if bad:
                    errs.append(f"{i}: 禁止文字 {''.join(set(bad))}: {s[:40]}")
        if s.startswith("選択肢生成,"):
            pass
    if depth != 0:
        errs.append(f"末尾で括弧が閉じていない depth={depth}")
    return errs

if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        if "/scen/" in p:
            n, errs = check_scen(p)
            status = "OK" if (n >= 5000 and not errs) else "NG"
            if status == "NG":
                ok = False
            print(f"{status} {p} 字数={n}")
            for e in errs[:30]:
                print("   ", e)
        else:
            errs = check_card(p)
            print(("OK " if not errs else "NG ") + p)
            for e in errs[:30]:
                print("   ", e)
            if errs:
                ok = False
    sys.exit(0 if ok else 1)
