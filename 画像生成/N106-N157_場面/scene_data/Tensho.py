# N107 魔王城の天将（Tensho）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（竜の剣士も曲線のある体つき）。
# エルベティエ：原作は青い半透明のスライム → pale turquoise-white の半透明に置き換え。
# ウンディーネ：原作は水色の肌と髪 → pale mint の肌と髪に置き換え。泉の光も青ではなく淡い白緑の光にする。
# 挿入は 尾の先（魔王・竜の剣士）・粘体・細い水流 だけなので pen は付けない。淫魔の尾は前を包むだけ（後ろには入れない）。
# 蛇体の巻きつきは苦しくない（温かく重いだけ）。分身・取り巻きは出さず、どの絵も責め手1人＋主人公。
SCALE = "a glowing purple scale-shaped mark on his left chest"
COIL = "her warm red snake body coiled gently around him from ankles to chest"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, fangs"
LAMIA_NEG = SOFT_NEG + ", human legs on the lamia, feet on the lamia, crushing, choking, pain"
SLIME_NEG = SOFT_NEG + ", human legs on the slime woman, grotesque, melting face, dissolving skin"
DATA = {
 "code": "Tensho",
 "world": "demon lord's castle on a black rocky mountain, black stone walls, purple candelabra light, red carpet, fantasy, detailed background",
 "bg": "grand throne room of a demon lord's castle, an obsidian throne on a dais, twelve tall candelabra with purple flames in two rows, long red carpet, black stone pillars, high vaulted ceiling, wide empty stone floor, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "アリスフィーズ16世",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, lamia, red snake lower body, long thick red snake tail with a slender tip, purple skin, white hair, very long hair, flower hair ornament, third eye on forehead, golden eyes, pointy ears, purple and black armor, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the white-haired lamia queen with purple skin",
         "pose": "upper body raised high on her coiled red snake body, arms crossed under her chest, proud haughty smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": LAMIA_NEG},
   "e1": {"type": "woman", "jp": "アルマエルマ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, light purple hair, very long hair, pointy ears, black curved horns, violet eyes, black bat wings, slender succubus tail with a heart-shaped tip, black martial artist leotard, purple sash, black arm sleeves, bare feet, soft voluptuous feminine body, huge breasts, narrow waist",
          "name": "the purple-haired succubus with black horns",
          "pose": "light martial arts stance on one foot, one hand beckoning, her heart-tipped tail swaying, playful teasing smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "エルベティエ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, slime woman, monster girl, translucent pale turquoise-white slime body, glossy gel skin, long translucent slime hair, fin-like crest on her head, red eyes, lower body melting into a wide puddle of slime, sleeveless dress shaped from her own slime, soft curvy feminine body, large breasts",
          "name": "the translucent slime queen with red eyes",
          "pose": "rising from a wide puddle of her own slime, arms folded, cold expressionless face, looking down at viewer with red eyes",
          "neg": SLIME_NEG},
   "e3": {"type": "woman", "jp": "ウンディーネ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, water spirit, monster girl, pale mint skin, pale mint hair, long flowing wet hair, silver-grey eyes, lower body a large pale mint slime-like water tail, thin dress of flowing clear water, water droplets floating around her, slender curvy feminine body, large breasts",
          "name": "the mint-haired water spirit",
          "pose": "floating upright on her water tail, one hand raised with a small sphere of water above her palm, calm quiet expression, looking at viewer",
          "neg": SLIME_NEG},
   "boss": {"type": "woman", "jp": "グランベリア",
            "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, dragon woman, red hair, long hair, golden eyes, a thin old scar across one eye, gold and black armor, purple cape, green dragon-scaled forearms and hands, green dragon-scaled shins, thick green dragon tail with a smooth rounded tip, large sword on her back, soft curvy feminine body, large breasts",
            "name": "the red-haired dragon swordswoman with a green tail",
            "pose": "standing straight with one scaled hand resting on the hilt of her large sword, serious composed expression, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "gate":     "main gate of the castle, black rock gate, burning braziers, stone statues above the gate, mountain wind",
   "hall":     "great hall, high ceiling, purple candelabra, red carpet, thick heavy curtains along the wall",
   "spring":   "underground spring chamber, clear spring water, pale glowing ripples, cool mist, a flat stone at the water's edge, wet rocks",
   "canal":    "stone corridor with a water channel running along the floor, moss, wet stone, an iron grating at the far exit with faint light",
   "pool":     "wide pool filled with pale translucent wobbling slime, damp warm air, stone rim",
   "cistern":  "low-ceilinged stone cistern, dark still water, dripping water, cold stone wall",
   "alma":     "boudoir with pale purple drapes, sweet incense smoke, a soft wide bed, a dressing table with a mirror and small bottles of scented oil without text",
   "yard":     "training courtyard of packed earth, wooden striking posts, castle walls, open sky",
   "arena":    "circular stone arena floor, empty spectator seats, swords hung on the wall, scorch marks",
   "granroom": "plain austere room, sword rack, a firm bed, a fireplace with glowing charcoal, a wool blanket on the floor",
   "kitchen":  "castle kitchen at night, large cauldron, spice jars without text, baked sweets on a plate, a wooden counter",
   "vault":    "treasure vault, heaps of gold and silver, old armor, dim lamp light, an empty stone pedestal at the back",
   "window":   "corridor with a huge arched window, night view of the monster lands, moon, his reflection in the glass",
   "throne":   "throne room, obsidian throne, rows of tall candelabra with purple flames, wide black stone floor",
   "bed":      "demon lord's bedchamber, large canopy bed with red silk sheets, a thick stone pillar, a single candelabra",
 },
 "atk": {
   "m1": ("throne", "he kneels on the stone floor with his shirt pulled open, the lamia queen leans down from above, all three of her eyes glowing, her fingertip tracing " + SCALE + ", the end of her red snake tail curling around his ankle, his hips trembling"),
   "m2": ("throne", "he is held upright, " + COIL + ", the lamia queen behind his shoulder pinching and rolling both his nipples with her long fingers, proud smile, " + SCALE + ", he cannot move, flushed"),
   "m3": ("bed", "from side, " + COIL + ", the lamia queen pulls his face close and kisses him deeply, her long tongue in his mouth, saliva trail, the slender tip of her snake tail in his anus, anal, " + SCALE),
   "e1": ("alma", "he lies on his back on the soft bed, the succubus sits behind his head pinning both his arms between her thighs, leaning over his face smiling, her heart-shaped tail tip opened and wrapped around his penis, sucking, " + SCALE),
   "e2": ("pool", "he stands in the pool wrapped from the neck down in translucent slime, the slime queen rises in front of him looking down coldly, slime sucking his nipples, a thin stream of slime flowing into his anus, his whole body trembling, " + SCALE),
   "e3": ("spring", "he floats curled inside a large sphere of clear water above the spring, limbs held still by the water, the water spirit beside the sphere with one hand raised, thin water currents stroking his nipples and flowing into his anus, " + SCALE),
   "boss": ("arena", "from side, he stands held from behind, the dragon swordswoman grips both his wrists together in one scaled hand, her other hand pinching his nipple, the rounded tip of her green dragon tail in his anus, anal, his legs parted, " + SCALE),
 },
 "atk_desc": {
   "m1": "the lamia queen makes him kneel and offer his chest with the gaze of her three eyes.",
   "m2": "the lamia queen coils him up in her warm snake body and rolls his nipples.",
   "m3": "the lamia queen tastes his mouth with a deep kiss while her tail tip presses inside him.",
   "e1": "the succubus pins him with her legs and drains him with her heart-shaped tail.",
   "e2": "the slime queen wraps him from the neck down and presses on him from inside.",
   "e3": "the water spirit floats him in a water prison and strokes him with thin currents.",
   "boss": "the dragon swordswoman holds him from behind for training, pinching his nipple and pressing in with her tail.",
 },
 "lose": {
   # アリスフィーズ 技1（誘惑の魔眼）
   "btl_m1":     ("throne", "all the purple candelabra lit, he kneels with his shirt open offering his chest, " + COIL + ", the lamia queen leans over staring with three glowing eyes, the slender tip of her tail in his anus, a glowing purple kiss mark on his forehead, cum dripping untouched"),
   "onani_m1":   ("window", "kneeling alone before the huge window, staring at his own reflection in the glass, one fingertip tracing " + SCALE + ", his other hand reaching behind to stroke his own anus, penis untouched, the lamia queen watches far away outside the glass"),
   "inochi_m1":  ("throne", "he stands before the open doors of the throne room looking up, the lamia queen holds his chin and stares into his face with three glowing eyes, her red snake body winding up from his feet to his waist, a red silk rug beside the throne, " + SCALE + ", knees giving way"),
   "onedari_m1": ("bed", "he lies on the red silk sheets looking up, " + COIL + ", the lamia queen over him staring with all three glowing eyes, her fingers pinching his nipples, a single candelabra burning beside the bed, " + SCALE + ", cum dripping untouched"),
   # アリスフィーズ 技2（★蛇体の巻きつき）
   "btl_m2":     ("throne", "from side, on the wide stone floor, he is wrapped in thick red coils from ankles to chest, the lamia queen holds him against her, rolling his nipples with long fingers, the slender oiled tip of her tail in his anus, anal, " + SCALE + ", his penis pressed against her smooth belly scales, cum"),
   "onani_m2":   ("vault", "sitting alone behind a heap of gold, his brown cloak wrapped tightly around his body, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, penis untouched, the lamia queen watches far away from the vault door"),
   "inochi_m2":  ("kitchen", "he is wrapped up to his neck in red coils beside the wooden counter, the lamia queen feeds him a baked sweet mouth to mouth, crumbs on his lips, her fingers pinching his nipple inside the coils, a plate of sweets, " + SCALE + ", flushed"),
   "onedari_m2": ("bed", "from side, by the thick stone pillar, he is wrapped in four turns of red snake body, the lamia queen looks away blushing while rolling his nipple, the tip of her tail deep in his anus, anal, small notches carved on the pillar, " + SCALE + ", cum dripping"),
   # アリスフィーズ 技3（魔王の味見）
   "btl_m3":     ("bed", "from side, he is wrapped against the bed pillar by red coils, the lamia queen holds his face and kisses him deeply, long tongue, saliva running down his chin, the tip of her tail pressing deep in his anus, anal, " + SCALE + ", cum dripping"),
   "onani_m3":   ("kitchen", "leaning alone against the kitchen counter at night, sucking two of his own fingers with his tongue, the other hand reaching behind with a finger in his own anus, penis untouched, the lamia queen watches far away from the doorway"),
   "inochi_m3":  ("throne", "dawn light through high windows, he is wrapped in red coils before the throne, offering his tongue, the lamia queen kisses him deeply, saliva trail, the tip of her tail in his anus, anal, a small silver cup beside the throne, " + SCALE),
   "onedari_m3": ("vault", "from side, on top of a heap of gold, " + COIL + ", the lamia queen kisses him long and deep, tongues, the tip of her tail deep in his anus, anal, an empty stone pedestal behind them, " + SCALE + ", cum on his stomach"),
   # アルマエルマ（★テイルドレイン）
   "btl_e1":     ("alma", "he lies on his back on the bed, the succubus sits behind his head pinning both his arms between her thighs, laughing at his ear, her heart-shaped tail tip wrapped around his penis, sucking, a pale purple ribbon tied around his neck, " + SCALE + ", cum"),
   "onani_e1":   ("hall", "sitting alone behind the thick curtain, trailing a thin leather cord along his own inner thigh and behind to tickle his own anus, penis untouched, the succubus watches far away across the great hall"),
   "inochi_e1":  ("yard", "he lies on his back on the packed earth, held in a soft ground hold, the succubus pins his arms with her legs, smiling down, her heart-shaped tail tip wrapped loosely around his penis, sucking gently, " + SCALE + ", dazed"),
   "onedari_e1": ("alma", "in front of the dressing table mirror, he sits held between her legs, the succubus kisses him deeply from the side, tongues, her oiled fingers in his anus, fingering, her heart-shaped tail tip wrapped around his penis, a small oil bottle without text, " + SCALE),
   # エルベティエ（★粘体の包み込み）
   "btl_e2":     ("pool", "he floats upright in the slime pool wrapped from the neck down in translucent slime, the slime queen looks down coldly at his face, slime sucking his nipples, a thin stream of slime inside his anus pressing from within, a small glass vial on the stone rim, " + SCALE + ", cum clouding the slime"),
   "onani_e2":   ("cistern", "sitting alone against the cold wall beside the dark water, stroking his own nipple with wet cold fingers, a wet finger of the other hand in his own anus, penis untouched, the slime queen's face rising far away from the water surface, watching"),
   "inochi_e2":  ("canal", "he floats in the water channel just before the iron grating, the water turned to translucent slime wrapping his whole body up to the neck, the slime queen rises beside him holding a small iron key, cold stare, " + SCALE + ", trembling"),
   "onedari_e2": ("pool", "he is sunk to his neck in the slime pool looking up, the slime queen stands over him with red eyes, slime sucking both his nipples, slime flowing deep into his anus, the whole pool rippling, " + SCALE + ", cum clouding the slime"),
   # ウンディーネ（★水の牢）
   "btl_e3":     ("spring", "he floats curled inside a large sphere of clear water above the spring, unable to move his limbs, the water spirit rests her palm on the sphere, thin currents stroking his nipples and inner thighs, a thin warm current flowing into his anus, " + SCALE + ", cum drifting in the water"),
   "onani_e3":   ("spring", "kneeling alone in the shallow spring behind a rock, looking at his own face on the water surface, one hand on his own nipple, the other hand stroking his own anus under the water, penis untouched, the water spirit watches far away across the spring"),
   "inochi_e3":  ("spring", "he stood in the spring and the water has lifted him into a sphere, floating with his limbs loose, the water spirit beside him guiding a gentle current over " + SCALE + " and into his anus, calm smile, mist"),
   "onedari_e3": ("spring", "he floats inside a sphere of water, a round mirror of water in front of his flushed face, the water spirit behind the sphere with one hand raised, fast thin currents on his nipples and flowing into his anus, " + SCALE + ", cum drifting in the water"),
   # グランベリア（★竜の稽古）
   "btl_boss":   ("arena", "from side, in the middle of the stone arena, he is held from behind, the dragon swordswoman grips his wrists together in one scaled hand, her other hand pinching his nipple, the warm rounded tip of her green tail in his anus, anal, a wooden practice sword on the wall, " + SCALE + ", cum dripping"),
   "onani_boss": ("yard", "standing alone behind a wooden striking post with both hands braced on the wall, back arched, then one warmed hand pinching his own nipple, the other reaching behind with a finger in his own anus, penis untouched, the dragon swordswoman watches far away across the courtyard, blushing"),
   "inochi_boss":("arena", "a wooden practice sword dropped on the stone floor, he is held from behind, the dragon swordswoman grips his wrists together, breathing warm breath on his neck, her fingers rolling his nipple, the tip of her green tail in his anus, anal, " + SCALE + ", knees weak"),
   "onedari_boss":("granroom", "from side, on a wool blanket before the charcoal fire, he sits held from behind, the dragon swordswoman looks away blushing, warm breath on his neck, rolling his nipple, the rounded tip of her green tail deep in his anus, anal, " + SCALE + ", cum dripping"),
 },
 "lose_desc": "keeps him in the castle forever as the demon lord's cherished treasure, twelve glowing purple scale marks on his left chest.",
 "onanie": {
   "master": ("vault", "sitting with his brown cloak wrapped tightly around his body, one hand pinching and rolling his own nipple, an oiled finger of the other hand in his own anus, penis untouched"),
   "e1": ("hall", "sitting behind a curtain, trailing a thin leather cord along his own inner thigh and behind to tickle his own anus, penis untouched"),
   "e2": ("cistern", "sitting against the cold wall, stroking his own nipple with wet cold fingers, a wet finger of the other hand in his own anus, penis untouched"),
   "e3": ("spring", "kneeling in the shallow spring, looking at his own face on the water surface, one hand on his own nipple, the other stroking his own anus under the water, penis untouched"),
   "boss": ("yard", "one hand braced on the wall with his back arched, the other warmed hand pinching his own nipple, then reaching behind to his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "a tall black iron candelabra with a single purple flame just lit, faint purple scale-shaped glow in the air around the flame, close-up"),
   "2": (None, "gate", "the huge black rock gate of the castle slowly opening, burning braziers on both sides, purple light spilling out from inside, low angle"),
   "3": ("m", "throne", "seated high on the obsidian throne with her red snake body coiled around its base, all three eyes glowing, one hand raised, overwhelming proud smile, looking down"),
   "4": (None, "alma", "a small glass bottle of pink scented oil without text on the dressing table, the stopper off, sweet pink vapor rising, a pale purple ribbon beside it, close-up"),
   "5": (None, "throne", "the empty obsidian throne seen from the red carpet, three of the purple candelabra lit and the rest dark, quiet oppressive air"),
 },
}
