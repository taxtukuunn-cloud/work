# N136 三つの塔と城（Hunter）画像データ。登場人物は全員20歳以上。5人とも大人の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# ウンディーネ：原作は水色の長髪 → pale mint hair／light green eyes に置き換え（青・水色は主人公と紛れるため使わない）。
# ナイトメア：夜空色のドレス → dark violet の星柄の寝間着ドレスと書く（navy を避ける）。
# デミウルゴス：肌の色は tags に書かず、場面ごとに WHITE（白い肌）／BLACK（黒い肌の形態）を行為文に足す。
# 挿入は上級サキュバスの凹凸のある尻尾だけ（尾なので pen なし）。デミウルゴスは指まで。踏み祓いは体重をかけない（痛みなし）。
# 絵には冒険者カード（文字なし）か鐘を必ず一つ入れる。
CARD = "a blank adventurer card without text glowing faintly beside him"
BELL = "a white bell hanging above"
WHITE = "her skin pale white"
BLACK = "her skin turned dark ebony black with white hair"
BN = {"neg": "pale skin on the woman"}
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
FOOT_NEG = SOFT_NEG + ", stomping, crushing, pain, shoes, boots"
DATA = {
 "code": "Hunter",
 "world": "fantasy land of three stone towers and a dark castle, a white trial tower shining in the north, grass plains, cold wind, soft magical light, detailed background",
 "bg": "wide grass plain in daytime, three tall stone towers and a dark castle in the distance, a white tower glowing faintly far in the north, wind over the grass, drifting clouds, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "デミウルゴス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, white hair, very long straight hair, golden eyes, thin white sleeveless robe, bare shoulders, barefoot, bare feet, soft curvy feminine body, huge breasts, wide hips",
         "name": "the white-haired tower master in a thin white robe",
         "pose": "standing barefoot on a white floor, one arm stretched out pointing sternly at the viewer, serious angry frown, looking down at viewer with golden eyes",
         "neg": FOOT_NEG},
   "e1": {"type": "woman", "jp": "中級サキュバス",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, dark-skinned female, glossy brown skin, silver hair, long wavy hair, glowing pink eyes, small curved horns, purple succubus dress, purple thighhighs, thin succubus tail, soft curvy feminine body, large breasts",
          "name": "the silver-haired brown-skinned succubus in a purple dress",
          "pose": "one finger raised as if giving a command, the other hand on her hip, teasing confident smile, looking at viewer with glowing pink eyes",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "ウンディーネ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, long legs, pale mint hair, very long flowing hair, light green eyes, fair translucent skin, sheer white water robe, water droplets on her skin, floating orbs of clear water around her, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the mint-haired water spirit in a sheer water robe",
          "pose": "arms crossed under her heavy breasts, an orb of clear water floating over one open palm, bold big-sisterly grin, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ナイトメア",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, purple hair, very long hair, sleepy half-closed violet eyes, dark violet nightgown dress with tiny star pattern, bare shoulders, hugging a white pillow, soft curvy feminine body, large breasts",
          "name": "the purple-haired dream spirit in a starry nightgown",
          "pose": "hugging a white pillow to her chest, head tilted, sleepy gentle smile, one finger on her lips, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "上級サキュバス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long straight hair, cold crimson eyes, black curved horns, black leather bondage-style outfit, black thigh boots, long smooth black tail with gentle rounded ridges, soft curvy feminine body, huge breasts, wide hips",
            "name": "the black-haired horned succubus in a black leather outfit",
            "pose": "sitting on a black throne with legs crossed, chin resting on one hand, her long ridged tail raised beside her, cold disdainful stare, looking down at viewer",
            "neg": SOFT_NEG + ", scary, fangs"},
 },
 "places": {
   "guild":    "adventurer guild reception, wooden counter, notice board with blank papers without text, warm lamp light",
   "field":    "grass plain, three stone towers and a castle in the distance, wind, tall grass",
   "t1stairs": "dim stone staircase landing inside a tower, sweet pale haze in the air, a small bedding of cushions on the landing",
   "t1room":   "tower bedroom with a starry night-sky ceiling, a wide soft bed, many pillows, quiet dim light",
   "t3stairs": "stone staircase with water flowing down the steps, a waterside landing with a stone bench, damp air, ripples",
   "t3room":   "tower chamber filled with shallow clear water, floating orbs of water, a soft bed made of water, cool light",
   "gate":     "castle gate with an open iron door, black roses climbing the walls, cold mist",
   "corridor": "castle corridor with a red carpet, a rest alcove with a long bench and white sheets, sweet haze, candle light",
   "hall":     "castle hall with a huge standing mirror, a bed before the mirror, red carpet, candle light",
   "throne":   "castle throne room, a black throne on a dais, a black rug at the foot of the throne, cold dim light",
   "trial_gate": "entrance of a white tower, white stone arch, soft white light pouring out, cold wind",
   "trial_mid":  "middle floor of a white tower, a prayer place with white pillars, white stone floor, soft light",
   "trial_land": "white stone staircase landing in a white tower, a white stone seat by the wall, soft light",
   "top":      "top floor of a white tower, wide white stone floor, pure white light, open arches to the sky",
   "resident": "inner room at the top of a white tower, a white bed, a white rug, a blank card without text displayed in a frame on the wall",
 },
 "atk": {
   "m1": ("top", "he kneels on the white floor with his shirt opened, head lowered, the tower master stands over him pointing sternly down at his crotch, scolding with an angry serious face, " + WHITE + ", white light around them, " + BELL + ", he trembles and blushes"),
   "m2": ("top", "he lies on his back on the white floor, the tower master sits on a low white step above him, her warm bare sole resting gently on his penis and slowly circling, footjob, the toes of her other bare foot stroking his nipple, " + WHITE + ", serious frown, " + CARD),
   "m3": ("top", "he lies on his back on the white floor, the tower master leans over him kissing him deeply and roughly, tongues, saliva, two oiled fingers of her hand in his anus, fingering, " + BLACK + ", " + BELL + ", his hips lifting", BN),
   "e1": ("hall", "he kneels before the huge mirror rubbing his own cheek and chest against her glossy brown thigh, the succubus stands looking down with glowing pink eyes, one finger raised giving a command, teasing smile, " + CARD + ", his reflection in the mirror"),
   "e2": ("t3room", "he sits in the shallow water, the water spirit kneels facing him pressing his face between her huge breasts, breast smother, orbs of clear water covering both his hands, his own fingers moved to stroke his own nipple and inner thigh, " + CARD),
   "e3": ("t1room", "he lies limp on his back on the wide bed, unable to move, the dream spirit lies beside him kissing his lips softly, her fingertips slowly stroking his nipple, a white pillow under his head, sleepy smile, " + CARD),
   "boss": ("throne", "he kneels on the black rug at the foot of the throne, his own hands pinching his own nipples as if controlled, the horned succubus sits on the throne above looking down coldly, her long ridged tail curved behind him with its tip in his anus, " + CARD),
 },
 "atk_desc": {
   "m1": "the tower master scolds him and makes him kneel for a cleansing rite.",
   "m2": "the tower master cleanses him with her warm bare sole, gently circling without any weight.",
   "m3": "the tower master in her dark form seals his lips with a rough kiss while pressing inside with her fingers.",
   "e1": "the succubus commands him with her charming eyes to rub himself against her skin.",
   "e2": "the water spirit moves his own fingers with water while holding his face between her breasts.",
   "e3": "the dream spirit layers charm kisses until he cannot move, then strokes him slowly.",
   "boss": "the horned succubus controls his hands, forbids release and teases him inside with her ridged tail.",
 },
 "lose": {
   # デミウルゴス 技1（塔の祓い＋★踏み祓い）
   "btl_m1":     ("top", "he lies on his back on the white floor after kneeling, lips parted begging, the tower master stands over him pointing at him sternly, one warm bare sole resting on his penis and circling, footjob, " + WHITE + ", " + BELL + ", " + CARD + ", cum on his stomach"),
   "onani_m1":   ("trial_mid", "kneeling alone behind a white pillar in the prayer place, lips moving as if chanting, one hand rubbing his own nipple, the other hand reaching behind to his own anus, penis untouched, " + CARD + ", the tower master watches far away in the white light"),
   "inochi_m1":  ("trial_gate", "he kneels under the white stone arch with his head bowed, the tower master stands before him with arms crossed, scolding, the toes of one bare foot pressing lightly on his penis, footjob, " + WHITE + ", white light pouring out, " + CARD + ", cum dripping"),
   "onedari_m1": ("resident", "he lies on his back on the white rug, mouth open as if repeating words, the tower master sits on the edge of the white bed, her bare sole slowly circling on his penis, footjob, counting on her fingers, " + WHITE + ", " + CARD + ", cum on his stomach"),
   # デミウルゴス 技2（★塔の踏み祓い）
   "btl_m2":     ("top", "he lies on his back on the white floor, the tower master sits on a low white step, rubbing his penis with her bare sole, footjob, the toes of her other foot on his nipple, " + BLACK + ", short scornful smirk, " + BELL + ", " + CARD + ", cum on his stomach", BN),
   "onani_m2":   ("resident", "lying alone on his back at the foot of the white bed, knees bent high, pressing the sole of his own foot against his own lower belly, hands flat on the rug, penis untouched, " + CARD + ", the tower master watches far away from the doorway"),
   "inochi_m2":  ("top", "he lies on his back on the white floor holding perfectly still, fists clenched at his sides, the tower master sits on a low white step with her bare sole circling on his penis, footjob, " + BLACK + ", " + BELL + ", his hips lifting despite himself, cum dripping", BN),
   "onedari_m2": ("resident", "he lies on his back on a low white bed, the tower master sits above him holding his penis between both her bare soles, rubbing, footjob, " + BLACK + ", looking down, " + CARD + ", cum on his stomach", BN),
   # デミウルゴス 技3（黒の祓い＋★踏み祓い）
   "btl_m3":     ("top", "he lies on his back on the white floor, the tower master leans over him holding his jaw, kissing him deeply and roughly, tongues, saliva trail, two oiled fingers in his anus, fingering, " + BLACK + ", a torn strip of white cloth on his wrist, " + BELL + ", cum on his stomach", BN),
   "onani_m3":   ("trial_land", "sitting alone on the white stone seat on the landing, sucking two of his own fingers deeply as if kissing, the other hand reaching behind pressing his own anus, penis untouched, " + CARD + ", the tower master watches far away from the stairs above"),
   "inochi_m3":  ("trial_gate", "he stands pressed back against the white stone arch, the tower master holds his face kissing him deeply without letting go, tongues, her oiled fingers in his anus, fingering, " + BLACK + ", white light behind them, " + CARD + ", his knees giving way", BN),
   "onedari_m3": ("resident", "he lies on his back on the white bed, the tower master lies half over him kissing him roughly, tongues, saliva, her fingers deep in his anus, fingering, her bare foot resting on his thigh, " + BLACK + ", " + CARD + ", cum on his stomach", BN),
   # 中級サキュバス（★サキュバスの命令）
   "btl_e1":     ("hall", "before the huge mirror, he kneels straddling her thigh rubbing his hips against her glossy brown thigh, the succubus sits on the bed edge looking down with glowing pink eyes, one finger raised commanding, " + CARD + ", their reflection in the mirror, cum on her thigh"),
   "onani_e1":   ("corridor", "lying alone face down on the long bench, rubbing his chest and nipples against the white sheet, hips rocking, penis untouched, " + CARD + ", the succubus watches far away down the red carpet corridor"),
   "inochi_e1":  ("gate", "he kneels at the castle gate with his jacket off, rubbing his cheek against her brown stomach, the succubus stands over him with one finger pointing down at the ground, teasing smile, glowing pink eyes, black roses, " + CARD + ", cum dripping"),
   "onedari_e1": ("hall", "on the bed before the huge mirror, he lies on top of the reclining succubus rubbing his whole body against her glossy brown skin, face between her breasts, the succubus strokes his hair whispering a command, " + CARD + ", cum between them"),
   # ウンディーネ（★水の操り）
   "btl_e2":     ("t3room", "he floats on his back on the soft water bed, the water spirit leans over him pressing his face between her huge breasts, breast smother, orbs of water covering his hands, his own fingers stroking his own nipples, a pale water-drop charm on his neck, " + CARD + ", cum on his stomach"),
   "onani_e2":   ("t3stairs", "sitting alone on the stone bench by the flowing water, wet hands, one wet hand stroking his own nipple, the other stroking his own inner thigh, penis untouched, " + CARD + ", the water spirit watches far away from the top of the stairs"),
   "inochi_e2":  ("t3room", "he stands before a closed door in the water chamber, the water spirit holds him from the side pressing his face into her huge breasts, orbs of water on his hands, his own fingers stroking his own nipple and inner thigh, " + CARD + ", cum dripping"),
   "onedari_e2": ("t3room", "he lies on the soft water bed, the water spirit lies beside him holding his head between her huge breasts for a long time, orbs of water slowly guiding his own fingers over his own nipples, gentle grin, " + CARD + ", cum on his stomach"),
   # ナイトメア（★おまじないのキス）
   "btl_e3":     ("t1room", "he lies limp on his back on the wide bed under the starry ceiling, the dream spirit leans over him kissing his lips, her fingertips stroking his nipple, her other hand on his inner thigh, a dark violet pillow under his head, " + CARD + ", cum on his stomach"),
   "onani_e3":   ("t1stairs", "sitting alone against the wall on the landing, half asleep, one fingertip pressed to his own lips, the other hand stroking his own nipple, penis untouched, " + CARD + ", the dream spirit watches far away from the stairs above hugging a pillow"),
   "inochi_e3":  ("t1room", "he lies on the bed with his face turned up waiting, the dream spirit sits beside him bending down to kiss his forehead, her hand stroking his neck and nipple, morning light through the window, pillows, " + CARD + ", cum dripping"),
   "onedari_e3": ("t1room", "he lies limp on the wide bed, the dream spirit lies on her side against him kissing his lips again and again, her fingertip slowly circling his nipple, sleepy smile, pillows around them, " + CARD + ", cum on his stomach"),
   # 上級サキュバス（★支配と射精禁止）
   "btl_boss":   ("throne", "from side, he kneels on all fours on the black rug at the foot of the throne, one of his own hands pinching his own nipple, the horned succubus stands behind him with arms crossed, her long ridged tail in his anus, a small black horn charm on his neck, " + CARD + ", cum dripping untouched"),
   "onani_boss": ("hall", "kneeling alone before the huge mirror, one oiled finger pressing his own anus then stopping, biting his lip holding back, penis untouched, " + CARD + ", the horned succubus watches far away reflected in the mirror"),
   "inochi_boss":("gate", "from side, he stands bent forward with his hands on the iron gate, his own hand pinching his own nipple, the horned succubus stands behind him looking away coldly, her long ridged tail in his anus, black roses, " + CARD + ", legs trembling, cum dripping"),
   "onedari_boss":("throne", "he lies on his back on the black rug at the foot of the throne, both his own hands pinching his own nipples, the horned succubus sits on the throne with legs crossed holding up three fingers, her long ridged tail deep in his anus, " + CARD + ", cum on his stomach"),
 },
 "lose_desc": "drains his level down to one and keeps him inside the towers forever as a cherished resident.",
 "onanie": {
   "master": ("top", "lying on his back, pressing the sole of his own foot against his own lower belly, hands at his sides, a blank card without text glowing, penis untouched"),
   "e1": ("corridor", "lying face down on a bench, rubbing his chest and nipples against a white sheet, a blank card without text glowing, penis untouched"),
   "e2": ("t3stairs", "sitting by the water, wet hands stroking his own nipple and inner thigh, a blank card without text glowing, penis untouched"),
   "e3": ("t1stairs", "sitting half asleep against the wall, a fingertip on his own lips, the other hand stroking his own nipple, a blank card without text glowing, penis untouched"),
   "boss": ("hall", "kneeling before a mirror, an oiled finger pressing his own anus then stopping, biting his lip, a blank card without text glowing, penis untouched"),
 },
 "magic": {
   "1": (None, "guild", "a blank adventurer card without text lying on a wooden counter, glowing and blinking with soft pale light, close-up"),
   "2": (None, "t1stairs", "a dim stone spiral staircase leading up inside a tower, faint light from above, a soft shadow of someone coming down, no humans"),
   "3": ("e2", "t3room", "raising one hand, a large orb of clear cool water floating and swirling above her palm, small orbs around her, bold grin"),
   "4": ("e1", "corridor", "blowing sweet pink haze from her palm toward the viewer, glowing pink eyes, teasing smile, red carpet behind her"),
   "5": ("m", "top", "standing barefoot under a large white bell, one hand raised to ring it, soft rings of light spreading from the bell, serious face"),
 },
}
