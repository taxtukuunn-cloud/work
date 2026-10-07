# N125 中央の塔（LastTower）画像データ。登場人物は全員20歳以上。5人とも上級淫魔の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。全員、大きな胸とむっちりした太腿。筋肉の線は描かない。
# 青・水色のキャラはいない。淫女王とくノ一はどちらも黒髪の設定なので、絵では 淫女王＝jet black の下ろした長髪／くノ一＝紫がかった黒の一つ結び と書き分ける。
# 挿入は指だけ（pen なし）。淫女王の尻尾は内もも・手首に触れるだけで入れない。メイド・マッドサイエンティスト・ナースの絵では後ろに触れない。
# 注射器の先は肌に触れるだけで刺さない（傷・流血なし）。記録帳・カードに文字は描かない。
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
NEEDLE_NEG = "needle piercing skin, injection, stabbed, wound, tube in the body, scary"
DECK = "a leather deck case at his hip glowing faint pink"
CARDS = "blank cards with a glowing pink heart-shaped crest and without text"
TAIL = "her smooth black tail stroking his inner thigh"
DROP = "the blunt tip of a syringe resting on the skin beside his nipple without piercing, a single drop of pink liquid"
DATA = {
 "code": "LastTower",
 "world": "inside a tall stone tower in a fantasy town wrapped in sweet pink mist, cold stone walls, a stone spiral staircase, faint pink glow, detailed background",
 "bg": "throne room on the top floor of a tall stone tower, long red carpet, a black throne on a dais, tall arched windows showing a misty town far below, thin sweet pink mist, candle stands, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "淫女王",
         "tags": "adult woman, mature female, mature face, sharp adult features, 32 years old, adult proportions, beautiful detailed eyes, tall, long legs, jet black hair, very long straight hair, hair down, two curved black horns, red eyes, golden crown, black and red queen dress with an open neckline, black bat wings, smooth black succubus tail, soft voluptuous feminine body, huge breasts, thick thighs, wide hips",
         "name": "the horned queen in a black and red dress",
         "pose": "one hand on her hip, the other hand lazily waving, bored superior smirk, looking down at viewer with red eyes",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "メイド",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, chestnut brown hair, long hair, brown eyes, black maid dress, white apron, white maid headdress, soft curvy feminine body, huge breasts, thick thighs",
          "name": "the chestnut-haired maid in a white apron",
          "pose": "holding a silver tray at her side, one hand at the bib of her apron, composed teasing smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "マッドサイエンティスト",
          "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver hair, bob cut, amber eyes, glasses, open white lab coat, black leotard, soft curvy feminine body, large breasts, thick thighs",
          "name": "the silver-bob scientist in a lab coat",
          "pose": "pushing up her glasses with one finger, holding a round flask of pink liquid in the other hand, confident knowing smirk, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ナース",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, pink hair, medium wavy hair, green eyes, white nurse cap, white nurse uniform with an open neckline, white stockings, soft curvy feminine body, huge breasts, thick thighs",
          "name": "the pink-haired nurse in a white uniform",
          "pose": "leaning forward with one hand on her knee, holding up a syringe of pink liquid without a needle in the other hand, playful inviting smile, looking at viewer",
          "neg": SOFT_NEG + ", " + NEEDLE_NEG},
   "boss": {"type": "woman", "jp": "くノ一",
            "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair with a violet sheen, long high ponytail, violet eyes, purple cloth mask over her mouth, purple kunoichi outfit with an open neckline, white tabi socks, soft curvy feminine body, huge breasts, thick thighs",
            "name": "the ponytailed kunoichi in a purple outfit",
            "pose": "kneeling formally with one hand at the neckline of her outfit, the other hand gesturing politely to her side, calm quiet eyes, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "front":    "foot of a very tall stone tower in a closed misty town, heavy tower door, sweet pink mist on the cobblestones",
   "hall":     "entrance hall on the first floor of the tower, cold stone floor, a stone spiral staircase rising to the ceiling",
   "exam":     "examination room on the third floor of the tower, white curtains, a padded examination table, a metal tray, stone walls",
   "ward":     "sickroom in the tower, a white bed, a drip stand with a bag of pink liquid, white curtains, stone walls",
   "lab":      "laboratory on the fifth floor of the tower, glassware, bubbling flasks, shelves of bottles without labels, stone walls",
   "bench":    "experiment room in the tower, a soft padded experiment bench, a writing desk, thin sweet pink mist",
   "maidroom": "maid's waiting room on the seventh floor of the tower, a tea table, a silver tray, a teapot, chairs, stone walls with drapes",
   "bedroom":  "empty master bedroom in the tower, a luxurious large bed, heavy curtains, a neatly made room without an owner",
   "tatami":   "tatami room on the eleventh floor of the tower, tatami mats, a hanging scroll without text, an incense burner with thin smoke",
   "hidden":   "dim hidden room behind sliding doors, a futon on tatami, a paper lantern",
   "landing":  "landing of the stone spiral staircase, an arched window showing the misty town below, wind",
   "door":     "stone landing before the top floor, a heavy double door with four round seals without text, cold stone steps",
   "throne":   "throne room on the top floor of the tower, red carpet, a black throne, tall arched windows",
   "royalbed": "queen's bedchamber, a large canopy bed, red silk sheets, sweet haze, candlelight",
 },
 "atk": {
   "m1": ("throne", "he kneels on the red carpet looking up, the horned queen stands before the throne pulling the neckline of her dress open to show her deep cleavage, he opens his own shirt and pinches his own nipple, her smooth black tail holding his other wrist away, " + DECK),
   "m2": ("throne", "he lies on his back with his head sunk in the horned queen's thick thighs as she sits on the throne, the queen leans over so her huge breasts in the opened dress cover his face, one hand rolling his nipple, two oiled fingers of her other hand in his anus, fingering, " + TAIL),
   "m3": ("royalbed", "from side, he lies on his back on the red silk, the horned queen straddles him squeezing his penis between her thick thighs, kissing him deeply, tongues, saliva trail, her hand reaching down with two oiled fingers in his anus, fingering, her black wings folded around them"),
   "e1": ("maidroom", "he sits on a chair with his legs apart, the maid kneels between his knees with her apron bib lowered and her dress front opened, his penis held between her huge breasts, paizuri, slowly rocking, looking up with a composed smile, " + DECK),
   "e2": ("bench", "he lies dazed on the padded bench in pink mist, the scientist leans over him with her lab coat open, licking his nipple, her hand circling his lower belly, an open flask releasing mist, a blank notebook without text beside her, his penis untouched"),
   "e3": ("exam", "he sits on the examination table with his shirt opened, the nurse bends forward showing her deep cleavage before his face, " + DROP + ", her other hand pinching his other nipple, he stares at her chest"),
   "boss": ("tatami", "he sits on the tatami staring at her chest, the kunoichi kneels at his side with the neckline of her outfit pulled open, one fingertip stroking his nipple, the oiled fingers of her other hand in his anus, fingering, a bamboo oil tube on the mat"),
 },
 "atk_desc": {
   "m1": "the queen shows off her chest and makes him touch himself while watching.",
   "m2": "the queen sinks his head into her lap, covers his face with her chest and presses inside with her fingers.",
   "m3": "the queen pins him between her thighs and seals his lips while her fingers press deep.",
   "e1": "the maid shows him her service, holding him between her breasts.",
   "e2": "the scientist dazes him with sweet mist and tests his body with hand and tongue.",
   "e3": "the nurse fixes his eyes on her chest and examines his nipples with a drop of sweet medicine.",
   "boss": "the kunoichi holds his gaze with her chest while her careful hands work his nipple and prostate.",
 },
 "lose": {
   # 淫女王 技1（乳房の見せつけ）
   "btl_m1":     ("throne", "he kneels on the red carpet looking up, the horned queen stands over him holding her dress neckline open, her smooth black tail pinning his wrist, his free hand pinching his own nipple, " + CARDS + " scattered on the carpet, a red crown jewel on a cord at his neck, cum dripping untouched"),
   "onani_m1":   ("landing", "sitting alone on the stair landing by the arched window, holding up a blank card with a glowing pink crest and staring at it, the other hand rubbing his own nipple, hips shifting, penis untouched, the horned queen watches far away from the stairs above"),
   "inochi_m1":  ("door", "he lies on the stone step before the sealed double door with his head on the horned queen's lap, the queen sits on the step leaning over so her breasts in the opened dress cover his face, one hand rolling his nipple, two fingers of her other hand in his anus, fingering, cum dripping"),
   "onedari_m1": ("throne", "he sits on a rug at the foot of the throne looking up, the horned queen seated above leans forward with her neckline open, he rubs his own nipple counting, the queen's fingertip pinching his other nipple, her smooth black tail holding his wrist, cum dripping untouched"),
   # 淫女王 技2（★女王の膝枕）
   "btl_m2":     ("throne", "he lies on his back with his head sunk in the horned queen's thick thighs on the throne, a red lap blanket over his chest, the queen's huge breasts in the opened dress resting on his face, her fingers rolling his nipple, two oiled fingers deep in his anus, fingering, " + TAIL + ", cum on his stomach"),
   "onani_m2":   ("bedroom", "lying alone on the large bed with his head sunk in a pillow, his own jacket draped over his face, one hand stroking his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, the horned queen watches far away from the doorway"),
   "inochi_m2":  ("throne", "evening light through the tall windows, he lies drowsy with his head on the horned queen's lap on the throne, one black wing draped over him like a blanket, her breasts above his face, her fingers in his anus, fingering, " + DECK + ", cum dripping untouched"),
   "onedari_m2": ("royalbed", "on the canopy bed the horned queen sits back against the pillows, he lies with his head on her thick thighs, her huge breasts in the opened dress covering his face, two oiled fingers deep in his anus, fingering, " + TAIL + ", his toes curled, cum on his stomach"),
   # 淫女王 技3（女王の口づけ）
   "btl_m3":     ("royalbed", "from side, he lies on his back on the red silk, the horned queen straddles him squeezing his penis between her thick thighs, kissing him deeply, tongues, saliva trail, two oiled fingers of her hand in his anus, fingering, her black wings wrapped around them, a red silk ribbon tied on his wrist, cum between her thighs"),
   "onani_m3":   ("hidden", "lying alone on the futon with a pillow clamped between his thighs, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger pressing into his own anus, penis untouched, the horned queen watches far away from the opened sliding door"),
   "inochi_m3":  ("royalbed", "morning light through the canopy, he lies with his head on the horned queen's lap on the red silk, the queen bends down kissing him, tongues, her breasts against his cheek, two fingers of her hand in his anus, fingering, half of the wide bed left empty beside them, cum dripping"),
   "onedari_m3": ("royalbed", "from side, he lies on his side on the red silk facing the horned queen, her thick thighs clamped around his hips squeezing his penis between them, kissing him deeply, saliva, her hand behind him with two oiled fingers in his anus, fingering, morning light, cum on her thighs"),
   # メイド（★メイドのご奉仕）
   "btl_e1":     ("maidroom", "he lies on his back on a sofa, the maid lies over him chest to chest with her apron bib lowered and dress front opened, the tips of her breasts rubbing his nipples, her thick thighs clamping his hips, a white frill ornament pinned on his collar, " + CARDS + " on the tea table, cum on his stomach"),
   "onani_e1":   ("bedroom", "sitting alone on the edge of the large bed, pressing his own chest together with both forearms and rubbing his own nipples against them, rocking, penis untouched, the maid watches far away from the doorway holding a silver tray"),
   "inochi_e1":  ("maidroom", "he stands with his arms raised wearing nothing, his clothes folded neatly on a chair, the maid stands against him with her dress front opened, the tips of her breasts rubbing his nipples, her thigh pressed between his legs, cum dripping untouched"),
   "onedari_e1": ("maidroom", "he sits on the tea chair, the maid straddles his lap with her thick thighs clamping his hips, her dress front opened, the tips of her breasts rubbing his nipples, a teacup steaming on the table, composed smile, cum dripping untouched"),
   # マッドサイエンティスト（★魅了の香り）
   "btl_e2":     ("bench", "he lies dazed on the padded bench in thick pink mist, the scientist leans over with her lab coat open, her leotard chest pressed to his arm, her tongue licking his nipple, an open flask in her hand pouring mist, a single blank notebook page without text on his chest, cum on his stomach untouched"),
   "onani_e2":   ("lab", "sitting alone on the floor between the shelves, sniffing an open glass bottle with a dazed face, one fingertip circling his own nipple, penis untouched, the scientist watches far away writing in a blank notebook"),
   "inochi_e2":  ("lab", "he sits slumped on a stool in pink mist, the scientist bends in front of him, her hand rubbing one nipple while her tongue licks the other, a brass key dangling from her finger out of his reach, glasses glinting, cum dripping untouched"),
   "onedari_e2": ("bench", "he lies on the padded bench breathing deeply from a flask the scientist holds to his face, pink mist, her tongue on one nipple and her fingers on the other, lab coat open, a blank notebook without text on the desk, cum on his stomach untouched"),
   # ナース（★魔乳の診察）
   "btl_e3":     ("exam", "he lies back on the examination table, the nurse leans over him with her deep cleavage swaying before his face, both her hands pinching and rolling his glistening pink-wet nipples, a syringe without a needle resting on the metal tray, a white cap ornament pinned on his shirt, cum on his stomach untouched"),
   "onani_e3":   ("ward", "lying alone on the white bed, one palm pressed on his own lower belly, the other hand pinching his own nipple, penis untouched, the nurse watches far away through the gap of the white curtain"),
   "inochi_e3":  ("exam", "he sits on a stool with his shirt opened, the nurse sits facing him leaning forward with her cleavage before his eyes, her palm circling his lower belly, her other hand pinching his nipple, a blank clipboard without text on the table, cum dripping untouched"),
   "onedari_e3": ("exam", "he sits on the examination table leaning back on his hands, the nurse stands between his knees, spreading a drop of pink liquid over his nipple with her fingertip, pinching his other nipple, her open neckline close to his face, cum dripping untouched"),
   # くノ一（★魔乳の誘惑）
   "btl_boss":   ("tatami", "he lies on his back on the tatami with his knees raised, the kunoichi kneels beside him leaning over with her outfit neckline open above his face, one hand rolling his nipple, two oiled fingers of her other hand in his anus, fingering, a purple cloth tied on his wrist, " + CARDS + " on the mat, cum on his stomach"),
   "onani_boss": ("hidden", "sitting alone on the futon in the dim hidden room with his head tilted back, carefully circling both his own nipples with his fingertips, penis untouched, the kunoichi watches far away from the gap of the sliding door"),
   "inochi_boss":("tatami", "he sits on a floor cushion holding a teacup stopped halfway, the kunoichi sits close at his side with her outfit neckline open, one hand inside his shirt on his nipple, the fingers of her other hand behind him in his anus, fingering, a tea set and thin steam, cum dripping untouched"),
   "onedari_boss":("tatami", "he sits on a floor cushion leaning back on his hands with his legs apart, the kunoichi kneels in front leaning forward with her outfit neckline open, one hand pinching his nipple, two oiled fingers of her other hand in his anus, fingering, a bamboo oil tube, cum dripping untouched"),
 },
 "lose_desc": "keeps him on the top floor of the tower forever as the queen's cherished pet hero, all twelve cards of his deck turned pink.",
 "onanie": {
   "master": ("landing", "sitting against the wall with his jacket draped over his face, one hand stroking his own nipple, the other hand reaching behind to stroke his own anus, penis untouched"),
   "e1": ("bedroom", "sitting on the bed edge, pressing his own chest together with both forearms and rubbing his own nipples, penis untouched"),
   "e2": ("lab", "sitting between the shelves, sniffing an open glass bottle with a dazed face, a fingertip circling his own nipple, penis untouched"),
   "e3": ("ward", "lying on the white bed, one palm on his own lower belly, the other hand pinching his own nipple, penis untouched"),
   "boss": ("hidden", "sitting on the futon with his head tilted back, carefully circling his own nipples with his fingertips, penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "two blank cards lying on the red carpet, their faces turning into a glowing pink heart-shaped crest pattern, soft warm glow, cards without text, close-up"),
   "2": (None, "hall", "a stone spiral staircase winding up into the dark height of the tower, faint pink light coming down from above, cold stone steps, quiet"),
   "3": ("e2", "lab", "pulling the stopper from a round flask, sweet pink mist swirling out around her, knowing smirk behind her glasses"),
   "4": ("e3", "exam", "holding up a syringe of pink liquid without a needle, a single pink drop at its blunt tip, playful wink"),
   "5": ("m", "throne", "sitting on the black throne with her legs crossed, chin resting on one hand, a vial of oil on the armrest, bored superior smile"),
 },
}
