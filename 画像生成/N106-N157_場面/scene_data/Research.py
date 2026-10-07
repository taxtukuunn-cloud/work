# N156 魔の研究者たち（Research）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。不気味にせず、妖しく美しく。
# 原作は金髪が3人（塔の主・令嬢・幽霊）、緑髪が2人（合成獣・花のスライム）。同じMOD内で髪色を被らせないため、
#   塔の主＝golden blonde（直毛）／令嬢＝honey blonde（縦ロール）／幽霊＝pale platinum blonde（長い直毛）、
#   合成獣＝dark green／花のスライム＝light lime green と書き分ける。瞳に青・水色は使わない。
# 挿入は塔の主の触手の先だけ（細い触手。pen なし）。令嬢・合成獣は指のように細い触手の先でほぐすだけ。幽霊・花のスライムは後ろに触れない。
# 搾精球＝赤い花の大きなつぼみ（歯も棘もない）。光の輪・粘液・触手はすべて痛みなし。主人公の手首には白い標本の札（文字なし）。
TAG = "a palm-sized blank white tag without text strapped to his wrist"
BALL = "a huge red flower bud of soft layered petals closed around his lower body up to the waist"
RING = "warm glowing golden rings of light around his wrists and ankles"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, horror, fangs, gore"
BALL_NEG = "teeth, sharp thorns piercing skin, vore, swallowed whole, wound"
DATA = {
 "code": "Research",
 "world": "a tall research tower of monster scholars beyond a great misty swamp, red flowers and vines, glass test tubes, old books, soft dim light, detailed background",
 "bg": "top floor laboratory of a tall tower, walls decorated with red flowers and smooth thorny vines, a huge open leather book without text on a stone pedestal, a large throne-like chair, shelves of glass test tubes, a tall window showing a misty swamp of white flowers far below, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "アドラメレク",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, golden blonde hair, long straight hair, red eyes, glossy red armor plates over a red dress, long yellow ribbon-like sashes, red flowers in her hair, plant monster woman, smooth red flower-stem tentacles rising behind her, rose vine ornaments, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the golden-haired tower mistress in red armor",
         "pose": "one hand holding a large open book without text, the other hand raised with a red flower-stem tentacle curling around her fingers, haughty studious smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG + ", " + BALL_NEG},
   "e1": {"type": "woman", "jp": "キメラホムンクルス",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark green hair, medium hair, two curved horns, amber eyes, chimera woman, monster girl, large white feathered wings, slender green tentacles from her back, a smooth scaled fish tail behind her, thin golden seam lines on her skin, white lab coat over a black bodysuit, soft voluptuous feminine body, huge breasts",
          "name": "the green-haired horned chimera with white wings",
          "pose": "holding a glass test tube in one hand, white wings half spread, calm observing expression, faint smile, looking at viewer",
          "neg": SOFT_NEG + ", stitches, scars, patchwork flesh"},
   "e2": {"type": "woman", "jp": "ガイストビーネ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, pale platinum blonde hair, very long straight hair, silver-grey eyes, ghost woman, pale faintly translucent skin, white draped cloth dress, long white cloth sleeves covering her hands, faint soft glow, slender curvy feminine body, large breasts",
          "name": "the pale-blonde ghost in white cloth",
          "pose": "leaning out of an ornate old gilded picture frame with her upper body, one cloth-covered hand reaching out, quiet lonely smile, looking at viewer",
          "neg": SOFT_NEG + ", skull, corpse, rotting"},
   "e3": {"type": "woman", "jp": "ブロム娘",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, wide hips, light lime green hair, long wet hair, white flowers in her hair, yellow-green eyes, slime woman, monster girl, translucent green slime body, glossy translucent skin, white flower petals on her body like a dress, soft curvy feminine body, large breasts",
          "name": "the translucent green slime woman with white flowers in her hair",
          "pose": "standing ankle-deep in swamp water, one hand waving, clear green slime dripping from her fingers, friendly open smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "カサンドラ",
            "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, honey blonde hair, long drill hair, ringlets, violet eyes, white frilled blouse, long black skirt, black ribbon tie, monster girl, many smooth glossy yellow tentacles from under her skirt, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the drill-haired lady in a white blouse with yellow tentacles",
            "pose": "one hand raised like a conductor, yellow tentacles swaying around her like ribbons, graceful ladylike smile, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "swamp":    "edge of a great misty swamp, field of white flowers, damp earth, sweet haze",
   "shallows": "swamp shallows, ankle-deep green water, white flowers floating on the surface, warm mist",
   "mansion":  "entrance hall of an old western mansion by the swamp, wide staircase, faded carpet, candlelight",
   "music":    "music room of an old mansion, an old grand piano, sheet music without text, a velvet armchair, candelabra",
   "bedroom":  "mansion bedroom, canopy bed with lace curtains, soft pillows, dim lamp",
   "gate":     "entrance of a tall tower, glossy red armored door, red flowers, swamp mist",
   "archive":  "tower archive room, piles of old books without text, dust in the light, an old desk, quill pens",
   "gallery":  "long corridor lined with old portraits in gilded frames, cool dim air, stone floor",
   "painting": "room inside a painting, faded soft light, silent old bedroom, antique bed, painterly haze",
   "lab":      "alchemy laboratory, glass test tubes, culture tanks, design drawings without text, a padded examination table covered with soft cloth",
   "tank":     "room of glowing culture tanks, pale green light, bubbles, a chair in front of a tank",
   "observe":  "observation room with mirrored walls, a writing desk, a cloth-padded observation table",
   "corridor": "white corridor in the middle of the tower, red flower patterns on the walls, a tall window ledge",
   "top":      "top floor laboratory, red flowers and smooth thorny vine ornaments, a huge open book without text on a pedestal, a large chair",
   "specimen": "specimen room at the top of the tower, a soft wide bed, a huge book without text on a stand, red flowers, warm lamp light",
 },
 "atk": {
   "m1": ("top", "he stands before the huge open book with his shirt open, the tower mistress stands beside him reading aloud from the book, one finger pointing at his chest without touching, his nipples erect, hips trembling, embarrassed, " + TAG),
   "m2": ("observe", "from side, he sits on the padded table, " + BALL + ", the tower mistress stands over him, a smooth red tentacle curled around his nipple, a slender red tentacle tip in his anus behind him, studious smile, " + TAG, {"neg": BALL_NEG}),
   "m3": ("specimen", "he lies on his back on the soft bed, the tower mistress leans over him holding his chin, kissing him deeply, tongues, saliva trail, a slender red tentacle tip reaching between his legs to his anus, " + TAG),
   "e1": ("lab", "he lies on the padded table, " + RING + ", the chimera leans over him wrapping her white wings around him, a green tentacle curled around his nipple, her scaled fish tail stroking his inner thigh, calm observing face, " + TAG),
   "e2": ("gallery", "he stands frozen stiff before a large gilded picture frame, the ghost leans out of the frame holding his face with cloth-covered hands, long kiss, her cloth sleeve brushing his nipple, his arms still at his sides, " + TAG),
   "e3": ("shallows", "he stands in the shallows with his lower body enclosed inside the slime woman's translucent green body, visible through it, clear green slime poured over his shoulders, her translucent hands stroking his wet nipples, friendly smile, " + TAG),
   "boss": ("music", "he sits in the velvet armchair, glossy yellow tentacles gently holding his wrists and ankles and gliding over his chest, tentacle tips rubbing his nipples, the lady stands beside the piano conducting with one hand, graceful smile, " + TAG),
 },
 "atk_desc": {
   "m1": "the tower mistress reads his body's records aloud and his body reacts exactly as she reads.",
   "m2": "the tower mistress wraps his lower body in a soft red flower bud and examines him with her tentacles.",
   "m3": "the tower mistress seals his lips with a long kiss while a slender tentacle presses inside.",
   "e1": "the chimera holds him with warm rings of light and strokes him with wings, tentacle and tail at once.",
   "e2": "the ghost stops his body and gives him a long cool kiss from her picture frame.",
   "e3": "the slime woman wraps his lower body in her translucent body and coats him in sweet nectar.",
   "boss": "the lady performs a tentacle concert over his whole body.",
 },
 "lose": {
   # アドラメレク 技1（研究記録の朗読）
   "btl_m1":     ("top", "from side, he sits on the pedestal step, " + BALL + ", the tower mistress stands holding the huge open book, reading aloud, a slender red tentacle tip in his anus behind him, his nipples erect untouched, a gold clasp on the book cover, cum dripping", {"neg": BALL_NEG}),
   "onani_m1":   ("archive", "sitting alone behind piles of books, shirt open, one hand rubbing his own nipple, the other hand reaching behind to his own anus, lips moving as if whispering notes, penis untouched, the tower mistress watches far away from the doorway"),
   "inochi_m1":  ("gate", "he stands with his back against the red armored door, " + BALL + ", the tower mistress stands close writing on the tag at his wrist with a fingertip, a red tentacle stroking his neck, he cannot step away, cum dripping", {"neg": BALL_NEG}),
   "onedari_m1": ("specimen", "he lies on the soft bed with his shirt open, " + BALL + ", the tower mistress sits beside him reading from the open book, one hand raised counting, his nipples erect untouched, back arched, pleading face, cum dripping", {"neg": BALL_NEG}),
   # アドラメレク 技2（★搾精球）
   "btl_m2":     ("observe", "from side, before the mirrored wall, he sits on the padded table, " + BALL + ", the tower mistress stands behind him, red tentacles curled around both his nipples and his neck, a slender tentacle tip in his anus, a single red flower on the desk, cum dripping from the petals", {"neg": BALL_NEG}),
   "onani_m2":   ("corridor", "sitting alone on the window ledge, a soft cloth pouch pressed over his crotch, one hand rubbing his own nipple, the other hand reaching behind to his own anus, penis untouched, the tower mistress watches far away down the corridor"),
   "inochi_m2":  ("observe", "he lies on the padded observation table, " + BALL + ", the tower mistress sits at the desk beside him with a quill, a red tentacle tracing his nipple, mirrors reflecting them, he reaches toward her asking for more, cum dripping", {"neg": BALL_NEG}),
   "onedari_m2": ("specimen", "from side, he lies in the middle of the soft bed with knees raised, " + BALL + ", the tower mistress leans over him, red tentacles rolling both his nipples, a slender tentacle tip deep in his anus, pleased haughty smile, cum dripping from the petals", {"neg": BALL_NEG}),
   # アドラメレク 技3（標本の口づけ）
   "btl_m3":     ("specimen", "he lies on his back on the soft bed, the tower mistress over him kissing him deeply, tongues, saliva trail, " + BALL + ", a red tentacle stroking his nipple, a golden blank tag without text on his wrist, cum dripping", {"neg": BALL_NEG}),
   "onani_m3":   ("top", "sitting alone behind the large chair, sucking two of his own fingers as if kissing, the other hand reaching behind pressing a finger into his own anus, penis untouched, the tower mistress watches far away beside the huge book"),
   "inochi_m3":  ("top", "he sits on the tower mistress's lap in the large chair, his face tilted up offering his lips, the tower mistress holds his chin kissing him, tongues, " + BALL + ", the huge open book beside them, cum dripping", {"neg": BALL_NEG}),
   "onedari_m3": ("specimen", "from side, he lies on one half of the soft bed, the tower mistress lies over him kissing him deeply, saliva trail, a slender red tentacle tip deep in his anus, another red tentacle stroking his nipple, morning light, cum on his stomach"),
   # キメラホムンクルス（★アルケミスバインド）
   "btl_e1":     ("lab", "he lies on the padded table, " + RING + ", the chimera leans over him, her white wings wrapped around his body, a green tentacle around his nipple, her fish tail stroking his inner thigh, a slender green tentacle tip in his anus, a glowing ring bracelet, cum dripping untouched"),
   "onani_e1":   ("tank", "sitting alone on the chair before a glowing tank, his wrists loosely tied with a cord, stroking his own chest with a white quill feather, a smooth glass bottle against his inner thigh, penis untouched, the chimera watches far away behind the tanks"),
   "inochi_e1":  ("lab", "he sits on the padded table holding out both wrists by himself, a warm glowing golden ring of light closing around them, the chimera stands before him holding a test tube, one white wing stroking his cheek, calm faint smile, cum dripping"),
   "onedari_e1": ("lab", "he lies on the padded table with arms open, " + RING + ", the chimera's white wings covering his body like a blanket, a green tentacle circling his nipple, her fish tail on his inner thigh, the chimera watching his face closely, cum on his stomach"),
   # ガイストビーネ（★愛欲の接吻）
   "btl_e2":     ("gallery", "he stands frozen stiff before a large gilded picture frame, the ghost leans out of the frame with her upper body, kissing him, long kiss, saliva trail, her cloth-covered hands not touching him, a miniature old empty frame hanging from his neck cord, cum dripping untouched"),
   "onani_e2":   ("gallery", "standing alone before an old portrait, gazing up at the painting, shirt open, pinching his own nipple, lips parted, penis untouched, the ghost watches far away from inside another picture frame"),
   "inochi_e2":  ("painting", "inside the faded painted room, he stands before an old door with his hand off the handle, the ghost holds his other hand and pulls him gently back, kissing him, her cloth sleeve around his waist, soft faded light, cum dripping"),
   "onedari_e2": ("painting", "he lies on the antique bed in the faded painted room, the ghost lies beside him kissing him deeply, her cloth-covered hand rolling his nipple, her other cloth sleeve draped over his crotch, quiet smile, cum on the white cloth"),
   # ブロム娘（★花の粘液の檻）
   "btl_e3":     ("shallows", "he stands in the shallows, his lower body enclosed inside the slime woman's translucent green body, his whole upper body glistening with clear green slime, her translucent hands stroking his nipples from behind, a white flower in his hair, cum clouding inside her translucent body"),
   "onani_e3":   ("swamp", "kneeling alone hidden among the white flowers, shirt open, spreading flower nectar on his own nipple with his fingertips, rubbing it, penis untouched, the slime woman watches far away from the water"),
   "inochi_e3":  ("shallows", "he stands still in the middle of the shallows facing the far bank, translucent green slime rising from the water up to his waist, the slime woman behind him with her chin on his shoulder, her translucent hands on his chest, laughing, cum dripping"),
   "onedari_e3": ("shallows", "he lies back among floating white flowers in the shallows, covered in clear green slime, the slime woman lies over him pressing her translucent breasts against his chest, her fingers stroking his slick nipple, bright smile, cum on his stomach"),
   # カサンドラ（★触手の演奏会）
   "btl_boss":   ("music", "he sits in the velvet armchair, glossy yellow tentacles gently holding his wrists and ankles, tentacle tips rubbing both his nipples, a slender yellow tentacle tip in his anus, the lady stands at the piano conducting, a blank sheet of music without text on his lap, cum dripping untouched"),
   "onani_boss": ("bedroom", "sitting alone on the canopy bed, shirt open, humming with lips parted, stroking his own nipples in rhythm with both hands, penis untouched, the lady watches far away through the lace curtains"),
   "inochi_boss":("mansion", "in the entrance hall, he sits on the staircase steps, yellow tentacles gliding slowly all over his body, tentacle tips circling his nipples, the lady stands above him on the stairs humming with one hand raised, he reaches toward her asking for one more piece, cum dripping"),
   "onedari_boss":("music", "he sits in the velvet armchair facing a floating mirror of water that reflects him, yellow tentacles wrapped gently around his chest and thighs, a slender tentacle tip in his anus, the lady stands behind the chair with her hands on his shoulders, graceful smile, cum dripping"),
 },
 "lose_desc": "keeps him in the tower forever as the cherished final specimen, a white tag filled with twelve records on his wrist.",
 "onanie": {
   "master": ("archive", "sitting behind piles of books, a soft cloth pouch pressed over his crotch, one hand rubbing his own nipple, the other hand reaching behind to his own anus, penis untouched"),
   "e1": ("tank", "sitting on a chair, wrists loosely tied with a cord, stroking his own chest with a white quill feather, penis untouched"),
   "e2": ("gallery", "standing before an old portrait, gazing at the painting, pinching his own nipple, lips parted, penis untouched"),
   "e3": ("swamp", "kneeling among white flowers, spreading flower nectar on his own nipple and rubbing it, penis untouched"),
   "boss": ("bedroom", "sitting on the canopy bed, humming, stroking his own nipples in rhythm with both hands, penis untouched"),
 },
 "magic": {
   "1": (None, "top", "a palm-sized blank white tag without text on a thin band lying on a stone pedestal, two faint glowing red lines on it, soft red glow, close-up"),
   "2": (None, "gallery", "a long dim corridor of old portraits in gilded frames, one large empty frame glowing softly from inside, faint mist flowing out of it"),
   "3": ("e1", "lab", "holding up one hand with warm glowing golden rings of light floating above her palm, white wings half spread, calm observing smile"),
   "4": (None, "swamp", "a round glass flask without text filled with clear green glossy liquid, a cork beside it, white swamp flowers around it, sweet haze, close-up"),
   "5": (None, "top", "a huge open leather book without text on a stone pedestal, its pages turning by themselves, red flower petals drifting, soft glow"),
 },
}
