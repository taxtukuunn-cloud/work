# -*- coding: utf-8 -*-
"""オナニー場面（*_onanie_*）を「主人公ひとり」の構図にする（2026-09-28 ユーザー決定）
相手が遠くで見ている構図をやめ、相手の人物描写・見ている描写・2人を示すタグを外す。
gen.py が撮る直前にこの変換をかける（prompts\\*.json は書き換えない）。model.json の "solo_onanie": false で旧方式。"""
import json, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PD = os.path.join(HERE, "prompts")

# 相手・見ている構図を示す節（この語を含む区切りは丸ごと外す）
DROP = re.compile(r"watch|far (?:away|in the background)|in the background|small in frame|tiny in frame|distant figure|from afar|"
                  r"not touching him|no physical contact|more than two meters|two different characters|stands? at the doorway|"
                  r"remains? fully in control|one-directional|only receives|never penetrates|the one being dominated|"
                  r"\bsubmissive\b|\bdominant\b|dominant confident|femdom|femboy dominant|\bcmnm\b|\byaoi\b|\bduo\b|two people|"
                  r"slightly shorter than|taller than|shorter than the|solo focus|male focus|in the foreground|main subject|"
                  r"^not wearing |he pleasures himself during the card battle|while the .* (?:watches|only watches)|"
                  r"is alone and touches only himself|\b(?:she|her|herself)\b|\bcfnm\b|clothed female|only the man is naked|"
                  r"^not touching$|\bthe other character\b|^fully clothed$|^not naked$", re.I)
COUNT = re.compile(r"^(?:\d(?:boys?|girls?)|1boy in the foreground|multiple boys|multiple girls|hetero)$", re.I)


HERO_BLOCK = re.compile(r"the (?:naked )?(?:navy|dark blue)[- ]blue?[^:,]*?:\s")
FEM_END = re.compile(r"only the man is naked|the woman keeps all her clothes|clothed female|\bcfnm\b|not touching$", re.I)


def strip_partner_blocks(pos):
    """「相手の名前: 相手の説明…」の塊と、相手の名前そのものを文から外す（N1〜N15 系の書き方）"""
    names = set()
    for m in re.finditer(r"(the [^:]{5,200}?):\s", pos):
        name = ("the " + m.group(1).split(", the ")[-1]) if ", the " in m.group(1) else m.group(1)
        if re.search(r"navy|dark blue", name) or len(name) > 160 or re.search(r"[()]|background|foreground|watch", name):
            continue
        if not re.search(r"haired|\bhair\b|wearing|woman|girl|femboy|maid|android|newhalf|\bin a\b", name):
            continue
        names.add(name)
    for name in sorted(names, key=len, reverse=True):
        # 相手の説明ブロック（名前: … 主人公ブロックの手前まで。無ければ次の場所の説明まで）
        i = pos.find(name + ":")
        if i >= 0:
            j = HERO_BLOCK.search(pos, i + len(name))
            end = j.start() if j else len(pos)
            if not j:
                # 主人公ブロックが後ろに無い形：相手の説明は「, the navy…」か文末まで
                k = pos.find(", the navy", i)
                end = k + 2 if k >= 0 else len(pos)
            pos = pos[:i] + pos[end:]
        pos = pos.replace(name, "")
        first = name.split(", ")[0]
        if len(first) > 12:
            pos = pos.replace(first, "")
    return re.sub(r"(,\s*)+,", ",", pos)


def solo(pos):
    pos = strip_partner_blocks(pos)
    segs = [s.strip() for s in pos.split(",")]
    # 途中に出てくる相手の人数タグ（1girl 等）から、相手の説明の終わり（cfnm 等）までを外す（N16〜N23 系）
    fem = False
    keep = []
    for i, s in enumerate(segs):
        if i > 6 and re.fullmatch(r"1girl|2girls|1other", s.strip(), re.I):
            fem = True; continue
        if fem:
            if FEM_END.search(s):
                if re.search(r"only the man is naked", s, re.I):
                    fem = False          # 相手の説明の最後（N16〜N23 系の決まった書き方）
                continue
            if re.search(r"\b(?:room|shed|hall|greenhouse|garden|forest|cave|corridor|interior|house|bath|street|tower|shrine|temple|bed(?:room)?|floor of|castle|ship|stage|office|dorm|library|lab)\b", s, re.I) and not re.search(r"\b(?:her|she)\b", s):
                fem = False
            else:
                continue
        keep.append(s)
    segs = keep
    out, skip = [], False
    for s in segs:
        if not s:
            continue
        low = s.lower()
        # 相手の人物ブロック（例 "the brown-haired femboy …: adult male" ／ "…not touching him: the tall … maid"）
        if re.match(r"^the (?![^:]*(?:navy|dark blue))[^:]{3,120}:\s", s) or re.search(r"(?:only watching|not touching him):\s", s):
            skip = True
            continue
        if skip:
            # 主人公のブロックか場所の説明に戻ったら終わり
            if re.match(r"^(?:the (?:navy|dark blue)|THE NEW|[a-z ]*(?:interior|room|hall|street|tower|fortress|castle|shrine|forest|"
                        r"cave|bath|onsen|club|office|studio|ship|train|library|lab|clinic|salon|dorm|garden|temple|stage|palace|"
                        r"bedroom|mansion|tavern|casino|circus|police|school|house|camp|village|city|night|evening|sunset)\b)", s, re.I):
                skip = False
            else:
                continue
        if COUNT.match(s) or DROP.search(s):
            continue
        out.append(s)
    txt = ", ".join(out)
    # 品質・安全タグの直後に「ひとり」を入れる
    m = re.search(r"\b(explicit|nsfw|sensitive|general|safe)\b", txt)
    head = "1boy, solo, alone, no other people"
    if m:
        txt = txt[:m.end()] + ", " + head + txt[m.end():]
    else:
        txt = head + ", " + txt
    return txt


def solo_neg(neg):
    add = "2boys, 1girl, 2girls, multiple boys, multiple girls, other person, another person, watcher, audience, people in background, crowd"
    neg = re.sub(r",\s*(?:2boys in foreground|the watcher in foreground|the watcher naked)(?=\s*,|\s*$)", "", neg)
    if "other person, another person, watcher" not in neg:
        neg = neg.rstrip(", ") + ", " + add
    return neg


def main():
    """確認用：python solo_onanie.py <MODコード> で、そのMODのオナニー場面を変換後の文で表示する（ファイルは書き換えない）"""
    mod = sys.argv[1] if len(sys.argv) > 1 else "Knight"
    P = json.load(open(os.path.join(PD, mod + ".json"), encoding="utf-8"))
    for k, e in P.items():
        if "_onanie_" in k:
            print("==", k); print(solo(e["positive"])); print()


if __name__ == "__main__":
    main()
