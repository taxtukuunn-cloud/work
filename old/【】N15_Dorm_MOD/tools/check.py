#!/usr/bin/env python3
"""N15 Dorm scenario checker. usage: python3 check.py scen/*.txt"""
import re, sys, json
SPEAKERS = {"サクラ", "ハナ", "マナ", "サキ", "ミズキ", "主人公"}
BAD = set(",$%&#{}<>;\\/")
LINE_RE = re.compile(r"^(サクラ|ハナ|マナ|サキ|ミズキ|主人公)「(.*)」$")

def parse(path):
    items, errs = [], []
    for i, raw in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        s = raw.strip()
        if not s:
            continue
        if s in ("[CG]", "[絶頂]"):
            items.append((s, None)); continue
        m = LINE_RE.match(s)
        if m:
            items.append((m.group(1), m.group(2)))
            body = m.group(2)
        elif s.startswith("＊"):
            body = s[1:]
            items.append(("＊", body))
        else:
            errs.append(f"L{i}: 不正な行: {s[:40]}"); continue
        bad = [c for c in body if c in BAD]
        if bad:
            errs.append(f"L{i}: 禁止文字 {''.join(sorted(set(bad)))}: {body[:30]}")
        if len(body) > 130:
            errs.append(f"L{i}: 長すぎ({len(body)}字)")
        if "「" in body or "」" in body:
            errs.append(f"L{i}: 本文内に「」: {body[:30]}")
    return items, errs

def count(items):
    return sum(len(b) for k, b in items if b)

if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        if p.endswith(".json"):
            try:
                d = json.load(open(p, encoding="utf-8"))
                txt = json.dumps(d, ensure_ascii=False)
                def walk(o):
                    if isinstance(o, str):
                        b = [c for c in o if c in BAD]
                        if b: print(f"{p}: 禁止文字 {set(b)} in {o[:30]}")
                    elif isinstance(o, dict):
                        for v in o.values(): walk(v)
                    elif isinstance(o, list):
                        for v in o: walk(v)
                walk(d); print(f"{p}: JSON OK")
            except Exception as e:
                ok = False; print(f"{p}: JSON ERROR {e}")
            continue
        items, errs = parse(p)
        n = count(items)
        cg = sum(1 for k, _ in items if k == "[CG]")
        cl = sum(1 for k, _ in items if k == "[絶頂]")
        st = "OK" if n >= 5000 and not errs and cg >= 1 and cl >= 2 else "NG"
        if st == "NG": ok = False
        print(f"{st} {p}: {n}字 CG{cg} 絶頂{cl} エラー{len(errs)}")
        for e in errs[:10]:
            print("   ", e)
    sys.exit(0 if ok else 1)
