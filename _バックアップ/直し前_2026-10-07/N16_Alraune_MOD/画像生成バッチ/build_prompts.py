# -*- coding: utf-8 -*-
"""N16 Alraune: alraune_prompts.json と読む用プロンプト一覧を作る。"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, "
       "child, loli, shota, young, teenage, underage, flat chest female, muscular, abs, pectorals, bara, hairy, "
       "collar, choker, leash, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
       "eyes visible on the man, 2boys, futanari, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies")
NEG_MALE = ", pussy, vagina, breasts on the man, long hair on the man, black hair on the man, green hair on the man"
NEG_TOOL = ", dildo, sex toy, strap-on, penis on the woman, merged, fused, overlapping penises"
NEG_STAND = ", nipples, nude, naked, topless, 1boy"

C = {  # tags, English name
 "FLORA": ("1girl, alraune, plant girl, mature female, adult woman, tall, green hair, very long hair, flower crown, gold eyes, "
           "dress made of leaves and petals, upper body rising from a giant pink flower, gentle smile, large breasts",
           "the green-haired alraune queen rising from a giant pink flower"),
 "IVY":   ("1girl, plant girl, adult woman, brown hair, braided hair, green eyes, ivy vines wrapped around her arms and legs, "
           "brown gardener apron over a green dress, expressionless, medium breasts",
           "the brown-haired gardener girl in an apron with ivy on her arms"),
 "POLLEN":("1girl, plant girl, adult woman, yellow hair, fluffy bob cut, orange eyes, glowing golden pollen particles, "
           "sheer yellow petal dress, mischievous smile, medium breasts",
           "the yellow-haired pollen spirit in a sheer petal dress"),
 "NEPEN": ("1girl, plant girl, adult woman, red-purple hair, long hair, yellow-green eyes, "
           "large bulbous pitcher plant skirt, red-purple leaf top, seductive smile, long tongue, large breasts",
           "the red-purple-haired pitcher plant girl with a huge pitcher skirt"),
 "YUG":   ("1girl, dryad, mature female, adult woman, very tall, white hair, very long hair, young leaves in hair, jade eyes, "
           "dress of bark and moss, branches growing from her back, huge roots at her feet, serene, large breasts",
           "the very tall white-haired world tree dryad in a bark dress"),
}
HERO = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult male, petite, short, "
        "slender, skinny, soft body, narrow shoulders, thin arms, smooth pale skin, no muscles, blush, height difference, "
        "he is much shorter than her, nude male, completely naked man, penis")
CLOTHED = "cfnm, clothed female, the woman keeps all her clothes on, only the man is naked"

ROOM = {
 "flower":  "inside a ruined glass greenhouse, broken glass ceiling, sunbeams, overgrown ivy, giant flowers, petals in the air, detailed background",
 "canopy":  "inside a greenhouse, under a canopy of hanging ivy vines, soft green moss bed, dim green light, detailed background",
 "arch":    "inside a greenhouse, arched glass doorway completely covered in ivy vines, bright light from outside, detailed background",
 "dewshelf":"inside a misty greenhouse, wooden seedling shelves full of potted cuttings, morning dew drops, detailed background",
 "spring":  "inside a greenhouse, small pool of glowing amber honey, surrounded by flowers, warm golden light, detailed background",
 "honeystore":"honey storeroom, wooden shelves lined with glass honey jars, amber light, detailed background",
 "moon":    "ruined glass greenhouse at night, moonlight through broken glass ceiling, pale blue shadows, glowing flowers, detailed background",
 "table":   "inside a greenhouse, giant flower-shaped table set for breakfast, glass jars of honey, morning light, detailed background",
 "bed":     "central flower bed of a greenhouse, cloud of golden pollen in the air, sunbeams, detailed background",
 "eastwing":"east wing of a glass greenhouse, golden pollen drifting in sunbeams, tall flowers, detailed background",
 "rain":    "rainy greenhouse, rain streaming down the glass roof, stone bath filled with rainwater, light steam, detailed background",
 "potting": "greenhouse potting room, wooden workbench, pruning shears, clay pots, gardening tools on the wall, detailed background",
 "shed":    "small wooden tool shed, gardening tools, stacked clay pots, closed notebook on a shelf, dim light, detailed background",
 "hedge":   "inside a greenhouse, tall trimmed hedges, cut ivy branches on the ground, detailed background",
 "bigpot":  "inside a greenhouse, huge terracotta flower pot filled with soil, detailed background",
 "sunflower":"sunflower field inside a greenhouse, giant soft flower bed, sunbeams, golden pollen, detailed background",
 "vials":   "inside a greenhouse, wooden shelf of small glass vials filled with glowing colorful pollen, detailed background",
 "bog":     "carnivorous plant bog inside a greenhouse, giant pitcher plants, amber water, humid air, detailed background",
 "stones":  "stepping stones across a carnivorous plant bog, giant pitcher plant mouth ahead, detailed background",
 "root":    "base of a giant world tree inside a greenhouse, huge roots forming a cradle, glowing moss, detailed background",
 "corridor":"underground corridor of glowing roots, roots on walls and ceiling emitting soft light, detailed background",
 "hollow":  "inside a huge tree hollow, walls of wood, dripping amber sap, dim light, detailed background",
 "branch":  "high in the branches of a giant tree, cradle made of branches and leaves, sky through the glass ceiling, detailed background",
}
STATE = {
 "btl": "defeated, exhausted, limp body, tears of pleasure, cum",
 "onani": "deeply embarrassed, flustered, sweat, being watched",
 "inochi": "dazed, trembling, giving in",
 "onedari": "begging, eager, submissive posture, open mouth",
}
SEED = {"m1": "FLORA", "m2": "FLORA", "m3": "FLORA", "e1": "IVY", "e2": "POLLEN", "e3": "NEPEN", "boss": "YUG"}

items = []
def add(key, seed, pos, neg=NEG, rembg=False):
    items.append({"key": key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})

def scene(key, who, action, room, sentence, state="", tool=False):
    tags, name = C[who]
    parts = [Q, "explicit", tags, HERO, action]
    if state:
        parts.append(state)
    parts += [CLOTHED, ROOM[room], sentence.replace("{W}", name)]
    add(key, who, ", ".join(parts), NEG + NEG_MALE + (NEG_TOOL if tool else ""))

# ---- 立ち絵（背景除去） ----
STAND = {
 "Alraune_master": ("FLORA", "full body, the whole giant flower visible, arms open, welcoming, looking at viewer, smile"),
 "Alraune_e1": ("IVY", "standing, holding pruning shears, ivy vines trailing from her fingers, looking at viewer"),
 "Alraune_e2": ("POLLEN", "standing, blowing golden pollen from her palm, one eye closed, looking at viewer"),
 "Alraune_e3": ("NEPEN", "standing, the huge pitcher skirt fully visible, licking her lips, looking at viewer"),
 "Alraune_boss": ("YUG", "standing, roots spreading on the ground, from below, looking down at viewer, calm"),
}
for k, (w, pose) in STAND.items():
    add(k, w, ", ".join([Q, "safe", "solo", C[w][0], pose, "full body, simple background, white background"]), NEG + NEG_STAND, rembg=True)

add("Alraune_bg", "BG", ", ".join([Q, "safe", "no humans, scenery", "inside a huge ruined glass greenhouse deep in a forest, broken glass ceiling, sunbeams, "
    "overgrown ivy and vines, giant flowers taller than a person, a huge pink flower in the center, petals and golden pollen in the air, detailed background"]),
    NEG + ", 1girl, 1boy, people")

# ---- 技CG ----
scene("Alraune_atk_m1", "FLORA", "from front, he is lifted up on the giant flower in front of her, thin green vines from her body coil around his chest and wrap his nipples, vines sucking his nipples, nipple play, she holds his shoulders, erection", "flower",
      "{W} coils thin vines around his nipples while holding him on her flower.", "")
scene("Alraune_atk_m2", "FLORA", "from side, he kneels on all fours on a petal in front of her, a thick green vine drips glowing amber honey jelly into his anus, anal, honey dripping on his thighs, she strokes his back, erection", "flower",
      "{W} feeds sweet amber honey jelly into him through a vine.", "", True)
scene("Alraune_atk_m3", "FLORA", "from side, he is held in the air by vines, a green vine penetrates his anus, anal, a cloud of golden pollen around his face, he inhales the pollen, dazed, drooling, she blows pollen toward him, erection", "bed",
      "{W} pushes a vine into him from behind while making him breathe her golden pollen.", "", True)
scene("Alraune_atk_e1", "IVY", "from front, she hugs him from behind, ivy vines from her arms bind his whole body tightly, vines squeeze his chest and pinch his nipples, erection", "potting",
      "{W} binds him tightly with ivy vines from behind and squeezes his chest.")
scene("Alraune_atk_e2", "POLLEN", "from side, she leans down and kisses him deeply, golden pollen sparkles between their lips, honey dripping from their lips, he sits on a flower, erection", "sunflower",
      "{W} bends down and kisses him while golden pollen sparkles around them.")
scene("Alraune_atk_e3", "NEPEN", "from front, he is half swallowed into her huge pitcher skirt up to his waist, she bends down and licks his nipple with her long tongue, saliva, nipple licking, erection", "bog",
      "{W} holds him inside her pitcher skirt and licks his nipple.")
scene("Alraune_atk_boss", "YUG", "from side, he is suspended in a cradle of huge roots, thin roots coil around his nipples, a green vine penetrates his anus, anal, arms and legs held by roots, she looks down at him, erection", "root",
      "{W} holds him in her roots, coiling his nipples and entering him with a vine at the same time.", "", True)

# ---- 魔法・罠 ----
add("Alraune_magic_1", "FLORA", ", ".join([Q, "safe", C["FLORA"][0], "holding out a wooden spoon dripping with glowing amber honey toward viewer, pov, smile", ROOM["flower"]]), NEG + NEG_STAND)
add("Alraune_magic_2", "BG2", ", ".join([Q, "safe", "no humans, scenery", "green ivy vines creeping across a stone greenhouse floor, vines forming a trap loop, dim light, fallen petals", "detailed background"]), NEG + ", 1girl, 1boy, people")
add("Alraune_magic_3", "POLLEN", ", ".join([Q, "safe", C["POLLEN"][0], "blowing a thick cloud of golden glittering pollen mist from her palms, playful", ROOM["eastwing"]]), NEG + NEG_STAND)
add("Alraune_magic_4", "FLORA", ", ".join([Q, "safe", C["FLORA"][0], "dropping a single glowing seed from her fingertips into dark soil, a small sprout glowing below, gentle smile", ROOM["dewshelf"]]), NEG + NEG_STAND)
add("Alraune_magic_5", "BG", ", ".join([Q, "safe", "no humans, scenery", "interior of a warm glass greenhouse, fogged glass walls, humid air, giant flowers, hanging vines, soft warm light, detailed background"]), NEG + ", 1girl, 1boy, people")

# ---- 特殊（命乞い・おねだり） ----
scene("Alraune_inochigoi", "FLORA", "from front, he stands hesitating with his hand lowered, she looks at him with sad pleading eyes, vines around his ankles slowly loosening, erection", "arch",
      "{W} pleads with him while loosening the vines, and he hesitates.", STATE["inochi"])
scene("Alraune_onedari", "FLORA", "from front, he kneels on a large petal and looks up at her, hands together in front of his chest, she looks down at him with a gentle smile, vines reaching toward him, erection", "flower",
      "He begs {W} for her vines.", STATE["onedari"])

# ---- オナニー（主人公が主役・責め手は奥で見ているだけ） ----
ONA = {  # 得意技に合わせた自慰（v4）。ペニスに触れない
 "Alraune_onanie_m": ("FLORA", "canopy", "he sits on the moss in the foreground, both hands on his own flat chest, pinching and twisting his own nipples with his fingertips as if they were vines, thin green vines loosely wrapped around his wrists"),
 "Alraune_onanie_e1": ("IVY", "shed", "he sits on the floor in the foreground with his legs spread, two fingers of one hand pressing deep into his perineum below his balls, his other hand gripping the floor"),
 "Alraune_onanie_e2": ("POLLEN", "eastwing", "he kneels in golden pollen in the foreground, hands-free, both hands behind his back on the floor, arching his hips, drooling, breathing in the pollen, precum dripping"),
 "Alraune_onanie_e3": ("NEPEN", "bog", "he is on all fours in the foreground seen from the side, one honey-wet hand reaching behind him, fingertips circling his own anus, his other hand on the ground"),
 "Alraune_onanie_boss": ("YUG", "corridor", "he lies on his back in the foreground with his knees up, one hand pinching his own nipple, the fingers of his other hand inserted into his own anus from below"),
}
NEG_ONA = ", hand on penis, holding penis, stroking penis, handjob, hand on crotch, penis on the woman, woman holding penis, woman touching penis, girl in foreground, girl close-up, woman touching her own breasts, woman groping herself"
for k, (w, room, act) in ONA.items():
    tags, name = C[w]
    pos = ", ".join([Q, "explicit", "the naked navy-haired man is the main subject in the foreground, close-up on him", HERO, act, "penis untouched, hands far away from his penis, erection, embarrassed, blush",
                     tags, "she is a tiny distant figure far in the background, arms crossed, only watching him, her hands are not on her own body, she has no penis, not touching", CLOTHED, ROOM[room],
                     f"{name} watches him from a distance while he pleasures himself without touching his penis."])
    add(k, w, pos, NEG + NEG_MALE + NEG_ONA)

# ---- 敗北CG 28枚 ----
L = {}
L["btl_m1"] = ("from front, he lies wrapped inside huge pink petals on top of her giant flower, three small flower buds blooming on his chest, thin vines coiled around his nipples, she embraces him from above, ejaculation", "flower",
               "{W} wraps him in her petals and makes buds bloom on his chest.")
L["onani_m1"] = ("from above, he lies on his back on a soft moss bed in the foreground, both of his hands on his own flat chest pinching his own nipples, green vines wrapped around his wrists, penis untouched, far behind him she sits on her flower with her hands folded on her own lap, watching and smiling, precum", "canopy",
                 "{W} guides his fingers on his nipples with her vines on the moss bed.")
L["inochi_m1"] = ("from behind, he stands at an ivy-covered archway reaching toward the bright outside, vines from behind wrap his chest and nipples and pull him back, she smiles behind him", "arch",
                  "The vines {W} loosened come back and pull him away from the exit.")
L["onedari_m1"] = ("from front, he kneels among seedling shelves and pushes out his own flat chest, tiny green sprouts growing on his own nipples, she bends down and plants a tiny cutting on his chest with her fingertips, her leaf dress fully covers her breasts, erection", "dewshelf",
                   "{W} plants small cuttings on his chest where he asked.")
L["btl_m2"] = ("from side, he lies on his stomach at the edge of a glowing honey pool, a vine pours amber honey jelly into his anus, anal, honey all over his thighs, she caresses his hair, her leaf dress fully covers her breasts, ejaculation", "spring",
               "{W} fills him with honey jelly beside the honey spring.", True)
L["onani_m2"] = ("from front, he sits among shelves of honey jars, honey-coated fingers pinching his own nipples, honey dripping down his chest, penis untouched, a small glass jar placed under him, she watches smiling, ejaculation", "honeystore",
                 "{W} watches him pinch his honey-covered nipples and collects what spills in a jar.")
L["inochi_m2"] = ("from side, he lies on his side under moonlight, she holds a vine that feeds amber honey into his anus, anal, she smiles kindly, honey dripping", "moon",
                  "{W} gives him her so-called antidote honey under the moonlight.", True)
L["onedari_m2"] = ("from side, he lies on his stomach on a giant flower-shaped table, hips raised toward her, she holds a golden spoon and a vine dripping honey into his anus, anal, erection", "table",
                   "{W} serves him spoonfuls of honey jelly on the breakfast table.", True)
L["btl_m3"] = ("from side, he lies on his back suspended horizontally in the air by vines in front of her, legs spread and held up by vines, a vine penetrates his anus, anal, surrounded by a golden pollen cloud, drooling, she stands on her flower and holds his chin, ejaculation", "bed",
               "{W} roots him with vines inside a cloud of golden pollen.", True)
L["onani_m3"] = ("from front, he sits in golden pollen pinching his own nipples with both hands, dazed, drooling, a green vine touches his anus from behind, penis untouched, she blows pollen at him from above", "eastwing",
                 "{W} blows more pollen at him while he cannot stop playing with his nipples.")
L["inochi_m3"] = ("from side, he sits in a stone bath of rainwater, wet, vines under the water enter his anus, anal, she washes pollen from his hair with her hands, rain on the glass roof", "rain",
                  "{W} pretends to wash the pollen away while her vines go deeper.", True)
L["onedari_m3"] = ("from front, he sits on the edge of her giant flower taking a deep breath of golden pollen, a vine penetrates his anus, anal, she counts on her fingers smiling, erection", "flower",
                   "{W} counts his breaths as he inhales her pollen and takes her vines.", True)
L["btl_e1"] = ("from side, he lies bound on a wooden workbench by ivy vines, a very thin vine enters the tip of his penis, urethral insertion, sounding, she holds pruning shears calmly, ejaculation", "potting",
               "{W} repots him on the workbench and threads a thin vine into him.")
L["onani_e1"] = ("from front, he sits against the wall of a tool shed with legs spread, two fingers pressing deep into his own perineum, his other wrist tied to a shelf by ivy, penis untouched, she stands writing in a notebook with a blank page, ejaculation", "shed",
                 "{W} records every press of his fingers in her gardening log.")
L["inochi_e1"] = ("from front, he stands between hedges, she cuts a vine with pruning shears, and many new vines sprout and wrap his waist and chest, squeezing him, erection", "hedge",
                  "{W} cuts one vine and twice as many sprout around him.")
L["onedari_e1"] = ("from front, he sits inside a huge terracotta pot filled with soil up to his waist, legs spread, a thin vine enters the tip of his penis, urethral insertion, she kneels beside the pot adjusting the vine", "bigpot",
                   "{W} repots him in a huge pot and threads a thin vine into him.")
L["btl_e2"] = ("from side, he lies on a giant soft flower bed in a sunflower field, covered in golden pollen, eyes hidden, drooling, trembling, she lies beside him blowing pollen on his face, hands-free ejaculation", "sunflower",
               "{W} makes him come without touching, only with her pollen.")
L["onani_e2"] = ("from front, he kneels in drifting golden pollen, hands-free, both hands behind his back, hips shaking, drooling, penis untouched, she floats beside him counting with her fingers raised, hands-free ejaculation", "eastwing",
                 "{W} counts aloud while he comes without touching himself.")
L["inochi_e2"] = ("from above, he lies on his back on a garden path, she kneels beside his head, not on top of him, and bends down to kiss him upside down, spider-man kiss, golden pollen and honey between their mouths, his cheeks puffed, holding his breath, his own penis is erect, she has no penis, erection", "flower",
                  "{W} seals his lips with a kiss so he can only breathe her pollen.")
L["onedari_e2"] = ("from front, he kneels in front of a shelf of glowing pollen vials, she holds a vial to his nose and leans in to kiss him, pollen sparkling, erection", "vials",
                   "{W} lets him smell the pollen he chose and kisses him.")
L["btl_e3"] = ("from above, he is swallowed inside her huge pitcher skirt up to his chest, amber honey and soft petals inside, she leans over and licks his nipples with her long tongue, only his upper body visible, ejaculation", "bog",
               "{W} keeps him inside her pitcher skirt and licks him.")
L["onani_e3"] = ("from side, he is on all fours at the edge of the bog, honey-wet fingertips of one hand circling his own anus from behind, penis untouched, she peeks from the rim of her pitcher with her long tongue out, ejaculation", "bog",
                 "{W} peeks at him as he imitates her tongue with his own fingers.")
L["inochi_e3"] = ("from behind, he is on all fours on a stepping stone at the mouth of her giant pitcher, she licks his anus with her long tongue, anilingus, erection", "stones",
                  "{W} turns the exit into the mouth of her pitcher and licks him from behind.")
L["onedari_e3"] = ("from side, he climbs into her pitcher skirt himself, she holds his hips and licks his anus with her long tongue, anilingus, he clings to the rim, erection", "bog",
                   "He climbs into {W}'s pitcher and asks to be licked.")
L["btl_boss"] = ("from side, he lies in a cradle of huge roots, thin roots coil on his nipples, a green vine penetrates his anus, anal, glowing ring patterns on his skin like tree rings, she looks down from above, ejaculation", "root",
                 "{W} carves tree rings into him with her roots and vines.", True)
L["onani_boss"] = ("from front, he lies on his back in an underground corridor of glowing roots, one hand pinching his own nipple, fingers of his other hand inserted into his own anus from below, glowing roots wrap his ankles, penis untouched, she looks down from far above, ejaculation", "corridor",
                   "{W} watches from far above as he opens himself for her roots.")
L["inochi_boss"] = ("from side, he lies on his back inside a tree hollow, thin tube-like roots dripping amber sap enter his penis tip and his anus, urethral insertion, anal, sap dripping, she kneels over him, erection", "hollow",
                    "{W} fills him with sap through thin roots inside the tree hollow.", True)
L["onedari_boss"] = ("from side, he lies in a cradle of branches high in the tree, a thin root enters his penis tip and a vine enters his anus, urethral insertion, anal, amber sap, she holds him in her arms from behind", "branch",
                     "{W} fills him with sap in the branch cradle where he asked.", True)

for rk, v in L.items():
    action, room, sentence = v[0], v[1], v[2]
    tool = len(v) > 3 and v[3]
    route, who = rk.split("_")
    scene(f"Alraune_lose_{rk}", SEED[who], action, room, sentence, STATE[route], tool)
    if route == "onani":
        items[-1]["negative"] += NEG_ONA

assert len(items) == 53, len(items)
json.dump({"code": "Alraune", "images": items}, open(os.path.join(HERE, "alraune_prompts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "N16_Alraune_ComfyUI_Prompts.md"), "w", encoding="utf-8") as f:
    f.write("# N16 Alraune ComfyUI プロンプト一覧（53枚）\n\n")
    for it in items:
        f.write(f"## {it['key']}\n- seed_char: {it['seed_char']}　背景除去: {'あり' if it['rembg'] else 'なし'}\n\n**positive**\n```\n{it['positive']}\n```\n**negative**\n```\n{it['negative']}\n```\n\n")
print("ok", len(items))
