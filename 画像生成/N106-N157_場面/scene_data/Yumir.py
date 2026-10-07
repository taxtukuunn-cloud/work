# N118 六大創生魔の楽園（Yumir）画像データ。登場人物は全員20歳以上。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# ユーミール：原作は片方の角が青い氷の角 → frost-white ice horn と書く。瞳はピンク紫 → pink-violet eyes。
# ケイト・ラミー：原作は角・翼・尻尾が青緑 → jade green と書く。2人は成人の男の娘（type otoko）。
# ネコ：原作は水色の短髪 → silver-white short hair に置き換え（瞳は赤）。
# 髪色：ユーミール＝deep violet／パンドラ＝magenta-red／ケイト＝coral pink／ラミー＝pale lavender／ネコ＝silver-white。
# 挿入（pen: penis）は ユーミールのラグナロク（m3 の atk・btl・inochi・onedari）、パンドラ（atk・btl・inochi・onedari）、
# ケイト（atk・btl・inochi・onedari）だけ。独裁前立腺スイッチは掌のボタン（何も入れない）なので pen なし。ラミーとネコは後ろに触れない。
# 主人公の女装：ケイトの本（btl・inochi・onedari）は珊瑚色のフリルのドレス、m2 の btl・inochi は水色のエプロンドレス。体は変えない。
# 値札は生成りの紙に赤い紐（文字・数字は描かない）。責めに痛みはない（ブーツは乗せて押し回すだけ）。
P = {"pen": "penis"}
TAG = "blank cream paper price tags without text on a red cord around his neck"
SW = "a palm-sized round button switch"
DRESS = "a coral-pink frilled dress with white gloves and a ribbon, the dress hem lifted at the back"
APRON = "a frilled pale blue apron dress and white thighhigh socks"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
BOOT_NEG = "stomping, crushing, pain, bruise, sword drawn, blade"
DATA = {
 "code": "Yumir",
 "world": "inside a merchant's magic bag that holds a whole universe, starry night sky all around, clocks, hammers, crystals and glass bottles floating in the air, soft starlight, detailed background",
 "bg": "wide grassy plain under a vast starry sky inside a magic bag, clocks, wooden hammers, crystals and glass bottles floating and slowly turning in the air, soft starlight, distant nebula, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ユーミール",
         "tags": "adult woman, mature female, mature face, 30 years old, adult proportions, beautiful detailed eyes, very tall, long legs, deep violet hair, short hair, a red flame-like horn on one side and a frost-white ice-like horn on the other side, pink-violet eyes, purple bodysuit, long white coat with wide sleeves, several slender purple tails, soft curvy feminine body, huge breasts, wide hips",
         "name": "the violet-haired merchant in a white wide-sleeved coat",
         "pose": "holding open a large merchant bag with a starry galaxy visible inside, a clock and a glass bottle floating beside her, cheerful easygoing smile, waving one wide sleeve, looking down at viewer",
         "height_note": "she is very tall and much taller than him",
         "neg": SOFT_NEG},
   "e1": {"type": "otoko", "jp": "ケイト",
          "tags": "adult male, otoko no ko, trap, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, slender, flat chest, feminine face, coral pink hair, very long hair, ahoge, jade green curled horns, emerald green eyes, white frilled swimsuit-style outfit, red corset, dark red thigh-high boots, jade green wings, jade green tail",
          "name": "the coral-haired incubus in a red corset",
          "pose": "one hand on the hip, the other hand raised showing a ring on the finger, confident teasing smile, looking at viewer",
          "neg": "scary, fangs"},
   "e2": {"type": "otoko", "jp": "ラミー",
          "tags": "adult male, otoko no ko, trap, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, slender, flat chest, feminine face, pale lavender hair, short hair, flower hair ornament, jade green curled horns, pink eyes, off-shoulder black frilled dress, black long boots, jade green wings, jade green tail",
          "name": "the lavender-haired incubus in a black frilled dress",
          "pose": "leaning forward with one finger on the lips, the other hand waving, bright friendly smile, looking at viewer",
          "neg": "scary, fangs"},
   "e3": {"type": "woman", "jp": "長乳を盛ったネコ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver-white hair, short hair, cat ears, red eyes, wide-brimmed hat with a large white feather, musketeer coat, rapier sheathed at her hip, tall leather boots, cat tail, soft curvy feminine body, huge breasts, long heavy breasts",
          "name": "the cat-eared swordswoman in a feathered hat",
          "pose": "tipping her feathered hat with one hand in a theatrical bow, the other hand on her hip, relaxed big-sisterly grin, looking at viewer",
          "neg": SOFT_NEG + ", " + BOOT_NEG},
   "boss": {"type": "woman", "jp": "開箱のパンドラ",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, magenta-red hair, very long hair, yellow curled horns, golden eyes, large black feathered wings, glowing violet magic circle patterns on her skin, dark purple elegant dress, purple tail, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the black-winged demoness with yellow curled horns",
            "pose": "black wings half spread, one hand held out palm up as if offering a gift, a glowing violet magic circle floating above her palm, graceful calm smile, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "stall":    "open-air merchant stall in bright daylight, colorful goods, cloth sunshade, a huge open merchant bag with stars visible inside",
   "entrance": "falling through a starry void just inside the mouth of the bag, goods floating all around, no ground",
   "plain":    "grassy plain under the starry sky, clocks, hammers, crystals and bottles floating and slowly turning",
   "dango":    "dango stall with a long wooden bench, steaming pots, glossy dango skewers on plates, warm lantern light",
   "inn":      "cozy cat inn interior, fireplace with a warm fire, large cushions, a feathered hat on a hook by the front door, tall boots by the door",
   "lavender": "wide lavender field, purple flowers swaying in a gentle wind, starry sky above",
   "castle":   "great hall of a white and coral-colored castle, frilled curtains, tall mirrors, polished floor, chandeliers",
   "corridor": "castle corridor with pillars and tall windows, starlight on the floor, a window seat",
   "bedroom":  "castle bedroom, canopy bed with frilled curtains, soft pillows, candlelight",
   "dress":    "dressing room full of dresses, frills and ribbons on racks, tall mirrors, a chaise longue",
   "cosmos":   "distorted starry space with warped constellations, glowing violet magic circles floating, soft ground, pale violet mist",
   "box":      "inside the bottom of a huge box, smooth dark walls, the underside of the lid as a ceiling, one faint point of light, silence",
   "store":    "storehouse with long wooden shelves of goods with blank tags without text, wooden crates, a ladder, lamp light",
   "bed":      "huge soft futon bed floating in the middle of the starry sky, fluffy blankets, stars very close",
   "deepest":  "tiny cozy room lined with soft cloth at the very back of the bag, a round window showing stars, fluffy futon",
 },
 "atk": {
   "m1": ("plain", "he stands limp with a dango skewer at his lips, the very tall merchant wraps both arms around him inside her open white coat, his head below her chest, one of her tails patting his head, a hand-sized spray bottle in her hand, " + TAG + ", knees giving way"),
   "m2": ("plain", "he lies on his back on the grass with his knees up, the merchant kneels beside him holding up " + SW + " and pressing it with her thumb, two of her tails stroking his nipple and inner thigh, her feather-trimmed gloved hand resting on his belly, his hips arched, trembling, " + TAG),
   "m3": ("bed", "from side, he lies on his back on the big futon with legs spread, the very tall merchant over him wrapping him in her arms, her penis in his anus, anal, kissing him deeply, tongues, saliva, one of her tails stroking his nipple, his own penis separate, " + TAG, P),
   "e1": ("castle", "from side, he stands bent forward with his hands on a tall mirror, the coral-haired incubus stands behind him holding his waist, penetrating him from behind, anal, the tip of the incubus's jade green tail touching the nape of his neck with a faint glow, his own penis separate, " + TAG, P),
   "e2": ("dress", "he sits on a stool before a mirror, the lavender-haired incubus leans in kissing him on the lips, kiss, the incubus's fingertip circling his nipple, smiling eyes, his hands limp at his sides, " + TAG),
   "e3": ("inn", "he sits on a cushion before the fireplace, the cat-eared swordswoman kneels in front of him hugging his head and shoulders into her long clothed bosom, his face buried in her cleavage, her cat tail stroking his inner thigh, a sprig of silvervine in her hand, " + TAG),
   "boss": ("cosmos", "from side, he floats in the air with glowing violet rings of light around his wrists and ankles, the winged demoness behind him wrapping him in her black wings, her penis in his anus, anal, pale violet mist around his face, her fingertip tracing his nipple, his own penis separate, " + TAG, P),
 },
 "atk_desc": {
   "m1": "the merchant feeds him a sweet dango, takes his strength away and wraps him in her big body.",
   "m2": "the merchant makes his insides tremble from a distance by clicking her button switch while her tails caress him.",
   "m3": "the merchant takes him on the starry bed while kissing him deeply.",
   "e1": "the incubus links their senses with a tail tip on his neck while taking him from behind.",
   "e2": "the incubus kisses him again and again while circling his nipple.",
   "e3": "the swordswoman serves her master by wrapping his face and chest in her long bosom.",
   "boss": "the demoness holds him in the air with rings of light and gives him her gift inside her wings.",
 },
 "lose": {
   # ユーミール 技1（創生巨神の慈愛）
   "btl_m1":     ("bed", "the merchant sits on the big futon holding him on her lap wrapped in her open coat, his back against her, feeding him a dango skewer with one hand, her other hand pressing " + SW + ", one of her tails patting his head, he is limp, cum dripping untouched, " + TAG),
   "onani_m1":   ("dango", "sitting alone on the stall bench, a dango skewer in his mouth, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, the merchant watches far away through the steam"),
   "inochi_m1":  ("stall", "he sits on the rim of the huge open bag with his back to the bright daylight, the merchant crouches in front feeding him a dango, empty plates stacked beside them, her other hand pressing " + SW + ", cum dripping untouched, " + TAG),
   "onedari_m1": ("bed", "he lies limp in the middle of the big futon, three empty skewers beside him, the merchant lies next to him with one arm around him, two of her tails stroking his nipples, her thumb pressing " + SW + ", a hand-sized spray bottle on the blanket, cum on his stomach"),
   # ユーミール 技2（★独裁前立腺スイッチ）
   "btl_m2":     ("store", "he stands in front of a shelf of goods with his knees trembling, hands clutching the apron, the merchant stands behind him without touching, holding up " + SW + " and pressing it, a camera hanging from her neck, the blank tags on the shelves swaying, " + TAG, {"hero_outfit": APRON}),
   "onani_m2":   ("plain", "kneeling alone behind a floating clock, wearing feather-trimmed gloves, one gloved hand stroking his own chest, a finger of the other hand in his own anus, penis untouched, the merchant watches far away among the floating goods"),
   "inochi_m2":  ("store", "he stands beside a ladder hugging a blank ledger without text to his chest, the merchant crouches behind him, her feather-trimmed gloved hand stroking his inner thigh under the apron hem, pressing " + SW + " in her other hand, his legs trembling", {"hero_outfit": APRON}),
   "onedari_m2": ("bed", "he lies on his back on the futon, the merchant sits beside him, her feather-trimmed gloved hand stroking his nipple, her thumb clicking " + SW + ", the tip of one tail barely grazing his penis, counting smile, cum on his stomach, " + TAG),
   # ユーミール 技3（ラグナロク）
   "btl_m3":     ("bed", "from side, he lies on his back on the big futon with legs lifted, the very tall merchant over him wrapping him in her arms, her penis in his anus, anal, kissing him deeply, tongues, saliva trail, one tail stroking his nipple, his own penis separate, cum on his stomach, " + TAG, P),
   "onani_m3":   ("deepest", "curled up alone wrapped in a big fluffy blanket, sucking two of his own fingers, the other hand reaching behind with a finger in his own anus, penis untouched, the merchant watches far away at the round window"),
   "inochi_m3":  ("bed", "from side, he sits on the merchant's lap facing her on the futon, her arms wrapped around him, her penis in his anus, anal, kissing him, unmoving stars above, her tails curled around his back, his own penis separate, cum dripping", P),
   "onedari_m3": ("bed", "from side, he lies on his side cradled among her many tails, the merchant lies behind him holding him, her penis in his anus, anal, turning his face back to kiss him, blushing shy smile, his own penis separate, cum on the blanket", P),
   # ケイト（★フォビドゥンリンク）
   "btl_e1":     ("castle", "from side, he stands bent forward with his gloved hands on a tall mirror, the incubus stands behind him penetrating him, anal, the tip of the incubus's tail glowing at the nape of his neck, the incubus's hand stroking his chest through the frills, matching rings on their fingers, his own penis separate, cum dripping", {"pen": "penis", "hero_outfit": DRESS}),
   "onani_e1":   ("lavender", "kneeling alone among the lavender flowers, pressing a lavender sprig to the side of his own neck, the other hand reaching behind with a finger in his own anus, penis untouched, the incubus watches far away at the edge of the field"),
   "inochi_e1":  ("castle", "from side, in the ballroom before a tall mirror, the incubus holds his waist from behind as if dancing, penetrating him, anal, one hand raising his gloved hand in a dance pose, tail tip at the nape of his neck, his own penis separate, cum dripping", {"pen": "penis", "hero_outfit": DRESS}),
   "onedari_e1": ("dress", "from side, he lies on his back on a chaise longue among hanging dresses, the incubus kneels between his legs penetrating him, anal, the tip of the incubus's tail glowing on the side of his neck, a mirror reflecting them, his own penis separate, cum on the frills", {"pen": "penis", "hero_outfit": DRESS}),
   # ラミー（★メロメロキッス）
   "btl_e2":     ("dress", "he stands before a tall mirror, the incubus holds his cheek and kisses him deeply, tongues, saliva trail, the incubus's other hand pinching his nipple, a flower hair ornament tucked in his hair, cum dripping untouched, " + TAG),
   "onani_e2":   ("corridor", "standing alone behind a pillar, kissing the back of his own hand, the other hand circling his own nipple with a fingertip, penis untouched, the incubus watches far away down the corridor"),
   "inochi_e2":  ("lavender", "he kneels among the flowers holding a bundle of lavender in both arms, the incubus kneels in front kissing him lightly on the lips, kiss, one hand pinching his nipple, cum dripping untouched, " + TAG),
   "onedari_e2": ("bedroom", "he lies on his back on the canopy bed, the incubus lies over him propped on the elbows kissing him deeply, tongues, both hands circling his nipples with fingertips, cum on his stomach, " + TAG),
   # 長乳を盛ったネコ（★長い乳のご奉仕さ）
   "btl_e3":     ("inn", "he lies back on large cushions before the fireplace, the swordswoman leans over him covering his face and chest with her long heavy clothed bosom, rubbing against his nipples, her cat tail stroking his inner thigh, a white feather in his hand, cum on his stomach"),
   "onani_e3":   ("inn", "sitting alone in a corner with a blanket wrapped around his upper body, sniffing a cloth pouch of silvervine, rubbing his own nipple with the blanket edge, penis untouched, the swordswoman watches far away at the door"),
   "inochi_e3":  ("inn", "at the front door under the hanging feathered hat, the swordswoman stands hugging his head into her long clothed bosom, his knees giving way, her cat tail curled around his thigh, a sprig of silvervine in her hand, cum dripping untouched, " + TAG),
   "onedari_e3": ("inn", "he lies on his back on a cushion before the fireplace, the swordswoman stands over him resting the heel of her tall boot gently on his lower belly, slowly circling, leaning down so her bosom sways above his face, relaxed grin, cum on his stomach", {"neg": BOOT_NEG}),
   # 開箱のパンドラ（★全てのものへの贈り物）
   "btl_boss":   ("cosmos", "from side, he floats in the air with glowing violet rings of light around his wrists and ankles, the demoness behind him wrapping him in her black wings, her penis deep in his anus, anal, pale violet mist around his face, a faint magic circle mark on his wrist, his own penis separate, cum dripping", P),
   "onani_boss": ("box", "kneeling alone inside a faintly glowing magic circle on the floor, one hand tracing his own nipple, a finger of the other hand in his own anus, penis untouched, the demoness watches far away in the dark with her wings folded"),
   "inochi_boss":("box", "from side, he lies on his back on the smooth floor beside the faint point of light, his skin glistening with a pale violet shimmer, the demoness over him holding still, her penis deep in his anus, anal, her wings spread above like a roof, his own penis separate, cum on his stomach", P),
   "onedari_boss":("box", "from side, he lies on his back looking up at the lid ceiling, his wrists held above his head by glowing violet rings of light, the demoness kneels between his legs, her penis in his anus, anal, breathing pale violet mist over his face, his own penis separate, cum on his stomach", P),
 },
 "lose_desc": "keeps him forever inside the merchant's bag as a cherished not-for-sale treasure, twelve blank price tags on a red cord around his neck.",
 "onanie": {
   "master": ("plain", "kneeling behind a floating clock, wearing feather-trimmed gloves, one gloved hand stroking his own chest, a finger of the other hand in his own anus, penis untouched"),
   "e1": ("lavender", "kneeling among the lavender, pressing a lavender sprig to the side of his own neck, a finger of the other hand in his own anus, penis untouched"),
   "e2": ("corridor", "standing behind a pillar, kissing the back of his own hand, the other hand circling his own nipple, penis untouched"),
   "e3": ("inn", "sitting with a blanket wrapped around his upper body, sniffing a pouch of silvervine, rubbing his own nipple with the blanket edge, penis untouched"),
   "boss": ("box", "kneeling inside a faintly glowing magic circle, one hand tracing his own nipple, a finger of the other hand in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "store", "two blank cream paper price tags without text on red cords lying on a wooden shelf, soft warm glow, close-up"),
   "2": ("m", "stall", "cupping one hand beside her mouth and calling out cheerfully, waving her other wide sleeve, big bright smile"),
   "3": (None, "plain", "a hand-sized glass spray bottle without text puffing a soft pale mist, floating in the starry air, close-up"),
   "4": (None, "dango", "three glossy honey-glazed dango skewers on a plain plate without text, steam rising, close-up"),
   "5": (None, "store", "long wooden shelves of goods with blank tags without text, a ladder, an open blank ledger without text on a crate, warm lamp light"),
 },
}
