# -*- coding: utf-8 -*-
"""男の娘キャラを女性寄りにするプロンプト修正 v2（2026-09-26）
必ず prompts_男の娘修正前\ の元ファイルから作り直す（何回実行しても同じ結果）。
・単独の絵（主人公が写らない：立ち絵・魔法など）…顔も体つきも女性寄りに
・Auction の場面は先頭に「紺髪の男が透けドレス、相手は自分の服」を入れる（Auction_lose_onedari_e1 で服が入れ替わったため）
・主人公と一緒の場面 …顔だけ女性寄りに（体つきまで女性寄りにすると、主人公と服や役が入れ替わり、
  責め手が小柄に見えたため＝v1 の Auction_lose_btl_boss）。役の入れ替わりを避けるタグも足す
"""
import json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
MODS = ["Android", "Auction", "Circle", "Gym", "Inma", "Kitsune", "Knight", "Maid", "Ninja", "Summoner"]
OLD = "mature face, sharp adult features"
NEW_SOLO = ("otoko no ko, trap, very feminine, beautiful feminine face, pretty face, long eyelashes, soft jawline, "
            "light makeup, glossy lips, narrow shoulders, slender, elegant adult beauty")
NEW_SCENE = "mature face, beautiful feminine face, long eyelashes, light makeup, glossy lips"
NEG_SOLO = "masculine face, manly, square jaw, thick eyebrows, facial hair, stubble, broad shoulders, muscular"
NEG_SCENE = "facial hair, stubble, thick eyebrows, square jaw, role reversal, reverse roles, receiver penetrating, receiver on top, receiver dominant"
NEG_EXTRA = {  # MODごとの服の入れ替わり防止（場面のみ）
    "Auction": ("vest on the navy-haired man, suit on the navy-haired man, trousers on the navy-haired man, monocle on the navy-haired man, "
                "white noble clothes on the navy-haired man, white cloak on the navy-haired man, navy-haired man penetrating, "
                "navy-haired man's penis inserted, chastity device on the attacker, sheer dress on the attacker, "
                "the attacker wearing lingerie, the attacker kneeling, long hair man being penetrated"),
}
POS_EXTRA = {  # MODごとに場面の先頭へ入れる服の指定（場面のみ）
    "Auction": ("the navy-haired man wears the sheer white chiffon dress, red ribbon choker and white garter stockings, "
                "the other man stays fully dressed in his own dark vest or noble clothes with trousers"),
}
bak = os.path.join(HERE, "prompts_男の娘修正前")
os.makedirs(bak, exist_ok=True)

def add_neg(neg, add):
    have = set(x.strip() for x in neg.split(","))
    extra = [x.strip() for x in add.split(",") if x.strip() and x.strip() not in have]
    return neg.rstrip(", ") + (", " + ", ".join(extra) if extra else "")

for m in MODS:
    p = os.path.join(HERE, "prompts", m + ".json")
    b = os.path.join(bak, m + ".json")
    if not os.path.exists(b):
        shutil.copy2(p, b)
    P = json.load(open(b, encoding="utf-8"))
    ns = nc = 0
    for k, v in P.items():
        if OLD not in v["positive"]:
            continue
        if ", solo," not in v["positive"]:
            v["positive"] = v["positive"].replace(OLD, NEW_SCENE)
            v["negative"] = add_neg(v["negative"], NEG_SCENE + (", " + NEG_EXTRA[m] if m in NEG_EXTRA else ""))
            if m in POS_EXTRA:
                v["positive"] = POS_EXTRA[m] + ", " + v["positive"]
            nc += 1
        else:
            v["positive"] = v["positive"].replace(OLD, NEW_SOLO)
            v["negative"] = add_neg(v["negative"], NEG_SOLO)
            ns += 1
    json.dump(P, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("%s: 単独 %d件・場面 %d件を修正" % (m, ns, nc))
