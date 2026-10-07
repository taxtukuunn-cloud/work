# N89 花嫁修業（Bride）画像データ。登場人物は全員20歳以上。女性＋ニューハーフ（リュシエンヌ・アルベルティーヌ＝NH）。
# 女装あり：主人公は28本すべて純白の花嫁のドレス（ウィッグなし）。挿入はアルベルティーヌ（花婿役）だけ。修了証書・誓約書・名簿は文字なし。
DRESS = ("a pure white wedding dress with a bare-shoulder bodice, thin lace at the chest and a skirt flaring from the waist, "
         "a sheer white veil, white elbow-length gloves, white stockings, no wig")
DRESS_V = DRESS + ", the veil lifted back from his face"
DRESS_OPEN = DRESS + ", the bodice unbuttoned showing his flat chest"
DRESS_HEM = DRESS + ", the skirt hem lifted"
DRESS_ALL = DRESS + ", the bodice unbuttoned showing his flat chest, the skirt hem lifted"
SHEET = "a white bedsheet wrapped around his body like a wedding dress, a thin pillowcase cloth over his head like a veil"
DATA = {
 "code": "Bride",
 "world": "elegant western-style mansion of a bridal finishing school, victorian interior, white roses, soft warm light, detailed background",
 "bg": "elegant mansion parlor, crackling fireplace, deep green velvet long sofa, tea set on a low table, pendulum clock, lace curtains, white roses in a vase",
 "josou": "pure white wedding dress, bare shoulders, lace at the chest, flaring skirt, sheer white veil, white elbow-length gloves, white stockings, no wig",
 "chars": {
   "m":    {"type": "woman", "jp": "オルタンス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 44 years old, adult proportions, beautiful detailed eyes, very tall, long legs, voluptuous, black hair, chignon, red eyes, red lipstick, deep green long dress with a white lace collar, headmistress, huge breasts",
            "name": "the tall black-haired headmistress in a deep green dress",
            "pose": "standing with hands folded in front, elegant gentle smile, looking at viewer"},
   "e1":   {"type": "woman", "jp": "メイヴィス",
            "tags": "adult woman, mature female, mature face, 31 years old, adult proportions, beautiful detailed eyes, long legs, brown hair, hair bun, green eyes, crimson dress, white apron, sleeves rolled up, housekeeping teacher, large breasts",
            "name": "the brown-haired housekeeping teacher in a crimson dress and white apron",
            "pose": "standing with hands on her hips, warm caring smile, looking at viewer"},
   "e2":   {"type": "nh", "jp": "リュシエンヌ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, pink hair, long wavy hair, amber eyes, tight pink dress, sheer stockings, high heels, etiquette teacher, large breasts",
            "name": "the pink-haired etiquette teacher in a tight pink dress",
            "pose": "standing straight with one hand raised, strict elegant smile, looking at viewer"},
   "e3":   {"type": "woman", "jp": "ジョゼ",
            "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, red hair, twin braids, brown eyes, cream blouse, long skirt, pincushion bracelet, tape measure around her neck, seamstress, medium breasts",
            "name": "the red-braided seamstress with a tape measure",
            "pose": "standing, holding a tape measure stretched between her hands, cheerful grin, looking at viewer"},
   "boss": {"type": "nh", "jp": "アルベルティーヌ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 38 years old, adult proportions, beautiful detailed eyes, very tall, elegant, feminine body, long legs, blonde hair, long hair in an elegant updo, purple eyes, black and gold formal gown, black tailcoat jacket over her shoulders, countess, huge breasts",
            "name": "the tall blonde countess in a black and gold gown",
            "pose": "standing with a black tailcoat draped over her shoulders, confident sweet smile, looking at viewer"},
 },
 "places": {
   "classroom": "old academy classroom, rows of wooden desks, blank blackboard, afternoon sunlight through tall windows",
   "parlor":    "mansion parlor, fireplace, deep green velvet long sofa, pendulum clock, tea set",
   "office":    "headmistress's office, heavy oak desk, flower stamp and pink ink pot, blank certificate without text, portraits of brides on the wall",
   "kitchen":   "mansion kitchen, copper pots, oven, baked sweets on a tray, washing tub, tasting plates",
   "laundry":   "laundry yard, large wooden washtub with soap foam, rows of white sheets hanging and swaying in the wind",
   "bath":      "marble bathroom, clawfoot bathtub full of foam, rising steam, wet marble edges",
   "etiquette": "etiquette hall, a wall of full-length mirrors, polished wooden floor",
   "dining":    "long dining table, silver candelabras with lit candles, rows of plates and cutlery",
   "sewing":    "sewing room, dress forms, piles of fabric, pin boxes, sewing machine, a white dress with basting threads",
   "wardrobe":  "dress wardrobe room, rows of white wedding dresses on hangers, veil boxes, a low fitting platform and a tall mirror",
   "dorm":      "small dormitory bedroom at night, narrow bed with white sheets, small window, dim light",
   "chapel":    "chapel, colorful stained glass light, altar with candles and white flowers, pipe organ, aisle",
   "arbor":     "rose garden gazebo at dusk, white roses, ivy-covered pillars, small table",
   "ballroom":  "ballroom, crystal chandelier, grand piano, polished floor, mirrored walls",
   "bedroom":   "luxurious bedroom, canopy bed with silk sheets, candlestick by the pillow",
 },
 "atk": {
   "m1": ("office", "he kneels on the carpet, the headmistress holds his face buried between her huge breasts, sliding a long white glove onto his arm, the veil draped over his head, trembling", {"hero_outfit": DRESS}),
   "m2": ("wardrobe", "he stands on the low fitting platform before the tall mirror, the headmistress lowers the sheer veil over his face, the white silk of the dress glowing faintly and caressing his sides and thighs, no hands on him, trembling", {"hero_outfit": DRESS}),
   "m3": ("classroom", "he stands before the teacher's desk, the headmistress lifts his veil and kisses him deeply, tongues, her gloved fingers pinching his nipple through the open bodice", {"hero_outfit": DRESS_OPEN}),
   "e1": ("bath", "he sits in the foam-filled clawfoot tub, the housekeeping teacher kneels behind him hugging him and washing his chest in slow circles with soapy hands, foam all over, steam, blush"),
   "e2": ("etiquette", "he stands before the mirror wall, the etiquette teacher tilts his chin up with one finger and kisses him long and deep under his lifted veil, tongues, saliva trail, back straight, trembling", {"hero_outfit": DRESS_V}),
   "e3": ("sewing", "he stands on a fitting stool with the bodice opened, the seamstress wraps a soft tape measure around his chest and pulls it tight over his nipples, reading the numbers aloud, trembling", {"hero_outfit": DRESS_OPEN}),
   "boss": ("bedroom", "he sits on the silk sheets of the canopy bed, the countess sits behind him whispering into his ear, her lips at his ear, pinching both his nipples through the open bodice, trembling", {"hero_outfit": DRESS_OPEN}),
 },
 "atk_desc": {
   "m1": "the headmistress holds him to her bosom like a lady.",
   "m2": "the headmistress dresses him in a bewitched wedding dress.",
   "m3": "the headmistress teaches him the vow kiss.",
   "e1": "the housekeeping teacher teaches him the bathing lesson.",
   "e2": "the etiquette teacher teaches him a lady's kiss.",
   "e3": "the seamstress takes his measurements.",
   "boss": "the countess whispers the rules of the wedding night.",
 },
 "lose": {
   # オルタンス 技1（淑女の抱擁）
   "btl_m1":     ("office", "he kneels on the carpet with his face and veil sunk between the headmistress's huge breasts, the headmistress strokes his back, the white silk caressing his thighs, cum soaking the inside of the skirt, a blank certificate without text on the desk", {"hero_outfit": DRESS_HEM}),
   "onani_m1":   ("dorm", "kneeling alone on the narrow bed hugging a pillow to his chest and burying his face in it, stroking his own thigh through the sheet, penis untouched, the headmistress stands at the far doorway watching", {"hero_outfit": SHEET}),
   "inochi_m1":  ("parlor", "he sits on the green velvet sofa before the fireplace with his veiled face held to the headmistress's bosom, the headmistress reads a blank contract paper without text above his head, trembling", {"hero_outfit": DRESS}),
   "onedari_m1": ("chapel", "he kneels at the altar in the stained glass light, the headmistress hugs his veiled head to her huge breasts and whispers his vow into his ear, a blank vow paper without text on the altar", {"hero_outfit": DRESS}),
   # オルタンス 技2（花嫁のドレス）
   "btl_m2":     ("wardrobe", "he stands on the fitting platform before the mirror, the headmistress lowers the veil over his face, his breath misting the veil, the glowing white silk caressing him, cum dripping under the skirt", {"hero_outfit": DRESS}),
   "onani_m2":   ("dorm", "sitting alone on the narrow bed wrapped in a white sheet like a dress, stroking his own chest and thighs over the cloth, breath misting the cloth veil, penis untouched, the headmistress watches from the far doorway", {"hero_outfit": SHEET}),
   "inochi_m2":  ("office", "he sits on a chair before the oak desk with gloved hands on his knees, the headmistress spreads his skirt so the silk slides up his inner thighs, a locked white box on the desk, trembling", {"hero_outfit": DRESS_HEM}),
   "onedari_m2": ("ballroom", "he stands alone in the middle of the ballroom floor with gloved hands folded in front, his breath misting the lowered veil, reflected in the mirrored walls, the headmistress stands behind him watching, cum under the skirt", {"hero_outfit": DRESS}),
   # オルタンス 技3（誓いの口づけ）
   "btl_m3":     ("classroom", "he leans on the teacher's desk, the headmistress lifts his veil and kisses him deeply, tongues, her gloved hand pinching his nipple through the opened bodice, cum on the skirt", {"hero_outfit": DRESS_OPEN}),
   "onani_m3":   ("dorm", "kneeling alone on the narrow bed, lifting the cloth veil with one hand and puckering his lips at the dark, pinching his own nipple with the other hand, penis untouched, the headmistress watches from the far doorway", {"hero_outfit": SHEET}),
   "inochi_m3":  ("arbor", "he sits in the gazebo at dusk, the headmistress kisses him through his lowered veil, a small hourglass of pink sand on the table beside a blank contract paper without text", {"hero_outfit": DRESS}),
   "onedari_m3": ("chapel", "he kneels on the kneeler before the altar, the headmistress lifts his veil and kisses him deeply, tongues, her gloved fingers rolling his nipple through the opened bodice, candles, cum on the skirt", {"hero_outfit": DRESS_OPEN}),
   # メイヴィス（湯浴みの作法）
   "btl_e1":     ("bath", "he sits on the edge of the clawfoot tub, the housekeeping teacher hugs him tightly from the front with foamy arms, his face against her apron, soap foam on the white dress, cum under the skirt", {"hero_outfit": DRESS}),
   "onani_e1":   ("dorm", "standing alone by the washstand, his body covered in soap foam, hugging himself tightly with foamy arms, rubbing his own chest in circles, penis untouched, the housekeeping teacher watches from the far doorway"),
   "inochi_e1":  ("laundry", "he stands among the swaying white sheets, the housekeeping teacher hugs him through a hanging sheet, foam on his gloves, the washtub full of foam beside them, cum under the skirt", {"hero_outfit": DRESS}),
   "onedari_e1": ("bedroom", "he lies on the silk sheets of the canopy bed, the housekeeping teacher lies beside him hugging him to her chest, patting his back, a bar of soap by the pillow, soap foam on the skirt", {"hero_outfit": DRESS}),
   # リュシエンヌ（淑女の口づけ）
   "btl_e2":     ("etiquette", "he stands straight before the mirror wall, the etiquette teacher lifts his veil and kisses him long and deep, tongues, saliva, his knees trembling, cum under the skirt", {"hero_outfit": DRESS_V}),
   "onani_e2":   ("dorm", "sitting alone on the narrow bed, kissing the back of his own hand and sucking two of his own fingers, saliva running down his wrist, penis untouched, the etiquette teacher watches from the far doorway"),
   "inochi_e2":  ("dining", "he sits at the long candlelit dining table, the etiquette teacher beside him lifts his veil and kisses him deeply, tongues, silver candelabra, soup plate, cum under the skirt", {"hero_outfit": DRESS_V}),
   "onedari_e2": ("ballroom", "he waltzes with the etiquette teacher under the chandelier, the etiquette teacher kisses him mid-turn with his veil lifted, his skirt swirling, flushed, trembling", {"hero_outfit": DRESS_V}),
   # ジョゼ（採寸）
   "btl_e3":     ("sewing", "he stands on the fitting stool with the bodice open, the seamstress tightens a soft tape measure over his nipples, reading numbers aloud, cum on the white skirt, dress forms around", {"hero_outfit": DRESS_OPEN}),
   "onani_e3":   ("dorm", "sitting alone on the narrow bed, wrapping a thin cord around his own bare chest and pulling it tight over his nipples, whispering numbers, penis untouched, the seamstress watches from the far doorway"),
   "inochi_e3":  ("wardrobe", "he stands between rows of hanging white dresses, the seamstress tightens the tape measure around his chest over the bodice, a blank measurement sheet without text on a clipboard, trembling, cum under the skirt", {"hero_outfit": DRESS}),
   "onedari_e3": ("parlor", "he sits before the fireplace with the tape measure around his neck, the seamstress reads numbers from a blank paper without text, his nipples stiff under the bodice, cum under the skirt", {"hero_outfit": DRESS}),
   # アルベルティーヌ（初夜の心得／花婿役）
   "btl_boss":   ("bedroom", "from side, he lies on his back on the silk sheets of the canopy bed with his legs lifted, the tall countess kneels between his legs penetrating his anus with her own penis, anal, whispering into his ear, pinching his nipple, his own penis separate", {"pen": "penis", "hero_outfit": DRESS_ALL}),
   "onani_boss": ("dorm", "lying alone on the narrow bed, one hand cupped over his own ear, the other hand pinching his own nipple, lips parted, penis untouched, the countess watches from the far doorway"),
   "inochi_boss":("parlor", "from side, he kneels on the green velvet sofa gripping the backrest, the countess behind him penetrating his anus with her own penis, anal, whispering into his veiled ear, pinching his nipple, his own penis separate", {"pen": "penis", "hero_outfit": DRESS_ALL}),
   "onedari_boss":("chapel", "he kneels at the altar, the countess hugs him from behind whispering into his veiled ear, sliding a gold ring onto the ring finger of his long white glove, a blank vow paper without text on the altar, cum on the skirt", {"hero_outfit": DRESS}),
 },
 "lose_desc": "marries him off as a bride in a pure white wedding dress.",
 "onanie": {
   "master": ("dorm", "sitting on the narrow bed wrapped in a white sheet like a dress, a cloth veil over his head, stroking his own chest and thighs over the sheet, penis untouched", {"hero_outfit": SHEET}),
   "e1": ("bath", "standing by the tub covered in soap foam, hugging himself with foamy arms, rubbing his own chest in circles, penis untouched"),
   "e2": ("etiquette", "standing before the mirror, kissing the back of his own hand, sucking two of his own fingers, penis untouched"),
   "e3": ("sewing", "standing by a dress form, pulling a tape measure tight around his own chest over his nipples, penis untouched"),
   "boss": ("dorm", "lying on the narrow bed, one hand cupped over his own ear, pinching his own nipple with the other hand, penis untouched"),
 },
 "magic": {
   "1": ("m", "office", "pressing a flower-shaped stamp onto a blank certificate without text on the oak desk, pink ink pot, gentle smile"),
   "2": (None, "parlor", "a blank school brochure without text and an envelope with a wax seal without text on a tea table, white roses"),
   "3": ("boss", "chapel", "holding up a sheer white veil that floats in the air like a snare, beckoning with one finger, sweet smile"),
   "4": (None, "wardrobe", "a pure white wedding dress with a veil and long white gloves on a dress form, glowing faintly, rows of dresses behind"),
   "5": ("e1", "kitchen", "ringing a small brass hand bell, a folded white apron over her arm, warm smile"),
 },
}
