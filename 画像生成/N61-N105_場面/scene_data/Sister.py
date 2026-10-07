# N64 女神教の告解室（Sister）画像データ。登場人物は全員20歳以上。全員女性。帳面・記録簿・目録・暦は文字なし。
# 本編キャラ（シスター・パイズリ処刑人・ぱふぱふ処刑人・クレリック・イージス）は本編の立ち絵を見ずに、本文の手がかり
# （修道服・胸に穴のある処刑服と覆面・斧・「胸は大きくない」クレリック・浮遊する盾と神器の盾）と役から決めた見た目。
# 構成表の注意どおり、敗北28本は主人公が見習いの黒い修道服（白い襟・ウィッグなし）のまま。
HABIT = "a plain black long-sleeved novice monk habit with a white collar, no veil, no wig"
HABIT_CHEST = HABIT + ", the front of the habit unfastened showing his flat chest"
HABIT_OPEN = HABIT + ", the hem of the habit lifted"
HABIT_BOTH = HABIT + ", the front unfastened showing his flat chest, the hem lifted"
ROSARY = "a rosary of pale beads around his neck"
ST = {"pen": "strapon", "hero_outfit": HABIT_BOTH}   # シスターの聖具（本文では白い革帯。build 側の既定は黒いハーネスなので色は書かない）

