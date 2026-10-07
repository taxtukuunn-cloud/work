# N116 創生種の神殿（Sosei）画像データ。登場人物は全員20歳以上。責め手5人は全員女性（創生種の淫魔）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（竜の娘も柔らかく豊満）。
# 髪色の書き分け：設定では イルミナ＝紫の長髪／セメト＝濃い紫の短髪／ゴグ＝紫の短髪 と紫が3人いるので、
#   イルミナ＝light lilac purple、セメト＝dark plum purple、ゴグ＝wine red-purple と言い分けた（原作に青・水色のキャラはいない）。
# ふたなりの挿入（pen: penis）は ハーロットの竜の契り（m3）と ゴグマゴグのメイティングプレグ（e2）だけ。指・尻尾は pen なし。
# イルミナ・セメト・ラヴァーは挿入しない（指まで。ラヴァーは乳首とラバーと振り子だけ）。
# ラヴァーの本（e3）は主人公が黒いラバーの衣装を着せられる（hero_outfit）。体は変えない。
# セメトの従者・催恋慈の信徒は描かない（3人以上を出さない）。浮かぶ目玉は灯りのような丸い飾りとして描き、怖くしない。
P = {"pen": "penis"}
MARK = "a pale pink eye-and-heart crest drawn on his chest over his heart"
RUBBER = "a glossy black rubber bodysuit from neck to toe with an eye emblem on the chest and a thin clear window over his heart"
R = {"hero_outfit": RUBBER}
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, fangs"
EYE_NEG = "gore, bloodshot, veins, horror, creepy, scary"
DATA = {
 "code": "Sosei",
 "world": "sandstone temple district on a paradise island, eye-crest banners, drifting incense smoke, soft pink lamp light, detailed background",
 "bg": "sandstone temple gate in daytime, banners with a stylized eye crest without text, drifting incense smoke, warm sand on the ground, a black rock dragon temple far away behind the gate, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ドラゴンハーロット",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long hair, black dragon horns, crown, golden eyes, large black dragon wings, black dragon tail, black and purple gothic dress, long skirt, soft curvy feminine body, huge breasts, wide hips",
         "name": "the black-haired dragon queen in a gothic dress",
         "pose": "wings half spread, one hand raised with long fingers beckoning, haughty regal smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "セメト",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, dark plum purple hair, short hair, glasses, purple eyes, curled purple horns, ankh earrings, white lab coat, purple bikini, test tube holder on her thigh, white gloves, soft curvy feminine body, large breasts",
          "name": "the brown-skinned scientist queen in a white lab coat",
          "pose": "holding up a glass test tube without text between two fingers, the other hand adjusting her glasses, commanding confident smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "ゴグマゴグ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, very tall, long legs, wine red-purple hair, short hair, red horns, amber eyes, dragon wings, scaled dragon legs, thick scaled dragon tail, simple cloth top and loincloth, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the red-horned dragon woman with a scaled tail",
          "pose": "hunching her shoulders shyly, both hands holding a sparkling stone to her chest, timid gentle smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ラバーズ・ラヴァー",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, long legs, blonde hair, long hair, black nun veil, blindfold with an eye emblem, glossy black rubber bodysuit, ring pendulum on a chain, slender curvy feminine body, large breasts",
          "name": "the blonde nun in a black rubber bodysuit and blindfold",
          "pose": "dangling a ring pendulum from one raised hand, the other hand on her cheek, sweet sticky smile, facing viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "イルミナ",
            "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, long legs, light lilac purple hair, very long hair, purple horns, face veil with an eye emblem covering her eyes, purple dress, segmented purple tail, round floating eye-shaped lanterns around her, slender curvy feminine body, large breasts",
            "name": "the veiled lilac-haired priestess in a purple dress",
            "pose": "one hand pinching the edge of her veil, blank tarot cards without text floating beside her, slow dreamy smile, facing viewer",
            "neg": SOFT_NEG + ", " + EYE_NEG},
 },
 "places": {
   "gate":    "sandstone temple gate, eye-crest banners without text, incense smoke, warm sand",
   "chapel":  "chapel with a high ceiling, many pendulums hanging from above, pink lamp light, rows of prayer cushions",
   "confess": "narrow confession booth, a lattice window, dim light, wooden bench",
   "dress":   "dressing room, racks of glossy black rubber outfits, a large mirror, soft light",
   "yochi":   "quiet divination room, blank tarot cards without text floating in the air, round eye-shaped lamps, dark drapes",
   "grotto":  "glass grotto, walls of glass panels, reflected light, many reflections",
   "lab":     "white laboratory inside a sandstone pyramid, shelves of glass test tubes without text, glass instruments",
   "opr":     "treatment room, a soft padded treatment table, softly glowing culture tanks, trays of glass vials",
   "hangar":  "chariot hangar, a golden chariot, sand on the stone floor, tall doors",
   "valley":  "red rock valley, hot wind, shadow of wings crossing overhead, distant cliffs",
   "nest":    "large cave nest, bed of hay and cloth, a pile of sparkling stones, warm dim light",
   "spring":  "steaming hot spring among warm rocks, thick steam, flat warm rock",
   "temple":  "black rock temple interior, a black dragon statue, purple flames in braziers, a woven rug",
   "throne":  "black throne on a dais, black gothic drapes, purple flames, stone steps",
   "bed":     "dragon bedchamber, a huge bed, purple canopy drapes, dragon scale ornaments, dim purple light",
 },
 "atk": {
   "m1": ("throne", "he kneels on the stone steps holding his shirt open, " + MARK + ", the dragon queen stands over him with black wings spread wide, looking down, purple aura around her, his knees trembling"),
   "m2": ("temple", "he stands held inside her folded black wings, the dragon queen embraces him from behind, her tail coiled around his waist, long fingers pinching his nipple, two oiled fingers of her other hand in his anus, fingering, " + MARK),
   "m3": ("bed", "from side, he lies on his back on the huge bed with legs spread, the dragon queen over him with wings folded around them, her penis in his anus, anal, kissing him deeply, hot breath, saliva, his own penis separate, " + MARK, P),
   "e1": ("opr", "he lies on his back on the padded treatment table with his shirt open, the scientist queen leans over him dripping warm liquid from a test tube onto his nipple, two gloved fingers of her other hand in his anus, fingering, watching through her glasses, " + MARK),
   "e2": ("nest", "from side, he lies on his side on the hay bed, the dragon woman lies behind him hugging him tightly in both arms, her scaled tail wrapped around his legs, her penis in his anus, anal, not moving, his own penis separate, " + MARK, P),
   "e3": ("dress", "he stands before the large mirror, the blonde nun stands behind him tracing circles on his nipple through the rubber with a fingertip, her other hand swinging a ring pendulum before his face, " + MARK + " showing through the window", R),
   "boss": ("yochi", "he kneels on a cushion with hips raised, the veiled priestess crouches beside him lifting the edge of her veil slightly with one hand, two fingers of her other hand in his anus, fingering, round eye-shaped lanterns floating close around him, " + MARK, {"neg": EYE_NEG}),
 },
 "atk_desc": {
   "m1": "the dragon queen spreads her wings and makes him kneel with her aura.",
   "m2": "the dragon queen wraps him in her wings, pinching his nipple and pressing inside with her fingers.",
   "m3": "the dragon queen seals a pact with a deep kiss while taking him from the front.",
   "e1": "the scientist queen raises his sensitivity with warm drops and measures him with gloved fingers.",
   "e2": "the dragon woman hugs him from behind and holds still inside him.",
   "e3": "the blonde nun dresses him in black rubber and traces his nipple through it while a pendulum swings.",
   "boss": "the veiled priestess lifts her veil slightly while floating eye lanterns watch him.",
 },
 "lose": {
   # ハーロット 技1（ドラゴニックオーラ＋竜の抱擁）
   "btl_m1":     ("throne", "he kneels on the steps holding his shirt open with both hands, " + MARK + " glowing, the dragon queen stands over him with wings spread, bending to pinch his nipple, a black scale necklace on his neck, cum dripping untouched"),
   "onani_m1":   ("temple", "kneeling alone on the rug before the black dragon statue, looking up, tracing the pink crest on his chest with one hand, the other hand reaching behind to stroke his own anus, penis untouched, the dragon queen watches far away from the shadows"),
   "inochi_m1":  ("valley", "he kneels at the mouth of the valley inside the shadow of her wings, the dragon queen stands before him folding one wing around his back, her fingers on his nipple, her tail around his waist, " + MARK + ", looking up at her"),
   "onedari_m1": ("throne", "he kneels on the step beside the throne with his shirt open, the dragon queen sits on the throne covering him with one wing, pinching his nipple, two fingers of her other hand in his anus, fingering, " + MARK + ", cum dripping"),
   # ハーロット 技2（★竜の抱擁）
   "btl_m2":     ("temple", "he is wrapped inside her closed black wings, the dragon queen holds him from behind, tail coiled around his waist, rolling his nipple, two oiled fingers deep in his anus, fingering, " + MARK + " glowing, a glass orb beside them, cum dripping"),
   "onani_m2":   ("spring", "sitting alone on a warm rock wrapped head to toe in his brown cloak, one hand inside rubbing his own nipple, the other hand reaching behind to his own anus, pink glow leaking from the cloak, penis untouched, the dragon queen watches far away through the steam"),
   "inochi_m2":  ("bed", "dawn light, he lies curled inside her black wings on the huge bed, the dragon queen holds him from behind pinching his nipple, two fingers in his anus, fingering, her tail around his waist, " + MARK + ", cum on the sheets"),
   "onedari_m2": ("bed", "he sits on her lap on the bed facing away, the dragon queen wraps both wings tightly around him, tail coiled around his waist, one hand on his nipple, two fingers of her other hand in his anus, fingering, " + MARK + ", cum dripping"),
   # ハーロット 技3（竜の契り）
   "btl_m3":     ("bed", "from side, he lies on his back on the huge bed with legs lifted, the dragon queen over him holding his waist, wings folded around them, her penis in his anus, anal, deep kiss, hot breath, a black scale ring on his finger, his own penis separate, cum on his stomach", P),
   "onani_m3":   ("throne", "sitting alone on the floor behind the throne, sucking two of his own fingers with hot breath, the other hand reaching behind with a finger in his own anus, " + MARK + " glowing, penis untouched, the dragon queen watches far away from beside the drapes"),
   "inochi_m3":  ("temple", "from side, on the woven rug before the dragon statue, he lies on his back, the dragon queen over him with wings spread above, her penis in his anus, anal, kissing him, breathing into his mouth, " + MARK + " glowing bright, his own penis separate", P),
   "onedari_m3": ("bed", "from side, he sits on her lap facing her on the bed, arms around her neck, the dragon queen holding his hips, her penis in his anus, anal, deep kiss, saliva trail, wings closed around them, his own penis separate, cum dripping", P),
   # セメト（★ベッティ・パピルス）
   "btl_e1":     ("opr", "he lies on his back on the padded table with his shirt open, the scientist queen leans over him dripping warm liquid onto his nipple, two gloved fingers pressing deep in his anus, fingering, a blank tag without text on his wrist, " + MARK + ", cum on his stomach"),
   "onani_e1":   ("lab", "crouching alone behind a shelf, smearing leftover liquid from a test tube onto his own nipple, a wet finger of the other hand in his own anus, penis untouched, the scientist queen watches far away from the doorway"),
   "inochi_e1":  ("hangar", "he sits on the golden chariot seat on her lap facing forward, the scientist queen holds him from behind pinching both his nipples, a clipboard without text beside her, his shirt open, " + MARK + ", trembling"),
   "onedari_e1": ("opr", "he lies on the padded table holding his own knees, the scientist queen stands between his legs, two gloved fingers in his anus, fingering, her other hand holding an open blank notebook without text, " + MARK + ", wet nipples, cum dripping"),
   # ゴグマゴグ（★メイティングプレグ）
   "btl_e2":     ("nest", "from side, he lies on his side on the hay bed, the dragon woman hugs him from behind in both arms, scaled tail wrapped around his legs, her penis in his anus, anal, not moving, a sparkling stone in his hand, his own penis separate, cum dripping", P),
   "onani_e2":   ("valley", "lying alone behind a red rock hugging a blanket tightly around his body, one hand reaching behind with a finger in his own anus, " + MARK + " glowing, penis untouched, the dragon woman watches far away from the rocks"),
   "inochi_e2":  ("nest", "from side, napping on the hay bed, he lies on top of the dragon woman facing her, held in her arms, her penis in his anus, anal, her wing over his back, bowls of fruit beside the bed, his own penis separate, cum dripping", P),
   "onedari_e2": ("nest", "from side, he sits on her lap facing her on the hay bed, the dragon woman hugs him tightly with both arms, tail around his waist, her penis in his anus, anal, his face against her soft chest, his own penis separate, cum dripping", P),
   # ラヴァー（★女装魔法・ラバー）
   "btl_e3":     ("dress", "he stands before the large mirror, the blonde nun behind him tracing his nipple through the rubber with a fingertip, swinging a ring pendulum before his face, " + MARK + " showing through the window, his knees weak, wet spot on the rubber", R),
   "onani_e3":   ("confess", "sitting alone on the bench in the booth, dangling a thin string with a ring like a pendulum before his face, tracing his own nipple over his shirt with a fingertip, penis untouched, the blonde nun watches far away through the lattice window"),
   "inochi_e3":  ("gate", "he stands before the temple gate looking up at the eye-crest banner, the blonde nun stands behind him stroking both his nipples through the rubber, a ring pendulum hanging from her wrist, " + MARK + " showing through the window, legs trembling", R),
   "onedari_e3": ("dress", "he kneels before the large mirror, the blonde nun kneels behind him, one fingertip stroking his nipple through the rubber, the other hand swinging a ring pendulum beside the mirror, his reflection, wet spot on the rubber", R),
   # イルミナ（★第五の重波動）
   "btl_boss":   ("yochi", "he kneels on a cushion with hips raised, the veiled priestess crouches beside him lifting her veil slightly, two fingers in his anus, fingering, round eye-shaped lanterns floating close around him, " + MARK + ", his mouth open speaking, cum dripping untouched", {"neg": EYE_NEG}),
   "onani_boss": ("grotto", "kneeling alone before a glass wall staring at his own reflection, lips moving, one hand reaching behind with a finger in his own anus, " + MARK + " reflected in the glass, penis untouched, the veiled priestess watches far away as a reflection"),
   "inochi_boss":("chapel", "he kneels under the hanging pendulums, the veiled priestess kneels behind him lifting her veil slightly beside his face, two fingers in his anus, fingering, her other hand on his chest over the crest, pink light, cum dripping", {"neg": EYE_NEG}),
   "onedari_boss":("yochi", "he sits on the floor with his shirt open, the veiled priestess sits before him pinching his nipple, a blank tarot card without text floating between them, round eye-shaped lanterns watching his whole body, " + MARK + ", cum dripping untouched", {"neg": EYE_NEG}),
 },
 "lose_desc": "keeps him on the island forever as the dragon queen's cherished consort, the pink crest on his chest complete.",
 "onanie": {
   "master": ("temple", "wrapped in his brown cloak, one hand inside rubbing his own nipple, the other hand reaching behind to his own anus, penis untouched"),
   "e1": ("lab", "crouching, smearing liquid from a test tube on his own nipple, a wet finger in his own anus, penis untouched"),
   "e2": ("valley", "hugging a blanket tightly around his body, one finger in his own anus, penis untouched"),
   "e3": ("confess", "sitting, watching a ring on a string swing like a pendulum, tracing his own nipple with a fingertip, penis untouched"),
   "boss": ("grotto", "kneeling before a glass wall staring at his reflection, one finger in his own anus, penis untouched"),
 },
 "magic": {
   "1": ("m", "throne", "drawing a glowing pale pink eye-and-heart crest in the air with the tip of her black tail, two fresh strokes of light, amused regal smile"),
   "2": (None, "chapel", "rows of empty prayer cushions under many hanging pendulums, pink lamp light, faint ripples of sound in the air, incense smoke"),
   "3": (None, "temple", "twelve round eye-shaped lamps in a row on a black rock wall, one lamp open and glowing soft pink, gentle light, not scary"),
   "4": (None, "lab", "a glass test tube of warm pink syrupy liquid in a holder, one drop falling from its lip, sweet steam, tube without text, close-up"),
   "5": (None, "chapel", "interior of a high chapel, a large ring pendulum swinging at the center, pink lamps, drifting incense smoke, quiet and solemn"),
 },
}
