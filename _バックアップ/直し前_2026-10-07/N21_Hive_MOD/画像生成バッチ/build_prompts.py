# -*- coding: utf-8 -*-
"""N21 蜂の女王の巣（Hive）画像プロンプト生成 → hive_prompts.json（51枚）
登場人物は全員20歳以上の成人。個人利用のみ。N20 Vampire の build_prompts.py と同じ書き方。
N20 で崩れた点の対策を最初から入れている：
 - 乳首舐めで男女が逆転 → 「he lies on his back… she bends down and licks the nipple on his flat male chest」＋ COVER ＋ ネガティブ
 - オナニーで手がペニスに → 両手とも胸より上／後ろ、ペニスは触れずに立っているだけ、と明記
 - 女性の下半身が裸 → COVER
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_CORE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, "
            "child, loli, shota, boy, young, teenage, underage, childlike, child body, youthful body, baby face, round face, chubby cheeks, "
            "short limbs, big head, chibi, small body, petite male, petite female, muscular, abs, pectorals, bara, hairy, "
            "blood, bleeding, wound, gore, needle, syringe, stinger, injection, leash, extra legs, three legs, four legs, "
            "eyes visible on the man, 2boys, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies, "
            "insect body, giant insect, bee monster, larva")
NEG_ARMS = ", extra arms"          # ワスプ以外に付ける
NEG_SOLO = ", 2girls, twins, same face"
NEG_NOFUTA = ", futanari, penis on the woman, woman with penis"
NEG_SCENE = (", pussy, vagina, breasts on the man, long hair on the man, blonde hair on the man, brown hair on the man, "
             "black hair on the man, orange hair on the man, blue hair on the woman, antennae on the man, insect wings on the man, "
             "wings on the man, chitin armor on the man, apron on the man, dress on the man, crown on the man, clothes on the man, "
             "naked woman, nude woman, exposed breasts, breasts out, nipples on the woman, man sucking breast, man licking breast, "
             "woman nude from the waist down")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, strap-on"
NEG_ONANI = (", woman touching him, hetero sex, hands on him, woman masturbating, girl masturbating, penis on the woman, "
             "hand on penis, holding penis, handjob, stroking penis, penis grab, hand near penis, masturbating penis, hand on crotch")

ROOM = ("inside a giant beehive, glowing golden hexagonal honeycomb walls made of beeswax, dripping golden honey, "
        "warm amber light, floating pollen, detailed background")

PROT = ("1boy, faceless male, navy blue hair, short messy hair, hair over eyes, bangs covering eyes, "
        "adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, lean, "
        "not muscular, defined jawline, adam's apple, collarbones, flat male chest, "
        "ordinary human man with no antennae and no wings, nude male, completely naked, penis, he is a head shorter than her")
TUBE = ("a very thin flexible golden tube inserted into the tip of his penis, urethral insertion, golden jelly glistening at the tip, "
        "no needle")
JELLY = "thick glistening golden royal jelly"
COVER = "her dress fully covers her chest and legs, she keeps her clothes on, only the man is naked"

CH = {
    "m": dict(seed="APIS",
              tags="1girl, bee girl, queen bee, antennae on her forehead, large translucent insect wings, adult woman, mature female, "
                   "tall woman, blonde hair, long curly hair, amber eyes, yellow and black royal dress with a high collar, "
                   "gold crown, motherly smile, large breasts",
              name="the tall blonde queen bee in a yellow and black royal dress"),
    "e1": dict(seed="BEE",
               tags="1girl, bee girl, antennae, small insect wings, adult woman, brown hair, ponytail, amber eyes, "
                    "yellow and brown work uniform with rolled sleeves, work gloves, cheerful smile, medium breasts",
               name="the brown-haired worker bee girl in a yellow and brown work uniform"),
    "e2": dict(seed="WASP",
               tags="1girl, wasp girl, antennae, insect wings, adult woman, black hair, short hair, red eyes, "
                    "black and yellow chitin armor covering her body, four arms, two human arms and two extra black chitin arms "
                    "growing from her back, aggressive grin, medium breasts",
               name="the black-haired wasp girl in black chitin armor with four arms"),
    "e3": dict(seed="HONEY",
               tags="1girl, bee girl, antennae, small insect wings, adult woman, orange hair, long wavy hair, gold eyes, "
                    "cream dress with a honey-soaked apron, honey dripping, sweet smile, large breasts",
               name="the orange-haired bee girl in a honey-soaked apron"),
    "boss": dict(seed="MELISSA",
                 tags="1girl, bee girl, princess, antennae, large insect wings, adult woman, tall woman, platinum blonde hair, "
                      "very long straight hair, amber eyes, white and gold royal dress, gold tiara, haughty smile, large breasts",
                 name="the tall platinum-haired bee princess in a white and gold dress"),
}

PL = {
    "royalcell": "royal chamber, a large golden hexagonal beeswax cradle like a bed",
    "throne":    "queen's hall, huge beeswax throne on hexagonal steps",
    "nuptial":   "nuptial chamber, golden silk bedding beside the royal cradle",
    "honeystore": "honey storehouse, hexagonal honey cells stacked up to the ceiling, some sealed with wax",
    "pollen":    "pollen storehouse, golden pollen dust floating in the air, sacks of pollen",
    "droneroom": "row of small hexagonal rooms where drones live",
    "corridor":  "long hexagonal corridor leading to a bright exit, daylight at the end",
    "flowers":   "flower field at the entrance of the hive in sunlight, big tree trunk behind",
    "sky":       "in the sky above a forest, the giant tree hive below, sunlight",
    "queenroom": "queen's private room, canopy bed, honey incense smoke",
    "vanity":    "queen's dressing room, large amber mirror",
    "queenbed":  "queen's bed in front of the royal cradle, dawn light",
    "workshop":  "beeswax workshop, wooden workbench, pots of melted wax",
    "workers":   "worker bees' quarters at night, rows of small beds, dim lantern",
    "outerwall": "outer walkway of the hive, honeycomb wall on one side, forest far below",
    "storework": "honey storehouse workroom, workbench, honey pots, a small brass bell",
    "barracks":  "soldier bees' barracks, black chitin armor and spears on the walls",
    "cell":      "hive gate, a small prison cell with bars made of beeswax",
    "gate":      "hive gate opening to the forest, bright green forest outside",
    "training":  "soldier bees' training ground, black chitin targets",
    "spring":    "shallow pool of golden honey inside the hive, honey spring",
    "corner":    "dim corner of the honey storehouse, honey pots",
    "dispensary": "honey distribution counter near the exit, rows of honey jars",
    "honeyroom": "cozy private room with a bed covered in honey-colored sheets, honey jars",
    "whitecell": "white and gold royal cradle chamber, white beeswax walls",
    "audience":  "audience hall with a white throne, several naked slim men kneeling in a row far in the background",
    "swarm":     "in the sky over a forest with a swarm of flying bee girls in the distance, tree branches",
    "silkroom":  "bedroom with white silk curtains and a white silk bed",
}

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Hive_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def arms(who):
    return "" if who == "e2" else NEG_ARMS


def scene(key, who, place, action, desc, futa=False, insert=False, onani=False, flaccid=False):
    c = CH[who]
    body = "semi-erect penis" if flaccid else "erection"
    if onani:
        pos = ", ".join([Q, "explicit", PROT, body, "solo focus, he is in the foreground", action, "both of his hands are clearly away from his penis",
                         c["name"] + " stands far in the background fully clothed, watching, small in frame, not touching him",
                         ROOM, PL[place], desc])
    else:
        futa_tag = ", futanari, large penis on the woman" if futa else ""
        pos = ", ".join([Q, "explicit", "1girl and 1boy, " + c["tags"] + futa_tag, PROT, body, action, COVER,
                         ROOM, PL[place], desc])
    neg = NEG_CORE + arms(who) + NEG_SOLO + ("" if futa else NEG_NOFUTA) + NEG_SCENE + \
        (NEG_INSERT if (insert or futa) else "") + (NEG_ONANI if onani else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵（背景除去）
STAND = {
    "master": ("m", "standing, wings spread, holding a small golden honey dipper, gentle smile, looking down at viewer"),
    "e1": ("e1", "standing, carrying a wooden tray of honeycomb, energetic pose, one hand raised"),
    "e2": ("e2", "standing with her four arms crossed, holding a spear with a chitin hand, smirking down at viewer"),
    "e3": ("e3", "standing, holding a honey jar, licking honey from her finger, sweet smile"),
    "boss": ("boss", "standing tall, one hand on her hip, wings spread, looking down at viewer with contempt"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe", c["tags"], pose, "looking at viewer, full body, simple background, white background"]),
        NEG_CORE + arms(w) + NEG_SOLO + NEG_NOFUTA, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery",
                           "inside a giant beehive in a great tree, glowing golden hexagonal honeycomb walls, huge beeswax throne, "
                           "dripping honey, warm amber light, floating pollen, detailed background"]),
    NEG_CORE + NEG_ARMS + NEG_SOLO + NEG_NOFUTA)

# ---- 技CG
scene("atk_m1", "m", "royalcell",
      "he lies on his back in the golden hexagonal cradle, she sits beside him holding a small amber jar of " + JELLY + ", " + TUBE +
      ", her fingers gently guiding the tube, he arches his back", "the queen bee feeds royal jelly into him through a thin tube.")
scene("atk_m2", "m", "throne",
      "he lies on his back on the throne steps, she bends down and licks the nipple on his flat male chest while the tips of her antennae "
      "stroke his other nipple, erect nipples", "the queen bee licks his nipple and strokes him with her antennae.")
scene("atk_m3", "m", "nuptial",
      "from side, he lies on his back on the golden bedding with his legs lifted, she leans over him penetrating his anus with her "
      "futanari penis, anal, " + TUBE + ", his own penis separate", "the queen bee takes him from both sides.", futa=True)
scene("atk_e1", "e1", "workshop",
      "from side, he lies face down on the workbench with his hips raised, she pushes a lump of warm golden beeswax jelly into his anus "
      "with her gloved fingers, anal insertion, golden jelly dripping", "the worker bee fills him with warm beeswax jelly.", insert=True)
scene("atk_e2", "e2", "barracks",
      "she holds him from behind, her two black chitin arms pinning his arms, her two human hands pinching and twisting both of his nipples, "
      "erect nipples, he stands on tiptoe trembling", "the wasp girl pins him with four arms and plays with his nipples.")
scene("atk_e3", "e3", "spring",
      "from side, he is on all fours in the shallow golden honey pool with his hips raised, honey dripping down his back and buttocks, "
      "she kneels behind him licking his anus, anilingus", "the honey bee licks the honey off him.")
scene("atk_boss", "boss", "whitecell",
      "he lies on his back in the white and gold cradle, " + TUBE + ", golden jelly dripping from his anus, "
      "she sits beside him pinching his nipple with one hand and holding the jelly jar with the other",
      "the bee princess fills him with jelly in front and behind while pinching his nipple.", insert=True)

# ---- 敗北28（主人公と、そのシナリオの責め手だけ）
L = [
 # m1 ロイヤルゼリー
 ("btl_m1", "m", "royalcell", "he lies on his back in the golden hexagonal cradle, " + TUBE + ", she holds a small golden spoon and an amber jar, a small amber vial pendant around his neck, cum on his belly, dazed", {}),
 ("onani_m1", "m", "honeystore", "sitting on the floor with his knees apart, pressing two fingers of one hand hard against his own perineum below his balls, the other hand on the floor, penis untouched and standing, honey cells sealed with wax behind him, some with his fingerprint", {"onani": True}),
 ("inochi_m1", "m", "corridor", "he kneels in the hexagonal corridor with the bright exit behind him, " + TUBE + ", she kneels beside him holding the tube, a golden honey thread tied around his wrist leading back into the hive", {}),
 ("onedari_m1", "m", "queenroom", "he lies on the canopy bed with his legs open, begging, " + TUBE + ", she feeds a golden spoonful of jelly into the tube, a tiny golden spoon pendant on his neck", {}),
 # m2 触角と舌
 ("btl_m2", "m", "throne", "he lies on his back on the throne steps, she bends down and licks the nipple on his flat male chest, her antenna tip on his other nipple, both his nipples glistening with honey, cum on his belly", {}),
 ("onani_m2", "m", "pollen", "kneeling upright in golden pollen dust, pinching both of his own nipples with fingertips stained yellow with pollen, both hands on his chest, hands far away from his crotch, penis untouched and standing", {"onani": True}),
 ("inochi_m2", "m", "flowers", "he has collapsed on his knees in the flower field, she bends down from behind and strokes his nipples with her antennae, a small beeswax flower brooch on his chest, three flowers", {}),
 ("onedari_m2", "m", "vanity", "he sits on a stool in front of the large amber mirror begging, she stands behind him and bends down licking the nipple on his flat male chest, her antenna on the other nipple, an amber antenna-shaped chest ornament", {}),
 # m3 針管とふたなり
 ("btl_m3", "m", "nuptial", "from side, on the golden bedding he lies on his back with his legs lifted, she penetrates his anus with her futanari penis, anal, " + TUBE + ", his own penis separate, cum", {"futa": True}),
 ("onani_m3", "m", "droneroom", "sitting inside a small hexagonal room with his knees apart, pressing his own perineum with two fingers, the other arm reaching behind with one finger at his own anus, penis untouched and standing, a hexagonal crest pressed into the wax wall behind him", {"onani": True}),
 ("inochi_m3", "m", "sky", "in the sky she holds him from behind in her arms while flying with her large wings, penetrating his anus with her futanari penis, anal, his legs dangling, golden scales dust sparkling on his back, " + TUBE + ", his own penis separate", {"futa": True}),
 ("onedari_m3", "m", "queenbed", "from side, on the queen's bed he lies on his back with his legs spread begging, she kneels between his legs penetrating his anus with her futanari penis, anal, a beeswax ring on his left ring finger, his own penis separate", {"futa": True}),
 # e1 ビー（蜜蝋のアナルゼリー）
 ("btl_e1", "e1", "workshop", "from side, he lies face down on the workbench with his hips raised, she pushes golden beeswax jelly into his anus with two gloved fingers, anal insertion, a small beeswax plug in her other hand, cum on the bench", {"insert": True}),
 ("onani_e1", "e1", "workers", "kneeling on all fours on a small bed at night, one arm reaching behind with two honey-wet fingers pushed into his own anus, golden honey dripping, penis untouched and hanging", {"onani": True}),
 ("inochi_e1", "e1", "outerwall", "on the outer walkway he kneels with his hips raised, she presses warm beeswax jelly into his anus with her fingers, anal insertion, a brown worker's sash tied around his waist, forest far below", {"insert": True}),
 ("onedari_e1", "e1", "storework", "from side, he bends over the workbench begging, she holds up three small lumps of golden beeswax jelly and pushes one into his anus, anal insertion, a small brass bell on a cord around his neck", {"insert": True}),
 # e2 ワスプ（四本の腕・乳首）
 ("btl_e2", "e2", "barracks", "she holds him from behind, her two black chitin arms pinning him, her human fingers pinching both of his nipples, the tip of a thin tube touching the side of his neck with a drop of red liquid, no needle, a small red mark on his neck, cum", {}),
 ("onani_e2", "e2", "cell", "kneeling upright behind beeswax bars, pinching both of his own nipples with both hands and squeezing his chest between his wrists, hands far away from his crotch, penis untouched and standing, a black chitin arm reaching through the bars", {"onani": True}),
 ("inochi_e2", "e2", "gate", "at the hive gate with the green forest outside, she hugs him from behind with all four arms, chitin fingers pinching his nipples, red marks of four arms on his waist and chest", {}),
 ("onedari_e2", "e2", "training", "he stands against a black chitin target begging, she pins him with her chitin arms and pinches both of his nipples with her human hands, a black chitin collar around his neck", {}),
 # e3 ハニー（アナル舐め）
 ("btl_e3", "e3", "spring", "from side, he is on all fours in the golden honey pool with his hips raised, honey covering his body, she kneels behind licking his anus, anilingus, cum dripping into the honey", {}),
 ("onani_e3", "e3", "corner", "kneeling on all fours, one arm reaching behind with honey-dripping fingers stroking his own anus, penis untouched and hanging, a small honey jar beside him", {"onani": True}),
 ("inochi_e3", "e3", "dispensary", "he leans over the honey counter hugging a honey jar, she stands behind him and bends down licking the honey off his buttocks, anilingus, honey dripping on his chest, a honey-drop shaped ornament on his chest", {}),
 ("onedari_e3", "e3", "honeyroom", "from side, on the honey-colored bed he lies face down with his hips raised begging, she pours honey from a jar onto his back and licks his anus, anilingus, a honey-colored ribbon tied around his neck", {}),
 # boss メリッサ
 ("btl_boss", "boss", "whitecell", "from side, in the white and gold cradle he lies on his back with his legs lifted, she leans over licking the nipple on his flat male chest while penetrating his anus with her futanari penis, anal, her large wings spread, a platinum collar on his neck, his own penis separate, cum", {"futa": True}),
 ("onani_boss", "boss", "audience", "kneeling on the white floor before the white throne, pinching his own nipple with one hand, the other arm reaching behind pressing his perineum and one finger at his own anus, hands far away from the front of his crotch, penis untouched and standing, a bracelet of braided platinum hair on his wrist", {"onani": True}),
 ("inochi_boss", "boss", "swarm", "on a thick tree branch in the sky, she holds him on her lap from behind, " + TUBE + ", golden jelly dripping from his anus, her fingers pinching his nipple, a swarm of bee girls around", {"insert": True}),
 ("onedari_boss", "boss", "silkroom", "from side, on the white silk bed he lies on his back with his legs open begging, she kneels between his legs penetrating his anus with her futanari penis, anal, licking the nipple on his flat male chest, a platinum chain anklet on his ankle, his own penis separate", {"futa": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him her drone.", **opt)

# ---- オナニーCG（その相手の得意技に合わせた自慰。ペニスには触れない）
ONACT = {
    "m": "sitting on the floor with his knees apart, pressing two fingers of one hand hard against his own perineum below his balls, the other hand on the floor, penis untouched and standing",
    "e1": "kneeling on all fours, one arm reaching behind with two honey-wet fingers pushed into his own anus, golden honey dripping, penis untouched and hanging",
    "e2": "kneeling upright, pinching both of his own nipples with both hands and squeezing his chest between his wrists, hands far away from his crotch, penis untouched and standing",
    "e3": "kneeling on all fours, one arm reaching behind with honey-dripping fingers stroking his own anus, penis untouched and hanging",
    "boss": "kneeling, pinching his own nipple with one hand, the other arm reaching behind pressing his perineum and one finger at his own anus, penis untouched and standing",
}
ON = {"master": ("throne", "m"), "e1": ("workers", "e1"), "e2": ("barracks", "e2"), "e3": ("honeystore", "e3"), "boss": ("whitecell", "boss")}
for k, (place, who) in ON.items():
    scene("onanie_" + k, who, place, ONACT[who] + ", flushed, sweat, trembling",
          "she only watches him from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "holding up a small amber jar full of glowing golden royal jelly and a golden spoon toward viewer, gentle smile, pov", "royalcell"),
    ("magic_2", "e1", "a swarm of cute bee girls flying out around her, she points forward cheerfully", "outerwall"),
    ("magic_3", "e3", "offering a dripping honey dipper toward viewer, honey strings, sweet smile, pov", "spring"),
    ("magic_4", "e1", "worker bee girls returning to the hive at sunset, she waves, carrying pollen baskets", "flowers"),
    ("magic_5", "m", "standing beside a large glowing golden hexagonal cradle, beckoning with one finger", "royalcell"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "sensitive", c["tags"], act, "looking at viewer", ROOM, PL[place]]),
        NEG_CORE + arms(who) + NEG_SOLO.replace(", 2girls", "" if key in ("magic_2", "magic_4") else ", 2girls") + NEG_NOFUTA)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Hive", "images": images}, open(os.path.join(here, "hive_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
