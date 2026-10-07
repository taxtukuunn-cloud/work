# N115 破戒種の島（Hakai）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（武人のオメガも曲線のある体つき）。
# 原作に青／水色の髪・瞳のキャラはいない。オメガの瞳は目印に指定がないので violet eyes とした。
# 金髪が2人いるので書き分ける：エノラマ＝金のツインテール（毛先が赤橙のグラデーション）／熟女＝蜂蜜色のゆるい長髪（honey-gold）。
# 挿入はオメガの硬い尻尾の先だけ（尾なので pen なし）。メタ・エノラマ・熟女は指、アカズキンは尻尾の先で入口をくすぐるだけ（入れない）。
# 槍は突かない（柄で押さえる・立てて持つ）。拳銃は人に向けない（下げる・空へ向ける）。マッチとピンクの炎は熱くない（火傷なし）。
# ライブ会場の観客は描かない（3人以上を出さない）。落書き・旗・看板に文字は描かない。主人公の右手の甲に赤い輪の紋。
MARK = "a glowing red ring-shaped crest on the back of his right hand"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, fangs"
SPEAR_NEG = "spear piercing, stabbing, stabbed, wound, spear tip touching him"
GUN_NEG = "gun pointed at him, aiming at a person, shooting, muzzle flash at a person, bullet, wound"
FIRE_NEG = "burn, burning skin, scorched, wound, fire on clothes"
TAIL = "the smooth rounded tip of her hard tail in his anus, anal, tail insertion"
BIND = "her hard tail coiled around both his wrists"
DATA = {
 "code": "Hakai",
 "world": "volcanic island of a warlike succubus tribe, black rock, distant red lava glow, a smoking volcano on the horizon, sulfur haze, warm wind, detailed background",
 "bg": "stone circular arena built on the rim of a volcano crater, cracked stone floor, hot wind and drifting embers, a black rock castle with white and red banners without text far away, a red river of lava winding below, dusk sky, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "オメガ・デス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, very tall, long legs, silver hair, pale lavender gradient hair, very long hair, white horns, violet eyes, white leotard, black pantyhose, large white and red feathered wings, long hard segmented white tail with a smooth rounded tip, red spear, soft curvy feminine body, huge breasts, wide hips",
         "name": "the silver-haired warrior in a white leotard",
         "pose": "standing with a red spear planted upright at her side, wings half spread, tail raised behind her, proud fearless smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG + ", " + SPEAR_NEG},
   "e1": {"type": "woman", "jp": "エノラマ・レイ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, gradient hair, red-orange hair tips, long twintails, pink horns, red eyes, black bodysuit open at the front, cleavage, red jacket with a fur collar, golden feathered wings, scale pattern on her thighs, striped tail, soft curvy feminine body, huge breasts",
          "name": "the blonde twintail succubus in a red fur-collar jacket",
          "pose": "one hand on her hip, the other hand making a teasing pointing gesture, golden wings spread, smug mocking grin, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "アカズキン",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, twin braids, red eyes, red hooded cape, black bodysuit, two pistols in thigh holsters, thin demon tail, red high heels, slender curvy feminine body, large breasts",
          "name": "the pink-braided succubus in a red hooded cape",
          "pose": "holding a red apple out in one hand, the other hand lifting the edge of her cape in a curtsy, elegant innocent-looking smile, looking at viewer",
          "neg": SOFT_NEG + ", " + GUN_NEG},
   "e3": {"type": "woman", "jp": "マッチ売りの熟女",
          "tags": "adult woman, mature female, mature face, gentle mature features, 35 years old, adult proportions, beautiful detailed eyes, tall, long legs, honey-gold hair, long wavy hair, amber eyes, red hooded robe with small horns on the hood, wicker basket of matches on her arm, small warm flame floating beside her, thin tail, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the honey-haired match seller in a red hooded robe",
          "pose": "holding a lit match up in one hand, a wicker basket on her other arm, a small flame floating beside her, soft motherly-warm smile, looking at viewer",
          "neg": SOFT_NEG + ", " + FIRE_NEG},
   "boss": {"type": "woman", "jp": "メタ・リメイク",
            "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, magenta hair, very long hair, curled ram horns, red eyes, pale pink skin, black leotard, white fur bolero, bat wings, thin demon tail with a spade tip, electric guitar shaped staff, pink flames around her, soft curvy feminine body, huge breasts",
            "name": "the magenta-haired rock singer in a fur bolero",
            "pose": "strumming an electric guitar shaped staff, one leg forward, pink flames swirling, confident rock star grin, looking at viewer",
            "neg": SOFT_NEG + ", " + FIRE_NEG},
 },
 "places": {
   "beach":   "black sand beach, waves washing ashore, driftwood, sulfur haze",
   "forest":  "forest of twisted trees with small red berries, dim light, drifting mist",
   "hut":     "match seller's hut interior, a lit fireplace, a basket full of matches, a rocking chair, flickering shadows on the wall",
   "snow":    "small snowy town square, falling snow, a glowing street lamp, snow-covered cobblestones",
   "apple":   "dim forest of red apple trees, red apples on the branches and on the ground, tangled roots",
   "cellar":  "hideout cellar, piles of round firework shells, a rolled map, a plain red flag without text on the wall, lantern light",
   "hangout": "rocky hangout with colorful abstract graffiti without text on the rocks, an old radio, bags of snacks, cushions",
   "cliff":   "cliff of golden rock, strong wind, wide view of the sea far below",
   "live":    "live stage lit by glowing lava light, huge amplifiers, stage smoke, spotlights, empty dark audience area",
   "green":   "dressing room, a large mirror with light bulbs, fur coats on a rack, guitars on stands, makeup table",
   "lava":    "bank of a red lava river, a black rock bridge, heat haze, dark boulders",
   "arena":   "stone circular arena on the rim of a volcano crater, hot wind, drifting embers, erupting glow in the sky",
   "hall":    "great hall of a black rock castle, white and red banners without text, rows of spears on racks, a training circle marked on the stone floor",
   "bedroom": "bedchamber in a black rock castle, a hard wide bed covered with thick furs, a spear rack, a window showing the glowing volcano",
 },
 "atk": {
   "m1": ("arena", "he lies on his back on the stone floor with his stomach exposed and arms open, the warrior stands over him looking down, the wooden shaft of her red spear resting across his shoulder holding him down, spear tip pointed away, his knees weak, " + MARK),
   "m2": ("arena", "from side, he lies on his back pinned on the stone floor, the warrior kneels between his spread legs, " + BIND + " above his head, one of her hands pinching his nipple, " + TAIL + ", his own penis separate, " + MARK),
   "m3": ("bedroom", "from side, he is held in the warrior's arms on the furs, the warrior kissing him deeply, tongues, saliva trail, " + BIND + ", " + TAIL + ", his own penis separate, breathless"),
   "e1": ("hangout", "he kneels with his face buried between her huge breasts, the twintail succubus hugs his head to her chest with one arm, her other hand rubbing his nipple, smug grin, his arms limp, striped tail curled around his thigh, " + MARK),
   "e2": ("apple", "he sits against the roots of an apple tree, the succubus in the red cape kneels over his lap feeding him a bite of red apple mouth to mouth, kiss, apple juice dripping from his lips, her fingers pinching his nipple, pistols holstered, " + MARK),
   "e3": ("hut", "he lies on a rug before the fireplace with his shirt open, the match seller kneels beside him holding a lit match near his chest without touching, warm glow on his skin, her other hand pinching his nipple, gentle smile, " + MARK),
   "boss": ("live", "he kneels on the stage trembling, the rock singer stands behind him strumming her guitar staff, visible sound ripples in the air, harmless pink flames licking over his bare chest, the spade tip of her tail flicking his nipple, " + MARK),
 },
 "atk_desc": {
   "m1": "the warrior makes him fall on his back and show his stomach with her fighting spirit alone.",
   "m2": "the warrior pins him down, binds his wrists with her hard tail and presses the tail tip inside him.",
   "m3": "the warrior steals his breath with a forceful kiss while her tail tip presses inside him.",
   "e1": "the twintail succubus smothers him sweetly between her breasts and copies other techniques better.",
   "e2": "the succubus in the red cape feeds him an apple mouth to mouth that heats his body.",
   "e3": "the match seller warms his skin with a harmless match flame and pinches his nipple.",
   "boss": "the rock singer shakes his body with guitar sound and flicks his nipples with her tail.",
 },
 "lose": {
   # オメガ 技1（キル・ザ・キング＝威圧）
   "btl_m1":     ("arena", "from side, he lies on his back on the stone floor with his stomach exposed, the warrior kneels over him, the shaft of her red spear lying across his shoulder, " + BIND + ", her fingers pinching his nipple, " + TAIL + ", his own penis separate, cum on his stomach, " + MARK),
   "onani_m1":   ("hall", "lying alone on his back in a corner of the hall with his stomach exposed, one hand rubbing his own nipple, the other hand reaching down stroking his own anus, penis untouched, " + MARK + ", the warrior watches far away holding her spear upright"),
   "inochi_m1":  ("lava", "he lies on his back on the black rock bridge with his stomach exposed, the warrior stands over him looking down with her spear upright at her side, her hard tail coiling around his wrists, heat haze, his knees trembling, cum dripping untouched, " + MARK),
   "onedari_m1": ("bedroom", "he lies on the furs looking up, the warrior kneels over him staring down, her long hard tail coiled around his whole body from chest to thighs, the tail tip pressing into his anus, anal, his own penis separate, cum dripping, " + MARK),
   # オメガ 技2（★尻尾の組み打ち）
   "btl_m2":     ("arena", "from side, he lies on his back pinned on the stone floor, the warrior kneels between his spread legs, " + BIND + " above his head, her hand rolling his nipple, " + TAIL + ", a red bracelet on his wrist, his own penis separate, cum on his stomach, erupting glow in the sky"),
   "onani_m2":   ("cliff", "kneeling alone behind a golden rock, his wrists bound together with his own belt, reaching behind with his bound hands, a finger in his own anus, penis untouched, wind blowing his hair, " + MARK + ", the warrior watches far away on the cliff top"),
   "inochi_m2":  ("arena", "he lies face down on the stone floor after a grappling match, the warrior kneels on one knee over his back, " + BIND + " behind his back, " + TAIL + ", her free hand raised as if calling the start, his own penis separate, cum dripping, " + MARK),
   "onedari_m2": ("hall", "from side, inside the training circle under the banners, he lies on his back, the warrior over him pinching his nipple, " + BIND + " tightly above his head, " + TAIL + ", his own penis separate, cum on his stomach, " + MARK),
   # オメガ 技3（デストピア＝キス＋尻尾）
   "btl_m3":     ("bedroom", "from side, he is held tight in the warrior's arms on the furs, the warrior kissing him deeply without letting go, tongues, saliva trail, her fingers pinching his nipple, " + BIND + ", " + TAIL + ", his own penis separate, cum on his stomach, volcano glowing in the window"),
   "onani_m3":   ("green", "crouching alone in the dark corner behind the dressing room, sucking two of his own fingers deeply as if kissing, the other hand reaching behind pressing a finger into his own anus, penis untouched, " + MARK + ", the warrior watches far away from the doorway"),
   "inochi_m3":  ("bedroom", "morning light, he lies in the furs offering his lips, the warrior leans over him kissing him deeply, tongues, saliva trail, " + BIND + ", her wing covering them, his body limp, cum dripping untouched, " + MARK),
   "onedari_m3": ("bedroom", "from side, he sits on the warrior's lap on the bed facing her, the warrior kissing him deeply, tongues, saliva trail, " + BIND + " behind his back, " + TAIL + ", his own penis separate, cum on his stomach, volcano glowing in the window"),
   # エノラマ・レイ（★戒滅・豊玉魔法）
   "btl_e1":     ("hangout", "he kneels with his face buried between her huge breasts, the twintail succubus holds his head to her chest, one hand rolling his nipple, two glossy fingers of her other hand in his anus, fingering, smug grin, a golden feather ornament in his hair, cum dripping untouched, " + MARK),
   "onani_e1":   ("forest", "kneeling alone behind a twisted tree, pressing his face into his rolled-up brown cloak, one hand rubbing his own nipple, the other hand reaching behind stroking his own anus, penis untouched, " + MARK + ", the twintail succubus watches far away between the trees"),
   "inochi_e1":  ("cliff", "he hangs limp in her arms on the golden rock, the twintail succubus holds him from the front pressing his face into her huge breasts, her striped tail stroking his inner thigh, mocking laugh, wind, golden wings spread, cum dripping untouched, " + MARK),
   "onedari_e1": ("hangout", "he lies on the cushions with his face buried in her huge breasts, the twintail succubus lies over him hugging his head, pinching his nipple, her glossy fingers in his anus, fingering, a radio and snack bags beside them, cum dripping, " + MARK),
   # アカズキン（★リンゴをどうぞ❤）
   "btl_e2":     ("apple", "he sits against the roots of an apple tree with his shirt open, the succubus in the red cape stands over him tracing his nipple with the toe of her red high heel without stepping, the tip of her thin tail tickling the entrance of his anus, a bitten apple in her hand, pistols holstered, cum on his stomach, " + MARK),
   "onani_e2":   ("apple", "sitting alone under an apple tree, biting a red apple held in one hand, juice on his chin, the other hand pinching his own nipple, flushed skin, penis untouched, " + MARK + ", the succubus in the red cape watches far away between the trees"),
   "inochi_e2":  ("apple", "he kneels naked on the forest floor among scattered clothes, the succubus in the red cape crouches in front feeding him a slice of apple from her lips, kiss, her pistols lowered at her sides, sweet pink smoke drifting in the air, cum dripping untouched, " + MARK),
   "onedari_e2": ("cellar", "he sits on a chair under the plain red flag, the succubus in the red cape straddles his lap feeding him apple mouth to mouth, kiss, juice dripping, her fingers pinching his nipple, the tip of her thin tail tickling the entrance of his anus, cum dripping, " + MARK),
   # マッチ売りの熟女（★暖かな火）
   "btl_e3":     ("hut", "he lies on his back on a rug before the fireplace, the match seller kneels beside him holding a lit match near his chest without touching, her other hand between his legs with two oiled fingers in his anus, fingering, burnt matchsticks on the floor, a blank matchbox without text, cum on his stomach, " + MARK),
   "onani_e3":   ("snow", "crouching alone under the street lamp in the falling snow, staring up at the lamp flame, one hand reaching behind stroking his own anus with warmed fingers, penis untouched, white breath, " + MARK + ", the match seller watches far away across the square"),
   "inochi_e3":  ("snow", "he kneels in the snow staring into a match flame held before his face, the match seller kneels behind him holding the lit match in front of his face, her other hand pinching his nipple, a faint vision of himself begging inside the flame, a full basket of matches, cum dripping untouched, " + MARK),
   "onedari_e3": ("hut", "he sits in the rocking chair before the fireplace with his shirt open, the match seller leans over him from the side holding a third lit match near his chest without touching, her other hand pinching his nipple, he stares into the flame, cum dripping untouched, " + MARK),
   # メタ・リメイク（★エンター・サドマゾ）
   "btl_boss":   ("live", "he kneels on all fours on the stage, the rock singer kneels behind him, two oiled fingers in his anus, fingering, the spade tip of her tail flicking his nipple, her guitar staff floating and ringing with visible sound ripples, harmless pink flames on his skin, a guitar pick on a cord around his neck, cum dripping, " + MARK),
   "onani_boss": ("lava", "sitting alone behind a boulder by the lava river, flicking both his own nipples with his fingertips in rhythm, head tilted as if listening, penis untouched, " + MARK + ", the rock singer watches far away on the black rock bridge with her guitar staff"),
   "inochi_boss":("live", "he kneels on the stage with his face buried in her fur bolero and huge breasts, the rock singer holds his head to her chest and sings into his ear, her tail stroking his back, spotlights, stage smoke, his arms limp, cum dripping untouched, " + MARK),
   "onedari_boss":("green", "he sits on a chair facing the large mirror, the rock singer stands behind him with her guitar staff slung, one hand flicking his nipple, her tail tip holding his chin toward the mirror, his reflection flushed, he trembles on the edge, cum dripping, " + MARK),
 },
 "lose_desc": "keeps him on the island forever as a cherished sparring partner of the tribe, all twelve lines of the crest on his hand glowing red.",
 "onanie": {
   "master": ("cliff", "kneeling, his wrists bound together with his own belt, reaching behind with a finger in his own anus, penis untouched"),
   "e1": ("forest", "kneeling, pressing his face into his rolled-up cloak, one hand rubbing his own nipple, the other stroking his own anus, penis untouched"),
   "e2": ("apple", "sitting under an apple tree, biting a red apple, the other hand pinching his own nipple, penis untouched"),
   "e3": ("snow", "crouching under the street lamp, staring at the flame, stroking his own anus with warmed fingers, penis untouched"),
   "boss": ("lava", "sitting behind a boulder, flicking his own nipples with his fingertips in rhythm, penis untouched"),
 },
 "magic": {
   "1": (None, "arena", "a glowing white ring-shaped crest made of twelve short lines floating in the air, two of the lines turned glowing red, embers drifting, close-up, without text"),
   "2": (None, "lava", "a great volcano rumbling at dusk, a low column of smoke and red glow at the crater, faint tremor ripples in the air, distant view"),
   "3": ("e2", "apple", "holding one pistol pointed straight up at the sky, sweet pink smoke curling from the barrel and drifting around her, playful elegant smile"),
   "4": (None, "apple", "a single glossy red apple with one bite taken out resting on a tree root, juice glistening, faint pink shimmer rising from it, close-up"),
   "5": (None, "lava", "a black rock castle beyond a lava river, white and red banners without text fluttering on its towers, the gate standing open, red glow on the walls"),
 },
}
