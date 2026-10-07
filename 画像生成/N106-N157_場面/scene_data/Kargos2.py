# N128 カルゴス団・新幹部（Kargos2）画像データ。登場人物は全員20歳以上。5人とも成人女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作に青・水色の髪や瞳の指定はない
# （瞳の色はこのMOD用に決めた：シックス＝amber、バニー・バニー＝violet、コルダ＝red。テレサは仮面、ライフピンクはヘルメットで顔を見せない）。
# 髪色は 銀（テレサ）／緑（シックス）／金（バニー・バニー）／黒（コルダ）で被らせない。ライフピンクは髪がヘルメットの中。
# 挿入はシックスの柔らかい実験器具だけ（pen: toy）。テレサは指だけ（pen なし）。バニー・バニー、コルダ、ライフピンクは後ろに触れない。
# 鞭は空で鳴らすだけ（肌を打たない・跡なし）。顔面騎乗は体重を掛けきらない。主人公の胸元には金色の小さな天秤の印。
# テレサの仮面：m3（仮面の下）系は「半分ずらす」まで。素顔は描かない（唇だけ見える）。番号札・モニターに文字や数字は描かない。
T = {"pen": "toy"}
MARK = "a small glowing golden balance-scale mark on his chest below his collarbone"
ROD = "a soft warm rounded rod instrument in his anus"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary"
WHIP_NEG = "whip striking skin, whip marks, welts, wound, bruise"
DATA = {
 "code": "Kargos2",
 "world": "secret base of an evil organization in a modern city at night, cold lamps, banners with an emblem without text, a small golden balance scale motif, detailed background",
 "bg": "quiet stone hall deep inside a secret base, a giant golden balance scale on a stone pedestal in the center, polished stone floor, tall pillars, a dark banner with an emblem without text far away, soft cold light, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "テレサ",
         "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, tall, long legs, very long straight silver hair, white-silver mask covering her upper face, gold body jewelry, gold armlets, gold necklace, thin white robe, smooth slender curvy body, slender fingers, large breasts",
         "name": "the silver-haired woman in a white-silver mask",
         "pose": "holding up a small golden balance scale in one hand, the other hand at her side, calm neutral closed mouth, face turned to viewer",
         "neg": SOFT_NEG + ", mask removed, bare face"},
   "e1": {"type": "woman", "jp": "バニー・バニー",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, long wavy blonde hair, violet eyes, purple domino mask, rabbit ears headband, black bunny girl leotard, bow tie collar, wrist cuffs, black pantyhose, white fluffy rabbit tail, soft voluptuous body, huge breasts, wide hips, large round buttocks",
          "name": "the blonde bunny girl in a purple domino mask",
          "pose": "looking back over her shoulder showing her fluffy white rabbit tail, holding a champagne glass, teasing smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "コルダ",
          "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, long straight black hair, cold red eyes, black military uniform, black peaked military cap, black gloves, polished black boots, holding a black riding whip, soft voluptuous body, gigantic breasts, wide hips",
          "name": "the black-haired officer in a black military uniform",
          "pose": "standing at attention with one hand on her hip, the whip resting on her shoulder, cold stern gaze, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", " + WHIP_NEG},
   "e3": {"type": "woman", "jp": "ライフピンク",
          "tags": "adult woman, mature female, 26 years old, adult proportions, long legs, pink skintight glossy battle suit covering her whole body, white gloves and boots, full-face pink helmet with a dark visor, face hidden, hair hidden inside the helmet, emblem on her chest without text, slender curvy feminine body, large breasts",
          "name": "the heroine in a pink skintight battle suit and full-face helmet",
          "pose": "standing with arms crossed under her chest, head tilted, looking down at viewer through the dark visor",
          "neg": SOFT_NEG + ", helmet removed, bare face, visible hair"},
   "boss": {"type": "woman", "jp": "シックス",
            "tags": "adult woman, mature female, mature face, 31 years old, adult proportions, beautiful detailed eyes, tall, long legs, green hair, twin braids, round glasses, amber eyes, white lab coat, tight low-cut black top under the lab coat, black pencil skirt, thin rubber gloves, soft voluptuous body, gigantic breasts, wide hips",
            "name": "the green-braided doctor in a white lab coat and round glasses",
            "pose": "holding her lab coat open with one hand to show off her cleavage in the tight top, a blank clipboard without text in the other hand, wide excited grin, looking at viewer",
            "neg": SOFT_NEG + ", scalpel, needle, syringe, blood"},
 },
 "places": {
   "under":    "base basement corridor, heavy iron door, cold lamp, iron bars of a cell far behind",
   "bridge":   "large bridge at night, cold stone railing, river below, city lights far away, wind",
   "tunnel":   "secret room deep in a dark tunnel, damp walls, a single bare light bulb, water drops",
   "city":     "back alley of a neon-lit downtown at night, air conditioner units on the wall, neon glow without text",
   "club":     "dim hostess club lounge, red velvet sofas, champagne glasses, rabbit-ear ornaments, low warm light",
   "vip":      "club VIP room, canopy sofa with red cushions, a fluffy white rabbit-tail cushion, champagne bucket, thick padded door",
   "ward":     "hospital room at dusk, white bed, drawn curtain, IV stand, orange light from the window",
   "surgery":  "operating room, a soft padded operating table, round surgical lamp, a blank monitor without text, tray of soft rounded instruments",
   "prison":   "great prison entrance hall, iron bars, cold wide stone floor, dripping water",
   "pool":     "indoor prison pool, white tiles, cold still water, a poolside chair, rippling light reflections",
   "floor":    "base first floor hall, polished floor, humming machines, thick pillars, a dark banner with an emblem without text",
   "officer":  "officer's private room, military flags without text, a black leather chair, polished boots on a rack",
   "store":    "hidden storeroom, dusty shelves of old files, an old hero suit on a stand, a thin beam of light between the shelves",
   "scale":    "quiet stone hall, a giant golden balance scale on a stone pedestal, golden pans, polished stone floor",
   "private":  "private bedroom, masks displayed on the wall, a soft bed with thin white drapes, a small golden balance scale on a bedside table",
 },
 "atk": {
   "m1": ("scale", "he kneels before the pedestal with his shirt opened, the masked woman stands over him holding a small golden balance scale that casts a beam of warm light on his chest, her other hand pinching his nipple with slender fingers, " + MARK + ", the scale tilting, he trembles"),
   "m2": ("floor", "he kneels on the polished floor with his chin lifted, the masked woman bends down behind him whispering into his ear, her lips at his ear, one slender hand under his chin, her small golden scale tilting in her other hand, " + MARK + ", his knees apart, flushed"),
   "m3": ("private", "he lies on his back on the soft bed, the masked woman leans over him with her mask pushed half up showing only her lips, kissing him deeply, her palm covering his hidden eyes, two wet slender fingers of her other hand in his anus, fingering, " + MARK),
   "e1": ("vip", "he lies on his back on the canopy sofa, the bunny girl sits gently on his face with her large round buttocks facing his head, her fluffy white tail at his nose, she leans forward stroking his nipple with one hand and his penis with the other, " + MARK + ", teasing smile"),
   "e2": ("officer", "he stands rigidly at attention with his arms at his sides, the officer holds his face buried between her gigantic breasts through her opened uniform top, her whip raised in the air without touching him, stern cold gaze, " + MARK + ", his knees trembling"),
   "e3": ("store", "he lies on his back on the storeroom floor, the heroine in the pink suit lies on top of him pinning his wrists with her body weight, her visor looking down at his face, one gloved hand stroking his nipple, the other on his penis, " + MARK),
   "boss": ("surgery", "from side, he lies on his back on the soft operating table with knees raised, the doctor stands between his legs holding her lab coat open showing her cleavage, her gloved hand pressing " + ROD + ", his own penis untouched, a blank monitor, " + MARK, T),
 },
 "atk_desc": {
   "m1": "the masked woman weighs his heart with the light of her golden scale and pinches his nipple.",
   "m2": "the masked woman keeps whispering which side he wants to tilt toward until he kneels by himself.",
   "m3": "the masked woman pushes her mask half up and kisses him while pressing inside with her fingers.",
   "e1": "the bunny girl sits on his face and tickles his nose with her tail while stroking him.",
   "e2": "the officer drills him at attention with his face held between her breasts.",
   "e3": "the heroine pins him down with her suited body and looks down through her visor.",
   "boss": "the doctor experiments on him with a soft instrument at a steady rhythm while showing off her chest.",
 },
 "lose": {
   # テレサ 技1（★天秤の裁き）
   "btl_m1":     ("scale", "he lies on his back at the foot of the stone pedestal with his shirt open, the masked woman kneels beside him, a beam of light from her small golden scale on his chest, pinching his nipple, two wet slender fingers in his anus, fingering, a small gold scale necklace on him, cum dripping untouched"),
   "onani_m1":   ("store", "kneeling alone behind a dusty shelf, tracing the glowing golden scale mark on his chest with a fingertip, the other hand reaching behind with a finger in his own anus, penis untouched, the masked woman watches far away in the thin beam of light"),
   "inochi_m1":  ("under", "he leans back against the heavy iron door holding his own shirt open, the masked woman stands close casting warm light from her small golden scale onto his chest, pinching his nipple with slender fingers, " + MARK + ", his knees giving way, cum dripping untouched"),
   "onedari_m1": ("scale", "he sits on the stone pedestal next to the golden pan with his legs apart, the masked woman stands between them, light from her scale on his chest, two wet fingers pressing in his anus, fingering, her other hand on his nipple, " + MARK + ", cum dripping"),
   # テレサ 技2（中立の誘い＋★）
   "btl_m2":     ("floor", "he kneels on the polished floor with his chin lifted, the masked woman kneels behind him whispering into his ear, her fingers pressing in his anus from behind, fingering, light from her scale on his chest, a blank white mask without text lying beside his knee, cum dripping"),
   "onani_m2":   ("bridge", "crouching alone in the shadow of the stone railing at night, lips moving as if asking himself a question, one hand reaching behind pressing a finger into his own anus, penis untouched, the masked woman watches far away on the bridge, hair in the wind"),
   "inochi_m2":  ("scale", "he kneels before the giant golden scale with his mouth open mid-answer, the masked woman bends to his ear whispering, one hand pinching his nipple, the golden pan tilting down beside them, " + MARK + ", flushed, cum dripping untouched"),
   "onedari_m2": ("private", "he kneels at the foot of the soft bed looking up, the masked woman sits on the bed edge leaning to his ear, flustered posture with one hand near her mask, her other hand casting light from the small scale on his chest, " + MARK + ", cum dripping untouched"),
   # テレサ 技3（仮面の下＋★）
   "btl_m3":     ("private", "he lies on his back on the bed under white drapes, the masked woman over him with her mask pushed half up showing only her lips, kissing him deeply, tongues, her palm covering his hidden eyes, two fingers in his anus, fingering, a mask cord tied on his wrist, cum on his stomach"),
   "onani_m3":   ("pool", "sitting alone on the poolside tiles, covering half of his own face with one hand while sucking two fingers of it, the other hand reaching behind with a finger in his own anus, penis untouched, the masked woman watches far away across the still water"),
   "inochi_m3":  ("scale", "he stands with his back against the stone pedestal, the masked woman holds his face and kisses him with her mask pushed half up showing only her lips, her other hand behind him with fingers in his anus, fingering, " + MARK + ", cum dripping untouched"),
   "onedari_m3": ("private", "from behind her shoulder, he lies on half of the soft bed, the silver-haired woman over him holds her removed mask in one hand with her face turned away from view, kissing him, her fingers deep in his anus, fingering, long silver hair falling over them, cum on his stomach", {"neg": "her face visible from the front"}),
   # バニー・バニー（★ラビットヒッププレス）
   "btl_e1":     ("vip", "he lies on his back on the canopy sofa, the bunny girl sits gently on his face with her large round buttocks, her fluffy white tail tickling his nose, she leans forward stroking his nipple and his penis, a small white rabbit-tail charm on his neck, cum on his stomach"),
   "onani_e1":   ("club", "lying alone on his back behind a red sofa, pressing a red cushion onto his own face with one hand, the other hand stroking his own nipple, penis untouched, the bunny girl watches far away from the counter with a glass"),
   "inochi_e1":  ("club", "he lies back on the red velvet sofa, the bunny girl leans over him feeding him champagne mouth to mouth, kiss, champagne dripping from his lips, her huge soft breasts pressed against his chest, empty glasses on the table, " + MARK),
   "onedari_e1": ("vip", "he lies on his back on the sofa with a fluffy white rabbit-tail cushion beside his head, the bunny girl sits gently on his face looking back over her shoulder, one hand stroking his nipple, her finger raised as if counting, cum dripping untouched"),
   # コルダ（★乳指導）
   "btl_e2":     ("officer", "he stands at attention with heels together, the officer holds his face deep between her gigantic breasts through her opened uniform top, rocking him gently, her whip raised in the air without touching him, a blank rank badge without text pinned on his chest, cum dripping untouched"),
   "onani_e2":   ("tunnel", "standing alone at attention under the bare light bulb with heels together and back straight, both hands pinching his own nipples, penis untouched, the officer watches far away from the tunnel doorway with her whip"),
   "inochi_e2":  ("prison", "he stands at attention on the cold stone floor of the prison hall, the officer holds his face between her gigantic breasts, rocking him as praise, her whip held up in the air, a blank dog tag without text on his neck, cum dripping untouched"),
   "onedari_e2": ("officer", "he stands at attention beside the door like a sentry, the officer presses his face deep between her gigantic breasts with one arm, cracking her whip in the empty air with the other, cold satisfied smile, " + MARK + ", cum dripping untouched"),
   # ライフピンク（★元ヒーローの拘束）
   "btl_e3":     ("store", "he lies on his back on the storeroom floor, the heroine in the pink suit lies on top of him pinning him with her whole body, her visor close above his face, one gloved hand stroking his nipple, the other on his penis, a pink badge without text on his chest, cum on his stomach"),
   "onani_e3":   ("floor", "lying alone face down on the polished floor behind a pillar, pressing his chest to the floor with his own weight, one hand under his chest stroking his own nipple, penis untouched, the heroine in the pink suit watches far away across the hall"),
   "inochi_e3":  ("city", "he is pressed with his back against the alley wall, the heroine in the pink suit pins him with her whole body, her helmet beside his ear as if whispering, one gloved hand stroking his nipple, neon glow, " + MARK + ", his knees weak, cum dripping untouched"),
   "onedari_e3": ("store", "he lies face down on the floor beside the old hero suit on its stand, the heroine in the pink suit lies on his back pinning him, her helmet at his ear whispering, her gloved hand reaching under his chest to stroke his nipple, cum dripping untouched"),
   # シックス（★人体実験）
   "btl_boss":   ("surgery", "from side, he lies on his back on the soft operating table with knees raised, the doctor stands between his legs holding her lab coat open showing her cleavage, her gloved hand pressing " + ROD + ", a blank tag without text on his wrist, his own penis untouched, cum on his stomach", T),
   "onani_boss": ("ward", "lying alone on his back on the white bed behind the drawn curtain with knees raised, pressing a finger into his own anus at a steady rhythm, penis untouched, the doctor watches far away through a gap in the curtain"),
   "inochi_boss":("ward", "from side, he lies on the white hospital bed with a soft ring device around his head, the doctor sits on the bed edge with her lab coat open, her gloved hand pressing " + ROD + ", a blank clipboard without text on the sheet, his own penis untouched, cum dripping", T),
   "onedari_boss":("surgery", "from side, he lies on the operating table with legs apart, the doctor leans over him with her lab coat open, counting on the fingers of one gloved hand, the other hand slowly pressing " + ROD + ", an assistant's stool beside the table, his own penis untouched, cum on his stomach", T),
 },
 "lose_desc": "keeps him forever at the masked woman's side as the cherished weight of her golden scale, the golden mark on his chest tilted all the way to the evil side.",
 "onanie": {
   "master": ("scale", "kneeling, tracing the glowing golden scale mark on his chest with a fingertip, the other hand reaching behind with a finger in his own anus, penis untouched"),
   "e1": ("club", "lying on his back, pressing a cushion onto his own face with one hand, the other hand stroking his own nipple, penis untouched"),
   "e2": ("officer", "standing at attention with heels together, both hands pinching his own nipples, penis untouched"),
   "e3": ("floor", "lying face down pressing his chest to the floor with his own weight, one hand under his chest stroking his own nipple, penis untouched"),
   "boss": ("ward", "lying on his back with knees raised, pressing a finger into his own anus at a steady rhythm, penis untouched"),
 },
 "magic": {
   "1": (None, "scale", "close-up of a golden pan of a balance scale with two tiny golden weights on it, the pan tilting down, soft warm glow, faint ring of light as if chiming"),
   "2": (None, "officer", "a row of ornate doors along a dim corridor, one door slightly open with warm light spilling out, door plates blank without text"),
   "3": ("boss", "surgery", "holding her white lab coat wide open with both hands to show off her deep cleavage in the tight low-cut top, excited laughing grin, sparkles"),
   "4": (None, "club", "a tall champagne glass with a tiny rabbit-ear ornament on its rim, golden champagne with fine bubbles, a bottle without text in an ice bucket, low warm light"),
   "5": (None, "scale", "a giant golden balance scale on a stone pedestal in a silent hall, one pan lowered, a faint ripple of light in the air, shafts of cold light"),
 },
}
