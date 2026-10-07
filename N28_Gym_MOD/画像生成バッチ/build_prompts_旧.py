# -*- coding: utf-8 -*-
"""N28 パーソナルトレーナー（Gym）画像プロンプト生成 → gym_prompts.json（51枚）
N26 Kitsune の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
責め手は男の娘のトレーナー（胸は平ら・筋肉なし・ウェアは着たまま）。
主人公は場面では裸か会員用の黒いコンプレッションシャツ（紺髪・顔なし・150cm・非筋肉質）。
魔導マシンの灯りは琥珀色（主人公の紺髪と紛れないため。青い光は使わない）。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, watermark, signature, text, letters, sign, logo, numbers, digital display, "
            "child, loli, shota, young, teenage, underage, muscular, abs, pectorals, biceps, bara, bodybuilder, hairy, broad shoulders, manly, "
            "1girl, girl, female, woman, breasts, large breasts, medium breasts, cleavage, pussy, vagina, "
            "twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the small man, futanari, vaginal, penetration by the small man, merged bodies, "
            "blood, injury, crying in pain, blue light, cyan light")
NEG_SCENE = (", 3boys, navy hair on the trainer, blue hair, nude trainer, naked trainer, the trainer undressed, topless trainer, muscular trainer")
NEG_NUDE = ", clothes on the small man, shirt on the small man, sportswear on the small man"
NEG_WEAR = ", sports bra on the small man, leggings on the small man"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, strap-on"
NEG_NOPENIS = ", trainer's penis visible, erect trainer, strap-on"
NEG_ONANI = (", trainer touching him, hand on penis, holding penis, stroking penis, handjob, penis grab, "
             "trainer masturbating, trainer in foreground")

GYM = ("members-only personal gym in a fantasy town, converted stone warehouse, magic-powered training machines glowing warm amber, "
       "wall mirrors")

PROT = ("1boy, male, adult male, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, androgynous, "
        "petite, short, slender, narrow shoulders, narrow waist, thin legs, flat chest, smooth pale skin, no muscles, skinny, blush, height difference")
PROT_NUDE = PROT + ", completely nude"
PROT_WEAR = (PROT + ", wearing only a tight black long-sleeve compression shirt, erect nipples visible through the thin fabric, bottomless")

TR_COMMON = ("adult male, otoko no ko, trap, androgynous, very feminine face, girlish, delicate features, soft face, slim waist, "
             "flat chest, no breasts, slender, no muscles, both eyes clearly visible")

CH = {
    "m": dict(seed="HAYATE",
              tags=TR_COMMON + ", tall, brown hair, short ponytail, amber eyes, energetic smile, white sports crop top on a flat chest, "
                   "black leggings, towel around neck",
              name="the tall brown-ponytailed trainer in a white crop top and black leggings"),
    "e1": dict(seed="AI",
               tags=TR_COMMON + ", long pink hair, purple eyes, calm smile, lavender long-sleeve yoga top, lavender yoga pants, barefoot",
               name="the long pink-haired yoga instructor in lavender yoga wear"),
    "e2": dict(seed="SOU",
               tags=TR_COMMON + ", green hair, mushroom cut, brown eyes, focused expression, white massage therapist tunic, black pants, "
                    "small oil bottle on his belt",
               name="the green mushroom-haired massage therapist in a white tunic"),
    "e3": dict(seed="RUI",
               tags=TR_COMMON + ", blonde hair, bob cut, green eyes, flirty smile, white polo shirt, black short shorts, receptionist",
               name="the blonde bob-haired receptionist in a white polo shirt and black short shorts"),
    "boss": dict(seed="TAIGA",
                 tags=TR_COMMON + ", very tall, long black hair, gold eyes, domineering, cold smile, black track jacket zipped up, black track pants",
                 name="the very tall long black-haired gym owner in a black track jacket"),
}

PL = {
    "gym": "training room, wall of mirrors, rubber floor mats, dumbbell racks, treadmills, warm amber lights, detailed background",
    "dev": "dim development room, large magic-powered machine with a padded seat and a slowly moving mechanical arm, amber lamps on the machine, mirror, detailed background",
    "stretch": "stretching area, padded massage table, stretch mats, foam rollers, mirror, warm lights, detailed background",
    "locker": "locker room, metal lockers, wooden bench, folded towels, detailed background",
    "shower": "shower room, white tiles, steam, water droplets, detailed background",
    "office": "trainers' office, desk, shelves of member folders, blank menu board, desk lamp, detailed background",
    "counter": "gym reception counter at night, potted plants, warm lamps, detailed background",
    "backroom": "small room behind the reception counter, small sofa, shelves of member cards, dim lamp, detailed background",
    "lounge": "members' lounge, leather sofas, smoothie bar, large windows at night, detailed background",
    "yoga": "yoga studio, wooden floor, indirect warm lighting, incense smoke, yoga mats, detailed background",
    "medit": "small meditation room, floor cushions, candles, a small brass bell, dim light, detailed background",
    "roof": "rooftop terrace of the gym at sunrise, yoga mats, town roofs below, golden morning light, detailed background",
    "treat": "treatment room, aroma diffuser, warm towels, rows of oil bottles, massage bed, soft light, detailed background",
    "waiting": "small waiting room of the treatment area, wooden bench, potted plant, aroma, detailed background",
    "private": "private treatment room, massage bed with white sheets, candle light, detailed background",
    "owner": "owner's room on the top floor, two large custom machines glowing amber, huge window with night town view, detailed background",
    "hall": "top floor corridor in front of a heavy wooden door, dim lights, detailed background",
    "exit": "gym entrance hall at night, glass doors, a body measuring machine with amber lamps, detailed background",
    "night": "dark gym machine room after closing, only the amber machine lamps glowing, moonlight through high windows, detailed background",
}

CLOTHED = "the trainer keeps his sportswear on, fully clothed trainer"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Gym_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, insert=False, onani=False, penis=False, wear=False, machine=False):
    c = CH[who]
    body = PROT_WEAR if wear else PROT_NUDE
    cloth_neg = NEG_WEAR if wear else NEG_NUDE
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", body,
                         "the small navy-haired man is the main subject in the foreground, he pleasures himself without touching his penis, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         GYM, PL[place], desc])
        neg = NEG_BASE + NEG_SCENE + cloth_neg + NEG_ONANI + NEG_NOPENIS + ", dildo, sex machine"
    else:
        tr = c["tags"] + (", his leggings pulled down at the front, his large erect penis exposed" if penis else "")
        only = "only the small navy-haired man is nude" if not wear else "the small navy-haired man wears only a black compression shirt"
        pos = ", ".join([Q, "explicit", "2boys, yaoi, duo, two people", "THE TRAINER (taller, dominant): " + tr,
                         "THE SMALL MAN (smaller, submissive, clearly visible in the picture): " + body, action,
                         CLOTHED + ", " + only, GYM, PL[place], desc])
        neg = NEG_BASE + NEG_SCENE + cloth_neg + (NEG_INSERT if insert else NEG_NOPENIS)
        if not machine and not insert:
            neg += ", dildo, sex machine"
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing, one hand on hip, other hand giving a thumbs up, towel around neck, looking down at viewer, from below, energetic smile"),
    "e1": ("e1", "standing in tree pose on one bare foot, hands pressed together in front of chest, eyes half closed, calm smile"),
    "e2": ("e2", "standing, holding a small glass oil bottle in one hand, rubbing oil between his fingers, focused gentle look"),
    "e3": ("e3", "standing, leaning forward slightly, one finger on his lips, holding a blank membership card, winking, flirty smile"),
    "boss": ("boss", "standing tall with arms crossed, looking down at viewer, from below, cold smile, imposing"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]), NEG_BASE, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", GYM, "training room at night, rows of magic-powered training machines with warm amber lamps, "
                           "rubber floor mats, dumbbell racks, big mirrors, high stone walls, detailed background"]), NEG_BASE)

# ---- 技CG
scene("atk_m1", "m", "gym",
      "the small man walks on a treadmill, trembling, arms around his own chest, small vibrators under his tight shirt on both nipples, "
      "the trainer stands beside the treadmill holding a small remote control, smiling, reflection in the mirror",
      "the trainer turns up the vibration in his shirt.", wear=True)
scene("atk_m2", "m", "dev",
      "from side, the small man on all fours on the padded seat of a sex machine, straps around his waist and thighs, "
      "the machine's arm thrusts a smooth dildo attachment into his anus, sex machine, the trainer stands beside the machine counting, hand on the control lever",
      "the development machine keeps its steady rhythm.", machine=True)
scene("atk_m3", "m", "stretch",
      "from side, the small man lies on his back on the massage table with legs raised, clear suction cups on both nipples connected by tubes to an amber glowing machine, nipple suction, "
      "the trainer stands between his legs and penetrates his anus with his large penis, anal sex",
      "the trainer matches his hips to the machine's rhythm.", insert=True, penis=True, machine=True)
scene("atk_e1", "e1", "yoga",
      "the small man sits cross-legged on a yoga mat with soles together, eyes hidden by bangs, mouth open, hands-free orgasm, trembling, "
      "the instructor sits behind him with one palm pressed on the small man's lower belly and lips at his ear, guiding his breathing",
      "breathe in, hold, breathe out.")
scene("atk_e2", "e2", "treat",
      "from side, the small man lies face down on the massage bed, oily glistening skin, the therapist stands beside him and inserts two oiled fingers into his anus, anal fingering, "
      "prostate massage, other hand pressing the small man's lower back, warm towel",
      "the therapist works out the knot inside him.")
scene("atk_e3", "e3", "backroom",
      "the small man sits on the small sofa, the receptionist leans over him kissing him deeply, french kiss, tongues, saliva, "
      "the receptionist's fingers pinching the small man's nipple",
      "a sweet welcome kiss for the new member.")
scene("atk_boss", "boss", "owner",
      "from side, the small man is strapped on his knees between two large amber glowing machines, clear suction cups on both nipples from one machine, nipple suction, "
      "the other machine's arm thrusts a smooth dildo attachment into his anus, sex machine, the owner stands with his hand on the control lever, looking down",
      "two machines finish his body.", machine=True)

# ---- 敗北28（場面・構図・結末の印）
M, I, P, W = {"machine": True}, {"insert": True, "penis": True, "machine": True}, {"insert": True, "penis": True}, {"wear": True}
L = [
 # m1 ハヤテ・ウェア内蔵のローター（主人公はウェア姿）
 ("btl_m1", "m", "gym", "the small man on a running treadmill, gasping, both hands clutching his own chest, small vibrators hidden under his shirt on both nipples, hands-free orgasm, cum dripping down his thighs, the trainer beside the treadmill with a remote control, reflection in the mirror", W),
 ("onani_m1", "m", "locker", "the small man sits on the locker room bench flicking his own nipples through the shirt with his fingers, the trainer leaning against the lockers behind him holding a remote control, an open locker", W),
 ("inochi_m1", "m", "stretch", "the small man sits on a stretch mat doing a seated forward bend, trembling, the trainer pressing his back from behind with a remote control in one hand, a folded towel beside him", W),
 ("onedari_m1", "m", "office", "the small man stands by the desk with his shirt pulled up over his chest, pointing at his own left nipple, begging, the trainer sits at the desk writing on a blank sheet with a pen, a small remote control on the desk", W),
 # m2 ハヤテ・★開発マシン
 ("btl_m2", "m", "dev", "from side, the small man on all fours on the padded seat of a sex machine, straps on his waist and thighs, the machine's arm thrusting a smooth dildo attachment into his anus, sex machine, hands-free orgasm, cum, the trainer beside him raising the lever, a row of attachments of different sizes on a shelf", M),
 ("onani_m2", "m", "night", "from side, in the dark machine room the small man kneels on the floor reaching back with two fingers in his own anus, anal fingering, the trainer standing at the doorway turning on an amber lamp, holding a key", {}),
 ("inochi_m2", "m", "dev", "from side, the small man strapped on the padded seat of a sex machine, sex machine, the dildo attachment inside his anus, the trainer holding a clipboard with a blank paper and a pen toward the small man's hand", M),
 ("onedari_m2", "m", "dev", "from side, the small man on all fours on the sex machine looking back at the trainer, begging, the machine's arm pushing a dildo attachment into his anus at an angle, sex machine, the trainer adjusting a dial on the machine", M),
 # m3 ハヤテ・【同時】マシンに胸を任せて
 ("btl_m3", "m", "stretch", "from side, the small man lies on his back on the massage table with legs raised, clear suction cups on both nipples, nipple suction, the trainer penetrates his anus with his large penis, anal sex, cum on the small man's belly", I),
 ("onani_m3", "m", "shower", "from side, the small man with both hands on the tile wall, clear suction cups on his nipples, nipple suction, the trainer stands behind him penetrating his anus, anal sex, steam, water droplets, the trainer's sportswear wet", I),
 ("inochi_m3", "m", "stretch", "from side, the small man in bridge pose on the stretch mat, clear suction cups on his nipples, nipple suction, the trainer kneels holding his hips and penetrates his anus, anal sex", I),
 ("onedari_m3", "m", "stretch", "from side, the small man lies on the massage table begging with legs spread, clear suction cups on his nipples, nipple suction, the trainer about to penetrate him with his large penis, two oiled fingers raised", I),
 # e1 アイ・★呼吸法＋開脚ポーズでパール
 ("btl_e1", "e1", "yoga", "the small man sits in bound angle pose on a yoga mat, trembling, hands-free orgasm, cum on the mat, the instructor sits behind him with a palm on his lower belly whispering, a string of anal beads on the mat beside them", {}),
 ("onani_e1", "e1", "yoga", "the small man sits cross-legged alone in the corner of the studio with eyes hidden by bangs, hands resting on his knees, mouth open breathing, flushed, the instructor kneeling behind him with lips near his ear", {}),
 ("inochi_e1", "e1", "medit", "the small man sits on a meditation cushion with hands on his knees, head tilted back, hands-free orgasm, the instructor kneels in front of him ringing a small brass bell", {}),
 ("onedari_e1", "e1", "roof", "from side, the small man in a wide-legged straddle pose on a yoga mat at sunrise, a string of anal beads half inserted in his anus, anal beads, the instructor behind him with a palm on his belly", {}),
 # e2 ソウ・★前立腺マッサージ＋オイルで乳首
 ("btl_e2", "e2", "treat", "from side, the small man lies face down on the massage bed with oily skin, the therapist inserts two oiled fingers into his anus, anal fingering, prostate massage, hands-free orgasm, cum on the sheet, warm towels", {}),
 ("onani_e2", "e2", "waiting", "from side, the small man kneels on the bench of the waiting room reaching back with oiled fingers in his own anus, the therapist behind him placing his hand over the small man's hand, guiding his fingers, a small oil bottle on the bench", {}),
 ("inochi_e2", "e2", "treat", "the small man lies on his back on the massage bed, oily chest, the therapist rubbing oil on both of his nipples with his fingertips, a stack of blank coupon tickets on the side table", {}),
 ("onedari_e2", "e2", "private", "from side, the small man lies on his side on the massage bed begging, knees drawn up, the therapist sits behind him with two oiled fingers inside his anus, anal fingering, prostate massage, candle light", {}),
 # e3 ルイ・★入会記念のキス＋規約の読み上げ
 ("btl_e3", "e3", "backroom", "the small man sits on the small sofa, the receptionist straddles his lap in shorts and kisses him deeply, french kiss, tongues, saliva trail, fingers pinching the small man's nipples, a blank membership card with a pink lipstick kiss mark on the table", {}),
 ("onani_e3", "e3", "counter", "the small man sits on the sofa in front of the reception counter with the receptionist's finger in his mouth, sucking on it, the receptionist sits beside him smiling, other hand rubbing the small man's wet nipple", {}),
 ("inochi_e3", "e3", "counter", "the small man leans on the reception counter holding a pen over a blank sheet, the receptionist leans over the counter kissing him, french kiss, one hand on the small man's nipple", {}),
 ("onedari_e3", "e3", "lounge", "the small man sits on a leather sofa, the receptionist kisses his ear while whispering, the small man's head tilted, blushing, the receptionist's fingers on his nipple", {}),
 # boss タイガ・★【同時】二台のマシン＋最終メニュー
 ("btl_boss", "boss", "owner", "from side, the small man lies on his back on a padded bench between two amber glowing machines with legs raised, clear suction cups on both nipples, nipple suction, the owner penetrates his anus with his large penis, anal sex, cum on his belly, a heavy key on a cord on the bench", {"insert": True, "penis": True, "machine": True}),
 ("onani_boss", "boss", "hall", "the small man kneels in the dim corridor pinching his own nipple upward with one hand and reaching back with two fingers into his own anus with the other, anal fingering, the heavy door open with the owner standing in the doorway looking down", {}),
 ("inochi_boss", "boss", "exit", "from side, the small man strapped on the seat of the amber measuring machine near the glass doors, clear suction cups on his nipples, nipple suction, a machine arm thrusting a smooth attachment into his anus, sex machine, the owner standing beside with arms crossed", M),
 ("onedari_boss", "boss", "owner", "from side, the small man kneels between the two amber machines begging, clear suction cups on his nipples, nipple suction, a machine arm thrusting a smooth attachment into his anus, sex machine, the owner standing in front of him with a hand on his chin", M),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " has finished shaping his body.", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "night", "from side, kneeling on the rubber mat, reaching back with two fingers into his own anus in a steady rhythm like a machine, anal fingering, not touching his penis, flushed", {}),
    "e1": ("e1", "yoga", "sitting cross-legged on a yoga mat, hands resting on his knees, not using his hands, mouth open breathing out, eyes hidden, hands-free, trembling, not touching his penis", {}),
    "e2": ("e2", "treat", "from side, kneeling on the massage bed, reaching back with oiled fingers into his own anus, anal fingering, glistening oil, not touching his penis", {}),
    "e3": ("e3", "counter", "sitting on a sofa sucking on two of his own fingers, other wet finger rubbing his own nipple, not touching his penis, drooling", {}),
    "boss": ("boss", "owner", "kneeling, one hand pinching and pulling up his own nipple, other hand reaching back with two fingers into his own anus, anal fingering, not touching his penis", {}),
}
for k, (who, place, act, opt) in ON.items():
    scene("onanie_" + k, who, place, act, "he trains himself alone in the trainer's style while the trainer watches from afar.", onani=True, **opt)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "holding out a blank flyer toward viewer with one hand, winking, thumbs up with the other hand, energetic smile", "counter"),
    ("magic_2", "m", "holding up a shaker bottle of pink protein shake toward viewer, smiling, towel around neck", "gym"),
    ("magic_3", "e3", "behind the reception counter holding a blank appointment book and a pen, finger on lips, winking", "counter"),
    ("magic_4", "boss", "standing beside a large amber glowing training machine with leather straps hanging from it, one hand on the machine, looking at viewer, cold smile", "dev"),
    ("magic_5", "m", "standing with a large sports bag on his shoulder, pointing forward, energetic, sunrise", "roof"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", GYM, PL[place]]), NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Gym", "images": images}, open(os.path.join(here, "gym_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
