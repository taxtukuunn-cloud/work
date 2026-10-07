# -*- coding: utf-8 -*-
"""N30 忍びの隠れ里（Ninja）画像プロンプト生成 → ninja_prompts.json（51枚）
N26 Kitsune の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
責め手は男の娘の忍び（胸は平ら・装束は着たまま）。主人公は場面では裸（紺髪・顔なし・150cm・非筋肉質）。
分身の術の場面（clones=True）は同じ顔の忍びが複数並ぶので、ネガティブの「双子・同じ顔・3boys」を外す。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_CORE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, watermark, signature, text, letters, sign, logo, numbers, kanji, symbol on headband, "
            "child, loli, shota, young, teenage, underage, muscular, abs, pectorals, bara, hairy, broad shoulders, manly, "
            "1girl, girl, female, woman, breasts, large breasts, medium breasts, cleavage, pussy, vagina, "
            "extra legs, three legs, four legs, extra arms, "
            "eyes visible on the small man, futanari, vaginal, penetration by the small man, merged bodies, "
            "blood, injury, wound, weapon, sword, kunai, crying in pain, bruise, rope burn")
NEG_TWIN = ", twins, same face, same hair color"
NEG_BASE = NEG_CORE + ", animal" + NEG_TWIN
NEG_SCENE = (", navy hair on the ninja, blue hair, ninja outfit on the small man, clothes on the small man, headband on the small man, "
             "nude ninja, naked ninja, the ninja undressed")
NEG_3BOYS = ", 3boys, 4boys"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, strap-on"
NEG_NOPENIS = ", ninja's penis visible, erect ninja, strap-on"
NEG_ONANI = (", ninja touching him, hand on penis, holding penis, stroking penis, handjob, penis grab, "
             "ninja masturbating, ninja in foreground")

VILLAGE = "hidden ninja village in a misty mountain valley at night, thatched roofs, mist, moonlight"

PROT_BODY = ("1boy, male, adult male, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, androgynous, "
             "petite, short, slender, narrow shoulders, narrow waist, thin legs, flat chest, smooth pale skin, no muscles, blush, height difference, "
             "completely nude")

NIN_COMMON = "ninja, adult male, otoko no ko, trap, androgynous, very feminine face, girlish, delicate features, soft face, slim waist, flat chest, no breasts, both eyes clearly visible"

CH = {
    "m": dict(seed="KAGEROU",
              tags=NIN_COMMON + ", tall, long black hair, high ponytail, red eyes, calm, cool expression, "
                   "black shinobi outfit, black cloth mouth cover pulled down around his neck, black tabi",
              name="the tall black-haired ninja with a high ponytail in a black shinobi outfit"),
    "e1": dict(seed="HAYABUSA",
               tags=NIN_COMMON + ", short grey hair, gold eyes, energetic grin, "
                    "light grey genin ninja outfit, sleeveless, coil of red rope at his waist",
               name="the grey short-haired ninja in a light grey sleeveless outfit with red rope at his waist"),
    "e2": dict(seed="SHIGURE",
               tags=NIN_COMMON + ", purple bob cut hair, grey eyes, mysterious smile, half-closed eyes, "
                    "purple ninja outfit with long wide sleeves, small hanging incense burner with thin smoke",
               name="the purple bob-haired ninja in a purple outfit with a small incense burner"),
    "e3": dict(seed="TSUMUGI",
               tags=NIN_COMMON + ", brown hair, single long braid, green eyes, gentle smile, "
                    "moss green herbalist ninja outfit, white apron, wooden medicine box on his back",
               name="the brown braided ninja in a green herbalist outfit with a white apron"),
    "boss": dict(seed="OBORO",
                 tags=NIN_COMMON + ", very tall, long white hair, red eyes, expressionless, cold eyes, "
                      "dark grey jonin ninja outfit, metal forehead protector headband with a plain blank plate",
                 name="the very tall white-haired ninja in a dark grey jonin outfit with a forehead protector"),
}

PL = {
    "zashiki": "inner tatami room of a ninja manor, shoji screens, irori sunken hearth with glowing charcoal, hanging scroll without writing, andon paper lamp, detailed background",
    "futon": "inner tatami room of a ninja manor at night, futon, shoji screens, andon paper lamp, incense smoke, detailed background",
    "incense": "inner tatami room of a ninja manor, incense burner with thick smoke, andon paper lamp, shoji screens, detailed background",
    "dojo": "wooden ninja dojo, polished wooden floor, wooden training dummy, coils of red rope on the wall, detailed background",
    "kura": "dim storehouse interior, red ropes hanging from wooden beams, old wooden chests, detailed background",
    "attic": "hidden attic room of a ninja manor, low wooden beams, a secret sliding panel, dim light, shadows, detailed background",
    "yagura": "top of a wooden watchtower at night, railing, misty village far below, moonlight, detailed background",
    "taki": "waterfall training ground, wet rocks, white spray and mist, moonlight, detailed background",
    "onsen": "outdoor rock hot spring in the mountains, steam, moonlight, detailed background",
    "yakushi": "herbalist hut, medicine grinder, shelves of jars, a jar of amber jelly, dried herbs, warm lamp light, detailed background",
    "herbs": "storehouse full of dried herbs hanging from the ceiling, baskets, dim light, detailed background",
    "genjutsu": "dark room filled with purple incense smoke, several paper lanterns casting long moving shadows on shoji, detailed background",
    "lamp_room": "small dark room with a single andon paper lamp casting a large shadow on the wall, detailed background",
    "fogpath": "mountain path in thick white fog at night, stone lanterns, detailed background",
    "gate": "large wooden gate of a hidden village at night, mist, torches, detailed background",
    "bridge": "rope suspension bridge over a deep misty valley at night, detailed background",
    "bamboo": "bamboo grove behind the village at night, moonlight, detailed background",
    "engawa": "moonlit wooden veranda, shoji screens behind, garden, detailed background",
    "shoji_shadow": "moonlit wooden veranda, a large shadow projected on a paper shoji screen, detailed background",
    "chashitsu": "small tea room, tatami, sunken hearth, incense smoke, hanging scroll without writing, detailed background",
    "jonin": "underground hidden room of a ninja manor, black tatami, wooden gears and karakuri mechanisms on the walls, revolving lanterns, detailed background",
    "jonin_bed": "private bedroom of a ninja master, dark futon, folding screen, a single lamp, detailed background",
    "river": "riverbank at the edge of a village at night, pebbles, moon reflected on the river, mist, detailed background",
}

CLOTHED = "the ninja keeps his outfit on, fully clothed ninja, only the small navy-haired man is nude"
ROPE = "soft red rope bondage on the small man, shibari, chest rope, no pain"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Ninja_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, insert=False, onani=False, penis=False, clones=0, rope=False):
    c = CH[who]
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", PROT_BODY,
                         "the small navy-haired nude man is the main subject in the foreground, he pleasures himself without touching his penis, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         VILLAGE, PL[place], desc])
        neg = NEG_BASE + NEG_SCENE + NEG_3BOYS + NEG_ONANI + NEG_NOPENIS
    else:
        nin = c["tags"] + (", his outfit parted at the front, his large erect penis exposed" if penis else "")
        if clones:
            head = "%dboys, yaoi, shadow clone technique, %d identical copies of the same ninja with the same face, " % (clones + 2, clones + 1)
        else:
            head = "2boys, yaoi, duo, two people, "
        pos = ", ".join([Q, "explicit", head + "THE NINJA (taller, dominant): " + nin,
                         "THE SMALL MAN (smaller, submissive, clearly visible in the picture): " + PROT_BODY,
                         action] + ([ROPE] if rope else []) + [CLOTHED, VILLAGE, PL[place], desc])
        neg = NEG_CORE + ", animal" + ("" if clones else NEG_TWIN + NEG_3BOYS) + NEG_SCENE + (NEG_INSERT if insert else NEG_NOPENIS)
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing, arms crossed, looking down at viewer, from below, a red rope coiled over one shoulder, calm"),
    "e1": ("e1", "standing, one fist raised, holding a coil of red rope, energetic grin, looking at viewer"),
    "e2": ("e2", "standing, holding a small hanging incense burner with purple smoke curling around him, mysterious smile, finger on lips"),
    "e3": ("e3", "standing, holding a small glass vial of amber jelly, gentle smile, medicine box on his back"),
    "boss": ("boss", "standing tall, arms at his sides, looking down at viewer, from below, expressionless, faint smoke around his feet"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]), NEG_BASE)
    images[-1]["rembg"] = True

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "hidden ninja village in a misty mountain valley at night, thatched roof houses, "
                           "water wheel, wooden watchtower, bamboo, paper lanterns, thick mist, moonlight, detailed background"]), NEG_BASE)

# ---- 技CG
scene("atk_m1", "m", "zashiki",
      "the small man kneels on the tatami with his hands tied behind his back, red rope above and below his chest making his nipples stand out, "
      "the ninja kneels beside him and licks one nipple, one hand tightening the rope",
      "the leader binds him and licks his chest.", rope=True)
scene("atk_m2", "m", "incense",
      "the small man sits in seiza facing the ninja, the ninja's palm pressed flat on the small man's lower belly, both breathing in sync, the small man's head thrown back, "
      "hands-free orgasm, trembling, eyes hidden, the ninja whispering a count",
      "the leader's breathing technique makes him climax without touch.")
scene("atk_m3", "m", "futon",
      "from side, the small man lies on his back on the futon with legs raised, one ninja kisses him deeply on the lips, tongue kiss, "
      "and the identical second ninja kneels between his legs and penetrates his anus with his large penis, anal sex",
      "the leader and his shadow clone take him at once.", insert=True, penis=True, clones=1)
scene("atk_e1", "e1", "dojo",
      "the small man is tied with red rope to a wooden training dummy, bent forward, the ninja stands behind him pressing a small smooth wooden dildo into his anus, "
      "prostate, grin, the rope rubbing the small man's nipples",
      "the genin drills him with the wooden tool.", rope=True)
scene("atk_e2", "e2", "genjutsu",
      "from behind, the small man kneels on all fours in purple smoke, the ninja kneels behind him and licks his anus with a long tongue, anilingus, "
      "long shadows from the lanterns stretching over the small man's body, the ninja's half-closed eyes",
      "the illusionist's shadow tongue.")
scene("atk_e3", "e3", "yakushi",
      "from side, the small man lies on a low wooden table with legs spread, the ninja holds a thin tube inserting amber jelly into the small man's urethra, urethral insertion, "
      "his other gloved finger in the small man's anus, amber jelly dripping, gentle smile",
      "the herbalist fills him with the secret jelly.")
scene("atk_boss", "boss", "jonin",
      "the small man sits on black tatami, two identical white-haired ninja clones kneel at his sides each licking one of his nipples, "
      "and the same ninja in front of him slowly inserts a thin silver beaded urethral sound into his penis, urethral insertion",
      "the jonin's shadow clones.", clones=2)

# ---- 敗北28
L = [
 ("btl_m1", "m", "zashiki", "by the sunken hearth the small man kneels with hands tied behind his back and three red ropes across his chest, the ninja kneels beside him licking his nipple, his palm on the small man's lower belly, cum on the tatami, glowing charcoal", {"rope": True}),
 ("onani_m1", "m", "kura", "in the storehouse the small man kneels with a red rope wrapped around his own chest, the ninja stands behind him tightening the rope and leaning down to lick his nipple, ropes hanging from the beams", {"rope": True}),
 ("inochi_m1", "m", "bridge", "at the foot of the rope suspension bridge the small man kneels with a red rope tied in a decorative knot on his chest, the ninja standing behind him holding the rope end, licking his nipple, mist", {"rope": True}),
 ("onedari_m1", "m", "engawa", "on the moonlit veranda the small man kneels begging with his chest pushed forward, red rope across his chest, the ninja kneels beside him licking his right nipple, full moon", {"rope": True}),
 ("btl_m2", "m", "incense", "the small man sits in seiza facing the ninja, the ninja's palm pressed on the small man's lower belly, the small man's head thrown back in a hands-free orgasm, cum on his thighs, incense smoke spiraling", {}),
 ("onani_m2", "m", "dojo", "on the dojo floor the small man sits cross-legged, the ninja sits behind him with one palm on the small man's lower belly and the other on his chest, whispering a count into his ear, hands-free orgasm, trembling", {}),
 ("inochi_m2", "m", "taki", "at the waterfall the small man stands naked in the shallow water, a folded white robe on a rock, the ninja stands behind him with a palm on his lower belly, both breathing together, hands-free orgasm, spray", {}),
 ("onedari_m2", "m", "chashitsu", "in the tea room the small man kneels facing the ninja with his eyes hidden, the ninja's palm on the small man's lower belly and two fingers touching his forehead, hands-free orgasm, incense smoke", {}),
 ("btl_m3", "m", "futon", "from side, the small man lies on his back on the futon with legs raised, one ninja kisses him deeply, tongue kiss, the identical second ninja penetrates his anus with his large penis, anal sex, cum, two pillows on the futon", {"insert": True, "penis": True, "clones": 1}),
 ("onani_m3", "m", "attic", "from side, in the dim attic the small man is on all fours, one ninja kisses him while the identical second ninja kneels behind him penetrating his anus, anal sex, a third identical ninja watching from the shadow of a beam", {"insert": True, "penis": True, "clones": 2}),
 ("inochi_m3", "m", "gate", "from side, just inside the big wooden gate the small man stands bent over against a gate post, one ninja kisses him while the identical second ninja stands behind him penetrating his anus, anal sex, mist, torches", {"insert": True, "penis": True, "clones": 1}),
 ("onedari_m3", "m", "zashiki", "from side, by the sunken hearth the small man sits on one ninja's lap facing away, penetrated by his large penis, anal sex, an identical second ninja kisses him, black go stones lined up on the tatami", {"insert": True, "penis": True, "clones": 1}),
 ("btl_e1", "e1", "dojo", "the small man is tied with red rope to a wooden training dummy, bent forward, the ninja behind him presses a small smooth wooden dildo deep into his anus, prostate, cum dripping, grin", {"rope": True}),
 ("onani_e1", "e1", "bamboo", "from side, in the bamboo grove the small man kneels on all fours, the ninja crouches behind him guiding the small man's own two fingers inside his anus with his hand, a bamboo tube of oil beside them, grin", {}),
 ("inochi_e1", "e1", "bridge", "on the swaying rope suspension bridge the small man holds the rope railing bent forward with a red rope around his waist tied to the railing, the ninja behind him pressing a small wooden dildo into his anus, mist below", {"rope": True}),
 ("onedari_e1", "e1", "kura", "in the storehouse the small man kneels on a wooden chest begging with red rope across his chest, the ninja behind him showing three small wooden dildos of different sizes, one pressed into the small man's anus", {"rope": True}),
 ("btl_e2", "e2", "genjutsu", "from behind, the small man lies face down in purple incense smoke with hips raised, the ninja licks his anus, anilingus, a small ash mark drawn on the small man's lower belly, long lantern shadows", {}),
 ("onani_e2", "e2", "lamp_room", "from side, in the small dark room the small man kneels on all fours with one wet finger at his own anus, the ninja kneels behind him and licks his anus, anilingus, a large shadow of the ninja on the wall", {}),
 ("inochi_e2", "e2", "fogpath", "on the foggy mountain path the small man kneels on all fours on the stones, the ninja behind him licking his anus, anilingus, a small purple incense pouch hanging from the small man's neck, thick fog", {}),
 ("onedari_e2", "e2", "shoji_shadow", "on the moonlit veranda the small man kneels bent forward begging, the ninja behind him licking his anus, anilingus, their shadow projected large on the paper shoji screen", {}),
 ("btl_e3", "e3", "yakushi", "from side, the small man lies on a low wooden table with legs spread, amber jelly inserted in his urethra through a thin tube and dripping from his anus, urethral insertion, cum, the ninja smiling holding a paper medicine packet", {}),
 ("onani_e3", "e3", "herbs", "from side, among hanging dried herbs the small man kneels with one finger in his own anus and a thumb pressing his perineum, the ninja kneels behind him adding amber jelly onto his finger, gentle smile", {}),
 ("inochi_e3", "e3", "onsen", "in the steaming rock hot spring the small man sits on the rock edge half in the amber tinted water, legs spread, the ninja beside him inserting amber jelly into his urethra with a thin tube, urethral insertion, a hand towel on the rock", {}),
 ("onedari_e3", "e3", "yakushi", "the small man lies back on the table begging with legs spread, the ninja holds a wooden spoon heaped with amber jelly over him, a thin tube in the small man's urethra, urethral insertion, jars on shelves", {}),
 ("btl_boss", "boss", "jonin", "from side, the small man lies on his back on black tatami, two identical white-haired ninja clones lick his nipples, the same ninja kneels between his legs penetrating his anus with his large penis, anal sex, a thin silver beaded urethral sound in the small man's penis", {"insert": True, "penis": True, "clones": 2}),
 ("onani_boss", "boss", "yagura", "on top of the watchtower the small man sits against the railing, two identical white-haired ninja clones kneel at his sides each licking one of his nipples, the same ninja in front inserting a thin silver beaded urethral sound, urethral insertion, moonlight", {"clones": 2}),
 ("inochi_boss", "boss", "river", "on the moonlit riverbank the small man kneels frozen, a silver needle stuck into his shadow on the pebbles, two identical white-haired ninja clones kneel at his sides licking his nipples, the same ninja standing over him, mist", {"clones": 2}),
 ("onedari_boss", "boss", "jonin_bed", "from side, on the dark futon the small man lies on his back with legs raised begging, the white-haired ninja penetrates his anus with his large penis, anal sex, an identical clone licks his nipple, a black braided cord around the small man's wrist", {"insert": True, "penis": True, "clones": 1}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him one of the village.", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "zashiki", "sitting in seiza, both hands resting flat on his own lower belly, not touching his penis, eyes hidden, head tilted back, deep breath, hands-free, trembling"),
    "e1": ("e1", "dojo", "from side, kneeling on all fours, reaching back with two oiled fingers inserted into his own anus, anal fingering, not touching his penis"),
    "e2": ("e2", "lamp_room", "from behind, kneeling on all fours, reaching back and stroking his own anus with a wet finger, a large lantern shadow over him, not touching his penis"),
    "e3": ("e3", "herbs", "sitting with legs spread, one thumb pressing his own perineum and one finger inserted in his own anus, not touching his penis, flushed"),
    "boss": ("boss", "yagura", "sitting against the railing, each hand pinching one of his own nipples, thighs squeezed tightly together, not touching his penis, drooling"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in the ninja's style while the ninja watches from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "throwing a small round smoke ball, a burst of white smoke around his feet, looking at viewer", "zashiki", False),
    ("magic_2", "e2", "holding up the small incense burner, thick purple smoke curling toward viewer, finger on lips, mysterious smile", "genjutsu", False),
    ("magic_3", "e1", "a hawk perched on his raised forearm with a small rolled message tied to its leg, grin", "yagura", True),
    ("magic_4", "e1", "crouching in the forest holding the end of a red rope snare springing up from fallen leaves, grin", "bamboo", False),
    ("magic_5", "m", "standing on a watchtower with the misty hidden village spread out behind him, arms crossed, looking at viewer", "yagura", False),
]
for key, who, act, place, animal in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", VILLAGE, PL[place]]),
        (NEG_CORE + NEG_TWIN) if animal else NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Ninja", "images": images}, open(os.path.join(here, "ninja_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
