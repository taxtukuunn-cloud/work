#!/usr/bin/env python3
"""N11 checker.
scene mode (default for scenes/*.txt): count body chars, forbidden chars, allowed commands.
card mode (--card): brace balance, if without {, lone else, forbidden chars in text lines,
attack types, image refs.
"""
import sys, re, os

ALLOWED_SCENE = {"話者", "セリフ", "説明", "画像", "画像全削除", "フラッシュ", "SE", "射精",
                 "主人公攻撃タイプ弱点付与", "ウェイト"}
FORBID = set(",$%&#{}<>;@")
ATTACK_TYPES = set("通常攻撃 おっぱい パイズリ ぱふぱふ フェラ 手コキ 足コキ 脇コキ ハグ ふとももコキ 膝コキ 尻コキ 尻尾コキ 髪コキ キス スマタ 素股 魔法責め 触手 触手コキ 耳責め 乳首責め 強制自慰 パンチラ 息 本番".split())
TEXT_CMDS = ("セリフ", "説明", "アラート", "技名表示")


def body_len(text):
    return len(text.replace("\\n", ""))


def check_scene(path):
    errs = []
    total = 0
    lines = open(path, encoding="utf-8").read().splitlines()
    for i, raw in enumerate(lines, 1):
        l = raw.strip()
        if not l:
            errs.append(f"{i}: 空行")
            continue
        cmd, _, rest = l.partition(",")
        if cmd not in ALLOWED_SCENE:
            errs.append(f"{i}: 使えない命令 {cmd}")
            continue
        if cmd in ("セリフ", "説明"):
            bad = [c for c in rest if c in FORBID]
            if bad:
                errs.append(f"{i}: 本文に禁止文字 {''.join(sorted(set(bad)))} : {rest[:30]}")
            total += body_len(rest)
        if cmd == "主人公攻撃タイプ弱点付与":
            t = rest.split(",")[0]
            if t not in ATTACK_TYPES:
                errs.append(f"{i}: 攻撃タイプ不正 {t}")
    if lines and not lines[-1].startswith("主人公攻撃タイプ弱点付与"):
        errs.append("最終行が弱点付与ではない")
    if not any(x.startswith("画像,#Slime/Slime_lose_") for x in lines):
        errs.append("敗北CGの画像行がない")
    return total, errs


def check_card(path):
    errs = []
    depth = 0
    lines = open(path, encoding="utf-8").read().splitlines()
    prev_if = None
    for i, raw in enumerate(lines, 1):
        l = raw.strip()
        if prev_if is not None:
            if l != "{":
                errs.append(f"{prev_if}: if の次行が {{ ではない")
            prev_if = None
        if l.startswith("if,") or l.startswith("while,"):
            prev_if = i
        if l == "{":
            depth += 1
        elif l == "}":
            depth -= 1
        elif l == "}else{":
            if depth <= 0:
                errs.append(f"{i}: else の位置が不正")
        elif l in ("else", "}else", "else{"):
            errs.append(f"{i}: 単独 else")
        if l.startswith("@"):
            if depth != 0:
                errs.append(f"{i}: セクション開始時に括弧が閉じていない depth={depth}")
                depth = 0
        cmd, _, rest = l.partition(",")
        if cmd in TEXT_CMDS:
            txt = re.sub(r"\{\$[^}]+\}", "", rest)
            bad = [c for c in txt if c in FORBID]
            if bad:
                errs.append(f"{i}: 本文に禁止文字 {''.join(sorted(set(bad)))} : {rest[:30]}")
        if cmd in ("攻撃タイプランダム変更", "攻撃タイプ固定"):
            for t in rest.split(","):
                if t and t not in ATTACK_TYPES:
                    errs.append(f"{i}: 攻撃タイプ不正 {t}")
        if cmd == "if" and rest.startswith("攻撃タイプ,==,"):
            t = rest.split(",")[2]
            if t not in ATTACK_TYPES:
                errs.append(f"{i}: 攻撃タイプ不正 {t}")
        if cmd == "主人公攻撃タイプ弱点付与":
            t = rest.split(",")[0]
            if t not in ATTACK_TYPES:
                errs.append(f"{i}: 攻撃タイプ不正 {t}")
        for m in re.findall(r"#[^,\s]+", l):
            if not re.fullmatch(r"#Slime/Slime_[A-Za-z0-9_]+\.png", m):
                errs.append(f"{i}: 画像参照が不正 {m}")
        if cmd in ("話者変更", "画像表示"):
            errs.append(f"{i}: 非公式コマンド {cmd}")
    if depth != 0:
        errs.append(f"末尾で括弧が閉じていない depth={depth}")
    raw = open(path, "rb").read()
    if raw.replace(b"\r\n", b"").count(b"\n"):
        errs.append("改行コードがCRLFでない")
    if not lines or lines[0].strip() != "default":
        errs.append("1行目が default ではない")
    return errs


def main():
    args = sys.argv[1:]
    card = "--card" in args
    args = [a for a in args if a != "--card"]
    ok_all = True
    for p in args:
        if card:
            errs = check_card(p)
            print(("OK " if not errs else "NG ") + os.path.basename(p))
        else:
            total, errs = check_scene(p)
            if total < 5000:
                errs.append(f"字数不足 {total}字（5000字以上必要）")
            print(("OK " if not errs else "NG ") + f"{os.path.basename(p)} {total if not card else ''}字")
        for e in errs[:40]:
            print("   ", e)
        ok_all &= not errs
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
