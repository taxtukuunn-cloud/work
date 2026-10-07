# -*- coding: utf-8 -*-
"""N23 足の女王様（Heels）画像プロンプト生成 → heels_prompts.json（52枚）
N22 Prison の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
主人公は侍女のドレスを着せられた後の姿（女装モード）で描く。責め手は常に服を着ている。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, watermark, signature, text, letters, sign, logo, numbers, "
            "child, loli, shota, young, teenage, underage, petite female, muscular, abs, pectorals, bara, hairy, "
            "childlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, small body, petite male, boy, "
            "twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the man, 2boys, futanari, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies, "
            "blood, injury, whip, whipping, crying in pain")
# 女装モード：主人公も女物を着るので、女の子2人・百合と取り違えないように
NEG_SCENE = (", 2girls, yuri, pussy, vagina, breasts on the man, cleavage on the man, long hair on the man, wig, "
             "black hair on the man, blonde hair on the man, blue hair on the woman, navy hair on the woman, maid apron on the woman in black bondage dress")
NEG_WOMAN_NOMAID = ", apron on the woman, maid headdress on the woman, maid dress on the woman, hair over eyes on the woman, woman with hidden eyes, solo"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis"
NEG_NOSTRAP = ", strap-on, dildo"
NEG_ONANI = (", woman touching him, hetero sex, hand on penis, holding penis, stroking penis, handjob, penis grab, "
             "woman masturbating, girl in foreground, hand on crotch, hand on own penis")

SALON = "luxurious black salon, black walls, deep red carpet, gold candlelight"

# 2026-09-26 LoRA撮り直しで変更：petite/short/androgynous/narrow shoulders の組み合わせは幼く見えるため使わない（N21の教訓）。
# 小柄さは「相手より頭ひとつ低い」で表す。
PROT_BODY = ("1boy, male, adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, "
             "defined jawline, adam's apple, collarbones, flat male chest, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, "
             "smooth pale skin, blush, he is a head shorter than her, height difference")
MAID = ("crossdressing adult man, he wears a black knee-length maid dress with a white collar and a white frilled apron, "
        "black thigh-high garter stockings, garter belt, black strap shoes, flat male chest")

CH = {
    "m": dict(seed="CLAUDIA",
              tags="1girl, dominatrix, mature female, adult woman, tall, very long legs, long straight black hair, blunt bangs above her eyebrows, both red eyes clearly visible, smug, "
                   "black glossy latex bondage dress with a red corset belt, long black opera gloves, black patent stiletto high heels with red soles, sheer black stockings, large breasts",
              name="the tall black-haired dominatrix in a black bondage dress and red-soled stiletto heels"),
    "e1": dict(seed="MINA",
               tags="1girl, adult woman, blonde hair, bob cut, green eyes, teasing smile, "
                    "classic black maid uniform with a short skirt, black pantyhose, medium breasts",
               name="the blonde bob-haired maid in black pantyhose"),
    "e2": dict(seed="ZARA",
               tags="1girl, adult woman, tall, short red hair, side-swept bangs, both gold eyes clearly visible, cold expression, "
                    "black leather bodysuit, black leather gloves, holding a thin riding crop, knee-high leather boots, medium breasts",
               name="the red short-haired trainer in black leather with gloves and a riding crop"),
    "e3": dict(seed="RITA",
               tags="1girl, adult woman, brown hair, long hair, brown eyes, gentle diligent smile, "
                    "long dark brown maid dress, white apron, white headdress, medium breasts",
               name="the brown long-haired maid in a long dark brown maid dress"),
    "boss": dict(seed="AUGUSTA",
                 tags="1girl, empress, mature female, adult woman, very tall, platinum blonde hair, curly hair, long hair, purple eyes, regal, "
                      "purple and platinum royal gown, golden crown, high heels, large breasts",
                 name="the very tall platinum-haired empress in a purple royal gown and crown"),
}

PL = {
    "throne": "throne room, black throne, red carpet runway, low black velvet ottoman in front of the throne, candelabras, detailed background",
    "shoes":  "shoe room, walls of shelves full of high heels, velvet bench, soft lamp light, detailed background",
    "hall":   "grand entrance hall, black marble floor, red-carpeted staircase, tall double doors, chandelier, detailed background",
    "vanity": "dressing room with a large three-panel mirror vanity, perfume bottles, velvet chaise longue, detailed background",
    "wardrobe": "wardrobe room, racks of black maid dresses and stockings, dress form, detailed background",
    "tailor": "tailoring room, measuring platform, bolts of black fabric, dress forms, tape measure, detailed background",
    "door":   "narrow service back door of the salon at night, lantern, detailed background",
    "maids":  "maids' room, row of small beds, white sheets, morning light, detailed background",
    "laundry": "laundry room, stockings hanging on drying lines, wooden tubs, detailed background",
    "stairs": "narrow servants' staircase, dim lamp, detailed background",
    "mirror": "mirrored training room, black leather long bench, mirrors on every wall, detailed background",
    "peep":   "small side room with a peephole window, dim light, detailed background",
    "terrace": "rooftop terrace at night, stone balustrade, city lights below, moon, detailed background",
    "desk":   "trainer's office, heavy black desk, papers, lamp, detailed background",
    "service": "service room, white bed, bottles of scented oil, white curtains, soft light, detailed background",
    "bath":   "marble bathroom, large marble bathtub, steam, candles, detailed background",
    "guest":  "elegant guest room, wardrobe, travel bag, detailed background",
    "pantry": "maids' waiting room, small table with a service bell, detailed background",
    "audience": "empress's audience hall upstairs, white-gold and purple throne, purple carpet, tall pillars, detailed background",
    "grand":  "palace-like grand staircase with landings, white marble, purple carpet, detailed background",
    "bed":    "empress's bedchamber, huge bed with a purple canopy, gold posts, detailed background",
}

CLOTHED = "the women keep their clothes on, fully clothed females, only the man is dressed in a maid outfit"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Heels_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, strap=False, insert=False, onani=False, extra_women=""):
    c = CH[who]
    body = PROT_BODY + ", " + MAID
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", body,
                         "the navy-haired adult man in a maid dress is the main subject in the foreground, he pleasures himself without touching his penis, both of his hands are clearly away from his penis, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         SALON, PL[place], desc])
    else:
        women = c["tags"] + (", black leather strap-on harness worn over her dress, black strap-on" if strap else "")
        duo = "" if extra_women else "1girl, 1boy, duo, two people, "
        pos = ", ".join([Q, "explicit", duo + "THE WOMAN: " + women + extra_women,
                         "THE MAN (smaller, clearly visible in the picture): " + body, action, CLOTHED, SALON, PL[place], desc])
    neg = NEG_BASE + NEG_SCENE + ("" if who in ("e1", "e3") else NEG_WOMAN_NOMAID) + ("" if strap else NEG_NOSTRAP) + (NEG_INSERT if (insert or strap) else "") + (NEG_ONANI if onani else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing, one leg forward showing a red-soled stiletto heel, hand on her hip, looking down at viewer, from below, smug"),
    "e1": ("e1", "standing, holding a pair of black stockings stretched between her hands, teasing smile, winking"),
    "e2": ("e2", "standing, pointing the riding crop toward viewer, other hand on her hip, cold stare"),
    "e3": ("e3", "standing, hands folded in front of her apron, polite bow, gentle smile, holding a small bottle of oil"),
    "boss": ("boss", "standing tall, holding a scepter, looking down at viewer, from below, regal, imposing"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]), NEG_BASE, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "luxurious black salon throne room, black walls, deep red carpet, black throne, "
                           "low black velvet ottoman, gold candelabras, shelves of red-soled high heels, detailed background"]), NEG_BASE)

# ---- 女装娘カード（侍女にされた男モンスター。主人公とは別人：茶髪・がっしり過ぎない成人男性）
add("josou", "JOSOU", ", ".join([Q, "safe, solo, 1boy, adult man, mature male, 27 years old, adult proportions, adam's apple, crossdressing, brown messy short hair, embarrassed, blush, looking away, "
                                 "black knee-length maid dress, white apron, white collar, black garter stockings, holding down his skirt hem, full body, simple background, white background"]),
    NEG_BASE + ", 1girl, breasts", rembg=True)

# ---- 技CG
scene("atk_m1", "m", "throne",
      "she sits on the black throne with legs crossed, he kneels at her feet with his skirt lifted, she presses the red sole of her stiletto heel against his crotch, footjob, shoejob, from side, looking down at him",
      "the queen tramples him with her heel.")
scene("atk_m2", "m", "wardrobe",
      "she stands behind him and pulls a black stocking up his thigh, her fingers caressing his leg through the fabric, he trembles in front of a mirror, half dressed as a maid",
      "the queen dresses him as her maid piece by piece.")
scene("atk_m3", "m", "throne",
      "from side, he lies on his back on the low ottoman in front of the throne, maid dress neckline pulled down exposing his flat chest, she stands and pegs his anus with her strap-on, anal, "
      "her other leg raised with the stiletto heel resting on his nipple, one hand on the throne armrest",
      "the queen treads on his chest while taking him.", strap=True, insert=True)
scene("atk_e1", "e1", "maids",
      "he sits on the edge of a small bed, she kneels and rolls a black stocking up his leg, her fingers stroking his thigh, teasing smile",
      "the maid puts stockings on him.")
scene("atk_e2", "e2", "mirror",
      "she stands behind him, her lips at his ear, giving orders, her riding crop pointing at his chin without touching, he stands at attention with hands behind his back, dazed eyes, "
      "small pink egg vibrators under the bodice of his maid dress on his nipples",
      "the trainer conditions him with commands.")
scene("atk_e3", "e3", "service",
      "from behind, he is on all fours on the white bed, maid skirt flipped up, she kneels behind him and licks his anus, anilingus, her hands holding his hips, polite diligent face",
      "the service maid serves him with her tongue on the queen's orders.")
scene("atk_boss", "boss", "audience",
      "from side, he kneels on all fours on the purple carpet in his maid dress, neckline pulled down, the empress stands behind him and pegs him with her strap-on, anal, "
      "two maids kneel on either side licking his nipples: a blonde bob maid on the left and a brown long-haired maid on the right",
      "the empress takes him while her maids lick his chest.", strap=True, insert=True,
      extra_women=", 3girls, two maids assisting: blonde bob-haired maid in black pantyhose, brown long-haired maid in a brown maid dress")

# ---- 敗北28（主人公と主役の責め手。boss の同時技だけ侍女2人を描く）
TWO_MAIDS = ", 3girls, two maids assisting: blonde bob-haired maid in black pantyhose, brown long-haired maid in a brown maid dress"
L = [
 ("btl_m1", "m", "throne", "she sits on the throne, he kneels on the red carpet with his skirt lifted, she rubs his crotch with the sole of her red-soled stiletto, footjob, cum on her shoe, a silver heel-shaped anklet on his ankle", {}),
 ("onani_m1", "m", "shoes", "from above, he lies face down on the carpet in front of the shoe shelves, she stands over him and presses her stiletto heel on his back, three pairs of heels lined up beside them", {}),
 ("inochi_m1", "m", "hall", "the dominatrix stands behind him, at the tall double doors, the hem of his maid skirt is pinned to the marble floor by her stiletto heel, he reaches for the door handle, a black ribbon tied around his ankle", {}),
 ("onedari_m1", "m", "vanity", "she sits on the velvet chaise longue in front of the three-panel mirror, he kneels begging, her stockinged bare foot pressing his crotch, footjob, her heels removed beside her, a small silver bell on his neck", {}),
 ("btl_m2", "m", "wardrobe", "she stands behind him tying the ribbon of his white apron, her hand caressing his chest through the dress fabric, he trembles and climaxes in the mirror, white lace choker collar", {}),
 ("onani_m2", "m", "vanity", "he lies face down on the carpet in front of the three-panel mirror in his maid dress, she places her heel on his lower back, his reflections in three mirrors", {}),
 ("inochi_m2", "m", "door", "at the back door she holds out a new folded maid dress, he stands half dressed in another maid dress, her heel stepping on his skirt hem, a small key on a chain at her chest", {}),
 ("onedari_m2", "m", "tailor", "he stands on the measuring platform in a basted maid dress, she wraps a tape measure around his waist, her heel pressing between his legs over the skirt, bolts of black fabric", {}),
 ("btl_m3", "m", "throne", "from side, he lies on his back on the ottoman with legs raised, neckline pulled down, she pegs him with her strap-on, anal, her stiletto heel on his nipple, cum, black velvet cloth on the ottoman", {"strap": True, "insert": True}),
 ("onani_m3", "m", "throne", "night, only candles, from side, his wrists tied with a black ribbon, he lies on the ottoman, she pegs him with her strap-on, anal, her heel on his chest, candle flames", {"strap": True, "insert": True}),
 ("inochi_m3", "m", "throne", "from side, near the throne room door he is bent over the ottoman, she stands behind him with oiled fingers in his anus, anal fingering, her strap-on ready, a small chair beside the throne", {"strap": True, "insert": True}),
 ("onedari_m3", "m", "throne", "from side, on the red carpet runway he lies on his back begging, she pegs him deeply with her strap-on, anal, her heel pressing his nipple, a tiny pair of red-soled shoes on his feet", {"strap": True, "insert": True}),
 ("btl_e1", "e1", "maids", "from side, the navy-haired man lies on his back on a small bed in his maid dress with his skirt lifted, she sits at the foot of the bed and rubs his crotch with her pantyhose-clad soles, footjob, teasing smile", {}),
 ("onani_e1", "e1", "laundry", "from side, among stockings hanging on drying lines, the navy-haired man sits on a stool in his maid dress with his skirt lifted, she stands and presses her pantyhose sole between his legs, footjob, a stocking dangling from her hand", {}),
 ("inochi_e1", "e1", "stairs", "from side, on the servants' staircase the navy-haired man in a maid dress sits on a step, she kneels a step below rolling a new black stocking up his leg, a garter ring on his thigh", {}),
 ("onedari_e1", "e1", "maids", "morning, at a white vanity table he sits in his maid dress, she stands and presses her pantyhose foot on his lap, footjob, fishnet stockings over his black stockings", {}),
 ("btl_e2", "e2", "mirror", "he stands at attention in front of the mirrors, she whispers orders into his ear from behind, hands-free orgasm, trembling, egg vibrators under his bodice, a small silver whistle on his neck", {}),
 ("onani_e2", "e2", "peep", "the navy-haired man in a maid dress stands alone in the middle of a small dim room, eyes closed, hands clasped behind his back, trembling, hands-free; far behind him the red-haired woman in a black leather bodysuit watches through a small window in the wall, holding a black notebook", {}),
 ("inochi_e2", "e2", "terrace", "night, at the balustrade the navy-haired man in a maid dress kneels on the stone floor, she stands behind him holding a small remote control, egg vibrators under his bodice, city lights", {}),
 ("onedari_e2", "e2", "desk", "the red-haired woman in a black leather bodysuit sits in an armchair behind the black desk turning a small dial, in front of the desk stands the navy-haired man in a maid dress holding a sheet of paper and reading it aloud, trembling, small pink egg vibrators under his bodice", {}),
 ("btl_e3", "e3", "service", "from behind, he is on all fours on the white bed with his skirt flipped up, she licks his anus, anilingus, a small bottle of scented oil on the bed", {}),
 ("onani_e3", "e3", "bath", "at the marble bathtub, he leans over the edge in a wet maid dress with his skirt lifted, she kneels behind him and licks his anus, anilingus, steam", {}),
 ("inochi_e3", "e3", "guest", "he bends over the bed in the guest room with his skirt lifted, she kneels behind him inserting a small black vibrator into his anus after oiling it, anal, travel bag on the floor", {"insert": True}),
 ("onedari_e3", "e3", "pantry", "from behind, he kneels on a chair with his skirt lifted, she kneels behind him with two oiled fingers in his anus, anal fingering, a service bell on the table", {"insert": True}),
 ("btl_boss", "boss", "audience", "from side, he kneels on all fours in his maid dress, neckline pulled down, she pegs him with her strap-on, anal, two maids lick his nipples on both sides, a white-gold collar with a purple gem on his neck", {"strap": True, "insert": True, "two": True}),
 ("onani_boss", "boss", "audience", "from side, he is on all fours as her footstool, her high heels resting on a small purple cushion on his back, she sits on the throne, he trembles", {}),
 ("inochi_boss", "boss", "grand", "on a landing of the grand staircase he kneels, she stands one step above and pegs him from behind with her strap-on, anal, two maids lick his nipples", {"strap": True, "insert": True, "two": True}),
 ("onedari_boss", "boss", "bed", "on the bed under the purple canopy, he lies on his back with legs raised, she pegs him with her strap-on, anal, two maids lick his nipples on both sides, a purple armband with a gold crest on his sleeve", {"strap": True, "insert": True, "two": True}),
]
for key, who, place, action, opt in L:
    two = opt.pop("two", False)
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him her maid forever.", extra_women=TWO_MAIDS if two else "", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "throne", "lying face down on the red carpet with his hips raised, rubbing his flat chest against the carpet, hands flat on the floor, not touching his penis, imagining a heel on his back, flushed"),
    "e1": ("e1", "maids", "sitting on a small bed, stroking his own inner thighs over black stockings, one finger pressing between his buttocks over the skirt, not touching his penis, flushed"),
    "e2": ("e2", "mirror", "standing at attention with hands clasped behind his back, hands-free, eyes closed, trembling, open mouth, not touching himself"),
    "e3": ("e3", "service", "from behind, kneeling on the bed with his skirt lifted, reaching back and stroking his own anus with a wet finger, not touching his penis"),
    "boss": ("boss", "audience", "kneeling, one wet finger rubbing his own nipple through the opened neckline, other hand reaching behind with two fingers in his own anus, not touching his penis, drooling"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in her style while she watches from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "pointing at the floor with one finger, commanding, looking down at viewer, from below, stiletto heels", "throne"),
    ("magic_2", "e1", "holding up a black maid dress and a pair of black stockings toward viewer, teasing smile", "wardrobe"),
    ("magic_3", "m", "holding a black envelope sealed with red wax toward viewer, smug", "hall"),
    ("magic_4", "m", "standing on the red carpet, one stiletto heel stepping forward toward viewer, from below, the carpet stretching into darkness", "hall"),
    ("magic_5", "m", "sitting on the black throne with legs crossed, a low black ottoman in front of her, looking down at viewer, from below", "throne"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", SALON, PL[place]]), NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Heels", "images": images}, open(os.path.join(here, "heels_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
