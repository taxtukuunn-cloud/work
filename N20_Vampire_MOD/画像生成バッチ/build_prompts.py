# -*- coding: utf-8 -*-
"""N20 吸血鬼の館（Vampire）画像プロンプト生成 → vampire_prompts.json（51枚）
登場人物は全員20歳以上の成人。個人利用のみ。N19 Twins の build_prompts.py と同じ書き方。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_CORE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, "
            "child, loli, shota, young, teenage, underage, petite female, muscular, abs, pectorals, bara, hairy, "
            "blood, bleeding, wound, gore, collar, leash, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the man, 2boys, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies")
NEG_SOLO = ", 2girls, twins, same face"
NEG_NOFUTA = ", futanari, penis on the woman, woman with penis"
NEG_SCENE = (", pussy, vagina, breasts on the man, long hair on the man, silver hair on the man, black hair on the man, "
             "blue hair on the woman, fangs on the man, wings on the man, bat wings on the man, maid headdress on the man, "
             "dress on the man, pantyhose on the man, cape on the man, clothes on the man, naked woman, nude woman")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, strap-on"
NEG_ONANI = (", woman touching him, hetero sex, hands on him, woman masturbating, girl masturbating, penis on the woman, "
             "hand on penis, holding penis, handjob, stroking penis, penis grab")
NEG_CAGE = ", erection, erect penis, large penis, cage on the chest, chest harness"

ROOM = "gothic vampire castle, flickering candlelight, deep red and black tones, detailed background"

PROT = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult male, androgynous, "
        "feminine body, petite, short, slender, narrow shoulders, narrow waist, thin arms, flat chest, smooth pale skin, "
        "no muscles, blush, height difference, nude male, completely naked, penis")
FANG = "two tiny pink fang marks on his skin, no blood"
CAGE = ("his penis is locked in a small flat silver chastity cage with a thin strap around his waist and a tiny silver padlock, "
        "flaccid penis inside the cage")

CH = {
    "m": dict(seed="NOCTIA",
              tags="1girl, vampire, adult woman, mature female, tall woman, silver hair, very long straight hair, red eyes, fangs, "
                   "black and red gothic dress with a high collar, long sleeves, elegant, cold smile, large breasts",
              name="the tall silver-haired vampire countess in a black and red gothic dress"),
    "e1": dict(seed="LILIA",
               tags="1girl, vampire, adult woman, black hair, bob cut, red eyes, fangs, pale skin, "
                    "black gothic maid outfit, white frilled apron, maid headdress, polite smile, medium breasts",
               name="the black-haired vampire maid in a black gothic maid outfit"),
    "e2": dict(seed="PIPI",
               tags="1girl, bat girl, adult woman, mature face, purple hair, short hair, red eyes, fang, "
                    "large dark purple bat wings instead of arms, black tube top, black shorts, playful grin, small breasts",
               name="the purple-haired bat girl with bat wings for arms"),
    "e3": dict(seed="CELES",
               tags="1girl, vampire, adult woman, mature face, red hair, very long hair, gold eyes, "
                    "black mourning dress, black veil, black pantyhose, silver key on a chain necklace, expressionless, medium breasts",
               name="the red-haired woman in a black mourning dress and black pantyhose"),
    "boss": dict(seed="VALENCIA",
                 tags="1girl, vampire, mature female, very tall woman, platinum blonde hair, very long hair, crimson eyes, fangs, "
                      "crimson royal gown, crimson cape with high collar, regal, haughty smile, huge breasts",
                 name="the very tall platinum-haired vampire queen in a crimson gown and cape"),
}

PL = {
    "bedroom":  "countess bedroom, canopy bed with red curtains, three candelabras",
    "mirror":   "hall of mirrors, walls covered with tall mirrors, candles",
    "bridge":   "drawbridge in thick fog at night, castle gate behind",
    "dining":   "long dining table, candelabra, empty wine glasses, red tablecloth",
    "balcony":  "moonlit castle balcony, full moon, stone railing",
    "gallery":  "portrait gallery, old portraits of nobles on the walls, red carpet",
    "chapel":   "ruined chapel, broken stained glass window, moonlight beams",
    "vanity":   "dressing room, triple mirror vanity, perfume bottles",
    "ballroom": "grand ballroom after a ball, crystal chandelier, red carpet",
    "tower":    "spiral stone staircase inside a tower, candle sconces",
    "guest":    "guest room, bed with cold white sheets, candlestick",
    "linen":    "linen room, shelves of folded white sheets, dim lamp",
    "backdoor": "foggy castle garden at the back door, mist, dead trees",
    "dayroom":  "guest room in daytime with thick curtains closed, thin line of light",
    "belfry":   "castle belfry, wooden beams, big bronze bell, many bats",
    "atticbox": "dusty attic storage, old trunks and costume boxes",
    "wall":     "castle wall walkway at night, battlements, towers, wind",
    "hammock":  "cloth hammock hanging between attic beams, moonlight",
    "crypt":    "underground crypt, rows of black coffins, white candles",
    "grave":    "foggy graveyard, stone mausoleum, bell",
    "irondoor": "crypt exit, heavy iron door, open black coffin",
    "celesroom": "dark bedroom, black lace canopy bed, wardrobe of mourning dresses",
    "throne":   "throne room, crimson throne, huge window with a full moon",
    "fountain": "courtyard with a fountain of red rose water, moonlight, roses",
    "sanctum":  "royal bedchamber, huge bed with a crimson canopy, moonlight",
}

CLOTHED = "the woman keeps her clothes on, only the man is naked"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Vampire_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, futa=False, insert=False, onani=False, cage=False):
    c = CH[who]
    body = CAGE if cage else "erection"
    if onani:
        pos = ", ".join([Q, "explicit", PROT, body, "solo focus, he is in the foreground", action,
                         c["name"] + " stands far in the background fully clothed, watching, small in frame, not touching him",
                         ROOM, PL[place], desc])
    else:
        futa_tag = ", futanari, large penis on the woman" if futa else ""
        pos = ", ".join([Q, "explicit", "1girl and 1boy, " + c["tags"] + futa_tag, PROT, body, action, CLOTHED,
                         ROOM, PL[place], desc])
    neg = NEG_CORE + NEG_SOLO + ("" if futa else NEG_NOFUTA) + NEG_SCENE + \
        (NEG_INSERT if (insert or futa) else "") + (NEG_ONANI if onani else "") + (NEG_CAGE if cage else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵（背景除去）
STAND = {
    "master": ("m", "standing, holding a glass of red wine, slight smile showing fangs, looking down at viewer"),
    "e1": ("e1", "standing, curtsey, holding her skirt, head slightly tilted, smile showing a fang"),
    "e2": ("e2", "flying, bat wings spread wide, leaning forward, cheerful open-mouth grin"),
    "e3": ("e3", "standing still, hands folded in front, holding the silver key on her chain, blank stare"),
    "boss": ("boss", "standing tall, one hand on her hip, cape flowing, looking down at viewer with contempt"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe", c["tags"], pose, "looking at viewer, full body, simple background, white background"]),
        NEG_CORE + NEG_SOLO + NEG_NOFUTA, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery",
                           "gothic vampire castle bedroom at night, canopy bed with red curtains, three lit candelabras, "
                           "tall window with a full moon and fog outside, stone walls, red carpet, detailed background"]),
    NEG_CORE + NEG_SOLO + NEG_NOFUTA)

# ---- 技CG
scene("atk_m1", "m", "bedroom",
      "he sits on the edge of the canopy bed, she stands and lifts his chin with one finger, deep kiss, tongues, saliva trail, "
      "his lips slightly red, his hands limp", "the vampire countess drains his energy with a long kiss.")
scene("atk_m2", "m", "bedroom",
      "she holds him from behind and bends down licking his nipple, her fangs near his nipple, " + FANG + " beside his nipples, erect nipples",
      "the vampire countess licks the fang marks on his chest.")
scene("atk_m3", "m", "ballroom",
      "from side, he lies on his back on the red carpet with his legs lifted, she leans over him kissing him deeply "
      "while penetrating his anus with her futanari penis, anal, his own penis separate",
      "the countess kisses him while penetrating him.", futa=True)
scene("atk_e1", "e1", "guest",
      "from side, he is on all fours on the bed with his hips raised, she kneels behind him licking his anus, anilingus, "
      "her mouth near his ear earlier, he grips the sheets", "the vampire maid licks him with her cold tongue.")
scene("atk_e2", "e2", "belfry",
      "she hangs upside down from a beam, the tips of her bat wings pressed on both of his nipples, vibrating, motion lines, "
      "he stands below trembling with his back arched", "the bat girl vibrates his nipples with her wing tips.")
scene("atk_e3", "e3", "crypt",
      "he sits on the edge of a black coffin, she kneels in front of him locking the tiny silver padlock of the chastity cage with her key, "
      "her pantyhose foot pressing between his legs", "the coffin keeper seals him with a chastity cage.", cage=True)
scene("atk_boss", "boss", "throne",
      "from side, he lies on his back on the red carpet in front of the throne with his legs lifted, she leans over licking the fang marks on his nipple "
      "while penetrating his anus with her futanari penis, anal, " + FANG + ", his own penis separate",
      "the vampire queen licks his fang marks while penetrating him.", futa=True)

# ---- 敗北28（主人公と、そのシナリオの責め手だけ）
L = [
 # m1 口づけ
 ("btl_m1", "m", "bedroom", "he sits on the canopy bed with his chin lifted, she kisses him deeply, tongues, saliva, one candle burning and two blown out with smoke, his lips stained red, cum on his belly, dazed", {}),
 ("onani_m1", "m", "mirror", "kneeling upright, sucking his own fingers, the other wet hand tracing his own neck and nipple, hands far away from his crotch, penis untouched, only he is reflected in the mirrors, she stands behind him but is not reflected in the mirror, a small silver hand mirror on the floor", {"onani": True}),
 ("inochi_m1", "m", "bridge", "on the foggy drawbridge he has turned back, she holds his face and kisses him deeply, a red gemstone ring on his left ring finger, his knees giving way", {}),
 ("onedari_m1", "m", "dining", "he sits on the long dining table, begging with his mouth open, she leans over and kisses him deeply, tongues, a letter with a red wax seal beside him", {}),
 # m2 牙跡
 ("btl_m2", "m", "balcony", "he leans back against the stone railing under the full moon, she licks his nipple, " + FANG + " beside both nipples, erect nipples, cum on his belly", {}),
 ("onani_m2", "m", "gallery", "kneeling upright, licking his own fingertips, wet fingertips rubbing both of his own nipples, " + FANG + " beside his nipples, hands far away from his crotch, penis untouched, old portraits looking down", {"onani": True}),
 ("inochi_m2", "m", "chapel", "moonlight through broken stained glass, she kisses the center of his chest with her fangs and pinches both of his nipples, a new pair of fang marks in the center of his chest, no blood", {}),
 ("onedari_m2", "m", "vanity", "he sits on the vanity stool in front of the triple mirror begging, she bites near his left nipple and rolls his right nipple with her finger, she is not reflected in the mirrors, a small silver fang-shaped charm on a chain on his chest", {}),
 # m3 首筋から唇へ（キス＋ふたなり）
 ("btl_m3", "m", "ballroom", "from side, on the red carpet under the chandelier, he lies on his back with his legs lifted, she kisses him deeply while penetrating his anus with her futanari penis, anal, " + FANG + " on his neck, his own penis separate, cum", {"futa": True}),
 ("onani_m3", "m", "bedroom", "kneeling beside the canopy bed outside the thin red curtain, sucking his own fingers, the other hand tracing his own neck and nipple, hands far away from his crotch, penis untouched, her silhouette behind the red curtain", {"onani": True}),
 ("inochi_m3", "m", "tower", "from side, on the spiral stone stairs he is bent forward on the steps, she stands behind him holding his chin and kissing him from the side while penetrating his anus with her futanari penis, anal, a red ribbon tied around his neck, his own penis separate", {"futa": True}),
 ("onedari_m3", "m", "bedroom", "from side, he lies on his back on the canopy bed with a pillow under his hips and his legs spread, begging, she lies over him kissing him while penetrating his anus with her futanari penis, anal, an old iron key on the nightstand, his own penis separate", {"futa": True}),
 # e1 リリア
 ("btl_e1", "e1", "guest", "from side, he lies face down with his hips raised on the cold white sheets, she kneels behind him licking his anus, anilingus, a brass key on a ribbon hanging from her apron, cum on the sheets, trembling", {}),
 ("onani_e1", "e1", "linen", "kneeling on all fours between shelves of sheets, one hand reaching behind with a fingertip circling his own anus, penis untouched, a crumpled stained sheet under him, a small silver hand bell on the shelf", {"onani": True}),
 ("inochi_e1", "e1", "backdoor", "in the foggy garden he is on his knees, she kneels behind him licking his anus, anilingus, she had whispered into his ear, " + FANG + " on his earlobe", {}),
 ("onedari_e1", "e1", "dayroom", "from side, curtains closed in daytime, he lies face down on the bed with his hips raised, she licks his anus, anilingus, a small hourglass on the bedside table, sleepy morning light", {}),
 # e2 ピピ
 ("btl_e2", "e2", "belfry", "she hangs upside down from a beam, her wing tips vibrating on both of his nipples, a string of red beads, anal beads, partly inserted in his anus, purple feathers stuck on his chest, cum", {"insert": True}),
 ("onani_e2", "e2", "atticbox", "kneeling upright among old trunks, fingertips trembling fast on both of his own nipples, vibrating motion lines, hands far away from his crotch, penis untouched, she hangs upside down from the ceiling beam watching and counting, a necklace of red beads on him", {"onani": True}),
 ("inochi_e2", "e2", "wall", "he sits on the battlement, she hugs him from the front wrapping him in her bat wings, her wings vibrating on his chest, a thin purple ribbon tied on his nipple, night wind", {}),
 ("onedari_e2", "e2", "hammock", "he lies in the cloth hammock begging, she wraps him in her bat wings, wing tips vibrating on his nipples, motion lines, a purple feather hair ornament in his hair", {}),
 # e3 セレス（貞操帯）
 ("btl_e3", "e3", "crypt", "he sits on the edge of a black coffin, she presses the sole of her black pantyhose foot on the chastity cage and his perineum, three coffin lids closed behind, leaking a little white fluid from the cage, trembling", {"cage": True}),
 ("onani_e3", "e3", "grave", "sitting on the ground with one knee up, pressing his own heel against his own perineum, hands on the ground, not touching the cage, a black ribbon tied around his ankle, she stands by the mausoleum looking down silently", {"onani": True, "cage": True}),
 ("inochi_e3", "e3", "irondoor", "he leans into an open black coffin reaching for a key at the bottom, she presses her black pantyhose foot on his back and her other foot between his legs on the cage, his name carved on the coffin", {"cage": True}),
 ("onedari_e3", "e3", "celesroom", "he lies on the black lace bed begging, she sits beside him with the silver key, a black ribbon with seven knots tied around his wrist, her pantyhose foot resting on his thigh", {"cage": True}),
 # boss ヴァレンシア
 ("btl_boss", "boss", "throne", "from side, in front of the crimson throne he lies on his back with his legs lifted, she leans over licking his nipple while penetrating his anus with her futanari penis, anal, a glowing red crest on his lower belly, his own penis separate, cum", {"futa": True}),
 ("onani_boss", "boss", "throne", "kneeling on the red carpet before the throne, one hand rubbing his own nipple with fang marks, the other arm reaching behind with two fingers in his own anus, hands far away from his crotch, penis untouched, a glowing red crest on his lower belly, she sits on the throne far behind looking down", {"onani": True}),
 ("inochi_boss", "boss", "fountain", "from side, on the rim of the rose water fountain, she folds his legs up and penetrates his anus with her futanari penis, anal, licking his nipple, a tiny red mark on his tongue, his own penis separate", {"futa": True}),
 ("onedari_boss", "boss", "sanctum", "from side, on the crimson canopy bed he lies on his back begging with his legs open, she kneels between his legs penetrating his anus with her futanari penis, anal, a gold crest ring on his finger, his own penis separate", {"futa": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him her vampire servant.", **opt)

# ---- オナニーCG（その相手の得意技に合わせた自慰）
ONACT = {
    "m": "kneeling upright, sucking his own fingers, the other wet hand tracing his own neck and nipple, hands far away from his crotch, penis untouched",
    "e1": "kneeling on all fours, one hand reaching behind with a fingertip circling his own anus, penis untouched",
    "e2": "kneeling upright, fingertips trembling fast on both of his own nipples, vibrating motion lines, hands far away from his crotch, penis untouched",
    "e3": "sitting on the floor with one knee up, pressing his own heel against his own perineum, hands on the floor, not touching the cage",
    "boss": "kneeling upright, one hand rubbing his own nipple, the other arm reaching behind with two fingers in his own anus, hands far away from his crotch, penis untouched",
}
ON = {"master": ("bedroom", "m"), "e1": ("linen", "e1"), "e2": ("atticbox", "e2"), "e3": ("crypt", "e3"), "boss": ("throne", "boss")}
for k, (place, who) in ON.items():
    scene("onanie_" + k, who, place, ONACT[who] + ", flushed, sweat, trembling",
          "he pleasures himself during the card battle while she watches from afar.", onani=True, cage=(who == "e3"))

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "standing on the balcony under a huge red full moon, arms open, cape of mist around her, looking back at viewer", "balcony"),
    ("magic_2", "m", "holding up a silver goblet of red wine toward viewer, licking her lips, pov", "dining"),
    ("magic_3", "e2", "a swarm of bats flying out of the belfry around her, she spreads her wings, excited grin", "belfry"),
    ("magic_4", "e3", "standing beside a black coffin in a corridor, the lid slightly open, pale candlelight, beckoning with one finger", "crypt"),
    ("magic_5", "m", "spraying a crystal perfume bottle toward viewer, pink mist, seductive smile, pov", "vanity"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "sensitive", c["tags"], act, "looking at viewer", ROOM, PL[place]]), NEG_CORE + NEG_SOLO + NEG_NOFUTA)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Vampire", "images": images}, open(os.path.join(here, "vampire_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