DATA = {
 "code": "Sister",
 "world": "grand white temple of a healing goddess religion in the city of Morgen, stone arches, stained glass, candlelight, detailed background",
 "bg": "interior of a grand white temple chapel, rows of wooden pews, altar with a statue of a goddess, colorful stained glass windows, candles, soft light",
 "josou": "a plain black long-sleeved novice monk habit with a white collar, no veil, no wig",
 "chars": {
   "m": {"strap": "white leather strap-on harness", "type": "woman", "jp": "シスター", "canon": True, "canon_img": "F08_Stand.png",
         "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, tall, nun, angel, blonde hair, long hair, green eyes, gentle droopy eyes, black and white nun habit, white wimple and black veil, silver rosary, gentle smile, gigantic breasts",
         "name": "the blonde nun in a black and white habit",
         "pose": "hands clasped in prayer under her huge chest, head tilted, serene gentle smile, looking at viewer"},
   "e1": {"type": "woman", "jp": "パイズリ処刑人", "canon": True, "canon_img": "EU22.png",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, executioner, red hair, long hair, pink eyes, black hood mask covering the top of her head, black leather executioner outfit with a large round opening over her cleavage, black gloves, black thigh boots, sweet smile, huge breasts",
          "name": "the red-haired executioner with a chest opening in her black outfit",
          "pose": "leaning forward pushing her cleavage through the round opening of her outfit, sweet teasing smile, looking at viewer"},
   "e2": {"type": "woman", "jp": "ぱふぱふ処刑人", "canon": True, "canon_img": "EU23.png",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, tall, executioner, dark brown hair, very long straight hair, purple eyes, black executioner dress with a deep neckline, dark red cloak, large executioner's axe, graceful ladylike smile, gigantic breasts",
          "name": "the brown-haired executioner lady with a large axe",
          "pose": "resting a large axe head-down beside her, one hand on her cheek, graceful ladylike smile, looking at viewer"},
   "e3": {"type": "woman", "jp": "クレリック", "canon": True, "canon_img": "EU85.png",
          "tags": "adult woman, mature female, mature face, 23 years old, adult proportions, beautiful detailed eyes, long legs, cleric, angel, light pink hair, short hair, brown eyes, small halo, white and gold cleric robe, short white cape, holding a healing staff, kind smile, small breasts",
          "name": "the pink-haired cleric in a white robe",
          "pose": "holding a healing staff with both hands, kind gentle smile, slight bow, looking at viewer"},
   "boss": {"type": "woman", "jp": "イージス", "canon": True, "canon_img": "EU69.png",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, long legs, very tall, angel, goddess guardian, white hair, very long hair, gold eyes, golden halo, white feathered wings, white and gold armored dress, holding a large sacred shield, several round shields floating around her, calm dignified smile, huge breasts",
            "name": "the white-haired angel with floating shields",
            "pose": "holding the sacred shield at her side, floating shields around her, calm dignified smile, looking down at viewer"},
 },
 "places": {
   "altar": "temple chapel in front of the altar, goddess statue, rows of pews, stained glass light",
   "nunroom": "nun's private bedroom in the temple, plain bed with white sheets, candle, small window",
   "punish": "underground stone punishment chamber of the temple, candelabras, a padded prayer kneeler, stone walls",
   "yard": "temple inner courtyard, an old wooden execution platform decorated with flowers, stone arcade",
   "cloister": "temple cloister at dusk, stone pillars and arches, long shadows, orange light",
   "infirmary": "temple infirmary, white beds with white curtains, herb shelves, bright window",
   "cathedral": "center of the great cathedral under huge stained glass windows, colored light beams, white marble floor",
   "confession": "narrow wooden confessional booth, lattice window, kneeler, dim candlelight",
   "choir": "choir seats of the chapel, folded white choir robes on a pew, organ pipes",
   "baptistery": "baptistery with a marble baptismal font of steaming holy water, white cloth, candles",
   "wardrobe": "temple vestry wardrobe room, racks of black habits and altar cloths, wooden shelves",
   "lodge": "pilgrim lodging room, simple bed with a thick wool blanket, candle, night",
   "scriptorium": "temple scriptorium, reading lectern, shelves of old books, ink pots, blank pages without text",
   "alcove": "narrow stone wall alcove in the cloister, three sides of stone, dim light",
   "fountain": "temple courtyard fountain with a goddess statue at sunset, stone rim, flowers",
   "belfry": "top of the temple bell tower at night, big bronze bell above, wooden floor, moonlight",
 },
 "atk": {
   "m1": ("altar", "he kneels before the altar, the nun kneels facing him with her fingers interlaced in prayer around his penis, slowly stroking, serene smile, his knees trembling"),
   "m2": ("nunroom", "he lies on the bed with his face buried in the nun's huge cleavage, the nun hugs his head and preaches softly, pressing her breasts on his cheeks, his body limp"),
   "m3": ("punish", "from side, he kneels bent over the padded kneeler, the nun kneels behind him pegging his anus with her strap-on, anal, reaching around pinching his nipples, his own penis separate", {"pen": "strapon"}),
   "e1": ("yard", "he kneels by the flower-decorated platform with his shirt open, the executioner presses the round opening of her outfit onto his chest, grinding her breasts over his nipples, sweet smile"),
   "e2": ("cloister", "he sits on the stone floor, the executioner lady has set her axe aside and pulls his face deep into her huge cleavage, cradling his head, his arms limp"),
   "e3": ("infirmary", "he lies on the white bed with his shirt open, the cleric sits beside him slowly stroking his nipples with her fingertips, whispering kindly, his body melting"),
   "boss": ("cathedral", "he is enclosed by floating shields, the white-haired angel holds his face and kisses him deeply, her fingers pinching his nipples, stained glass light"),
 },
 "atk_desc": {
   "m1": "the nun strokes him with hands clasped in prayer.",
   "m2": "the nun preaches to him while holding his face in her bosom.",
   "m3": "the nun performs the rite of holy punishment.",
   "e1": "the executioner grinds his nipples with her chest opening.",
   "e2": "the executioner lady needs no axe to execute him.",
   "e3": "the cleric heals his heart by stroking his nipples.",
   "boss": "the angel imprisons him in a cage of shields and a kiss.",
 },
 "lose": {
   # シスター 技1（祈りの手）
   "btl_m1": ("altar", "he kneels before the altar, the nun kneels facing him with her hands clasped in prayer around his penis, cum dripping between her fingers, serene smile, " + ROSARY, {"hero_outfit": HABIT_OPEN}),
   "onani_m1": ("confession", "kneeling alone at the kneeler in front of the confessional, hands clasped in prayer pressed to his chest, face buried in the cushion, arms squeezing his chest, penis untouched, the nun watches from the lattice window", {"hero_outfit": HABIT}),
   "inochi_m1": ("altar", "he kneels on the floor, the nun stands before him simply clasping her hands in prayer, no hands on him, his knees buckling, the hem of his habit wet, " + ROSARY, {"hero_outfit": HABIT}),
   "onedari_m1": ("confession", "he kneels at the lattice window of the confessional reading from a blank booklet without text, the nun on the other side clasps her hands, his body collapsing, " + ROSARY, {"hero_outfit": HABIT}),
   # シスター 技2（聖母の抱擁）
   "btl_m2": ("nunroom", "he lies on the nun's bed with his face buried in her huge cleavage, the nun hugs him preaching softly, her veil falling around him, cum on the sheets", {"hero_outfit": HABIT_OPEN}),
   "onani_m2": ("choir", "kneeling alone before a pew with his face buried in folded white choir robes, hands clasped in prayer, arms squeezing his own chest, penis untouched, the nun watches from the choir seats", {"hero_outfit": HABIT}),
   "inochi_m2": ("fountain", "he sits on the nun's lap by the fountain at sunset, face buried in her huge cleavage, his fingers gripping the hem of her habit, the nun pats his back, " + ROSARY, {"hero_outfit": HABIT}),
   "onedari_m2": ("altar", "he sits at the end of a pew, the nun beside him pulls his face into her huge cleavage and bounces her breasts, preaching, the hem of his habit wet", {"hero_outfit": HABIT}),
   # シスター 技3（聖罰の儀・ペニバン）
   "btl_m3": ("punish", "from side, he kneels bent over the padded kneeler, the nun kneels behind him pegging his anus with her strap-on, anal, pinching his nipples, his own penis separate, cum on the stone floor", ST),
   "onani_m3": ("baptistery", "kneeling alone at the rim of the baptismal font, face buried in a rolled white cloth, hands clasped in prayer, arms squeezing his own chest, murmuring, penis untouched, the nun watches from the doorway", {"hero_outfit": HABIT}),
   "inochi_m3": ("punish", "from side, he lies over the prayer kneeler, the nun behind him pegging his anus with her strap-on, anal, one hand pinching his nipple, candlelight, his own penis separate", ST),
   "onedari_m3": ("baptistery", "from side, he kneels at the steaming marble font, the nun behind him pegging his anus with her strap-on, anal, pinching both his nipples, his own penis separate, a blank catalog book without text", ST),
   # パイズリ処刑人（処刑服の穴で）
   "btl_e1": ("yard", "he kneels before the flower-decorated platform, the executioner presses the chest opening of her outfit onto his bare chest, grinding her breasts over his nipples, the hem of his habit wet", {"hero_outfit": HABIT_CHEST}),
   "onani_e1": ("wardrobe", "kneeling alone, pressing a soft altar cloth against his own chest and grinding it in circles over his nipples, penis untouched, the executioner watches from between the racks", {"hero_outfit": HABIT_CHEST}),
   "inochi_e1": ("yard", "at dawn he lies on his back on the wooden platform, the executioner straddles him pressing the round opening of her outfit onto his chest, grinding over his nipples, sweet smile", {"hero_outfit": HABIT_CHEST}),
   "onedari_e1": ("wardrobe", "in a dim room he sits on an old wooden bench, the executioner leans in grinding the chest opening of her outfit on his nipples, a thick blank record book without text beside, candle", {"hero_outfit": HABIT_CHEST}),
   # ぱふぱふ処刑人（斧はいらない）
   "btl_e2": ("cloister", "he sits on the stone floor, the executioner lady cradles his face in her huge cleavage, her axe leaning on a pillar, he is falling asleep, cum soaking his hem", {"hero_outfit": HABIT_OPEN}),
   "onani_e2": ("lodge", "curled up alone kneeling under a thick wool blanket over his head, hands clasped stroking his own chest, penis untouched, the executioner lady watches from the door holding her axe", {"hero_outfit": HABIT}),
   "inochi_e2": ("lodge", "he sleeps on the bed with his face buried in the executioner lady's huge cleavage, her axe leaning on the wall, moonlight, " + ROSARY, {"hero_outfit": HABIT}),
   "onedari_e2": ("belfry", "he lies with his head in the executioner lady's huge cleavage under the great bell, the executioner lady strokes his hair, her axe leaning on the wall, moonlight", {"hero_outfit": HABIT}),
   # クレリック（心の癒し）
   "btl_e3": ("infirmary", "he lies on the white bed, the cleric sits beside him slowly stroking both his nipples with her fingertips, kind smile, his body limp, the hem of his habit wet", {"hero_outfit": HABIT_CHEST}),
   "onani_e3": ("scriptorium", "kneeling alone before the reading lectern, slowly circling his own nipples with his fingertips, body relaxed, penis untouched, the cleric watches from between the shelves", {"hero_outfit": HABIT_CHEST}),
   "inochi_e3": ("infirmary", "he lies on the white bed, the cleric's small hand rests on his chest stroking his nipple, whispering into his ear, gentle smile, " + ROSARY, {"hero_outfit": HABIT_CHEST}),
   "onedari_e3": ("scriptorium", "he sits on the floor by candlelight, the cleric sits facing him stroking his nipples through his habit, praising him, a broom leaning on the shelf", {"hero_outfit": HABIT}),
   # イージス（盾の檻）
   "btl_boss": ("cathedral", "he kneels enclosed by floating shields, the white-haired angel kisses his forehead, stained glass light, his hem wet, " + ROSARY, {"hero_outfit": HABIT}),
   "onani_boss": ("alcove", "sitting alone with his back against the stone wall of the narrow alcove, sucking his own fingers, the other hand pinching his own nipple, penis untouched, the white-haired angel looks in from the entrance with her shield", {"hero_outfit": HABIT_CHEST}),
   "inochi_boss": ("cathedral", "he kneels surrounded by a ring of floating shields, the white-haired angel bends down kissing him deeply, her fingers pinching his nipples, golden halo glow", {"hero_outfit": HABIT_CHEST}),
   "onedari_boss": ("cathedral", "high near the stained glass he kneels inside a small cage made of floating shields, the white-haired angel kisses him through a gap, tongues, her fingers on his nipple", {"hero_outfit": HABIT_CHEST}),
 },
 "lose_desc": "keeps him in the temple forever as a devoted believer in a novice habit.",
 "onanie": {
   "master": ("confession", "kneeling with hands clasped in prayer, face buried in a pillow, arms squeezing his own chest, murmuring a sermon, penis untouched"),
   "e1": ("wardrobe", "pressing a soft cloth against his own nipples and grinding his chest in circles, penis untouched"),
   "e2": ("lodge", "under a wool blanket pulled over his head, face wrapped in warmth, stroking his own chest, penis untouched"),
   "e3": ("infirmary", "lying relaxed on the white bed, slowly stroking his own nipples with his fingertips, penis untouched"),
   "boss": ("alcove", "back pressed into the stone alcove, sucking his own fingers, the other hand pinching his own nipple, penis untouched"),
 },
 "magic": {
   "1": ("m", "altar", "the nun raises her hands and a warm golden blessing light with feathers pours down, serene smile"),
   "2": (None, "wardrobe", "a folded plain black novice habit with a white collar laid on a wooden bench, a rosary on top"),
   "3": (None, "confession", "an empty wooden confessional booth with a lattice window and a kneeler, dim candlelight, a faint pink glow"),
   "4": ("e3", "altar", "the cleric holds out a rosary with both hands offering it, kind inviting smile"),
   "5": ("boss", "cathedral", "the white-haired angel stands in the center of the great cathedral with her sacred shield, many shields floating in a circle, divine light"),
 },
}
