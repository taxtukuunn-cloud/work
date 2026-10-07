# N134 入江の森の魔女（Witches）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# 女帝：原作は青い肌 → pale lavender-grey skin に置き換え（主人公の紺と紛れないよう青・水色は使わない）。瞳は gold。
# エレクトリック：原作は黄色メッシュの短い黒髪。堕天女（長い黒髪）と髪色が被らないよう dark charcoal grey hair＋yellow streaks と書く。
# セクレタリ・シャトレの髪と瞳は資料に記述が少ないのでこのMOD用に決めた（栗色のまとめ髪／金の巻き毛ボブ）。
# 挿入技はない。後ろに入るのは指（堕天女・セクレタリ）と宙に浮く手袋の指（シャトレ）だけ＝pen なし。エレクトリック・女帝は後ろに触れない。
# 宙に浮く手袋は「3人以上を出さない」ため、中身のない手袋だけ（腕・体は描かない）。ムチは当てない（鳴らすだけ・触れるのは柄）。
# エレクトリックの本（atk e1・btl／inochi／onedari の e1）は主人公が黒いラバースーツを着せられる（hero_outfit。女装ではない・体は変えない）。絵には契約書か羽衣を必ず入れる。文字は描かない。
PAPER = "a blank contract paper without text floating beside him, faintly glowing"
RUBBER = "a tight glossy black rubber bodysuit from neck to toe with zippers on the chest and lower belly, a corner of a blank contract paper without text peeking from the suit's chest pocket, flat chest"
R = {"hero_outfit": RUBBER}
ROBES = "soft pink, purple and black celestial robes"
WRAP = "a pink robe wrapped around his wrists, a purple robe around his ankles, a black robe around his waist, floating in the air"
GLOVES = "floating white satin gloves with nothing inside"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, blood, wound"
GLOVE_NEG = SOFT_NEG + ", extra person, third person, disembodied arms, severed hands, gore"
WHIP_NEG = SOFT_NEG + ", whipping, whip hitting skin, whip marks, bruise, choking, tight collar, blue skin"
ELEC_NEG = SOFT_NEG + ", pain, electrocution, burns, lightning strike, scream"
DATA = {
 "code": "Witches",
 "world": "seaside cove forest of witches at night, damp green trees, sea mist, moonlight, soft pink purple and black cloth drifting between the trees, detailed background",
 "bg": "cove forest at night, damp green trees and tree roots, a moonlit spring deep in the forest, an old wooden stage with pink purple and black curtains, thin celestial robes drifting between the trees, sea mist, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "堕天女",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long straight hair, purple eyes, alluring eye makeup, thin white celestial dress, pink purple and black celestial robes floating around her shoulders, hagoromo, gold hair ornament, soft curvy feminine body, huge breasts, wide hips",
         "name": "the long black-haired celestial witch in a thin white dress",
         "pose": "one hand at her cheek, robes floating around her, gentle angelic smile with teasing half-closed eyes, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "エレクトリック",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, dark charcoal grey hair, bright yellow streaked hair, short hair, yellow eyes, glossy black rubber bodysuit with yellow lines, many electric cables around her arms and waist, small static sparks around her, goggles on her head, soft curvy feminine body, large breasts",
          "name": "the short-haired electric witch in a black rubber suit",
          "pose": "snapping her fingers with one hand, the other hand on her hip, triumphant cheerful grin, small sparks around her, looking at viewer",
          "neg": ELEC_NEG},
   "e2": {"type": "woman", "jp": "シャトレ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, blonde hair, short wavy bob, green eyes, black silk top hat, black tailcoat, white shirt, red bow tie, black shorts, black tights, magician's cane, white satin gloves, floating white satin gloves around her, soft curvy feminine body, large breasts",
          "name": "the blonde magician witch in a tailcoat and top hat",
          "pose": "tipping her top hat with one hand, twirling a cane with the other, proud showman smile, two empty white gloves floating beside her, looking at viewer",
          "neg": GLOVE_NEG},
   "e3": {"type": "woman", "jp": "女帝",
          "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale lavender-grey skin, silver hair, very long hair, gold eyes, small gold crown, black and gold long dress, long black gloves, coiled black whip in her hand, soft curvy feminine body, huge breasts, wide hips",
          "name": "the silver-haired empress witch in a black and gold dress",
          "pose": "holding a coiled whip in one hand and a soft leather collar in the other, cool sadistic smile, chin raised, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": WHIP_NEG},
   "boss": {"type": "woman", "jp": "セクレタリ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, chestnut brown hair, hair bun, brown eyes, glasses, dark grey business suit jacket, white blouse, tight skirt, black tights, high heels, a stack of blank contract papers without text in her arm, fountain pen, soft curvy feminine body, large breasts",
            "name": "the bespectacled secretary witch in a business suit",
            "pose": "holding out a blank contract paper and a pen toward the viewer, polished business smile, one hand adjusting her glasses, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "town":     "night entertainment district back alley, neon lights without text, wet asphalt, distant crowd blur",
   "park":     "small park at the forest entrance at night, an empty swing with chains, a street lamp, a stone seat like a throne, rubble",
   "wall":     "inside a ring of piled concrete rubble walls in the park, quiet, cold sand on the ground, moonlight from above",
   "path":     "narrow cove forest path, damp green ferns, big tree roots, sea mist, distant waves",
   "road":     "forest clearing like a stage near the forest exit, fallen leaves, floating lanterns in the air",
   "labgate":  "entrance of an abandoned laboratory, rusty gate, broken windows, a low humming fence, dust",
   "generator":"generator room of an abandoned laboratory, cables everywhere, a large humming generator, small static sparks in the air",
   "workshop": "rubber suit workshop, black rubber suits hanging in a row, paper patterns without text, a fitting table",
   "village":  "witches' village in the forest at night, small huts, laundry and thin robes hanging on lines, warm lamp light",
   "office":   "contract office, a wooden desk, stacks of blank papers without text, a stamp and red ink pad, a wall clock without numbers",
   "lounge":   "reception room, a leather sofa, a low table with a cold cup of tea, framed photo without text",
   "spring":   "moonlit spring deep in the cove, thin robes floating on the water surface, cold clear water, moon reflection",
   "stage":    "old wooden stage deep in the forest, pink purple and black curtains, creaking boards, an old dressing room mirror",
   "beach":    "white sand cove beach at night, quiet waves, moon, bamboo poles with pink purple and black robes hung to dry",
   "bedroom":  "celestial robe bedchamber, a bed draped in layers of pink purple and black thin robes, soft warm light, sweet haze",
 },
 "atk": {
   "m1": ("stage", "he lies with his head on the celestial witch's lap on the old stage, the celestial witch strokes his cheek, her gentle smile turning into a teasing smirk, a pink robe sliding around his wrist, he blushes and trembles, " + PAPER),
   "m2": ("spring", "above the spring, " + WRAP + ", the celestial witch floats beside him pinching his nipple with one hand, two oiled fingers of her other hand in his anus, fingering, shirt opened, teasing laugh, " + PAPER),
   "m3": ("bedroom", "on the robe-draped bed, the celestial witch embraces him wrapped together in her robes, kissing him deeply, tongues, saliva, her hand reaching behind him with fingers in his anus, fingering, he goes limp in her arms"),
   "e1": ("generator", "round electric pads stuck on his chest over the nipples and on his lower belly, thin cables to her hand, the electric witch holds a small dial, grinning in triumph, tiny soft sparks, his back arched, knees trembling", R),
   "e2": ("road", GLOVES + " hold his wrists and ankles in the air, more gloves tickle his sides and pinch his nipples, one gloved finger in his anus, fingering, shirt opened, the magician witch stands aside twirling her cane and watching, " + PAPER),
   "e3": ("park", "under the street lamp he kneels on all fours wearing a soft leather collar with a thin chain, the empress witch stands over him holding the chain loosely, stroking his nipple with the rounded handle of her whip, gazing down with glowing gold eyes, " + PAPER),
   "boss": ("office", "he stands before the desk with his arms lowered and chest pushed out, shirt opened, the secretary witch stands close behind him, rolling his nipple with one hand, two oiled fingers of her other hand in his anus, fingering, business smile, a floating blank contract paper without text glowing beside them"),
 },
 "atk_desc": {
   "m1": "the celestial witch's gentle smile suddenly turns into a teasing one.",
   "m2": "the celestial witch binds him in three robes, drains his energy and presses inside with her fingers.",
   "m3": "the celestial witch kisses him wrapped in her robes while pressing inside with her fingers.",
   "e1": "the electric witch dresses him in a rubber suit in a second and sends sweet tingling through pads on his nipples.",
   "e2": "the magician witch's floating gloves hold him, tickle him and press inside.",
   "e3": "the empress witch charms him with her gaze, collars him and strokes him with the whip handle.",
   "boss": "the secretary witch adds contract clauses his body must obey while caressing his nipple and pressing inside.",
 },
 "lose": {
   # 堕天女 技1（天女の微笑み＋★羽衣拘束）
   "btl_m1":     ("stage", "on the old stage, " + WRAP + ", the celestial witch holds his chin, smiling gently then teasingly, her other hand pinching his nipple, shirt opened, cum dripping untouched, a torn piece of pink robe tied on his wrist"),
   "onani_m1":   ("village", "kneeling alone behind a hut among hanging laundry, one hand pinching his own nipple, the other hand reaching behind to his own anus, lips moving as if whispering to himself, penis untouched, " + PAPER + ", the celestial witch watches far away between the hanging robes"),
   "inochi_m1":  ("stage", "he stands on the stage wrapped in the stage curtain robes of pink purple and black, the celestial witch holds his hand gently and leans to his ear with a teasing smirk, her other hand in his opened shirt pinching his nipple, his knees giving way, " + PAPER),
   "onedari_m1": ("bedroom", "he lies on the robe-draped bed wrapped in a pink robe, the celestial witch leans over him whispering into his ear, gentle smile and teasing eyes, one hand pinching his nipple, two fingers of her other hand in his anus, fingering, cum on his stomach"),
   # 堕天女 技2（★羽衣拘束）
   "btl_m2":     ("spring", "above the moonlit spring, " + WRAP + ", the celestial witch pinches his nipple and presses two oiled fingers deep in his anus, fingering, the robes glowing faintly as they drain him, shirt opened, cum dripping into the water, a braided cord of three colored robes on his wrist"),
   "onani_m2":   ("beach", "kneeling alone in the shadow of the drying poles, thin cloth wound loosely around his own wrists and ankles, one hand stroking his own nipple, the other hand reaching behind to his own anus, penis untouched, the celestial witch watches far away in the moonlight"),
   "inochi_m2":  ("spring", "he stands waist-deep in the spring reaching for a floating robe, three robes of pink purple and black coiling around his arms and waist, the celestial witch behind him pinching his nipple, her fingers in his anus under the water, fingering, he leans back into her"),
   "onedari_m2": ("bedroom", "on the robe-draped bed, a pink robe around his wrists and a purple robe around his ankles, lifted slightly off the bed, the celestial witch kneels beside him counting on her fingers with a smirk, two oiled fingers deep in his anus, fingering, cum on his stomach"),
   # 堕天女 技3（羽衣の口づけ＋★羽衣拘束）
   "btl_m3":     ("bedroom", "on the robe-draped bed, " + WRAP + ", the celestial witch holds his face and kisses him deeply, tongues, saliva trail, her other hand behind him with two fingers in his anus, fingering, cum dripping untouched, a blank contract paper without text glowing above them"),
   "onani_m3":   ("stage", "sitting alone in the corner of the dressing room wrapped in a thin cloth, sucking two of his own fingers, the other hand reaching behind to his own anus, penis untouched, an old mirror, the celestial witch watches far away from the curtain"),
   "inochi_m3":  ("path", "he leans back against a tree bound to the trunk by a pink robe, the celestial witch presses against him kissing him deeply, tongues, saliva, her hand behind him with fingers in his anus, fingering, a distant exit lantern far down the path, " + PAPER),
   "onedari_m3": ("bedroom", "on the bed, wrapped together with the celestial witch in three robes of pink purple and black, the celestial witch kisses him long and deep, tongues, her fingers in his anus, fingering, his arms limp, cum on the robes"),
   # エレクトリック（★秒で特製ラバースーツ）
   "btl_e1":     ("generator", "he kneels on the floor, round electric pads on his chest over the nipples, thin cables, the electric witch crouches in front holding a dial and one pad, triumphant grin, tiny soft sparks, his back arched, a wet stain on the suit", R),
   "onani_e1":   ("workshop", "sitting alone in the shadow of a pattern shelf, rubbing a wool sweater sleeve and touching his own nipple with a fingertip, a tiny static spark, shirt opened, penis untouched, " + PAPER + ", the electric witch watches far away from the fitting table"),
   "inochi_e1":  ("labgate", "he stands with his hand on a big lever beside the humming generator, round electric pads on his chest with cables running to the machine, the electric witch behind him adjusting a pad on his nipple, laughing, his legs trembling", R),
   "onedari_e1": ("generator", "he sits on a stool with the chest zipper opened, round electric pads directly on his bare nipples, the electric witch holds up her fingers counting with a dial in her other hand, grinning, tiny soft sparks, a wet stain on the suit", R),
   # シャトレ（★宙に浮く手袋）
   "btl_e2":     ("road", "in the clearing, " + GLOVES + " hold his wrists and ankles in the air, other gloves pinch both his nipples, one gloved finger deep in his anus, fingering, shirt opened, the magician witch stands aside with her cane raised, proud smile, cum dripping untouched, " + PAPER),
   "onani_e2":   ("path", "sitting alone on a tree root wearing cloth gloves, tracing his own side and nipple with gloved fingertips as if tickling, shirt opened, penis untouched, " + PAPER + ", the magician witch watches far away on the path"),
   "inochi_e2":  ("road", "he sits on the fallen leaves, many " + GLOVES + " hold his arms and legs, gloves tickle his sides and nipples, one gloved finger in his anus, fingering, the magician witch pouts with puffed cheeks pointing her cane at him, floating lanterns, " + PAPER),
   "onedari_e2": ("road", "he stands in the clearing with arms raised, five pairs of " + GLOVES + " around him, gloves on his wrists, gloves pinching his nipples, one gloved finger in his anus, fingering, the magician witch bows with her top hat in hand, cum dripping, " + PAPER),
   # 女帝（★アブソリュート・テンプテーション）
   "btl_e3":     ("park", "under the street lamp he kneels on all fours wearing a soft leather collar with a thin loose chain, the empress witch sits on the stone seat holding the chain, stroking his nipple with the rounded handle of her whip, gazing down with glowing gold eyes, cum dripping untouched, " + PAPER),
   "onani_e3":   ("wall", "kneeling alone on all fours behind the rubble, his own belt looped loosely around his neck, one hand rubbing his own nipple, shirt opened, penis untouched, " + PAPER + ", the empress witch watches far away on top of the rubble"),
   "inochi_e3":  ("wall", "inside the rubble walls, he kneels on all fours on the cold sand looking back over his shoulder, the empress witch stands behind gazing at him with glowing gold eyes, the rounded whip handle under his chest stroking his nipple, a soft leather collar on his neck, " + PAPER),
   "onedari_e3": ("park", "he sits on his knees at the foot of the stone seat wearing a soft leather collar, the empress witch seated above lifts his chin with one finger, gazing long into his face with glowing gold eyes, the rounded whip handle rolling his nipple, shirt opened, cum dripping"),
   # セクレタリ（★契約追加）
   "btl_boss":   ("office", "he stands bent slightly over the desk with his chest pushed out, shirt opened, the secretary witch behind him rolling his nipple, two oiled fingers deep in his anus, fingering, reading from a blank contract paper without text in the air, business smile, cum on the desk, a blank name card without text"),
   "onani_boss": ("lounge", "kneeling alone behind the sofa, a blank slip of paper without text on the floor before him, one hand stroking his own nipple, the other hand reaching behind to his own anus, penis untouched, the secretary witch watches far away from the doorway"),
   "inochi_boss":("office", "he sits at the desk holding a pen over a blank form without text, the secretary witch leans over his shoulder from behind, one hand in his opened shirt pinching his nipple, her other hand behind him with fingers in his anus, fingering, three blank papers on the desk, his hand trembling"),
   "onedari_boss":("office", "he stands before the desk with arms at his sides and chest pushed out, the secretary witch writes on a blank contract paper without text with a fountain pen, tracing his nipple with the pen barrel, her other hand behind him with fingers in his anus, fingering, cum dripping, a bundle of blank copies"),
 },
 "lose_desc": "keeps him in the cove forest forever as the witches' shared permanent contractor, cherished gently every night.",
 "onanie": {
   "master": ("beach", "kneeling with thin cloth wound loosely around his own wrists and ankles, one hand stroking his own nipple, the other hand reaching behind to his own anus, penis untouched, " + PAPER),
   "e1": ("workshop", "sitting, rubbing a wool sweater sleeve and touching his own nipple with a fingertip, a tiny static spark, penis untouched, " + PAPER),
   "e2": ("path", "sitting on a tree root wearing cloth gloves, tracing his own side and nipple with gloved fingertips as if tickling, penis untouched, " + PAPER),
   "e3": ("wall", "kneeling on all fours with his own belt looped loosely around his neck, one hand rubbing his own nipple, penis untouched, " + PAPER),
   "boss": ("lounge", "kneeling with a blank slip of paper without text on the floor, one hand stroking his own nipple, the other hand reaching behind to his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "office", "a blank contract paper without text lying on a desk, dark ink seeping into the paper by itself, a fountain pen beside it, faint purple glow, close-up"),
   "2": ("m", "path", "sending one pink celestial robe flying through the trees with a wave of her hand, robes swirling around her, playful smile"),
   "3": (None, "generator", "small soft static sparks dancing between hanging cables, a humming generator, faint yellow glow in the dusty air"),
   "4": (None, "park", "a soft black leather collar with a thin chain leash resting on a stone seat, a coiled whip beside it, street lamp light, collar without text"),
   "5": (None, "spring", "pink, purple and black thin robes floating on a still moonlit spring, moon reflection, gentle ripples, sea mist"),
 },
}
