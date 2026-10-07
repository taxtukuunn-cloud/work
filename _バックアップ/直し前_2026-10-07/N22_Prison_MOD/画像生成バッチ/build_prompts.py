# -*- coding: utf-8 -*-
"""N22 女看守の監獄（Prison）画像プロンプト生成 → prison_prompts.json（51枚）
N17 Scylla の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, numbers, "
            "child, loli, shota, young, teenage, underage, petite female, flat chest female, muscular, abs, pectorals, bara, hairy, "
            "collar, choker, leash, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the man, 2boys, futanari, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies, "
            "blood, injury, whip, crying in pain, "
            "childlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, "
            "small body, petite male, young boy, kid")
NEG_SCENE = ", pussy, vagina, breasts on the man, long hair on the man, black hair on the man, brown hair on the man, blonde hair on the man, purple hair on the man, grey hair on the man, uniform on the man, garter belt on the man, stockings on the man, harness on the man, peaked cap on the man, blue hair on the woman"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis"
NEG_NOSTRAP = ", strap-on, dildo"
NEG_ONANI = ", woman touching him, hetero sex, hand on penis, holding penis, stroking penis, handjob, penis on the woman, woman masturbating, girl in foreground, hand on crotch, hand near penis, touching penis"
NEG_CAGE = ", erection, large penis"

PRISON = "stone prison interior, cold grey stone walls, iron bars, dim light"

PROT = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult man, mature male, "
        "25 years old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, "
        "adam's apple, collarbones, flat male chest, smooth pale skin, blush, height difference, nude male, completely naked, "
        "ordinary human man, he is a head shorter than the woman")
CAGE = "small flat metal chastity cage on his penis, chastity belt, thin metal waist strap, flaccid penis locked in the cage"

CH = {
    "m": dict(seed="ISABEL",
              tags="1girl, mature female, adult woman, mature face, sharp adult features, adult proportions, long legs, tall, black hair, tied hair, neat hair bun, grey eyes, stern, "
                   "black prison warden uniform, black peaked cap, white gloves, ring of keys on her belt, black skirt, black pantyhose, large breasts",
              name="the tall black-haired warden in a black uniform, peaked cap and white gloves"),
    "e1": dict(seed="KEI",
               tags="1girl, adult woman, mature face, sharp adult features, 25 years old, adult proportions, long legs, brown hair, short hair, brown eyes, serious, "
                    "navy grey prison guard uniform, guard cap, small notebook, medium breasts",
               name="the brown-haired woman guard in a grey guard uniform holding a notebook"),
    "e2": dict(seed="DORA",
               tags="1girl, adult woman, mature face, sharp adult features, 25 years old, adult proportions, long legs, blonde hair, hair bun, green eyes, cold expression, "
                    "white lab coat over a grey uniform, red armband, black latex gloves, medium breasts",
               name="the blonde doctor in a white lab coat with black latex gloves"),
    "e3": dict(seed="VIOLA",
               tags="1girl, adult woman, mature face, sharp adult features, 25 years old, adult proportions, long legs, purple hair, wavy hair, long hair, purple eyes, sly smile, "
                    "dark purple interrogator suit, white shirt, pencil skirt, black knee-high boots, medium breasts",
               name="the purple-haired interrogator in a dark purple suit and black knee-high boots"),
    "boss": dict(seed="MAGDALENA",
                 tags="1girl, mature female, adult woman, mature face, sharp adult features, adult proportions, long legs, very tall, grey hair, very long hair, black eyes, imposing, "
                      "dark green military style uniform with gold buttons, long black greatcoat on her shoulders, black leather gloves, large breasts",
                 name="the very tall grey-haired governor in a military style uniform and a long black greatcoat"),
}

PL = {
    "exam":   "prison medical examination room, white tiled walls and floor, metal examination table, large mirror on the wall, bright cold light, detailed background",
    "intake": "prison intake room, height chart on the wall, shelves of metal number tags, wooden counter, detailed background",
    "cell":   "small prison cell at night, stone walls, iron bed, small barred window with moonlight, iron door with a peephole, detailed background",
    "pun":    "underground punishment cell, dark stone walls, iron bed, iron rings on the wall, tiny skylight, candle light, detailed background",
    "office": "warden's office, heavy wooden desk with papers, wall of hanging keys, desk lamp, detailed background",
    "med":    "prison infirmary, white curtains, examination chair, instrument shelves with glass bottles, detailed background",
    "inter":  "interrogation room, single table, one hanging lamp, two chairs, dark walls, detailed background",
    "corr":   "prison corridor lined with cell doors, rule board on the wall without letters, lanterns, detailed background",
    "gov":    "governor's office at the top of a stone tower, huge dark desk, wall covered with hundreds of hanging keys, tall window, detailed background",
    "priv":   "governor's private room, fireplace, leather armchair, dark wood, warm firelight, detailed background",
    "gate":   "inner side of the huge iron prison gate at night, stone archway, torches, detailed background",
    "visit":  "prison visiting room divided by iron bars, table on each side, detailed background",
}

CLOTHED = "the woman keeps her uniform on, fully clothed female, only the man is naked"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Prison_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, strap=False, insert=False, onani=False, cage=True):
    c = CH[who]
    body = PROT + (", " + CAGE if cage else "")
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", body,
                         "the naked navy-haired adult man is the main subject in the foreground, he pleasures himself without touching his penis, "
                         "both of his hands are clearly away from his penis, " + action,
                         "a small distant woman in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         PRISON, PL[place], desc])
    else:
        pos = ", ".join([Q, "explicit", c["tags"] + (", strap-on harness over her uniform skirt, black strap-on" if strap else ""), body,
                         action, CLOTHED, PRISON, PL[place], desc])
    neg = NEG_BASE + NEG_SCENE + (NEG_CAGE if cage else "") + ("" if strap else NEG_NOSTRAP) + (NEG_INSERT if (insert or strap) else "") + (NEG_ONANI if onani else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing upright, one gloved hand holding a ring of keys, other hand on her hip, looking down at viewer, stern"),
    "e1": ("e1", "standing at attention, holding an open notebook, reading aloud, serious face"),
    "e2": ("e2", "standing, snapping on a black latex glove, holding a thin metal rod, cold stare"),
    "e3": ("e3", "standing with one hand on her hip, finger on her lips, sly smile, half-closed eyes"),
    "boss": ("boss", "standing tall with arms crossed, greatcoat on her shoulders, looking down at viewer, imposing"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]),
        NEG_BASE, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "examination room of an old stone prison, white tiled walls, iron barred door, "
                           "metal examination table, large mirror, cold light from a high barred window, detailed background"]), NEG_BASE)

# ---- 技CG
scene("atk_m1", "m", "exam",
      "from front, he stands with both hands behind his head, she stands in front of him and pinches both of his nipples with her white gloved fingers, erect nipples, trembling",
      "the warden inspects his nipples with her white gloves.")
scene("atk_m2", "m", "intake",
      "from front, she kneels in front of him and locks the chastity cage with a small key, her gloved fingers pressing under the cage, he looks down, trembling, precum dripping from the cage",
      "the warden locks his chastity cage and inspects it.")
scene("atk_m3", "m", "pun",
      "from side, he is on all fours on the iron bed, she stands behind him and pegs his anus with her strap-on, anal, "
      "a thin metal rod with small beads inserted into the tip of his caged penis, urethral insertion",
      "the warden punishes him from the front and from behind at once.", strap=True, insert=True)
scene("atk_e1", "e1", "corr",
      "she stands behind him, girl behind boy, her lips at his ear, reading from her notebook, he stands with hands behind his head, dazed, open mouth, drooling",
      "the guard makes him recite the prison rules into his ear.")
scene("atk_e2", "e2", "med",
      "from side, he lies on the examination chair with legs spread in stirrups, she inserts a thin metal rod with small beads into his penis tip, urethral insertion, "
      "her other gloved fingers in his anus, anal fingering, clear blue jelly",
      "the doctor examines his urethra and anus at the same time.", insert=True, cage=False)
scene("atk_e3", "e3", "inter",
      "he sits on a chair, she leans over him and kisses him deeply, tongue, saliva string, her hand pinching his nipple, her booted foot between his legs",
      "the interrogator draws his confession out with a deep kiss.")
scene("atk_boss", "boss", "gov",
      "from side, he is bent over the huge desk, she stands behind him and pushes two gloved fingers into his anus, anal fingering, prostate massage, "
      "white fluid dripping from his chastity cage onto the floor",
      "the governor milks his prostate while he stays locked in chastity.")

# ---- 敗北28（1枚に描くのは主人公と主役の責め手だけ）
L = [
 ("btl_m1", "m", "exam", "from front, he stands in front of the large mirror with hands behind his head, she stands behind him and pinches both nipples with white gloved fingers, a metal number tag hanging from his neck, cum leaking from the chastity cage, trembling knees", {}),
 ("onani_m1", "m", "cell", "she opens the iron door and looks at him with a lantern, he kneels on the iron bed, pinching his own nipples, flushed, embarrassed", {}),
 ("inochi_m1", "m", "office", "he stands naked in front of her desk, she sits and holds a signed paper, her gloved fingers pinching his nipple across the desk, pen on the desk", {}),
 ("onedari_m1", "m", "exam", "he stands in front of the mirror with hands behind his head, begging, open mouth, she inspects his nipples with gloved fingers from behind, looking at the mirror", {}),
 ("btl_m2", "m", "intake", "from front, he stands against the height chart, she kneels and taps the chastity cage with a key, white fluid leaking through the cage slits, a tiny key on a thin chain around her neck", {}),
 ("onani_m2", "m", "cell", "he lies on the iron bed, legs spread, pressing his perineum with his fingers, the chastity cage untouched, she stands at the door holding a smaller chastity cage", {}),
 ("inochi_m2", "m", "office", "she sits on the desk with legs crossed, lifts the small key on the chain around her neck, he kneels in front of her, her boot tip under his chastity cage", {}),
 ("onedari_m2", "m", "office", "he kneels with hands behind his back, looking up, begging, she crouches and rubs his chastity cage with her gloved fingers, hourglass on the desk", {}),
 ("btl_m3", "m", "pun", "from side, on all fours on the iron bed, she pegs his anus from behind with her strap-on, anal, a thin beaded metal rod in his penis tip, urethral insertion, cum, arched back", {"strap": True, "insert": True}),
 ("onani_m3", "m", "pun", "from side, the naked navy-haired man is on all fours on the iron bed, the black-haired warden in uniform kneels behind him and pegs his anus with her black strap-on, anal, his number tag hanging on the cell door, drooling, tears of pleasure", {"strap": True, "insert": True}),
 ("inochi_m3", "m", "pun", "from side, he lies on his back on the iron bed with legs raised, she holds his legs and pegs him with her strap-on, anal, a key hanging on the iron ring on the wall", {"strap": True, "insert": True}),
 ("onedari_m3", "m", "pun", "from behind, she applies clear blue jelly and pushes two gloved fingers into his anus, anal fingering, preparing him, her strap-on visible, he looks back begging", {"strap": True, "insert": True}),
 ("btl_e1", "e1", "corr", "he stands in front of the rule board with hands behind his head, she whispers into his ear reading from her notebook, hands-free orgasm, white fluid leaking from the chastity cage, dazed eyes", {}),
 ("onani_e1", "e1", "exam", "from side, he is on all fours on the metal table, she pushes large anal beads into his anus one by one while reading from her notebook, anal beads, anal", {"insert": True}),
 ("inochi_e1", "e1", "cell", "night duty room with a small bed and a candle, she sits beside him and reads from a thick bound book of rules, he recites with his eyes half closed, blushing, trembling", {}),
 ("onedari_e1", "e1", "exam", "from side, he kneels on the metal table, raising his hips, begging, she holds a string of large anal beads, three beads already inside, anal beads", {"insert": True}),
 ("btl_e2", "e2", "med", "from side, he lies on the examination chair, legs in stirrups, a beaded metal rod in his penis tip, urethral insertion, her gloved fingers in his anus, anal fingering, blue jelly, cum", {"insert": True, "cage": False}),
 ("onani_e2", "e2", "med", "he lies on the infirmary bed at night, a small egg-shaped vibrator taped to each nipple, she writes on a clipboard beside the bed, he trembles, flushed", {}),
 ("inochi_e2", "e2", "med", "he sits on the examination chair, she sits at her desk writing a medical certificate, a thin beaded metal rod in his penis tip, urethral insertion, trembling", {"insert": True, "cage": False}),
 ("onedari_e2", "e2", "med", "he lies back on the examination chair, begging, pink egg vibrators taped on his nipples, she turns a small dial, clipboard", {}),
 ("btl_e3", "e3", "inter", "he sits on the chair, she sits on the table and kisses him deeply, french kiss, tongue, saliva string, her gloved hand pinching his nipple, signed paper on the table", {}),
 ("onani_e3", "e3", "inter", "she grabs his chin and kisses him deeply, tongue, saliva, he was sucking his own fingers, his fingers wet, her boot pressing his thigh", {}),
 ("inochi_e3", "e3", "inter", "night, lamp light, she straddles the chair in front of him and kisses him, tongue, saliva string, he trembles, open notebook on the table", {}),
 ("onedari_e3", "e3", "inter", "he kneels on the floor, looking up, begging with open mouth, she bends down to kiss him, tongue out, her knee-high boot on his thigh", {}),
 ("btl_boss", "boss", "gov", "from side, he is bent over the huge desk, she stands behind him with two gloved fingers in his anus, anal fingering, prostate massage, white fluid dripping from the chastity cage, a paper on the desk", {}),
 ("onani_boss", "boss", "gov", "he kneels in front of the wall of keys, she stands behind him, one hand holding up a key, other gloved hand pinching his nipple, he is dazed, drooling, white fluid leaking from the chastity cage", {}),
 ("inochi_boss", "boss", "gate", "from side, at the iron gate at night he bends forward holding the bars, she stands behind him with gloved fingers in his anus, anal fingering, prostate massage, torches", {}),
 ("onedari_boss", "boss", "priv", "she sits in the leather armchair by the fireplace, he kneels between her boots with his back to her, her gloved fingers in his anus from behind, anal fingering, she holds a key in her other hand", {}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him a prisoner for life.", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "cell", "standing upright at attention next to the iron bed, one hand reaching behind him fingering his own anus, other hand pressing his perineum, chastity cage untouched, trembling"),
    "e1": ("e1", "cell", "kneeling on the iron bed, hands on his knees, hands-free, reciting aloud with open mouth, dazed, twitching, trembling"),
    "e2": ("e2", "med", "from side, lying on the infirmary bed with legs raised, one hand pressing his perineum, other hand fingering his own anus, trembling"),
    "e3": ("e3", "inter", "sitting on the chair, sucking two fingers of one hand, other hand rolling his own nipple between wet fingers, flushed"),
    "boss": ("boss", "gov", "from side, on his knees bent forward, one hand reaching behind him with two fingers in his own anus, pressing rhythmically, drooling"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in her style while she watches from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "reading out a long paper in her gloved hands, stern, looking down at viewer", "office"),
    ("magic_2", "e2", "holding up a small flat metal chastity cage and a tiny key toward viewer, cold stare", "med"),
    ("magic_3", "m", "opening a heavy iron cell door with a big key, looking back at viewer", "pun"),
    ("magic_4", "m", "ringing her ring of keys with one hand raised, footsteps of guards approaching in the corridor behind her", "corr"),
    ("magic_5", "e1", "pulling a lever, iron bars dropping down behind her, pointing at viewer", "corr"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", PRISON, PL[place]]), NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Prison", "images": images}, open(os.path.join(here, "prison_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
