# N152 貴婦人の村と風光明媚の丘（Madam）画像データ。登場人物は全員20歳以上（数百年を生きる妖魔・魔物。見た目は26〜32歳）。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# メイドスキュラ：原作は紺色の髪 → 主人公と紛れるので dark violet hair に置き換え。
# マダムアンブレラ：原作は金髪 → キャンディ（金髪の巻き髪）と被るので pale platinum hair に置き換え。
# 挿入はマダムアンブレラの触手だけ（pen なし）。アラディアは指だけ。キャンディ・インセクト・メイドは後ろに触れない。
# キャンディのお菓子のスカートは包むだけ（食べる・飲み込む絵にしない）。虫の甲殻・触手は怖くしない（鎌・爪なし）。痛み・流血なし。
# 主人公の近くに白いティーカップを一つ入れる。
CUP = "a white porcelain teacup with a gold rim beside him"
W_NEG = "muscular female, abs, broad shoulders on the woman, scary, horror, fangs"
CANDY_NEG = W_NEG + ", eating a person, vore, swallowing, biting, melting body"
BUG_NEG = W_NEG + ", scythe, claws, mandibles, spider, grotesque, insect face"
TEN_NEG = W_NEG + ", grotesque, slime monster, tentacle from mouth"
DATA = {
 "code": "Madam",
 "world": "elegant village of noble ladies and a scenic green hill, afternoon tea party, white lace, silver tea sets, roses, windmills far away, soft daylight, detailed background",
 "bg": "scenic green hill tea party in daytime, flower field, windmills, a white table with a silver tea set and white teacups, plates of baked sweets, a witch's manor far away on the hilltop, gentle breeze, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "アラディア",
         "tags": "adult woman, mature female, mature face, 32 years old, adult proportions, beautiful detailed eyes, tall, green hair, long wavy hair, violet eyes, black witch hat, long purple opera gloves, black and purple witch dress, very voluptuous plump soft body, gigantic breasts, wide hips, thick thighs, soft belly",
         "name": "the green-haired witch in a black witch hat and purple gloves",
         "pose": "holding a silver teapot in one gloved hand, the other hand offering a white teacup, calm gracious hostess smile, looking at viewer",
         "height_note": "she is much taller than him",
         "neg": W_NEG},
   "e1": {"type": "woman", "jp": "マダムインセクト",
          "tags": "adult woman, mature female, mature face, 30 years old, adult proportions, beautiful detailed eyes, tall, brown hair, hair bun, amber eyes, wide-brimmed white hat, white lace dress, white lace gloves, white lace parasol, lower body of smooth glossy grey insect carapace shaped like a long bustle gown, slender soft fuzzy insect limbs at her waist, elegant curvy feminine body, large breasts",
          "name": "the brown-haired lady with a white lace parasol",
          "pose": "holding an open white lace parasol over her shoulder, the other lace-gloved hand at her lips, refined haughty smile, sparkling golden scales drifting from the parasol, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": BUG_NEG},
   "e2": {"type": "woman", "jp": "マダムアンブレラ",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, pale platinum hair, long wavy hair, golden eyes, purple noble dress, scylla, purple octopus tentacles below the waist, suction cups, holding a huge open purple umbrella, elegant curvy feminine body, large breasts",
          "name": "the platinum-haired scylla lady under a huge purple umbrella",
          "pose": "standing under her huge open purple umbrella, one purple tentacle raised playfully, finger at her chin, teasing elegant smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": TEN_NEG},
   "e3": {"type": "woman", "jp": "メイドスキュラ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, dark violet hair, short bob, grey eyes, white maid headdress, black maid dress, white apron, scylla, smooth pink tentacles below the waist without suction cups, slender curvy feminine body, large breasts",
          "name": "the violet-bob scylla maid in a black maid dress",
          "pose": "hands folded at her apron, one pink tentacle holding a silver teapot, another pink tentacle holding a white teacup on a saucer, brisk composed faint smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": TEN_NEG},
   "boss": {"type": "woman", "jp": "キャンディ",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, very tall, golden blonde hair, huge drill curls, pink eyes, golden crown, full glossy lips, bodice decorated with candies, enormous ball gown skirt made of sponge cake and whipped cream and marshmallows in place of legs, body made of sweets, soft voluptuous feminine body, huge breasts",
            "name": "the blonde queen of sweets with a crown and a giant cake skirt",
            "pose": "both hands lifting the edge of her enormous cake skirt in a curtsy, whipped cream on one fingertip, cheerful bouncy smile, looking at viewer",
            "height_note": "she is very tall and much taller than him",
            "neg": CANDY_NEG},
 },
 "places": {
   "entrance": "entrance of the ladies' village, white stone pavement, white lace banners fluttering in the wind",
   "teashop":  "village tea shop interior, white tables, silver tea set, plate of baked sweets, a jar of cream, a quiet seat at the back",
   "mansion":  "guest room of a village mansion, polished wooden floor, white bed, armchair, tea table by the window",
   "kitchen":  "mansion kitchen, copper kettles steaming, shelves of tea tins without text, a wooden chair in the corner",
   "road":     "road up the green hill, wildflowers by the roadside, breeze",
   "hill":     "scenic hilltop with a wide view, windmills turning, flower field, a forgotten umbrella lying open on the grass",
   "gazebo":   "garden gazebo in the rain, rain on the roof, a wet long bench, grey rainy light",
   "lane":     "tree-lined lane with dappled sunlight, a white bench, sparkling golden scales drifting in the air",
   "sweets":   "garden of sweets, a house made of cake, a pond of whipped cream, sugar candy flowers",
   "rose":     "rose garden, red roses, a white table, a bench with large cushions",
   "gate":     "black iron gate of the witch's manor with a witch crest, a tea table and two chairs beside the gate",
   "hall":     "great hall of the manor, chandelier, a very long tea table with white cloth, many teacups and silver teapots",
   "study":    "manor study, shelves of grimoires, a leather sofa, window light, a tea table",
   "bedroom":  "witch's private bedroom, purple canopy bed, witch hat stand, incense burner with sweet smoke",
   "seat":     "the best seat at the head of the long tea table beside the hostess's chair, a silver bell on the table, a bedroom door behind",
 },
 "atk": {
   "m1": ("hall", "he sits at the long tea table with dazed swirling thoughts, holding out his own teacup with both hands, the witch leans close beside him pouring tea from a silver teapot, whispering at his ear, faint purple magic haze around his head, steam rising, his knees pressed together"),
   "m2": ("bedroom", "he sits on the witch's lap on the canopy bed, sunk into her soft plump body, his face buried between her gigantic breasts, one gloved hand rubbing his nipple, two bare fingers of her other hand in his anus, fingering, one purple glove lying on the bed, " + CUP),
   "m3": ("study", "on the leather sofa, the witch holds him against her huge chest and kisses him deeply, tongues, tea dripping from their lips, her bare fingers between his legs in his anus, fingering, his hands limp, " + CUP),
   "e1": ("lane", "he sits on the white bench under her parasol, golden sparkling scales falling over him, dazed blissful, the parasol lady bends over him squeezing his penis between her breasts, paizuri, her soft fuzzy limbs hugging his waist, parasol still held up, " + CUP),
   "e2": ("gazebo", "under the huge purple umbrella, he is held up by purple tentacles around his wrists and ankles, legs spread, suction cups sucking both his nipples, a smooth slender tentacle in his anus, anal, the scylla lady watching close with a teasing smile, his own penis separate, rain outside"),
   "e3": ("mansion", "he sits in the armchair with his shirt open, the scylla maid kneels close stroking his penis carefully with her hand, handjob, pink tentacles rubbing both his nipples and inner thighs, another tentacle pouring tea, another holding a white teacup to his lips"),
   "boss": ("sweets", "he is wrapped up to his chest inside the opened giant cake skirt, layers of sponge and warm whipped cream around his body, his face pressed between the queen's huge breasts, her sweet palms stroking his back, cheerful smile, his head and shoulders outside the skirt, " + CUP),
 },
 "atk_desc": {
   "m1": "the witch keeps offering one more cup until he asks for a refill himself.",
   "m2": "the witch wraps him in her soft plump body, filling his sight with her breasts while pressing inside with two fingers.",
   "m3": "the witch seals his lips with a tea-scented kiss while her fingers press inside.",
   "e1": "the parasol lady dazes him with sparkling scales and gently squeezes him between her breasts.",
   "e2": "the scylla lady plays with him under her umbrella, suckers on his nipples and a smooth tentacle inside.",
   "e3": "the scylla maid serves him with her hand and pink tentacles while pouring tea at the same time.",
   "boss": "the queen of sweets wraps him inside her warm cake skirt and hugs his face to her sweet breasts.",
 },
 "lose": {
   # アラディア 技1（コンフューズ＋★）
   "btl_m1":     ("hall", "he sits on the witch's lap at the long tea table, sunk into her soft plump body, his face half buried in her gigantic breasts, holding out his teacup, one gloved hand rubbing his nipple, two bare fingers in his anus, fingering, a silver spoon with a witch crest on the saucer, cum dripping untouched"),
   "onani_m1":   ("study", "sitting alone on the leather sofa, sipping tea from a white teacup with a dazed look, his other hand inside his open shirt rubbing his own nipple, tea rippling in the cup, penis untouched, the witch watches far away from the doorway"),
   "inochi_m1":  ("gate", "he sits at the tea table beside the black gate, many empty saucers stacked, the witch stands behind him hugging his head into her huge soft chest, pouring another cup with her gloved hand, his hand reaching for the cup, the gate open behind them, dazed smile"),
   "onedari_m1": ("seat", "he sits in the best seat wrapped in the witch's arms from the side, his whole body sunk into her plump soft body, her breasts covering his eyes, her gloved hand tilting a teacup to his lips, her other hand on his nipple, a silver bell on the table, cum dripping untouched"),
   # アラディア 技2（★ヘブンズバスト）
   "btl_m2":     ("bedroom", "on the purple canopy bed, he lies on top of the witch sunk into her soft plump body, his face buried deep between her gigantic breasts, her thick thighs around his hips, one gloved hand pinching his nipple, two bare fingers deep in his anus, fingering, one purple glove on the pillow, cum on her belly"),
   "onani_m2":   ("rose", "kneeling alone on the garden bench with his face buried in a large cushion, one hand under his chest rubbing his own nipple, a finger of the other hand in his own anus, penis untouched, a teacup rippling on the white table, the witch watches far away behind the roses"),
   "inochi_m2":  ("hall", "he lies drowsy on a couch beside the long table, wrapped in the witch's arms and thighs like layers of soft quilts, his face buried in her breasts, her gloved hand stroking his hair, her other hand's fingers in his anus, fingering, " + CUP + ", cum dripping"),
   "onedari_m2": ("bedroom", "he sits between the witch's thighs on the canopy bed leaning back into her plump soft body, her breasts resting on his shoulders around his head, one gloved hand rolling his nipple, two bare fingers in his anus, fingering, he trembles, cum on his stomach, " + CUP),
   # アラディア 技3（お茶会の口づけ＋★）
   "btl_m3":     ("bedroom", "on the canopy bed, the witch holds him against her huge breasts and kisses him deeply, tongues, tea-colored saliva trail, two bare fingers pressing in his anus, fingering, a silver bell on the bedside table, cum dripping untouched"),
   "onani_m3":   ("study", "standing alone by the study window, sucking two of his own tea-wet fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, a teacup rippling on the windowsill, the witch watches far away from behind the bookshelves"),
   "inochi_m3":  ("gate", "at the open black gate, the witch bends down holding his chin with her gloved hand and kisses him, tea on their lips, her other arm pulling him into her soft plump body, his feet turned toward the manor, a teacup in his hand, knees trembling"),
   "onedari_m3": ("seat", "at the best seat, he sits sideways on the witch's lap, the witch kisses him long and deeply, tongues, her huge breasts pressed around his chest, her bare fingers deep in his anus, fingering, a silver bell and a teacup on the table, cum dripping"),
   # マダムインセクト
   "btl_e1":     ("lane", "he lies back on the white bench under the parasol, golden sparkling scales falling on his face, blissful dazed, the parasol lady squeezes his penis between her breasts, paizuri, her soft fuzzy limbs holding his hips, a lace-gloved fingertip on his nipple, a lace parasol charm on his wrist, cum on her breasts"),
   "onani_e1":   ("road", "crouching alone behind roadside flowers, pressing his face into the blossoms and breathing in the scent, dazed, one hand rubbing his own nipple through his open shirt, penis untouched, a teacup on the grass, the parasol lady watches far away up the road"),
   "inochi_e1":  ("lane", "he walks unsteadily along the lane arm in arm with the parasol lady under her white lace parasol, golden scales falling on him, blissful dazed smile, her lace-gloved hand inside his open shirt tracing his nipple, the same white bench behind them, a teacup in his hand"),
   "onedari_e1": ("lane", "he sits on the ground before the bench hugged by her soft fuzzy limbs, breathing in deeply the golden scales from the tilted parasol, the parasol lady squeezes his penis between her breasts, paizuri, holding still, refined smile, cum dripping, " + CUP),
   # マダムアンブレラ
   "btl_e2":     ("gazebo", "under the huge purple umbrella on the long bench, purple tentacles wrap his wrists and ankles, legs lifted, suction cups sucking both his nipples, a smooth slender tentacle deep in his anus, anal, the scylla lady leans over him smiling, a purple umbrella charm on his neck, his own penis separate, cum on his stomach untouched"),
   "onani_e2":   ("hill", "kneeling alone hidden under the forgotten open umbrella on the grass, one hand reaching behind with a wet finger in his own anus, penis untouched, a teacup rippling on the grass, a purple tentacle tip peeking far away beyond the umbrella ribs, the scylla lady watches from afar"),
   "inochi_e2":  ("gazebo", "heavy rain outside the gazebo, he sits on the wet bench pulled close under the huge purple umbrella, purple tentacles around his waist and thighs, suction cups sucking his nipples through his open shirt, the scylla lady resting her chin on his shoulder, he no longer looks at the rain, " + CUP),
   "onedari_e2": ("gazebo", "under the huge purple umbrella, five purple tentacles hold him up, two sucking his nipples with suction cups, two around his thighs spreading his legs, one smooth tentacle deep in his anus, anal, the scylla lady giggling close, his own penis separate, cum dripping untouched"),
   # メイドスキュラ
   "btl_e3":     ("mansion", "he sits in the armchair with his shirt open, the scylla maid kneels stroking his penis carefully from base to tip, handjob, pink tentacles rubbing his nipples and inner thighs, one tentacle pouring tea, one holding a teacup to his lips, a white apron ribbon tied on his wrist, cum on her hand"),
   "onani_e3":   ("kitchen", "standing alone in the kitchen corner, pouring tea from a teapot into a white teacup with one hand, the other hand inside his shirt rubbing his own nipple, tea spilling a little, penis untouched, the scylla maid watches far away from the doorway"),
   "inochi_e3":  ("mansion", "morning light in the guest room, he lies in the white bed hugged from behind by pink tentacles around his chest and thighs, tentacle tips stroking his nipples, the scylla maid beside the bed pouring tea with another tentacle, his travel bag neatly stored on a shelf, cum dripping"),
   "onedari_e3": ("mansion", "he sits on the edge of the white bed, the scylla maid kneels before him stroking his penis politely with her hand, handjob, pink tentacles wrapped around his nipples rolling them, three white teacups lined on the tea table, a tentacle pouring the third cup, cum on her hand"),
   # キャンディ
   "btl_boss":   ("sweets", "he is wrapped up to his chest inside the opened giant cake skirt, warm whipped cream and sponge layers around him, his face buried between the queen's huge breasts, her big glossy lips licking cream off his nipple, her sweet palms on his back, a candy crown charm on his neck, cum mixing in the cream"),
   "onani_boss": ("teashop", "sitting alone at the back seat of the tea shop with his shirt open, scooping cream from a jar and spreading it on his own nipples, rubbing them with creamy fingers, penis untouched, a teacup rippling on the table, the queen of sweets watches far away from across the shop"),
   "inochi_boss":("sweets", "he is wrapped to the waist in the giant cake skirt beside the cake house, mouth open waiting, the queen holds a forkful of cake to his lips with one hand, her other hand wiping cream from his mouth with a fingertip, her breasts against his shoulder, cheerful smile, " + CUP),
   "onedari_boss":("sweets", "inside the cake house on a bed of marshmallows, he is wrapped in the giant cake skirt up to his chest, cream dolloped on both his nipples, the queen bends down licking one nipple with her big tongue, her sweet palms stroking his sides and inner thighs, cum dripping in the cream"),
 },
 "lose_desc": "keeps him forever as a regular guest of the daily tea party on the hill, his white teacup never empty.",
 "onanie": {
   "master": ("rose", "kneeling on a bench with his face buried in a large cushion, one hand rubbing his own nipple, a finger of the other hand pressing his own anus, a teacup nearby, penis untouched"),
   "e1": ("road", "crouching by roadside flowers, breathing in their scent with a dazed look, rubbing his own nipple, penis untouched"),
   "e2": ("hill", "kneeling hidden under an open umbrella on the grass, a wet finger in his own anus, penis untouched"),
   "e3": ("kitchen", "pouring tea from a teapot with one hand, the other hand rubbing his own nipple under his shirt, penis untouched"),
   "boss": ("teashop", "sitting at a back table with his shirt open, spreading cream on his own nipples and rubbing them, penis untouched"),
 },
 "magic": {
   "1": (None, "hill", "a white porcelain teacup with a gold rim and a witch crest on a saucer, a silver teapot pouring tea into it, steam rising, tea brimming, close-up, cup without text"),
   "2": (None, "gate", "a shining silver bell hanging from a black iron bracket, ringing, faint sound ripples in the air, the manor behind, close-up"),
   "3": ("e1", "lane", "twirling her open white lace parasol, sparkling golden scales swirling around her in the dappled sunlight, refined knowing smile"),
   "4": (None, "teashop", "a silver plate of freshly baked sweets, madeleines and cookies, warm steam, a white lace napkin, close-up, plate without text"),
   "5": ("m", "hill", "sitting at a white tea table in the flower field, raising a silver teapot in her gloved hand, many white teacups laid out, windmills behind, gracious hostess smile"),
 },
}
