# N150 雪のほこらの天使たち（SnowAngel）画像データ。登場人物は全員20歳以上（天使は人間より長く生きている大人）。5人とも女性（ふたなり・NHなし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（戦乙女も曲線のある体つき）。
# 髪色は被らせない：エデン＝灰色／トリニティ＝エメラルドグリーンのポニーテール／ウラヌス＝金髪／エリシエル＝若草色（pale yellow-green）／ヴァルキリー＝淡いラベンダー（兜の下。資料に髪色の指定がないためこのMOD用に決めた）。
# 氷の柱は brief では「青く光る」だが、主人公の髪と紛れないよう絵では pale glowing ice と書く。瞳も青・水色を使わない。
# 挿入はエリシエルの聖蔦だけ（蔦なので pen なし）。エデンは指だけ。トリニティは素股（ドレスは脱がない・中には迎えない）。ヴァルキリーは上に跨る騎乗（主人公は動かない）。
# 光の十字架は光でできた温かい輪で留めるだけ（釘・傷・磔の苦痛は描かない）。雪・氷・光はすべて痛くない。主人公の背中にシャツ越しの淡く白い結晶の光。
SNOW = "faint white snowflake-shaped marks glowing softly on his back"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary"
CROSS = "glowing rings of soft white light around his wrists and ankles holding him on a floating cross of white light, arms spread"
CROSS_NEG = SOFT_NEG + ", nails, wound, crucifixion, wooden cross, pain, suffering, rope burn"
VINE = "smooth thornless green vines wrapped loosely around his wrists, ankles and waist"
VINE_NEG = SOFT_NEG + ", thorns, tentacle monster, slime, horror"
BEAST_NEG = SOFT_NEG + ", claws, fangs, horse body, human legs on the beast angel, horror"
RIDE = "cowgirl position, her white underskirt spread over his hips hiding where they join"
RIDE_NEG = "man on top, he thrusts, he holds her hips"
SUMATA = "her white dress hem lifted to her thighs, his penis clamped between her soft thighs, thigh sex"
DATA = {
 "code": "SnowAngel",
 "world": "sacred snow shrine of angels in a snowy country, walls and pillars of pale glowing ice, soft white holy light, drifting snow and white feathers, quiet, detailed background",
 "bg": "ice corridor inside a snow shrine, rows of tall pale glowing ice pillars, white light leaking from the far end, drifting snow and white feathers, polished stone floor, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "エデン",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, long legs, grey hair, very long hair, golden eyes, angel, halo, many large yellow-green feathered wings, white and pale green robe, gold ornaments, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the grey-haired cherub with countless yellow-green wings",
         "pose": "many yellow-green wings spread wide behind her, both arms open in welcome, one palm glowing with soft white light, calm merciful smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ウラヌス",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, blonde hair, very long hair, pink eyes, angel, halo, monster girl, taur, huge fluffy pink beast lower body soft like a cloud, large pink feathered wings, white sleeveless top, gold necklace, soft voluptuous feminine upper body, huge breasts",
          "name": "the blonde angel with a huge fluffy pink beast body",
          "pose": "her huge fluffy pink beast lower body curled comfortably, large pink wings half open, one hand on her cheek, easygoing gentle smile, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg_remove": ["extra legs", "three legs", "four legs"],
          "neg": BEAST_NEG},
   "e2": {"type": "woman", "jp": "エリシエル",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale yellow-green hair, very long straight hair, green eyes, angel, halo, white feathered wings, white and green robe, smooth green vines with white flowers coiled around her arms and waist, white flower hair ornament, slender curvy feminine body, large breasts",
          "name": "the yellow-green-haired angel wrapped in flowering vines",
          "pose": "holding a golden fruit in one hand, a smooth vine with a round bud tip raised beside her, white flowers blooming, quiet faint smile, looking at viewer",
          "neg": VINE_NEG},
   "e3": {"type": "woman", "jp": "ヴァルキリー",
          "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale lavender hair, long braid, silver-grey eyes, angel, white feathered wings, silver winged helmet, silver armor, silver breastplate, white skirt, white thighhighs, soft curvy feminine body, large breasts, wide hips",
          "name": "the valkyrie in silver armor and a winged helmet",
          "pose": "a long spear held upright in one hand, a greatsword resting on the floor beside her, white wings half spread, dignified confident smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "トリニティ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, emerald green hair, high ponytail, violet eyes, angel, white feathered wings, long white dress, white long gloves, gold cross ornament, soft voluptuous feminine body, large breasts, wide hips",
            "name": "the green-ponytail angel in a long white dress",
            "pose": "a scale of light floating above one raised palm, a cross of soft white light floating behind her, white wings folded, strict composed expression, looking at viewer",
            "neg": CROSS_NEG},
 },
 "places": {
   "field":    "snowfield in a blizzard, white world, footprints fading in the snow",
   "gate":     "entrance of the snow shrine, a tall gate of ice, white light leaking from inside, a stone guard seat, no wind inside the gate",
   "corridor": "ice corridor, rows of tall pale glowing ice pillars, white breath, shadows behind the pillars",
   "valhall":  "valkyrie's hall, a silver armor stand, spears displayed on the wall, a high window of light, polished stone floor",
   "vinehall": "chapel of vines, green vines climbing the ice walls, white flowers, a bed woven from vines",
   "orchard":  "fruit garden in the snow, trees bearing golden fruits, white flowers, soft snow on the ground",
   "beast":    "hall of the holy beast, a huge bed of soft clouds, pink light, fluffy floor",
   "crosshall": "hall of the cross, a cross of soft white light floating in the air, a floating scale of light, white glowing floor",
   "spring":   "unfrozen prayer spring, softly glowing warm water, stone edge, dripping water",
   "belfry":   "bell tower of the snow shrine, a large bell, a view of snowy mountains, clear air",
   "bedroom":  "angels' sleeping room, feather quilts, large cushions, warm light, scattered feathers",
   "paragate": "gate of paradise, an arch of light, flowers at its foot, dazzling white beyond the gate",
   "garden":   "garden of paradise, flowers blooming in the snow, a white seat among the flowers, warm breeze",
   "throne":   "a high throne of ice at the deepest part of the shrine, halo light, drifting yellow-green feathers",
   "wings":    "inside a cocoon of countless yellow-green feathered wings, warm soft light, feathers all around, nothing else visible",
 },
 "atk": {
   "m1": ("throne", "he stands before the ice throne taking one step forward, the cherub spreads her countless yellow-green wings wide, a faint vision of a flower garden glowing between the feathers, her hand held out to him, his arms hanging loose, " + SNOW),
   "m2": ("wings", "he kneels wrapped in her yellow-green wings, the cherub holds his face buried between her breasts, her glowing white fingertips stroking his nipple, two fingers of her other hand in his anus, fingering, his penis untouched, " + SNOW),
   "m3": ("spring", "he sits limp at the edge of the glowing spring leaning into her wings, the cherub kisses him deeply, tongues, saliva, his arms hanging powerless, two fingers of her hand in his anus, fingering, " + SNOW),
   "e1": ("beast", "he sinks into the huge fluffy pink beast body up to his chest, the blonde angel bends down pressing his face between her breasts, her large pink wings closed around them, soft pink fur stroking his back and legs, " + SNOW),
   "e2": ("vinehall", "from side, he lies on the bed of vines with knees raised, " + VINE + ", bud tips of two vines sucking his nipples, a smooth round-tipped vine in his anus, the vine angel sits beside him watching quietly, white flowers, " + SNOW),
   "e3": ("valhall", "from side, he lies on his back on the stone floor, the valkyrie without her breastplate straddles his hips, " + RIDE + ", her white wings pinning his arms and brushing his chest, a greatsword laid on the floor, " + SNOW, {"neg": RIDE_NEG}),
   "boss": ("crosshall", "he is held upright, " + CROSS + ", the white-dress angel presses against him from the front, " + SUMATA + ", a scale of light tilting beside them, strict calm face, " + SNOW),
 },
 "atk_desc": {
   "m1": "the cherub shows him a vision of paradise between her wings until he walks into them himself.",
   "m2": "the cherub wraps him in countless wings, buries his face in her breasts and presses inside with her fingers.",
   "m3": "the cherub drains the strength from his body with a deep kiss while her fingers press inside.",
   "e1": "the beast angel sinks him into her huge soft body and strokes him all over.",
   "e2": "the vine angel binds him with holy vines that suck his nipples and stroke deep inside.",
   "e3": "the valkyrie caresses him with her wings and rides him as a reward while he lies still.",
   "boss": "the white-dress angel holds him on a cross of light and rubs him between her thighs while weighing his pleasure.",
 },
 "lose": {
   # エデン 技1（快楽の園）
   "btl_m1":     ("throne", "he walks into her open wings by himself, the cherub closes countless yellow-green wings around his back, pressing his face to her breasts, her glowing hand on his nipple, two fingers in his anus, fingering, a vision of a flower garden between the feathers, cum dripping untouched, " + SNOW),
   "onani_m1":   ("garden", "kneeling alone hidden among the flowers, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + SNOW + ", the cherub watches far away from the white seat"),
   "inochi_m1":  ("paragate", "he stands in the arch of light looking into a dazzling flower garden, the cherub stands behind him spreading her wings, wrapping them around him from behind, her glowing hand sliding over his nipple, his knees giving way, cum dripping, " + SNOW),
   "onedari_m1": ("wings", "he sits in her lap inside the cocoon of wings looking up at a glowing vision, the cherub holds him from behind, her glowing fingers rolling his nipple, two fingers of her other hand in his anus, fingering, cum on his stomach, " + SNOW),
   # エデン 技2（★楽園の胸慰）
   "btl_m2":     ("wings", "he kneels inside the cocoon of wings, the cherub holds his face deep between her breasts, soft white light shining on his chest, her fingertips rolling his nipple, two fingers pressing deep in his anus, fingering, a glass orb of light beside them, cum on his stomach"),
   "onani_m2":   ("bedroom", "lying alone curled up under a feather quilt, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched, " + SNOW + " shining through the quilt, the cherub watches far away from the doorway"),
   "inochi_m2":  ("throne", "he sleeps sitting in her lap on the ice throne, the cherub covers him with layer upon layer of yellow-green wings, his cheek on her breasts, her hand stroking his nipple, snow falling outside a far window, cum dripping, " + SNOW),
   "onedari_m2": ("wings", "he lies on his side in the center of the wings, the cherub lies behind him holding him, one more wing folding over him, white light on his nipples, two fingers of her hand in his anus, fingering, cum on the feathers, " + SNOW),
   # エデン 技3（福音の口づけ）
   "btl_m3":     ("wings", "he hangs limp in her arms inside the wings, the cherub kisses him deeply, tongues, saliva trail, his arms dangling powerless, two fingers of her hand deep in his anus, fingering, a fragment of halo light on his chest, cum dripping untouched"),
   "onani_m3":   ("spring", "kneeling alone at the stone edge of the glowing spring, sucking two of his own fingers as if kissing, the other hand reaching behind pressing a finger in his own anus, penis untouched, " + SNOW + " reflected on the water, the cherub watches far away in the light"),
   "inochi_m3":  ("throne", "he kneels before the ice throne with his head tilted up, the cherub bends down holding his chin and kissing him, tongues, his hands fallen open on the floor, his travel bag left behind him, cum dripping, " + SNOW),
   "onedari_m3": ("wings", "he lies limp on his back on a bed of feathers, the cherub leans over him in a long deep kiss, tongues, saliva, her fingers deep in his anus, fingering, her wings rocking him gently, cum on his stomach, " + SNOW),
   # ウラヌス（★聖獣の愛撫）
   "btl_e1":     ("beast", "he is sunk into the huge fluffy pink beast body with only his shoulders showing, the blonde angel presses his face between her breasts with both arms, large pink wings closed tight, a soft glowing dragon of light coiled above, a pink feather ornament on his chest, cum overflowing"),
   "onani_e1":   ("bedroom", "lying alone sunk face up in a large cushion, both hands rubbing his own nipples, hips lifting, penis untouched, " + SNOW + ", the blonde angel watches far away, her pink wing peeking from behind the cushions"),
   "inochi_e1":  ("belfry", "at the top of the bell tower beside the large bell, he is wrapped in the fluffy pink beast body, the blonde angel closes her pink wings in front of his face hiding the snowy mountains, her hand stroking his nipple, cum dripping, " + SNOW),
   "onedari_e1": ("beast", "he lies on top of the huge fluffy pink beast body on the cloud bed, the blonde angel squeezes his face hard between her breasts, soft fur rocking his whole body, her fingers pinching his nipple, gentle smile, cum overflowing, " + SNOW),
   # エリシエル（★聖蔦の吸精）
   "btl_e2":     ("vinehall", "from side, he lies on the bed of vines with legs raised, " + VINE + ", bud tips sucking both his nipples, a smooth round-tipped vine deep in his anus, the vine angel kneels beside him touching his cheek, a bracelet of woven vine on his wrist, cum dripping untouched"),
   "onani_e2":   ("orchard", "sitting alone in the shadow of a fruit tree, holding a white flower to his nose and breathing in, the other hand rubbing his own nipple, penis untouched, " + SNOW + ", the vine angel watches far above from a branch, her long hair hanging down"),
   "inochi_e2":  ("orchard", "he leans back into a cradle of vines under a tree of golden fruits, the vine angel feeds him a golden fruit mouth to mouth, kiss, juice dripping from his lips, his skin flushed, bud tips of vines on his nipples, cum dripping, " + SNOW),
   "onedari_e2": ("vinehall", "from side, he lies face up on the bed of vines breathing in white flowers, " + VINE + ", bud tips sucking his nipples, two smooth slender vines in his anus, the vine angel sits at his head stroking his hair, quiet smile, cum on his stomach"),
   # ヴァルキリー（★戦乙女の天羽）
   "btl_e3":     ("valhall", "from side, he lies on his back beside the armor stand, the valkyrie without her breastplate straddles his hips, " + RIDE + ", her white wings pinning his arms, a wing tip tickling his nipple, a feather ornament from her helmet on his chest, cum overflowing, " + SNOW, {"neg": RIDE_NEG}),
   "onani_e3":   ("gate", "sitting alone in the shadow of the ice gate, stroking his own neck and nipple with a single white feather, shoulders trembling, penis untouched, " + SNOW + ", the valkyrie watches far away holding her spear upright"),
   "inochi_e3":  ("valhall", "he stands empty-handed before her, a wooden practice sword dropped on the stone floor, the valkyrie brushes his neck and chest with the tips of her white wings, her hand on his cheek, his knees giving way, cum dripping, " + SNOW),
   "onedari_e3": ("valhall", "from side, he lies on his back on the floor, the valkyrie without her breastplate straddles him holding him tight against her breasts, " + RIDE + ", her white wings wrapped around his whole body, proud smile, cum overflowing, " + SNOW, {"neg": RIDE_NEG}),
   # トリニティ（★快楽の十字架）
   "btl_boss":   ("crosshall", "he is held upright, " + CROSS + ", the white-dress angel presses against him from the front, " + SUMATA + ", her gloved fingers pinching his nipple, a scale of light tilted heavily, a scale charm on his neck, cum between her thighs"),
   "onani_boss": ("corridor", "standing alone with his back against an ice pillar, both arms spread wide like a cross, rocking his hips in the air, hands not touching himself, penis untouched, " + SNOW + " reflected in the ice, the white-dress angel watches far away down the corridor"),
   "inochi_boss":("crosshall", "he is held upright, " + CROSS + ", the white-dress angel stands close, " + SUMATA + ", holding up a scale of light, one pan sunk low, strict face, cum dripping"),
   "onedari_boss":("crosshall", "he lies on the white glowing floor with arms spread, glowing rings of soft white light holding his wrists to the floor, the white-dress angel sits astride his hips, " + SUMATA + ", three scales of light floating above, faint smile, cum between her thighs"),
 },
 "lose_desc": "keeps him in the snow shrine forever as a resident of paradise, twelve white snowflake marks glowing on his back.",
 "onanie": {
   "master": ("corridor", "sitting wrapped in his cloak behind an ice pillar, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched, " + SNOW),
   "e1": ("bedroom", "sunk into a large cushion, both hands rubbing his own nipples, hips lifting, penis untouched, " + SNOW),
   "e2": ("orchard", "crouching behind a tree, breathing in a white flower, the other hand rubbing his own nipple, penis untouched, " + SNOW),
   "e3": ("gate", "sitting behind the ice gate, stroking his own neck and nipple with a white feather, penis untouched, " + SNOW),
   "boss": ("corridor", "back against an ice pillar, both arms spread wide like a cross, rocking his hips, hands not touching himself, penis untouched, " + SNOW),
 },
 "magic": {
   "1": (None, "corridor", "two white snowflake-shaped marks of light floating in the air side by side, soft warm glow, drifting white feathers, close-up"),
   "2": (None, "belfry", "a large shrine bell ringing alone, faint ripples of sound in the clear air, a white feather drifting down, snowy mountains far away"),
   "3": ("e2", "vinehall", "blowing glittering white pollen from a white flower on her palm, the pollen drifting forward, quiet faint smile"),
   "4": ("m", "throne", "one palm raised, soft pure white light pouring from her hand, yellow-green wings spread, calm merciful smile"),
   "5": (None, "belfry", "a tall bell tower of ice standing on a snowy peak, a large bell inside, clear sky, long echoes drawn as faint rings of light"),
 },
}
