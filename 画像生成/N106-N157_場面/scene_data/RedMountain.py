# N154 レド山の虫たち（RedMountain）画像データ。登場人物は全員20歳以上（虫の魔物と蛇神は数百歳の大人）。5人とも女性（ふたなりではない）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# モスキート娘：原作は紺色のポニーテール・黒と青の縞の腹 → 髪は dark violet、腹は black and violet striped と書く（紺・青は主人公と紛れるため使わない）。
# 捧げ物の羽根：原作設定は赤・緑・青・黄 → 絵では red, green and gold と書く（青を避ける）。蛇神の羽も同じ。
# 髪色の書き分け：蛇神＝黒（資料に髪の記述なし。羽の冠と褐色の肌が目印）／モスキート娘＝濃い紫／カイコ娘＝白／カマキリ娘＝淡い緑／モス娘＝茶。
# 挿入は蛇神の指だけ（pen なし）。張形・ふたなりなし。騎乗（蛇神の口づけ・カマキリ娘の抱え込み）は彼女が迎える形で、主人公は仰向けで動かない。
# 痛みなし：口吻は刺さらず吸い付くだけ。鎌は刃を向けない（腕の内側で抱えるだけ）。蛇の胴の巻きつきは苦しくない。怖い・グロテスクにしない。
FEA = "a few colorful red, green and gold feathers attached to his back between his shoulder blades"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, gore, fangs, sharp teeth, hairy insect legs, extra insect legs"
SNAKE_NEG = SOFT_NEG + ", human legs on the woman, choking, strangling, snake head, forked tongue"
MOSQ_NEG = SOFT_NEG + ", needle, stinger piercing skin, blood, wound, bite mark"
MANT_NEG = SOFT_NEG + ", blade touching skin, cutting, wound, blood, weapon pointed at him"
COIL = "her warm smooth serpent body coiled gently around his legs, waist and chest"
DATA = {
 "code": "RedMountain",
 "world": "fantasy red-rock mountain of insect monster women, lush green slopes, drifting golden scale dust, colorful feathers on the wind, clouds close by, detailed background",
 "bg": "mountain summit altar in daytime, a stone altar decorated with colorful red, green and gold feathers, red rocks, long stone stairs, distant green mountain ridges and a sea of clouds, drifting golden scale dust, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ケツァルコァトル",
         "tags": "adult woman, mature female, mature face, elegant adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, lamia, monster girl, dark-skinned female, brown skin, black hair, very long hair, golden eyes, crown of colorful red, green and gold feathers, gold jewelry, white and gold bandeau top, huge colorful feathered wings on her back, her lower body is a giant long serpent body with smooth emerald green scales, snake lower body, soft voluptuous feminine body, huge breasts",
         "name": "the feather-crowned serpent goddess with huge colorful wings",
         "pose": "raised on her coiled serpent body, huge colorful wings spread wide, one hand held out in invitation, proud gentle smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SNAKE_NEG},
   "e1": {"type": "woman", "jp": "モスキート娘",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, insect girl, monster girl, dark violet hair, high ponytail, red eyes, thin antennae, transparent insect wings, black bandeau top, black shorts, black and violet striped insect abdomen behind her hips, a thin soft pink proboscis tube with a soft lip-like tip, soft curvy feminine body, large breasts",
          "name": "the violet-ponytail mosquito woman with transparent wings",
          "pose": "hovering just above the ground with wings blurred, hands on her hips, leaning forward, cocky confident grin, looking at viewer",
          "neg": MOSQ_NEG},
   "e2": {"type": "woman", "jp": "カイコ娘",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, insect girl, monster girl, white hair, long fluffy hair, feathery white antennae, dark red eyes, fluffy white moth wings, white fur collar, white silk dress, her lower body is a large soft white silkworm body, white silk threads in her hands, soft voluptuous feminine body, huge breasts",
          "name": "the white-haired silkworm woman with white wings",
          "pose": "holding a skein of white silk thread between her hands, head tilted, calm gentle smile, looking at viewer",
          "neg": SOFT_NEG + ", human legs on the woman"},
   "e3": {"type": "woman", "jp": "カマキリ娘",
          "tags": "adult woman, mature female, mature face, sharp adult features, 26 years old, adult proportions, beautiful detailed eyes, long legs, insect girl, monster girl, pale green hair, short hair, thin antennae, yellow eyes, expressionless, green chitin armor breastplate, green chitin plates on her hips and thighs, folded green mantis scythes along her forearms, human hands, green mantis wings, green mantis abdomen behind her hips, slender curvy feminine body, large breasts",
          "name": "the green-armored mantis woman with folded scythes",
          "pose": "standing in tall grass with her scythe forearms folded against her chest, blades turned inward, silent steady stare, looking at viewer",
          "neg": MANT_NEG},
   "boss": {"type": "woman", "jp": "モス娘",
            "tags": "adult woman, mature female, mature face, gentle adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, insect girl, monster girl, brown hair, long wavy hair, feathery brown antennae, amber eyes, large brown moth wings with eye patterns, brown fur collar, beige dress, fluffy brown moth abdomen behind her hips, glittering golden scale dust around her, soft voluptuous feminine body, huge breasts",
            "name": "the brown-haired moth woman with large brown wings",
            "pose": "holding a softly glowing lantern in one hand, large wings half open, golden scale dust drifting, calm dreamy smile, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "gate":    "mountain trailhead, red earth path, a wooden signpost without text, a lookout stone by the path, morning light",
   "grass":   "mountainside meadow of chest-high grass, a bed of flattened grass deep inside, warm haze",
   "perch":   "treetop lookout, a platform on thick branches, green leaves, a bed of leaves on a branch, wide view of the slopes",
   "village": "insect village, houses made of giant leaves, a tree stump in the square, jars of golden honey",
   "cocoon":  "cocoon room, rows of large white silk cocoons, soft dim light, white silk threads across the ceiling",
   "hut":     "silk spinning hut interior, a wooden spinning wheel, bundles of white silk thread, a blanket and a rug on the floor, soft light",
   "swamp":   "misty swamp, shallow muddy water, giant floating leaves like islands, reeds, a bed of grass on the bank",
   "forest":  "dark forest at night, big tree roots, night dew, a distant warm light between the trees, drifting golden dust",
   "plaza":   "lantern plaza at night, a large never-fading insect lantern light, golden scale dust dancing in the glow, a soft bed under the light",
   "falls":   "mountain waterfall, fine spray, wet rocks, a flat rock by the basin",
   "rocks":   "red rock mountain path, a sun-warmed boulder, a fallen colorful feather in a crack of the rock, wind",
   "stairs":  "long stone stairs to the summit, feather decorations on both sides, strong wind, clouds close by",
   "sky":     "open sky high above the mountain, sea of clouds below, sunlight",
   "altar":   "summit stone altar decorated with colorful feathers, a rug of feathers on the altar, clouds around",
   "nest":    "inside a giant nest woven from colorful red, green and gold feathers, a soft bed of feathers, warm dim light, no wind",
 },
 "atk": {
   "m1": ("altar", "he stands entranced before the altar, the serpent goddess rises above him singing with her mouth open, her huge colorful wings spread wide, her serpent body swaying in a dance, glowing notes of light in the air, " + FEA + ", his knees giving way"),
   "m2": ("nest", "he is held upright in the nest, " + COIL + ", the serpent goddess behind him strokes his neck and nipple with the soft tip of her wing feathers, one brown hand between his legs with two wet fingers in his anus, fingering, calm smile, he trembles"),
   "m3": ("nest", "from side, he lies on his back on the feather bed, the serpent goddess straddles his hips, cowgirl position, vaginal, lowering herself onto him, leaning down to kiss him deeply, tongues, her huge wings folded around them both like a tent, he lies still"),
   "e1": ("swamp", "he has fallen on a giant floating leaf, the mosquito woman clings to him from behind with arms and legs wrapped around him, his shirt gone, her thin soft proboscis tube sucking on his nipple without piercing, her fingers pinching his other nipple, wings buzzing, cocky grin, " + FEA),
   "e2": ("cocoon", "he is wrapped up to the neck in a smooth white silk cocoon, only his head out, the silkworm woman holds the cocoon against her chest, one white hand slipped inside the cocoon stroking his nipple, silk threads trailing from her fingers, gentle smile, he looks drowsy"),
   "e3": ("grass", "from side, he lies on his back on flattened grass, the mantis woman straddles his hips, cowgirl position, vaginal, her folded scythe forearms hooked behind his back holding him close, blades turned away, her face close staring silently into his, he lies still"),
   "boss": ("plaza", "he sits limp under the lantern light, the moth woman kneels before him wrapping her large brown wings around him, his penis between her breasts, paizuri, golden scale dust drifting into his open mouth, pale white sparkling dust falling on his nipples, dreamy smile"),
 },
 "atk_desc": {
   "m1": "the serpent goddess sings and dances with spread wings until he lies down on the altar by himself.",
   "m2": "the serpent goddess coils around him, strokes him with her feathers and presses deep inside with her fingers.",
   "m3": "the serpent goddess seals his lips and takes him inside her, wrapped in her wings.",
   "e1": "the mosquito woman chases him down, clings to him and sucks on his nipple with her soft proboscis.",
   "e2": "the silkworm woman wraps him in a warm silk cocoon and strokes him inside it.",
   "e3": "the mantis woman holds him in her scythe arms and takes him inside her while staring silently.",
   "boss": "the moth woman makes him drunk on golden scale dust and squeezes him between her breasts inside her wings.",
 },
 "lose": {
   # ケツァルコァトル 技1（天空の蛇神）
   "btl_m1":     ("altar", "he lies on his back on the feather rug of the altar, " + COIL + ", the serpent goddess sings above him with wings spread, stroking his nipple with a wing feather, two fingers of her brown hand in his anus, fingering, cum dripping untouched"),
   "onani_m1":   ("falls", "sitting alone on the flat rock by the waterfall, head tilted listening to a distant song, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + FEA),
   "inochi_m1":  ("sky", "high in the sky, the serpent goddess flies with huge wings spread, holding him in the coils of her serpent body, singing close to his ear, a wing feather stroking his chest, he clings to her, sea of clouds below, " + FEA),
   "onedari_m1": ("nest", "he lies in the center of the feather nest looking up, " + COIL + ", the serpent goddess dances above him with wings spread wide, singing, her wing tips brushing his nipples, he reaches up toward her, cum dripping untouched"),
   # ケツァルコァトル 技2（★羽根愛撫と蛇の抱擁）
   "btl_m2":     ("nest", "he is held upright in the nest, " + COIL + ", the serpent goddess behind him covers his nipple with the soft flat of a wing feather, two wet fingers of her brown hand pressing deep in his anus, fingering, a bracelet of green scales on his wrist, cum dripping untouched"),
   "onani_m2":   ("rocks", "sitting alone in the shade of a sun-warmed boulder, stroking his own neck and nipple with a single fallen colorful feather, shirt open, penis untouched, " + FEA),
   "inochi_m2":  ("nest", "night in the nest, he lies asleep with an armful of gathered feathers, " + COIL + ", the serpent goddess lies beside him laying her wing over him like a blanket, stroking his nipple with a feather, gentle smile, " + FEA),
   "onedari_m2": ("nest", "he lies on his side on the feather bed, his whole body wrapped in her serpent coils, the serpent goddess behind him, wing feathers on both his nipples, two fingers of her brown hand in his anus, fingering, counting with a smile, cum on the feathers"),
   # ケツァルコァトル 技3（蛇神の口づけ）
   "btl_m3":     ("nest", "from side, he lies on his back in the center of the nest, the serpent goddess straddles his hips, cowgirl position, vaginal, kissing him deeply, tongues, saliva trail, her wings wrapped around them both, a feather ring on his finger, he lies still, cum overflowing"),
   "onani_m3":   ("altar", "kneeling alone on the altar straddling a rolled-up feather rug like a pillow, sucking two of his own fingers as if kissing, hips rocking on the pillow, penis untouched, " + FEA),
   "inochi_m3":  ("altar", "he kneels on the altar with his face lifted, the serpent goddess bends down holding his cheeks in both brown hands, kissing him deeply as a vow, tongues, her wings closing around him, her serpent body around his waist, the stairs down far behind them"),
   "onedari_m3": ("nest", "from side, dawn light, he lies on his back on the feather bed, the serpent goddess sits astride his hips taking him deep, cowgirl position, vaginal, not moving, kissing him softly, the tip of a wing feather on his nipple, he lies still, cum overflowing"),
   # モスキート娘（★モスキートドレイン）
   "btl_e1":     ("swamp", "he lies on a giant floating leaf, the mosquito woman clings to him from behind with arms and legs wrapped around him, her soft proboscis tube sucking on his reddened nipple without piercing, her fingers pinching the other nipple, a black and violet striped band on his wrist, cum dripping untouched"),
   "onani_e1":   ("swamp", "sitting alone in the grass on the swamp bank, pinching his own nipples and pulling them forward as if being sucked, shirt open, penis untouched, " + FEA),
   "inochi_e1":  ("swamp", "he has stopped running knee-deep in the muddy shallows, the mosquito woman hovers behind him clinging to his back, her soft proboscis tube sucking on his nipple without piercing, wings buzzing, laughing, his knees giving way, " + FEA),
   "onedari_e1": ("swamp", "he lies on his back on a giant floating leaf, the mosquito woman lies over his legs, his penis between her breasts, paizuri, her soft proboscis tube stretched up sucking on his nipple, cocky grin, cum on her chest"),
   # カイコ娘（★吸精の繭）
   "btl_e2":     ("cocoon", "he is wrapped up to the neck in a white silk cocoon among other cocoons, the silkworm woman cradles the cocoon against her chest, one white hand inside the cocoon stroking his nipple through thin silk, a white silk bracelet, he looks blissful and drowsy, wet stain spreading on the silk"),
   "onani_e2":   ("hut", "curled up alone under a blanket beside the spinning wheel, only his face showing, his hand inside the blanket rubbing his own nipple, penis untouched, feathers on his back making the blanket bulge"),
   "inochi_e2":  ("hut", "he sits by the spinning wheel holding a silk spool, white silk threads wound round and round his arms and body up to his chest, the silkworm woman winds more thread around him, her hand stroking his nipple through the silk, gentle smile"),
   "onedari_e2": ("cocoon", "he lies in a half-finished white silk cocoon, the silkworm woman leans over him adding one more layer of silk thread, her other hand slowly stroking his nipple inside the silk, he looks up asking for more, wet stain on the silk"),
   # カマキリ娘（★抱え込み）
   "btl_e3":     ("grass", "from side, he lies on his back on flattened grass, the mantis woman straddles his hips, cowgirl position, vaginal, her folded scythe forearms hooked behind his back, blades turned away, staring silently into his face from very close, a green chitin charm on his neck, he lies still, cum overflowing"),
   "onani_e3":   ("perch", "lying alone on the bed of leaves on a branch, hugging himself tightly with one arm wrapped around his own back, the other hand rubbing his own nipple, penis untouched, " + FEA),
   "inochi_e3":  ("gate", "at the trailhead by the lookout stone, he kneels with scattered blank cards without text on the ground, the mantis woman kneels holding him against her chest with her folded scythe forearms behind his back, blades turned away, staring into his face, her fingers pinching his nipple"),
   "onedari_e3": ("grass", "from side, deep in the tall grass, he lies on his back with arms open, the mantis woman sits astride his hips taking him deep, cowgirl position, vaginal, her scythe forearms holding his back, blades turned away, a faint nod, silent stare, he lies still, cum overflowing"),
   # モス娘（★恍惚の鱗粉）
   "btl_boss":   ("plaza", "he sits limp on the bed under the lantern light, the moth woman behind him wraps her large brown wings around him, golden scale dust drifting into his open mouth, pale white sparkling dust falling on his nipples, faint sparkles, a brown moth-wing charm on a cord at his neck, cum dripping untouched"),
   "onani_boss": ("forest", "sitting alone against a big tree root at night, staring blankly at a distant warm light, mouth half open, one hand rubbing his own nipple, shirt open, penis untouched, " + FEA),
   "inochi_boss":("plaza", "morning light, the lantern still glowing, he sits beside the lantern holding its pole like a keeper, the moth woman kneels behind him with her wings around his shoulders, blowing golden scale dust toward his face, her hand on his nipple, dazed smile"),
   "onedari_boss":("plaza", "he lies on the bed under the lantern, the moth woman kneels over his legs, his penis between her breasts, paizuri, her large brown wings spread above them, thick golden scale dust falling, he breathes it in deeply, pale white sparkling dust on his nipples, cum on her chest"),
 },
 "lose_desc": "carries him up to the summit nest to live forever as the serpent goddess's cherished mate, twelve colorful feathers on his back.",
 "onanie": {
   "master": ("rocks", "sitting in the shade of a boulder, stroking his own neck and nipple with a single colorful feather, penis untouched"),
   "e1": ("swamp", "sitting in the grass, pinching his own nipples and pulling them forward as if being sucked, penis untouched"),
   "e2": ("hut", "curled up under a blanket with only his face showing, rubbing his own nipple inside the blanket, penis untouched"),
   "e3": ("perch", "lying on a bed of leaves, hugging himself with one arm around his own back, the other hand rubbing his own nipple, penis untouched"),
   "boss": ("forest", "sitting against a tree root, staring blankly at a distant light, rubbing his own nipple, penis untouched"),
 },
 "magic": {
   "1": ("m", "altar", "singing with her eyes closed and one hand on her chest, huge colorful wings spread wide, glowing notes of light and two colorful feathers drifting on the wind"),
   "2": (None, "grass", "tall grass rippling in rings as if stirred by many unseen wings, faint shimmering sound ripples in the air, glittering dust, a few transparent wing glints between the stems"),
   "3": (None, "grass", "fine white silk threads stretched between tall grass stems like a soft net, glistening with dew, close-up"),
   "4": (None, "village", "a wooden bowl of thick golden honey on a tree stump, a wooden spoon dripping honey, warm sweet haze, bowl without text"),
   "5": (None, "nest", "a giant empty nest woven from colorful feathers on the mountain summit, one feather floating down, warm sunlight, sea of clouds beyond"),
 },
}
