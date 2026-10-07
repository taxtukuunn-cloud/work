# N122 夢魔の魔王城（Queen2）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。髪・瞳の色は資料に無いので、5人で被らないように決めた
# （青・水色系は不使用。ソムニアの夜色のショールは dark violet-black と書く）。ソムニアはこのMOD用の新キャラ。
# 挿入はクイーンの尻尾の細い先端だけ（m3 の本。尻尾なので pen なし）。搾精口は包んで吸うだけ（歯なし・怖くしない＝花のつぼみ形の柔らかい先）。
# ヘルヴィナ・エデニア・シャオフーは指だけ。ソムニアは後ろに触れない。処刑台は布張りの柔らかい拘束台（刃物・血なし）。
# 主人公の左手首には黒い月の模様。小瓶・書類の文字は描かない。
MOON = "a black crescent moon mark on his left wrist"
BUD = "the soft flower-bud tip of her tail opened around his penis, sucking"
TIP = "the slim rounded tip of her tail inserted in his anus"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
TAIL_NEG = SOFT_NEG + ", teeth on the tail, monster mouth, horror, gore"
STOCK_NEG = SOFT_NEG + ", blade, guillotine, axe, blood, wound, choking"
DATA = {
 "code": "Queen2",
 "world": "castle of the succubus queen at the bottom of a dream world, endless night, a black moon in the sky, drifting black mist, violet flames, dreamy haze, detailed background",
 "bg": "throne room of a demon queen in a dream castle at night, a black throne on a dais, a large black moon floating under the high ceiling, a huge black and purple canopy bed at the side, violet flames in braziers, polished dark floor, black mist, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "クイーン",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, long legs, long wavy dark violet hair, golden eyes, small gold crown, black demon wings, black and purple queen dress with a high slit, long black fingernails, long tongue, bare feet, very long smooth black tail ending in a soft flower-bud-shaped tip, voluptuous feminine body, huge breasts, wide hips",
         "name": "the violet-haired queen in a crown and a black and purple dress",
         "pose": "sitting sideways on nothing with legs crossed, chin resting on the back of her hand, her long tail curling around her, haughty amused smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": TAIL_NEG},
   "e1": {"type": "woman", "jp": "エデニア",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, tall, long legs, platinum blonde hair, long hair, side ponytail, pink eyes, black feathered angel wings, white robe with very wide long sleeves, gold trim, bare shoulders, voluptuous feminine body, huge breasts, wide hips",
          "name": "the blonde fallen angel in a white wide-sleeved robe",
          "pose": "holding one wide sleeve open toward the viewer, the other hand at her mouth, teasing smug grin, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "シャオフー",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, black hair, double bun, bun covers, green eyes, small demon horns, red china dress with gold embroidery, side slit, thick thighs, huge ass, wide hips, slender waist, large breasts",
          "name": "the black-bun succubus in a red china dress",
          "pose": "standing turned halfway with her hip pushed out, holding a small medicine jar without text in one hand, the other hand lifting the hem of her dress at the slit, mocking laugh, looking down at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ソムニア",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver-grey hair, very long hair, loose single braid over her shoulder, sleepy half-closed violet eyes, black and white long maid dress, white apron, dark violet-black shawl, slender curvy feminine body, large breasts",
          "name": "the silver-braided head maid in a dark shawl",
          "pose": "hugging a large white pillow to her chest with both arms, head tilted, gentle drowsy smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "ヘルヴィナ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, crimson red hair, long straight hair, amber eyes, curved black demon horns, thin black demon tail, black high-collar officer dress with a heart-shaped cutout over her cleavage, black gloves, thick thighs, plump voluptuous feminine body, huge breasts, wide hips",
            "name": "the red-haired horned officer in a black dress with a heart cutout",
            "pose": "arms crossed under her chest, holding a sheaf of blank papers without text in one hand, proud tired sigh, looking down at viewer",
            "height_note": "she is much taller than him",
            "neg": STOCK_NEG},
 },
 "places": {
   "gate":     "gate at the bottom of the dream, a giant black gate half open, thick black mist, a black moon above",
   "maidroom": "maids' chamber, heaps of pillows and white sheets, lavender incense, soft warm lamps",
   "bedding":  "bedding storeroom, futons and quilts stacked up to the ceiling, quiet dim light, drowsy air",
   "china":    "chinese-style mansion hall, vermilion pillars, red paper lanterns, herbal haze",
   "pharmacy": "apothecary room, tall medicine cabinets with many small drawers, a stone mortar and pestle, small jars without text, sweet steam",
   "gold":     "golden temple, golden pillars, dazzling light, polished gold floor",
   "heaven":   "heavenly temple above white clouds, drifting feathers, a staircase of light, a soft cloud bed",
   "sleeve":   "a dreamlike soft room made of hanging white cloth like the inside of a wide sleeve, sweet pink haze, soft folds of fabric",
   "dark":     "temple of darkness, black stone pillars, violet flames, cold air, deep shadows behind the pillars",
   "exec":     "judgment hall, a padded pillory of black wood lined with soft velvet cushions, empty spectator seats, violet torchlight",
   "office":   "officer's study, a desk with piles of blank papers without text, a teacup, a bookshelf, lamp light",
   "corridor": "long castle corridor, tall windows showing a black moon, dark carpet, silent",
   "throne":   "demon queen's throne room, a black throne on a dais, a black moon floating under the ceiling, wide dark floor, violet flames",
   "bed":      "huge black and purple canopy bed, sheer canopy curtains, a black moon seen beyond the canopy, silk sheets, a small black bottle of oil on the bedside",
   "end":      "the end of the dream, a full black moon filling the sky, endless night, a canopy bed standing alone in black mist",
 },
 "atk": {
   "m1": ("throne", "he stands before the throne with his head tilted back, staring up at the black moon under the ceiling, the queen stands behind him holding his chin up with one long-nailed hand, whispering at his ear, her long tail coiling loosely around his legs, " + MOON + ", knees giving way"),
   "m2": ("bed", "he lies on his back on the bed, the queen's long tail coiled around his body, " + BUD + ", the queen leans over him, her long tongue wrapped around his nipple, her long nails tracing his side without scratching, " + MOON),
   "m3": ("throne", "from side, he lies on his back on the floor before the throne with knees up, the queen sits on the throne above him, her bare foot pressing his chest, her toes pinching his nipple, " + TIP + ", anal, his own penis separate, " + MOON),
   "e1": ("heaven", "he kneels on the cloud bed, the fallen angel kneels beside him covering his face with her wide white sleeve, his face buried inside the sleeve, pink haze leaking out, her other hand rubbing his nipple, teasing grin, his body limp, " + MOON),
   "e2": ("pharmacy", "he lies on his back on a low bench, glossy ointment shining on his nipples and inner thighs, the succubus sits over him with his head held between her thick thighs, her fingertip circling his nipple, mocking laugh, a small jar without text beside them, " + MOON),
   "e3": ("maidroom", "he lies on his side on the pillows hugging a large pillow, the head maid lies close behind him, her lips at his ear whispering a bedtime story, her fingertip gently stroking his nipple, his body going slack with sleep, " + MOON),
   "boss": ("exec", "he bends forward with his neck and wrists held in the padded velvet-lined pillory, the horned officer stands behind him, both gloved hands on his chest rolling his nipples, a faint warm pink glow at her fingertips, tired smirk, his legs trembling, " + MOON),
 },
 "atk_desc": {
   "m1": "the queen makes him gaze at the black moon until he no longer wishes to wake.",
   "m2": "the queen coils her tail around him, the soft bud tip sucking while her tongue licks his nipple.",
   "m3": "the queen steps on his chest from her throne while the slim tip of her tail presses inside him.",
   "e1": "the fallen angel makes him breathe the sweet scent inside her sleeve while teasing him.",
   "e2": "the succubus rubs sensitivity ointment on him and holds him between her heavy thighs.",
   "e3": "the head maid whispers a bedtime story into his ear and strokes his nipple as he falls asleep.",
   "boss": "the officer locks him in a soft padded pillory and pours warm corrupting heat through her fingers.",
 },
 "lose": {
   # クイーン 技1（クイン大技ディス＋搾精口の夜）
   "btl_m1":     ("throne", "he lies on his back staring up at the full black moon, the queen's long tail coiled around his body, " + BUD + ", the queen kneels over him licking his nipple with her long tongue, a black moon pendant on his neck, cum"),
   "onani_m1":   ("corridor", "standing alone at a tall window looking up at the black moon, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, " + MOON + " glowing, penis untouched, the queen watches far away at the end of the corridor"),
   "inochi_m1":  ("gate", "he stands before the half-open black gate holding its handle, looking through it at a black moon, the queen stands behind him, her long tail coiled around his waist and legs, " + BUD + ", her long nails on his chest, black mist, his knees giving way"),
   "onedari_m1": ("bed", "he lies inside the coils of the queen's long tail, looking up at the black moon beyond the canopy, " + BUD + ", the queen lies beside him, her long tongue on his nipple, " + MOON + " glowing, cum"),
   # クイーン 技2（★搾精口の夜）
   "btl_m2":     ("bed", "he lies on the silk sheets wrapped in the coils of the queen's long tail, " + BUD + ", the queen leans over him, her long tongue wrapped around his nipple, her long nails tracing his side without scratching, a ring of black scales on his finger, cum overflowing"),
   "onani_m2":   ("bedding", "sitting alone behind a stack of futons, a long white cloth wound around his body like coils, one wet fingertip stroking his own nipple, " + MOON + " glowing, penis untouched, the queen's tail tip peeks far away over the futons, the queen watches from the doorway"),
   "inochi_m2":  ("throne", "he crawls on the dark floor into the open coils of the queen's long tail, the queen sits on the floor before the throne with her arms open, " + BUD + ", her long tongue reaching his nipple, the black moon under the ceiling, no dawn, sleepy, cum dripping"),
   "onedari_m2": ("bed", "he lies in the middle of the bed tightly wrapped in the queen's long tail, " + BUD + ", the queen holds up four fingers counting, her long tongue licking his nipple, " + MOON + " glowing, his back arched, cum"),
   # クイーン 技3（クイン大技足＋搾精口の夜）
   "btl_m3":     ("throne", "from side, he lies on a rug at the foot of the throne, the queen sits on the throne above, her bare foot pressing his chest, her toes pinching his nipple, " + TIP + ", anal, his own penis separate, the full black moon above, cum on his stomach"),
   "onani_m3":   ("dark", "sitting alone behind a black stone pillar with one knee bent, pressing the sole of his own foot against his lower belly, a wet finger of one hand in his own anus, " + MOON + " glowing, penis untouched, the queen watches far away beside a violet flame"),
   "inochi_m3":  ("throne", "he kneels before the throne kissing the top of the queen's bare foot, the queen sits on the throne lifting his chin with the toes of her other foot, " + TIP + ", anal, his own penis separate, haughty laugh, " + MOON),
   "onedari_m3": ("throne", "from side, he lies on his back on a cushioned footstool, the queen sits on the throne above, one bare foot on his chest, the other on his lower belly, " + TIP + ", anal, his own penis separate, " + MOON + " glowing, cum on his stomach"),
   # エデニア（★袖のフェロモン）
   "btl_e1":     ("heaven", "he lies on the cloud bed with his face buried inside the fallen angel's wide white sleeve, the fallen angel kneels over him, her other hand between his legs with two oiled fingers in his anus, fingering, feathers drifting, a white feather and a black feather in his hair, cum dripping untouched"),
   "onani_e1":   ("sleeve", "kneeling alone among the hanging white cloth, his face pressed into the sleeve of his own shirt, one hand rubbing his own nipple, the other hand behind with a finger in his own anus, " + MOON + " glowing, penis untouched, the fallen angel watches far away through the folds of cloth"),
   "inochi_e1":  ("heaven", "he has sunk to his knees on the staircase of light, the fallen angel crouches on the step above wrapping her wide white sleeve over his head and face, her hand on his nipple, teasing grin, feathers drifting, " + MOON),
   "onedari_e1": ("heaven", "he lies on his side on the cloud bed breathing deeply inside the fallen angel's wide sleeve, the fallen angel lies behind him whispering teasingly at his ear, her oiled fingers in his anus, fingering, her wing folded over them, " + MOON + " glowing, cum dripping"),
   # シャオフー（★薬塗りと太腿）
   "btl_e2":     ("pharmacy", "he lies on his back on a low bench, glossy ointment on his nipples and inner thighs, the succubus sits over him with his head held between her thick thighs, leaning forward, two ointment-coated fingers in his anus, fingering, a small jar without text beside them, cum on his stomach"),
   "onani_e2":   ("china", "lying alone on his side under the red lanterns, squeezing a pillow between his own thighs, a fingertip rubbing his own nipple, " + MOON + " glowing, penis untouched, the succubus watches far away leaning on a vermilion pillar"),
   "inochi_e2":  ("china", "he lies face up on the floor beside a mortar and herbs, the succubus sits on his stomach with her huge ass, her back to his face, her ointment-coated fingertip rubbing his nipple, mocking laugh over her shoulder, a row of blank jars, " + MOON),
   "onedari_e2": ("pharmacy", "he sits on a low stool, the succubus stands over him with one leg on the bench, his face held between her thick thighs, her ointment-coated fingers stroking both his nipples from above, a mortar beside them, " + MOON + " glowing, cum dripping"),
   # ソムニア（★寝物語）
   "btl_e3":     ("maidroom", "he lies asleep on his side on a heap of pillows hugging a large pillow, the head maid lies close behind him under a quilt, her lips on his earlobe whispering, her fingertip stroking his nipple, a scrap of dark shawl tied on his wrist, dreamy haze, cum dripping untouched"),
   "onani_e3":   ("bedding", "lying alone half asleep on top of a stack of futons, hugging a pillow with one arm, the other fingertip slowly stroking his own nipple, " + MOON + " glowing, penis untouched, the head maid watches far below holding a pillow"),
   "inochi_e3":  ("maidroom", "he lies wrapped up to his shoulders in thick futons, hugging a pillow, the head maid sits beside his head, bending down to whisper at his ear, her hand slipped under the quilt on his chest, soft lamp light, " + MOON + ", drowsy"),
   "onedari_e3": ("maidroom", "he lies on his back with his head on the softest large pillow, the head maid lies along his side, her lips at his ear whispering the last line of a story, her fingertip on his nipple, dreamy haze, " + MOON + " glowing, cum dripping untouched"),
   # ヘルヴィナ（★堕落の処刑台）
   "btl_boss":   ("exec", "he bends forward with his neck and wrists held in the padded velvet-lined pillory, the horned officer stands behind him, one gloved hand rolling his nipple with a faint pink glow, two oiled fingers of her other hand in his anus, fingering, a black heart-shaped charm on his neck, cum dripping untouched"),
   "onani_boss": ("office", "lying alone face down in the corner of the study, holding a pillow over his own neck and one wrist, a wet finger of the other hand in his own anus, " + MOON + " glowing, penis untouched, the horned officer watches far away from the desk, sighing over her papers"),
   "inochi_boss":("dark", "he kneels at a low desk piled with blank papers without text holding a stamp, the horned officer kneels close behind him, her gloved hands slipped inside his shirt on his nipples, a faint pink glow, tired sigh, violet flames, " + MOON),
   "onedari_boss":("exec", "he bends forward locked in the padded velvet-lined pillory facing the empty seats, the horned officer stands beside him, one gloved palm pressed on his lower belly with a faint pink glow, her other hand behind him with fingers in his anus, fingering, " + MOON + " glowing, cum dripping"),
 },
 "lose_desc": "keeps him asleep in the dream castle forever, cherished as the queen's sustenance, twelve black moons full on his wrist.",
 "onanie": {
   "master": ("dark", "sitting behind a pillar with a long white cloth wound around his body like coils, a wet fingertip stroking his own nipple, " + MOON + ", penis untouched"),
   "e1": ("heaven", "kneeling behind a cloud, his face pressed into the sleeve of his own shirt, one hand rubbing his own nipple, a finger in his own anus, penis untouched"),
   "e2": ("china", "lying on his side, squeezing a pillow between his own thighs, a fingertip rubbing his own nipple, penis untouched"),
   "e3": ("bedding", "lying half asleep hugging a pillow, a fingertip slowly stroking his own nipple, penis untouched"),
   "boss": ("dark", "lying face down behind a pillar, holding a pillow over his own neck and wrist, a wet finger in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "a large black moon floating under a high ceiling, two thin crescents of pale violet light just filled in on its rim, cool glow, close-up"),
   "2": (None, "throne", "a small silver handbell on a black velvet cushion beside the arm of a throne, faint ripples of sound in the air, bell without text"),
   "3": (None, "china", "a bronze incense burner with pale violet smoke of herbs curling upward, dried herbs beside it, hazy sweet air"),
   "4": ("e2", "pharmacy", "holding up a small open jar of glossy ointment without text, a dab of ointment on her fingertip, mocking smile"),
   "5": ("m", "throne", "sitting on the black throne with one hand raised toward the black moon floating under the ceiling, her long tail curled at her feet, haughty laugh"),
 },
}
