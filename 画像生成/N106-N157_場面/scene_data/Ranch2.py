# N113 緑の森の人間牧場（Ranch2）画像データ。登場人物は全員20歳以上。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。女性の責め手に筋肉の線は描かない。
# レジーナだけが双成種（ふたなり）。挿入（pen: penis）は「牧場主の登録」の本（atk m3／btl_m3・inochi_m3・onedari_m3）だけ。指・舌・脚先は pen なし。
# ユダの髪・瞳・服は資料に目印がない（「派手な服・がま口の財布」だけ）ので仮に決めた。立ち絵を見て tags を直すこと。
# 警備淫A・Bの制帽は原作どおり青（blue police cap）。髪・瞳には青系を使っていない（A＝ピンク髪・赤い瞳／B＝紫髪・すみれ色の瞳）。
# ラバクネの脚先は丸くなめらかで撫でるだけ（中に入れない）。尾は刺さない。牙の絵は書かない。警棒は服の上から軽くつつくだけ（叩かない・入れない）。
# 応援要請（二人がかり）の本も、絵は警備淫B1人＋主人公（3人以上を出さない）。主人公の左耳には文字のない黄色い耳標。
P = {"pen": "penis"}
TAG = "a blank yellow ear tag without text clipped on his left ear"
SUIT = "his whole body below the neck wrapped in a tight glossy black rubber suit woven of threads"
HOLES = "round openings in the suit over his nipples and between his buttocks"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
BATON_NEG = "hitting, beating, baton insertion, bruise"
DATA = {
 "code": "Ranch2",
 "world": "human ranch hidden in a deep green forest, long wooden fences, hay, wooden barns, a watchtower with a bronze bell, soft sunlight through the trees, detailed background",
 "bg": "ranch in a green forest in daytime, a long wooden fence with a gate, hay bales, soft grass, a wooden watchtower with a bronze bell far away, tall green trees all around, sunlight, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "レジーナ",
         "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, short hair, pointy ears, amber eyes, black hat with two round horns, flower ornament on the hat, white shirt, red vest, black bikini top under the shirt, white pants, red boots, thin black tail, soft curvy feminine body, large breasts",
         "name": "the blonde rancher in a round-horned black hat",
         "pose": "holding a broom in one hand, the other hand on her hip, slightly blushing proud smile, looking at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "守銭奴のユダ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, red-orange hair, side ponytail, green eyes, gaudy colorful patchwork jacket, striped scarf, short skirt, mismatched striped thighhighs, large gold clasp coin purse hanging at her hip, soft curvy feminine body, large breasts",
          "name": "the orange-haired bounty woman with a clasp purse",
          "pose": "leaping forward with both arms thrown wide open, wide excited grin, clasp purse swinging, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "警備淫A",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, medium hair, dog ears, red eyes, blue police cap, police officer uniform, black necktie, pencil skirt, white gloves, black police baton, whistle on a cord around her neck, fluffy dog tail, soft curvy feminine body, large breasts",
          "name": "the pink-haired dog-eared guard in a police cap",
          "pose": "pointing a police baton forward, other hand on her hip, tongue out, eager panting grin, tail wagging, looking at viewer",
          "neg": SOFT_NEG + ", " + BATON_NEG},
   "e3": {"type": "woman", "jp": "警備淫B",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, purple hair, short bob, dog ears, violet eyes, blue police cap, police officer uniform, black necktie, pencil skirt, black police baton at her hip, whistle on a cord around her neck, fluffy dog tail, soft curvy feminine body, large breasts",
          "name": "the purple-haired dog-eared guard in a police cap",
          "pose": "resting a police baton on her shoulder, the other hand twirling a whistle on its cord, easygoing lazy smile, looking at viewer",
          "neg": SOFT_NEG + ", " + BATON_NEG},
   "boss": {"type": "woman", "jp": "ラバクネ",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, platinum white hair, short hair, curled ram horns, black eye mask, yellow eyes, arachne, spider lower body, glossy black rubber spider lower body with eight smooth rounded legs, glossy black latex bodysuit on her upper body, curled smooth black tail, soft voluptuous feminine body, huge breasts, narrow waist",
            "name": "the platinum-haired rubber spider woman in a black eye mask",
            "pose": "holding a strand of glossy black thread between both hands like a tailor measuring, head tilted, gentle earnest smile, looking at viewer",
            "height_note": "she is much taller than him",
            "neg": SOFT_NEG + ", human legs on the spider woman, hairy spider legs, scary, stinger, fangs piercing skin"},
 },
 "places": {
   "trail":      "green forest path, dappled sunlight, damp earth, birds in the trees",
   "pit":        "bottom of a round pit trap lined with thick soft hay, earthen walls, a round patch of sky above",
   "fence":      "outside a long wooden ranch fence, hay beyond the rails, forest edge",
   "north":      "forest clearing of soft grass north of the ranch, glossy black threads stretched between the trees",
   "nest":       "cave nest strung with glossy black rubber threads, webs with a rubber sheen, cool dim light",
   "nw":         "muddy forest path northwest of the ranch, a hidden wooden hut, blank wanted posters without text on a tree",
   "hideout":    "cluttered hideout interior, piles of junk and trinkets, stacks of old books without text, sweets on a table, cushions",
   "gate":       "large wooden ranch gate, a wooden gatehouse wall beside it, hay on the ground",
   "guardhut":   "wooden guard hut interior, police caps hanging on the wall, a desk, a bench, a folded blanket, lamp light",
   "hutback":    "back of a wooden guard hut outdoors, plank wall, grass, stacked firewood",
   "quarantine": "clean wooden examination hut, white padded table, folded white cloths, glass bottles without text",
   "pasture":    "soft grassy pasture inside the wooden fence, warm sunny spot, hay bales",
   "barn":       "barn-like sleeping stalls, beds of hay, wooden stall partitions, a hanging lamp",
   "milking":    "quiet milking room, soft padded table, clear soft tubes and glass jars, dim warm light",
   "house":      "cozy house built of forest wood, flower decorations, a bed with a quilt, a warm kitchen with a table and chairs",
   "tower":      "wooden watchtower platform overlooking the whole ranch, a large bronze bell, sunset sky",
 },
 "atk": {
   "m1": ("pasture", "he stands in the grass with his knees giving way, the rancher holds her hat with one hand and tilts his chin up with the other, kissing him deeply, tongues, saliva trail, faint sparkles around their lips, wooden fence behind, " + TAG),
   "m2": ("barn", "he lies on his back on the hay bed, the rancher kneels between his legs with her shirt open and bikini top shifted, his penis squeezed between her breasts, paizuri, one hand rolling his nipple, oiled fingers of her other hand in his anus, fingering, her black tail stroking his inner thigh, " + TAG),
   "m3": ("house", "from side, he lies on his back on the bed with legs spread, the rancher between his legs holding him face to face, her penis in his anus, anal, kissing him deeply, tongues, saliva, his own penis separate, flower decorations, " + TAG, P),
   "e1": ("hideout", "he lies face down over a heap of cushions with his hips raised and trousers lowered, the bounty woman kneels behind him kissing his buttock, tongue out, two oiled fingers in his anus, fingering, laughing eyes, clasp purse swinging, " + TAG),
   "e2": ("gate", "he stands with both hands on the gatehouse wall, trousers lowered, the pink-haired guard close behind him, white-gloved fingers of one hand in his anus, fingering, her other hand resting the tip of a police baton lightly on his back, sniffing his neck, tongue out, tail wagging, " + TAG),
   "e3": ("guardhut", "he stands held close from the front, the purple-haired guard hugs his waist with one arm and pinches his nipple through his shirt with her other hand, rolling it, teasing smile, dog tail swaying, his knees weak, " + TAG),
   "boss": ("nest", "he hangs upright in a web of black rubber threads, " + SUIT + ", round openings in the suit over his nipples, the rubber spider woman looms over him licking his nipple, the rounded tips of her eight legs stroking his body all at once, calm smile"),
 },
 "atk_desc": {
   "m1": "the rancher numbs him with a sweet paralyzing kiss until his knees give way.",
   "m2": "the rancher tends her livestock, squeezing him between her breasts while rolling his nipple and pressing inside with oiled fingers.",
   "m3": "the rancher registers him on her bed, sealing his mouth with a numbing kiss while taking him from the front.",
   "e1": "the bounty woman kisses his rear and taps his secret button with her fingers.",
   "e2": "the guard inspects him from behind against the wall with her gloved fingers.",
   "e3": "the guard inspects his chest from the front and rolls the nipple she finds.",
   "boss": "the rubber spider woman wraps him in a rubber suit and strokes him with all eight legs.",
 },
 "lose": {
   # レジーナ 技1（パラライズキッス＋★家畜の世話）
   "btl_m1":     ("pasture", "he has collapsed on his back in the grass, the rancher kneels over him kissing him deeply, tongues, one hand rolling his nipple, oiled fingers of her other hand in his anus, fingering, a flower ornament pinned in his hair, cum dripping untouched, " + TAG),
   "onani_m1":   ("pit", "kneeling alone on the hay at the bottom of the pit, tracing his own lips with a fingertip, the other hand reaching behind to stroke his own anus, penis untouched, the rancher looks down from the round opening far above"),
   "inochi_m1":  ("gate", "he stands before the large wooden gate at dusk, the rancher holds his face with both hands and kisses him, tongues, saliva trail, her black tail around his waist, his knees giving way, " + TAG),
   "onedari_m1": ("house", "he sits on a wooden kitchen chair with his shirt open, the blushing rancher bends over him kissing his chest, one hand rolling his nipple, her other hand between his legs with fingers in his anus, fingering, cum dripping, " + TAG),
   # レジーナ 技2（★家畜の世話）
   "btl_m2":     ("barn", "he lies on his back on the hay bed, the rancher kneels between his legs, his penis squeezed between her breasts, paizuri, one hand rolling his nipple, two oiled fingers pressing deep in his anus, fingering, a blank wooden nameplate without text on the stall partition, cum on her breasts, " + TAG),
   "onani_m2":   ("fence", "kneeling alone leaning against the outside of the wooden fence, squeezing his own chest together with his arms, rolling his own nipple, an oiled finger in his own anus, penis untouched, the rancher watches far away beyond the fence"),
   "inochi_m2":  ("quarantine", "he lies on his back on the white padded table, a plain white tunic lifted to his chest, the rancher stands beside him rolling his nipple, two oiled fingers in his anus, fingering, gentle scolding smile, cum on his stomach, " + TAG),
   "onedari_m2": ("milking", "he lies on the soft padded table, the rancher leans over him, his penis squeezed between her breasts, paizuri, rolling his nipple as she counts, two oiled fingers in his anus, fingering, a clear soft tube lying unused beside them, cum on her breasts, " + TAG),
   # レジーナ 技3（牧場主の登録）
   "btl_m3":     ("house", "from side, he lies on his back on the bed with legs lifted, the rancher over him holding his waist, her penis in his anus, anal, kissing him deeply, tongues, saliva trail, his own penis separate, cum on his stomach, a glowing golden ear tag without text on his left ear", P),
   "onani_m3":   ("tower", "kneeling alone on the watchtower floor at sunset, his face buried in a pile of hay, hips raised, a finger pressing deep in his own anus, penis untouched, the rancher watches far away from the top of the ladder"),
   "inochi_m3":  ("house", "from side, morning light, he lies on his side on the bed, the rancher embraces him from behind, her penis in his anus, anal, kissing his lips over his shoulder, her hand rolling his nipple, two plates on the kitchen table behind, his own penis separate, cum dripping, " + TAG, P),
   "onedari_m3": ("house", "from side, he sits on the rancher's lap on the bed facing her, his legs around her waist, her penis deep in his anus, anal, the blushing rancher kissing him, tongues, her hands holding his hips, his own penis separate, cum on his stomach, " + TAG, P),
   # ユダ（★アナマグラ発進！）
   "btl_e1":     ("hideout", "he lies face down over a heap of cushions among the junk, hips raised, the bounty woman kneels behind him kissing his buttock, two oiled fingers tapping deep in his anus, fingering, a blank wanted poster without text on the wall, cum dripping untouched, " + TAG),
   "onani_e1":   ("nw", "crouching alone behind the hidden hut, kissing the inside of his own forearm, the other hand reaching behind with a finger at his own anus, penis untouched, the bounty woman peeks far away from behind a tree"),
   "inochi_e1":  ("nw", "he lies on his back in the grass beside the muddy path, the bounty woman pounces on top hugging him tightly, showering his cheek and neck with kisses, lipstick marks, her hand slipped under him with fingers in his anus, fingering, laughing, cum dripping, " + TAG),
   "onedari_e1": ("hideout", "he kneels on all fours on a rug among trinkets and treasure chests, the bounty woman behind him counting on the fingers of one hand, kissing his buttock, two fingers of her other hand in his anus, fingering, cum dripping, " + TAG),
   # 警備淫A（★身体検査・後）
   "btl_e2":     ("gate", "he stands bent forward with both hands on the gatehouse wall, trousers lowered, the pink-haired guard behind him, two white-gloved fingers deep in his anus, fingering, her baton tip resting on his back, sniffing, tail wagging, a round cap badge pinned on his collar, cum dripping untouched, " + TAG),
   "onani_e2":   ("hutback", "standing alone with one hand on the plank wall, the other hand reaching behind to stroke his own anus, hips pushed back, penis untouched, the pink-haired guard peeks far away around the corner of the hut"),
   "inochi_e2":  ("gate", "he stands with his hands on the large wooden gate, the pink-haired guard crouches behind him, white-gloved fingers in his anus, fingering, her other hand holding up one finger as if asking for one more time, tongue out panting, tail wagging, cum dripping, " + TAG),
   "onedari_e2": ("guardhut", "he kneels on all fours on a blanket on the floor, the pink-haired guard kneels behind him, two white-gloved fingers in his anus, fingering, her baton tip poking his hip lightly over his shirt, happy grin, tail wagging, cum dripping, " + TAG),
   # 警備淫B（★身体検査・前）
   "btl_e3":     ("guardhut", "he sits slumped on a bench against the wall, the purple-haired guard kneels in front of him between his knees, pinching and rolling both his nipples through his shirt, a blank name badge without text pinned on his chest pocket, teasing smile, a wet spot on his trousers, " + TAG),
   "onani_e3":   ("pasture", "sitting alone in a sunny corner by the fence, searching his chest over his shirt with his fingertips, pinching his own nipple through the shirt, penis untouched, the purple-haired guard watches far away leaning on the fence"),
   "inochi_e3":  ("gate", "he stands with his back against the gate post, his shirt unbuttoned, the purple-haired guard in front of him rolling both his nipples directly with her fingers, a whistle held between her lips, his legs trembling, cum dripping down his thigh, " + TAG),
   "onedari_e3": ("guardhut", "night, he sits on the floor against the wall with his shirt open, the purple-haired guard kneels close in front pinching both his nipples at once, pulling gently, pleased smile, a blank envelope without text on the desk, cum dripping, " + TAG),
   # ラバクネ（★ラバー糸の多脚責め）
   "btl_boss":   ("nest", "he hangs upright in the web, " + SUIT + ", " + HOLES + ", the rubber spider woman holds him licking his nipple, her fingers in his anus, fingering, rounded leg tips stroking his thighs and sides, a black rubber choker on his neck, cum dripping"),
   "onani_boss": ("north", "sitting alone at the foot of a tree, loose black rubber threads wound around his chest and waist, rubbing his own squeezed nipple over the threads, penis untouched, the rubber spider woman watches far above from a branch"),
   "inochi_boss":("nest", "he stands on a web platform with his arms held out by threads, " + SUIT + ", the rubber spider woman behind him adjusting the fit like a tailor, the rounded tip of one leg stroking his chest, two more finished black suits hanging on threads, he trembles, cum dripping"),
   "onedari_boss":("nest", "he lies in a hammock of black threads, " + SUIT + ", " + HOLES + ", the rubber spider woman leans over him licking his nipple, two fingers in his anus, fingering, her eight leg tips resting gently around him, cum dripping"),
 },
 "lose_desc": "registers him as the cherished livestock of the forest ranch, a yellow ear tag on his left ear, gently cared for every day.",
 "onanie": {
   "master": ("fence", "kneeling, squeezing his own chest together with his arms, rolling his own nipple, an oiled finger in his own anus, penis untouched"),
   "e1": ("nw", "crouching, kissing the inside of his own forearm, the other hand reaching behind to stroke his own anus, penis untouched"),
   "e2": ("hutback", "standing with one hand on the plank wall, the other hand reaching behind to stroke his own anus, penis untouched"),
   "e3": ("pasture", "sitting, searching his chest over his shirt and pinching his own nipple through the shirt, penis untouched"),
   "boss": ("north", "sitting against a tree, black rubber threads wound around his chest, rubbing his own squeezed nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "fence", "a blank yellow ear tag without text resting on a wooden fence rail, soft warm glow, close-up"),
   "2": ("e3", "gate", "blowing a silver whistle, one hand raised to call for backup, cheerful easygoing smile"),
   "3": (None, "pit", "a round pit trap seen from above, thick soft hay at the bottom, scattered leaves around the rim, gentle sunlight"),
   "4": (None, "house", "a glass bottle of golden flower oil without text on a wooden table, fresh ranch flowers and a cup of milk beside it, warm light, close-up"),
   "5": (None, "pasture", "a long wooden ranch fence with a closed gate and an iron lock, hay bales, a bell tower far away, quiet afternoon light"),
 },
}
