# N145 孤独の地の蜘蛛たち（Spiders）画像データ。登場人物は全員20歳以上。5人とも女性（下半身が蜘蛛の魔物。ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。怖い・グロテスクにしない（脚の先は丸い・噛まない・食べない）。
# あやし土蜘蛛・アラクネ：原作は青い肌 → pale lavender skin／pale violet-grey skin に置き換え（青・水色は主人公と紛れるため）。
# 髪色を被らせない：ナクア＝黒／ロード＝銀（silver）／土蜘蛛＝原作は銀髪 → white hair（白）／アラクネ＝濃い紫の短髪／巫女アラクネ＝原作は紫 → light violet（薄い菫色）の長髪。
# 挿入はナクアの糸の紐（糸を撚った細い紐）と指だけ → pen なし。ロード・土蜘蛛・アラクネ・巫女アラクネは後ろに触れない。
# 絵は必ず「その責め手1人＋主人公」。主人公の体には白い糸が巻かれている。繭は空（中に人を描かない）。
THREAD = "white silk threads wound around his wrists and chest"
CORD = "a thin soft white cord of twisted silk thread in his anus"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
SPIDER_NEG = SOFT_NEG + ", human legs on the spider woman, hairy spider legs, sharp claws, stinger, fangs, biting, scary, horror, insect face"
TALISMAN = "blank white paper talismans without text stuck on his wrists and the center of his chest"
DATA = {
 "code": "Spiders",
 "world": "misty wasteland of spider women, countless white silk threads stretched everywhere, giant white spider webs glittering with dew, soft pale light through the mist, detailed background",
 "bg": "center of a giant white spider web stretched across a deep misty valley, bridges of white silk thread, white silk cocoons hanging, dew drops glittering on the threads, soft pale light, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "アトラク＝ナクア",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, pale skin, black hair, very long straight hair, red eyes, a row of red gem-like extra eyes on her forehead, arachne, spider lower body, glossy black giant spider lower body with eight smooth rounded legs, black sleeveless gown on her upper body, white silk thread ornaments, soft voluptuous feminine body, huge breasts, narrow waist",
         "name": "the black-haired spider goddess with red forehead eyes",
         "pose": "holding a single white silk thread between the fingers of both hands, head slightly tilted, quiet faint smile, looking down at viewer with red eyes",
         "height_note": "she is much taller than him",
         "neg": SPIDER_NEG},
   "e1": {"type": "woman", "jp": "あやし土蜘蛛",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, colored skin, pale lavender skin, white hair, medium hair, two short horns, golden eyes, arachne, spider lower body, giant red spider lower body with eight smooth rounded red legs, white onmyoji robe with wide sleeves on her upper body, blank paper talismans, soft voluptuous feminine body, huge breasts, narrow waist",
          "name": "the horned spider onmyoji with red spider legs",
          "pose": "holding a blank paper talisman without text between two fingers, the other hand tucked in her wide sleeve, calm polite smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SPIDER_NEG + ", text on talisman, letters"},
   "e2": {"type": "woman", "jp": "アラクネ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, colored skin, pale violet-grey skin, dark purple hair, short hair, yellow eyes, arachne, spider lower body, black spider lower body with eight smooth rounded legs, fur-trimmed top on her upper body, fur ornaments on her shoulders and waist, soft curvy feminine body, large breasts, narrow waist",
          "name": "the short-haired forest spider woman in fur ornaments",
          "pose": "arms crossed under her breasts, chin raised, a strand of sticky white thread dangling from one fingertip, haughty smirk, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": SPIDER_NEG},
   "e3": {"type": "woman", "jp": "巫女アラクネ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, tall, fair skin, light violet hair, very long hair, amber eyes, arachne, spider lower body, black spider lower body with eight smooth rounded legs, red kimono top with long sleeves, red skirt, shrine maiden, a cluster of golden bells in her hand, soft curvy feminine body, large breasts, narrow waist",
          "name": "the long-haired spider shrine maiden in a red kimono",
          "pose": "dancing with one long sleeve raised, ringing a cluster of golden bells, two front legs lifted in step, bright cheerful smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SPIDER_NEG},
   "boss": {"type": "woman", "jp": "アラクネロード",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, very tall, pale skin, silver hair, very long hair, red eyes, tiara woven of white thread, arachne, spider lower body, giant grey spider lower body with eight smooth rounded legs, regal grey and white gown with an open neckline on her upper body, soft voluptuous feminine body, huge breasts, narrow waist",
            "name": "the silver-haired spider ruler with a grey spider body",
            "pose": "one hand on her hip, the other hand holding out a net of white thread, chin raised, proud arrogant smile, looking down at viewer with red eyes",
            "height_note": "she is much taller than him",
            "neg": SPIDER_NEG},
 },
 "places": {
   "mist":    "foggy wasteland, cold mist, withered grass, white threads glinting here and there",
   "gate":    "entrance gate made of stretched white silk threads between rocks, a shadowed rock nook, mist",
   "shrine":  "red torii gate and a wooden shrine decorated with white threads, hanging bells, stone steps, tatami inside the shrine",
   "forest":  "forest with countless white threads stretched between the trees, dew drops shining on the threads",
   "anest":   "large white spider nest high in a tree, fur decorations, a soft bed of thread under the nest",
   "cave":    "damp rock cave, a soft bed of white thread, dripping water",
   "tshrine": "cave shrine with blank paper talismans without text pasted on the rock walls, shadows of red spider legs, a thread bed in the back",
   "fuda":    "room with walls covered in blank paper talismans without text, candles, floor cushions, ink stone",
   "edge":    "edge of a deep misty valley, a bridge of white thread, updraft, a bed of white thread on the cliff",
   "bridge":  "swaying bridge of white silk thread over a deep misty valley, sticky threads underfoot",
   "throne":  "throne room with a giant grey web throne, ornaments of woven white thread, a hanging net of white thread beside the throne",
   "cocoon":  "chamber with many empty white silk cocoons hanging from the ceiling, faint white glow",
   "rim":     "outer rim of a gigantic spider web, trembling threads, the web center visible far away through the mist",
   "bottom":  "bottom of the valley filled with still mist, white threads hanging down from above, quiet",
   "center":  "center of a gigantic white spider web over the valley, a white silk cocoon, dew on the threads, soft pale light",
 },
 "atk": {
   "m1": ("center", "he stands frozen still on the web with his arms at his sides, the spider goddess leans down close to his face gazing into him with glowing red eyes, one hand cupping his cheek, whispering, " + THREAD + ", his body leaning toward her, trembling"),
   "m2": ("rim", "he lies on his back stuck to a sticky white web with his arms and legs spread, the spider goddess looms over him, the rounded tips of her eight black legs stroking his neck, sides and inner thighs all at once, her fingers pinching his nipple, " + CORD + ", pre-cum"),
   "m3": ("center", "he lies back on the web, the spider goddess holds his face in one hand and kisses him deeply, tongues, saliva trail, two fingers of her other hand in his anus, fingering, " + THREAD + ", his toes curling"),
   "e1": ("fuda", "he sits frozen on a floor cushion, " + TALISMAN + ", the spider onmyoji kneels low in front of him, the fingers of both her hands stroking his nipple and his penis in an alternating weaving motion, calm smile, candle light"),
   "e2": ("anest", "he hangs upright under the tree nest with his wrists and ankles bound by sticky white thread, the forest spider woman presses her breasts around his face, breast smother, her hand winding more thread around his waist, haughty smirk"),
   "e3": ("shrine", "he sits on the stone steps staring up unable to look away, the spider shrine maiden dances right in front of him ringing golden bells, long red sleeve swirling, the rounded tips of her legs stroking his chest and thighs, " + THREAD + ", cheerful smile"),
   "boss": ("throne", "he hangs in the air with his arms and legs spread wide in a net of white thread, the spider ruler presses her breasts around his face, breast smother, the rounded tips of her grey legs stroking his sides, nipples and thighs, proud smile"),
 },
 "atk_desc": {
   "m1": "the spider goddess stills his whole body with her red gaze and a quiet whisper.",
   "m2": "the spider goddess sticks him to her web and strokes him with all eight legs while a soft thread cord teases inside.",
   "m3": "the spider goddess seals his lips with a kiss at the center of the web while her fingers loosen him.",
   "e1": "the spider onmyoji freezes him with paper talismans and strokes him with weaving fingers.",
   "e2": "the forest spider woman hangs him in sticky thread and smothers his face between her breasts.",
   "e3": "the spider shrine maiden charms him with a bell dance and strokes him with her legs.",
   "boss": "the spider ruler lifts him spread in her net and strokes him with eight legs, her breasts around his face.",
 },
 "lose": {
   # ナクア 技1（オールストップ＋★常世の粘網）
   "btl_m1":     ("center", "he lies frozen still on his back stuck to the sticky web, the spider goddess gazes down into his face with glowing red eyes, the rounded tips of her black legs stroking his whole body, " + CORD + ", " + THREAD + ", a fragment of white cocoon on his chest, cum on his stomach"),
   "onani_m1":   ("bottom", "sitting alone perfectly still in the mist, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, " + THREAD + ", penis untouched, the spider goddess watches far above hanging from a thread"),
   "inochi_m1":  ("bridge", "he stands frozen in the middle of the swaying thread bridge with one foot forward, the spider goddess behind him on the bridge, her hands sliding over his chest, pinching his nipple, whispering at his ear, " + THREAD + ", knees trembling, cum dripping"),
   "onedari_m1": ("center", "inside an open white cocoon he lies frozen still looking up, the spider goddess leans in pinching both his nipples, the rounded tips of two black legs stroking his thighs, quiet smile, glowing red eyes, " + THREAD + ", cum dripping"),
   # ナクア 技2（★常世の粘網）
   "btl_m2":     ("rim", "he lies on his back stuck to the sticky web with limbs spread, the spider goddess looms over him, eight rounded leg tips stroking his neck, sides, inner thighs and soles, her fingers rolling his nipple, " + CORD + ", a woven thread bracelet on his wrist, cum on his stomach untouched"),
   "onani_m2":   ("cocoon", "sitting alone behind an empty cocoon, loose white thread wound around his own chest and waist, one hand rubbing his own nipple, the other hand behind stroking his own anus, penis untouched, the spider goddess watches far away from the ceiling threads"),
   "inochi_m2":  ("edge", "he kneels at the cliff edge holding a single white thread in both hands, the spider goddess behind him winding a new loop of thread around his chest, her fingertip brushing his nipple, many loops of thread already around him, he trembles, cum dripping"),
   "onedari_m2": ("center", "he lies stuck to the web with limbs spread, the spider goddess over him, eight rounded leg tips stroking him all at once, one hand pinching his nipple, her other hand guiding " + CORD + ", glowing red eyes, cum on his stomach"),
   # ナクア 技3（巣の中心の口づけ＋★常世の粘網）
   "btl_m3":     ("center", "he lies on the web held in her arms, the spider goddess kisses him deeply, tongues, saliva trail, " + CORD + " held between her fingers, rounded leg tips stroking his sides, a tuft of soft black fur tied on his wrist thread, cum dripping"),
   "onani_m3":   ("edge", "lying alone on the thread bed at the cliff, sucking two of his own fingers as if kissing, the other hand behind pressing a finger into his own anus, " + THREAD + ", penis untouched, the spider goddess watches far away across the thread bridge"),
   "inochi_m3":  ("center", "he kneels on the web with his face tilted up, the spider goddess holds his chin and kisses him, saliva trail, her other hand winding one more loop of white thread around his waist, many loops around his body, his lips parted, cum dripping"),
   "onedari_m3": ("center", "inside half of a white cocoon he lies wrapped in soft thread, the spider goddess leans in kissing him deeply, tongues, " + CORD + " held in her fingers, a rounded leg tip stroking his chest, cum dripping"),
   # あやし土蜘蛛（★牡搾りの魔織）
   "btl_e1":     ("fuda", "he sits frozen on a floor cushion, " + TALISMAN + ", the spider onmyoji presses her breasts around his face, breast smother, her fingers stroking his penis in a weaving motion, handjob, candle light, cum on her fingers"),
   "onani_e1":   ("tshrine", "sitting alone in a corner of the cave shrine with blank scraps of paper stuck on his own wrists and chest, holding still, rubbing his own nipple with alternating fingertips, penis untouched, the spider onmyoji watches far away from the cave entrance"),
   "inochi_e1":  ("tshrine", "he stands before the talisman wall with one hand stopped in the air, a single blank paper talisman on the center of his chest, the spider onmyoji beside him tracing over the talisman with her fingertip, calm smile, " + THREAD + ", cum dripping"),
   "onedari_e1": ("fuda", "he lies back on floor cushions, three blank paper talismans without text on his wrists and chest, the spider onmyoji leans over him, her fingers slowly stroking his nipples in a weaving motion, her breasts close to his face, cum dripping untouched"),
   # アラクネ（★ネバネバ糸）
   "btl_e2":     ("anest", "he hangs upright under the tree nest wrapped round and round in sticky white thread, the forest spider woman kneels low before him, his penis between her breasts, paizuri, winding more thread around his chest with one hand, a fur ornament tied on his neck, cum on her breasts"),
   "onani_e2":   ("forest", "sitting alone behind a tree, his own wrists tied together with a plain string, rubbing his own nipple with his bound hands, penis untouched, the forest spider woman watches far above from a branch"),
   "inochi_e2":  ("forest", "at the edge of the forest he stands tangled in white threads between two trees, the forest spider woman in front of him winding one more loop around his waist, her other hand stroking his chest, smirk, he leans into the threads, cum dripping"),
   "onedari_e2": ("anest", "he lies in the middle of the big nest with his wrists bound by sticky white thread above his head, the forest spider woman presses her breasts around his face for a long time, breast smother, her hand slowly stroking his nipple, cum dripping"),
   # 巫女アラクネ（★魅了の踊り）
   "btl_e3":     ("shrine", "he kneels before the shrine staring up entranced, the spider shrine maiden dances close ringing golden bells, red sleeve swirling, the rounded tips of her eight legs stroking his neck, nipples and thighs all at once, a golden bell tied on his wrist thread, cum dripping untouched"),
   "onani_e3":   ("gate", "standing alone in the rock nook by the thread gate, swaying his hips as if dancing, both hands rubbing his own nipples, " + THREAD + ", penis untouched, the spider shrine maiden watches far away beyond the gate"),
   "inochi_e3":  ("shrine", "he stands at the red torii staring at her legs, the spider shrine maiden dances in front of the shrine ringing bells, laughing, one rounded leg tip stroking his chest, morning mist, " + THREAD + ", he trembles, cum dripping"),
   "onedari_e3": ("shrine", "inside the shrine he lies on the tatami looking up, the spider shrine maiden dances over him in a fast dance, bells ringing, eight rounded leg tips stroking his nipples and body, his penis wrapped in soft sticky white thread, cum soaking the thread"),
   # アラクネロード（★アラクネウェブ）
   "btl_boss":   ("throne", "he hangs in the air before the throne with arms and legs spread wide in a net of white thread, the spider ruler presses her breasts around his face, breast smother, rounded grey leg tips stroking his nipples and penis, a necklace of grey thread on his neck, cum dripping"),
   "onani_boss": ("cave", "sitting alone on the thread bed, one wrist hung above his head by a plain string looped on a rock, the other hand rubbing his own nipple, penis untouched, the spider ruler watches far away from the cave mouth"),
   "inochi_boss":("throne", "he stands before the throne raising both hands by himself, a net of white thread catching his wrists and lifting him, the spider ruler looks down at him from above, one rounded grey leg tip stroking his chest, proud smile, cum dripping"),
   "onedari_boss":("throne", "beside the throne he hangs by his wrists in a net of white thread, the spider ruler holds his head between her breasts for a long time, breast smother, eight rounded grey leg tips stroking his whole body, cum dripping"),
 },
 "lose_desc": "keeps him forever as the cherished catch at the center of the web, twelve loops of white thread wound around his body, wrapped in a warm white cocoon.",
 "onanie": {
   "master": ("bottom", "sitting perfectly still, loose white thread wound around his chest, one hand rubbing his own nipple, the other hand behind stroking his own anus, penis untouched"),
   "e1": ("tshrine", "sitting still with blank scraps of paper stuck on his wrists and chest, rubbing his own nipple with alternating fingertips, penis untouched"),
   "e2": ("forest", "sitting behind a tree, his own wrists tied with a plain string, rubbing his own nipple with his bound hands, penis untouched"),
   "e3": ("gate", "standing, swaying his hips as if dancing, both hands rubbing his own nipples, penis untouched"),
   "boss": ("cave", "sitting on a thread bed, one wrist hung above his head by a plain string, the other hand rubbing his own nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "mist", "a single long white silk thread drifting out of the mist and curling into two soft loops in the air, faint glow, dew drops, close-up"),
   "2": ("m", "center", "plucking one thread of the giant web with a fingertip, ripples of trembling running along the threads, quiet faint smile"),
   "3": (None, "fuda", "a single blank white paper talisman without text floating in the air above a candle, faint glow, ink stone beside it"),
   "4": (None, "gate", "a gate of white silk threads stretched between two rocks, the threads softly glowing, mist drifting through, no humans"),
   "5": (None, "cocoon", "one empty white silk cocoon hanging open with a warm faint glow inside, thin threads reaching out from it, no humans"),
 },
}
