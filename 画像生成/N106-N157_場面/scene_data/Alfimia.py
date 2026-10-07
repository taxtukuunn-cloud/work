# N139 神のゲームの塔4層（Alfimia）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# 髪色：女神＝金／悪魔＝黒に紫／大淫魔＝赤／屋敷の女王＝銀の巻き髪／神官＝淡い桃色（資料に髪色の指定がないので被らない色にした）。
# 挿入は女神の指だけ（pen なし）。悪魔の騎乗位は、仰向けで動かない主人公に悪魔が跨る形（主人公は受け身）。
# 屋敷の女王の分身は「3人以上を出さない」ため本体1人だけで描く（鏡に本人の姿が映る程度）。
# 大淫魔の顔面騎乗は苦しくない（太腿の間に隙間。痛み・窒息の絵にしない）。腕輪の数字・本・壁画の文字は描かない（光として描く）。
BR = "a thin gold bracelet glowing white on his wrist"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
SIT_NEG = "choking, suffocation, pain, crushed"
DATA = {
 "code": "Alfimia",
 "world": "endless white stone tower of a game of the gods, soft white divine light, floating glowing game board, white feathers drifting, detailed background",
 "bg": "exterior of an endless white stone tower seen from below, the top lost in white light, the shadow of great wings in the upper floors, a glowing game board floating in the air without text, pale sky, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "フレイ",
         "tags": "adult woman, mature female, mature face, elegant adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, very long hair, golden eyes, halo of light as a crown, large white feathered wings, thin white and gold goddess robe, gold jewelry, bare feet, soft curvy feminine body, huge breasts, wide hips",
         "name": "the blonde winged goddess in a thin white and gold robe",
         "pose": "standing before a white throne with wings half spread, one hand at the shoulder of her robe, haughty polite smile, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "大淫魔",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, red hair, long hair, amber eyes, black bondage-style leather outfit, black garter belts, thick thighs, plump thighs, floating in the air, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the red-haired succubus in a black leather outfit",
          "pose": "floating in the air with legs crossed, one finger at her lips, sultry smile, looking down at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "屋敷の女王",
          "tags": "adult woman, mature female, mature face, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver hair, long curly hair, drill curls, red eyes, gold crown, black and red ball gown, long gloves, soft curvy feminine body, huge breasts",
          "name": "the silver-curled queen in a black and red gown",
          "pose": "standing before a large mirror that shows her own reflection, one hand raised to her mouth in a queenly laugh, proud smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "神官サキュバス",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, pale pink hair, long straight hair, pale green eyes, white veil, white and purple priestess robe with an open neckline, cleavage, thin black succubus tail with a heart-shaped tip, soft curvy feminine body, huge breasts",
          "name": "the pink-haired priestess in a white and purple robe",
          "pose": "hands folded in prayer under her chest, serene gentle smile, tail curled behind her, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "ダンタリオン",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair with purple inner color, very long hair, violet eyes, black curved horns, monocle, black formal tailcoat suit, white cravat, holding an old book without text, soft curvy feminine body, huge breasts",
            "name": "the horned demon in a black tailcoat with a monocle",
            "pose": "sitting in an armchair with legs crossed, an open old book without text in one hand, adjusting her monocle, calm knowing smile, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "entrance": "entrance of the white stone tower, cold white stone floor, towering walls fading into light above, still air",
   "foyer":    "mansion foyer, red carpet, crystal chandelier, three identical doors side by side",
   "hall":     "mansion great hall, a huge gilded mirror on the wall, red carpet, sweet haze, candelabra",
   "bedroom":  "queen's bedroom, canopy bed with silk sheets, roses in a vase, a dressing table with a mirror",
   "dorm":     "convent dormitory room, stone walls, a simple bed with a white pillow, a single candle",
   "gate4":    "fourth floor entrance, a long cushioned bench with velvet cushions, pale floating lights",
   "corridor": "aerial corridor of soft floating platforms high above a sea of clouds, gentle wind",
   "chapel":   "chapel interior, stained glass casting colored light, rows of pews, an altar, incense smoke",
   "confess":  "confessional booth, wooden lattice window, velvet kneeler, a single candle",
   "study":    "demon's study, towering bookshelves, piles of old books without text, an armchair, a thick rug, candlelight",
   "truth":    "dim chamber with a faded mural of a tower on the wall without text, low dim light, a thick rug",
   "house":    "ordinary empty house bedroom, a futon on the floor, a window with white light",
   "garden":   "garden at the top of the tower, white flowers everywhere, white light, a white marble statue of a winged goddess",
   "throne":   "white throne on white steps, a glowing game board floating in the air without text, white light",
   "barn":     "white wooden hut in the corner of the flower garden, a bed of soft clean straw, white flowers at the door",
 },
 "atk": {
   "m1": ("throne", "he kneels on the white steps looking up, the goddess stands over him with her robe slipped off one shoulder, lifting his chin with the toes of her bare foot, wings spread, haughty smile, " + BR + ", his knees trembling"),
   "m2": ("garden", "he kneels among the white flowers, the goddess sits before him wrapping her white wings around him, his penis squeezed between her breasts, paizuri, feathers brushing his back, white glow inside the wings, " + BR),
   "m3": ("garden", "he lies on his back on the white flowers, the goddess leans over him holding his chin, kissing him deeply, tongues, saliva trail, two honey-wet fingers of her other hand in his anus, fingering, her halo glowing, " + BR),
   "e1": ("corridor", "he lies on his back on a soft floating platform, the succubus sits lightly on his face with her thick thighs around his head, facesitting, reaching forward to pinch his nipple and stroke his penis, sultry smile, " + BR, {"neg": SIT_NEG}),
   "e2": ("hall", "he kneels before the huge mirror, the queen kneels in front of him with her gown neckline pulled open, his penis squeezed between her breasts, paizuri, her gloved fingers stroking his nipple, her reflection in the mirror, " + BR),
   "e3": ("chapel", "he kneels before the altar, the priestess stands holding his head, his face buried between her breasts, breast smother, puffing her breasts around his cheeks, the tip of her tail stroking his nipple, serene smile, " + BR),
   "boss": ("study", "from side, he lies limp on his back on the thick rug with arms at his sides, the demon straddles his hips with her tailcoat open, cowgirl position, sitting still, leaning down to whisper at his ear, monocle glinting, " + BR),
 },
 "atk_desc": {
   "m1": "the goddess shows off her body and makes him kneel under her bare foot.",
   "m2": "the goddess wraps him in her white wings and squeezes him between her breasts.",
   "m3": "the goddess seals his lips with a kiss while her fingers press inside him.",
   "e1": "the succubus descends onto his face and holds him between her thighs while her hands tease him.",
   "e2": "the queen embraces him and squeezes him between her breasts before her mirror.",
   "e3": "the priestess purifies him by wrapping his face in her breasts and making him confess.",
   "boss": "the demon reads his heart aloud and takes him in while sitting astride him.",
 },
 "lose": {
   # フレイ 技1（★肢体見せつけ）
   "btl_m1":     ("throne", "he kneels on the white steps looking up, the goddess stands over him with her robe fallen to her waist, wings spread, both soles of her bare feet squeezing his penis, footjob, cum on her feet, " + BR + ", haughty smile"),
   "onani_m1":   ("garden", "kneeling alone before the white goddess statue looking up, one leg pulled in, rubbing his own lower belly with the sole of his own foot, penis untouched, " + BR + ", the goddess watches far away from behind the statue"),
   "inochi_m1":  ("entrance", "he kneels on the cold white stone having turned around, looking up, the goddess stands over him with her robe slipped down, stroking his chest with the top of her bare foot, white wings filling the view, " + BR + ", cum dripping untouched"),
   "onedari_m1": ("barn", "he sits on the soft straw bed looking up, the goddess stands over him with her robe open, the sole of her bare foot resting on his lower belly, rubbing, wings folded, " + BR + ", cum dripping"),
   # フレイ 技2（女神の抱擁）
   "btl_m2":     ("garden", "he kneels among the white flowers wrapped inside the white wings of the goddess, his penis squeezed between her breasts, paizuri, feathers stroking his sides, white glow, a single white feather in his hand, cum on her breasts"),
   "onani_m2":   ("house", "lying alone wrapped in a futon blanket, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + BR + ", the goddess watches far away outside the window"),
   "inochi_m2":  ("throne", "he lies in the lap of the goddess on the white throne, her white wings closed around him like a blanket, his penis squeezed between her breasts, paizuri, morning light, his face drowsy, " + BR + ", cum on her breasts"),
   "onedari_m2": ("barn", "he sits on the lap of the goddess on the straw bed, her white wings closed around both of them, his penis squeezed between her breasts, paizuri, her fingers counting, gentle haughty smile, cum dripping"),
   # フレイ 技3（女神の口づけ）
   "btl_m3":     ("garden", "he lies on his back on the white flowers with knees raised, the goddess over him with her robe fallen, kissing him deeply, tongues, flower honey dripping from their lips, two fingers in his anus, fingering, her halo glowing, cum on his stomach"),
   "onani_m3":   ("truth", "kneeling alone before the dim mural, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, " + BR + ", the goddess watches far away in a glow from the mural"),
   "inochi_m3":  ("throne", "he kneels before the white throne with his chin raised and tongue out, the goddess bends down holding his jaw, kissing him, tongues, her halo glowing above, two fingers of her other hand in his anus, fingering, cum dripping untouched"),
   "onedari_m3": ("barn", "he stands with his back against the inside of the hut door, the goddess presses close with her robe fallen, kissing him deeply, saliva trail, two honey-wet fingers in his anus, fingering, wings wrapped around the doorway, cum dripping"),
   # 大淫魔（★顔面騎乗）
   "btl_e1":     ("corridor", "he lies on his back on a soft floating platform above the clouds, the succubus sits lightly on his face with her thick thighs around his head, facesitting, her hands reaching forward rolling his nipple and stroking his penis, a black garter band around his neck, cum on his stomach", {"neg": SIT_NEG}),
   "onani_e1":   ("gate4", "lying alone on his back on the long bench, a velvet cushion resting on his face, both hands rubbing his own nipples, penis untouched, " + BR + ", the succubus watches far away floating near the ceiling"),
   "inochi_e1":  ("corridor", "he lies on his back on the last floating platform with arms open, the succubus hovers just above lowering her thick thighs around his face, facesitting, her fingers stroking his nipple, clouds below, " + BR + ", cum dripping untouched", {"neg": SIT_NEG}),
   "onedari_e1": ("corridor", "he lies on his back on a floating platform with a blanket, the succubus sits on his face holding his head between her thick thighs, facesitting, both her hands pinching his nipples, sultry smile, wind, cum on his stomach", {"neg": SIT_NEG}),
   # 屋敷の女王（★分身の抱擁）
   "btl_e2":     ("hall", "he sits on the red carpet before the huge mirror, the queen kneels in front of him with her gown neckline open, his penis squeezed between her breasts, paizuri, both her gloved hands rolling his nipples, her reflection in the mirror, a red jewel in his hand, cum on her breasts"),
   "onani_e2":   ("bedroom", "kneeling alone before the dressing table mirror, staring at his own reflection, both hands rubbing his own left and right nipples, penis untouched, " + BR + ", the queen watches far away from the canopy bed"),
   "inochi_e2":  ("foyer", "he kneels on the red carpet before three identical doors, the queen stands behind him embracing him, her breasts against his head, both her gloved hands stroking his nipples, her shoe tip touching his penis, queenly laugh, " + BR + ", cum dripping"),
   "onedari_e2": ("hall", "he kneels facing the huge mirror watching his own reflection, the queen kneels behind him embracing him, both her gloved hands pinching his nipples, her chin on his shoulder, crown glinting, cum dripping untouched"),
   # 神官サキュバス（★浄化のパフパフ）
   "btl_e3":     ("chapel", "he kneels before the altar, the priestess holds his head with his face buried between her breasts, breast smother, her other hand wrapped around his penis, handjob, the tip of her tail stroking his nipple, a strip of white veil over his shoulder, cum on her hand"),
   "onani_e3":   ("dorm", "lying alone face down on the simple bed, his face buried in the white pillow, one hand under his chest rubbing his own nipple, lips moving in confession, penis untouched, " + BR + ", the priestess watches far away at the candle-lit door"),
   "inochi_e3":  ("confess", "he kneels on the velvet kneeler, the lattice window open, the priestess leans through holding his head, his face buried between her breasts, breast smother, candlelight, " + BR + ", his lips moving, cum dripping untouched"),
   "onedari_e3": ("chapel", "he sits on a pew, the priestess stands between his knees with hands folded in prayer around his head, his face buried between her breasts, breast smother, colored light from the stained glass, the tip of her tail on his nipple, cum dripping"),
   # ダンタリオン（★言葉責めと騎乗）
   "btl_boss":   ("study", "from side, he lies limp on his back on the thick rug with arms at his sides, the demon straddles his hips with her tailcoat open, cowgirl position, sitting still, leaning down whispering at his ear, a monocle resting on his chest, " + BR + ", cum overflowing"),
   "onani_boss": ("truth", "kneeling alone on the rug before the dim mural, rocking his hips against the rug, both hands rubbing his own nipples, lips moving, penis untouched, " + BR + ", the demon watches far away closing a book without text"),
   "inochi_boss":("truth", "from side, he lies on his back on the rug before the dim mural, the demon straddles his hips, cowgirl position, sitting still, one hand on his chest, her lips at his ear whispering, his body limp and relieved, " + BR + ", cum overflowing"),
   "onedari_boss":("study", "from side, he lies on his back on a bed made on piles of old books before the armchair, the demon straddles his hips slowly, cowgirl position, writing in an open book without text with a quill, knowing smile, cum overflowing"),
 },
 "lose_desc": "keeps him forever in the tower as cherished livestock of the game of the gods, a gold bracelet glowing on his wrist.",
 "onanie": {
   "master": ("garden", "kneeling before the white goddess statue, one leg pulled in, rubbing his own lower belly with the sole of his own foot, penis untouched"),
   "e1": ("gate4", "lying on his back on the long bench with a velvet cushion on his face, rubbing his own nipples, penis untouched"),
   "e2": ("bedroom", "kneeling before the dressing table mirror, both hands rubbing his own left and right nipples, penis untouched"),
   "e3": ("dorm", "lying face down with his face buried in a white pillow, rubbing his own nipple, penis untouched"),
   "boss": ("truth", "kneeling on the rug before the dim mural, rocking his hips against the rug, rubbing his own nipples, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "a thin gold bracelet lying on a white step, soft white light shining from it, blank without text or numbers, close-up"),
   "2": ("m", "throne", "laughing aloud with one hand raised to her mouth, wings spread wide, white feathers scattering, rings of light spreading in the air"),
   "3": (None, "confess", "a wooden lattice window of a confessional glowing with warm candlelight from behind, a velvet kneeler in front, close-up, without text"),
   "4": (None, "foyer", "a red crystal perfume bottle with a gold atomizer on a table, a rose beside it, pink sweet mist drifting, bottle without text"),
   "5": (None, "throne", "a glowing white game board floating in the air with blank game pieces of light, white feathers drifting, without text or numbers"),
 },
}
