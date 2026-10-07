# N121 夢の闘技場とカジノ（Arena）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。髪色は5人で被らせず、青・水色系は使わない。
# 挿入はフォルトゥナの魔法の光の棒だけ（指二本ほどの太さの、角のない温かい光の棒＝道具扱い pen: toy）。ハクメイは指だけ（尻尾は入れない・pen なし）。
# マギナ・ラパン・ハーモニーは後ろに触れない。観客の夢魔たちは描かない（3人以上を出さない。歓声は背景の気配だけ）。
# 責めはすべて痛みなし。光のリボンは温かく柔らかい。主人公の首には銀のチップを通したリボン。チップ・カード・時計・帳面に文字は描かない。
T = {"pen": "toy"}
CHIP = "a ribbon strung with plain silver chips without text around his neck"
RIB = "soft glowing ribbons of light binding his wrists"
ROD = "a slim smooth glowing rod of warm light held in her hand"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
DATA = {
 "code": "Arena",
 "world": "dreamlike pleasure district inside a dream world, sweet hazy soft light, pastel glow, floating sparkles, soft clouds, detailed background",
 "bg": "dream world pleasure district at night, sweet hazy blurred lights, a round stone arena and a golden casino along a lantern-lit main street, a gate decorated with a huge ribbon far away, soft clouds on the ground, signboards without text, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "フォルトゥナ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark purple hair, very long straight hair, large ribbon in her hair, tiny witch hat ornament, violet eyes, cool expressionless face, black and purple witch dress with a deep open neckline, cleavage, detached sleeves, black thighhighs, soft curvy feminine body, large breasts",
         "name": "the purple-haired witch with a large hair ribbon",
         "pose": "arms crossed under her chest, one finger raised with a small ribbon of light curling around it, cold unimpressed stare, looking down at viewer",
         "neg": SOFT_NEG + ", smile, laughing"},
   "e1": {"type": "woman", "jp": "マギナ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, crimson red hair, long wavy hair, golden eyes, small black succubus horns, gold tiara, gold and red arena queen outfit, deep cleavage, long red cape with a gold clasp, gold bracelets, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the red-haired arena queen in a red cape",
          "pose": "one hand on her hip, the other hand holding a single blank playing card between two fingers near her cleavage, teasing sweet smile, looking down at viewer",
          "neg": SOFT_NEG + ", armor, sword"},
   "e2": {"type": "woman", "jp": "ラパン",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, short hair, boyish short cut, red eyes, rabbit ear hairband, black casino dealer vest with a deep open neckline, cleavage, white cuffs, bow tie, black tight pants, small thin succubus tail, slender curvy feminine body, large breasts",
          "name": "the short-haired dealer with a rabbit ear hairband",
          "pose": "fanning a deck of blank playing cards in one hand, the other hand in her pocket, relaxed confident half smile, looking at viewer",
          "neg": SOFT_NEG + ", leotard, long hair"},
   "e3": {"type": "woman", "jp": "ハーモニー",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, long twintails, green eyes, small succubus wings, orange and yellow arena dancer outfit, bare midriff, sheer veil skirt, small golden bells on her wrists and ankles, slender curvy feminine body, medium breasts, wide hips",
          "name": "the pink-twintailed dancer with golden bells",
          "pose": "dancing on one foot with one arm raised and the other hand reaching out to invite, bells swinging, bright open-mouthed cheerful smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "ハクメイ",
            "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, silver-white hair, long hair, fox ears, amber eyes, one large fluffy white fox tail, white and red shrine maiden style outfit, wide sleeves, red hakama skirt, calm gentle expression, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the white-haired fox-eared woman in a shrine maiden outfit",
            "pose": "standing with her hands folded in her sleeves, her fluffy fox tail curled forward at her side, calm gentle smile, looking at viewer",
            "neg": SOFT_NEG + ", multiple tails"},
 },
 "places": {
   "dream":   "entrance of the dream, floor of soft clouds, sweet blurred light, distant glow",
   "street":  "main street of the pleasure district at night, colorful lanterns, signboards without text, hazy lights",
   "arch":    "arena entrance, large stone arch, drifting sand dust, a dancers' waiting bench in the shadow",
   "stage":   "round sand stage of the arena, blurred spectator stands far away filled with soft lights, sand dust in the spotlight",
   "locker":  "arena waiting room, long wooden bench, folded towels, bottles of scented oil, warm lamp",
   "royal":   "queen's viewing box overlooking the arena, luxurious couch, red canopy curtains, gold railing",
   "casino":  "casino entrance, golden doors, crystal chandelier, red carpet",
   "roulette":"roulette table, spinning wheel with a small ball, stacks of plain silver chips without text",
   "poker":   "poker table with green felt, blank playing cards without text, champagne glasses with rising bubbles",
   "vip":     "casino VIP room, red velvet sofa, dim golden light, rabbit ear ornaments on the wall",
   "gate":    "front gate of a witch's house decorated with a huge ribbon, herb garden, hazy dream sky",
   "dojo":    "training room with a wooden plank floor, a softly glowing magic circle on the floor, shelves with bottles of herbal oil, a raised master's seat",
   "kitchen": "old-fashioned kitchen, a simmering pot on the stove, rising steam, wooden shelves",
   "library": "library of magic books, tall bookshelves, a quill pen, blank parchment without text, warm candlelight",
   "room":    "small disciple's bedroom, narrow bed, a wooden pillar, a window showing the dream sky, a stopped alarm clock with a blank face on the windowsill",
 },
 "atk": {
   "m1": ("dojo", "he kneels on the magic circle with both hands placed together on the floor in front of him, face raised, shirt half unbuttoned, the witch stands over him pointing down at him with one finger, cold stare, giving a command, " + CHIP + ", his knees trembling"),
   "m2": ("dojo", "from side, he lies on his back on the glowing magic circle with knees raised, " + RIB + " and ankles to the floor, the witch kneels beside him pinching his nipple with cool fingers, her other hand pressing " + ROD + " into his anus, anal, his own penis separate, he trembles on the edge, " + CHIP, T),
   "m3": ("dojo", "from side, he sits on the floor leaning back, " + RIB + " behind his back, the witch leans over him holding his chin, kissing him deeply, tongues, saliva trail, her other hand between his legs pressing " + ROD + " into his anus, anal, his own penis separate, " + CHIP, T),
   "e1": ("royal", "he sits on the couch pulled against her, the arena queen presses his face between her huge breasts, a blank playing card tucked in her cleavage beside his cheek, her fingers rolling his nipple, teasing smile, " + CHIP + ", his arms limp"),
   "e2": ("poker", "he lies on his back on the green felt table, the dealer leans over him, her fingertips sliding across his nipple like dealing a card, her other hand resting on his penis, handjob, blank cards scattered around, half smile, " + CHIP),
   "e3": ("stage", "he stands on the sand stage held in a dance pose, the dancer presses her body against him from the front holding his raised hand, her other hand pinching his nipple, her thigh rubbing between his legs, bells swinging, cheerful smile, " + CHIP),
   "boss": ("dojo", "he lies on his side on the plank floor, the fox-eared woman kneels behind him, her large fluffy white tail brushing over his chest with the tail tip tickling his nipple, two oiled fingers of her hand in his anus, fingering, her other palm on his lower belly, " + CHIP),
 },
 "atk_desc": {
   "m1": "the witch makes him take the pose of surrender with a single cold command.",
   "m2": "the witch binds him with ribbons of light and trains his patience, pinching his nipple and pressing inside with a rod of light.",
   "m3": "the witch seals his lips with a long cold kiss while pressing a rod of light inside him.",
   "e1": "the arena queen holds his card hostage in her cleavage and smothers his face between her breasts.",
   "e2": "the dealer strokes his nipples and his penis in turn with a card-dealing touch.",
   "e3": "the dancer rubs her body against him as they dance and pinches his nipple at the finishing pose.",
   "boss": "the fox-eared woman strokes his whole body with her fluffy tail and presses the spot deep inside with her fingers.",
 },
 "lose": {
   # フォルトゥナ 技1（冷たい命令＋★拘束の修行）
   "btl_m1":     ("dojo", "he kneels undressed on the magic circle in the pose of surrender, hands together on the floor, face raised, " + RIB + ", the witch stands over him, one hand pinching his nipple, cold stare, one of her large hair ribbons tied on his wrist, cum dripping untouched, " + CHIP),
   "onani_m1":   ("library", "kneeling alone in the shadow of a bookshelf, one hand rubbing his own nipple, the other hand reaching behind with a finger in his own anus, as if obeying an order, penis untouched, the witch stands far away between the shelves watching, " + CHIP),
   "inochi_m1":  ("gate", "he kneels in front of the ribbon gate in the pose of surrender, " + RIB + ", the witch stands before him with her arms crossed, one finger raised counting, cold stare, herb garden behind, he looks up waiting, " + CHIP),
   "onedari_m1": ("dojo", "he kneels frozen on the magic circle, " + RIB + " and his chest, the witch crouches in front of him pinching both his nipples, looking down coldly, her lips slightly parted saying one word, cum dripping untouched, " + CHIP),
   # フォルトゥナ 技2（★拘束の修行）
   "btl_m2":     ("dojo", "from side, he lies on his back on the glowing magic circle, " + RIB + " and ankles spread to the floor, the witch kneels between his legs pressing " + ROD + " into his anus, anal, her other hand rolling his nipple, a bracelet of light ribbon on his wrist, his own penis separate, cum on his stomach, " + CHIP, T),
   "onani_m2":   ("room", "lying alone on the narrow bed, a cloth sash loosely wrapped around his own wrists, one finger reaching behind in his own anus, hips stopped mid-motion, penis untouched, the witch stands far away in the doorway watching, a stopped clock on the windowsill, " + CHIP),
   "inochi_m2":  ("dojo", "from side, he lies on his back on the magic circle, " + RIB + " above his head, the witch sits beside him pressing " + ROD + " into his anus, anal, her other hand tightening the ribbon on his wrist, he waits eagerly, his own penis separate, cum dripping, " + CHIP, T),
   "onedari_m2": ("dojo", "from side, he lies on his side on the magic circle, " + RIB + ", the witch kneels behind him with two oiled fingers in his anus, fingering, a quill pen and a blank record book without text floating beside her, cold calm face, cum dripping, " + CHIP),
   # フォルトゥナ 技3（姉弟子の口づけ＋★拘束の修行）
   "btl_m3":     ("dojo", "from side, he sits leaning back on the magic circle, " + RIB + " behind his back, the witch holds his chin and kisses him deeply, tongues, saliva trail, her other hand pressing " + ROD + " into his anus, anal, a tiny witch hat ornament pinned on his collar, his own penis separate, cum on his stomach, " + CHIP, T),
   "onani_m3":   ("kitchen", "crouching alone in the corner of the kitchen, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, the witch stands far away at the simmering pot looking over her shoulder, " + CHIP),
   "inochi_m3":  ("gate", "he stands in front of the ribbon gate with his face raised, " + RIB + ", the witch bends down holding his chin and kisses him, lips pressed together, her eyes turned aside coldly, herb garden, his knees giving way, " + CHIP),
   "onedari_m3": ("room", "from side, by the window with the dream sky, he lies on his back on the narrow bed, " + RIB + " above his head, the witch leans over him kissing him deeply, tongues, her other hand pressing " + ROD + " deep into his anus, anal, a stopped clock on the windowsill, his own penis separate, cum on his stomach, " + CHIP, T),
   # マギナ（★女王の人質）
   "btl_e1":     ("royal", "he kneels undressed at the couch, the arena queen sits holding his head and pressing his face between her huge breasts, a blank playing card tucked in her cleavage, her other hand rolling his nipple, a gold cape clasp on a cord around his wrist, cum dripping untouched, " + CHIP),
   "onani_e1":   ("locker", "lying alone on the long bench, his face buried between a folded pillow, both hands rolling his own nipples, penis untouched, the arena queen stands far away at the door watching with a teasing smile, " + CHIP),
   "inochi_e1":  ("stage", "he kneels undressed on the sand stage, the arena queen kneels holding him against her chest, his face between her huge breasts, her red cape wrapped around his shoulders, blurred lights of the stands far away, sand dust, cum dripping untouched, " + CHIP),
   "onedari_e1": ("royal", "he lies across the couch with his head on her lap turned to her chest, the arena queen bends over him smothering his face with her huge breasts inside her red cape, licking her fingertip and rolling his nipple, a blank card in her cleavage, cum dripping, " + CHIP),
   # ラパン（★ディーラーの手）
   "btl_e2":     ("poker", "he lies on his back undressed on the green felt table, the dealer leans over him, one hand stroking his nipple with gliding fingertips, the other hand stroking his penis, handjob, blank cards and champagne glasses around, a rabbit ear ornament tied on his wrist, cum on his stomach, " + CHIP),
   "onani_e2":   ("vip", "sitting alone on the red velvet sofa, turning over a blank playing card with one hand, the other hand stroking his own nipple, penis untouched, the dealer stands far away leaning on the door frame watching, " + CHIP),
   "inochi_e2":  ("roulette", "he bends over the edge of the roulette table, the dealer stands beside him pressing his face into her cleavage with one arm, her other hand spinning the wheel, a small ball rolling, stacks of plain chips, his knees trembling, cum dripping untouched, " + CHIP),
   "onedari_e2": ("poker", "he sits in a chair at the green felt table with his shirt open, the dealer stands behind him reaching around, both hands gliding over his nipples like dealing cards, five blank cards laid out in front of him, half smile at his ear, cum dripping untouched, " + CHIP),
   # ハーモニー（★闘技場の舞）
   "btl_e3":     ("stage", "he stands undressed on the sand stage in a dance hold, the dancer presses her chest and thigh against him, holding his raised hand, pinching his nipple at the finishing pose, whispering at his ear, a golden bell tied on his wrist, cum dripping untouched, " + CHIP),
   "onani_e3":   ("arch", "standing alone in the shadow of the stone arch, swaying as if dancing, both hands pinching his own nipples, penis untouched, the dancer peeks far away from the stage side with a surprised smile, " + CHIP),
   "inochi_e3":  ("street", "he dances under the colorful lanterns, the dancer hugs him from behind swaying together, her lips at his ear cheering, one hand on his nipple, the other stroking his inner thigh, bells ringing, his legs weak, " + CHIP),
   "onedari_e3": ("stage", "in the middle of the sand stage, he leans back into her arms, the dancer hugs him from the front rubbing her chest against his, counting on her raised fingers, her lips at his ear, her thigh between his legs, cum dripping untouched, " + CHIP),
   # ハクメイ（★尻尾の修行）
   "btl_boss":   ("dojo", "he lies on his side undressed on the plank floor, the fox-eared woman kneels behind him, her large fluffy white tail wrapped over his chest with the tip tickling his nipple, two oiled fingers deep in his anus, fingering, her fox ears standing up, a tuft of white fur tied as a charm on his wrist, cum dripping untouched, " + CHIP),
   "onani_boss": ("kitchen", "sitting alone in the corner of the kitchen, stroking his own chest with the edge of a blanket, one palm on his lower belly, a finger of the other hand in his own anus, penis untouched, the fox-eared woman stands far away at the simmering pot watching, " + CHIP),
   "inochi_boss":("gate", "he stands before the ribbon gate hugging her large fluffy white tail with both arms, the fox-eared woman stands beside him looking back with a gentle smile, the tail tip stroking his cheek, lantern lights of the main street far behind, his knees weak, " + CHIP),
   "onedari_boss":("dojo", "he lies undressed with his head on her lap, the fox-eared woman sits on the floor giving him a lap pillow, her large fluffy white tail stroking his chest and inner thighs, two oiled fingers of her hand in his anus, fingering, her tail swaying happily, cum on his stomach, " + CHIP),
 },
 "lose_desc": "keeps him asleep in the dream world forever as a live-in disciple, a ribbon with twelve silver chips around his neck.",
 "onanie": {
   "master": ("room", "lying on the narrow bed, a cloth sash loosely wrapped around his own wrists, one finger in his own anus, stopping himself, penis untouched"),
   "e1": ("locker", "lying on the bench with his face buried in a folded pillow, rolling his own nipples, penis untouched"),
   "e2": ("vip", "sitting on the red sofa turning over a blank card, stroking his own nipple, penis untouched"),
   "e3": ("arch", "swaying as if dancing in the shadow of the arch, pinching his own nipples, penis untouched"),
   "boss": ("kitchen", "stroking his own chest with the edge of a blanket, a palm on his lower belly, a finger in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "roulette", "two plain silver chips without text threaded on a satin ribbon lying on green felt, cool soft shine, close-up"),
   "2": (None, "street", "an empty lantern-lit street with a brass megaphone resting on a wooden stand, faint sound ripples in the air, signboards without text"),
   "3": ("m", "dojo", "raising one hand with long glowing ribbons of soft light spiraling out from her fingertips, cold calm stare"),
   "4": (None, "poker", "a tall champagne glass with golden bubbles rising and popping, a bottle without a label beside it, sparkling light, close-up"),
   "5": (None, "room", "an old round alarm clock with a blank face and motionless hands on a windowsill, dream sky outside the window, quiet soft light, close-up"),
 },
}
