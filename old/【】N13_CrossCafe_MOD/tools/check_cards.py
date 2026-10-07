import sys, re, glob, os
D = sys.argv[1]
TYPES = set("通常攻撃 おっぱい パイズリ ぱふぱふ フェラ 手コキ 足コキ 脇コキ ハグ ふとももコキ 膝コキ 尻コキ 尻尾コキ 髪コキ キス スマタ 素股 魔法責め 触手 触手コキ 耳責め 乳首責め 強制自慰 パンチラ 息 本番".split())
secs_by_card = {}; errs = []; imgs = set()
files = sorted(glob.glob(D + "/Card/*.txt"))
for f in files:
    raw = open(f, "rb").read()
    if b"\r\n" not in raw or re.search(rb"[^\r]\n", raw): errs.append(f"{f}: CRLFでない")
    lines = raw.decode("utf-8").split("\r\n")
    if lines[0] != "default": errs.append(f"{f}: 1行目がdefaultでない")
    name = os.path.basename(f)[:-4]; secs = {}; cur = None; depth = 0
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if s.startswith("@"):
            if depth: errs.append(f"{name}:{i} 括弧が閉じていない（{cur}）")
            cur = s[1:]; secs[cur] = i; depth = 0; continue
        if not s: continue
        if s == "{": depth += 1
        elif s == "}": depth -= 1
        elif s == "}else{":
            if depth < 1: errs.append(f"{name}:{i} else位置")
        if depth < 0: errs.append(f"{name}:{i} 閉じ括弧過多"); depth = 0
        cmd, _, arg = s.partition(",")
        if cmd in ("if",):
            nxt = lines[i].strip() if i < len(lines) else ""
            if nxt != "{": errs.append(f"{name}:{i} ifの次が{{でない")
        if s == "else" or s.startswith("else,"): errs.append(f"{name}:{i} 単独else")
        if cmd in ("セリフ", "説明", "アラート") or (cmd == "効果設定" and ",explain," in s):
            body = arg if cmd != "効果設定" else s.split(",", 3)[3]
            if "," in body: errs.append(f"{name}:{i} 本文に半角カンマ")
            b2 = body.replace("{$表示用}", "")
            for ch in "$%&#{}<>":
                if ch in b2: errs.append(f"{name}:{i} 本文に禁止文字{ch}")
        if cmd in ("攻撃タイプランダム変更", "攻撃タイプ固定"):
            for t in arg.split(","):
                if t not in TYPES: errs.append(f"{name}:{i} 攻撃タイプ不明 {t}")
        if cmd == "if" and arg.startswith("攻撃タイプ,==,"):
            if arg.split(",")[2] not in TYPES: errs.append(f"{name}:{i} 攻撃タイプ不明")
        if cmd == "主人公攻撃タイプ弱点付与" and arg.split(",")[0] not in TYPES: errs.append(f"{name}:{i} 弱点タイプ不明")
        for m in re.findall(r"#CrossCafe/([\w]+\.png)", s): imgs.add(m)
        if "#" in s and "#CrossCafe/" not in s and cmd not in ("セリフ","説明"): errs.append(f"{name}:{i} 画像参照の形")
    if depth: errs.append(f"{name}: 最後の括弧が閉じていない")
    for sname in list(secs):
        if not sname.endswith("_街バトル") and sname != "初期設定" and sname + "_街バトル" not in secs:
            errs.append(f"{name}: {sname} の _街バトル 受け口なし")
    secs_by_card[name] = secs
for f in files:
    name = os.path.basename(f)[:-4]
    for l in open(f, encoding="utf-8"):
        m = re.match(r"\s*外部イベント実行,Card/(\w+),(\S+)", l)
        if m and m.group(2) not in secs_by_card.get(m.group(1), {}):
            errs.append(f"{name}: 呼び出し先なし {m.group(1)} {m.group(2)}")
        m = re.match(r"\s*イベント実行,(\S+)", l)
        if m and m.group(1) not in secs_by_card[name]:
            errs.append(f"{name}: イベント実行先なし {m.group(1)}")
print("\n".join(errs) if errs else "エラーなし")
print("画像", len(imgs)); print(" ".join(sorted(imgs)))
