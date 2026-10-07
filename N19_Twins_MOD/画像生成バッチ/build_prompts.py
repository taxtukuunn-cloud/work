# -*- coding: utf-8 -*-
"""N19 サキュバス双子の寝所（Twins）画像プロンプト生成 → twins_prompts.json（51枚）
登場人物は全員20歳以上の成人。個人利用のみ。N17 Scylla の build_prompts.py と同じ書き方。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_CORE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, "
            "child, loli, shota, young, teenage, underage, petite female, flat chest female, muscular, abs, pectorals, bara, hairy, "
            "collar, leash, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the man, 2boys, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies")
NEG_SOLO = ", twins, same face, same hair color"       # 1人の責め手の画像
NEG_TWIN = ", same hair color, same outfit, 3girls, identical hairstyle"   # 双子の画像（二人は髪色・服で描き分け）
NEG_NOFUTA = ", futanari, penis on the woman, woman with penis"
NEG_SCENE = (", pussy, vagina, breasts on the man, long hair on the man, blue hair on the woman, "
             "wings on the man, horns on the man, demon tail on the man, pointy ears on the man, glasses on the man, "
             "maid headdress on the man, clothes on the man, robe on the man, naked woman, nude woman")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, sex toy, strap-on"
NEG_ONANI = ", hand on crotch, pink hair on the man, orange hair on the man, crop top on the man, woman touching him, hetero sex, hands on him, woman masturbating, girl masturbating, penis on the woman, hand on penis, holding penis, handjob, stroking penis, penis grab"

ROOM = "dim violet candlelight, lavish succubus mansion, detailed background"

PROT = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult male, androgynous, "
        "feminine body, petite, short, slender, narrow shoulders, narrow waist, thin arms, flat chest, smooth pale skin, "
        "no muscles, blush, height difference, nude male, completely naked, penis")

RIRI = ("the older sister: pink hair, very long straight hair, purple eyes, black demon wings, black demon tail, "
        "black bondage-style dress, smirk, large breasts")
LALA = ("the younger sister: light purple hair, twintails, pink eyes, white demon wings, white demon tail, "
        "white frilly dress, calm half-closed eyes, medium breasts")

CH = {
    "tw": dict(seed="RIRILALA", neg=NEG_TWIN,
               tags="2girls, succubus sisters, adult women, mature faces, tall women, " + RIRI + ", " + LALA,
               name="the two succubus sisters, the pink-haired one in black and the light-purple-haired one in white"),
    "e1": dict(seed="MILK", neg=NEG_SOLO,
               tags="1girl, succubus, adult woman, brown hair, fluffy wavy hair, pink eyes, small demon wings, "
                    "black and white succubus maid outfit, frilled apron, gentle smile, large breasts",
               name="the brown-haired succubus maid in a black and white maid outfit"),
    "e2": dict(seed="NOCTO", neg=NEG_SOLO,
               tags="1girl, succubus, adult woman, mature face, black hair, bob cut, glasses, red eyes, "
                    "dark red scribe robe, long thin black demon tail, holding a quill pen, cold expression, medium breasts",
               name="the black-haired succubus scribe with glasses in a dark red robe"),
    "e3": dict(seed="PIXI", neg=NEG_SOLO,
               tags="1girl, imp, adult woman, mature face, orange hair, short hair, gold eyes, small bat wings, "
                    "thin black tail with a forked tip, black crop top, black shorts, smug grin, small breasts",
               name="the orange-haired imp woman in a black crop top with a forked tail"),
    "boss": dict(seed="NOX", neg=NEG_SOLO,
                 tags="1girl, succubus, mature female, very tall, silver hair, very long hair, gold eyes, "
                      "huge black demon wings, long black demon tail, black and deep purple night gown with star patterns, "
                      "motherly smile, huge breasts",
                 name="the very tall silver-haired succubus mother in a black and purple night gown with huge wings"),
}

PL = {
    "bed":     "succubus bedroom with mirror walls and mirror ceiling, big bed with a purple canopy, reflections, twin moons in the window",
    "wardrobe": "dressing room, many dresses on racks, tall standing mirrors on the left and right",
    "hall":    "grand entrance hall of a mansion, great staircase, heavy wooden double door",
    "balcony": "moonlit balcony at night, two moons side by side in the sky, stone railing",
    "bath":    "rose bath, marble bathtub filled with rose petals, steam",
    "door":    "in front of a large ornate bedroom door, purple carpet",
    "corridor": "long corridor lined with mirrors, candles",
    "mirroom": "room with mirrors on every wall, endless reflections",
    "garden":  "rose garden at night, garden path to the mansion gate, two moons",
    "maidroom": "cozy maid's room, small bed, cup of milk tea on a side table",
    "kitchen": "mansion kitchen, copper pots, jugs of milk, warm lamp light",
    "guest":   "guest room, fluffy bed, travel bag on the floor",
    "dining":  "morning dining room, silver tray and tea set on a long table, morning light",
    "records": "record room, shelves of parchment, ink pot, candlestick, stone table",
    "library": "library, reading desk, tall bookshelves, candle",
    "contract": "contract room, desk with sealing wax and stamps, candles",
    "lab":     "laboratory, padded examination table, glass instruments, candles",
    "attic":   "attic nest, pile of cushions, skylight with moonlight",
    "stairs":  "staircase landing inside the mansion, carpet, candle sconces",
    "roof":    "on the mansion roof at night, two moons, roof tiles",
    "nest":    "deep inside an attic nest of cushions, moonlight from a skylight",
    "silver":  "top floor bedchamber, huge bed with a night-blue canopy, silver moon light",
    "bigmirror": "bedchamber with a huge standing mirror",
    "gate":    "huge mansion front door before dawn, dark sky",
}

CLOTHED = "the women keep their dresses on, only the man is naked"
CLOTHED_1 = "the woman keeps her clothes on, only the man is naked"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Twins_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, futa=False, insert=False, onani=False):
    c = CH[who]
    clothed = CLOTHED if who == "tw" else CLOTHED_1
    if onani:
        pos = ", ".join([Q, "explicit", PROT, "erection, solo focus, he is in the foreground", action,
                         (("two women in long black and white dresses with demon wings" if who == "tw" else c["name"]) + " stand far in the background fully clothed, watching, small in frame, not touching him"),
                         ROOM, PL[place], desc])
    else:
        futa_tag = ""
        if futa:
            futa_tag = (", the pink-haired sister has a futanari penis" if who == "tw" else ", futanari, large penis on the woman")
        trio = "3people, 2girls and 1boy, the naked navy-haired man is between the two sisters, " if who == "tw" else "1girl and 1boy, "
        pos = ", ".join([Q, "explicit", trio + c["tags"] + futa_tag, PROT, "erection", action, clothed, ROOM, PL[place], desc])
    neg = NEG_CORE + c["neg"] + ("" if futa else NEG_NOFUTA) + NEG_SCENE + (NEG_INSERT if (insert or futa) else "") + (NEG_ONANI if onani else "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵（背景除去）
STAND = {
    "master": ("tw", "standing side by side, the pink-haired sister leaning forward with a finger on her lips, "
                     "the light-purple-haired sister hugging her sister's arm, tails intertwined"),
    "e1": ("e1", "standing, holding a silver tray with a tea cup, head tilted, gentle smile"),
    "e2": ("e2", "standing, holding an open ledger and a quill pen, pushing up her glasses"),
    "e3": ("e3", "hovering, hands on hips, leaning forward, looking down at viewer, teasing grin, forked tail curled"),
    "boss": ("boss", "standing tall, wings spread wide, arms open welcoming, looking down at viewer"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe", c["tags"], pose, "looking at viewer, full body, simple background, white background"]),
        NEG_CORE + c["neg"] + NEG_NOFUTA, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery",
                           "succubus bedroom at night, big bed with a purple canopy, walls and ceiling covered with mirrors, "
                           "violet candlelight, rose petals, two moons side by side outside the window, detailed background"]),
    NEG_CORE + NEG_SOLO + NEG_NOFUTA)

# ---- 技CG
scene("atk_m1", "tw", "bed",
      "he lies on his back on the bed between the two sisters, the pink-haired sister licks his right nipple, "
      "the light-purple-haired sister pinches his left nipple with her fingers, erect nipples, trembling",
      "the twin succubi attack his right and left nipples at the same time.")
scene("atk_m2", "tw", "bed",
      "from side, he is on all fours on the bed, the pink-haired sister kisses him deeply from the front, "
      "the light-purple-haired sister kneels behind him licking his anus, anilingus",
      "the twin succubi kiss him from the front and lick him from behind at the same time.")
scene("atk_m3", "tw", "bed",
      "from side, he is on all fours on the bed, the pink-haired sister kneels behind him and penetrates his anus with her futanari penis, anal, "
      "the light-purple-haired sister lies under his chest sucking his nipple, his own penis is separate and hangs down",
      "the older sister penetrates him from behind while the younger sister sucks his nipple.", futa=True)
scene("atk_e1", "e1", "maidroom",
      "she sits beside him on the small bed, licking his nipple, whispering into his ear, he melts, open mouth",
      "the succubus maid spoils him and licks his nipples.")
scene("atk_e2", "e2", "records",
      "he lies on the stone table, she draws a glowing red crest on his lower belly with her quill pen, "
      "her thin tail pushed into his anus, anal, trembling",
      "the succubus scribe draws a crest on him while her tail opens him.", insert=True)
scene("atk_e3", "e3", "attic",
      "from side, he lies on the cushions, the two tips of her forked tail: one very thin tip inserted into the tip of his penis, urethral insertion, "
      "the other tip pushed into his anus, anal, she looks down laughing",
      "the imp uses the two tips of her tail at once.", insert=True)
scene("atk_boss", "boss", "silver",
      "from side, she wraps him in her huge wings, her long tail pushed into his anus, anal, she sucks his nipple with her lips, "
      "he is limp in her arms",
      "the succubus mother wraps him in her wings, tail in his anus and lips on his nipple.", insert=True)

# ---- 敗北28（主人公と、そのシナリオの責め手だけを描く）
L = [
 ("btl_m1", "tw", "bed", "he lies on his back on the canopy bed between the sisters, the pink-haired one licks his right nipple, the light-purple-haired one pinches his left nipple, a small purple jewel on his right nipple and a pink jewel on his left nipple, cum on his belly, exhausted", {}),
 ("onani_m1", "tw", "wardrobe", "kneeling upright, both hands on his own chest, left fingernails pinching his left nipple, right wet fingertip rubbing his right nipple, hands far away from his crotch, penis untouched, standing between two tall mirrors, a small earring on each of his ears, the two sisters stand behind him whispering, not touching him", {"onani": True}),
 ("inochi_m1", "tw", "hall", "he stands at the heavy door with one hand on the handle, the light-purple-haired sister kisses his left nipple from the side, the pink-haired sister smiles behind him, thin glowing ring marks around his nipples", {}),
 ("onedari_m1", "tw", "balcony", "he sits on the stone railing bench, begging, the pink-haired sister licks his right nipple and the light-purple-haired sister teases his left nipple with her finger, a pink ribbon and a purple ribbon in her hands", {}),
 ("btl_m2", "tw", "bed", "from side, he is on all fours on the bed, the pink-haired sister kisses him deeply from the front, the light-purple-haired sister licks his anus from behind, anilingus, pink lipstick marks on his lips, cum dripping", {}),
 ("onani_m2", "tw", "bath", "kneeling upright, both hands on his own chest, left fingernails pinching his left nipple, right wet fingertip rubbing his right nipple, hands far away from his crotch, penis untouched, sitting alone on the edge of the rose bath, small perfume bottle on the edge, the two clothed sisters stand on the far side of the bath only watching", {"onani": True}),
 ("inochi_m2", "tw", "door", "in front of the bedroom door, the pink-haired sister kisses him deeply while the light-purple-haired sister kneels behind him licking his anus, anilingus, a tiny glowing crest on his tongue", {}),
 ("onedari_m2", "tw", "corridor", "from side, he is on his knees in the mirror corridor, begging, the pink-haired sister holds his chin for a kiss, the light-purple-haired sister behind him, anilingus, reflections in the mirrors", {}),
  ("btl_m3", "tw", "bed", "from side, on the mirrored canopy bed he is on all fours, the pink-haired sister kneels behind him penetrating his anus with her futanari penis, anal, the light-purple-haired sister lies under his chest sucking his nipple, a glowing crest of two facing crescent moons on his lower belly, his own penis separate, cum dripping", {"futa": True}),
 ("onani_m3", "tw", "mirroom", "kneeling upright, both hands on his own chest, left fingernails pinching his left nipple, right wet fingertip rubbing his right nipple, hands far away from his crotch, penis untouched, a faint pink crest glowing on his lower belly, the two sisters watch from a distance and whisper, endless mirror reflections", {"onani": True}),
  ("inochi_m3", "tw", "garden", "from side, on the rose garden path, the light-purple-haired sister sits on a garden bench sucking his nipple, the pink-haired sister stands behind him penetrating his anus with her futanari penis, anal, a small gate-shaped glowing crest on his lower belly, his own penis separate", {"futa": True}),
  ("onedari_m3", "tw", "bed", "from side, he lies on his back on the bed with his legs lifted, begging, the pink-haired sister kneels between his legs penetrating his anus with her futanari penis, anal, the light-purple-haired sister lies beside him sucking his nipple, his own penis separate", {"futa": True}),
 ("btl_e1", "e1", "maidroom", "he lies in her lap on the small bed, she licks his nipple, a small bell ribbon tied around his neck, cum on his belly, relaxed and melting", {}),
 ("onani_e1", "e1", "kitchen", "kneeling upright, licking his own fingertip, the wet fingertip rubbing his own nipple upward, other hand resting on his thigh, hands far away from his crotch, penis untouched, hiding in the corner of the kitchen, she peeks at him from the doorway showing her tongue", {"onani": True}),
 ("inochi_e1", "e1", "guest", "she hugs him from behind on the fluffy bed, whispering into his ear, his travel bag abandoned on the floor, a room key on a ribbon in her hand, he is dazed", {}),
 ("onedari_e1", "e1", "dining", "he sits in a chair at the breakfast table, begging, she leans over licking his nipple, a small silver hand bell on the silver tray", {}),
 ("btl_e2", "e2", "records", "he lies on the stone table, an unfinished glowing red crest drawn on his lower belly, her thin tail in his anus, anal, she writes in her ledger, cum on his belly", {"insert": True}),
 ("onani_e2", "e2", "library", "kneeling upright, one fingertip tracing a glowing red crest on his own lower belly above the navel, other hand pressed on the floor behind him, penis untouched, at the reading desk, she stands nearby writing notes in a ledger, cold stare", {"onani": True}),
 ("inochi_e2", "e2", "contract", "from side, the naked navy-haired man bends over the desk signing a parchment, the black-haired woman in the dark red robe and glasses stands behind him, her thin tail pushed into his anus, anal, a red wax seal mark on his hip", {"insert": True}),
 ("onedari_e2", "e2", "lab", "he lies on the examination table, begging, she holds her quill pen over his lower belly and her thin tail in his anus, anal, trembling", {"insert": True}),
 ("btl_e3", "e3", "attic", "from side, he lies on the cushions, her forked tail tips inserted in his penis tip and his anus, urethral insertion, anal, an orange ribbon tied around his neck, she laughs, cum", {"insert": True}),
 ("onani_e3", "e3", "stairs", "from side, kneeling, one hand pressing his own perineum from below, the other hand reaching behind fingering his own anus, penis untouched, on the staircase landing, an orange feather stuck in his hair, she crouches a few steps away counting on her fingers, teasing grin", {"onani": True}),
 ("inochi_e3", "e3", "roof", "on the moonlit roof she kisses him deeply, holding his face, he is weak in the knees, sweet drool, two moons", {}),
 ("onedari_e3", "e3", "nest", "from side, he lies on his back on the cushions, begging, her forked tail tips in his penis tip and anus, urethral insertion, anal, a small gold ring on her tail fork, moonlight", {"insert": True}),
 ("btl_boss", "boss", "silver", "from side, wrapped in her huge wings on the big bed, she penetrates his anus with her futanari penis, anal, a thin silver braided necklace on him, his own penis separate, cum", {"futa": True}),
 ("onani_boss", "boss", "bigmirror", "kneeling upright, one hand rubbing his own nipple, the other arm reaching behind his back fingering his own anus, hands far away from his crotch, penis untouched, in front of the huge mirror, a black feather on the floor, her tail slowly swaying far behind him", {"onani": True}),
 ("inochi_boss", "boss", "gate", "from side, at the huge door before dawn she wraps him in her wings from behind, her tail in his anus, anal, she sucks his nipple, a dark stone ring on his finger", {"insert": True}),
 ("onedari_boss", "boss", "silver", "from side, he kneels on the bed begging with a silver key hanging on a ribbon around his wrist, she penetrates his anus with her futanari penis, anal, his own penis separate", {"futa": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " drains his energy and makes him hers.", **opt)

ONACT = {'tw': 'kneeling upright, both hands on his own chest, left fingernails pinching his left nipple, right wet fingertip rubbing his right nipple, hands far away from his crotch, penis untouched', 'e1': 'kneeling upright, licking his own fingertip, the wet fingertip rubbing his own nipple upward, other hand resting on his thigh, hands far away from his crotch, penis untouched', 'e2': 'kneeling upright, one fingertip tracing a glowing red crest on his own lower belly above the navel, other hand pressed on the floor behind him, penis untouched', 'e3': 'from side, kneeling, one hand pressing his own perineum from below, the other hand reaching behind fingering his own anus, penis untouched', 'boss': 'kneeling upright, one hand rubbing his own nipple, the other arm reaching behind his back fingering his own anus, hands far away from his crotch, penis untouched'}
# ---- オナニーCG
ON = {"master": ("mirroom", "tw"), "e1": ("kitchen", "e1"), "e2": ("library", "e2"), "e3": ("attic", "e3"), "boss": ("bigmirror", "boss")}
for k, (place, who) in ON.items():
    scene("onanie_" + k, who, place, ONACT[who] + ", flushed, sweat, trembling",
          "he pleasures himself alone while they watch from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "tw", "both sisters blowing sweet pink breath toward viewer from the left and right, glowing pink mist, pov", "bed"),
    ("magic_2", "tw", "the pink-haired sister in front beckoning with a finger, the light-purple-haired sister peeking over her shoulder, seductive smiles, pov", "balcony"),
    ("magic_3", "tw", "the light-purple-haired sister ringing a small silver bell, the pink-haired sister waving, glowing magic circle", "hall"),
    ("magic_4", "tw", "the sisters reflected many times in the mirrors, smiling back at viewer from inside the mirrors", "mirroom"),
    ("magic_5", "tw", "the sisters lying on the canopy bed side by side, beckoning to viewer, pov", "bed"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "sensitive", c["tags"], act, "looking at viewer", ROOM, PL[place]]), NEG_CORE + c["neg"] + NEG_NOFUTA)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Twins", "images": images}, open(os.path.join(here, "twins_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
