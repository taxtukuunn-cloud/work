# N146 ミノタウロスの迷宮（Minotaur）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作に青・水色の髪や瞳のキャラはいない（置き換えなし）。
# 牛の魔物たちは豊満で柔らかい体つき（muscular・abs は書かずネガティブに入れる）。武器（大剣・斧・弓銃・如意棒）は持つか立てかけるだけで振るわない。
# 挿入する道具はない（pen は全部なし）。後ろに触れるのは牛魔王の指だけ。騎乗（魔王の口づけ・押し倒し・腰振り）は彼女が上に跨る形で、主人公は下で受け身。
# 斉天大聖の分身は「3人以上を出さない」ため本体1人だけで描く（胸で挟み、両手で乳首、尻尾で内ももを1人で。分身は描かない）。
# ミズタウロスは腰から下が牛の体（四つ足）。足で踏む技は撫でる・擦るだけ（痛みなし）。主人公の首には親指ほどの真鍮の牛の鈴。
BELL = "a thumb-sized brass cowbell on a leather cord around his neck"
BELLS = "many thumb-sized brass cowbells on a leather cord around his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, weapon swinging, stomping, pain"
TAUR_NEG = SOFT_NEG + ", human legs on the cow woman, two legs on the cow woman"
DATA = {
 "code": "Minotaur",
 "world": "vast underground stone labyrinth under a mountain, stone block walls, burning wall torches, bull horn ornaments, hay and warm torchlight, detailed background",
 "bg": "throne room deep in an underground stone labyrinth, stone block walls and wall torches, a golden throne draped with red cloth, gold ornaments, bull horn ornaments, a red bed beside the throne, warm torchlight, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "牛魔王",
         "tags": "adult woman, mature female, mature face, sharp adult features, 32 years old, adult proportions, beautiful detailed eyes, very tall, long legs, dark-skinned female, brown skin, blonde hair, long wavy hair, large black bull horns, red eyes, red draped cloth dress, gold jewelry, gold armlets, gold neck ornament, soft voluptuous feminine body, huge breasts, wide hips, thick thighs",
         "name": "the blonde black-horned demon queen in red cloth",
         "pose": "sitting on a golden throne with her chin on one hand, the other large hand held out as if to grab, bold haughty grin, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ハイミノタウロス",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, fair skin, pink hair, short hair, cow horns, cow ears, violet eyes, pink and gold plate armor, pink and gold breastplate, armored gauntlets, waist armor, greatsword sheathed on her back, kite shield, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the pink-haired horned knight in pink and gold armor",
          "pose": "holding a shield at her side, one armored hand on her chest in a knightly bow, polite confident smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "ミズタウロス",
          "tags": "adult woman, mature female, mature face, 34 years old, adult proportions, beautiful detailed eyes, fair skin, green hair, long hair in a loose side braid, cow horns, cow ears, amber eyes, white blouse, green skirt, taur, cow taur, lower body of a cow with four hooved legs, cream and brown cow fur, cow tail, soft ripe voluptuous upper body, huge breasts",
          "name": "the green-haired cow-bodied milk carrier in a white blouse",
          "pose": "carrying a metal milk can without text in one arm, the other hand offering a cup of milk, warm caring mature smile, looking at viewer",
          "neg": TAUR_NEG},
   "e3": {"type": "woman", "jp": "ジニタウロス",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, lightly tanned skin, black hair, medium shaggy hair, cow horns, cow ears, golden eyes, black leather vest, denim jeans, leather boots, crossbow slung on her back, cow tail, soft curvy feminine body, large breasts, wide hips",
          "name": "the black-haired horned lookout in a black leather vest and jeans",
          "pose": "one boot up on a wooden crate, arms resting on her knee, leaning forward, rough cocky grin, looking down at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "斉天大聖",
            "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, long legs, fair skin, red hair, very long hair, golden eyes, gold circlet on her forehead, red china dress with gold trim, side slit, brown monkey tail, long red staff with gold tips, soft curvy feminine body, huge breasts, slim waist",
            "name": "the long red-haired monkey-tailed woman in a red china dress",
            "pose": "resting a long red staff across her shoulders, one hand on her hip, proud toothy grin, tail curled up, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "gate":     "labyrinth entrance, closed heavy stone door, wall torches, bull horn ornaments, a wooden lookout seat",
   "corridor": "winding stone corridor, identical forking paths, torch shadows on the walls",
   "barn":     "stone cow barn, piles of hay, wooden fence, wooden pails, warm lantern light",
   "milkhut":  "milk hut interior, metal milk cans without text, wooden pails, cool air, hay bedding",
   "tower":    "lookout tower platform high above the labyrinth, wooden railing, wooden crates, a bedroll, a crossbow hung on the wall",
   "guard":    "knights' guardroom, armor stands and shields on the wall, a greatsword leaning on the wall, long bench, simple bed",
   "arena":    "training ground with a sand floor, wall torches, stone walls",
   "monkey":   "room draped with red cloth, a pile of peaches, a long red staff leaning on the wall, red cushions on the floor",
   "cloud":    "chamber filled with a soft fluffy white cloud bed, cool pale mist, golden light",
   "treasure": "treasure vault, heaps of gold coins and silver, horn-shaped cups, chests",
   "spring":   "underground spring, cold clear water, mossy rocks, dripping water",
   "feast":    "feast hall, long table with jugs of milk and wine, large platters, a seat of honor",
   "throne":   "throne room, golden throne draped with red cloth, red carpet, wall torches",
   "bedroom":  "bedchamber of the demon queen, large bed under a red cloth canopy, incense smoke, gold lamps",
   "bed":      "red bed beside the golden throne, red sheets and cushions, torchlight",
 },
 "atk": {
   "m1": ("throne", "he sits sideways on the lap of the demon queen on the golden throne, her large hand wrapped around his waist, her other hand holding his chin and tilting his face up, haughty grin, he leans his weight on her chest, " + BELL),
   "m2": ("bedroom", "from side, he lies on his back on the large bed, the demon queen lies on top of him pressing him down with her soft heavy body, his face buried between her breasts, breast smother, one of her hands pinching his nipple, two oiled fingers of her other hand in his anus, fingering, " + BELL),
   "m3": ("bed", "from side, he lies on his back on the red bed with arms limp, the demon queen straddles his hips, cowgirl position, leaning down and kissing him deeply, tongues, saliva trail, her breasts pressed on his chest, " + BELL),
   "e1": ("guard", "he lies on his back on the guardroom floor, the knight kneels between his legs with her breastplate removed, his penis squeezed tightly between her breasts, paizuri, one cold armored gauntlet holding his wrist down, polite smile, " + BELL),
   "e2": ("milkhut", "he sits leaning back against the hay bedding, the milk carrier bends her upper body over his lap with her blouse opened at the chest, milk poured over her breasts, his penis squeezed between her milky breasts, paizuri, a milk can beside them, " + BELL),
   "e3": ("tower", "he sits on the floor leaning back on his hands, the lookout sits on a wooden crate above him looking down, her bare foot pressing his penis against his lower belly, footjob, her other bare foot resting on his chest, boots set aside, cocky grin, " + BELL),
   "boss": ("monkey", "he lies on his back on red cushions, the long red staff laid beside him like a fence, the red-haired woman kneels between his legs with her china dress opened at the chest, his penis squeezed between her breasts, paizuri, both her hands stroking his nipples, her monkey tail stroking his inner thigh, " + BELL),
 },
 "atk_desc": {
   "m1": "the demon queen grabs him in her large hands and sets him on her lap until he leans on her.",
   "m2": "the demon queen pins him under her soft heavy body, buries his face in her breasts and presses inside with her fingers.",
   "m3": "the demon queen seals his lips with a deep kiss while sitting astride him.",
   "e1": "the knight pushes him down politely and squeezes him hard between her breasts, cold armor and warm skin.",
   "e2": "the milk carrier pours milk over her breasts and squeezes him slowly between them.",
   "e3": "the lookout looks down at him and rubs him with her bare foot without any pain.",
   "boss": "the monkey-tailed woman squeezes him between her breasts while her hands and tail stroke him everywhere at once.",
 },
 "lose": {
   # 牛魔王 技1（掴む・握る＋★メガトンプレス）
   "btl_m1":     ("throne", "he sits on the lap of the demon queen on the golden throne leaning back into her breasts, her large hand gripping his waist, her other hand holding his wrist, a gold-trimmed bell among " + BELLS + ", cum dripping untouched, dazed"),
   "onani_m1":   ("feast", "sitting alone beside the seat of honor, hugging himself tightly with one arm, fingers on his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, the demon queen watches far away from the end of the long table"),
   "inochi_m1":  ("treasure", "he reaches toward a gold cup on a heap of coins, the demon queen sits behind him on the gold gripping his outstretched wrist and pulling him onto her lap, her other hand around his waist, amused grin, " + BELLS + ", cum dripping"),
   "onedari_m1": ("bedroom", "he sits on the lap of the demon queen at the edge of the large bed, both her large hands gripping his waist firmly, her lips at his ear, he clings to her arm, " + BELLS + ", cum dripping untouched"),
   # 牛魔王 技2（★メガトンプレス）
   "btl_m2":     ("bedroom", "from side, he lies on his back on the large bed, the demon queen lies on top of him pressing him down, his face buried between her breasts, breast smother, her fingers rolling his nipple, two oiled fingers of her other hand deep in his anus, fingering, a red cloth sash tied on his wrist, cum between their stomachs"),
   "onani_m2":   ("barn", "lying alone on the hay bedding under a thick heavy quilt pulled up to his chest, one hand rubbing his own nipple under the quilt, the other hand stroking his own anus, penis untouched, the demon queen watches far away from the barn door"),
   "inochi_m2":  ("throne", "he lies face down on the red carpet before the throne reaching one hand forward, the demon queen lies over his back pressing him down with her soft weight, her arm around his waist pulling him back, her fingers on his nipple, " + BELLS + ", his hand going limp"),
   "onedari_m2": ("bed", "from side, he lies on his back on the red bed, the demon queen covers him with her whole soft body, his face buried between her breasts, breast smother, her fingers pinching his nipple, two oiled fingers pressing in his anus, fingering, " + BELLS + ", cum between their stomachs"),
   # 牛魔王 技3（魔王の口づけ＋★メガトンプレス）
   "btl_m3":     ("bed", "from side, he lies on his back on the red bed, the demon queen straddles his hips, cowgirl position, sinking her weight down, kissing him deeply, tongues, saliva trail, her hand pinching his nipple, a black horn fragment pendant on his neck cord, cum overflowing"),
   "onani_m3":   ("spring", "kneeling alone by the underground spring straddling a pillow and sinking his hips onto it, sucking two of his own fingers as if kissing, hands away from his crotch, penis untouched, the demon queen watches far away across the water"),
   "inochi_m3":  ("feast", "from side, he lies on his back on cushions beside the long table, the demon queen straddles his hips, cowgirl position, kissing him deeply, tongues, a horn cup of milk in her hand, platters on the table, " + BELLS + ", cum overflowing"),
   "onedari_m3": ("bed", "from side, he lies on his back on the red bed in dim dawn torchlight, the demon queen straddles his hips pressed chest to chest, cowgirl position, a long deep kiss, saliva trail, his arms limp on the sheets, " + BELLS + ", cum overflowing"),
   # ハイミノタウロス（★強圧巨乳パイズリ）
   "btl_e1":     ("guard", "he lies on his back on the guardroom floor, the knight kneels between his legs with her breastplate removed, his penis squeezed hard between her breasts, paizuri, her cold armored gauntlet holding his wrist, a pink and gold armor charm on his neck cord, cum on her breasts"),
   "onani_e1":   ("corridor", "sitting alone at a dead end of the stone corridor, pressing a pillow hard against his own chest, his fingers rubbing his own nipple under it, penis untouched, the knight watches far away at the corner of the corridor"),
   "inochi_e1":  ("guard", "he lies on his back on the long bench, the knight leans over him holding his wrist with a cold armored gauntlet, her breastplate removed, his face pressed between her warm breasts, breast smother, " + BELLS + ", cum dripping untouched"),
   "onedari_e1": ("guard", "he lies on the simple bed, the knight kneels between his legs with her breastplate removed, his penis squeezed hard between her breasts, paizuri, one armored finger raised as she counts aloud, gentle smile, " + BELLS + ", cum on her breasts"),
   # ミズタウロス（★熟女悩殺パイズリ）
   "btl_e2":     ("milkhut", "he sits leaning back against the hay bedding, the milk carrier bends her upper body over his lap with her blouse open, milk dripping over her breasts, his penis squeezed between her milky breasts, paizuri, a milk-can-shaped charm on his neck cord, cum and milk on her breasts"),
   "onani_e2":   ("barn", "kneeling alone beside a wooden pail of milk, dipping his fingers in the milk and spreading it on his own nipple, milk running down his chest, penis untouched, the milk carrier watches far away over the wooden fence"),
   "inochi_e2":  ("milkhut", "he sits on the floor between milk cans, the milk carrier lowers her upper body and feeds him milk mouth to mouth, kiss, milk dripping from his lips, her arms holding his head to her breasts, " + BELLS + ", cum dripping untouched"),
   "onedari_e2": ("milkhut", "he lies on the hay bedding, the milk carrier pours milk from a can over her breasts, his penis wrapped between her milky breasts, paizuri, slow movement, her milky finger circling his nipple, warm smile, cum and milk"),
   # ジニタウロス（★踏みにじり足コキ）
   "btl_e3":     ("tower", "he sits on the tower floor with his legs open, the lookout sits on a wooden crate above him looking down, her bare foot rubbing his penis against his lower belly, footjob, her other bare foot on his chest, a black leather button on his neck cord, " + BELLS + ", cum on her foot"),
   "onani_e3":   ("gate", "sitting alone in the shadow of the closed stone door, one knee pulled up, rubbing the sole of his own foot against his own lower belly, hands on the floor, penis untouched, the lookout watches far away from the lookout seat"),
   "inochi_e3":  ("corridor", "he kneels on the stone floor of the corridor with his head lowered, the lookout stands over him with one bare foot resting lightly on his shoulder, looking down with a cocky grin, hands on her hips, " + BELLS + ", cum dripping untouched"),
   "onedari_e3": ("tower", "he lies on his back on the bedroll, the lookout sits on a crate beside him, the sole of her bare foot stroking his penis on his lower belly, footjob, her other foot on his chest, his lips moving as he counts, cum on his stomach"),
   # 斉天大聖（★大乱舞）
   "btl_boss":   ("monkey", "he lies on his back on red cushions with the long red staff laid beside him like a fence, the red-haired woman kneels between his legs with her china dress opened, his penis squeezed between her breasts, paizuri, both her hands rolling his nipples, her monkey tail stroking his inner thigh, a strand of red hair tied on his neck cord, cum on her breasts"),
   "onani_boss": ("cloud", "lying alone sunk in the soft cloud bed, one hand rubbing his own nipple, the other hand stroking his own inner thigh, his neck arched, penis untouched, the red-haired woman watches far away sitting on a cloud"),
   "inochi_boss":("arena", "he lies on his back on the sand floor, the red-haired woman kneels over him, one hand stroking his nipple, the other hand on his neck, her monkey tail stroking his inner thigh, the long red staff stuck upright in the sand, " + BELLS + ", cum dripping untouched"),
   "onedari_boss":("monkey", "he lies on a bed of red cloth beside a pile of peaches, the red-haired woman kneels between his legs with her china dress opened, his penis held long between her breasts, paizuri, her fingers pinching both his nipples, proud grin, cum on her breasts"),
 },
 "lose_desc": "makes him the cherished treasure of the underground labyrinth forever, twelve thumb-sized brass cowbells on a leather cord around his neck.",
 "onanie": {
   "master": ("corridor", "lying behind a stone pillar under a thick heavy quilt, one hand rubbing his own nipple, the other hand stroking his own anus, penis untouched, " + BELL),
   "e1": ("corridor", "sitting at a dead end, pressing a pillow hard against his own chest, fingers rubbing his own nipple, penis untouched, " + BELL),
   "e2": ("barn", "kneeling beside a pail of milk, spreading milk on his own nipple with his fingers, penis untouched, " + BELL),
   "e3": ("gate", "sitting by the closed stone door, rubbing the sole of his own foot on his own lower belly, penis untouched, " + BELL),
   "boss": ("cloud", "lying on the cloud bed, one hand on his own nipple, the other stroking his own neck and inner thigh, penis untouched, " + BELL),
 },
 "magic": {
   "1": (None, "gate", "a soft leather cord with two thumb-sized brass cowbells and a blank red tag without text lying on a stone ledge, warm torchlight, close-up"),
   "2": (None, "corridor", "an empty winding stone corridor, hoofprints in the dust leading around the corner, a long horned shadow cast on the wall by torchlight, faint sound ripples"),
   "3": (None, "corridor", "a fork of two identical stone corridors with identical torches, faint mist on the floor, a blank weathered signpost without text"),
   "4": ("e2", "milkhut", "pouring fresh milk from a metal milk can into a wooden cup, steam and a sweet glow rising from the milk, offering the cup forward, warm smile"),
   "5": (None, "barn", "a quiet stone cow barn with an open wooden fence gate, piles of hay, rows of brass cowbells and blank red tags without text hanging from a beam, warm lantern light"),
 },
}
