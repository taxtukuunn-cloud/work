# N132 森と淫魔の領域（Moon2）画像データ。登場人物は全員20歳以上。6人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない。原作の立ち絵は参照していない）。
# 髪色は被らせない：リーゼ＝赤／ソレイユ（立ち絵の2人目だけ）＝金の巻き髪／ミュカス＝濃い紫／ダークエルフ＝銀／アルラウネ＝ピンクの花びら／マーチ＝明るい茶。
# 青・水色系の髪・瞳は使っていない（瞳は crimson／magenta／golden／pink／green。原作の色が不明な部分は役に合う色で決めた）。
# マスターは2人組：立ち絵だけ2人（pose に2人目）。技CG・敗北CGは「リーゼ1人＋主人公」に置き換え（ソレイユの役＝囁き・乳首・口づけもリーゼが行う）。
# ダークエルフの分体は「3人以上を出さない」ため本体1人だけで描く（耳・乳首・後ろを1人で。分体は描かない）。
# 挿入はアルラウネの細い蔦とミュカスの羽の触手だけ（どちらも pen なし）。ほかは指まで。マーチは後ろに触れない。
# 鞭は叩かない（房で撫でるだけ）。ハイヒールは靴底の平らな所で踏むだけ（痕・傷なし）。看板・本・時計は文字なし。主人公の首には赤と白のリボン。
RIB = "red and white silk ribbons tied in bows around his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
WHIP_NEG = "whip marks, bruise, wound, welts, whipping, heel digging into skin, pain, crying"
WING_NEG = "scary, grotesque, slimy monster, teeth, extra people"
VINE_NEG = "scary, grotesque, thorns, wound"
DATA = {
 "code": "Moon2",
 "world": "enchanted forest leading to a succubus domain, golden pollen drifting in the air, roses, red and white banners, two distant castles with bell towers, fantasy, detailed background",
 "bg": "stone-paved road leaving a deep forest toward a tall black iron gate, red and white banners fluttering on both sides, climbing roses, two distant castles with bell towers under a dusky sky, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "リーゼ＆ソレイユ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, succubus, red hair, very long straight hair, crimson eyes, black curved horns, slender black demon tail, black and red bondage-style dress, corset, long black gloves, black stockings, black high heels, a black riding whip with a soft tassel in her hand, soft curvy feminine body, huge breasts, wide hips",
         "name": "the red-haired succubus queen in a black and red dress",
         "pose": "one hand on her hip, holding a tasseled whip, elegant composed smile, looking down at viewer, standing beside a second adult woman with long curly golden hair, a gold crown, horns and a white and gold gown who covers her mouth with one hand and smiles sweetly",
         "neg": SOFT_NEG + ", " + WHIP_NEG},
   "e1": {"type": "woman", "jp": "ダークエルフ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark elf, dark-skinned female, dark brown skin, silver hair, very long straight hair, long pointy ears, glowing golden eyes, black and gold elven robe with a high slit, gold circlet, gold armlets, soft curvy feminine body, large breasts",
          "name": "the silver-haired dark elf in a black and gold robe",
          "pose": "reclining lazily on one elbow, one hand lifted with a faint purple mist around her fingers, bored teasing smirk, looking at viewer with glowing golden eyes",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "アルラウネ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, alraune, plant girl, monster girl, light green skin, hair made of pink flower petals, long pink hair, pink eyes, her lower body hidden inside a giant pink flower, green vines with rounded tips around her, leaf and petal top covering her chest, soft curvy feminine body, large breasts",
          "name": "the green-skinned alraune in a giant pink flower",
          "pose": "leaning forward out of her giant flower with both arms held open, vines swaying, sweet inviting smile, looking at viewer",
          "neg": SOFT_NEG + ", " + VINE_NEG + ", human legs on the alraune"},
   "e3": {"type": "woman", "jp": "マーチ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, light brown hair, medium wavy hair, white rabbit ear headband, green eyes, checkered tailcoat, white blouse, bow tie, short black skirt, white gloves, a gold pocket watch with a blank face on a chain, soft curvy feminine body, huge breasts",
          "name": "the woman in a checkered tailcoat with a rabbit-ear headband",
          "pose": "holding a teapot in one hand and a blank-faced pocket watch in the other, completely serious straight face, looking at viewer",
          "neg": SOFT_NEG + ", numbers on the watch"},
   "boss": {"type": "woman", "jp": "ミュカス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, succubus, dark purple hair, very long wavy hair, magenta eyes, large dark purple demon wings whose inner side is lined with many soft smooth pink tendrils, long slender tail with a flower-shaped tip, black and purple revealing dress, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the purple-haired winged succubus",
            "pose": "both large wings half spread showing the soft tendrils inside, one finger at her lips, relaxed big-sisterly smile, looking at viewer",
            "neg": SOFT_NEG + ", " + WING_NEG},
 },
 "places": {
   "entrance": "forest entrance, dappled sunlight through young leaves, a crooked blank wooden signboard without text, soft earth path",
   "tea":      "garden tea party, a long table with a white tablecloth, teacups and teapots, baked sweets, steam of black tea, hedges",
   "deep":     "deep forest, golden pollen drifting in the air, hanging vines, large flowers, damp moss",
   "flower":   "inside a giant pink flower bed, soft petals all around, pink dim light, glossy nectar",
   "elfwood":  "elven forest, giant trees with huge roots, clear air, a cold spring, leaves rustling",
   "manor":    "treetop elven manor interior, faint purple mist, incense, silver candlesticks, wooden floor, a long couch by the window",
   "swamp":    "misty purple swamp shore, soft mud, a fallen log, sweet purple haze over warm water",
   "gate":     "entrance of the succubus domain, tall black iron gate with stone pillars, red and white banners, roses, stone pavement",
   "nest":     "dim warm cave nest, soft moss floor, a bedding of soft cloth in the back, warm humid air",
   "training": "castle training hall, red carpet, whips hanging on the wall, red candles, smell of leather",
   "lroom":    "red private bedroom, red canopy bed, a chair in front of a bookshelf with blank book spines without text, red candles",
   "throne":   "white and gold throne hall, white marble floor, gold candlesticks, a tea set with rising steam beside the throne",
   "sroom":    "white private bedroom, white canopy bed, heaps of soft cushions, plates of sweets",
   "corridor": "castle corridor whose carpet is red on one side and white on the other, tall windows on both sides showing two bell towers",
   "bedroom":  "large shared bedroom, a huge bed under a canopy half red and half white, roses, a tea set on a side table",
 },
 "atk": {
   "m1": ("throne", "he kneels on the white marble floor, the succubus queen leans down behind him whispering sweetly into his ear, one gloved hand holding a teacup to his lips, her other hand resting on his shoulder, his knees weak, dazed, " + RIB),
   "m2": ("training", "from side, he lies on his back on the red carpet, the succubus queen stands over him resting the flat sole of her high heel on his chest, the soft tassel of her whip brushing his nipple without striking, elegant smile, " + RIB),
   "m3": ("bedroom", "he lies on his back on the huge bed, the succubus queen leans over him kissing him deeply, tongues, saliva trail, two rose-oiled fingers of her hand in his anus, fingering, his hips lifting, " + RIB),
   "e1": ("manor", "he kneels on the wooden floor beside the long couch, the dark elf reclines on the couch behind him licking his ear, one hand rolling his nipple, her oiled finger in his anus, fingering, glowing golden eyes, purple mist, " + RIB),
   "e2": ("flower", "he is held inside the giant pink flower against her chest, soft vines wound loosely around his wrists and ankles, vine tips stroking his nipples, a thin round-tipped vine in his anus, the alraune hugging him, golden pollen in the air, " + RIB),
   "e3": ("tea", "he sits undressed on a chair at the tea table pushing his chest forward, the woman in the tailcoat stands beside him pinching his nipple with her gloved fingers, a teapot in her other hand, serious straight face, " + RIB),
   "boss": ("nest", "he is wrapped inside her large wings with only his head and shoulders showing, soft pink tendrils stroking his neck, nipples and inner thighs, the flower-shaped tail tip wrapped around his penis, the winged succubus embracing him from behind, warm glow, " + RIB),
 },
 "atk_desc": {
   "m1": "the succubus queen pulls him into a sweet swamp of words until he kneels by himself.",
   "m2": "the succubus queen steps on his chest with her heel and strokes him with the whip tassel without striking.",
   "m3": "the succubus queen seals his lips with a kiss while pressing inside with her fingers.",
   "e1": "the dark elf holds his gaze with her charm eyes while teasing his ear, nipple and rear at once.",
   "e2": "the alraune draws him into her flower with pollen and vines and asks for his seed.",
   "e3": "the woman rewrites his common sense so he offers his nipples at the tea party.",
   "boss": "the winged succubus wraps his whole body in her wings and strokes him everywhere at once.",
 },
 "lose": {
   # 長の二人 技1（女王の祝福＋★取り合い）
   "btl_m1":     ("throne", "he kneels on the white marble floor before the throne, the succubus queen rests her stockinged foot on his thigh, leaning down whispering into his ear, one hand pinching his nipple, a braided red and white ribbon around his neck, cum dripping untouched"),
   "onani_m1":   ("gate", "sitting alone behind a stone gate pillar, lips moving as if whispering to himself, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, a loosened ribbon end at his neck, penis untouched, the succubus queen watches far away by the gate"),
   "inochi_m1":  ("corridor", "he lies on his back on the line where the carpet changes from red to white, the succubus queen stands over him with the flat sole of her heel on his lower belly, bending down to whisper and roll his nipple, " + RIB + ", cum on his stomach"),
   "onedari_m1": ("bedroom", "he lies in the middle of the huge bed, the succubus queen lies beside him holding his head to her chest, whispering into his ear, her fingers rolling his nipple, her stockinged foot pressing his thigh, " + RIB + ", cum dripping"),
   # 長の二人 技2（★鞭と甘言の取り合い）
   "btl_m2":     ("training", "from side, he lies on his back on the red carpet with knees raised, the succubus queen kneels over him, her stockinged foot pressing his penis against his lower belly, footjob, two rose-oiled fingers in his anus, fingering, a red whip tassel and a white lace ribbon at his neck, cum on his stomach"),
   "onani_m2":   ("lroom", "kneeling alone behind the red canopy curtain, one hand pinching his own nipple hard, a finger of the other hand gently in his own anus, a loosened ribbon end at his neck, penis untouched, the succubus queen watches far away from the doorway"),
   "inochi_m2":  ("corridor", "he sits on the two-colored carpet leaning back, the succubus queen stands close with her stockinged foot on his chest, the soft whip tassel stroking his inner thigh without striking, her other hand tilting his chin up, " + RIB + ", cum dripping"),
   "onedari_m2": ("bedroom", "he lies on his back under the half red half white canopy, the succubus queen sits beside him pressing her stockinged foot on his lower belly, leaning to lick his nipple, counting on her gloved fingers, " + RIB + ", cum on his stomach"),
   # 長の二人 技3（二人の長の口づけ＋★取り合い）
   "btl_m3":     ("bedroom", "from side, he lies on his back on the huge bed with legs spread, the succubus queen over him kissing him deeply, tongues, saliva trail, two oiled fingers pressing deep in his anus, fingering, red lipstick marks on his neck, " + RIB + ", cum on his stomach"),
   "onani_m3":   ("sroom", "lying alone buried in soft cushions, sucking the fingers of one hand as if kissing, a finger of the other hand in his own anus, a loosened ribbon end at his neck, penis untouched, the succubus queen watches far away by the white canopy bed"),
   "inochi_m3":  ("gate", "he stands with his back against the black gate, the succubus queen pins him there kissing him deeply, tongues, one hand behind him with two oiled fingers in his anus, fingering, his legs trembling, " + RIB + ", cum dripping"),
   "onedari_m3": ("bedroom", "he sits on the bed held in her arms from the front, the succubus queen kissing him deeply, saliva trail, her oiled fingers deep in his anus, fingering, her tail curled around his waist, lipstick marks on his cheek, " + RIB + ", cum dripping"),
   # ダークエルフ（★分体の惑い）
   "btl_e1":     ("manor", "he kneels beside the long couch facing her, the dark elf reclines holding his chin and staring into his face with glowing golden eyes, her other hand behind him with two oiled fingers in his anus, fingering, a clear glass bead on his neck ribbon, purple mist, cum dripping untouched"),
   "onani_e1":   ("elfwood", "sitting alone against a giant tree root, one hand touching his own ear and nipple, the other hand between his inner thighs reaching back to his own anus, a loosened ribbon end at his neck, penis untouched, the dark elf watches far away from a branch"),
   "inochi_e1":  ("swamp", "he has sunk to his knees in the soft mud in thick purple mist, the dark elf crouches behind him whispering into his ear, licking it, one hand rolling his nipple, glowing golden eyes, his body limp, " + RIB + ", cum dripping"),
   "onedari_e1": ("manor", "he sits on the window couch held from behind, the dark elf turns his face to stare into it with glowing golden eyes, both her hands pinching and rolling his nipples, bored teasing smirk, purple mist, " + RIB + ", cum dripping untouched"),
   # アルラウネ（★種をちょうだい）
   "btl_e2":     ("flower", "from side, he lies inside the giant pink flower wrapped in soft petals, vines loosely around his wrists and ankles, vine tips rolling his nipples, a thin round-tipped vine in his anus, the alraune hugging his head to her chest, golden pollen, a petal ornament in his hair, cum on his stomach"),
   "onani_e2":   ("deep", "kneeling alone beside a large flower, burying his face in the petals to smell it, one hand rubbing his own nipple, a finger of the other hand in his own anus, a loosened ribbon end at his neck, penis untouched, the alraune watches far away among the vines"),
   "inochi_e2":  ("deep", "he kneels in front of her giant flower, the alraune leans out holding his face and kissing him, feeding nectar mouth to mouth, glossy nectar dripping from his lips, vines stroking his nipples, golden pollen, " + RIB + ", cum dripping"),
   "onedari_e2": ("flower", "he lies on his stomach on the soft petals with hips raised, the alraune leans over his back blowing golden pollen at his face, two thin round-tipped vines in his anus, vine tips rolling his nipples, " + RIB + ", cum dripping"),
   # マーチ（★常識改変）
   "btl_e3":     ("tea", "he sits undressed at the long tea table with his chest pushed forward, the woman in the tailcoat pinches both his nipples from behind his chair, serious straight face, a stopped pocket watch with a blank face hanging from his neck, teacups, cum dripping untouched"),
   "onani_e3":   ("entrance", "standing alone behind the blank wooden signboard with his clothes folded at his feet, pinching both his own nipples, lips moving as if reciting a rule, a loosened ribbon end at his neck, penis untouched, the woman in the tailcoat watches far away on the path"),
   "inochi_e3":  ("tea", "he sits at the tea table holding out an empty teacup, the woman in the tailcoat pours tea with one hand and strokes his nipple with the back of a warm teaspoon with the other, serious straight face, many empty cups, " + RIB + ", cum dripping untouched"),
   "onedari_e3": ("tea", "he sits undressed on the chair at the head of the tea table with legs apart, the woman in the tailcoat bends down licking one nipple and pinching the other, a finger raised as if declaring a rule, " + RIB + ", cum dripping untouched"),
   # ミュカス（★包み込む羽）
   "btl_boss":     ("nest", "from side, he is wrapped inside her large wings with his flushed face showing, soft pink tendrils on his nipples and thighs, a tendril from the wing in his anus, the flower-shaped tail tip wrapped around his penis, the winged succubus holding him from behind, a soft purple feather tucked at his neck ribbon, cum"),
   "onani_boss":   ("swamp", "sitting alone behind a fallen log wrapped head to toe in a blanket, one hand inside the blanket at his own nipple, the other hand reaching behind to his own anus, a loosened ribbon end showing, penis untouched, the winged succubus watches far away in the purple mist"),
   "inochi_boss":  ("nest", "he lies curled on the moss floor inside her closed wings, only a gap showing his dazed face, soft pink tendrils stroking his nipples, a tendril in his anus, the winged succubus lying behind him stroking his hair, warm glow, " + RIB + ", cum dripping"),
   "onedari_boss": ("nest", "he sits in her lap on the soft bedding deep in the cave, her large wings closing around them, the flower-shaped tail tip sucking his penis, a wing tendril deep in his anus, the winged succubus whispering at his ear, " + RIB + ", cum"),
 },
 "lose_desc": "makes him the shared belonging of the two succubus queens, never leaving the forest again.",
 "onanie": {
   "master": ("gate", "sitting against a stone pillar, one hand pinching his own nipple hard, a finger of the other hand gently in his own anus, penis untouched"),
   "e1": ("elfwood", "sitting against a giant tree root, one hand at his own ear and nipple, the other hand stroking his inner thigh and reaching to his own anus, penis untouched"),
   "e2": ("deep", "kneeling beside a large flower smelling it, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched"),
   "e3": ("entrance", "standing behind a blank signboard with his shirt off, pinching both his own nipples, lips moving as if reciting a rule, penis untouched"),
   "boss": ("swamp", "wrapped in a blanket behind a fallen log, one hand inside the blanket at his own nipple, the other hand behind at his own anus, penis untouched"),
 },
 "magic": {
   "1": ("m", "gate", "holding up a red silk ribbon in one hand and a white silk ribbon in the other, about to tie them, elegant smile"),
   "2": (None, "corridor", "two castle bell towers seen through tall windows, a low bronze bell and a high silver bell swinging, faint sound ripples in the air, dusk light"),
   "3": (None, "swamp", "a quiet swamp covered in sweet purple mist, soft mud and warm still water, a fallen log, faint glowing haze"),
   "4": ("e2", "deep", "blowing a cloud of golden pollen from her open palm toward the viewer, vines swaying, sweet playful smile"),
   "5": (None, "bedroom", "a huge empty bed under a canopy half red and half white, a red ribbon and a white ribbon lying crossed on the pillow, roses, soft candle light"),
 },
}
