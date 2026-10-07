# N130 深海と造魔（Shrift2）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# カリブディス：原作は青緑の髪 → deep forest green hair に置き換え（瞳は violet）。腰から下はイソギンチャクの触手（怖くしない）。
# 影女：brief は黒髪だが絡新婦（黒髪）と被るので、影に溶ける charcoal grey の髪にした。分身は「3人以上を出さない」ため本体1人で描く。
# LOVERS：立ち絵だけ3人を1枚に（pose で2人を添える）。技CG・敗北CGは髪を下ろした1人＋主人公だけ。
# 絡新婦：人の姿だけ（蜘蛛の体・下腹部は描かない）。糸は柔らかい白い絹糸で締めつけない。
# 挿入はカリブディスの触手の先だけ（pen なし）。ほかは指（影女は影の指）まで。クラウンは後ろに触れない。
# 絵には必ずアミュレットか泡を一つ入れる。貝殻・予定表の文字は描かない。
AMU = "a cheap brass amulet with black streaks hanging on his neck"
BUB = "rising bubbles"
TENT_NEG = "scary, grotesque, slimy monster, teeth, suction marks on skin, bruise, tentacle in mouth"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
SPIDER_NEG = "spider legs, spider lower body, arachne, extra arms, extra breasts, insect, scary"
TIP = "a smooth round tentacle tip in his anus, anal"
SUCK = "thin tentacles sucking both his nipples"
DATA = {
 "code": "Shrift2",
 "world": "a demon-haunted modern city and a deep-sea temple beneath it, cold blue light through water, rising bubbles, coral pillars, glass flasks, long shadows, detailed background",
 "bg": "entrance of a deep-sea temple underwater, soft blue light from above, streams of rising bubbles, tall coral pillars, cold clear water, a bubbling cauldron and rows of glass flasks far inside, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "カリブディス",
         "tags": "adult woman, mature female, mature face, gentle adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, deep forest green hair, very long hair, violet eyes, round glasses, white lab-coat-like robe with very long sleeves covering her hands, sleeves past fingers, many soft pale green sea-anemone tentacles below the waist instead of legs, round suckers, glistening, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the green-haired sea witch in round glasses and a long-sleeved robe",
         "pose": "one long sleeve raised to her lips, the other sleeve holding a blank seashell tablet without text, tentacles gently swaying below her, calm scholarly smile, looking down at viewer",
         "height_note": "she is taller than him",
         "neg": SOFT_NEG + ", human legs, feet, " + TENT_NEG},
   "e1": {"type": "woman", "jp": "絡新婦",
          "tags": "adult woman, mature female, mature face, elegant adult features, 32 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long straight hair, hime cut, golden eyes, purple kimono with a silver web pattern, wide obi, kanzashi hairpin, pale skin, fully human appearance, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the black-haired lady in a purple kimono",
          "pose": "sitting gracefully with a long incense pipe-like burner in one hand, thin white silk threads glinting between her fingers, incense smoke, composed old-fashioned smile, looking at viewer",
          "height_note": "she is taller than him",
          "neg": SOFT_NEG + ", " + SPIDER_NEG},
   "e2": {"type": "woman", "jp": "クラウン",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, short wavy hair, magenta eyes, white half mask covering the upper face, black and white jester costume, fluffy white ruff collar, two-pointed jester hat, playing card ornaments without text, white gloves, soft curvy feminine body, large breasts",
          "name": "the masked jester in a black and white costume",
          "pose": "one hand raised about to snap her fingers, the other hand fanning blank playing cards without text, head tilted, playful grin, looking at viewer",
          "neg": SOFT_NEG + ", creepy clown, horror, red nose"},
   "e3": {"type": "woman", "jp": "影女",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, charcoal grey hair, very long hair fading into wisps of shadow, glowing red eyes, tight black kimono, black obi, pale skin, dark shadow wisps around her feet, soft curvy feminine body, huge breasts, narrow waist, wide hips",
          "name": "the shadow woman with red eyes in a black kimono",
          "pose": "rising out of a long shadow on the floor, one hand reaching toward the viewer, mischievous fond grin, looking at viewer with red eyes",
          "height_note": "she is taller than him",
          "neg": SOFT_NEG + ", ghost, horror"},
   "boss": {"type": "woman", "jp": "LOVERS",
            "tags": "adult woman, mature female, mature face, serene adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, long straight hair worn down, silver-grey eyes, white and gold angel dress, gold trim, halo, wings of soft light, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the blonde angel in a white and gold dress",
            "pose": "hands clasped as if singing a hymn, standing beside a second adult woman with a blonde braid and a third adult woman with a blonde updo, all three alike in white and gold angel dresses with wings of light, serene smile, looking at viewer",
            "height_note": "she is taller than him",
            "neg": SOFT_NEG + ", feathered wings, mermaid tail"},
 },
 "places": {
   "room":     "hotel room at night, a bed, shoji-style paper window with shadows cast on it, bedside table, dim lamp",
   "hall":     "long hotel corridor at night, green emergency light, soft carpet, long shadows stretching on the floor",
   "casino":   "underground casino, roulette wheel, card table with green felt, stacks of chips, still air",
   "vip":      "casino VIP room, red sofa, playing-card pattern wallpaper without text, a stopped mantel clock, glasses of sweet liquor",
   "village":  "deserted mountain village in thick mist, an old stone well, empty wooden houses, grey sky",
   "audience": "samurai mansion audience hall, tatami mats, gold folding screen, incense smoke, fine silk threads glinting across the ceiling",
   "nest":     "bedchamber draped in white silk threads, a futon woven from white silk thread, paper lantern, soft warm light",
   "lab_hall": "white sterile corridor of a research facility, flat ceiling lights, small security device lights",
   "command":  "research facility command room, rows of monitors glowing pale light without text, clean white floor, faint light motes",
   "gate":     "a tall gate of soft golden light, cloud-like soft floor, drifting light motes, sweet haze",
   "temple":   "entrance of a deep-sea temple underwater, pale light from above, coral pillars, rising bubbles, clear cold water",
   "crucible": "witch's laboratory underwater, a large bubbling cauldron, shelves of glass flasks and test tubes, sweet pink potion, rising bubbles",
   "seal":     "sealed chamber underwater, old heavy chains hanging loosely, an ancient magic circle on the stone floor, cold dim water",
   "lab":      "deep-sea research room, a stone examination table, blank seashell tablets without text, walls covered with soft sea anemone tentacles, swaying pale lantern light",
   "abyss":    "the lightless bottom of the deep sea, a soft bed of pale sea anemone tentacles, slowly rising bubbles, faint glow",
 },
 "atk": {
   "m1": ("abyss", "he lies in a cradle woven from soft pale green tentacles, gently rocked, the sea witch leans over him whispering into his ear, her long sleeve resting on his chest, his body limp and dazed, " + AMU + ", " + BUB, {"neg": TENT_NEG}),
   "m2": ("lab", "from side, he floats in the air, pale green tentacles coiled softly around his wrists and ankles, " + SUCK + ", " + TIP + ", the sea witch beside him stroking him through her long sleeve, his own penis separate, " + AMU, {"neg": TENT_NEG}),
   "m3": ("abyss", "he is held upright in the sea witch's arms, his face buried deep between her huge breasts through her opened robe collar, tentacles wrapped softly around his legs, " + TIP + ", his own penis separate, " + AMU + ", " + BUB, {"neg": TENT_NEG}),
   "e1": ("audience", "he lies on his back on the tatami, wrists and ankles stitched down with soft white silk threads, the lady in the purple kimono leans over him, her huge breasts covering his face through her loosened collar, one slender finger stroking his nipple, incense smoke, " + AMU, {"neg": SPIDER_NEG}),
   "e2": ("casino", "he sits frozen on the edge of the card table, chips hanging motionless in the air, the masked jester presses his face between her breasts through her opened costume front, her gloved fingers teasing his nipple, playful grin, " + AMU),
   "e3": ("room", "he stands frozen with his shadow pinned to the floor by black shadow threads, the shadow woman holds his face against her huge breasts, a dark shadow hand stroking his nipple, another shadow finger in his anus, fingering, shoji shadows, " + AMU),
   "boss": ("command", "he kneels on the white floor, the blonde angel kneels facing him kissing him deeply, tongues, one hand stroking his nipple, the oiled fingers of her other hand in his anus, fingering, wings of light folded around them, monitor glow, " + AMU),
 },
 "atk_desc": {
   "m1": "the sea witch rocks him in a tentacle cradle and whispers that he is her assistant.",
   "m2": "the sea witch lifts him with her tentacles, sucks his nipples with soft suckers and strokes inside with a smooth tentacle tip.",
   "m3": "the sea witch sinks his face into her breasts like a bath while a tentacle tip presses inside.",
   "e1": "the lady stitches him down with silk threads and wraps his face in her breasts amid incense.",
   "e2": "the jester stops time and plays with him between her breasts.",
   "e3": "the shadow woman pins his shadow and teases him everywhere at once with shadow hands.",
   "boss": "the angel kisses him while singing a hymn, her fingers on his nipple and inside him.",
 },
 "lose": {
   # カリブディス 技1（安息揺籠化）
   "btl_m1":     ("abyss", "he lies in a swaying cradle of soft pale green tentacles, tentacles coiled around his wrists and ankles, " + SUCK + ", " + TIP + ", the sea witch leans over whispering at his ear, a seashell necklace on his chest, his own penis separate, cum dripping untouched, " + BUB, {"neg": TENT_NEG}),
   "onani_m1":   ("room", "lying alone on the bed beside the swaying window curtain, rocking his body, one hand stroking his own nipple, a finger of the other hand in his own anus, penis untouched, " + AMU + " glowing, the sea witch watches far away as a silhouette on the shoji"),
   "inochi_m1":  ("temple", "he lies on a stone table by the coral pillars inside a cradle of tentacles, the sea witch leans over him, " + SUCK + ", " + TIP + ", a blank seashell tablet without text in her sleeve, his own penis separate, cum dripping, " + BUB, {"neg": TENT_NEG}),
   "onedari_m1": ("lab", "he lies in a tentacle cradle hanging beside the examination table, rocked slowly, the sea witch whispers at his ear, " + SUCK + ", " + TIP + ", his lips moving in answer, his own penis separate, cum dripping, " + AMU, {"neg": TENT_NEG}),
   # カリブディス 技2（★吸盤捕獲）
   "btl_m2":     ("lab", "from side, he floats high in the air, tentacles coiled around his wrists and ankles, " + SUCK + ", " + TIP + ", the sea witch holds a blank seashell tablet without text, his own penis separate, cum dripping untouched, " + AMU, {"neg": TENT_NEG}),
   "onani_m2":   ("crucible", "crouching alone behind the large cauldron, wearing a shirt with overlong sleeves, stroking his own nipple through the sleeve, a wet finger of the other hand in his own anus, penis untouched, " + AMU + " glowing, the sea witch watches far away among the flasks"),
   "inochi_m2":  ("seal", "he leans back against the old loose chains, tentacles coiled around his arms, " + SUCK + ", " + TIP + ", the sea witch close in front of him smiling, the magic circle faintly glowing, his own penis separate, cum dripping, " + AMU, {"neg": TENT_NEG}),
   "onedari_m2": ("lab", "from side, he lies on his back on the stone examination table, six tentacles wrapped around his limbs, " + SUCK + ", " + TIP + " deep, the sea witch counting on her sleeve, his own penis separate, cum on his stomach, " + AMU, {"neg": TENT_NEG}),
   # カリブディス 技3（乳房風呂入浴）
   "btl_m3":     ("abyss", "he is held in the sea witch's arms, his face sunk between her huge breasts through her opened robe collar, tentacles around his limbs, " + SUCK + ", " + TIP + ", a white pearl on a cord at his neck beside the amulet, his own penis separate, cum dripping, " + BUB, {"neg": TENT_NEG}),
   "onani_m3":   ("hall", "kneeling alone in a dark corner of the corridor, his face buried in a pillow, sucking two of his own fingers, the other hand reaching behind to stroke his own anus, penis untouched, " + AMU + " glowing, the sea witch watches far away at the end of the corridor"),
   "inochi_m3":  ("temple", "he sits sunk to his shoulders in the sea witch's embrace, the sea witch kissing him deeply, tongues, her huge breasts pressed around his neck, " + TIP + ", " + SUCK + ", his own penis separate, cum dripping, " + BUB, {"neg": TENT_NEG}),
   "onedari_m3": ("abyss", "he lies on the soft bed of pale tentacles, the sea witch over him, his face deep between her huge breasts, " + SUCK + ", " + TIP + " deep, his arms limp, his own penis separate, cum on his stomach, " + AMU + ", " + BUB, {"neg": TENT_NEG}),
   # 絡新婦（★愛し糸の呪縛）
   "btl_e1":     ("audience", "he lies on his back on the tatami, wrists and ankles stitched down with soft white silk threads from the ceiling, the lady in the purple kimono covers his face with her huge breasts, one finger on his nipple, two oiled fingers in his anus, fingering, a chip of incense wood by his amulet, cum on his stomach", {"neg": SPIDER_NEG}),
   "onani_e1":   ("village", "wrapped alone in a futon in an empty house, a cheap incense stick burning beside him, both hands stroking his own nipples under the blanket, penis untouched, " + AMU + " glowing, the lady in the purple kimono watches far away in the mist outside"),
   "inochi_e1":  ("village", "he lies on his back beside the old stone well in the mist, limbs stitched down with white silk threads, the lady in the purple kimono leans over him wrapping his face in her breasts, her finger pressing in his anus, fingering, cum dripping, " + AMU, {"neg": SPIDER_NEG}),
   "onedari_e1": ("nest", "he lies on the white silk-thread futon, wrists and ankles stitched down with silk threads, the lady in the purple kimono lies over him, his face deep between her huge breasts, her fingers on his nipple and in his anus, fingering, lantern light, cum on his stomach, " + AMU, {"neg": SPIDER_NEG}),
   # クラウン（★時間停止の胸遊び）
   "btl_e2":     ("casino", "he lies on his back on the card table, chips frozen in mid-air, the masked jester leans over pressing his face between her breasts through her opened costume front, pinching his nipple, snapping her fingers, a blank joker card on his chest, cum dripping untouched, " + AMU),
   "onani_e2":   ("vip", "sitting alone and perfectly still on the red sofa, holding his breath, both hands suddenly pinching his own nipples, penis untouched, " + AMU + " glowing, the masked jester watches far away leaning in the doorway"),
   "inochi_e2":  ("casino", "he sits at the card table with his hand frozen above a face-down card without text, the masked jester sits on the table edge hugging his head between her breasts, her gloved fingers on his nipple, roulette wheel stopped, cum dripping, " + AMU),
   "onedari_e2": ("vip", "he sits frozen on the red sofa, the masked jester straddles his lap pressing his face between her breasts, both gloved hands teasing his nipples, three fingers raised in a count, the stopped mantel clock, cum dripping untouched, " + AMU),
   # 影女（★影縫い）
   "btl_e3":     ("room", "he stands pinned by black shadow threads from the shoji shadows, the shadow woman holds his face against her huge breasts, a dark shadow hand stroking his nipple, a shadow finger pressing in his anus, fingering, a black woven cord tied to his amulet, cum dripping untouched"),
   "onani_e3":   ("hall", "crouching alone under the green emergency light, staring at his own long shadow on the carpet, one hand stroking his own nipple, a finger of the other hand in his own anus, penis untouched, " + AMU + " glowing, the shadow woman watches far away rising from the shadow"),
   "inochi_e3":  ("room", "he lies on the bed with one arm stretched toward the amulet on the bedside table, the arm pinned by shadow threads, the shadow woman lies over him wrapping his face in her breasts, a shadow finger in his anus, fingering, cum dripping"),
   "onedari_e3": ("room", "he lies on his back on the bed, wrists and ankles pinned by black shadow threads, the shadow woman kneels over him pressing her breasts onto his face, shadow hands on both his nipples, a shadow finger pressing in his anus, fingering, grinning, cum on his stomach, " + AMU),
   # LOVERS（★恋人たちの楽園）
   "btl_boss":   ("command", "he kneels on the white floor in the monitor glow, the blonde angel kneels facing him kissing him deeply, tongues, one hand stroking his nipple, oiled fingers of her other hand in his anus, fingering, wings of light around them, a charm of three woven light feathers by his amulet, cum dripping untouched"),
   "onani_boss": ("lab_hall", "kneeling alone in a corner of the white corridor, lips parted as if humming a hymn, one hand stroking his own nipple, a finger of the other hand in his own anus, penis untouched, " + AMU + " glowing, the blonde angel watches far away down the corridor"),
   "inochi_boss":("gate", "he kneels on the cloud-like floor before the tall gate of light, the blonde angel holds his face kissing him, her other hand behind him with oiled fingers in his anus, fingering, wings of light, drifting light motes, cum dripping, " + AMU),
   "onedari_boss":("command", "he sits on a white chair in the middle of the room, the blonde angel leans over him from the front kissing him, tongues, one hand on his nipple, oiled fingers in his anus, fingering, singing softly, wings of light spread, cum dripping, " + AMU),
 },
 "lose_desc": "takes him down to the deep sea forever as the witch's eternal research assistant, his brass amulet stained black with twelve shadow streaks.",
 "onanie": {
   "master": ("crucible", "crouching behind the cauldron in a shirt with overlong sleeves, stroking his own nipple through the sleeve, a wet finger of the other hand in his own anus, penis untouched, " + AMU),
   "e1": ("village", "wrapped in a futon beside a burning incense stick, both hands stroking his own nipples, penis untouched, " + AMU),
   "e2": ("vip", "sitting perfectly still on the red sofa holding his breath, then pinching both his own nipples at once, penis untouched, " + AMU),
   "e3": ("hall", "crouching under the green light staring at his own long shadow, one hand on his own nipple, a finger of the other hand in his own anus, penis untouched, " + AMU),
   "boss": ("lab_hall", "kneeling in the white corridor humming a hymn, one hand on his own nipple, a finger of the other hand in his own anus, penis untouched, " + AMU),
 },
 "magic": {
   "1": (None, "room", "a cheap brass amulet on a thin chain lying on a pillow, two fresh black shadow streaks running across it, cold faint glow, close-up, amulet without text"),
   "2": (None, "crucible", "a round glass flask of sweet pink potion on a shelf, a single large bubble rising and bursting at its neck, soft glow, close-up, flask without text"),
   "3": ("e2", "casino", "snapping her gloved fingers, a dome of faint light with playing-card patterns without text spreading around her, chips frozen in mid-air, playful wink"),
   "4": (None, "audience", "a small bronze incense burner on a lacquered tray, a chip of dark agarwood smoldering, thin fragrant smoke curling upward, fine silk threads glinting above, close-up"),
   "5": ("m", "crucible", "stirring the large bubbling cauldron with a long ladle held in her sleeve, rows of flasks glowing behind her, gentle scholarly smile, rising bubbles"),
 },
}
