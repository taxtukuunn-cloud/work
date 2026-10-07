#!/usr/bin/env python3
"""敗北シナリオの抜き出し・確認・差し戻し（全MOD共通）
extract <master.txt> <workdir>   : @敗北_* を workdir/orig/<name>.txt に（インデント除去・末尾の成立3行は除く）
check   <workdir> [name...]       : workdir/new/<name>.txt を確認
splice  <master.txt> <workdir> <out.txt> : new/ の本文を差し戻す（ほかのセクションは一切触らない）
"""
import sys, os, re, json

ALLOWED = {"画像", "話者", "セリフ", "説明", "フラッシュ", "射精", "ウェイト", "画面色変化", "画面色解除", "BGM", "SE", "効果音", "背景", "話者変更", "画像表示"}
BAD = set(",$%&#{}<>;!?")
NG = ["少年", "子供", "子ども", "幼い", "ロリ", "少女", "ショタ", "童", "♪"]
SEC = re.compile(r'(?m)^(@[^\r\n]*)\r?\n')


def split(text):
    parts = SEC.split(text)
    return parts


def tail_start(lines):
    # 末尾の「フラッシュ,白 → 説明,―― … ―― → 弱点付与」を残す
    for i in range(len(lines) - 1, -1, -1):
        s = lines[i].strip()
        if s.startswith("説明,――") and s.endswith("――"):
            j = i
            if j > 0 and lines[j - 1].strip().startswith("フラッシュ"):
                j -= 1
            return j
    for i in range(len(lines) - 1, -1, -1):
        if "弱点付与" in lines[i]:
            return i
    return len(lines)


def body_of(sec_text):
    lines = sec_text.replace("\r\n", "\n").split("\n")
    while lines and not lines[-1].strip():
        lines.pop()
    t = tail_start(lines)
    return lines[:t], lines[t:]


def count(lines):
    n = 0
    for l in lines:
        s = l.strip()
        c, _, b = s.partition(",")
        if c in ("セリフ", "説明"):
            n += len(b.replace("\\n", ""))
    return n


def extract(master, wd):
    t = open(master, encoding="utf-8-sig").read()
    p = split(t)
    os.makedirs(f"{wd}/orig", exist_ok=True)
    meta = {}
    for i in range(1, len(p), 2):
        k = p[i].strip()
        if k.startswith("@敗北_") and k != "@敗北_":
            body, tail = body_of(p[i + 1])
            name = k[1:]
            open(f"{wd}/orig/{name}.txt", "w", encoding="utf-8").write("\n".join(l.strip() for l in body) + "\n")
            sp = sorted({l.strip()[3:] for l in body if l.strip().startswith("話者,")})
            meta[name] = {"chars": count(body), "speakers": sp, "img": [l.strip() for l in body if l.strip().startswith("画像")]}
    json.dump(meta, open(f"{wd}/meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(meta), "sections;", "chars min", min(m["chars"] for m in meta.values()))


def check(wd, names):
    meta = json.load(open(f"{wd}/meta.json", encoding="utf-8"))
    names = names or sorted(meta)
    allok = True
    for n in names:
        errs = []
        f = f"{wd}/new/{n}.txt"
        if not os.path.exists(f):
            print("MISSING", n); allok = False; continue
        lines = [l.rstrip("\n") for l in open(f, encoding="utf-8") if l.strip()]
        for i, l in enumerate(lines, 1):
            c, _, b = l.partition(",")
            if c not in ALLOWED:
                errs.append(f"{i}: 使えないコマンド {l[:30]}")
            if c in ("セリフ", "説明"):
                bb = b.replace("\\n", "")
                if not bb.strip():
                    errs.append(f"{i}: 本文が空")
                bad = sorted(set(ch for ch in bb if ch in BAD))
                if bad:
                    errs.append(f"{i}: 禁止文字 {''.join(bad)}: {bb[:30]}")
                for w in NG:
                    if w in bb:
                        errs.append(f"{i}: 禁止語 {w}")
            if c == "話者" and b not in meta[n]["speakers"]:
                errs.append(f"{i}: 元にない話者 {b}")
        imgs = [l for l in lines if l.startswith("画像")]
        if imgs != meta[n]["img"]:
            errs.append(f"画像行が元と違う: {imgs} / 元 {meta[n]['img']}")
        ch = count(lines)
        if ch < meta[n]["chars"]:
            errs.append(f"字数 {ch} が元 {meta[n]['chars']} より少ない")
        hearts = sum(l.count("♡") for l in lines)
        if errs:
            allok = False
            print("NG", n, *errs, sep="\n  ")
        else:
            print(f"OK {n} 字数={ch}（元{meta[n]['chars']}） ♡={hearts}")
    return allok


def splice(master, wd, out):
    raw = open(master, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    t = raw.decode("utf-8-sig")
    crlf = "\r\n" in t
    p = split(t)
    n = 0
    for i in range(1, len(p), 2):
        k = p[i].strip()
        f = f"{wd}/new/{k[1:]}.txt"
        if k.startswith("@敗北_") and os.path.exists(f):
            old = p[i + 1].replace("\r\n", "\n")
            ind = re.match(r"\s*", [l for l in old.split("\n") if l.strip()][0]).group(0)
            body, tail = body_of(old)
            new = [ind + l.rstrip("\n") for l in open(f, encoding="utf-8") if l.strip()]
            trail = old[len(old.rstrip("\n")):]  # 元の末尾の空行
            p[i + 1] = "\n".join(new + tail) + (trail if trail else "\n")
            n += 1
    s = p[0] + "".join(p[i] + "\n" + p[i + 1] for i in range(1, len(p), 2))
    s = s.replace("\r\n", "\n")
    if crlf:
        s = s.replace("\n", "\r\n")
    open(out, "wb").write((b"\xef\xbb\xbf" if bom else b"") + s.encode("utf-8"))
    print("spliced", n)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "extract":
        extract(sys.argv[2], sys.argv[3])
    elif cmd == "check":
        sys.exit(0 if check(sys.argv[2], sys.argv[3:]) else 1)
    elif cmd == "splice":
        splice(sys.argv[2], sys.argv[3], sys.argv[4])


def readable(wd, out, title):
    import glob
    L = [title + "\n"]
    for f in sorted(glob.glob(f"{wd}/new/*.txt")):
        L.append(f"\n==================== {os.path.basename(f)[:-4]} ====================")
        sp = None
        for l in open(f, encoding="utf-8"):
            l = l.rstrip("\n"); c, _, b = l.partition(",")
            if c == "話者": sp = "僕" if b == "相手プレイヤー" else b.lstrip("%")
            elif c == "セリフ": L.append(f"{sp}「{b.replace(chr(92)+'n','')}」")
            elif c == "説明": L.append(b.replace("\\n", "\n"))
            elif c == "射精": L.append("（射精）")
    open(out, "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__" and sys.argv[1] == "read":
    readable(sys.argv[2], sys.argv[3], sys.argv[4])
