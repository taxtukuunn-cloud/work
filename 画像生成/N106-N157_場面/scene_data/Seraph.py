# N111 天界の熾天使（Seraph）画像データ。登場人物は全員20歳以上の成人。5人とも女性の天使（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（ウリエラも曲線のある体つき）。
# ガブリエラ：原作は水色の髪・水色の衣装 → pale mint hair・pale mint and white dress に置き換え（瞳は violet）。
# 金髪が3人いるので髪色を分ける：ミカエラ＝platinum blonde の長髪／ウリエラ＝orange-gold の短髪（褐色肌）／天使兵＝honey blonde の三つ編み。
# 挿入は ミカエラの光の細い棒（pen: toy）と ガブリエラのツタの先（体の外の蔦＝pen なし）だけ。サリエラ・天使兵は指だけ、ウリエラは後ろに触れない。
# 責めは痛みなし：鞭は跡を残さない・炎は火傷させない・大鎌は切らない（傷・流血・火傷は描かない）。主人公の背中には白い羽根が数枚。
T = {"pen": "toy"}
FEATHER = "a few short white feathers growing between his shoulder blades"
ROD = "a thin soft rod of warm white light, as thick as two fingers, extending from her sword hilt into his anus"
VINE = "a slender flower vine with a soft round tip wet with nectar"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, demon horns"
WHIP_NEG = "whip marks, welts, bruise, red marks, wound, pain, crying"
FIRE_NEG = "burn, burned skin, scorched, wound, pain"
SCYTHE_NEG = "cut, slashed, wound, scary, skull, grim reaper face, pain"
DATA = {
 "code": "Seraph",
 "world": "heavenly realm above a sea of clouds, endless white stone stairway of judgment, golden pillars, soft white holy light, floating white feathers, a distant bell tower, detailed background",
 "bg": "endless white stone stairway rising above a sea of clouds, each step faintly glowing, golden pillars on both sides, a distant bell tower, soft white holy light, floating white feathers, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ミカエラ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, platinum blonde hair, very long hair, golden eyes, angel, halo, six large white feathered wings, white and gold robe, gold ornaments, sword of light at her hip, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the platinum-blonde seraph with six white wings",
         "pose": "six white wings spread wide, one hand held out palm up glowing with white light, calm merciful smile, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ウリエラ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, orange-gold hair, short hair, amber eyes, angel, halo, white armor, white breastplate, mechanical wings of glowing orange flame, greatsword on her back, soft curvy feminine body, large breasts, wide hips",
          "name": "the brown-skinned seraph in white armor with flame wings",
          "pose": "greatsword resting on her shoulder, other hand on her hip, bold hearty grin, flame wings glowing, looking at viewer",
          "neg": SOFT_NEG + ", " + FIRE_NEG},
   "e2": {"type": "woman", "jp": "サリエラ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, white hair, long straight hair, red eyes, pale skin, angel, halo, black feathered wings, black bodysuit, long black scythe with a smooth dull blade, slender curvy feminine body, large breasts",
          "name": "the white-haired angel in a black bodysuit with black wings",
          "pose": "holding a long black scythe upright at her side, black wings half folded, cold quiet expression, gazing at viewer with red eyes",
          "neg": SOFT_NEG + ", " + SCYTHE_NEG},
   "e3": {"type": "woman", "jp": "天使兵",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, honey blonde hair, long single braid, green eyes, angel, halo, white feathered wings, purple breastplate, white short skirt, white thighhighs, white gloves, short riding whip, slender curvy feminine body, large breasts",
          "name": "the braided angel soldier in a purple breastplate",
          "pose": "standing at attention, tapping a short riding whip against her white-gloved palm, stern serious face, looking at viewer",
          "neg": SOFT_NEG + ", " + WHIP_NEG},
   "boss": {"type": "woman", "jp": "ガブリエラ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale mint hair, long wavy hair, flower hair ornament, violet eyes, angel, halo, white feathered wings, pale mint and white dress, long gloves, golden whip, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the mint-haired seraph with a golden whip",
            "pose": "holding a coiled golden whip in one hand, the other hand at her lips, strict yet amused smile, flower petals drifting, looking at viewer",
            "neg": SOFT_NEG + ", " + WHIP_NEG},
 },
 "places": {
   "cloud":    "entrance of clouds, soft cloud floor, cold wind, a distant bell",
   "stairs":   "white stone stairway of judgment, steps glowing one by one, no end in sight",
   "landing":  "first landing of the stairway, angel guard post, a row of white spears, white stone floor",
   "whip":     "hall of white marble, golden whips hanging on the wall, gold rings on the ceiling, sweet flowers",
   "garden":   "heavenly garden in full bloom, an arbor wrapped in flowering vines, a long bench, drowsy haze of petals",
   "gate":     "tall black gate at the back of heaven, pale white flames in braziers, cold air, dark stone floor",
   "library":  "archive of tall bookshelves, closed books without text, a white quill pen on a desk, silence",
   "forge":    "heavenly forge, glowing furnace, anvils, mechanical flame wings lined on racks, hot air",
   "forgeback":"warm shaded corner behind the forge, furnace vent, stacked white armor pieces, warm glow",
   "drill":    "training ground of white sand, racks of swords and spears, a shade tree at the edge",
   "chapel":   "cathedral with a high ceiling, colored light through stained glass, a wooden confession seat, pews",
   "spring":   "spring of softly glowing water, white flower petals on the surface, a flat stone seat at the edge",
   "bed":      "bedchamber of woven clouds, feather quilt, canopy with a small golden bell, soft light",
   "libra":    "silent hall with a giant golden balance scale, light raining down from its pans",
   "corridor": "corridor of golden pillars, six-winged crest reliefs, dazzling light",
   "throne":   "top tier of heaven, a throne of light, a bell tower behind it, a white rug beside the throne",
 },
 "atk": {
   "m1": ("libra", "he kneels before the giant golden scale bathed in light raining from its pans, the seraph stands over him with one hand under his chin, a glowing finger of her other hand in his anus, fingering, his lips parted as if confessing, " + FEATHER),
   "m2": ("corridor", "he sits leaning back against the seraph, her six white wings wrapped around him, her glowing white hand stroking his nipple, two glowing fingers of her other hand in his anus, fingering, his penis untouched, " + FEATHER),
   "m3": ("chapel", "from side, he lies on his back on a pew with knees raised, the seraph leans over him kissing him deeply, tongues, saliva, " + ROD + ", her wings spread above, his own penis separate, " + FEATHER, T),
   "e1": ("forge", "he lies pinned on his back on the forge floor, the armored seraph over him holding both his wrists above his head with one hand, her warm glowing fingers pinching and rolling his nipple, flame wings glowing around them, his skin flushed, " + FEATHER),
   "e2": ("gate", "he stands frozen before the black gate, the white-haired angel behind him resting the flat of her scythe blade on his shoulder without cutting, her cool fingers stroking his nipple, her other hand between his buttocks, fingering, " + FEATHER),
   "e3": ("landing", "he stands at attention with his shirt opened, the angel soldier taps his chest lightly with her riding whip, her white-gloved fingers pinching his nipple, stern face, counting, faint warm flush on his chest, " + FEATHER),
   "boss": ("whip", "he hangs standing with his wrists bound above his head by a golden whip tied to a ceiling ring, the mint-haired seraph stands beside him, flower vines stroking his inner thighs and nipples, " + VINE + " in his anus, his penis untouched, " + FEATHER),
 },
 "atk_desc": {
   "m1": "the seraph weighs his impurity before the golden scale and makes him confess.",
   "m2": "the seraph wraps him in six wings and purifies him with hands and fingers of light.",
   "m3": "the seraph blesses him with a deep kiss while a soft rod of light warms him inside.",
   "e1": "the armored seraph pins him down and judges his nipples with her warm fingers.",
   "e2": "the black-winged angel leaves him only two sensations and teases them with cool fingers.",
   "e3": "the angel soldier taps his chest with her whip and rolls his nipple by the rules.",
   "boss": "the mint-haired seraph hangs him by her golden whip while flower vines tease him.",
 },
 "lose": {
   # ミカエラ 技1（天秤の審判＋★天ノ悦）
   "btl_m1":     ("libra", "he kneels before the giant golden scale tilting to one side, bathed in light from its pans, the seraph kneels behind him wrapping her wings around him, two glowing fingers in his anus, fingering, a tiny golden scale pendant on his neck, cum dripping untouched, " + FEATHER),
   "onani_m1":   ("chapel", "kneeling alone in colored stained-glass light, lips moving as if confessing, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + FEATHER + " glowing, the seraph descends far away in the light"),
   "inochi_m1":  ("stairs", "he kneels on a glowing white step looking up, the seraph stands one step above holding his chin, light pouring over him, a glowing finger of her other hand in his anus, fingering, the stairway leading up into light, cum dripping, " + FEATHER),
   "onedari_m1": ("throne", "he kneels on the white rug beside the throne of light, the seraph sits on the throne leaning down, her glowing fingertip circling his nipple, two glowing fingers of her other hand in his anus, fingering, gentle approving smile, cum dripping untouched"),
   # ミカエラ 技2（★天ノ悦）
   "btl_m2":     ("corridor", "he sits in the seraph's lap leaning back, her six white wings closed around them like a cocoon, soft light inside, her glowing hand on his chest, two glowing fingers deep in his anus, fingering, one larger white feather among the feathers on his back, cum on his stomach"),
   "onani_m2":   ("spring", "kneeling alone in the shallow glowing water, a wet glowing finger of his own hand in his own anus, the other hand on the stone seat, penis untouched, " + FEATHER + ", the seraph's face reflected far away on the water"),
   "inochi_m2":  ("bed", "he lies on his side under the feather quilt on the cloud bed, the seraph lies behind him with a wing over him, her glowing hand stroking his chest, a glowing finger in his anus, fingering, soft night light, cum on the quilt, " + FEATHER),
   "onedari_m2": ("throne", "he lies on his back across the seraph's lap on the throne of light, legs parted, two glowing fingers of the seraph pressing in his anus, fingering, her other hand raised showing four fingers, bell tower behind, cum on his stomach, penis untouched"),
   # ミカエラ 技3（祝福の口づけ＋★天ノ悦）
   "btl_m3":     ("chapel", "from side, he lies on his back before the altar in stained-glass light with knees raised, the seraph over him kissing him deeply, tongues, saliva trail, " + ROD + ", her wings spread, his own penis separate, cum on his stomach, " + FEATHER, T),
   "onani_m3":   ("library", "sitting alone on the floor between bookshelves, kissing the back of his own hand, the other hand reaching behind with a finger in his own anus, penis untouched, " + FEATHER + " glowing, the seraph sets down a quill pen far away at the desk"),
   "inochi_m3":  ("corridor", "he stands with his back against a golden pillar, the seraph holds his face in both glowing hands and kisses his lips, tongues, one wing curled around his waist, a faint six-winged crest glowing on his back, knees giving way, cum dripping untouched"),
   "onedari_m3": ("bed", "from side, he lies on his back on the cloud bed under a canopy with a golden bell, the seraph over him kissing his lips, " + ROD + " deeply, her hand on his cheek, his own penis separate, cum on his stomach, " + FEATHER, T),
   # ウリエラ（★裁きの炎）
   "btl_e1":     ("forge", "he lies pinned on his back by the glowing furnace, the armored seraph straddles his thighs holding both his wrists above his head with one hand, rolling his nipple with a warm glowing fingertip, her other palm pressing his lower belly, flame wings around them, a tiny metal feather charm on his neck, cum on his stomach"),
   "onani_e1":   ("forgeback", "sitting alone in the warm corner by the furnace vent, warming his fingers in the hot air and pinching his own nipples, penis untouched, " + FEATHER + " glowing, the armored seraph watches far away at the forge door"),
   "inochi_e1":  ("drill", "he lies on his back on the white sand, the armored seraph sits astride his hips pressing him down with her weight, grinding, one hand pinning his wrists above his head, the other rolling his nipple, a dropped wooden sword beside them, bold grin, cum dripping"),
   "onedari_e1": ("drill", "under the shade tree at the edge of the training ground, he lies wrapped in the seraph's warm flame wings, the armored seraph beside him pinching both his nipples with warm fingers, blowing hot breath on them, his back arched, cum on his stomach, penis untouched"),
   # サリエラ（★罪と罰）
   "btl_e2":     ("gate", "he lies limp on his back on the dark stone before the black gate, the white-haired angel kneels beside him, the flat of her scythe blade resting on his arm without cutting, her cool fingers on his nipple, two fingers of her other hand in his anus, fingering, one black feather among the white feathers on his back, cum dripping untouched"),
   "onani_e2":   ("library", "sitting alone against a bookshelf, head tilted back, one hand stroking his own nipple, the other hand reaching behind to his own anus, the rest of his body slack, penis untouched, the white-haired angel watches far away between the shelves with her scythe"),
   "inochi_e2":  ("gate", "he stands in the open black gate unable to speak, lips parted soundlessly, the white-haired angel in front of him gazing into his face with glowing red eyes, one hand stroking his nipple, the other reaching behind him, fingers in his anus, pale white flames, cum dripping"),
   "onedari_e2": ("gate", "he kneels before the black gate with lips parted soundlessly, the white-haired angel kneels behind him, her black wings around him, pinching his nipple with cool fingers, a finger of her other hand stopped at his anus, teasing, he trembles on the edge, pale white flames"),
   # 天使兵（★愛の鞭）
   "btl_e3":     ("landing", "he stands with his hands behind his head before the row of white spears, the angel soldier stands close rolling his nipple between white-gloved fingers, her riding whip resting lightly on his inner thigh, stern face, a single white glove tucked at his waist, cum dripping untouched, " + FEATHER),
   "onani_e3":   ("cloud", "kneeling alone on the soft cloud floor, patting his own chest lightly with an open palm, pinching his own nipple with the other hand, penis untouched, " + FEATHER + " glowing, the angel soldier on patrol watches far away"),
   "inochi_e3":  ("stairs", "he bends forward with his hands on a white step, his folded clothes on the step beside him, the angel soldier stands behind him, an oiled white-gloved finger in his anus, fingering, her other gloved hand reaching around to roll his nipple, stern inspecting face, cum dripping"),
   "onedari_e3": ("landing", "he stands with his arms raised, the angel soldier taps his chest lightly with her riding whip, her white-gloved hand pinching his nipple, a faint approving smile, a blank white armband without text on his arm, faint warm flush on his chest, cum dripping untouched"),
   # ガブリエラ（★黙示の神鞭）
   "btl_boss":   ("whip", "he hangs standing on tiptoe with his wrists bound above his head by a golden whip tied to a ceiling ring, the mint-haired seraph stands behind him cracking a second golden whip in the air, flower vines curling on his inner thighs and nipples, " + VINE + " in his anus, a golden tassel bracelet on his wrist, cum dripping untouched"),
   "onani_boss": ("garden", "sitting alone on the arbor bench, a flower vine wound around his own wrist, rubbing his own nipple, the other hand reaching behind to his own anus, penis untouched, " + FEATHER + " glowing, the mint-haired seraph watches far away among the flowers"),
   "inochi_boss":("garden", "he lies drowsy on the grass in the middle of the flower garden, head in the mint-haired seraph's lap, the seraph holds a blooming flower to his nose, her fingers stroking his nipple, " + VINE + " in his anus, petals falling, sleepy face, cum on his stomach"),
   "onedari_boss":("whip", "he stands facing the marble wall with his wrists hooked on a gold wall bracket and bound by a golden whip, the mint-haired seraph beside him lifting his chin, a flower vine on his nipple, " + VINE + " deep in his anus, pleased smile, cum dripping untouched"),
 },
 "lose_desc": "keeps him in heaven forever as her cherished charge to be purified every day, twelve white feathers on his back.",
 "onanie": {
   "master": ("spring", "kneeling in a shaft of light by the glowing water, a wet glowing finger of his own hand in his own anus, pressing, penis untouched"),
   "e1": ("forgeback", "sitting by the furnace vent, pinching his own nipples with fingers warmed in the hot air, penis untouched"),
   "e2": ("library", "sitting against a bookshelf with his body slack, stroking only his own nipple and his own anus, penis untouched"),
   "e3": ("cloud", "kneeling on the cloud floor, patting his own chest and inner thigh lightly with his palm, pinching his own nipple, penis untouched"),
   "boss": ("garden", "sitting on the arbor bench, a flower vine wound around his own wrist, rubbing his own nipple and reaching behind to his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "a great golden bell hanging in a white bell tower, soft rings of light spreading from it, white feathers drifting, bell without text"),
   "2": ("m", "chapel", "singing a hymn with one hand on her chest, wings half spread, glowing notes of light rising, serene face"),
   "3": ("e2", "gate", "one hand lifted beside her glowing red eye, darkness spreading softly around her like mist, black feathers drifting, cold calm face"),
   "4": (None, "garden", "a cluster of pale pink flowers releasing a soft drowsy haze, petals drifting, a golden censer on the arbor bench, close-up"),
   "5": (None, "stairs", "the endless white stairway seen from below, three steps glowing brighter than the others, golden pillars, a single white feather on the lowest step"),
 },
}
