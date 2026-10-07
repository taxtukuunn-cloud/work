# N155 エルフの里とくのいち軍団（ElfNinja）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（侍も曲線のある体つき）。
# 髪色を被らせない：エルフ姫＝黒のロング／サムライエルフ＝原作は黒のポニーテール → dark brown（焦げ茶）のポニーテール／スキュラ＝赤／アラクネ＝紫／サキュバス＝白。
# 原作に青・水色の髪や瞳のキャラはいない。瞳は violet／green／golden／yellow／pink に振り分け（青系は使わない）。
# 挿入は指と、くのいちスキュラの細い触手の先だけ → pen なし。サムライエルフ・アラクネ・サキュバスは後ろに触れない。
# 契りの口づけ（m3）は姫が上に跨って迎える形（主人公は仰向けで動かない）。刀は抜かない（腰・刀掛けの鞘に収まったまま）。
# 影縫いは「影を糸で地面に縫う」術（体には刺さない）。蜘蛛の糸の網はやわらかい。札は無地（文字なし）。主人公の左手の薬指に赤い組紐。
CORD = "a thin red braided silk cord wound around his left ring finger"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
SWORD_NEG = "drawn sword, unsheathed blade, sword pointed at him, blood, wound"
TENT = "warm glossy red tentacles"
WEB = "soft white spider silk threads holding his wrists and ankles to the garden trees"
SHADOW = "his shadow on the ground stitched down with a single glowing thread"
DATA = {
 "code": "ElfNinja",
 "world": "elf village mansion deep in a great forest at night, japanese-style cypress wood architecture, tatami and shoji screens, incense smoke, red braided cord ornaments with small bells, moonlight, detailed background",
 "bg": "inner chamber of a japanese-style elf mansion at night, tatami floor, shoji screens glowing with moonlight, bamboo blinds, a red kimono hanging on a wooden kimono rack, incense smoke rising from a burner, red braided cord ornaments and small golden bells, silk floor cushions, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "エルフ姫",
         "tags": "adult woman, mature female, mature face, elegant adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, elf, long pointy ears, pale skin, black hair, very long straight hair, hime cut, violet eyes, gold hairpin, red kimono with long sleeves, gold obi, sheathed katana at her waist, soft voluptuous feminine body, huge breasts, narrow waist, wide hips",
         "name": "the black-haired elf princess in a red kimono",
         "pose": "one hand resting on the hilt of her sheathed katana, the other hand raised with her long sleeve swaying, graceful gentle smile, looking at viewer",
         "neg": SOFT_NEG + ", " + SWORD_NEG},
   "e1": {"type": "woman", "jp": "くのいちスキュラ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, pale skin, red hair, long wavy hair, golden eyes, scylla, monster girl, many smooth red tentacles from the waist down instead of legs, white high-leg leotard on her upper body, ninja arm guards, soft voluptuous feminine body, huge breasts, narrow waist",
          "name": "the red-haired tentacle kunoichi in a white leotard",
          "pose": "rising from a pond with her red tentacles spread on the water, one finger at her lips, alluring relaxed smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", human legs on the tentacle woman, suckers with teeth, scary, slimy horror"},
   "e2": {"type": "woman", "jp": "くのいちアラクネ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, colored skin, grey skin, purple hair, short bob, yellow eyes, arachne, spider lower body, glossy dark purple giant spider lower body with eight smooth rounded legs, purple ninja outfit on her upper body, fishnet sleeves, white silk thread from her fingertips, soft curvy feminine body, large breasts, narrow waist",
          "name": "the purple-haired grey-skinned spider kunoichi",
          "pose": "stretching a single white silk thread between the fingers of both hands, cool composed faint smile, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", human legs on the spider woman, hairy spider legs, sharp claws, fangs, biting, scary, horror, insect face"},
   "e3": {"type": "woman", "jp": "くのいちサキュバス",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, white hair, medium hair, two black horns, pink eyes, black bat wings, thin black tail, short red kimono with a loose neckline, black thighhighs, soft curvy feminine body, large breasts, narrow waist",
          "name": "the white-haired horned kunoichi with bat wings",
          "pose": "leaning against a vermilion gate post with arms crossed under her breasts, one sleeve swaying, frank cheerful grin, looking at viewer",
          "neg": SOFT_NEG + ", scary, fangs"},
   "boss": {"type": "woman", "jp": "サムライエルフ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, elf, long pointy ears, pale skin, dark brown hair, long high ponytail, green eyes, white sarashi chest wrap, bare shoulders, red hakama, sheathed katana at her hip, barefoot, soft voluptuous feminine body, huge breasts, narrow waist, wide hips",
            "name": "the brown-ponytail elf samurai in red hakama",
            "pose": "standing straight with one hand resting on her sheathed katana, serious earnest face with a faint blush, looking at viewer",
            "neg": SOFT_NEG + ", " + SWORD_NEG},
 },
 "places": {
   "entrance": "entrance of an elf village, giant trees, sunbeams through leaves, forest path",
   "path":     "mossy stone-paved village path, stone lanterns, a sitting stone in the shade of a tree, mansion roofs far away",
   "gate":     "vermilion mansion main gate, lookout platform above the gate, a small side door, paper lanterns",
   "guard":    "ninja guard room, tatami floor, wooden pillar, incense burner, sliding closet with futon",
   "webgarden":"night garden with white spider silk threads stretched between garden trees glittering in the moonlight, night dew, a hammock-like bed woven of silk under a tree",
   "pond":     "mansion pond with koi, arched stone bridge, stepping stones across the water, moon reflected on the water",
   "azumaya":  "wooden gazebo at the pond side, long wooden bench, wet planks, water ripples",
   "dojo":     "wooden-floored dojo, polished planks, a few tatami mats in the corner, wooden swords resting on a wall rack",
   "samurai":  "plain samurai room, a sword rack, folded white sarashi cloth, simple futon and pillow, cypress wood walls",
   "corridor": "long mansion corridor at night, shoji screens, moonlight on the wooden floor",
   "tearoom":  "small tea room, hanging scroll without text, floor cushions, iron kettle steaming, tea bowl and whisk",
   "himegarden":"princess's garden at night, cherry tree in bloom, stone lantern, small bells tied to branches, falling petals",
   "front":    "in front of the inner chamber, painted sliding doors, red braided cord ornaments, incense smoke leaking through the doors",
   "okunoma":  "inner chamber, a red kimono on a kimono rack, incense burner, bamboo blinds, silk cushions on tatami",
   "shinjo":   "bridal bedchamber next to the inner chamber, red futon, a small golden bell by the pillow, moon behind shoji screens",
 },
 "atk": {
   "m1": ("okunoma", "he kneels limp on a silk cushion, a blank white paper talisman without text stuck on his bare chest, soft pale sparks glowing over his skin, the princess kneels close in front holding his cheek, gazing into his face, chanting softly, he nods weakly, " + CORD),
   "m2": ("okunoma", "he lies on his back on the tatami with his shirt open, the princess kneels beside him, her long red sleeve brushing his chest, one white finger circling his nipple, two oiled fingers of her other hand in his anus, fingering, gentle knowing smile, " + CORD),
   "m3": ("shinjo", "from side, he lies still on his back on the red futon with arms at his sides, the princess straddles his hips with her kimono hem parted and her obi still tied, cowgirl position, leaning down kissing him deeply, tongues, saliva trail, one finger on his nipple, " + CORD),
   "e1": ("azumaya", "he is held up above the bench, " + TENT + " coiled around his wrists, ankles and waist, thin tentacle tips circling his nipples, a thin smooth tentacle tip in his anus, anal, the tentacle kunoichi holds his face to her chest, alluring smile, his own penis separate, " + CORD),
   "e2": ("webgarden", "he stands spread between two garden trees, " + SHADOW + ", " + WEB + ", the spider kunoichi in front of him plucking a single silk thread stretched across his nipple with one finger, cool smile, moonlight, " + CORD),
   "e3": ("guard", "he lies pinned on his back on the tatami, the horned kunoichi lies over him holding him down with one arm, her kimono neckline open, her fingers flicking his nipple with motion blur, her other hand stroking his penis, handjob, cheerful grin, " + CORD),
   "boss": ("dojo", "he lies on his back on the wooden floor, the elf samurai holds him down from the side in a pinning hold, her unwrapped breasts pressed over his face, breast smother with room to breathe, her hand stroking his nipple, serious face, " + CORD),
 },
 "atk_desc": {
   "m1": "the princess numbs him sweetly with a talisman chant and asks until he nods.",
   "m2": "the princess learns every part of his body with her white fingers and presses deep inside.",
   "m3": "the princess seals the vow with a kiss while taking him in on the red futon.",
   "e1": "the tentacle kunoichi wraps his whole body and strokes inside with a thin tentacle tip.",
   "e2": "the spider kunoichi stitches his shadow, webs his limbs and plucks a thread across his nipple.",
   "e3": "the horned kunoichi corners him with hands too fast to see.",
   "boss": "the elf samurai pins him down and holds his face in her breasts.",
 },
 "lose": {
   # エルフ姫 技1（陰陽・雷痺唱）
   "btl_m1":     ("okunoma", "he lies limp on his back on the tatami, a blank white paper talisman without text on his bare chest, soft pale sparks over his skin, the princess leans over him gazing into his face, one white finger on his nipple, two oiled fingers in his anus, fingering, he nods, cum dripping untouched, " + CORD),
   "onani_m1":   ("himegarden", "sitting alone in the shadow of a stone lantern, holding a blank sheet of paper against his own chest, rubbing his own nipple under it, penis untouched, the princess watches far away from behind the cherry tree, " + CORD + " glowing red"),
   "inochi_m1":  ("path", "he stands frozen on the mossy stone path with weak knees, a blank white paper talisman without text on his chest, soft pale sparks, the princess stands close holding his hand and gazing into his face, asking gently, her sleeve around his shoulder, " + CORD),
   "onedari_m1": ("shinjo", "he lies on the red futon looking up, a blank white paper talisman without text on his bare chest, soft pale sparks over his skin, the princess sits beside him holding his face in both hands, gazing close, whispering a question, he nods, cum dripping untouched, " + CORD),
   # エルフ姫 技2（★姫の手ほどき）
   "btl_m2":     ("okunoma", "he lies on his back on the tatami with knees raised, the princess kneels between his legs, her red sleeve draped over his stomach, one white finger stroking his nipple, two oiled fingers pressing deep in his anus, fingering, a gold hairpin laid beside his head, cum on his stomach untouched, " + CORD),
   "onani_m2":   ("tearoom", "kneeling alone on a floor cushion, stroking his own chest with a strip of red cloth, one finger of the other hand reaching behind to stroke his own anus, penis untouched, a red kimono sleeve of the princess visible far away at the small door, " + CORD + " glowing red"),
   "inochi_m2":  ("tearoom", "he sits on a floor cushion holding out an empty tea bowl with both hands, the princess sits close behind him, her arms around him, one white finger stroking his nipple through his open collar, the kettle steaming, gentle smile, " + CORD),
   "onedari_m2": ("okunoma", "behind the bamboo blinds, he lies on his side on silk cushions, the princess lies behind him, one white finger rolling his nipple, two oiled fingers pressing in his anus, fingering, counting softly at his ear, cum dripping untouched, " + CORD),
   # エルフ姫 技3（契りの口づけ）
   "btl_m3":     ("shinjo", "from side, he lies still on his back on the red futon, the princess straddles his hips with her kimono hem parted and her obi tied, cowgirl position, leaning down kissing him deeply, tongues, saliva trail, her finger on his nipple, a red braided cord ring on his finger, cum overflowing"),
   "onani_m3":   ("corridor", "kneeling alone on the moonlit wooden floor, straddling a pillow, sucking two of his own fingers as if kissing, penis untouched, the silhouette of the princess in a kimono on the shoji screen far away, " + CORD + " glowing red"),
   "inochi_m3":  ("front", "he stands with his back against the painted sliding door, the princess holds his face in both hands kissing him deeply, tongues, saliva trail, her red sleeves around his neck, the doors behind them open to a red futon, his knees giving way, " + CORD),
   "onedari_m3": ("shinjo", "from side, at dawn, he lies still on his back on the red futon, the princess sits on his hips unmoving, cowgirl position, taking him in deep, leaning down in a long kiss, her finger resting on his nipple, pale morning light through the shoji, cum overflowing, " + CORD),
   # くのいちスキュラ（★乱れ触手愛撫）
   "btl_e1":     ("azumaya", "from side, he is wrapped from ankles to chest in " + TENT + " on the long bench, thin tentacle tips sucking his nipples, a thin smooth tentacle tip in his anus, anal, the tentacle kunoichi holds his head to her chest, a small red tentacle charm around his neck, his own penis separate, cum dripping untouched, " + CORD),
   "onani_e1":   ("pond", "crouching alone in the shadow under the stone bridge, a wet rope wound around his own chest and waist, one finger reaching behind to stroke his own anus, penis untouched, the red hair of the tentacle kunoichi rising from the water far away, " + CORD + " glowing red"),
   "inochi_e1":  ("pond", "he stands waiting on a stepping stone in the middle of the pond, " + TENT + " rising from the water coiled around his ankles and thighs, the tentacle kunoichi rises behind him, a tentacle tip circling his nipple under his open shirt, moon on the water, " + CORD),
   "onedari_e1": ("azumaya", "from side, he lies on the long bench held by five " + TENT + " around his limbs and waist, two thin tips circling his nipples, one thin smooth tentacle tip deep in his anus, anal, the tentacle kunoichi leans over him smiling, his own penis separate, cum on his stomach, " + CORD),
   # くのいちアラクネ（★影縫いと粘網）
   "btl_e2":     ("webgarden", "he stands spread between two garden trees, " + SHADOW + ", " + WEB + ", the spider kunoichi plucks a silk thread stretched across both his nipples, her other finger tracing his inner thigh, a bracelet of white silk thread on his wrist, cum dripping untouched, " + CORD),
   "onani_e2":   ("guard", "sitting alone against the wooden pillar, one wrist tied to the pillar with a loose cord, the other hand tracing his own nipple, penis untouched, a single silk thread hanging from the ceiling, the spider kunoichi watches far above from the rafters, " + CORD + " glowing red"),
   "inochi_e2":  ("webgarden", "he stands still among the glittering threads with one hand reaching to touch a thread, " + SHADOW + ", the spider kunoichi behind him stepping on his shadow, her fingertip tracing his nipple from behind, a silk thread across his chest, " + CORD),
   "onedari_e2": ("webgarden", "he lies on his back on the bed woven of silk under a garden tree, soft silk threads holding his wrists and ankles, the spider kunoichi leans over him plucking a thread stretched across his nipples, calm approving smile, cum dripping untouched, " + CORD),
   # くのいちサキュバス（★男殺しの魔蜘蛛）
   "btl_e3":     ("guard", "he lies pinned on his back on the tatami of the gate guard room, the horned kunoichi over him, her kimono open, his penis squeezed between her breasts, paizuri, her fingers flicking both his nipples with motion blur, a red kimono sash around his wrist, cum on her breasts, " + CORD),
   "onani_e3":   ("path", "sitting alone in the shade of a roadside tree, flicking his own nipples quickly with the fingers of both hands, penis untouched, the horned kunoichi watches far away from the top of the gate with her wings folded, " + CORD + " glowing red"),
   "inochi_e3":  ("gate", "he stands with his back against the closed vermilion gate, staring hard, the horned kunoichi in front of him with one arm around his waist, her fingers flicking his nipple with motion blur, her other hand stroking his penis, handjob, laughing, his knees giving way, " + CORD),
   "onedari_e3": ("guard", "he lies on his back on the tatami, the horned kunoichi lies over him with her bat wings wrapped around them, her bare breasts pressing hard on his penis, paizuri, her fingers flicking his nipples with motion blur, proud grin, cum on her breasts, " + CORD),
   # サムライエルフ（★寝技・乳固め）
   "btl_boss":   ("dojo", "he lies on his back on the wooden floor, the elf samurai pins him from the side, her unwrapped breasts pressed over his face, breast smother with room to breathe, her hand stroking his penis, handjob, a strip of white sarashi cloth tied on his wrist, cum on his stomach, " + CORD),
   "onani_boss": ("samurai", "lying alone on the simple futon, pressing a pillow over his own face with one arm, the other hand stroking his own nipple, penis untouched, the elf samurai stands far away at the sword rack setting down her sheathed katana, " + CORD + " glowing red"),
   "inochi_boss":("dojo", "at sunrise, he lies on the wooden floor after reaching out to grapple, the elf samurai pins him again from the side, her unwrapped breasts over his face, breast smother with room to breathe, her bare foot stroking his lower belly, footjob, cum dripping, " + CORD),
   "onedari_boss":("dojo", "on the tatami mats in the corner, he lies on his back, the elf samurai holds him down firmly, her unwrapped breasts over his face, breast smother with room to breathe, her fingers stroking his nipple, faint blush on her serious face, cum dripping untouched, " + CORD),
 },
 "lose_desc": "keeps him in the elf mansion forever as the princess's cherished groom, a red braided cord wound twelve times around his ring finger.",
 "onanie": {
   "master": ("okunoma", "kneeling, stroking his own neck and nipple with a strip of red cloth like a sleeve, one wet finger reaching behind to stroke his own anus, penis untouched"),
   "e1": ("pond", "crouching by the water, a wet rope wound around his own chest, one finger stroking his own anus, penis untouched"),
   "e2": ("guard", "sitting against a pillar, one wrist tied to it with a loose cord, tracing his own nipple, penis untouched"),
   "e3": ("gate", "leaning on the gate post, flicking his own nipples quickly with both hands, penis untouched"),
   "boss": ("dojo", "lying on a tatami mat, pressing a pillow over his own face, stroking his own nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "okunoma", "two small golden bells on red braided silk cords hanging from a carved wooden transom, ringing by themselves, faint sound ripples, incense smoke, close-up"),
   "2": ("m", "corridor", "holding a small bamboo whistle to her lips with one hand, her long sleeve swaying, shadows of ninja gathering on the roof behind the shoji, calm smile"),
   "3": (None, "webgarden", "a large soft white spider silk net stretched between two garden trees, glittering with night dew in the moonlight, empty, close-up"),
   "4": (None, "front", "sweet pale pink incense smoke drifting out through the gap of painted sliding doors, a small bronze incense burner on the floor, warm lamp light"),
   "5": (None, "shinjo", "a red futon laid out with two pillows, a small golden bell on a red braided cord by the pillow, moonlight through shoji screens, quiet, empty room"),
 },
}
