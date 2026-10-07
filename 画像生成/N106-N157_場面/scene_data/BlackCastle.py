# N153 異世界の魔王城（BlackCastle）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作が青・水色の髪や瞳のキャラはいない（青系は使っていない）。
# 髪色：黒華＝紫／黒薔薇＝金／黒蛇＝白（編み込み）／モンクデーモン＝赤／スキュラサーバント＝赤紫。筋肉の線は描かない（格闘家・騎士も曲線のある体つき）。
# 挿入具なし（pen は使わない）。後ろは黒華とモンクデーモンの指だけ。黒華の尻尾はおちんちんを包んで吸う（後ろには入れない絵にする）。
# 黒の口づけ（m3）は黒華が上に跨って迎える形。主人公は仰向けで動かない。
# 吸血は牙が肌を破らない（血・傷なし）。足は撫でるだけ（踏まない）。蛇は噛まない。蛇体の締め付けは苦しくない。武器は使わない。
# inochi_m2 の会議は「3人以上を出さない」ため黒華1人＋主人公で描く（ほかの二将は描かない）。
CH = "a black leather choker set with round glossy black gems on his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary"
VAMP_NEG = SOFT_NEG + ", blood, bite wound, fangs piercing skin, bleeding, stepping hard, trampling"
SNAKE_NEG = SOFT_NEG + ", snake bite, snake fangs, strangling, pained face, weapon in hand"
TAIL = "her black tail with a soft heart-shaped tip wrapped over his penis, sucking it"
DATA = {
 "code": "BlackCastle",
 "world": "another world demon lord's castle of black stone, purple flame lights, purple banners, glossy black surfaces, heavy quiet air, detailed background",
 "bg": "throne room of a demon lord's castle, black stone pillars, an empty black throne, twelve tall black candlesticks with purple flames, purple banners without text, a black carpet before the throne, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "黒華",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, succubus, purple hair, long wavy hair, purple eyes, glossy black enamel bodysuit, black enamel long gloves, black bat wings, black tail with a heart-shaped tip, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the purple-haired succubus in a black enamel bodysuit",
         "pose": "one gloved hand on her hip, the other hand reaching out as if claiming a treasure, her tail curling beside her, relaxed possessive smile, looking at viewer with purple eyes",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "黒蛇",
          "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, dark-skinned female, brown skin, white hair, long braided hair, amber eyes, green armor breastplate, green pauldrons, lamia, snake lower body, very long emerald green snake tail with smooth scales and a slender tip, soft curvy feminine body, large breasts",
          "name": "the white-braided lamia knight in green armor",
          "pose": "upright on her coiled green snake tail, arms folded under her chest, a trident and a shield resting against the wall behind her, proud calm faint smile, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": SNAKE_NEG + ", human legs on the lamia"},
   "e2": {"type": "woman", "jp": "モンクデーモン",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, red hair, medium hair, two short curved horns, yellow eyes, purple bat wings, purple sling bikini, black boots, soft curvy feminine body, large breasts, wide hips",
          "name": "the red-haired horned monk in a purple sling bikini",
          "pose": "standing in a light open-palm martial arts stance, one palm glowing with soft warm light, cheerful sporty smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", punching, kicking, fighting"},
   "e3": {"type": "woman", "jp": "スキュラサーバント",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, magenta hair, low bun, white maid headdress, pink eyes, black and white long maid dress, white apron, scylla, many soft pink tentacles below the waist, soft round suckers, soft curvy feminine body, large breasts",
          "name": "the magenta-haired scylla maid with pink tentacles",
          "pose": "bowing politely while holding a silver tray with a teapot and a teacup, pink tentacles spread neatly under her skirt, quiet polite smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", human legs on the maid, slimy horror, scary tentacles"},
   "boss": {"type": "woman", "jp": "黒薔薇",
            "tags": "adult woman, mature female, mature face, sharp adult features, 31 years old, adult proportions, beautiful detailed eyes, tall, long legs, vampire, blonde hair, long straight hair, red eyes, black silk top hat, red and black high-collared cape, black gentleman's suit with a white cravat, black knee boots, a sheathed rapier at her hip, soft curvy feminine body, large breasts",
            "name": "the blonde vampire in a top hat and a red and black cape",
            "pose": "one hand touching the brim of her top hat, the other hand holding her cape open, cool polite smile, bats flying around her, looking down at viewer",
            "height_note": "she is much taller than him",
            "neg": VAMP_NEG + ", drawn sword"},
 },
 "places": {
   "gate":     "a glowing gate of light floating in the air under a purple sky, a faint green meadow seen through the gate, black stone path, no wind",
   "front":    "great front gate of the black stone castle, purple banners without text, stone pavement, a stone bench beside the gate",
   "hall":     "castle entrance hall, polished black marble floor, purple lights, high ceiling, a black leather bench by the wall",
   "pantry":   "servants' tea room, silver trays and tea sets, a steaming kettle, a small table and a wooden armchair, warm steam",
   "guest":    "castle guest room, black canopy bed, purple curtains, a large standing mirror, pillows and blankets",
   "dojo":     "castle training hall, stone floor and wooden boards, incense smoke, warm hazy air, a sleeping mat in the corner",
   "knight":   "knights' hall, a stand of green armor, shields lined on the wall, a trident on a wall rack, a rug beside the armor",
   "corridor": "long castle corridor of black stone, purple lights at even intervals, a wide round sunken nest at the far end",
   "garden":   "garden of black roses at night, a huge full moon, bats in the sky, a white stone bench",
   "vamp":     "red and black vampire's chamber, a cape on a stand, wine racks, a velvet couch, roses in a vase",
   "council":  "council room, a round black table, three high-backed chairs, purple lights",
   "throne":   "throne room, an empty black throne, twelve black candlesticks with purple flames, a black carpet",
   "private":  "succubus's private room, glossy black enamel furniture, an enamel couch and an enamel bed, purple incense smoke",
   "treasury": "treasure vault, heaps of round black gems, a large flat-lidded treasure chest, cool glittering light",
   "bedroom":  "hidden bedchamber behind the treasure vault, a glossy black enamel bed, purple lights, purple incense smoke, quiet",
 },
 "atk": {
   "m1": ("throne", "he stands on the black carpet with his chin lifted, offering his neck, the succubus leans close holding his cheek with one gloved hand, her glowing purple eyes staring into his face, whispering, his arms hanging loose, " + CH),
   "m2": ("private", "he lies limp on the enamel couch leaning back into her arms, the succubus hugs him from behind, one gloved finger circling his nipple, " + TAIL + ", his arms hanging powerless, relaxed dazed face, " + CH),
   "m3": ("private", "from side, he lies on his back on the enamel bed without moving, the succubus straddles his hips, girl on top, leaning down kissing him deeply, tongues, saliva trail, her enamel thighs squeezing his waist, her hands holding his wrists, " + CH),
   "e1": ("corridor", "he stands wrapped from ankles to chest in her green snake coils, arms held inside, many slender finger-thin green snakes sliding over his neck, nipples and sides, licking with tiny tongues, the lamia knight holds his chin looking down, calm unpained face, " + CH),
   "e2": ("dojo", "he lies on his back on the stone floor, the monk kneels between his legs pressing his penis between her large breasts, paizuri, one glowing warm palm on his lower belly, cheerful smile, his back arched, " + CH),
   "e3": ("pantry", "he sits in the wooden armchair, his wrists and ankles held gently by pink tentacles, the scylla maid stands beside him holding a teacup to his lips, other pink tentacles stroking both his nipples, his inner thigh and coiled around his penis, " + CH),
   "boss": ("garden", "he kneels on the grass under the full moon, the vampire sits on the white stone bench with one boot off, her bare foot stroking his chest, her toes rolling his nipple, a rose-colored kiss mark on his neck, bats behind him, " + CH),
 },
 "atk_desc": {
   "m1": "the succubus melts his mind with her purple gaze until he offers his choker himself.",
   "m2": "the succubus drains him with her tail while holding his powerless body in her enamel arms.",
   "m3": "the succubus seals his lips with a kiss and rides him while he lies still.",
   "e1": "the lamia knight captures him in her coils and lets countless slender snakes caress his whole body.",
   "e2": "the monk warms his lower belly with her glowing palm and rubs him between her breasts.",
   "e3": "the scylla maid serves him tea while her tentacles caress three places at once.",
   "boss": "the vampire makes him kneel under the full moon and strokes his chest with her bare foot.",
 },
 "lose": {
   # 黒華 技1（恍惚の魔眼）
   "btl_m1":     ("throne", "he kneels on the black carpet before the lit candlesticks, chin lifted high offering his neck, the succubus holds his face with both gloved hands, glowing purple eyes close to his, " + TAIL + ", the largest black gem on his choker, cum dripping"),
   "onani_m1":   ("guest", "standing alone before the large mirror, staring at his own reflection, one hand tracing the choker on his neck, the other hand rubbing his own nipple, penis untouched, the succubus watches far away from behind the purple curtain"),
   "inochi_m1":  ("gate", "he stands with his back to the glowing gate, turned toward the castle, the succubus holds his chin gazing into his face with glowing purple eyes, her other arm around his waist, his knees weak, the open gate behind them, " + CH),
   "onedari_m1": ("bedroom", "he lies on the enamel bed looking up, the succubus lies beside him propped on one elbow, glowing purple eyes close above his face, whispering, " + TAIL + ", her finger on his lips, cum dripping, " + CH),
   # 黒華 技2（★テイルドレイン）
   "btl_m2":     ("private", "he lies limp on the enamel couch in her arms, the succubus holds him from behind, one bare hand between his legs with two oiled fingers in his anus, fingering, her gloved hand rolling his nipple, her tail curled beside them, a single black glove lying on the couch, cum on his stomach, " + CH),
   "onani_m2":   ("treasury", "lying alone and limp in the shadow of the treasure chest, one hand circling his own nipple, a finger of the other hand stroking his own anus, the gems on his choker glowing purple, penis untouched, the succubus watches far away beyond the heaps of gems"),
   "inochi_m2":  ("council", "he sits limp on the succubus's lap in a high-backed chair at the round black table, his head resting on her chest, her fingertip touching his forehead, " + TAIL + ", his arms hanging loose, " + CH + ", cum dripping"),
   "onedari_m2": ("bedroom", "he lies limp on his side in the middle of the enamel bed, the succubus lies behind him holding him, two oiled fingers pressing in his anus, fingering, " + TAIL + ", her lips at his ear, counting smile, cum dripping, " + CH),
   # 黒華 技3（黒の口づけ）
   "btl_m3":     ("private", "from side, he lies on his back on the enamel bed without moving, the succubus straddles his hips, girl on top, kissing him deeply, tongues, saliva trail, the tip of her tail stroking his nipple, a vial of purple incense at the bedside, cum, " + CH),
   "onani_m3":   ("guest", "kneeling alone on the canopy bed straddling a pillow, sucking two of his own fingers as if kissing, hips still, the gems on his choker glowing purple, penis untouched, the succubus watches far away from the gap in the purple curtain"),
   "inochi_m3":  ("throne", "he kneels on the black carpet before the empty throne, the succubus kneels facing him holding his face, kissing him deeply, tongues, the twelve candlesticks lit with purple flames around them, her tail around his waist, " + CH + ", cum dripping"),
   "onedari_m3": ("bedroom", "from side, he lies on his back on the enamel bed, the succubus sits astride his hips, girl on top, not moving, bending down in a long deep kiss, the tip of her tail circling his nipple, his hands lying open on the sheet, cum, " + CH),
   # 黒蛇（★千蛇）
   "btl_e1":     ("corridor", "he is wrapped from ankles to chest in her green snake coils, the lamia knight without her breastplate holds his face against her brown breasts, slender finger-thin green snakes curled around his nipples, the tip of her tail stroking his inner thigh, a green scale bracelet on his wrist, calm unpained face, cum dripping"),
   "onani_e1":   ("knight", "sitting alone in the shadow of the armor stand, a long cloth wound tightly around his body from ankles to chest, stroking his own neck and nipple over the cloth, penis untouched, the lamia knight watches far away from the doorway"),
   "inochi_e1":  ("corridor", "he stands still in the middle of the long corridor looking back, the lamia knight coils her green snake tail around his legs and waist from behind, her arms around his shoulders, the tip of her tail stroking his inner thigh, calm unpained face, " + CH),
   "onedari_e1": ("corridor", "in the round sunken nest, he lies wrapped in her green snake coils, many slender finger-thin green snakes sliding over his neck, nipples, sides and penis, the lamia knight looks down with a faint approving smile, her hand on his hair, calm unpained face, cum dripping, " + CH),
   # モンクデーモン（★堕技胸淫）
   "btl_e2":     ("dojo", "he lies on his back on the stone floor with knees raised, the monk kneels beside him, one glowing warm palm on his lower belly, two oiled fingers of her other hand in his anus, fingering, her breasts above his chest, a purple cord charm on his choker, cum on his stomach untouched"),
   "onani_e2":   ("dojo", "lying alone on the sleeping mat in the corner, one palm pressed on his own lower belly, a finger of the other hand stroking his own anus, penis untouched, the gems on his choker glowing purple, the monk watches far away across the hall"),
   "inochi_e2":  ("dojo", "he lies pinned gently on his back on the wooden boards, the monk holds him down with her body, her large breasts pressing his penis, paizuri, one glowing warm palm on his lower belly, cheerful smile, unpained face, " + CH + ", cum dripping"),
   "onedari_e2": ("dojo", "he lies on his back on the sleeping mat holding his own knees, the monk kneels between his legs, two oiled fingers in his anus, fingering, her other glowing palm on his lower belly, counting aloud with a smile, cum on his stomach, " + CH),
   # スキュラサーバント（★ご奉仕天国）
   "btl_e3":     ("pantry", "he sits in the wooden armchair, wrists and ankles held gently by pink tentacles, the scylla maid stands beside him with her blouse opened at the chest, holding a teacup to his lips, pink tentacles stroking both his nipples, a silver tea-leaf charm on his choker, cum on his stomach"),
   "onani_e3":   ("hall", "sitting alone on the black leather bench by the wall, holding a teacup in one hand, the other hand inside his shirt rubbing his own nipple, penis untouched, the scylla maid watches far away across the marble hall holding a tray"),
   "inochi_e3":  ("guest", "he lies on the canopy bed in the morning, the scylla maid sits at the bedside holding a teacup to his lips, pink tentacles under the blanket stroking his nipples and inner thighs, polite smile, " + CH + ", cum dripping"),
   "onedari_e3": ("pantry", "he sits at the small table with three empty teacups, the scylla maid stands behind him with her hands on his shoulders, pink tentacles stroking his nipples, inner thigh and coiled around his penis at once, polite smile, cum dripping, " + CH),
   # 黒薔薇（★満月のレクイエム）
   "btl_boss":   ("garden", "he kneels on the grass under the full moon, the vampire stands behind him wrapping her cape around him, her lips sucking the side of his neck, rose-colored kiss marks on his neck, a black rose corsage on his chest, bat wings brushing his back, cum dripping untouched"),
   "onani_boss": ("vamp", "kneeling alone in the shadow of the wine rack, tracing the side of his own neck with his fingertips, the other hand rubbing his own nipple, penis untouched, the gems on his choker glowing purple, the vampire watches far away from the velvet couch"),
   "inochi_boss":("garden", "he kneels beside the white stone bench looking up at the huge full moon, the vampire sits on the bench with one boot off, her bare foot stroking his lower belly and penis softly, footjob, her hand tilting his chin, rose-colored kiss marks on his neck, " + CH),
   "onedari_boss":("vamp", "he kneels before the velvet couch inside her opened cape, the vampire seated on the couch leans down sucking his neck with her lips, her bare foot stroking his chest, her toes on his nipple, rose-colored kiss marks, cum dripping, " + CH),
 },
 "lose_desc": "keeps him in the demon lord's castle forever as its cherished black treasure, twelve black gems on his choker.",
 "onanie": {
   "master": ("treasury", "lying limp beside the treasure chest, one hand circling his own nipple, a finger of the other hand stroking his own anus, penis untouched"),
   "e1": ("knight", "sitting with a long cloth wound around his body, stroking his own neck and nipple over the cloth, penis untouched"),
   "e2": ("dojo", "lying on the sleeping mat, one palm on his own lower belly, a finger of the other hand stroking his own anus, penis untouched"),
   "e3": ("hall", "sitting on the leather bench with a teacup in one hand, the other hand rubbing his own nipple, penis untouched"),
   "boss": ("vamp", "kneeling, tracing the side of his own neck with his fingertips, the other hand rubbing his own nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "two tall black candlesticks lit with purple flames, close-up, a round glossy black gem resting on the black carpet between them, soft purple glow"),
   "2": (None, "front", "a large purple banner without text swaying slowly on a black stone gate tower, purple sky, quiet"),
   "3": ("m", "throne", "leaning forward with one gloved finger at her lips, her purple eyes glowing softly, alluring gaze, close-up of her face and chest"),
   "4": (None, "pantry", "a silver tray with a steaming cup of red tea and a teapot, sweet pink steam rising, a single pink tentacle tip setting down a sugar bowl, cup without text"),
   "5": (None, "treasury", "a heap of round glossy black gems and an open treasure chest, cool glitter, a black enamel bed faintly seen through a doorway behind"),
 },
}
