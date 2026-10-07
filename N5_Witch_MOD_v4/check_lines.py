#!/usr/bin/env python3
import json, sys

BAD = set(",$%&#{}<>;!?()")
NTECH = {"m": 3, "e1": 2, "e2": 2, "e3": 2, "boss": 2}
PREP = set()


def strings(o, path=""):
    if isinstance(o, str):
        yield path, o
    elif isinstance(o, list):
        for i, x in enumerate(o):
            yield from strings(x, f"{path}[{i}]")
    elif isinstance(o, dict):
        for k, x in o.items():
            yield from strings(x, f"{path}.{k}")


def check(p):
    key = p.rsplit("/", 1)[-1].split(".")[0]
    errs = []
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return [f"JSONとして読めない: {e}"]
    for k in ["techs", "prep", "summon", "turn_end", "onedari_intro", "onedari", "inochi_first", "inochi_again",
              "inochi_fail", "inochi_trap", "onani_first", "onani_again", "onani_player", "onani_desc", "end", "win", "conv", "flavor"]:
        if k not in d:
            errs.append(f"キーがない: {k}")
    if errs:
        return errs
    if len(d["techs"]) != NTECH[key]:
        errs.append(f"techs の数 {len(d['techs'])}（{NTECH[key]}）")
    for i, t in enumerate(d["techs"]):
        for side in ("player", "monster"):
            v = t.get(side)
            if not (isinstance(v, list) and len(v) == 4 and all(isinstance(x, list) and len(x) == 2 for x in v)):
                errs.append(f"techs[{i}].{side} は [[責め,反応]]×4")
    if key in PREP:
        pr = d["prep"]
        if not (isinstance(pr, dict) and len(pr.get("player", [])) == 2 and len(pr.get("monster", [])) == 2):
            errs.append("prep の形")
    if len(d["onedari"]) != NTECH[key] or not all(len(x) == 3 for x in d["onedari"]):
        errs.append("onedari は [名前,ねだる言葉,返事]×技の数")
    if key == "m":
        if len(d["turn_end"]) != 4:
            errs.append("レンの turn_end は4つ")
        if "quest" not in d:
            errs.append("quest がない")
        else:
            q = d["quest"]
            for k in ["first", "won_before", "prev", "prev_alert", "choices", "decline", "start", "lost_line", "prev_continue", "kaisou"]:
                if k not in q:
                    errs.append(f"quest.{k} がない")
            if "first" in q and not q["first"][0].startswith("説明:"):
                errs.append("quest.first[0] は 説明: で始める")
            if "prev" in q and sorted(q["prev"].keys()) != ["1", "2", "3", "4"]:
                errs.append("quest.prev は 1〜4")
            if "choices" in q and len(q["choices"]) != 3:
                errs.append("quest.choices は3つ")
    for path, s in strings(d):
        s2 = s[3:] if s.startswith("説明:") else s
        bad = [c for c in s2 if c in BAD]
        if bad:
            errs.append(f"{path}: 禁止文字 {''.join(sorted(set(bad)))}: {s2[:30]}")
        if not s2.strip():
            errs.append(f"{path}: 空")
        if len(s2.replace('\\n', '')) > 160 and not path.endswith("flavor"):
            errs.append(f"{path}: 長すぎ（{len(s2)}字）")
    return errs


if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        e = check(p)
        print(("OK " if not e else "NG ") + p)
        for x in e[:40]:
            print("   ", x)
        ok &= not e
    sys.exit(0 if ok else 1)
