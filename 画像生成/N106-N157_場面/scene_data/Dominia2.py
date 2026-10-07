# N124 女権帝国の街角（Dominia2）画像データ。登場人物は全員20歳以上。5人とも人間の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（教官も引き締まった曲線の体つき）。
# 髪色の書き分け：ベルナ＝赤の縦ロール／ボルフェイノ＝短い淡い灰金（設計メモは金髪。ゼシーリアと被らないよう ash blonde に寄せた）／
#   ゼシーリア＝蜂蜜色の金の巻き髪／ヴィオレッタ＝濃い紫のボブ（設計メモに髪色の指定なし）／ソフィリア＝栗色の長い直毛（指定なし）。青・水色は不使用。
# 挿入（pen: strapon）はベルナの「頭領のドリル」の本だけ（atk m3・btl_m3・inochi_m3・onedari_m3）。指は pen なし。
# ドリルは工具として描かない（回る看板と指の回し方だけ）。鞭は持つだけで体に当てない。顔面騎乗は息ができる構図。
# ヴィオレッタの変装（キャット・レディ）は、取り調べの場面で「猫の耳の帽子と黒い手袋」を行為文に書く。主人公には着せない。
S = {"pen": "strapon"}
BOOK = "a leather passbook without text lying beside him"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
TOOL_NEG = "power drill, electric drill, tool in hand, machine, weapon"
WHIP_NEG = "whipping, whip marks, hitting, spanking"
DATA = {
 "code": "Dominia2",
 "world": "fantasy town of a matriarchal empire, cobblestone streets, flower beds and stone houses, a rocky mountain in the distance, warm daylight, detailed background",
 "bg": "cobblestone street of a green fantasy town in daytime, flower beds along stone houses, a church spire, a rocky mountain far away with a spinning drill-shaped signboard without text, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ベルナ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, very tall, long legs, red hair, long hair, drill hair, twin ringlets, amber eyes, black leather bodysuit, long black cape with red lining, black gloves, belt with a glass oil vial, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the red-ringlet gang boss in a black leather bodysuit and cape",
         "pose": "one hand on her hip, the other arm thrown out flaring her cape in a grand declaration, hearty open-mouthed laugh, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG + ", " + TOOL_NEG},
   "e1": {"type": "woman", "jp": "ヴィオレッタ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, dark purple hair, bob cut, violet eyes, garrison cap, dark grey security bureau uniform jacket, pencil skirt, black pantyhose, black gloves, handcuffs at her belt, well-balanced feminine body, large breasts",
          "name": "the purple-bob investigator in a garrison cap and uniform",
          "pose": "holding up a pair of handcuffs in one hand, a blank notebook without text in the other, serious confident smirk, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "ゼシーリア",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, honey gold hair, long curly hair, green eyes, white nun veil, black nun habit with a wide open back, long skirt, soft curvy feminine body, large breasts, very wide hips, huge ass",
          "name": "the gold-curled nun in a backless habit",
          "pose": "standing turned halfway showing her back and large hips, looking back over her shoulder, one hand at her cheek, elegant ladylike laugh, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ソフィリア",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, very long legs, chestnut brown hair, long straight hair, hazel eyes, white nun veil, short black nun dress, glossy black thighhigh stockings, slender feminine body, medium breasts, beautiful legs",
          "name": "the chestnut-haired nun in a short habit and black stockings",
          "pose": "sitting on a wooden bench with her legs crossed, one glossy stockinged foot extended toward the viewer, hands folded in prayer, gentle calm smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "ボルフェイノ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 31 years old, adult proportions, beautiful detailed eyes, very tall, long legs, pale ash blonde hair, very short hair, silver-grey eyes, peaked military cap, dark green military instructor uniform, tight trousers, black boots, white gloves, riding crop in her hand, toned curvy feminine body, large breasts, wide hips",
            "name": "the short-haired drill instructor in a peaked cap and military uniform",
            "pose": "standing straight with feet apart, tapping a riding crop against her own palm, stern commanding smirk, looking down at viewer",
            "height_note": "she is much taller than him",
            "neg": SOFT_NEG + ", " + WHIP_NEG},
 },
 "places": {
   "street":    "cobblestone street of a green town, flower beds, stone houses, shaded alley corner",
   "legchurch": "house converted into a chapel, altar draped with black stockings, incense smoke, framed paintings of legs",
   "chapel":    "quiet prayer room, long wooden bench, a padded footrest stand, candles, incense",
   "canal":     "canal city waterway, stone bridge, moored gondola, stone bench by the water",
   "hip1":      "chapel hall filled with large soft cushions, a rounded marble statue, incense smoke, stained glass",
   "hip2":      "nun's private room upstairs, soft wide bed, cushions, lace curtains, warm lamp",
   "bureau":    "security bureau office, stacks of blank papers, hard wooden chairs, filing cabinets",
   "interro":   "underground interrogation room, cold overhead lamp, bare desk, wooden chair, mirrored wall",
   "costume":   "costume storage room, racks of disguise outfits, a cat-ear cap on a shelf, a dressing mirror",
   "yard":      "military training ground, packed sand, wooden fence, flagpole, morning light",
   "office":    "instructor's office, hard cot, desk, a blank roster board without text on the wall, a glass oil vial",
   "railway":   "abandoned mountain railway, rusty rails, weeds, mountain wind, a tunnel mouth",
   "tunnel":    "inside an old railway tunnel, dim light from the far opening, rusty rails, a hanging lantern",
   "gate":      "hidden rock door on a rocky mountain, a spinning drill-shaped signboard without text above it, boulders",
   "warroom":   "hideout strategy room in a cave, a large map table, a blank hanging banner without text, lanterns",
   "bossroom":  "gang boss's bedroom in a cave, a large bed with red sheets, trophies on shelves, stone walls, warm lamps",
 },
 "atk": {
   "m1": ("warroom", "he kneels on all fours on the floor under the blank banner, the gang boss stands over him flaring her cape, one arm raised in a grand declaration, laughing boldly, an oiled fingertip of her other hand circling at his anus, his hips rising, " + BOOK),
   "m2": ("bossroom", "he kneels on all fours on the large bed, the gang boss kneels behind him pressing her chest against his back, two oiled fingers twirling in his anus, fingering, her other hand pinching and twisting his nipple, confident grin, his penis untouched, " + BOOK),
   "m3": ("bossroom", "from side, he kneels on all fours on the large bed, the gang boss kneels behind him pegging his anus with her strap-on, anal, one hand on his chin turning his face back, kissing him deeply, tongues, saliva trail, his own penis separate", S),
   "e1": ("interro", "he sits on a wooden chair with his wrists cuffed behind the chair back with padded handcuffs, the investigator wearing a black cat-ear cap straddles his lap face to face, her black-gloved fingers pinching both his nipples, whispering into his ear, teasing smirk"),
   "e2": ("hip1", "he lies on his back on a large cushion, the nun sits on his face facing his feet, facesitting, her large soft buttocks resting on his face with his nose free, she leans forward stroking his nipple with one hand and cupping his penis in her other palm, elegant smile"),
   "e3": ("chapel", "he kneels on the floor before the long bench, the nun sits on the bench above him, the toes of one glossy black-stockinged foot pinching his nipple, the sole of her other foot pressing circles on his lower belly, footjob, hands folded in prayer, gentle smile"),
   "boss": ("yard", "he stands in a half squat with his hands behind his head, the drill instructor stands close behind him, one hand pinching his nipple, two oiled fingers of her other hand in his anus, fingering, a riding crop tucked under her arm not touching him, his knees trembling on the edge"),
 },
 "atk_desc": {
   "m1": "the gang boss declares again and again that his rear has earned the honor of being first.",
   "m2": "the gang boss twirls her oiled fingers inside him while twisting his nipple.",
   "m3": "the gang boss takes him from behind and turns his face back for a deep kiss.",
   "e1": "the investigator interrogates him from his lap, toying with his nipples until he confesses.",
   "e2": "the nun blesses him by sitting on his face and slowly stroking him.",
   "e3": "the nun teaches him to worship her legs with her stockinged feet.",
   "boss": "the instructor makes him hold a stance and stops him on the edge again and again.",
 },
 "lose": {
   # ベルナ 技1（ドリル団の勧誘＋ドリルの指）
   "btl_m1":     ("warroom", "he kneels on all fours under the blank banner with his hips raised, the gang boss crouches behind him, one arm raised declaring loudly, two oiled fingers of her other hand twirling in his anus, fingering, a blank metal badge without text on a cord at his neck, cum dripping untouched"),
   "onani_m1":   ("tunnel", "kneeling alone on all fours between the rusty rails, one hand reaching behind to stroke his own anus, lips moving as if reciting, penis untouched, the gang boss stands far away at the tunnel mouth as a silhouette"),
   "inochi_m1":  ("gate", "he kneels on all fours on the rocks under the spinning signboard, the gang boss sits on a boulder beside him reading aloud from a blank scroll without text held in one hand, two fingers of her other hand twirling in his anus, fingering, he nods dreamily, cum dripping"),
   "onedari_m1": ("bossroom", "he kneels on all fours on the large bed looking back, the gang boss leans over his back with her lips at his ear whispering, two oiled fingers twirling in his anus, fingering, her other hand pinching his nipple, his hips pushed up, cum dripping untouched"),
   # ベルナ 技2（★ドリルの指）
   "btl_m2":     ("bossroom", "he kneels on the large bed with his chest down and hips raised, the gang boss kneels behind him, her breasts on his back, two oiled fingers twirling deep in his anus, fingering, her other hand twisting his nipple, a gold spiral charm on a cord at his neck, cum dripping untouched"),
   "onani_m2":   ("warroom", "kneeling alone on all fours beside the map table, an oiled finger of one hand circling inside his own anus, penis untouched, the gang boss watches far away from the doorway with her arms crossed"),
   "inochi_m2":  ("tunnel", "he stands bent forward with both hands on the tunnel wall, the gang boss stands behind him, two oiled fingers twirling in his anus, fingering, her other hand rolling his nipple, a hanging lantern, light from the far opening, legs trembling, cum dripping"),
   "onedari_m2": ("bossroom", "he lies face down across the foot of the large bed with his hips raised, the gang boss sits on the bed edge beside him, two oiled fingers twirling in his anus, fingering, her other hand raised counting on her fingers, proud grin, cum dripping untouched"),
   # ベルナ 技3（頭領のドリル）
   "btl_m3":     ("bossroom", "from side, he kneels on all fours on the large bed, the gang boss kneels behind him pegging his anus with her strap-on, anal, her hand on his chin turning his face back, kissing him deeply, tongues, saliva trail, a blank bronze plaque without text on the bedside shelf, his own penis separate, cum dripping", S),
   "onani_m3":   ("gate", "kneeling alone on all fours behind a boulder, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger pressed into his own anus, penis untouched, the gang boss watches far away from the rock door"),
   "inochi_m3":  ("warroom", "from side, at night, he bends forward over the large map table, the gang boss stands behind him pegging his anus with her strap-on, anal, leaning over him and turning his chin back to kiss him, lantern light, his own penis separate, cum dripping", S),
   "onedari_m3": ("bossroom", "from side, he lies on his side on the large bed, the gang boss lies behind him holding him in her arms, her strap-on in his anus, anal, turning his face back for a deep kiss, her fingers pinching his nipple, one pillow shared, his own penis separate, cum on the sheets", S),
   # ヴィオレッタ（★公安の取り調べ）
   "btl_e1":     ("interro", "he sits on the wooden chair with his wrists cuffed behind the chair back with padded handcuffs, the investigator wearing a black cat-ear cap straddles his lap face to face, black-gloved fingers rolling both his nipples, a blank card without text on a lanyard at his neck, cum dripping untouched"),
   "onani_e1":   ("costume", "standing alone with his wrists crossed behind his back, pressing his chest against the wall, hips rocking, penis untouched, racks of costumes, the investigator watches far away from the doorway"),
   "inochi_e1":  ("canal", "he sits on a stone bench by the canal with his wrists cuffed behind his back with padded handcuffs, the investigator sits astride his lap, one black-gloved hand pinching his nipple, her other hand holding a blank notebook without text, a gondola and a bridge behind, cum dripping"),
   "onedari_e1": ("interro", "he sits on the wooden chair with his wrists cuffed tightly behind the chair back, the investigator wearing a black cat-ear cap sits on his lap, one black-gloved hand rolling his nipple, the other tilting his chin up, mirrored wall behind, he talks breathlessly, cum dripping untouched"),
   # ゼシーリア（★巨尻の祝福）
   "btl_e2":     ("hip1", "he lies on his back on a large cushion, the nun sits on his face facing his feet, facesitting, her large soft buttocks on his face with his nose free, one hand stroking his nipple, her other palm slowly cupping his penis, a round blank badge without text on his chest cord, cum on his stomach"),
   "onani_e2":   ("hip2", "lying alone on his back on the soft bed, holding a large cushion over his own face with one hand, the other hand slowly stroking his own nipple, penis untouched, the nun watches far away from the doorway"),
   "inochi_e2":  ("hip1", "he lies on his back before the marble statue with his hands clasped in prayer on his chest, the nun lowers her large buttocks onto his face, facesitting, his nose free, her hand reaching forward to stroke his nipple, incense smoke, cum dripping"),
   "onedari_e2": ("hip2", "he lies on his back on the carpet at the foot of the nun's bed, the nun sits deep on his face facing his feet, facesitting, his nose free, both her hands slowly stroking his nipples, his penis untouched, cum dripping, elegant smile"),
   # ソフィリア（★美脚の教え）
   "btl_e3":     ("chapel", "he kneels on the floor before the long bench, the nun sits above him, the toes of one glossy black-stockinged foot pinching his nipple, the sole of her other foot pressing circles on his lower belly, a strip of black stocking tied around his upper arm, cum dripping untouched"),
   "onani_e3":   ("street", "sitting alone in the shade of a flower bed on the cobblestones, wearing only socks, pressing his own socked heel against his lower belly in circles, one hand on his chest, penis untouched, the nun watches far away down the street"),
   "inochi_e3":  ("legchurch", "he kneels before the stocking-draped altar kissing the nun's black-stockinged knee, the nun sits holding her leg out to him, the toes of her other foot pinching his nipple, hands folded in prayer, incense smoke, cum dripping untouched"),
   "onedari_e3": ("chapel", "he sits on the floor beneath the padded footrest stand looking up, the nun sits on the bench above him, the toes of one glossy black-stockinged foot pinching his nipple hard, the sole of her other foot pressing his lower belly, candlelight on the stockings, cum dripping untouched"),
   # ボルフェイノ（★鬼教官の特訓）
   "btl_boss":   ("yard", "he stands at attention with his back straight and arms at his sides, the drill instructor stands close behind him, one hand pinching his nipple, two oiled fingers of her other hand pressing in his anus, fingering, a riding crop tucked under her arm, a plain blank armband on his upper arm, cum dripping untouched"),
   "onani_boss": ("office", "standing alone at attention beside the hard cot, heels together, both hands pinching his own nipples, penis untouched, the drill instructor watches far away from the doorway with her arms crossed"),
   "inochi_boss":("yard", "in the morning light, he stands in a half squat with his hands behind his head, the drill instructor stands beside him, one oiled finger pressing in his anus, fingering, her other hand raised giving a command, a flagpole behind, his legs trembling on the edge"),
   "onedari_boss":("office", "he stands at attention before the desk, the drill instructor stands behind him with her chin over his shoulder, one hand rolling his nipple, two oiled fingers of her other hand in his anus, fingering, a riding crop lying on the desk, stern approving smirk, cum dripping untouched"),
 },
 "lose_desc": "has him carried off to the gang hideout and kept forever as the gang's cherished first trophy, his passbook filled with twelve stamps.",
 "onanie": {
   "master": ("street", "kneeling on all fours in a shaded alley corner, an oiled finger of one hand circling inside his own anus, penis untouched"),
   "e1": ("street", "standing with his wrists crossed behind his back, pressing his chest against a stone wall, hips rocking, penis untouched"),
   "e2": ("hip2", "lying on his back, holding a large cushion over his own face, the other hand slowly stroking his own nipple, penis untouched"),
   "e3": ("street", "sitting on the cobblestones wearing only socks, pressing his own socked heel against his lower belly in circles, penis untouched"),
   "boss": ("yard", "standing at attention with heels together and back straight, both hands pinching his own nipples, penis untouched"),
 },
 "magic": {
   "1": (None, "gate", "a round brass seal stamp with a spiral emblem resting on an open blank leather passbook, two fresh spiral ink marks without text, close-up"),
   "2": ("m", "gate", "pointing up at the spinning drill-shaped signboard, her cape flaring in the wind, shouting a rallying call, bold hearty laugh"),
   "3": (None, "interro", "a pair of steel handcuffs with soft padded lining lying open on the bare desk under the cold lamp, close-up"),
   "4": (None, "hip1", "a brass incense burner on a cushion, sweet pale smoke curling upward in soft light, close-up"),
   "5": (None, "street", "an open leather-bound passbook lying on the cobblestones, several round blank ink stamps without text on its pages, a faint spiral glow above it, close-up"),
 },
}
