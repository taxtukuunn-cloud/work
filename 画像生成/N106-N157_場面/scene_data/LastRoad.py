# N126 街道と古城（LastRoad）画像データ。登場人物は全員20歳以上。5人とも女性の上級淫魔（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（剣士・騎士も曲線のある体つき）。
# 挿入技なし：後ろに入れるのはヴァンパイアの指だけ（pen なし）。姫騎士・パステト・仙女・ウォーリアは後ろに触れない。
# ヴァンパイアの牙は肌を破らない（首筋には唇を当てるだけ。傷・流血なし）。
# 仙女：brief は黒髪だが、パステト（黒髪おかっぱ）と髪色が被るので dark purple hair（紫がかった黒）にした。
# 姫騎士：鎧とマントの青は服の色だけ（髪は金・瞳は緑。青い髪・青い瞳は使わない）。パステトの猫の耳は耳飾り（獣人ではない）。
# 主人公はポケットか手元にピンクに光る地図（文字なし）。
MAP = "a folded paper map glowing faint pink in his pocket, map without text"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
VAMP_NEG = SOFT_NEG + ", blood, bite wound, fangs piercing skin, scary"
DATA = {
 "code": "LastRoad",
 "world": "fantasy highway leading across grassland, forest and desert to an old gothic castle, dusk light, candlelight, detailed background",
 "bg": "wide grassland highway at dusk, a dirt road, a weathered wooden signpost with blank boards without text, spires of an old gothic castle on the horizon, a distant bell tower, warm orange sky, wind in the grass, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ヴァンパイア",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, silver hair, very long straight hair, red eyes, black and red gothic dress, black cape with a high collar, soft voluptuous feminine body, huge breasts, thick thighs",
         "name": "the silver-haired vampire in a black and red dress",
         "pose": "one hand holding a glass of red wine, the other hand raised with a beckoning finger, haughty confident smile, looking down at viewer with red eyes",
         "neg": VAMP_NEG},
   "e1": {"type": "woman", "jp": "パステト",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, dark-skinned female, brown skin, black hair, blunt bob cut, golden eyes, gold cat-ear shaped hair ornament, wide gold necklace, thin white egyptian linen dress, gold anklets, barefoot, soft curvy feminine body, large breasts, thick thighs",
          "name": "the bob-haired woman in a white linen dress and gold anklets",
          "pose": "sitting on a stone step with one bare foot raised toward the viewer, gold anklet shining, hands on her hips, smug confident smile, looking at viewer",
          "neg": SOFT_NEG + ", animal ears, cat tail"},
   "e2": {"type": "woman", "jp": "仙女",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark purple hair, long hair tied up in an elegant bun, hair stick, violet eyes, pale pink kimono, thin translucent white celestial shawl floating around her shoulders, soft voluptuous feminine body, huge breasts, thick thighs",
          "name": "the hermit woman in a pale pink kimono and a floating shawl",
          "pose": "holding a small smoking incense burner in both hands, pale pink smoke drifting, relaxed sleepy smile, head tilted, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ウォーリア",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, red hair, short hair, brown eyes, light brown leather armor open at the chest, cleavage, leather shorts, leather boots, soft curvy feminine body, huge breasts, thick thighs",
          "name": "the red-haired swordswoman in light leather armor",
          "pose": "one hand on her hip, the other hand pointing at the viewer as a challenge, a sheathed greatsword lying in the grass beside her, bright cheerful laugh, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "姫騎士",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, very long wavy hair, green eyes, white plate armor with blue trim open at the chest, deep cleavage, blue cape, white armored skirt, sheathed sword at her hip, soft voluptuous feminine body, huge breasts, thick thighs",
            "name": "the blonde knight in white armor",
            "pose": "one hand on the clasp at the chest of her armor, the other hand held out gently, sheathed sword at her hip, kind big-sisterly smile, looking at viewer",
            "neg": SOFT_NEG + ", drawn sword"},
 },
 "places": {
   "gate":       "entrance of the highway in the cool morning, a wooden signpost with blank boards without text, a map seller's stall, dry earth road, grassland far away",
   "plain":      "wide grassland under a clear sky, tall grass swaying in the wind, soft earth, an old castle bell tower far away",
   "rocks":      "rocky spot in the grassland, large sun-warmed boulders, a sunny sheltered hollow, short grass",
   "forest":     "entrance of a deep dim forest, sweet-scented trees, drifting mist, wet fallen leaves",
   "spring":     "clear forest spring, mossy bank, dripping water, soft bed of moss, mist",
   "hermit":     "inside a bamboo hermitage, tatami floor, a smoking incense burner, tea set, pale pink smoke, paper window",
   "desert":     "desert of warm sand dunes at night, countless near stars, cool air",
   "pyramid":    "foot of a giant pyramid, huge sun-baked stone steps, blowing sand, bright sunlight",
   "tomb":       "pyramid inner chamber, gold decorations, burning torches, golden bottles of perfumed oil, a stone bed covered with cloth",
   "mountain":   "rocky narrow mountain road, a wooden lookout hut with a simple bed and an open window, cold wind, castle banners far away",
   "castlegate": "castle entrance, lowered drawbridge, huge stone gate, cold stone steps, quiet with no guards",
   "garden":     "castle courtyard rose garden, a stone fountain with sparkling water, red roses, a white tea table",
   "hall":       "great hall of an old castle, dusty chandelier, many candles, red carpet, a long sofa, fireplace embers",
   "cellar":     "underground wine cellar, large wooden barrels, stone floor, a single candle, cool dim air",
   "bedroom":    "windowless castle bedroom, bed with a black canopy and red silk sheets, candles, a single chair, a wine shelf",
   "belfry":     "bell tower of the old castle at dusk, a large bronze bell under stone arches, grassland and a long road far below",
 },
 "atk": {
   "m1": ("hall", "he kneels on the red carpet, the vampire stands over him lifting his chin with one cold fingertip, staring down into his face with glowing red eyes, her other hand pinching his nipple through his open shirt, haughty smile, " + MAP + ", knees trembling"),
   "m2": ("hall", "from side, on the long sofa, he sits sideways on the vampire's lap, his penis squeezed between her thick thighs, thigh sex, the vampire holds a glass of red wine and tilts his chin up with her other hand, glowing red eyes, wine dripping from his lips"),
   "m3": ("bedroom", "he lies on his back on the red silk sheets, the vampire straddles his hips, his penis pressed between her thighs, the vampire leans down kissing him deeply, tongues, saliva trail, one of her hands reaching under him, two fingers in his anus, fingering, candlelight"),
   "e1": ("tomb", "he sits on the cloth-covered stone bed leaning back on his hands, the bob-haired woman sits facing him with her legs stretched out, both her brown soles clasping his penis, footjob, toes teasing the tip, gold anklets shining, smug smile, torchlight"),
   "e2": ("hermit", "he lies limp on the tatami wrapped in pale pink incense smoke, the hermit woman kneels beside him, one fingertip slowly circling his nipple, her other hand slowly stroking his penis from base to tip, handjob, a smoking incense burner beside them, sleepy smile"),
   "e3": ("plain", "he lies on his back in the grass, the swordswoman straddles his waist pinning his wrists with one hand, her leather armor open, her huge breasts swaying above his face, flicking his nipple with her other hand, cheerful laugh, a sheathed greatsword lying in the grass, " + MAP),
   "boss": ("castlegate", "he sits on the stone steps of the gate leaning back, the blonde knight kneels between his legs, the chest clasp of her armor undone, his penis between her huge breasts, paizuri, the knight looks up at him with a gentle smile, sheathed sword at her hip"),
 },
 "atk_desc": {
   "m1": "the vampire makes him kneel with her charming red gaze.",
   "m2": "the vampire feeds him red wine and squeezes him between her thighs on her lap.",
   "m3": "the vampire straddles him, kissing him deeply while pressing inside with her fingers.",
   "e1": "the pyramid mistress rubs him between her soles while her gold anklets ring.",
   "e2": "the hermit woman slows time with incense and strokes him with endlessly slow hands.",
   "e3": "the swordswoman pins him in the grass and sways her breasts above his face.",
   "boss": "the knight refuses to fight and serves him between her breasts to end his journey.",
 },
 "lose": {
   # ヴァンパイア 技1（★魅了の魔眼）
   "btl_m1":     ("hall", "he kneels on the red carpet with his hips raised, the vampire crouches beside him holding his chin, staring into his face with glowing red eyes, two oiled fingers of her other hand in his anus, fingering, two faint red kiss marks on his neck, cum dripping untouched, " + MAP),
   "onani_m1":   ("garden", "kneeling alone at the edge of the stone fountain, staring at his own reflection in the water, one hand tracing his own neck, the other hand reaching behind to stroke his own anus, penis untouched, the vampire watches far away among the roses"),
   "inochi_m1":  ("bedroom", "he sits on the single chair with his shirt open, the vampire leans over him from the front holding his chin, glowing red eyes close to his, her other hand between his legs with a finger in his anus, fingering, candles, cum dripping untouched, " + MAP),
   "onedari_m1": ("bedroom", "he sits on the chair with his head tilted to the left, the vampire stands beside him with her lips resting softly on the right side of his neck without biting, looking into his face with red eyes, two fingers of her hand in his anus, fingering, a candle burned low, cum dripping"),
   # ヴァンパイア 技2（夜の宴）
   "btl_m2":     ("hall", "from side, on the long sofa, he sits on the vampire's lap, his penis squeezed tight between her thick thighs, thigh sex, the vampire tilts his chin up and stares with glowing red eyes, an empty wine glass in his hand, wine on his lips, cum on her thighs"),
   "onani_m2":   ("cellar", "sitting alone on the stone floor against a barrel, squeezing a pillow between his own thighs, one hand rubbing his own nipple, a cup of red wine beside him, penis untouched, the vampire watches far away from the cellar stairs"),
   "inochi_m2":  ("hall", "he sits slumped on the vampire's lap on the long sofa, the vampire holds his face and feeds him red wine mouth to mouth, kiss, wine dripping down his chin, his penis between her thighs, thigh sex, empty glasses on the table, a wine barrel beside them"),
   "onedari_m2": ("bedroom", "from side, on the red silk bed in front of the wine shelf, he lies on his side held from behind by the vampire, his penis squeezed between her thick thighs, thigh sex, the vampire kisses his neck softly without biting, four empty wine glasses, cum on the sheets"),
   # ヴァンパイア 技3（血の契り）
   "btl_m3":     ("bedroom", "he lies on his back on the red silk sheets, the vampire straddles his hips, his penis pressed between her thighs, kissing him deeply, tongues, saliva trail, her hand reaching under him with two fingers in his anus, fingering, a red ring on his finger, cum on his stomach"),
   "onani_m3":   ("hall", "kneeling alone astride a pillow on the long sofa, rocking his hips against it, sucking two of his own fingers as if kissing, penis untouched, the vampire watches far away from the doorway of the hall"),
   "inochi_m3":  ("bedroom", "he lies on his back on the left side of the bed, the vampire straddles him holding his hand up, sliding a red ring onto his finger, glowing red eyes looking down at him, his penis pressed between her thighs, cum on his stomach, candles"),
   "onedari_m3": ("bedroom", "morning candlelight, he lies on his back on the red silk sheets with arms open, the vampire lies over him, lips just parted from a kiss, saliva trail, staring into his face with red eyes, her fingers in his anus, fingering, cum on his stomach"),
   # パステト（★ボクの足）
   "btl_e1":     ("tomb", "he lies on his back on the cloth-covered stone bed, the bob-haired woman sits at his feet, one brown sole rubbing his penis against his stomach, footjob, her other foot stroking his nipple with her toes, gold anklets ringing, a gold anklet on his own ankle, cum on his stomach"),
   "onani_e1":   ("pyramid", "sitting alone in the shadow of the huge stone steps with one knee pulled up, stroking his own lower belly with the sole of his own foot, penis untouched, the bob-haired woman watches far away from the top of the steps"),
   "inochi_e1":  ("desert", "he lies on his back on the cool night sand under the stars, the bob-haired woman sits beside him resting one warm brown sole on his chest, toes at his nipple, gold anklet shining, smug smile, " + MAP + ", cum dripping untouched"),
   "onedari_e1": ("tomb", "he sits on the stone bed glistening with warm oil, the bob-haired woman sits facing him, both her oiled soles clasping his penis, footjob, gold anklets ringing, golden oil bottles beside them, the woman counts on her fingers, cum on her feet"),
   # 仙女（★仙術の香）
   "btl_e2":     ("hermit", "he lies limp on the tatami in thick pale pink incense smoke, the hermit woman kneels beside him, one fingertip slowly stroking his nipple, her other hand slowly stroking his penis upward, handjob, a small cloth pouch on a cord around his neck, cum dripping slowly"),
   "onani_e2":   ("spring", "sitting alone on the mossy bank of the spring, breathing in a thin trail of incense smoke, very slowly circling his own nipple with one fingertip, penis untouched, the hermit woman watches far away through the mist"),
   "inochi_e2":  ("forest", "he stands in the misty forest wrapped in the thin white shawl, his feet floating just off the ground, the hermit woman holds him from behind against her breasts, one fingertip stroking his nipple, incense smoke trailing, " + MAP + ", cum dripping untouched"),
   "onedari_e2": ("hermit", "he lies on the tatami on a bed of thin white shawls, the hermit woman kneels over him holding one fingertip on his nipple in a single endless stroke, a cup of cold tea beside them, pale pink smoke, relaxed smile, cum on his stomach"),
   # ウォーリア（★組み打ちの誘惑）
   "btl_e3":     ("plain", "he lies on his back in the grass, the swordswoman straddles his hips grinding against him, her leather armor open, huge breasts swaying above his face, flicking both his nipples, laughing, a red hair cord tied around his wrist, cum on his stomach"),
   "onani_e3":   ("rocks", "lying alone on his back in the grass beside a sun-warmed boulder, shirt open, flicking both his own nipples with his fingertips, penis untouched, the swordswoman watches far away from the top of a boulder"),
   "inochi_e3":  ("plain", "he lies down in the grass by himself with arms spread, the swordswoman kneels astride his waist leaning forward, huge breasts swaying close above his face, flicking his nipple with one finger, bright laugh, a sheathed greatsword in the grass, cum dripping untouched"),
   "onedari_e3": ("rocks", "he lies on his back on a flat sunny boulder, the swordswoman lies on her side next to him propped on one elbow, her huge breasts swaying beside his face, flicking his nipple, her thigh rubbing his hips, cheerful grin, cum on his stomach"),
   # 姫騎士（★姫騎士の奉仕）
   "btl_boss":   ("castlegate", "he sits on the stone steps of the gate leaning back, the blonde knight kneels between his legs with the chest clasp of her armor undone, his penis between her huge breasts, paizuri, a strip of blue cape cloth tied around his wrist, cum on her breasts, gentle smile"),
   "onani_boss": ("mountain", "sitting alone in the shadow of the wooden lookout hut, shirt open, pressing his own chest together with both forearms and rubbing his own nipples, penis untouched, the blonde knight watches far away on the mountain road"),
   "inochi_boss":("garden", "he lies with his head on the blonde knight's lap beside the white tea table, the knight strokes his hair and leans down, the chest clasp of her armor undone, the tip of her breast brushing his nipple, tea cups, red roses, cum dripping untouched"),
   "onedari_boss":("castlegate", "he stands with his back against the stone gate, the blonde knight kneels in front of him, his penis between her huge breasts, paizuri, the knight counts softly looking up at him, her clasp undone, sheathed sword at her hip, cum on her breasts"),
 },
 "lose_desc": "ends his journey for good, his map painted entirely pink as the bell of the old castle tolls twelve times.",
 "onanie": {
   "master": ("garden", "kneeling at the edge of the fountain, staring at his own reflection in the water, one hand tracing his own neck, the other hand stroking his own anus, penis untouched"),
   "e1": ("pyramid", "sitting with one knee pulled up, stroking his own lower belly with the sole of his own foot, penis untouched"),
   "e2": ("spring", "sitting on the moss in thin incense smoke, very slowly circling his own nipple with one fingertip, penis untouched"),
   "e3": ("rocks", "lying on his back in the grass with his shirt open, flicking both his own nipples, penis untouched"),
   "boss": ("mountain", "sitting with his shirt open, pressing his own chest together with both forearms and rubbing his own nipples, penis untouched"),
 },
 "magic": {
   "1": (None, "gate", "an old parchment road map spread on a wooden stall, two sections of the drawn road painted glowing pink, a brush with pink paint beside it, map without text, close-up"),
   "2": (None, "gate", "a weathered wooden signpost at a fork in the road, blank arrow boards without text, one arrow turning by itself, faint pink sparkles, dusk"),
   "3": ("boss", "castlegate", "undoing the chest clasp of her armor with one hand, deep cleavage, leaning forward, gentle inviting smile, sheathed sword at her hip"),
   "4": (None, "tomb", "a small golden bottle of warm perfumed oil on a cloth-covered stone bed, glossy golden oil dripping from its lip, torchlight, bottle without text"),
   "5": (None, "belfry", "a large old bronze bell swinging by itself under stone arches, soft sound ripples in the air, faint pink glow, dusk sky"),
 },
}
