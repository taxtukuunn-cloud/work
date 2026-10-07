# N138 夢の魔法学院（Nympho）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# 舞台は大人の魔術師の研修所（夢の中の魔法学院）。学生服・制服・机の並ぶ部屋は描かない。
# サイーダ：原作は青い髪（淫魔化でピンク）→ 髪は pale mint に置き換え。淫魔化はイーヴァのピンク髪と被るので髪色は変えず、
#           「髪の先と瞳が淡いバラ色に光る」（rose glow）で表す。
# 後ろに入れるのは指だけ（イーヴァ・サイーダ）なので pen は全場面なし。学院長・ジョディー・メイリアは後ろに触れない。
# 主人公の胸には研修生の証（銀の丸いバッジ。ピンクに光る）。紙・カルテ・修了証・記録は文字なし（blank / without text）。
BADGE = "a round silver badge glowing pink on his chest"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, school uniform, serafuku, classroom desks"
DATA = {
 "code": "Nympho",
 "world": "dreamlike academy of magic for adult mages inside a dream, soft hazy light, drifting pink mist, pink sky outside the windows, detailed background",
 "bg": "dreamlike academy of magic in a pink haze, tall black iron gate with a crest, a bell tower, stone buildings for adult mages, blurry townscape far away, pink sky, drifting pink mist, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "イーヴァ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, succubus, long pink hair, curved black horns, pink eyes, black and pink evening dress, bare shoulders, thin black tail with a heart-shaped tip, bat wings, soft curvy feminine body, large breasts, narrow waist",
         "name": "the pink-haired succubus in a black and pink dress",
         "pose": "one finger at her lips, the other hand beckoning, tail swaying, teasing impish smile, looking at viewer with pink eyes",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ジョディー",
          "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, long straight black hair, narrow upturned eyes, dark brown eyes, rimless glasses, black tailored instructor jacket, black pencil skirt, black pantyhose, soft curvy feminine body, large breasts",
          "name": "the black-haired instructor with glasses",
          "pose": "adjusting her glasses with one hand, a red pen in the other hand, calm composed face, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "サイーダ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, long legs, long wavy pale mint hair, gentle droopy violet eyes, white doctor coat, cream blouse, tight skirt, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the mint-haired doctor in a white coat",
          "pose": "one hand on her chest, the other hand held out with a soft glow of healing light, gentle kind smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "メイリア",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, chestnut brown hair, loose hair bun, soft green eyes, paint-stained apron, cream blouse, long brown skirt, soft curvy feminine body, large breasts",
          "name": "the chestnut-bun painter in a paint-stained apron",
          "pose": "holding a paintbrush and a wooden palette, head tilted, shy timid smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "学院長",
            "tags": "adult woman, mature female, mature face, sharp adult features, 33 years old, adult proportions, beautiful detailed eyes, tall, long legs, long silver hair in an elegant updo, violet eyes, long black robe with a high collar, crystal pendant necklace, barefoot, bare feet, soft curvy feminine body, large breasts, wide hips",
            "name": "the silver-haired headmistress in a black robe",
            "pose": "sitting in a large armchair with her legs crossed, one bare foot extended forward, chin resting on her hand, elegant haughty smile, looking down at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "town":    "entrance of a dream town, blurry stone streets in thick pink mist, soft cobblestones, a distant bell tower",
   "gate":    "front gate of the academy, tall black iron gate with a crest, bell tower behind, pink mist at the ground",
   "hall":    "long academy corridor, tall windows showing a pink sky, a long bench under a window, stone pillars",
   "art":     "art studio, wooden easels, canvases, jars of paint and brushes, a model stand draped with cloth, smell of oil paint",
   "artprep": "art storeroom, shelves of paint jars, paintings covered with cloth, a low model stand, dim light",
   "clinic":  "infirmary, white curtains, a clean bed with a soft pillow, glass medicine bottles without text on a shelf",
   "storage": "old storeroom, old tools, dust in the light, an old bed with a blanket, a bundle of soft rope on the floor",
   "staff":   "instructors' office, a large adult office desk, papers without text, a steaming teacup, a red pen",
   "arena":   "sparring hall, wide wooden plank floor, magic practice targets, very high ceiling",
   "aula":    "grand lecture hall at night, tiered seats, a wooden stage, pink mist glowing through tall windows",
   "office":  "headmistress's office, a large desk and a high-backed armchair, crystal ornaments, a deep soft rug, window over the dream town",
   "private": "headmistress's private room, thick soft carpet, crystal lamps, incense smoke, a low couch",
   "roof":    "academy rooftop under a pink sky, a large bell, a tall crystal mirror, view over the dream town, mist flowing in the wind",
   "inner":   "bedroom deep inside the dream, a heart-shaped window, a canopy bed, thick pink mist, sweet haze",
   "throne":  "center of the dream world, a bed made of pink clouds, a throne made of clouds, pink sky all around",
 },
 "atk": {
   "m1": ("inner", "he kneels before the heart-shaped window, the succubus stands over him lifting his chin with one finger, staring down into his face with glowing pink eyes, her tail tip hovering near his chest, his body going limp, " + BADGE),
   "m2": ("throne", "he lies on his back on the cloud bed, the succubus leans over him, one hand pinching and rolling his nipple, two fingers of her other hand wet with pink nectar in his anus, fingering, her tail tip hovering over his penis without touching, teasing smile, " + BADGE),
   "m3": ("throne", "from side, he lies on the cloud bed, the succubus lies over him holding his cheek and kissing him deeply, tongues, sweet pink nectar dripping from their lips, her other hand between his legs with two fingers in his anus, fingering, " + BADGE),
   "e1": ("arena", "he stands frozen on the plank floor wrapped in faint rings of light, the instructor leans against him with her jacket collar opened, licking his nipple, her hand wrapped around his penis, handjob, calm eyes behind glasses, " + BADGE),
   "e2": ("clinic", "he sits on the infirmary bed, the doctor holds his head and buries his face between her huge breasts through her opened white coat, breast smother, a rose glow on her hair tips, her other hand glowing with soft healing light on his back, " + BADGE),
   "e3": ("art", "he sits on the model stand staring at a glowing canvas, the painter kneels in front of him painting warm pink paint on his nipple with a soft brush, her breasts pressed against his penis, gentle smile, " + BADGE),
   "boss": ("office", "he kneels on the rug in front of the armchair, the headmistress sits with her robe hem raised to her knees, both her bare soles holding his penis between them, footjob, a crystal shining soft light on his chest, haughty smile, " + BADGE),
 },
 "atk_desc": {
   "m1": "the succubus shows him her pink eyes and the dream grows deeper.",
   "m2": "the succubus waits until he begs, then strokes his nipple and presses inside with her fingers.",
   "m3": "the succubus feeds him a sweet dream kiss while her fingers press inside him.",
   "e1": "the instructor holds him still with gentle magic and spars with her hand and tongue.",
   "e2": "the doctor wraps his face in her breasts and heals him so his body stays sensitive.",
   "e3": "the painter shows him a moving picture and paints his nipple with warm paint.",
   "boss": "the headmistress educates him with her bare feet from her chair under crystal light.",
 },
 "lose": {
   # イーヴァ 技1（イーヴァの瞳）
   "btl_m1":     ("inner", "he kneels before the heart-shaped window looking up, the succubus crouches holding his chin, glowing pink eyes close to his face, her other hand pinching his nipple, an eye-shaped pink brooch beside the badge on his chest, " + BADGE + ", cum dripping untouched"),
   "onani_m1":   ("roof", "kneeling alone before the tall crystal mirror, staring at his own reflection, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + BADGE + ", the succubus watches far away from the sky"),
   "inochi_m1":  ("gate", "he kneels before the closed black iron gate, the succubus stands holding his face in both hands, glowing pink eyes staring into his, her tail tip circling his nipple, the gate stays shut, " + BADGE + ", knees trembling"),
   "onedari_m1": ("throne", "he sits at the foot of the cloud throne looking up, the succubus sits on the throne leaning down holding his chin, glowing pink eyes, her other hand reaching down with two fingers in his anus, fingering, " + BADGE + ", cum dripping"),
   # イーヴァ 技2（★おねだりの夢）
   "btl_m2":     ("throne", "he lies on his back on the cloud bed with his mouth open as if begging, the succubus leans over him rolling his nipple, two nectar-wet fingers pressing deep in his anus, fingering, her tail tip hovering over his penis, a blank sheet of paper without text in the clouds, cum on his stomach"),
   "onani_m2":   ("hall", "kneeling alone behind a stone pillar, lips moving as if begging, one hand pinching his own nipple, a wet finger of the other hand in his own anus, penis untouched, " + BADGE + ", the succubus watches far away from the window bench"),
   "inochi_m2":  ("aula", "he sits on the stage at night with his thighs pressed together, the succubus kneels behind him pinching his nipple, her fingers in his anus, fingering, pink mist through the tall windows, " + BADGE + ", cum dripping, tears of relief"),
   "onedari_m2": ("throne", "he kneels on all fours at the foot of the cloud throne, the succubus sits beside him counting on the fingers of one hand, two fingers of her other hand deep in his anus, fingering, smiling, " + BADGE + ", cum dripping untouched"),
   # イーヴァ 技3（夢の口づけ）
   "btl_m3":     ("throne", "from side, he lies on the cloud bed, the succubus over him kissing him deeply, tongues, pink nectar running from his lips, two fingers of her hand in his anus, fingering, a heart-shaped shard of pink glass in his hand, cum on his stomach"),
   "onani_m3":   ("inner", "sitting alone in the shadow of the canopy bed, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger pressing his own anus, penis untouched, " + BADGE + ", the succubus watches far away by the heart-shaped window"),
   "inochi_m3":  ("town", "he stands in thick pink mist at the town entrance leaning forward on his toes, the succubus holds his face and kisses him deeply, tongues, saliva trail, her hand behind him with fingers in his anus, fingering, " + BADGE + ", knees giving way"),
   "onedari_m3": ("throne", "he lies on the cloud bed with his arms around her neck, the succubus kisses him long and deep, sweet nectar overflowing, two fingers deep in his anus, fingering, her tail wrapped around his thigh, " + BADGE + ", cum on his stomach"),
   # ジョディー（★教官長の手合わせ）
   "btl_e1":     ("arena", "he stands frozen on the plank floor in faint rings of light, the instructor kneels before him licking the tip of his penis, her hand stroking it, handjob, her other hand pinching his nipple, spare glasses hanging on a cord at his neck, " + BADGE + ", cum on her hand"),
   "onani_e1":   ("staff", "sitting alone on the floor behind the large desk, rubbing his own nipple with one hand, lips moving as if scoring himself, penis untouched, " + BADGE + ", the instructor watches far away from the doorway"),
   "inochi_e1":  ("arena", "he stands frozen mid-step in rings of light with his arm reaching out, the instructor presses close licking his nipple carefully, her hand around his penis, handjob, sad gentle eyes behind glasses, " + BADGE + ", cum dripping"),
   "onedari_e1": ("staff", "he sits on a chair beside the desk, the instructor leans over him licking his nipple, her hand stroking his penis, handjob, a red pen and a blank score sheet without text on the desk, a steaming teacup, " + BADGE + ", cum on her hand"),
   # サイーダ（★淫魔化の誘惑）
   "btl_e2":     ("clinic", "he lies on the infirmary bed, the doctor lies beside him holding his face buried between her huge breasts through her opened white coat, breast smother, two fingers of her other hand in his anus, fingering, soft healing light, a rose glow on her hair tips, a braided cord on his wrist, cum on his stomach"),
   "onani_e2":   ("storage", "lying alone on the old bed hugging a white pillow to his chest with his face buried in it, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + BADGE + ", the doctor watches far away among the old tools"),
   "inochi_e2":  ("clinic", "he lies on the infirmary bed behind white curtains, the doctor leans over him pressing her huge breasts on his face, her glowing hand on his chest, two fingers of her other hand in his anus, fingering, a rose glow on her hair tips, " + BADGE + ", cum dripping"),
   "onedari_e2": ("clinic", "he sits on the edge of the bed hugging her waist, the doctor stands holding his face between her huge breasts, a healing glow on his nipple under her fingertip, her other hand behind him with fingers in his anus, fingering, a blank clipboard without text on the bed, cum dripping"),
   # メイリア（★動く絵）
   "btl_e3":     ("art", "he sits on the model stand staring at a glowing canvas, the painter kneels before him with his penis between her breasts under her apron, paizuri, stroking his paint-covered nipple with a brush, pink paint on his chest, " + BADGE + ", cum on her apron"),
   "onani_e3":   ("artprep", "sitting alone behind a cloth-covered painting, tracing circles on his own nipple with a fingertip as if painting, head tilted back, penis untouched, " + BADGE + ", the painter watches far away from the doorway holding a brush"),
   "inochi_e3":  ("art", "he stands on the model stand with his arms at his sides, the painter stands close painting warm pink paint on his nipple with a brush, an unfinished blank canvas on the easel, her other hand steadying his hip, " + BADGE + ", legs trembling, cum dripping"),
   "onedari_e3": ("art", "he stands before an easel staring at a glowing canvas, the painter stands behind him reaching around, spreading pink paint over both his nipples with her fingers, her breasts pressed on his back, smiling, " + BADGE + ", cum dripping untouched"),
   # 学院長（★素足の教育）
   "btl_boss":   ("office", "he kneels inside transparent crystal walls in front of the armchair, the headmistress sits with her robe hem raised, both her bare soles squeezing his penis between them, footjob, crystal light on his chest, a crystal shard on a cord at his neck, cum on her feet"),
   "onani_boss": ("private", "sitting alone on the thick carpet with one leg pulled in, stroking his own lower belly with the sole of his own foot, toes curled, penis untouched, " + BADGE + ", the headmistress watches far away from the low couch"),
   "inochi_boss":("office", "he kneels on the rug kissing the top of her bare foot, the headmistress sits in the armchair, her other bare foot stroking his chest, a blank certificate without text on the desk, a crystal glowing brightly, " + BADGE + ", cum dripping untouched"),
   "onedari_boss":("office", "he kneels before the armchair with his chest pushed forward, the headmistress sits pinching his nipple with her bare toes, a beam of crystal light on his nipple, a blank record book without text on her lap, haughty smile, " + BADGE + ", cum dripping"),
 },
 "lose_desc": "keeps him forever in the unwaking dream academy as a dream resident, his silver badge dyed fully pink.",
 "onanie": {
   "master": ("hall", "kneeling behind a stone pillar, lips moving as if begging, pinching his own nipple, a wet finger of the other hand in his own anus, penis untouched"),
   "e1": ("staff", "sitting on the floor behind the desk, rubbing his own nipple, lips moving as if scoring himself, penis untouched"),
   "e2": ("storage", "lying on the old bed hugging a white pillow with his face buried in it, rubbing his own nipple, the other hand stroking his own anus, penis untouched"),
   "e3": ("artprep", "sitting behind a cloth-covered painting, tracing circles on his own nipple with a fingertip as if painting, penis untouched"),
   "boss": ("private", "sitting on the thick carpet with one leg pulled in, stroking his own lower belly with the sole of his own foot, penis untouched"),
 },
 "magic": {
   "1": (None, "gate", "a round silver badge divided into twelve rings, the two outer rings dyed glowing pink, lying on a dark cloth, soft warm glow, close-up, badge without text"),
   "2": (None, "roof", "a large bronze bell hanging in a bell tower under a pink sky, faint sound ripples in the air, pink mist flowing"),
   "3": ("boss", "office", "raising one hand, transparent warm crystal walls rising around her, crystal pendant glowing, elegant haughty smile"),
   "4": (None, "clinic", "a small glass bottle of thick sweet pink medicine with a cork on a white tray, bottle without text, soft light, close-up"),
   "5": ("m", "town", "spreading her arms and bat wings, thick pink mist pouring down from the pink sky around her, tail swaying, impish laughing smile"),
 },
}
