#!/usr/bin/env python3
"""構造を保ったままの敗北シナリオ書き直し用（Rosetta・Ruin・Yakai など if を含むセクション向け）
extract <master> <wd> <セクション名,...> [--split 正規表現]
   セクション本体を行のまま（インデント付き）wd/orig/<名前>.txt に書く。
   --split を付けると、行頭（インデント除く）がその正規表現に合う行でさらに分割する（名前_01, _02 ...）。
check <wd> [名前...]   話者・セリフ・説明 以外の行（空行除く）が元と同じ並びか、字数が元以上か、禁止文字を確認
splice <master> <wd> <out>
"""
import sys, os, re, json

TEXT = {"話者", "話者変更", "セリフ", "説明"}
BAD = set(",$%&#{}<>;!?")
NG = ["少年", "子供", "子ども", "幼い", "ロリ", "少女", "ショタ", "童", "♪"]
SEC = re.compile(r'(?m)^(@[^\r\n]*)\r?\n')


def cmd(l):
    return l.strip().split(",", 1)[0]


def count(lines):
    n = 0
    for l in lines:
        c, _, b = l.strip().partition(",")
        if c in ("セリフ", "説明"):
            n += len(b.replace("\\n", ""))
    return n


def skeleton(lines):
    return [l.strip() for l in lines if l.strip() and cmd(l) not in TEXT]


def extract(master, wd, names, split=None):
    t = open(master, encoding="utf-8-sig").read().replace("\r\n", "\n")
    p = SEC.split(t)
    os.makedirs(f"{wd}/orig", exist_ok=True)
    meta = {"master": master, "units": []}
    for i in range(1, len(p), 2):
        k = p[i].strip()
        if k[1:] not in names:
            continue
        body = p[i + 1]
        stripped = body.rstrip("\n")
        trail = body[len(stripped):]
        lines = stripped.split("\n")
        chunks = [[]]
        for l in lines:
            if split and re.match(split, l.strip()) and chunks[-1]:
                chunks.append([])
            chunks[-1].append(l)
        units = []
        for j, ch in enumerate(chunks):
            name = k[1:] if len(chunks) == 1 else f"{k[1:]}_{j:02d}"
            open(f"{wd}/orig/{name}.txt", "w", encoding="utf-8").write("\n".join(ch) + "\n")
            units.append({"name": name, "chars": count(ch), "skel": skeleton(ch)})
        meta["units"].append({"section": k, "trail": trail, "chunks": units})
    json.dump(meta, open(f"{wd}/meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for u in meta["units"]:
        for c in u["chunks"]:
            print(c["name"], c["chars"])


def check(wd, names):
    meta = json.load(open(f"{wd}/meta.json", encoding="utf-8"))
    ok = True
    for u in meta["units"]:
        for c in u["chunks"]:
            n = c["name"]
            if names and n not in names:
                continue
            f = f"{wd}/new/{n}.txt"
            if not os.path.exists(f):
                print("MISSING", n); ok = False; continue
            lines = open(f, encoding="utf-8").read().rstrip("\n").split("\n")
            errs = []
            sk = skeleton(lines)
            if sk != c["skel"]:
                for a, (x, y) in enumerate(zip(sk + ["<END>"] * 5, c["skel"] + ["<END>"] * 5)):
                    if x != y:
                        errs.append(f"構造行が元と違う（{a+1}番目の構造行）: 新『{x[:40]}』 元『{y[:40]}』")
                        break
            for i, l in enumerate(lines, 1):
                cc, _, b = l.strip().partition(",")
                if cc in ("セリフ", "説明"):
                    bb = b.replace("\\n", "")
                    if not bb.strip():
                        errs.append(f"{i}: 本文が空")
                    bad = sorted(set(ch for ch in bb if ch in BAD))
                    if bad:
                        errs.append(f"{i}: 禁止文字 {''.join(bad)}: {bb[:30]}")
                    for w in NG:
                        if w in bb:
                            errs.append(f"{i}: 禁止語 {w}")
            ch = count(lines)
            if ch < c["chars"]:
                errs.append(f"字数 {ch} が元 {c['chars']} より少ない")
            if errs:
                ok = False
                print("NG", n, *errs, sep="\n  ")
            else:
                print(f"OK {n} 字数={ch}（元{c['chars']}）")
    return ok


def splice(master, wd, out):
    meta = json.load(open(f"{wd}/meta.json", encoding="utf-8"))
    raw = open(master, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    t = raw.decode("utf-8-sig")
    crlf = "\r\n" in t
    p = SEC.split(t.replace("\r\n", "\n"))
    bysec = {u["section"]: u for u in meta["units"]}
    n = 0
    for i in range(1, len(p), 2):
        k = p[i].strip()
        if k in bysec:
            u = bysec[k]
            parts = [open(f"{wd}/new/{c['name']}.txt", encoding="utf-8").read().rstrip("\n") for c in u["chunks"]]
            p[i + 1] = "\n".join(parts) + u["trail"]
            n += 1
    s = p[0] + "".join(p[i] + "\n" + p[i + 1] for i in range(1, len(p), 2))
    if crlf:
        s = s.replace("\n", "\r\n")
    open(out, "wb").write((b"\xef\xbb\xbf" if bom else b"") + s.encode("utf-8"))
    print("spliced", n)


if __name__ == "__main__":
    a = sys.argv
    if a[1] == "extract":
        split = None
        if "--split" in a:
            k = a.index("--split"); split = a[k + 1]; a = a[:k] + a[k + 2:]
        extract(a[2], a[3], a[4].split(","), split)
    elif a[1] == "check":
        sys.exit(0 if check(a[2], a[3:]) else 1)
    elif a[1] == "splice":
        splice(a[2], a[3], a[4])
