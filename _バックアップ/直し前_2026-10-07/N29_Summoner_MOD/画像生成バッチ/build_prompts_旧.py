# -*- coding: utf-8 -*-
"""N29 触手使いの魔導塔（Summoner）画像プロンプト生成 → summoner_prompts.json（51枚）
N26 Kitsune の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
責め手は男の娘の召喚術師（胸は平ら・ローブは着たまま）。触手は術師が魔法陣から召喚し指先で操る（体から生やさない）。
主人公は場面では裸（紺髪・顔なし・150cm・非筋肉質）。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, numbers, runes, writing, "
            "child, loli, shota, young, teenage, underage, muscular, abs, pectorals, bara, hairy, broad shoulders, manly, "
            "1girl, girl, female, woman, breasts, large breasts, medium breasts, cleavage, pussy, vagina, "
            "twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the small man, futanari, vaginal, penetration by the small man, merged bodies, "
            "blood, injury, crying in pain, gore, monster girl, octopus girl, scylla, "
            "blue tentacles, green tentacles, tentacles growing from the summoner's body, tentacle hair")
NEG_SCENE = (", 3boys, navy hair on the summoner, blue hair on the summoner, robe on the small man, clothes on the small man, "
             "hood on the small man, gloves on the small man, nude summoner, naked summoner, the summoner undressed")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, strap-on"
NEG_NOPENIS = ", summoner's penis visible, erect summoner, strap-on, dildo"
NEG_ONANI = (", summoner touching him, tentacles touching him, hand on penis, holding penis, stroking penis, handjob, penis grab, "
             "summoner masturbating, summoner in foreground")

TOWER = "inside an old stone magic tower at night, glowing purple and gold magic circles, candles, old books"

PROT_BODY = ("1boy, male, adult male, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, androgynous, "
             "petite, short, slender, narrow shoulders, narrow waist, thin legs, flat chest, smooth pale skin, no muscles, blush, height difference, "
             "completely nude")

TENT = ("translucent purple tentacles with fine cilia, glistening with lavender slime, "
        "rising out of a glowing purple magic circle, controlled by the summoner's raised fingers")

MAGE = ("adult male, otoko no ko, trap, androgynous, very feminine face, girlish, delicate features, soft face, slim waist, flat chest, "
        "no breasts, both eyes clearly visible")

CH = {
    "m": dict(seed="LUKE",
              tags=MAGE + ", tall, long straight purple hair, gold eyes, gentle sadistic smile, deep purple summoner robe with gold trim, long slender fingers",
              name="the tall purple-haired summoner in a deep purple robe"),
    "e1": dict(seed="PINO",
               tags=MAGE + ", messy curly orange hair, green eyes, eager smile, oversized light brown apprentice robe, sleeves too long, holding a piece of chalk",
               name="the orange-haired apprentice in an oversized light brown robe"),
    "e2": dict(seed="RICK",
               tags=MAGE + ", short pink hair, red eyes, teasing smile, black and pink frilled outfit, "
                           "a small round purple tentacle familiar creature sitting on his shoulder",
               name="the pink-haired familiar master in a black and pink outfit with a tiny purple tentacle pet"),
    "e3": dict(seed="EDO",
               tags=MAGE + ", messy unkempt brown hair, amber eyes, eccentric grin, dark green work apron over a shirt, black rubber gloves up to the elbows",
               name="the brown-haired keeper in a dark green work apron and elbow-length black gloves"),
    "boss": dict(seed="WERNER",
                 tags=MAGE + ", very tall, long straight white hair, purple eyes, cold expression, white and silver archmage robe, silver ring on his finger",
                 name="the very tall white-haired archmage in a white and silver robe"),
}

PL = {
    "lab": "summoner's laboratory, an experiment table, shelves of glass flasks, a huge magic circle drawn on the stone floor, detailed background",
    "lab_circle": "summoner's laboratory seen from above, the whole stone floor covered by one glowing magic circle, a small bed in the center, detailed background",
    "stairs": "landing of a stone spiral staircase, magic lamps on the wall, detailed background",
    "sendback": "round chamber with a glowing return magic circle on the floor, pillars of light, detailed background",
    "bookshelf": "tall bookshelves of old tomes, a wooden chair in front, a floating crystal orb, detailed background",
    "vats": "underground chamber lined with tall glass vats filled with glowing lavender slime, glass tubes, detailed background",
    "bath": "stone bathtub filled with warm glowing lavender slime, steam, candles, detailed background",
    "specimen": "specimen room, shelves of glass jars without labels, a small amber bottle, dim light, detailed background",
    "bedroom": "the summoner's private bedroom, canopy bed with purple sheets, candles, detailed background",
    "guest": "small guest room of the tower, simple bed, one candle, stone wall, detailed background",
    "gate": "entrance hall of the tower, huge wooden double door slightly open to the dark forest, night wind, detailed background",
    "observatory": "open rooftop observatory at the top of the tower, starry night sky, brass telescope, star chart on the floor, detailed background",
    "practice": "apprentice practice room, stone floor covered with half-drawn chalk magic circles, detailed background",
    "library": "tower library, wooden reading desk, old books, candlelight, detailed background",
    "familiar_room": "cozy bedroom piled with pink and black cushions and blankets, detailed background",
    "greenhouse": "indoor greenhouse of the tower, strange tentacle plants and moss, glass roof, moonlight, detailed background",
    "breeding": "tentacle breeding room, iron cages and glass aquariums, humid air, wet stone floor, detailed background",
    "exp_room": "experiment room with a stone experiment table, glowing circles, detailed background",
    "tank": "breeding room, a large shallow glass aquarium with water on the floor, detailed background",
    "grand": "grand summoning hall, an enormous glowing magic circle with rings of light rising to the high ceiling, detailed background",
    "corridor_top": "stone corridor at the top floor of the tower, tall windows, moonlight, detailed background",
    "forbidden": "forbidden archive of the library, chained old tomes, a lectern, faint glowing sigils in the air, detailed background",
    "top_bed": "archmage's bedchamber at the top of the tower, a crystal pedestal, white canopy bed, moonlight, detailed background",
}

CLOTHED = "the summoner keeps his robe on, fully clothed summoner, only the small navy-haired man is nude"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Summoner_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, insert=False, onani=False, mage_penis=False, tent=True):
    c = CH[who]
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", PROT_BODY,
                         "the small navy-haired nude man is the main subject in the foreground, he pleasures himself without touching his penis, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         TOWER, PL[place], desc])
        neg = NEG_BASE + NEG_SCENE + NEG_ONANI + NEG_NOPENIS
    else:
        mage = c["tags"] + (", his robe parted at the front, his large erect penis exposed" if mage_penis else "")
        pos = ", ".join([Q, "explicit", "2boys, yaoi, duo, two people, tentacles" if tent else "2boys, yaoi, duo, two people",
                         "THE SUMMONER (taller, dominant, standing or kneeling above): " + mage,
                         "THE SMALL MAN (smaller, submissive, clearly visible in the picture): " + PROT_BODY,
                         action, (TENT if tent else ""), CLOTHED, TOWER, PL[place], desc])
        neg = NEG_BASE + NEG_SCENE + (NEG_INSERT if insert else NEG_NOPENIS)
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing, one hand raised with fingers spread, a glowing purple magic circle floating above his palm with a few thin purple tentacles curling out of it, looking down at viewer, from below, gentle sadistic smile"),
    "e1": ("e1", "standing, holding chalk up proudly, a tiny glowing chalk magic circle at his feet with one very thin purple tentacle poking out, eager smile"),
    "e2": ("e2", "standing, head tilted, finger on his lips, tongue slightly out, the small purple tentacle familiar on his shoulder sticking out its tongue-like tentacle too"),
    "e3": ("e3", "standing, arms spread with elbow-length black gloves, holding a glass jar with a curled purple tentacle inside, eccentric grin"),
    "boss": ("boss", "standing tall, hands clasped, behind him a huge glowing magic circle with a swarm of purple tentacles rising, looking down at viewer, from below, imposing"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]), NEG_BASE, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "interior of an old stone magic tower at night, spiral staircase, bookshelves, glass flasks, "
                           "huge glowing purple and gold magic circles on the floor and in the air, candles, moonlight through tall windows, detailed background"]), NEG_BASE)

# ---- 技CG
scene("atk_m1", "m", "lab",
      "the small man lies on his back on the experiment table, the summoner stands beside him conducting with his fingers, "
      "thin purple tentacles curl around the small man's chest, cilia brushing both nipples, one tentacle tip shaped like a sucker latched onto a nipple",
      "the summoner's tentacles develop his nipples.")
scene("atk_m2", "m", "vats",
      "from side, the small man lies face down on a table in front of the glass vats, a thin tentacle tube pumps lavender slime into his anus, anal jelly, slime dripping, "
      "the summoner stands beside him holding a flask, other tentacles under his chest on his nipples",
      "aphrodisiac slime is poured into him.")
scene("atk_m3", "m", "lab_circle",
      "from side, the small man lies on his back in the center of the magic circle with legs raised, the summoner kneels between his legs and penetrates his anus with his large penis, anal sex, "
      "purple tentacles wrapping the small man's chest and sucking both nipples at the same time",
      "the summoner takes him while tentacles hold his chest.", insert=True, mage_penis=True)
scene("atk_e1", "e1", "practice",
      "the small man sits on the chalk-drawn floor with legs spread, the apprentice kneels in front of him guiding one very thin purple tentacle from a small chalk circle into the small man's urethra, urethral insertion, "
      "a faint glowing magic circle in front of the small man's eyes",
      "the apprentice's tiny tentacle enters him from inside.")
scene("atk_e2", "e2", "familiar_room",
      "from behind, the small man is on all fours on the cushions, the pink-haired summoner kneels behind him and licks his anus, anilingus, "
      "the small purple familiar creature beside his face also licking with its tongue-like tentacle, two tongues",
      "master and familiar lick him together.", tent=False)
scene("atk_e3", "e3", "breeding",
      "from side, the small man kneels on all fours on the wet stone floor, the keeper kneels beside him, a purple tentacle crawling out of a glass aquarium slides into the small man's anus, "
      "the keeper's black-gloved hand guiding it, feeding time",
      "the keeper's pet tentacle crawls inside.")
scene("atk_boss", "boss", "grand",
      "the small man hangs suspended in the air above the enormous magic circle, held by a swarm of purple tentacles, thin tentacles sucking both nipples and one thin tentacle inserted in his urethra, urethral insertion, "
      "the archmage stands below with one hand raised",
      "the archmage's tentacle swarm fills him.")

# ---- 敗北28
L = [
 ("btl_m1", "m", "lab", "the small man lies on his back on the experiment table arching, many thin purple tentacles wrapped around his chest, sucker-tipped tentacles latched on both nipples, hands-free orgasm, cum on his belly, the summoner stands beside him dictating notes, a tiny glowing magic circle on the edge of the small man's areola", {}),
 ("onani_m1", "m", "stairs", "on the stone stair landing the small man sits against the wall twisting his own fingers around his nipples, two thin purple tentacles wrapped around his fingers, the summoner crouching one step above observing, a floating crystal orb", {}),
 ("inochi_m1", "m", "sendback", "the small man stands in the center of the glowing return magic circle, purple tentacles rising from the circle wrapping his legs and chest and sucking his nipples, his knees buckling, the summoner outside the circle smiling, a small glowing sigil between his nipples", {}),
 ("onedari_m1", "m", "bookshelf", "the small man sits naked on a wooden chair in front of bookshelves with his chest pushed out, four purple tentacles sucking and stroking his nipples, the summoner stands beside the chair with a notebook, dictating", {}),
 ("btl_m2", "m", "vats", "from side, the small man lies face down on a table in front of glass vats, a thin glass tube from a vat pumping lavender slime into his anus, anal jelly, tentacles under his chest on his nipples, slime overflowing, the summoner holding a flask", {}),
 ("onani_m2", "m", "bath", "the small man sits half submerged in the stone bathtub of glowing lavender slime, purple tentacles rising from the slime wrapped around his chest and nipples, the summoner kneeling at the edge of the tub holding one slime-soaked glove", {}),
 ("inochi_m2", "m", "specimen", "from side, the small man bends over a table in the specimen room, the summoner behind him pressing a small amber bottle's thin nozzle into the small man's anus, anal jelly, tentacles on his nipples, shelves of unlabeled jars", {}),
 ("onedari_m2", "m", "bedroom", "on a canopy bed with purple sheets the small man lies on his side with his knees up, a thin glass syringe with measurement lines inserted in his anus, anal jelly, the summoner sitting beside him pressing the plunger slowly, tentacles on his nipples", {}),
 ("btl_m3", "m", "lab_circle", "from side, the small man lies on his back in the center of the glowing floor magic circle with legs raised, the summoner penetrates his anus with his large penis, anal sex, tentacles sucking both nipples, cum", {"insert": True, "mage_penis": True}),
 ("onani_m3", "m", "guest", "from side, on a simple bed the small man lies on his side, the summoner lies behind him penetrating his anus with his large penis, anal sex, purple tentacles wrapped around the small man's chest, a purple tassel cord tied around the small man's neck", {"insert": True, "mage_penis": True}),
 ("inochi_m3", "m", "gate", "from side, the small man stands with both hands pressed against the huge open wooden door, night forest outside, the summoner stands behind him penetrating his anus, anal sex, tentacles from a floor circle wrapping the small man's chest and nipples, a key hanging from the summoner's neck", {"insert": True, "mage_penis": True}),
 ("onedari_m3", "m", "observatory", "from side, under the starry sky the small man sits on the summoner's lap facing away, penetrated by the summoner's large penis, anal sex, tentacles sucking both nipples, a star chart on the floor, brass telescope", {"insert": True, "mage_penis": True}),
 ("btl_e1", "e1", "practice", "the small man sits on the chalk-covered floor leaning back on his hands with legs spread, a very thin purple tentacle from a small chalk circle inserted deep into his urethra, urethral insertion, hands-free orgasm, the apprentice kneeling in front cheering, a small chalk magic circle drawn on the small man's inner thigh", {}),
 ("onani_e1", "e1", "library", "the small man sits under the reading desk with legs spread, a very thin purple tentacle inserted into his urethra, urethral insertion, a small glowing magic circle lighting him, the apprentice crouching and peeking under the desk, a small bell on the desk", {}),
 ("inochi_e1", "e1", "stairs", "on the spiral staircase the small man sits on a step with legs spread, the apprentice one step below pulling a thin purple tentacle half out of the small man's urethra, urethral insertion, a glowing circle in front of the small man's eyes", {}),
 ("onedari_e1", "e1", "practice", "the small man lies on his back in the middle of a chalk magic circle begging, the apprentice kneeling beside him guiding a thin tentacle into the small man's urethra, urethral insertion, the circle glowing orange, an orange cord tied on the small man's wrist", {}),
 ("btl_e2", "e2", "familiar_room", "from side, the small man on all fours on cushions, the pink-haired summoner licking the small man's nipple from below while the small purple familiar licks his anus with its tongue-like tentacle, anilingus, a pink ribbon tied on the small man's ankle", {"tent": False}),
 ("onani_e2", "e2", "bath", "from behind, the small man kneels on the edge of the slime bathtub with two wet fingers at his own anus, the pink-haired summoner kneels behind him licking his anus, anilingus, the small familiar licking beside, steam", {"tent": False}),
 ("inochi_e2", "e2", "greenhouse", "from behind, among tentacle plants and moss the small man kneels on all fours, the pink-haired summoner and the small familiar both lick his anus, anilingus, two tongues, moonlight through the glass roof", {"tent": False}),
 ("onedari_e2", "e2", "familiar_room", "from behind, the small man lies face down on a pile of cushions with hips raised begging, the pink-haired summoner and the familiar lick his anus together, anilingus, one cushion under his chest", {"tent": False}),
 ("btl_e3", "e3", "breeding", "from side, the small man on all fours on the wet stone floor, several purple tentacles crawling out of aquariums, one inserted in his anus and a thin one in his urethra, the keeper kneeling beside him with a black glove, cum", {}),
 ("onani_e3", "e3", "breeding", "from side, in front of a glass aquarium the small man kneels on all fours with his own two fingers in his anus, a purple tentacle sliding in alongside his fingers, the keeper standing beside with a small bell", {}),
 ("inochi_e3", "e3", "exp_room", "from side, the small man lies on the stone experiment table, a folded dark green apron beside him, a purple tentacle inserted into his anus, the keeper standing beside him demonstrating with black-gloved hands", {}),
 ("onedari_e3", "e3", "tank", "the small man sits in a shallow glass aquarium of water with legs spread, several purple tentacles of different thickness crawling to his anus, one inside, the keeper kneeling outside the tank releasing another from a jar", {}),
 ("btl_boss", "boss", "grand", "from side, above the enormous glowing magic circle the small man lies on his back held by tentacles, the archmage kneels between his legs penetrating his anus, anal sex, a swarm of thin tentacles on both nipples and in his urethra, urethral insertion, rings of light", {"insert": True, "mage_penis": True}),
 ("onani_boss", "boss", "corridor_top", "in the moonlit top floor corridor the small man kneels, a swarm of thin purple tentacles wrapped around his nipples and one in his urethra, urethral insertion, the archmage standing over him, a silver ring around the small man's ankle", {}),
 ("inochi_boss", "boss", "forbidden", "the small man kneels at a lectern holding an open old tome with faint glowing sigils rising from its pages, tentacles swarming up his body onto his nipples and into his urethra, urethral insertion, glowing sigil patterns on the small man's skin, the archmage behind him", {}),
 ("onedari_boss", "boss", "top_bed", "from side, on a white canopy bed the small man lies on his back with legs raised, the archmage penetrates his anus, anal sex, tentacles on both nipples and in his urethra, urethral insertion, a silver ring on the small man's left finger, a crystal pedestal", {"insert": True, "mage_penis": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him a vessel for tentacles.", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "stairs", "sitting against the wall, twisting his own fingers like tentacles around both of his own nipples, poking the tips, not touching his penis, flushed, trembling"),
    "e1": ("e1", "library", "sitting with legs spread, one finger tracing his own perineum below his testicles upward, not touching his penis, head thrown back, flushed"),
    "e2": ("e2", "familiar_room", "from behind, kneeling on all fours on cushions, reaching back and stroking his own anus with two wet fingers, not touching his penis"),
    "e3": ("e3", "breeding", "from side, kneeling on all fours, reaching back with two fingers inserted into his own anus, wriggling them, anal fingering, not touching his penis"),
    "boss": ("boss", "corridor_top", "kneeling, one hand twisting around his own nipple, the other pressing his own perineum, not touching his penis, drooling, flushed"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in the summoner's style while the summoner watches from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "kneeling and pressing his palm on a huge glowing purple magic circle on the floor, purple tentacles rising from it, looking at viewer", "lab"),
    ("magic_2", "m", "holding up a small glass bottle of glowing lavender slime toward viewer, a drop running down the glass, gentle sadistic smile", "specimen"),
    ("magic_3", "e2", "ringing a small bell, the small tentacle familiar on his shoulder, cheerful wink, looking at viewer", "stairs"),
    ("magic_4", "e3", "crouching and pointing at thin purple tentacles hiding in the cracks of the stone floor, eccentric grin, looking at viewer", "breeding"),
    ("magic_5", "e3", "standing beside a stone planter full of lavender slime with many young purple tentacles sprouting from it, spreading his gloved arms, looking at viewer", "greenhouse"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, TOWER, PL[place]]), NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Summoner", "images": images}, open(os.path.join(here, "summoner_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
