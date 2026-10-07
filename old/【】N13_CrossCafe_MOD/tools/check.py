# 使い方: python3 check.py <シナリオファイル...>
# 字数（セリフ・説明の本文のみ）・禁止文字・コマンド名をチェックする
import sys, re
OK_CMDS = {"話者","セリフ","説明","画像","フラッシュ","SE","射精","画像全削除"}
bad_total = 0
for p in sys.argv[1:]:
    text = open(p, encoding="utf-8").read().replace("\r", "")
    n = 0; errs = []
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s: continue
        cmd, _, arg = s.partition(",")
        if cmd not in OK_CMDS:
            errs.append(f"{i}: 使えないコマンド「{cmd}」")
            continue
        if cmd in ("セリフ","説明"):
            if "," in arg: errs.append(f"{i}: 本文に半角カンマ")
            for ch in "$%&#{}<>":
                if ch in arg: errs.append(f"{i}: 本文に禁止文字 {ch}")
            n += len(arg.replace("\\n", ""))
        if cmd == "話者" and arg not in ("自分","相手"):
            errs.append(f"{i}: 話者は 自分 か 相手")
    status = "OK" if n >= 5000 and not errs else "NG"
    if status == "NG": bad_total += 1
    print(f"{status} {p}: {n}字")
    for e in errs[:20]: print("   ", e)
sys.exit(1 if bad_total else 0)
