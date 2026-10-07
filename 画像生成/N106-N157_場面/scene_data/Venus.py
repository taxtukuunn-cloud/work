# N119 娼館ヴィーナス（Venus）画像データ。登場人物は全員20歳以上。責め手5人は全員女性（ふたなりではない）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作の立ち絵は参照できないため、嬢3人の髪色・服はこのMOD用に決めたもの。
# 髪色の書き分け：レイディアス＝silver-white／アテナ＝blonde／シャトレー＝light pink／システィア＝chestnut brown／リゼ＝black。青・水色系は使っていない。
# 挿入（pen: strapon）はアテナの本だけ（atk boss・btl_boss・inochi_boss・onedari_boss）。レイディアスとリゼは指まで（pen なし）。シャトレーとシスティアは後ろに触れない。
# アテナの分身は「3人以上を出さない」ため本体1人で描く（後ろから貫きながら両手で乳首を摘む形に置き換え、もう一人は大きな鏡の映り込みで示すだけ）。
# レイディアスのヒールは丸い踵で重さを掛けない（下腹に軽く当てるだけ。痛み・跡なし）。
# シャトレーの本（e1）は主人公がフリルのドレスを着せられる（hero_outfit。体は変えない・平らな胸）。onedari だけピンクのドレス。
# 主人公の手の甲には濃い桃色のハートのスタンプ。会員カード・報告書・契約書・書類・予約表に文字は描かない。
S = {"pen": "strapon"}
HEART = "a deep pink heart-shaped stamp mark on the back of his hand"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
HEEL_NEG = "stomping, trampling, pain, bruise, wound, sharp stiletto, scary"
FRILL = "a white frilled dress with ribbons, white lace lingerie under it, flat chest, no wig"
PINK = "a pink frilled dress with ribbons, white lace lingerie under it, flat chest, no wig"
F = {"hero_outfit": FRILL}
PK = {"hero_outfit": PINK}
HN = {"neg": HEEL_NEG}
DATA = {
 "code": "Venus",
 "world": "luxurious high-class brothel in a back street at night, red carpets, red lamps, velvet curtains, sweet incense haze, silk sheets, large mirrors, detailed background",
 "bg": "reception hall of a luxurious brothel at night, red carpet, red lamps, velvet curtains, a polished reception counter with a silver handbell and a stamp pad, a long corridor of closed doors leading deeper, sweet incense haze, no humans, without text",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "レイディアス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver-white hair, very long straight hair, silver-grey eyes, glowing eyes, white and silver evening dress, white lace lingerie under the dress, white high heels, succubus, elegant, soft curvy feminine body, huge breasts, wide hips",
         "name": "the silver-haired succubus in a white and silver dress",
         "pose": "sitting on the edge of a large white bed with legs crossed, one white high heel dangling from her toes, hand at her chin, polite mocking smile, looking down at viewer with silver-grey eyes",
         "neg": SOFT_NEG + ", " + HEEL_NEG},
   "e1": {"type": "woman", "jp": "シャトレー",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, light pink hair, loosely curled long hair, innocent-looking amber eyes, long tongue, frilled rose dress, ribbons, soft slender feminine body, medium breasts",
          "name": "the pink-curled hostess in a frilled rose dress",
          "pose": "holding up a white frilled dress on a hanger toward the viewer, the other hand covering a teasing giggle, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "システィア",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, chestnut brown hair, very long hair, gentle droopy green eyes, soft cream silk gown with a sash, cleavage, soft voluptuous feminine body, gigantic breasts, wide hips",
          "name": "the chestnut-haired hostess in a soft cream gown",
          "pose": "both arms open in a welcoming embrace, the gown slightly loose at the chest, gentle sleepy smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "リゼ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, black hair, bob cut, violet eyes, black service dress, white gloves, neat attendant, soft slender feminine body, large breasts",
          "name": "the black-bob attendant in a black dress and white gloves",
          "pose": "one white-gloved hand extended as if guiding a guest, the other hand at her chest, polite service smile with a hint of mischief, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "アテナ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, very long hair, red eyes, black dominatrix bondage outfit, black leather corset, black long gloves, black thigh-high boots, queenly, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the blonde queen in a black bondage outfit",
            "pose": "standing with one hand on her hip, the other hand lifting her chin in a commanding gesture, a faint translucent mirror image of herself behind her, confident sweet smile, looking down at viewer",
            "neg": SOFT_NEG + ", whip marks, pain"},
 },
 "places": {
   "street":  "foggy back street at night, cobblestones, red lamps, a heavy door with warm light leaking out",
   "front":   "brothel reception, red carpet, polished counter, a stamp pad and a silver handbell, a blank ledger without text",
   "lounge":  "waiting lounge, velvet sofas and cushions, heavy curtains, a large wall mirror, glasses with ice on a low table",
   "hall1":   "ground floor corridor, thick red carpet, rows of closed doors, red light leaking from under the doors",
   "room1":   "private room, round bed with silk sheets, mirrored ceiling, red lamp, sweet incense",
   "room2":   "dressing room, wardrobe full of frilled dresses, dressing table, tall standing mirror, face powder and flower perfume",
   "room3":   "wide private room, huge wall mirror, black leather costumes on a rack, red lamp",
   "hall2":   "dim upstairs corridor with wooden floorboards, closed doors, a single red lamp",
   "play":    "playroom, shelves of soft toys and silk sashes, a padded cloth-covered table, mirrors on all four walls",
   "bath":    "marble bathroom, large marble bathtub full of foam, thick steam, soap bubbles",
   "bar":     "bar counter, rows of bottles, glasses with ice, a mirror behind the counter",
   "backstage": "hostesses' backstage room, rows of dressing tables with lit mirrors, dresses on racks, a back door",
   "stairs":  "narrow spiral staircase, white light from above, cold handrail, a landing",
   "inner":   "innermost room in white and silver, a large white bed, soft silver-white glow, a silver handbell hanging, no red lamps",
   "last":    "cozy windowless back room, a fluffy bed with many pillows, a silver handbell on the wall, a door locked from outside",
 },
 "atk": {
   "m1": ("inner", "he kneels on the white bed looking up, the succubus sits before him holding his chin, staring into his face with glowing silver-grey eyes, his own hands pinching his own nipples as ordered, mocking polite smile, " + HEART + ", trembling"),
   "m2": ("inner", "he lies on his back on the white bed, the succubus sits on the bed edge above him, the toe of her white high heel resting lightly on his lower belly, two oiled fingers of her hand in his anus, fingering, looking down with a mocking smile, " + HEART, HN),
   "m3": ("inner", "he lies on his back on the white bed, the succubus straddles his hips with her dress open showing white lace lingerie, grinding on him through her panties, no insertion, kissing him deeply, tongues, one oiled hand reaching behind with fingers in his anus, " + HEART),
   "e1": ("room2", "he stands in front of the tall mirror, the hostess stands close holding his cheek, her long tongue entwined with his tongue in a deep kiss, saliva, her other hand pinching his nipple through the dress, giggling eyes, " + HEART, F),
   "e2": ("room1", "he kneels on the round bed, the hostess kneels in front with her gown open at the chest, burying his face between her gigantic breasts, one hand stroking his head, the other hand stroking his nipple, gentle smile, " + HEART),
   "e3": ("room1", "he lies on his side on the round bed, the attendant sits beside him, one white glove removed, two oiled bare fingers in his anus, fingering his prostate, her gloved hand raised in a stop gesture, polite teasing smile, his penis untouched, " + HEART),
   "boss": ("room3", "from side, he stands bent forward with his hands on the huge mirror, the blonde queen stands behind him pegging his anus with her strap-on, anal, both her gloved hands reaching around pinching his nipples, her reflection in the mirror, his own penis separate, " + HEART, S),
 },
 "atk_desc": {
   "m1": "the succubus makes him touch himself with her silver gaze.",
   "m2": "the succubus trains him with the toe of her white heel and her oiled fingers.",
   "m3": "the succubus grinds on him through her lingerie while kissing him and pressing inside with her fingers.",
   "e1": "the hostess dresses him up and kisses him with her long tongue in front of the mirror.",
   "e2": "the hostess wraps his face in her breasts and strokes his nipple.",
   "e3": "the attendant politely presses his prostate and stops just before he comes.",
   "boss": "the queen takes him from behind while pinching his nipples before the great mirror.",
 },
 "lose": {
   # レイディアス 技1（白銀の瞳）
   "btl_m1":     ("inner", "he lies on his back on the white bed, one of his own hands on his own nipple, the succubus stands over him in white lace lingerie with her dress glowing and fading, glowing silver-grey eyes, her white high heel resting lightly on his lower belly, a silver handbell, cum dripping untouched, " + HEART, HN),
   "onani_m1":   ("lounge", "kneeling alone before the large wall mirror, staring at his own reflection, one hand pinching his own nipple, the other hand reaching behind to his own anus, penis untouched, " + HEART + " glowing, the succubus watches far away from behind a curtain"),
   "inochi_m1":  ("stairs", "he sits on the landing of the spiral staircase with a blank paper without text and a pen fallen beside him, his own hand on his own nipple, the succubus sits on a higher step staring down with glowing silver-grey eyes, her heel resting lightly on his lower belly, " + HEART, HN),
   "onedari_m1": ("inner", "he sits on the white bed with both hands on his own chest, pinching his own nipples, counting, the succubus sits facing him holding his chin, glowing silver-grey eyes close to his, two oiled fingers of her other hand in his anus, fingering, cum dripping"),
   # レイディアス 技2（★最終調教）
   "btl_m2":     ("inner", "he lies on his back on the white bed with legs open, the succubus sits above him, her rounded white heel resting lightly on his lower belly, two oiled fingers pressing deep in his anus, fingering, looking down with a mocking smile, a silver handbell, cum on his stomach, " + HEART, HN),
   "onani_m2":   ("hall2", "sitting alone on the floorboards against the wall, pressing the toe of his own shoe held in his hand against his own lower belly, an oiled finger of the other hand in his own anus, penis untouched, " + HEART + " glowing, the succubus watches far away down the corridor"),
   "inochi_m2":  ("inner", "he lies on his back on the white bed with a blank contract paper without text on his chest, the succubus sits above him, her rounded white heel resting lightly on his lower belly, her oiled fingers in his anus, fingering, two overlapping pink heart stamps on his hand, cum dripping", HN),
   "onedari_m2": ("last", "he lies on his back on the fluffy bed among pillows, the succubus sits beside him holding a silver key, the toe of her white heel resting lightly on his lower belly, two oiled fingers in his anus, fingering, counting smile, cum on his stomach, " + HEART, HN),
   # レイディアス 技3（素股と口づけ）
   "btl_m3":     ("inner", "he lies on his back on the white bed, the succubus straddles his hips in white lace lingerie with her dress open, grinding on him through her panties, no insertion, kissing him deeply, tongues, saliva trail, one oiled hand behind with fingers in his anus, twelve pink heart marks glowing on his hand, cum on his stomach"),
   "onani_m3":   ("room1", "kneeling alone on the round bed straddling a pillow, rubbing his hips on the pillow, sucking two of his own fingers as if kissing, penis untouched by hands, mirrored ceiling above, " + HEART + " glowing, the succubus watches far away from the doorway"),
   "inochi_m3":  ("bath", "he lies back in the foamy marble bathtub, the succubus straddles his hips in the foam wearing wet white lace lingerie, grinding on him, no insertion, kissing him, her oiled hand under the water with fingers in his anus, steam, soap bubbles, " + HEART),
   "onedari_m3": ("last", "he lies on his back on one half of the fluffy bed, the succubus straddles his hips in white lace lingerie, grinding on him through her panties, no insertion, kissing him deeply while grinding, her fingers deep in his anus behind, pillows, cum on his stomach, " + HEART),
   # シャトレー（★女装キス）
   "btl_e1":     ("room2", "he stands in front of the tall mirror with a frilled ribbon in his hair, the hostess embraces him from the side, her long tongue entwined with his tongue, deep kiss, saliva trail, her fingers rolling his nipple through the dress, his reflection in the mirror, cum dripping under the dress, " + HEART, F),
   "onani_e1":   ("backstage", "standing alone in front of a lit dressing table mirror, pinching his own nipples through the dress, lips parted, penis untouched, " + HEART + " glowing, the hostess watches far away from the doorway covering a giggle", F),
   "inochi_e1":  ("backstage", "he stands before a backstage mirror beside the back door, the hostess behind him whispering teasingly in his ear, then her long tongue at his lips, her hand pinching his nipple through the dress, his flushed reflection, " + HEART, F),
   "onedari_e1": ("room2", "he sits on the dressing table chair, the hostess leans over him holding his chin, a very long deep kiss with her long tongue, saliva trail, her other hand rolling his nipple through the pink dress, dresses in the wardrobe behind, cum dripping under the dress, " + HEART, PK),
   # システィア（★ぱふぱふ）
   "btl_e2":     ("room1", "he kneels on the round bed, the hostess kneels in front with her gown open at the chest, his face buried deep between her gigantic breasts, her hand stroking his head, her other hand stroking his nipple, their reflection in the mirrored ceiling, her gown sash around his wrist, cum dripping untouched, " + HEART),
   "onani_e2":   ("lounge", "kneeling alone by a velvet sofa, face buried in a cushion, one hand under his shirt stroking his own nipple, penis untouched, " + HEART + " glowing, the hostess watches far away from across the lounge with a gentle smile"),
   "inochi_e2":  ("lounge", "he sleepily lies on a velvet sofa, the hostess sits holding his upper body sandwiched lengthwise between her gigantic breasts with her gown open, her hand stroking his nipple, a glass with ice on the table, night outside the curtains, " + HEART),
   "onedari_e2": ("room1", "he lies in the middle of the round bed, the hostess lies over him with her gown open, his face wrapped between her gigantic breasts, swaying them, one hand stroking his head, the other stroking his nipple, counting softly, cum dripping untouched, " + HEART),
   # リゼ（★前立腺責め）
   "btl_e3":     ("room1", "he lies on his back on the round bed holding his knees, the attendant kneels between his legs, one white glove removed and tucked in his hand, two oiled bare fingers pressing deep in his anus, fingering his prostate, polite smile, his penis untouched, cum on his stomach, " + HEART),
   "onani_e3":   ("hall1", "kneeling alone in the shadow of a closed door in the corridor, an oiled finger in his own anus, holding still on the edge, biting his lip, penis untouched, " + HEART + " glowing, the attendant watches far away down the corridor"),
   "inochi_e3":  ("front", "he sits on a chair behind the reception counter with blank papers without text on his lap, the attendant crouches beside him, one white glove removed, her oiled fingers in his anus, fingering, her gloved finger raised to her lips, a stamp pad on the counter, cum dripping, " + HEART),
   "onedari_e3": ("room1", "he lies on his side on the round bed, the attendant sits behind him, two oiled bare fingers in his anus, fingering his prostate, her white-gloved hand raised in a stop gesture, teasing smile, he trembles on the edge, a blank booking sheet without text on the bedside, " + HEART),
   # アテナ（★分身の二重責め）
   "btl_boss":   ("room3", "from side, he stands bent forward with his hands on the huge mirror, the blonde queen behind him pegging his anus with her strap-on, anal, both her gloved hands reaching around pinching his nipples, her reflection in the mirror, a black collar on his neck, his own penis separate, cum dripping", S),
   "onani_boss": ("room3", "kneeling alone before the huge mirror, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, front and back at once, penis untouched, " + HEART + " glowing, the blonde queen watches far away reflected in the mirror"),
   "inochi_boss":("play", "from side, he lies face down on the padded cloth-covered table with his wrists held by soft silk sashes, the blonde queen behind him pegging his anus with her strap-on, anal, leaning to whisper in his ear, mirrors on the walls reflecting her, his own penis separate, cum dripping", S),
   "onedari_boss":("room3", "from side, he kneels on all fours on the carpet facing the huge mirror, the blonde queen kneels behind him, her strap-on deep in his anus, anal, holding still, both her gloved hands pinching his nipples, her reflection in the mirror, his own penis separate, cum dripping, " + HEART, S),
 },
 "lose_desc": "keeps him in the brothel forever as its cherished exclusive, twelve pink heart stamps filling his blank membership card without text.",
 "onanie": {
   "master": ("lounge", "kneeling before a wall mirror staring at his own reflection, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, penis untouched, " + HEART),
   "e1": ("backstage", "standing before a dressing table mirror, pinching his own nipples through the dress, penis untouched, " + HEART, F),
   "e2": ("lounge", "face buried in a velvet cushion, one hand stroking his own nipple, penis untouched, " + HEART),
   "e3": ("hall1", "kneeling in the shadow of a door, an oiled finger in his own anus, holding still on the edge, penis untouched, " + HEART),
   "boss": ("room3", "kneeling before a huge mirror, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, penis untouched, " + HEART),
 },
 "magic": {
   "1": (None, "front", "a heart-shaped rubber stamp and a pink ink pad beside a blank membership card without text with two fresh deep pink heart stamps, soft warm glow, close-up"),
   "2": (None, "inner", "a silver handbell hanging on a silk cord, faint sound ripples in the air, soft silver-white light, close-up"),
   "3": (None, "street", "a single red lamp glowing in the night fog above a heavy brothel door, hazy red halo, cobblestones, lamp without text"),
   "4": ("e3", "room1", "holding a glass vial of warm flower-scented oil in one bare hand, one white glove removed, golden oil dripping from the vial, polite smile"),
   "5": (None, "lounge", "an empty velvet sofa with cushions before a large wall mirror, heavy curtains, two glasses with ice on a low table, warm dim light"),
 },
}
