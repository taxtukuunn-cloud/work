# -*- coding: utf-8 -*-
"""N18 Lamia: lamia_prompts.json と読む用プロンプト一覧を作る（52枚）。"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, speech bubble, comic, english text, "
            "child, loli, shota, young, teenage, underage, flat chest female, muscular, abs, pectorals, bara, hairy, "
            "collar, choker, leash, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "human legs on the lamia, eyes visible on the man, 2boys, vaginal, penetration by male, nude female, "
            "female nudity, topless female, exposed female breasts, breasts out, female nipples, merged bodies, vore, swallowing, eating, blood, injury, "
            "the man touching the woman, groping, human legs on the woman, female legs, female feet, barefoot woman, thighs on the woman, pantyhose, stockings, kneeling woman")
NEG = NEG_BASE + ", futanari"
NEG_MALE = (", pussy, vagina, breasts on the man, long hair on the man, snake tail on the man, scales on the man, "
            "green hair on the man, yellow hair on the man, black hair on the man, red hair on the man, blonde hair on the man")
NEG_TOOL = ", dildo, sex toy, strap-on, penis on the woman"
NEG_FUTA = ", dildo, sex toy, strap-on, merged, fused, overlapping penises, penis inside the woman, the man penetrating"
NEG_STAND = ", nipples, nude, naked, topless, penis, 1boy"

C = {  # tags, English name
 "SHESKA": ("1girl, lamia, snake girl, no legs, her whole body below the waist is one thick snake tail, snake lower body, long green snake tail, green scales, mature female, adult woman, tall, "
            "green hair, long braided hair, gold hair ornaments, gold eyes, slit pupils, priestess, sheer white priestess robe, "
            "gold jewelry, long forked tongue, calm smile, large breasts",
            "the green-haired lamia priestess with a long green snake tail"),
 "VIPERA": ("1girl, lamia, snake girl, no legs, her whole body below the waist is one thick snake tail, snake lower body, yellow snake tail, yellow scales, adult woman, yellow hair, short hair, "
            "green eyes, slit pupils, light bronze armor, stern expression, forked tongue, medium breasts",
            "the yellow-haired lamia guard in bronze armor with a yellow snake tail"),
 "COBRA":  ("1girl, lamia, snake girl, no legs, her whole body below the waist is one thick snake tail, snake lower body, black snake tail, black scales, adult woman, black hair, hime cut, long hair, "
            "red eyes, slit pupils, cobra hood ornament behind her neck, small fangs, black silk dress, seductive smirk, medium breasts",
            "the black-haired cobra lamia in a black silk dress with a black snake tail"),
 "LINGUA": ("1girl, lamia, snake girl, no legs, her whole body below the waist is one thick snake tail, snake lower body, red snake tail, red scales, adult woman, red hair, hair bun, gold eyes, "
            "slit pupils, black and white maid outfit, very long tongue, polite smile, medium breasts",
            "the red-haired lamia maid with a red snake tail and a very long tongue"),
 "UROBORA":("1girl, lamia, snake girl, no legs, her whole body below the waist is one thick snake tail, giant snake lower body, extremely long white snake tail, white scales, mature female, very tall, "
            "platinum blonde hair, absurdly long hair, crimson eyes, slit pupils, gold crown, gold scale armor dress, regal, large breasts",
            "the huge white-scaled lamia queen with platinum hair and a gold crown"),
}
HERO = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult male, petite, short, "
        "slender, narrow shoulders, thin arms, smooth pale skin, no muscles, blush, height difference, "
        "he is much shorter than her, nude male, completely naked man, penis")
CLOTHED = "cfnm, clothed female, the woman keeps all her clothes on and her breasts covered, only the man is naked"
FUTA = "futanari, the lamia has a penis, her penis penetrates his anus from behind, anal, his own penis is separate and visible, side view"

ROOM = {
 "temple":    "inside an ancient desert temple, sandstone pillars, snake statues and carvings, warm torchlight, detailed background",
 "boudoir":   "priestess bedchamber in a desert temple, silk sheets spread over soft sand, oil lamps, snake carvings, detailed background",
 "mirror":    "temple hall whose floor is covered by shallow still water like a mirror, a shaft of light from a hole in the ceiling, detailed background",
 "stairs":    "long sandstone stairway leading up out of a desert temple, bright daylight at the top, detailed background",
 "idol":      "in front of a giant snake god statue, a golden hourglass on a stone altar, oil lamps, detailed background",
 "moonaltar": "round stone altar under moonlight in a ruined desert temple, detailed background",
 "shedroom":  "dim temple room with translucent shed snake skins hanging on the walls, detailed background",
 "courtyard": "temple courtyard with a fountain of flowing sand, palm trees, sunlight, detailed background",
 "makeup":    "priestess dressing room with a large bronze mirror and gold jewelry boxes, detailed background",
 "greataltar":"great altar at the feet of a colossal snake god statue, incense smoke, detailed background",
 "eyes":      "meditation hall with countless carved snake eyes on the walls glowing gold, detailed background",
 "colonnade": "long colonnade corridor of a desert temple, rows of sandstone pillars, detailed background",
 "canopy":    "bed with a canopy of sheer golden veils in a temple bedchamber, detailed background",
 "guardroom": "guard room in a watchtower at a temple entrance, a spear leaning on the wall, an hourglass on a table, detailed background",
 "cell":      "barred cell room in a guard post at night, torchlight, detailed background",
 "gate":      "temple gate opening onto desert sand dunes, bright daylight, detailed background",
 "towertop":  "top of a stone watchtower at night overlooking the desert, starry sky, detailed background",
 "incense":   "rock ledge bed with burning incense burners, thin purple smoke, dim light, detailed background",
 "eggs":      "warm sand chamber with rows of white snake eggs half buried in the sand, amber light, detailed background",
 "spring":    "small underground spring in a temple, still clear water, a black cup on the stone edge, detailed background",
 "blackroom": "private chamber with a black silk hanging hammock bed, dim red lamps, detailed background",
 "bath":      "temple bathhouse with a warm sand bath, steam, bottles of fragrant oil, detailed background",
 "maidroom":  "small servants room with a narrow bed and a candlestick, door slightly open, detailed background",
 "guestroom": "temple guest room with packed travel bags and a backpack on the floor, detailed background",
 "pantry":    "serving room beside a temple kitchen, silver trays and a small silver bell, detailed background",
 "throne":    "vast underground cavern, torches, the lamia's white snake body coiled into a huge ring like a throne, detailed background",
 "torchring": "round stone floor ringed by torches in front of a throne in a vast underground cavern, detailed background",
 "ringpath":  "circular stone passage running around the edge of a vast underground cavern, torches, detailed background",
 "queenbed":  "queen's bedchamber in an underground cavern, a round bed of white scales and gold ornaments, detailed background",
}
STATE = {
 "btl": "defeated, exhausted, limp body, tears of pleasure, cum",
 "onani": "deeply embarrassed, flustered, sweat, being watched",
 "inochi": "dazed, trembling, giving in",
 "onedari": "begging, eager, submissive posture, open mouth",
}
SEED = {"m1": "SHESKA", "m2": "SHESKA", "m3": "SHESKA", "e1": "VIPERA", "e2": "COBRA", "e3": "LINGUA", "boss": "UROBORA"}

items = []
def add(key, seed, pos, neg=NEG, rembg=False):
    items.append({"key": key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})

def scene(key, who, action, room, sentence, state="", mode=""):
    """mode: '' 通常 / 'futa' ふたなり挿入 / 'tool' 器具を出さない念押し"""
    tags, name = C[who]
    parts = [Q, "explicit", tags, HERO]
    if mode == "futa":
        parts.append(FUTA)
    parts.append(action)
    if state:
        parts.append(state)
    parts += [CLOTHED, ROOM[room], sentence.replace("{W}", name)]
    if mode == "futa":
        neg = NEG_BASE + NEG_MALE + NEG_FUTA
    else:
        neg = NEG + NEG_MALE + NEG_TOOL
    add(key, who, ", ".join(parts), neg)

# ---- 立ち絵（背景除去） ----
STAND = {
 "Lamia_master": ("SHESKA", "full body, the whole long snake tail visible and coiled on the ground, holding a gold staff, looking at viewer, forked tongue slightly out"),
 "Lamia_e1": ("VIPERA", "full body, the whole snake tail visible, holding a spear upright, looking down at viewer, arms crossed"),
 "Lamia_e2": ("COBRA", "full body, the whole snake tail visible and coiled, cobra hood spread, finger on her lips, looking at viewer"),
 "Lamia_e3": ("LINGUA", "full body, the whole snake tail visible, hands folded in front, bowing slightly, long tongue out, looking at viewer"),
 "Lamia_boss": ("UROBORA", "full body, the enormous white snake tail coiled in a huge ring around her, from below, looking down at viewer"),
}
for k, (w, pose) in STAND.items():
    add(k, w, ", ".join([Q, "safe", "solo", C[w][0], pose, "simple background, white background"]), NEG + NEG_STAND, rembg=True)

add("Lamia_bg", "BG", ", ".join([Q, "safe", "no humans, scenery", "deep inside an ancient temple in a desert ruin, tall sandstone pillars, "
    "huge carved snake statues with gold eyes, torchlight, sand on the floor, incense smoke, a dark doorway leading deeper, detailed background"]),
    NEG + ", 1girl, 1boy, people")

# ---- 技CG ----
scene("Lamia_atk_m1", "SHESKA", "from side, her green snake tail coils around his legs and waist and lifts his hips up, he is on all fours, she bends down behind him and licks his anus with her long forked tongue, anilingus, saliva, erection", "temple",
      "{W} coils her tail around him and licks him from behind with her long forked tongue.")
scene("Lamia_atk_m2", "SHESKA", "from front, her snake tail coils around his arms and waist and holds him up in front of her chest, she bends down and licks both of his nipples at once with the two tips of her forked tongue, nipple licking, saliva, erection", "temple",
      "{W} holds him in her coils and licks both of his nipples with the two tips of her forked tongue.")
scene("Lamia_atk_m3", "SHESKA", "from side, he is held from behind inside her green coils, she turns his face and kisses him deeply with her long forked tongue in his mouth, tongue kiss, saliva, his legs spread, erection", "temple",
      "{W} seals his mouth with a deep kiss of her long tongue while entering him from behind.", "", "futa")
scene("Lamia_atk_e1", "VIPERA", "from front, her yellow tail coils around his legs, she holds his face and stares into his eyes with glowing green slit pupils, hypnosis, he stands frozen, her forked tongue flicks at his nipple, erection", "guardroom",
      "{W} freezes him with her stare and flicks his nipple with her tongue.")
scene("Lamia_atk_e2", "COBRA", "from side, her black tail coils around his waist, she gently bites the side of his neck with small fangs, no blood, the thin tip of her tail teases his anus, dazed, drooling, erection", "incense",
      "{W} gently bites his neck and teases him with the thin tip of her tail.")
scene("Lamia_atk_e3", "LINGUA", "from side, her red tail coils tightly around his chest and squeezes, the coils rub his nipples, she kneels behind him and licks his anus with her very long tongue, anilingus, erection", "bath",
      "{W} coils around his chest and licks deep into him from behind.")
scene("Lamia_atk_boss", "UROBORA", "from side, he is held in the middle of her huge white coils, she licks his anus with her long forked tongue from behind, anilingus, the thin tip of her tail curls around his nipples at the same time, erection", "throne",
      "{W} licks him from behind while the tip of her tail plays with his nipples at the same time.")

# ---- 魔法・罠 ----
add("Lamia_magic_1", "SHESKA", ", ".join([Q, "safe", C["SHESKA"][0], "her snake tail forming a large inviting ring on the floor, arms open toward viewer, pov, gentle smile", ROOM["temple"]]), NEG + NEG_STAND)
add("Lamia_magic_2", "BG2", ", ".join([Q, "safe", "no humans, scenery", "a translucent shed snake skin lying on a sandstone temple floor, torchlight, shadows of a large snake behind a pillar", "detailed background"]), NEG + ", 1girl, 1boy, people")
add("Lamia_magic_3", "SHESKA", ", ".join([Q, "safe", C["SHESKA"][0], "close-up of her face, glowing gold slit-pupil eyes staring at viewer, hypnotic, pov", ROOM["eyes"]]), NEG + NEG_STAND)
add("Lamia_magic_4", "BG3", ", ".join([Q, "safe", "no humans, scenery", "white snake eggs half buried in warm sand, one egg starting to crack with soft light", ROOM["eggs"]]), NEG + ", 1girl, 1boy, people")
add("Lamia_magic_5", "BG", ", ".join([Q, "safe", "no humans, scenery", "grand hall of a desert snake temple, sand flowing down steps like a waterfall, huge snake statue, torchlight, detailed background"]), NEG + ", 1girl, 1boy, people")

# ---- 命乞い ----
scene("Lamia_inochigoi", "SHESKA", "from front, he stands holding a card raised to strike but his hand stops, she looks up at him with teary pleading eyes, her snake tail quietly curling around his ankle, erection", "temple",
      "{W} pretends to plead for mercy, and his hand stops.", STATE["inochi"])

# ---- オナニー（主人公が主役・責め手は奥で見ているだけ） ----
# v4：オナニーは相手の得意技に合わせた自慰（ペニスは使わない）
ONA = {
 "Lamia_onanie_m": ("SHESKA", "mirror", "he kneels on all fours, one wet finger only tracing the rim of his own anus from behind, not inserting, his other hand on the floor, teasing himself, hands away from his penis"),
 "Lamia_onanie_e1": ("VIPERA", "cell", "he sits on the floor pinching his own nipple between two wet fingers like a forked tongue, flicking it, both hands on his chest, hands away from his penis"),
 "Lamia_onanie_e2": ("COBRA", "eggs", "he sits on warm sand with no hands on his body except fingertips touching two small bite marks on the side of his neck, head tilted back, dazed, eyes hidden, trembling, hands-free"),
 "Lamia_onanie_e3": ("LINGUA", "maidroom", "he lies on his side on a narrow bed with one wet finger deep in his own anus from behind, searching inside, hands away from his penis"),
 "Lamia_onanie_boss": ("UROBORA", "torchring", "he lies face down with his chest pressed and rubbing on the stone floor, one wet finger stroking his own anus from behind, hips slightly raised, hands away from his penis"),
}
FAR = {  # 奥に小さく立つ責め手（タグ一式は入れない：主人公に蛇の尾が混ざるため）
 "SHESKA": "a green-haired woman in a white robe whose lower body is a green snake tail",
 "VIPERA": "a yellow-haired woman in bronze armor whose lower body is a yellow snake tail",
 "COBRA": "a black-haired woman in a black dress whose lower body is a black snake tail",
 "LINGUA": "a red-haired maid whose lower body is a red snake tail, peeking from the doorway",
 "UROBORA": "a platinum-haired queen with a crown whose lower body is a huge white snake tail, on a distant throne",
}
for k, (w, room, act) in ONA.items():
    tags, name = C[w]
    pos = ", ".join([Q, "explicit", "male masturbation, solo focus, the naked man is the main subject, large in the center foreground, 1boy", HERO,
                     "he has two normal human legs and bare feet, no tail, no scales on him",
                     act + ", erection, embarrassed, blush",
                     "far away in the background stands " + FAR[w] + ", very small in the frame, only watching him, not touching",
                     ROOM[room]])
    add(k, w, pos, NEG + NEG_MALE + NEG_TOOL + ", hand on penis, stroking penis, handjob, lamia boy, male lamia, snake tail on the man, man with snake lower body, 2boys, merged bodies, woman in the foreground")

# ---- 敗北CG 28枚 ----
L = {}
# m1 長い舌（アナル舐め）
L["btl_m1"] = ("from side, on silk sheets he lies inside her green coils with only his hips raised, three coils around his waist, a thin gold chain around his waist, she licks his anus with her long forked tongue, anilingus, ejaculation", "boudoir",
               "{W} licks him deep from behind while her tail coils him tighter.")
L["onani_m1"] = ("from front, he kneels in shallow mirror-like water and pushes his own finger into his anus, a gold ring on that finger, his reflection in the water, she beside him slowly extends her very long forked tongue to show its length, ejaculation", "mirror",
                 "{W} shows him how much deeper her tongue reaches than his finger.")
L["inochi_m1"] = ("from behind, he lies face down on the stone steps reaching toward the light, her green tail wraps his ankle and pulls him back, she licks his anus with her long tongue, anilingus, snake scale marks on his ankle", "stairs",
                  "{W} pulls him back down the stairs by the ankle and licks him.")
L["onedari_m1"] = ("from side, he kneels on all fours in front of a snake god statue with his hips raised to her, a small gold hourglass pendant on his neck, she licks his anus with her long forked tongue, anilingus, hourglass on the altar, erection", "idol",
                   "He offers himself to {W} while the hourglass runs.")
# m2 先割れの舌（乳首舐め）
L["btl_m2"] = ("from front, on a round moonlit altar her tail binds his arms behind him so his chest sticks out, she licks both of his nipples at once with the two tips of her forked tongue, gold oil shining on his chest, ejaculation", "moonaltar",
               "{W} licks both nipples at once under the moonlight.")
L["onani_m2"] = ("from front, he sits among hanging shed snake skins pinching his own nipple with his fingers, a thin translucent snake skin over his chest, she beside him flicks the two tips of her forked tongue in the air, ejaculation", "shedroom",
                 "{W} shows him her forked tongue while he tries with his fingers.")
L["inochi_m2"] = ("from front, by a sand fountain her tail suddenly coils around his waist and chest as he turns back, she licks his nipple, thin gold rings on his nipples, nipple licking, erection", "courtyard",
                  "{W} catches him as he turns back and licks his chest again.")
L["onedari_m2"] = ("from front, he sits before a bronze mirror holding his chest out, gold bracelet on his wrist, she leans over his shoulder from behind and licks his nipple with her forked tongue, their reflection in the mirror, nipple licking, erection", "makeup",
                   "{W} licks his nipple in front of the mirror as many times as he asked.")
# m3 蛇の瞳とふたなり
L["btl_m3"] = ("on the great altar he lies on his side with legs spread inside her coils, gold lipstick on his lips, she kisses him deeply with her long forked tongue, tongue kiss, saliva, ejaculation", "greataltar",
               "{W} keeps his mouth sealed with her long tongue while she takes him on the altar.", "", "futa")
L["onani_m3"] = ("he sits in her coils with gold powder on his eyelids, she holds him from behind and kisses him deeply with her long forked tongue, tongue kiss, saliva, dazed, ejaculation", "eyes",
                 "{W} takes over from his own fingers, kissing him and entering him.", "", "futa")
L["inochi_m3"] = ("he is pressed against a pillar with legs spread, her tail around his waist, a gold snake necklace on his neck, she forces a deep kiss with her long forked tongue, tongue kiss, erection", "colonnade",
                  "{W} pries his lips open with her tongue and takes him against the pillar.", "", "futa")
L["onedari_m3"] = ("on a veiled canopy bed he lies on his side and spreads his legs for her by himself, she kisses him deeply with her long forked tongue, tongue kiss, saliva, her coils around him, erection", "canopy",
                   "He asks {W} for a kiss and opens his legs as she enters him.", "", "futa")
# e1 ヴィペラ
L["btl_e1"] = ("from front, in the guard room he is pinned against the wall by her yellow tail, a small wooden tag hanging on his neck, she stares into his eyes and licks his nipple with her forked tongue, nipple licking, hourglass on the table, ejaculation", "guardroom",
               "{W} interrogates him with her stare and her tongue.")
L["onani_e1"] = ("from front, he sits on the floor of a barred cell stroking his penis and pinching his nipple, she watches through the bars with a closed notebook in her hand, ejaculation", "cell",
                 "{W} watches him through the bars on night watch.")
L["inochi_e1"] = ("from front, at the temple gate with sand dunes outside, her yellow tail coils around his ankles and waist, she holds his chin and stares into his eyes, hypnosis, yellow scale marks on his ankles, erection", "gate",
                  "{W} catches him at the gate the moment he turns his back.")
L["onedari_e1"] = ("from front, on top of the watchtower at night he kneels and holds his chest out to her, a small bell on a cord at his neck, she bends down and licks his nipple with her forked tongue, nipple licking, stars, erection", "towertop",
                   "He asks {W} for his duty at every change of the watch.")
# e2 コブラ
L["btl_e2"] = ("from side, on a rock ledge bed among incense smoke, her black tail coils around him, she gently bites the side of his neck, two tiny fang marks, no blood, dazed, eyes hidden, drooling, hands-free ejaculation", "incense",
               "{W} bites his neck softly and her sweet venom makes him come.")
L["onani_e2"] = ("he sits on warm sand among snake eggs pushing his wet fingers into his anus, a small vial beside him, she lies coiled nearby and waves the thin tip of her black tail in front of him, masturbation, ejaculation", "eggs",
                 "{W} dangles the tip of her tail while his fingers cannot reach.")
L["inochi_e2"] = ("from side, at the spring he holds a black cup, her black tail coils around his body as he turns away, the thin tip of her tail slides into his anus, anal, dazed, erection", "spring",
                  "{W}'s antidote cup was another dose of venom.")
L["onedari_e2"] = ("from side, he lies face down in a black silk hammock, a black scale ring on his finger, the thin tip of her black tail enters his anus, anal, she bites his neck gently, no blood, erection", "blackroom",
                   "He asks {W} for his daily dose in her hammock.")
# e3 リングァ
L["btl_e3"] = ("from side, in a warm sand bath her red tail coils around his body, she licks his anus with her very long tongue, anilingus, steam, oil shining on his skin, ejaculation", "bath",
               "{W} cleanses every part of him with her tongue in the sand bath.")
L["onani_e3"] = ("he lies on a narrow bed with white gloves on his hands touching his anus, she has entered from the door and licks deep into his anus with her very long tongue, anilingus, candlelight, ejaculation", "maidroom",
                 "{W} helps him with her tongue where his gloved fingers cannot reach.")
L["inochi_e3"] = ("from front, beside his packed bags her red tail coils tightly around his chest and arms, the coils squeeze and rub his nipples, a red braided cord tied to his bag, erection", "guestroom",
                  "{W} coils around him as he reaches for his bags.")
L["onedari_e3"] = ("from side, he bends over a serving table with hips raised, a small silver bell beside him, she licks his anus with her very long tongue, anilingus, polite smile, erection", "pantry",
                   "He places his morning order with {W}.")
# boss ウロボラ
L["btl_boss"] = ("in the center of her huge white coiled ring he lies on his side, a single white scale on his chest, the tip of her tail curls around his nipple, ejaculation", "throne",
                 "{W} takes him in the center of her ring throne.", "", "futa")
L["onani_boss"] = ("he sits on a round floor in the foreground stroking himself, her huge white coils encircle the floor, she looks down from far above with her long tongue out and the tip of her tail moving, a platinum braided bracelet on his wrist, ejaculation", "torchring",
                   "{W} watches from her throne as her coils close around him.")
L["inochi_boss"] = ("in a circular passage her white snake body coils around him as he turns back, a gold ring of a snake biting its own tail on his ankle, erection", "ringpath",
                    "{W} catches him when the circle leads him back to her.", "", "futa")
L["onedari_boss"] = ("from side, on a bed of white scales he lies on his stomach wearing a small gold crown, she licks his anus with her long forked tongue, anilingus, the tip of her tail curls around his nipple, erection", "queenbed",
                     "He swears to be {W}'s mate and offers himself.")

for rk, v in L.items():
    action, room, sentence = v[0], v[1], v[2]
    mode = v[4] if len(v) > 4 else ""
    route, who = rk.split("_")
    scene(f"Lamia_lose_{rk}", SEED[who], action, room, sentence, STATE[route], mode)

assert len(items) == 52, len(items)
json.dump({"code": "Lamia", "images": items}, open(os.path.join(HERE, "lamia_prompts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "N18_Lamia_ComfyUI_Prompts.md"), "w", encoding="utf-8") as f:
    f.write("# N18 Lamia ComfyUI プロンプト一覧（52枚）\n\n")
    for it in items:
        f.write(f"## {it['key']}\n- seed_char: {it['seed_char']}　背景除去: {'あり' if it['rembg'] else 'なし'}\n\n**positive**\n```\n{it['positive']}\n```\n**negative**\n```\n{it['negative']}\n```\n\n")
print("ok", len(items))
