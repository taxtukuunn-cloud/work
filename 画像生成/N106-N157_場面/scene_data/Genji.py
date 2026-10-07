# N106 ゲンジアマゾネスの密林（Genji）画像データ。登場人物は全員20歳以上。5人とも女性の双成種（ふたなり）・褐色肌・尻尾あり。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（武人も曲線のある体つき）。
# 比叡：原作は青い瞳 → silver-grey eyes に置き換え（髪は淡いミント＝pale mint）。阿黒：原作の尻尾は青緑 → jade green tail と書く。
# ふたなりの挿入（pen: penis）は 鞍馬の頭領の褒美（m3）・比叡の立ち抱擁（boss）・混登呂の btl／onedari だけ。尻尾・指は pen なし。
# 御土の影分身は「3人以上を出さない」ため本体1人だけで描く（耳・乳首・後ろを1人で。分身は描かない）。
# 淫毒矢は丸い吸い口で刺さらない（傷・流血なし）。主人公の手首には赤い組紐。
P = {"pen": "penis"}
CORD = "a red braided cord tied around his wrist"
ARROW = "pale pink arrows with soft round suction-cup tips stuck on his skin without piercing"
ARROW_NEG = "sharp arrowhead, arrow piercing skin, stabbed, wound, scary"
SOFT_NEG = "muscular female, abs, broad shoulders, biceps, scary, fangs"
DATA = {
 "code": "Genji",
 "world": "vast dim tropical jungle of an amazon tribe, giant trees and hanging vines, ferns, humid haze, shafts of light through the canopy, detailed background",
 "bg": "deep dim tropical jungle in daytime, giant trees, thick ferns and hanging vines, a narrow animal trail, humid mist, shafts of light through the canopy, a red and black great tent far away between the trees, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "鞍馬",
         "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, black hair, red streaked hair, long high ponytail, leaf hair ornament, red eyes, pointy ears, fur stole, green crop top, red gauntlets, black thighhighs, katana at her hip, green tail with a leaf-shaped tip, crest tattoo on her thigh, soft curvy feminine body, large breasts",
         "name": "the black-ponytail chieftain in a fur stole",
         "pose": "one hand on her hip, the other hand beckoning, bold hearty grin, looking at viewer with red eyes",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "混登呂",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, blonde hair, long hair, helmet with purple horns, amber eyes, grey armor breastplate, white loincloth, round gold shield, yellow tail, soft curvy feminine body, large breasts",
          "name": "the blonde warrior in a purple-horned helmet",
          "pose": "holding a round gold shield at her side, one finger raised as if giving an order, polite composed smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "御土",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, dark-skinned female, brown skin, light brown hair, short hair, ocelot ears, golden eyes, black mouth mask, black ninja bodysuit, spotted ocelot tail, slender curvy feminine body, medium breasts",
          "name": "the ocelot-eared ninja in a black bodysuit",
          "pose": "crouching lightly on one knee, one hand forming a ninja hand sign, calm quiet eyes, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "阿黒",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, wide hips, dark-skinned female, brown skin, red tribal markings on her skin, grey hair, medium hair, horned beast headdress, yellow eyes, fur collar, hunter outfit, bow, jade green tail, slender feminine body, small breasts",
          "name": "the grey-haired huntress in a horned beast headdress",
          "pose": "resting a bow on her shoulder, leaning forward, cocky toothy grin, looking at viewer",
          "neg": SOFT_NEG + ", " + ARROW_NEG},
   "boss": {"type": "woman", "jp": "比叡",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, long legs, dark-skinned female, brown skin, pale mint hair, long braid, white hood, silver-grey eyes, prayer bead necklace, black bodysuit, long wooden staff, brown tail, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the mint-braided guardian in a white hood",
            "pose": "leaning on a long wooden staff, one arm open as if to pick someone up, big-sisterly grin, looking down at viewer",
            "height_note": "she is very tall and much taller than him",
            "neg": SOFT_NEG},
 },
 "places": {
   "trail":   "jungle entrance animal trail, damp earth, knee-high ferns, footprints",
   "hunt":    "northern jungle hunting ground, dim under a high canopy, giant tree roots, moss",
   "watch":   "treetop lookout platform, wooden planks on thick branches, rope railing, sea of green treetops",
   "hammock": "hammock woven from vines between two trees, dappled sunlight through leaves",
   "village": "amazon warrior camp, stilt huts, campfire, hanging furs",
   "dojo":    "training ground of packed earth, wooden training dummies, jungle around",
   "paddy":   "terraced rice paddies full of water, narrow earthen footpath, warm mud",
   "river":   "slow river of thick pale glossy water, slippery stones in the shallows, flowers on the bank",
   "falls":   "waterfall basin, roaring waterfall, fine spray, mossy rocks, rainbow",
   "spring":  "steaming hot spring surrounded by rocks, thick steam, jungle flowers",
   "bridge":  "five-tiered rope suspension bridge over a deep gorge, wooden planks and thick ropes, a wooden checkpoint gate",
   "oilhut":  "hut interior, clay jars of scented oil, fur rugs, warm lamp light",
   "shrine":  "mossy stone shrine, an old tree with many red braided cords tied on it, a flat stone",
   "feast":   "feast square at night, a large bonfire, drums, dancing shadows",
   "tent":    "inside a red and black great tent, incense smoke, bed of layered furs, sword rack, bundles of red braided cords hanging",
   "lodge":   "hunter's hut interior, furs on the floor, bows and quivers on the wall",
 },
 "atk": {
   "m1": ("feast", "he kneels before the bonfire, the chieftain stands over him gripping his chin and tilting his face up, staring down with glowing red eyes, grinning, his hips pushed out, " + CORD + ", knees trembling"),
   "m2": ("shrine", "he lies on his back on the flat stone, the chieftain leans over him, one hand pinching and rolling his nipple, two oiled fingers of her other hand in his anus, fingering, her green tail stroking his inner thigh, appraising grin, " + CORD),
   "m3": ("tent", "from side, he lies on his back on the layered furs with legs spread, the chieftain between his legs holding him, her penis in his anus, anal, kissing him deeply, tongues, saliva, his own penis separate, " + CORD, P),
   "e1": ("village", "he stands pressed against a hut wall behind her round gold shield, the blonde warrior pinches both his nipples with glowing warm fingertips, rolling them, giving orders, composed smile, his back arched, " + CORD),
   "e2": ("hunt", "he kneels under a giant tree, the ninja kneels close behind him, her mask pulled down, licking his ear, one hand rolling his nipple, the fingers of her other hand in his anus, fingering, spotted tail curled around his thigh, " + CORD),
   "e3": ("hunt", "he has fallen to his knees among the roots, " + ARROW + " on his chest and inner thighs, the huntress crouches in front flicking his nipple with her fingertip, cocky grin, bow in her other hand, " + CORD),
   "boss": ("bridge", "from side, the tall guardian stands holding him up face to face in her arms, his legs wrapped around her waist, his feet off the ground, lowering him onto her penis, anal, his own penis separate, he clings to her shoulders, " + CORD, P),
 },
 "atk_desc": {
   "m1": "the chieftain makes him kneel with her burning red gaze.",
   "m2": "the chieftain appraises her trophy, rolling his nipple and pressing inside with oiled fingers.",
   "m3": "the chieftain rewards him on the furs with a deep kiss while taking him from the front.",
   "e1": "the warrior controls his body by commanding his nipples left and right.",
   "e2": "the ninja teases his ear, nipple and rear all at once from behind.",
   "e3": "the huntress hunts his nipples after her soft arrows raise his sensitivity.",
   "boss": "the guardian lifts him off the ground and lowers him slowly in a standing embrace.",
 },
 "lose": {
   # 鞍馬 技1（灼眼）
   "btl_m1":     ("feast", "he kneels before the bonfire with his hips raised, the chieftain crouches holding his chin, staring into his face with glowing red eyes, two oiled fingers of her other hand in his anus, fingering, cum dripping untouched, " + CORD),
   "onani_m1":   ("spring", "kneeling alone at the edge of the hot spring, staring at his reflection in the water, one oiled hand reaching behind to stroke his own anus, penis untouched, the chieftain watches far away through the steam"),
   "inochi_m1":  ("shrine", "he stands before the old tree of red cords, the chieftain holds his chin and stares into his face with glowing red eyes, her other hand pinching his nipple, her green tail around his thigh, his knees giving way, " + CORD),
   "onedari_m1": ("tent", "he sits on the furs looking up, the chieftain sits facing him holding his face in one hand, glowing red eyes close to his, her other hand between his legs with fingers in his anus, fingering, a lamp with a red glass shade, cum dripping"),
   # 鞍馬 技2（★戦利品の検分）
   "btl_m2":     ("shrine", "he lies on his back on the flat stone, the chieftain leans over him rolling his nipple with one hand, two oiled fingers pressing deep in his anus, fingering, her green tail stroking his inner thigh, a gold bell on his wrist cord, cum on his stomach"),
   "onani_m2":   ("oilhut", "lying alone on a fur rug beside the oil jars, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, penis untouched, the chieftain watches far away from the doorway"),
   "inochi_m2":  ("village", "he stands inside a stilt hut with his hands on the wall, the chieftain behind him pinching his nipple, her oiled fingers in his anus, fingering, a red paint mark below his collarbone, " + CORD + ", legs trembling, cum dripping"),
   "onedari_m2": ("dojo", "he leans back against a wooden training dummy, the chieftain stands close rolling his right nipple, two oiled fingers of her other hand in his anus, fingering, counting grin, a blank wooden tag without text hanging from his neck, cum dripping"),
   # 鞍馬 技3（頭領の褒美）
   "btl_m3":     ("tent", "from side, he lies on his back on the layered furs with legs lifted, the chieftain over him holding his waist, her penis in his anus, anal, kissing him deeply, tongues, saliva trail, his own penis separate, cum on his stomach, " + CORD, P),
   "onani_m3":   ("hammock", "lying alone in the swaying vine hammock, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, the chieftain watches far below under the trees"),
   "inochi_m3":  ("tent", "from side, he sits on the chieftain's lap on the furs facing her, her penis in his anus, anal, the chieftain feeding him fruit wine mouth to mouth, kiss, wine dripping from his lips, a wooden cup, his own penis separate", P),
   "onedari_m3": ("falls", "from side, he lies on his back on a wet flat rock by the waterfall, the chieftain over him, her penis in his anus, anal, kissing him deeply, spray and rainbow, a green leaf ornament on a cord around his neck, his own penis separate, cum on his stomach", P),
   # 混登呂（★支配の乳首）
   "btl_e1":     ("village", "from side, he stands bent forward with his hands on the hut wall, the blonde warrior behind him without her breastplate, her penis in his anus, anal, both her hands pinching his nipples, a gold shield charm pinned on his chest cord, his own penis separate, cum dripping", P),
   "onani_e1":   ("dojo", "kneeling alone in the shadow of a wooden training dummy, pinching his own right nipple then left, lips moving as if giving orders, penis untouched, the blonde warrior watches far away across the training ground"),
   "inochi_e1":  ("paddy", "he kneels in the warm mud beside the narrow paddy path, the blonde warrior stands over him pinching his nipple with a glowing warm fingertip, her other finger pointing ahead, composed smile, mud on his knees, " + CORD + ", cum dripping"),
   "onedari_e1": ("village", "from side, by the campfire, he kneels on all fours on a fur, the blonde warrior kneels behind him, her penis in his anus, anal, reaching around to roll both his nipples, a blank notebook without text beside them, his own penis separate, cum dripping", P),
   # 御土（★影分身）
   "btl_e2":     ("hunt", "he kneels under a giant tree, the ninja kneels behind him with her mask pulled down, licking his ear, one hand rolling his nipple, two fingers of her other hand deep in his anus, fingering, a black cord tied around his neck, cum dripping untouched"),
   "onani_e2":   ("watch", "sitting alone at the foot of the lookout tree, one hand covering his own ear, the other hand rubbing his own nipple, hips shifting, penis untouched, the ninja watches far above from a branch"),
   "inochi_e2":  ("trail", "he stands on the animal trail looking back over his shoulder, the ninja close behind him, her mask pulled down, her tongue on his ear, her hand sliding over his nipple, spotted tail around his waist, " + CORD + ", knees trembling"),
   "onedari_e2": ("falls", "in a rock cave behind the waterfall, he stands with his wrists tied above his head with soft cords, the ninja presses against his back, licking his ear, her fingers stopped at his nipple and his anus, teasing, curtain of water, he trembles on the edge"),
   # 阿黒（★淫毒矢）
   "btl_e3":     ("hunt", "he lies on his back among the roots, " + ARROW + " on his chest and inner thighs, the huntress straddles his legs pinching and flicking his nipples, the tip of her jade green tail tickling his anus, a bowstring tied around his waist, cum on his stomach"),
   "onani_e3":   ("trail", "sitting alone hidden in the ferns, tracing faint pink round marks on his chest with a fingertip, flicking his own nipple, penis untouched, the huntress watches far away crouching on the trail"),
   "inochi_e3":  ("trail", "he lies face down on the trail before a hut, " + ARROW + " on his back, the huntress crouches over him, her jade green tail wrapped around his ankle, her hand under his chest pinching his nipple, a leather anklet on his ankle, grinning"),
   "onedari_e3": ("lodge", "he lies on his back on the furs with arms open, " + ARROW + " on his chest and inner thighs, the huntress kneels beside him flicking his nipple, the tip of her jade green tail pressing into his anus, laughing, cum on his stomach"),
   # 比叡（★立ち抱擁）
   "btl_boss":   ("bridge", "from side, at the checkpoint gate, the tall guardian stands holding him up face to face, his legs around her waist, his feet off the ground, her penis deep in his anus, anal, his own penis separate, he clings to her neck, a blank wooden pass tag without text on his neck, cum on her stomach", P),
   "onani_boss": ("watch", "leaning alone against the tree trunk on the lookout platform, one leg raised, sinking onto his own finger in his anus, the other palm pressing his lower belly, penis untouched, the guardian watches far away from the ladder"),
   "inochi_boss":("bridge", "from side, on the swaying top tier of the rope bridge, the tall guardian stands holding him up in her arms, his legs around her waist, her penis in his anus, anal, her palm glowing warm on his lower belly, a carrying strap over her shoulder, his own penis separate, cum dripping", P),
   "onedari_boss":("spring", "from side, in the steaming hot spring, the tall guardian stands waist-deep holding him up high in her arms, lowering him slowly onto her penis, anal, his legs around her waist, his arms around her neck, steam, his own penis separate, cum in the water", P),
 },
 "lose_desc": "keeps him in the jungle forever as the tribe's cherished trophy, a red braided cord with twelve knots on his wrist.",
 "onanie": {
   "master": ("oilhut", "lying on a fur rug, one hand pinching and rolling his own nipple, an oiled finger of the other hand in his own anus, penis untouched"),
   "e1": ("dojo", "kneeling, pinching his own right nipple then left as if obeying orders, penis untouched"),
   "e2": ("hunt", "sitting against a tree, one hand covering his own ear, the other hand rubbing his own nipple, penis untouched"),
   "e3": ("trail", "sitting in the ferns, tracing faint pink round marks on his chest and flicking his own nipple, penis untouched"),
   "boss": ("watch", "leaning against a tree trunk with one leg raised, sinking onto his own finger in his anus, palm pressing his lower belly, penis untouched"),
 },
 "magic": {
   "1": (None, "shrine", "a red braided silk cord with two fresh knots lying on a mossy stone, soft warm glow, close-up"),
   "2": (None, "feast", "a large tribal drum with a hide drumhead and two drumsticks standing alone at dusk, faint sound ripples in the air, distant jungle"),
   "3": ("m", "hunt", "tossing a round smoke bomb in one hand, sweet pink incense smoke swirling around her, playful bold grin"),
   "4": (None, "oilhut", "a clay jar of warm scented oil with a wooden ladle, glossy golden oil dripping, jungle flowers beside it, lamp light, jar without text"),
   "5": (None, "shrine", "a mossy stone shrine and an old tree with many red braided cords tied to its branches, quiet shafts of light, a single drum resting at its roots"),
 },
}
