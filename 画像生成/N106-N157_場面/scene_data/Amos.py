# N149 聖山アモスの修道女たち（Amos）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# シスキュバス：原作は青い長髪 → pale lavender hair に置き換え（瞳は gold）。
# ラミア：原作は青い目・水色の蛇体 → violet eyes・pearl white の蛇体に置き換え。髪は honey gold の縦ロール。
# シスターラミア：原作は水色の頭巾と服 → pale mint and white の頭巾と服に置き換え。髪は platinum blonde の直毛（ラミアの金髪と被らせない）。蛇体は緑。
# ハイスラッグ娘：原作は黒髪の巻き毛 → ナメクジシスターの黒髪と被らせないため dark brown の巻き毛。
# 挿入はラミアの尻尾の先だけ（pen なし）。シスキュバスは指だけ。ほかの3人は後ろに触れない。
# 祝福の口づけ（m3）は院長が上に跨って迎える形（主人公は仰向けで動かない）。
# 蛇体の締め付けは苦しくない・粘液は溶かさない（痛み・消化・牙・毒を思わせる絵にしない）。主人公の首に白い珠の足されたロザリオ。
ROS = "a wooden rosary with white pearl beads around his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
SNAKE_NEG = SOFT_NEG + ", human legs on the woman, feet on the woman, open-mouthed snake, snake head, venom, biting, choking, pained face"
SLUG_NEG = SOFT_NEG + ", human legs on the woman, feet on the woman, melting skin, acid, dissolving, insect, grotesque, eye stalks"
DATA = {
 "code": "Amos",
 "world": "old white stone convent on a holy mountain, pilgrim path, candles and incense, stained glass light, clear mountain air, distant bell tower, detailed background",
 "bg": "interior of a convent cathedral on a holy mountain, tall stained glass windows casting colored light, rows of wooden pews, white stone pillars, many lit candles, an altar without text, mountains visible through a window, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "シスキュバス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale lavender hair, very long straight hair, gold eyes, short curved black horns, bat wings on her back, thin black demon tail with a spade tip, purple nun habit, purple veil, long sleeves, purple rosary, succubus, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the lavender-haired abbess in a purple habit",
         "pose": "hands clasped in prayer under her chest, serene gentle smile, wings slightly open, tail curled, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ラミア",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, honey gold hair, long drill hair, twin ringlets, hair ribbon, violet eyes, white frilled blouse, black skirt, lamia, snake lower body, very long pearl white snake tail with smooth fine scales and a slender tip, soft curvy feminine body, large breasts",
          "name": "the gold-ringlet lamia in a white frilled blouse",
          "pose": "upper body raised high on her coiled pearl white tail, one hand at her mouth in a haughty laugh, chin lifted, proud smile, looking down at viewer",
          "height_note": "raised on her coils she is much taller than him",
          "neg": SNAKE_NEG},
   "e2": {"type": "woman", "jp": "ナメクジシスター",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, black hair, long straight hair, pale grey eyes, half-closed eyes, black nun habit, black veil with a white band, slug girl, monster girl, the hem of her habit ends in a smooth glossy dark grey slug lower body instead of legs, glossy slime, soft curvy feminine body, large breasts",
          "name": "the black-haired slug nun in a black habit",
          "pose": "hands clasped in prayer, head slightly bowed, faint quiet smile, a glossy slime trail behind her, looking at viewer",
          "neg": SLUG_NEG},
   "e3": {"type": "woman", "jp": "ハイスラッグ娘",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, dark brown hair, curly hair, medium hair, yellow eyes, black wide-brimmed hat with a feather, black elegant dress, long sleeves, slug girl, monster girl, huge glossy yellow and black striped slug lower body instead of legs, glossy slime, soft curvy feminine body, large breasts, wide hips",
          "name": "the curly-haired slug lady in a black hat",
          "pose": "upper body upright on her large yellow and black slug body, one slime-wet hand extended in invitation, elegant relaxed smile, looking at viewer",
          "height_note": "on her large slug body she is much taller than him",
          "neg": SLUG_NEG},
   "boss": {"type": "woman", "jp": "シスターラミア",
            "tags": "adult woman, mature female, mature face, 32 years old, adult proportions, beautiful detailed eyes, tall, platinum blonde hair, very long straight hair, green eyes, gentle droopy eyes, pale mint and white sister veil, pale mint and white sister habit, lamia, snake lower body, very long emerald green snake tail with smooth scales, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the platinum-blonde lamia sister in a pale mint veil",
            "pose": "upper body raised on her coiled emerald green tail, both arms open as if to embrace, kind caring smile, looking down at viewer",
            "height_note": "raised on her coils she is much taller than him",
            "neg": SNAKE_NEG},
 },
 "places": {
   "tower":    "entrance of a damp stone tower at the foot of the mountain, mossy stones, glossy slime trails, a large bed of soft moss beside the door",
   "stairs":   "dim spiral stone staircase inside the tower, damp glossy handrail, a shadowed landing",
   "chapel":   "small chapel inside the tower, wooden pews, a small altar without text, candles, glossy wet floor",
   "foot":     "foot of the holy mountain at dawn, pilgrim signpost without text, long stone steps, morning mist",
   "trail":    "narrow mountain path, large rocks by the roadside, clear air, distant peaks",
   "rocks":    "shaded rocky hollow on the mountain, cool boulders, a flat rock like a bed in the shade",
   "spring":   "mountainside spring, clear cold water, a smooth prayer stone, waterside grass",
   "gate":     "white convent gate, pale banners, a bell tower above, a stone bench beside the gate",
   "court":    "convent courtyard, white flowers, a stone fountain, a smooth prayer stone",
   "cathedral":"convent cathedral, stained glass windows, colored light on the floor, wooden pews, candles",
   "confess":  "narrow confessional booth, lattice window, dark velvet curtains and cushions, dim light",
   "bedroom":  "simple convent bedroom, plain bed with a pillow and a blanket, pale curtains",
   "office":   "abbess's office, heavy wooden desk, a long couch, a wardrobe with purple habits, candles",
   "belfry":   "top of the bell tower, a large bronze bell overhead, open arches with a view of mountains, wind, a watchman's bedding on the floor",
   "offering": "small room beside the abbess's office, a white bed, many candles, incense smoke",
 },
 "atk": {
   "m1": ("cathedral", "he kneels on the stone floor with his shirt open, the abbess stands over him holding a glowing cross of soft light against his chest, her other hand raised in blessing, chanting, his hands clasped, knees trembling, " + ROS),
   "m2": ("office", "he sits on the long couch leaning into her, the abbess holds his face buried between her huge breasts, her habit open at the chest, one hand slowly stroking his nipple, her demon tail tickling his inner thigh, " + ROS),
   "m3": ("offering", "from side, he lies still on his back on the white bed, the abbess straddles his hips riding him, cowgirl position, leaning down to kiss him deeply, tongues, saliva trail, her wings spread, her hands on his chest, " + ROS),
   "e1": ("rocks", "he stands wrapped from ankles to chest in her pearl white snake coils, arms pinned, the lamia holds his chin looking down proudly, the slender tip of her tail slipping between his legs from behind into his anus, anal, calm unpained face, " + ROS),
   "e2": ("chapel", "he lies on a wooden pew with his wrists and ankles stuck down by glossy clear slime, shirt open, the slug nun leans over him with her hands clasped in prayer, her long glossy tongue licking his nipple, slime glistening on his chest, " + ROS),
   "e3": ("tower", "he lies on his back on the moss bed, the slug lady rests her huge yellow and black slug body over his legs and hips like a heavy blanket, her human upper body upright looking down at him, her slime-wet hand stroking his nipple, relaxed face, " + ROS),
   "boss": ("spring", "he is gently wrapped from feet to shoulders in her emerald green snake coils, only his head showing, the lamia sister holds his face against her huge breasts, stroking his hair, kind smile, his body relaxed and calm, " + ROS),
 },
 "atk_desc": {
   "m1": "the abbess presses a cross of light to his chest and makes him recite her prayer on his knees.",
   "m2": "the abbess wraps his face in her breasts while her hand and tail slowly caress him.",
   "m3": "the abbess seals his lips with a blessing kiss and takes him in while he lies still.",
   "e1": "the lamia coils around his whole body and strokes inside him with the tip of her tail.",
   "e2": "the slug nun sticks him down with warm slime and licks his nipples with her glossy tongue.",
   "e3": "the slug lady lies over him with her warm heavy slug body and drains him slowly.",
   "boss": "the lamia sister wraps him in her coils and holds his face to her chest to heal him.",
 },
 "lose": {
   # シスキュバス 技1（サニークロス＋★胸淫）
   "btl_m1":     ("cathedral", "he kneels in the colored stained glass light with his hands clasped, the abbess kneels before him pressing his face into her huge breasts, a glowing cross of soft light floating at his chest, her hand stroking his nipple, a purple rosary added around his neck, cum dripping untouched, " + ROS),
   "onani_m1":   ("court", "kneeling alone behind the prayer stone among white flowers, lips moving in prayer, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, glowing white beads on his rosary, the abbess watches far away beyond the flowers"),
   "inochi_m1":  ("gate", "he kneels before the white gate with his hands clasped, head bowed, the abbess stands over him holding a glowing cross of soft light above his chest, her other hand lifting his chin, serene smile, morning light, his knees trembling, " + ROS),
   "onedari_m1": ("offering", "he kneels on the white bed looking up, the abbess sits before him holding his face to her huge breasts, one finger raised as if counting, a glowing cross of soft light at his chest, candles, cum dripping untouched, " + ROS),
   # シスキュバス 技2（★シスターの胸淫）
   "btl_m2":     ("office", "he lies across her lap on the long couch, the abbess holds his face buried between her huge breasts, her habit open at the chest, two oiled fingers of her other hand in his anus, fingering, her demon tail tickling his inner thigh, a purple button in his hand, cum dripping untouched"),
   "onani_m2":   ("bedroom", "lying alone face down on the plain bed, face buried in a pillow, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched, glowing white beads on his rosary, the abbess watches far away from behind the curtain"),
   "inochi_m2":  ("confess", "in the narrow confessional, he kneels on a velvet cushion, the abbess sits close holding his face between her huge breasts, her hand stroking his nipple, whispering forgiveness into his ear, lattice window behind them, cum dripping, " + ROS),
   "onedari_m2": ("offering", "he sits sideways on the abbess's lap on the white bed, his face held between her huge breasts, her hand stroking his nipple, two oiled fingers of her other hand in his anus, fingering, a soft healing glow around her hand, cum on his stomach, " + ROS),
   # シスキュバス 技3（祝福の口づけ）
   "btl_m3":     ("office", "from side, he lies still on his back on the long couch, the abbess straddles his hips riding him, cowgirl position, leaning down kissing him deeply, tongues, saliva trail, her hand stroking his nipple, a signet ring on a cord around his neck, wings spread"),
   "onani_m3":   ("belfry", "kneeling alone straddling a pillow on the watchman's bedding under the large bell, sucking two of his own fingers as if kissing, penis untouched, glowing white beads on his rosary, the abbess watches far away from the top of the stairs"),
   "inochi_m3":  ("cathedral", "he stands before the altar with his head tilted back, the abbess holds his face in both hands kissing him deeply, tongues, saliva trail, her wings folding around him, her tail around his waist, colored light, his knees giving way, " + ROS),
   "onedari_m3": ("offering", "from side, he lies still on his back on the white bed, the abbess sits astride his hips without moving, cowgirl position, leaning down to hold his face against her huge breasts, whispering a prayer, candles and incense smoke, " + ROS),
   # ラミア（★ラミアロール）
   "btl_e1":     ("rocks", "he is wrapped from ankles to chest in her pearl white snake coils on the flat rock, arms pinned, the lamia leans over him smirking, the slender tip of her tail in his anus, anal, a hair ribbon tied on his rosary, calm unpained face, cum dripping untouched"),
   "onani_e1":   ("trail", "sitting alone in the shadow of a roadside rock, a thin cord wound tightly around his own chest and waist, one hand pulling the cord, a wet finger of the other hand stroking his own anus, penis untouched, glowing white beads on his rosary, the lamia watches far away from the top of the rock"),
   "inochi_e1":  ("trail", "he stands on the narrow path wrapped to the waist in her pearl white coils, arms raised in surrender, the lamia holds his chin, the tip of her tail stroking his inner thigh, haughty smile, his knees trembling, " + ROS),
   "onedari_e1": ("rocks", "he lies on the flat rock fully wrapped in her pearl white snake coils from ankles to shoulders, the lamia rests her chin on her hand looking down at him, the slender tip of her tail deep in his anus, anal, satisfied smirk, calm unpained face, cum dripping untouched, " + ROS),
   # ナメクジシスター（★ナメクジ胸舐め）
   "btl_e2":     ("chapel", "he lies on a wooden pew with wrists and ankles stuck down by glossy clear slime, his whole body glistening wet, the slug nun leans over him with hands clasped, her long glossy tongue licking his nipple, a black button on his rosary, cum dripping untouched"),
   "onani_e2":   ("stairs", "sitting alone in the shadow of the stair landing, shirt open, rubbing his own nipple with slime-wet fingertips, penis untouched, glowing white beads on his rosary, the slug nun watches far away from the stairs below"),
   "inochi_e2":  ("chapel", "he sits on a wooden pew with his hands clasped in prayer, shirt open, the slug nun kneels close with her long glossy tongue on his nipple, her hands clasped too, candles, his lips trembling mid-prayer, slime on his chest, " + ROS),
   "onedari_e2": ("chapel", "he lies on the floor before the small altar, his whole body covered in glossy clear slime, the slug nun leans over him pressing her slime-wet breasts through her open habit against his stomach, her tongue on his nipple, cum on his stomach, " + ROS),
   # ハイスラッグ娘（★スラッグドレイン）
   "btl_e3":     ("tower", "he lies on his back on the moss bed, the slug lady's huge yellow and black slug body covers him from feet to chest like a heavy blanket, her upper body upright looking down with a smile, hands not touching him, a black feather tucked in his rosary, relaxed dazed face, slime glistening"),
   "onani_e3":   ("stairs", "lying alone on his back in the shadow of the stair landing under a heavy quilt pulled up to his chest, one hand rubbing his own nipple, penis untouched, glowing white beads on his rosary, the slug lady watches far away from the stairs below"),
   "inochi_e3":  ("stairs", "he lies on his back on the stair landing, the slug lady's yellow and black slug body resting over his legs and hips, her upper body leaning down holding a lantern, her slime-wet hand on his cheek, elegant smile, " + ROS),
   "onedari_e3": ("tower", "he lies on the large moss bed with arms open, the slug lady's huge yellow and black slug body covering him up to the chest, her slime-wet hands stroking his nipples, her hat tilted, pleased smile, relaxed dazed face, slime glistening, " + ROS),
   # シスターラミア（★至福の蛇体）
   "btl_boss":   ("spring", "by the clear spring, he is gently wrapped from feet to shoulders in her emerald green snake coils, the lamia sister holds his face buried in her huge breasts, her hands not touching below, a strip of pale mint cloth tied on his rosary, relaxed calm face, cum dripping untouched"),
   "onani_boss": ("trail", "lying alone in the shadow of a roadside rock wrapped tightly in a blanket from shoulders to feet, one hand inside the blanket rubbing his own nipple, penis untouched, glowing white beads on his rosary, the lamia sister watches far away on the path"),
   "inochi_boss":("gate", "before the white convent gate, the lamia sister carries him wrapped in her emerald green snake coils, his arms clinging around her coils, his head resting on her chest, her hand stroking his hair, the bell tower above, relaxed sleepy face, " + ROS),
   "onedari_boss":("spring", "at the water's edge, he is wrapped to the chest in her emerald green snake coils, the lamia sister holds him from behind with her cheek against his head, her fingers gently stroking his nipple, kind smile, relaxed calm face, cum dripping, " + ROS),
 },
 "lose_desc": "keeps him in the mountain convent forever as its cherished prayer offering, a rosary with twelve white pearl beads around his neck.",
 "onanie": {
   "master": ("cathedral", "kneeling behind a pew, face buried in his rolled-up cloak, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched"),
   "e1": ("trail", "crouching behind a rock, a thin cord wound around his own chest and waist, pulling it tight, a wet finger stroking his own anus, penis untouched"),
   "e2": ("stairs", "sitting on the stair landing, shirt open, rubbing his own nipple with slime-wet fingertips, penis untouched"),
   "e3": ("stairs", "lying on his back under a heavy quilt on the stair landing, rubbing his own nipple, penis untouched"),
   "boss": ("trail", "lying behind a rock wrapped tightly in a blanket, one hand inside rubbing his own nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "cathedral", "a wooden rosary with two glowing white pearl beads lying on a stone altar without text, soft warm glow, close-up"),
   "2": (None, "belfry", "a large old bronze bell swinging in the bell tower, faint sound ripples in the air, mountains beyond the arches"),
   "3": ("m", "cathedral", "hands clasped in prayer, a soft warm healing light spreading from her hands, serene smile, wings slightly open"),
   "4": (None, "court", "a convent courtyard with white flowers and a stone fountain, faint glowing ripples of song drifting through the air, an open blank hymn book without text on the prayer stone"),
   "5": (None, "offering", "a white bed in a candlelit room, three lit candles on a stand, incense smoke curling, a wooden rosary with white pearl beads on the pillow"),
 },
}
