# -*- coding: utf-8 -*-
"""N27 騎士団（Knight）画像プロンプト生成 → knight_prompts.json（51枚）
登場人物は全員20歳以上の成人（責め手は男の娘の騎士）。個人利用のみ。N20 Vampire の build_prompts.py と同じ書き方。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_CORE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, c"
            "hild, loli, shota, young, teenage, underage, muscular, abs, pectorals, bara, hairy, broad shoulders, manly, ma"
            "sculine face, breasts, large breasts, medium breasts, cleavage, 1girl, female, woman, blood, bleeding, wound, "
            "gore, weapon pointed, sword fighting, collar, leash, extra legs, three legs, four legs, extra arms, numbers, b"
            "ad feet, extra toes, eyes visible on the navy-haired man, vaginal, merged bodies, crying in pain, injury, chil"
            "dlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, small bo"
            "dy, petite male, young boy, kid")
NEG_SOLO = ", twins, same face, same hair color"
NEG_SCENE = (", 3boys, navy hair on the knight, blue hair on the knight, the knight undressed, knight without armor, "
             "armor on the navy-haired man, clothes on the navy-haired man, cape on the navy-haired man, boots on the navy-haired man, "
             "blonde hair on the naked man, long hair on the naked man, naked knight, nude knight, knight undressed, "
             "pussy, vagina, breasts on the man")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, strap-on"
NEG_NOPEN = ", penis on the knight, knight's penis, erection on the knight"
NEG_ONANI = (", knight touching him, hands on him, knight masturbating, hand on penis, holding penis, handjob, stroking peni"
             "s, penis grab, hand on crotch, hand near penis, touching penis")
NEG_CAGE = ", erection, erect penis, large penis, cage on the chest, chest harness"

ROOM = "medieval stone fortress on a cliff, torchlight, heraldic banners without text, detailed background"
OTOKO = ("adult male, mature face, sharp adult features, 25 years old, adult proportions, long legs, otoko no ko, trap, "
         "androgynous, very feminine, delicate features, slim waist, flat chest, no breasts, tall, both eyes clearly vis"
         "ible")

PROT = ("faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult man, mature male, 25 yea"
        "rs old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, "
        "adam's apple, collarbones, flat male chest, flat chest, smooth pale skin, blush, height difference, nude male,"
        " completely naked, penis, ordinary human man, he is a head shorter than the other man")
CAGE = ("his penis is locked in a small flat silver chastity cage with a thin strap around his waist and a tiny silver padlock, "
        "flaccid penis inside the cage")
BUJIE = "a thin chain of small silver beads inserted into his urethra, urethral insertion, sounding"
JELLY = "translucent light blue jelly dripping from his urethra and anus"

CH = {
    "m": dict(seed="ALVIN",
              tags=OTOKO + ", blonde hair, long hair, ponytail, green eyes, silver plate armor with slim design, knight commander, "
                   "one gauntlet on the left hand, proud expression, cmnm",
              name="the blonde ponytailed knight commander in slim silver armor"),
    "e1": dict(seed="RIO",
               tags=OTOKO + ", brown hair, short hair, brown eyes, light leather armor, squire, leather boots, smug grin, cmnm",
               name="the brown-haired squire in light leather armor and boots"),
    "e2": dict(seed="ELSIE",
               tags=OTOKO + ", green hair, long hair, gold eyes, mage robe, small breastplate, holding a staff, intellectual calm expression, cmnm",
               name="the green-haired mage knight in a robe and breastplate"),
    "e3": dict(seed="NOEL",
               tags=OTOKO + ", red hair, medium hair, green eyes, archer outfit, quiver on the back, boots, lazy teasing smile, cmnm",
               name="the red-haired archer knight with a quiver"),
    "boss": dict(seed="JULIUS",
                 tags=OTOKO + ", white hair, long hair, gold eyes, white paladin armor, white cape, very tall, gentle merciless smile, cmnm",
                 name="the white-haired paladin in white armor and cape"),
}

PL = {
    "interrog": "stone interrogation room, wooden chair with leather straps, stone table, bottles of holy water, sword rack on the wall",
    "cell":     "underground dungeon cell, straw on the floor, iron bars, one oil lamp",
    "armory":   "armory, racks of armor, polishing cloths, jars of oil, torch",
    "yard":     "sandy training yard at sunset, wooden practice swords, fortress walls",
    "library":  "mage's library, shelves of spell books, candles, glowing magic circle on the floor",
    "watch":    "top of a watchtower at night, bow and quiver, cold wind, torch",
    "wall":     "castle wall walkway at dusk, battlements, arrow slit",
    "chapel":   "chapel with a holy water fountain, stained glass, altar",
    "hall":     "hall of investiture, rows of banners, commander's chair on a dais",
    "office":   "commander's office, oak desk, parchment, wax seal, map, empty sword rack",
    "bedroom":  "commander's bedroom, hard wooden bed without canopy, banner on the wall, candle",
    "guard":    "guardroom with a fireplace, leather bench, hourglass",
}

CLOTHED = "the knight keeps his armor on, only the shorter navy-haired man is naked, the knight is taller than him"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Knight_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, insert=False, onani=False, cage=False):
    c = CH[who]
    body = CAGE if cage else "erection"
    if onani:
        pos = ", ".join([Q, "explicit", "2boys, solo focus on the shorter navy-haired man, " + PROT, body, "he is in the foreground", action,
                         c["name"] + " stands far in the background fully armored, watching, small in frame, not touching him",
                         ROOM, PL[place], desc])
    else:
        pen = ", the knight's armor opened only at the crotch, the knight's large penis exposed, two separate penises" if insert else ""
        pos = ", ".join([Q, "explicit", "2boys, " + c["tags"] + pen, "and a naked shorter adult man: " + PROT, body, action, CLOTHED,
                         ROOM, PL[place], desc])
    neg = NEG_CORE + NEG_SOLO + NEG_SCENE + (NEG_INSERT if insert else NEG_NOPEN) + \
        (NEG_ONANI if onani else "") + (NEG_CAGE if cage else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵（背景除去）
STAND = {
    "master": ("m", "standing, one hand resting on the hilt of a sheathed sword, chin up, looking down at viewer"),
    "e1": ("e1", "standing with a wooden practice sword on the shoulder, one hand on hip, grinning"),
    "e2": ("e2", "standing, holding the staff upright, light rope of magic floating around the other hand, calm"),
    "e3": ("e3", "standing relaxed, holding a bow loosely, a small silver key dangling from one finger, lazy smile"),
    "boss": ("boss", "standing tall, hands folded as if in prayer, cape flowing, benevolent smile"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe", "solo, 1boy", c["tags"], pose, "looking at viewer, full body, simple background, white background"]),
        NEG_CORE + NEG_SOLO, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery",
                           "stone interrogation room inside a medieval fortress, wooden chair with leather straps, stone table, "
                           "torchlight, heraldic banner with a plain crest and no text, sword rack, detailed background"]),
    NEG_CORE + NEG_SOLO)

# ---- 技CG
scene("atk_m1", "m", "interrog",
      "he sits strapped in the wooden chair, the commander stands lifting his chin with the pommel of a sheathed sword and kisses him deeply, "
      "tongues, saliva trail", "the knight commander kisses the prisoner.")
scene("atk_m2", "m", "armory",
      "from front, he sits on the armor stand table with his chest out, the commander bends down licking his right nipple "
      "while pinching his left nipple with the gauntlet fingers, erect nipples", "the knight commander tests both nipples with gauntlet and tongue.")
scene("atk_m3", "m", "interrog",
      "from side, he lies on his back on the stone table with his legs lifted, the commander stands between his legs penetrating his anus, anal, "
      + BUJIE + ", his own penis separate", "the knight commander punishes him with beads and his own body.", insert=True)
scene("atk_e1", "e1", "yard",
      "from side, he is pinned face down on the sand with his hips raised, the squire kneels on his back holding his arm, "
      "a small vibrator inserted in his anus, motion lines, his face in the sand", "the squire pins him down and vibrates him.", insert=True)
scene("atk_e2", "e2", "library",
      "he floats slightly above the magic circle bound spread-eagle by glowing ropes of light around his wrists and ankles, "
      "the mage knight stands at a distance pointing the staff, chanting, his back arched, no hands on him", "the mage knight makes him climax with a spell.")
scene("atk_e3", "e3", "watch",
      "he kneels on the watchtower floor, the archer crouches behind him hugging him, one hand pressing his perineum below the cage, "
      "a small silver key on a string in the archer's teeth", "the archer locks him in a chastity cage.", cage=True)
scene("atk_boss", "boss", "chapel",
      "he lies on his back on the altar with his legs spread, the paladin stands over him pouring light blue jelly from a glass vial, "
      + JELLY, "the paladin fills him with holy jelly.")

# ---- 敗北28（主人公と、そのシナリオの責め手だけ）
L = [
 # m1 口づけ
 ("btl_m1", "m", "interrog", "he sits strapped in the leather chair, the commander lifts his chin with the sword pommel and kisses him deeply, tongues, saliva, cum on his belly, dazed", {}),
 ("onani_m1", "m", "cell", "kneeling upright on the straw, sucking his own fingers, the other wet hand rubbing his own nipple, hands far away from his crotch, penis untouched, the commander stands outside the iron bars watching", {"onani": True}),
 ("inochi_m1", "m", "office", "he kneels with his hands behind his back, his own sword lying on the floor, the commander lifts his chin with the pommel of that sword and kisses him deeply, parchment with a wax seal on the desk", {}),
 ("onedari_m1", "m", "bedroom", "he sits on the edge of the hard bed with his mouth open begging, the commander bends down kissing him deeply, tongues, saliva trail, a candle and a written order on the small table", {}),
 # m2 手甲と舌
 ("btl_m2", "m", "armory", "from front, he lies on the armor stand table with his chest out, the commander licks his right nipple while pinching the left with the gauntlet, jars of oil around, cum on his belly", {}),
 ("onani_m2", "m", "cell", "sitting on the straw with his chest out, one wet fingertip rubbing his right nipple, the other hand pinching his left nipple hard, hands far away from his crotch, penis untouched, the commander watches from outside the bars", {"onani": True}),
 ("inochi_m2", "m", "office", "morning light through a slit window, he sits on the desk, the commander licks one nipple and pinches the other with the gauntlet, tiny silver crest charms clipped on both of his nipples", {}),
 ("onedari_m2", "m", "hall", "he kneels on the dais steps before the commander's chair begging, the commander seated leans forward licking his right nipple and pinching his left with the gauntlet, banners behind", {}),
 # m3 尋問室の処罰
 ("btl_m3", "m", "interrog", "from side, he lies on his back on the stone table with legs lifted, the commander penetrates his anus, anal, " + BUJIE + ", his own penis separate, cum leaking, leather straps", {"insert": True}),
 ("onani_m3", "m", "cell", "on all fours on the straw with his hips raised, one arm reaching behind with two of his own fingers in his own anus, penis untouched, oil jar beside him, the commander watches from outside the bars", {"onani": True}),
 ("inochi_m3", "m", "office", "from side, daylight, he is bent over the oak desk with his hands tied to the desk leg by a leather belt, the commander behind him penetrating his anus, anal, " + BUJIE + ", his own penis separate, blank parchment under him", {"insert": True}),
 ("onedari_m3", "m", "bedroom", "from side, he lies on the hard bed holding his own knees up begging, the commander kneels between his legs penetrating his anus, anal, " + BUJIE + ", his own penis separate, a punishment ledger open on the side table", {"insert": True}),
 # e1 リオ
 ("btl_e1", "e1", "yard", "from side, sunset, he is pinned face down on the sand with hips raised, the squire kneels on him, a small vibrator in his anus, motion lines, cum on the sand", {"insert": True}),
 ("onani_e1", "e1", "cell", "face down on the straw with his hips raised, one arm reaching behind with trembling fingers in his own anus, penis untouched, the squire watches from outside the bars with a lamp", {"onani": True}),
 ("inochi_e1", "e1", "armory", "from side, he is pinned face down on the armor maintenance table, the squire holds his arm behind his back, a small vibrator in his anus, a parchment and oil jar beside them", {"insert": True}),
 ("onedari_e1", "e1", "guard", "from side, he lies on the rug before the fireplace with his hips raised begging, the squire kneels beside him holding a vibrator inserted in his anus, an hourglass on the bench", {"insert": True}),
 # e2 エルシー
 ("btl_e2", "e2", "library", "he floats above the magic circle bound by glowing ropes of light at wrists and ankles, back arched, cum in the air, the mage knight stands far away with the staff raised, no hands on him", {}),
 ("onani_e2", "e2", "cell", "lying on the straw on his back holding his own wrists together above his head and his ankles pressed together as if bound, eyes closed, back arched, hands far from his crotch, penis untouched, the mage knight watches from outside the bars", {"onani": True}),
 ("inochi_e2", "e2", "interrog", "daylight, he lies on the stone table bound spread-eagle by glowing ropes of light, the mage knight stands at the head of the table with the staff, one glowing word floating above him, cum on his belly", {}),
 ("onedari_e2", "e2", "guard", "he kneels before the fireplace with glowing light ropes around his wrists, ankles and waist, mouth open chanting, the mage knight stands behind him with arms folded holding the staff", {}),
 # e3 ノエル（貞操帯）
 ("btl_e3", "e3", "watch", "he kneels on the watchtower floor at night, the archer crouches behind him pressing two fingers on his perineum below the cage, small round rotors taped on both of his nipples, a little white fluid leaking from the cage", {"cage": True}),
 ("onani_e3", "e3", "cell", "sitting on the straw with knees up, one hand pressing his own perineum below the cage, the other arm reaching behind with a finger in his own anus, not touching the cage, the archer watches from outside the bars", {"onani": True, "cage": True}),
 ("inochi_e3", "e3", "guard", "he sits in the archer's lap on the leather bench before the fireplace, a key on a string held in his own fist, the archer's fingers in his anus from below, a second silver padlock hanging on the cage, rotors on his nipples", {"cage": True}),
 ("onedari_e3", "e3", "wall", "dusk, he sits beside the archer in an arrow slit niche on the wall walkway, both facing forward, the archer's hand between his legs pressing below the cage, a feather quill on the ledge", {"cage": True}),
 # boss ユリウス
 ("btl_boss", "boss", "chapel", "he lies on his back on the altar with legs spread, the paladin pours light blue jelly from a vial, " + JELLY + ", stained glass light, trembling", {}),
 ("onani_boss", "boss", "chapel", "from side, sitting on the rim of the holy water fountain, one hand pressing his own perineum, the other arm reaching behind with fingers in his own anus, penis untouched, the paladin watches from the chapel door far behind", {"onani": True}),
 ("inochi_boss", "boss", "hall", "from side, at night in the hall of banners, he sits on the paladin's lap facing him on the commander's chair, the paladin kisses him deeply while penetrating his anus, anal, a faint light blue crest glowing on his lower belly, his own penis separate", {"insert": True}),
 ("onedari_boss", "boss", "guard", "he kneels on the rug before the fireplace begging, hugging a ledger to his chest, the paladin stands over him tilting a vial, " + JELLY + ", firelight", {}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him the knights' servant.", **opt)

# ---- オナニーCG（その相手の得意技に合わせた自慰）
ONACT = {
    "m": "kneeling upright, one wet fingertip rubbing his right nipple, the other hand pinching his left nipple hard, hands far away from his crotch, penis untouched",
    "e1": "face down with his hips raised, one arm reaching behind with trembling fingers in his own anus, penis untouched",
    "e2": "lying on his back holding his own wrists together above his head, ankles pressed together as if bound, eyes closed, back arched, penis untouched",
    "e3": "sitting with knees up, one hand pressing his own perineum below the cage, the other arm reaching behind with a finger in his own anus, not touching the cage",
    "boss": "kneeling upright, one hand pressing his own perineum, the other arm reaching behind with two fingers in his own anus, penis untouched",
}
ON = {"master": ("interrog", "m"), "e1": ("yard", "e1"), "e2": ("library", "e2"), "e3": ("watch", "e3"), "boss": ("chapel", "boss")}
for k, (place, who) in ON.items():
    scene("onanie_" + k, who, place, ONACT[who] + ", flushed, sweat, trembling",
          "he pleasures himself during the card battle while the knight watches from afar.", onani=True, cage=(who == "e3"))

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "pointing forward giving an order toward viewer, banners behind him, torchlight", "hall"),
    ("magic_2", "m", "holding up a parchment with a wax seal toward viewer, the other hand on the sword hilt, pov", "office"),
    ("magic_3", "e3", "on the watchtower lighting a signal fire, smoke rising, looking back at viewer with a lazy smile", "watch"),
    ("magic_4", "e1", "standing under a heavy iron portcullis being lowered, grinning, wooden sword on the shoulder", "yard"),
    ("magic_5", "m", "standing beside the leather strapped chair holding a bottle of holy water, beckoning with one finger, pov", "interrog"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "sensitive", "solo, 1boy", c["tags"], act, "looking at viewer", ROOM, PL[place]]), NEG_CORE + NEG_SOLO)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Knight", "images": images}, open(os.path.join(here, "knight_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
