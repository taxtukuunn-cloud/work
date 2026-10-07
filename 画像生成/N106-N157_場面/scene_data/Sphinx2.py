# N112 砂漠のピラミッド（Sphinx2）画像データ。登場人物は全員20歳以上（何百年・何千年も王墓を守ってきた成人女性の番人たち）。女性のみ（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない。
# 原作で青／紺の部分：コブラ娘の髪は原作は紺 → dark emerald green hair に置き換え。スフィンクスの従える蛇は原作は青 → jade green snakes に置き換え。
# ネフェルラミアスは三姉妹でカード1枚。立ち絵だけ3人を1枚に（tags は長姉、pose に妹2人）。技CG・敗北CGは長姉1人＋主人公だけ（妹は描かない）。
#   立ち絵のネガには共通の 2girls が残る（場面側の人数を守るため外していない）。3人で撮る時はユーザー側で人物ごとに分けて指定する。
# 挿入はコブラ娘の尾の先だけ（体の一部なので pen なし）。ほかは指まで。毒針は丸い先が触れるだけで刺さらない。毒牙は噛まずに吸うだけ。
# はさみは力を入れずに手首を支えるだけ。ミイラ娘は健康な肌（腐敗・骸骨は描かない）。腕輪・壁の謎は文字なし。痛み・傷の絵は書かない。
GOLD = "gold bangles on his wrists and ankles and a gold collar necklace"
TAIL = "the slender smooth tip of her snake tail in his anus, anal"
STING = "the rounded tip of her scorpion tail touching his skin without piercing, a glistening pink drop"
WRAP = "wrapped from his feet to his neck in soft white bandages, only his nipples and hips left uncovered"
FING = "two oiled fingers of her other hand in his anus, fingering"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, horror"
LAMIA_NEG = SOFT_NEG + ", human legs on the lamia, feet on the lamia, crushing, choking, biting, fangs piercing skin, pain"
DATA = {
 "code": "Sphinx2",
 "world": "inside an ancient desert pyramid tomb, sandstone walls with faded wall paintings without text, flickering torches, gold ornaments, jars of scented oil, drifting incense smoke, detailed background",
 "bg": "torchlit corridor of an ancient royal tomb inside a pyramid, faded wall paintings without text, sandstone pillars, jars of scented oil, a warm golden glow from a treasure chamber far at the end, drifting incense smoke, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "スフィンクス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, black hair, very long straight hair, gold crown, gold eyes, tan skin, gold collar necklace, gold armlets, white egyptian halter top, sphinx, lion lower body, four lion legs with tawny fur, lion tail with a tuft, large white feathered wings, two slender jade green snakes resting on her shoulders, soft voluptuous feminine body, huge breasts",
         "name": "the black-haired sphinx with white wings",
         "pose": "reclining on her lion body with her human torso upright, chin resting on one hand, white wings half spread, amused haughty smile, looking down at viewer with gold eyes",
         "height_note": "she is much taller than him",
         "neg_remove": ["extra legs", "three legs", "four legs"],
         "neg": SOFT_NEG + ", human legs on the sphinx, lion head, beast face, claws scratching, snake biting"},
   "e1": {"type": "woman", "jp": "コブラ娘",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, dark emerald green hair, long hair, cobra hood behind her head, red eyes, slit pupils, large grey gauntlets, black bandeau top, gold neck ring, lamia, black and yellow-green cobra lower body, long snake tail with a slender smooth tip, soft curvy feminine body, large breasts",
          "name": "the green-haired cobra lamia with grey gauntlets",
          "pose": "rising on her coiled cobra body, one large gauntlet hand at her chin, proud teasing smile, looking down at viewer with red eyes",
          "neg": LAMIA_NEG},
   "e2": {"type": "woman", "jp": "サソリ娘",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, purple hair, very long hair, amber eyes, glossy black scorpion carapace armor fitted to her body, a pair of large black scorpion pincers at her sides, long segmented black scorpion tail with a rounded tip, soft curvy feminine body, large breasts, wide hips",
          "name": "the purple-haired scorpion woman in black carapace",
          "pose": "one hand on her hip, scorpion tail curled up over her shoulder, impatient confident smirk, looking at viewer",
          "neg": SOFT_NEG + ", insect legs, extra insect limbs, stinger piercing skin, stabbed, wound, pincers cutting"},
   "e3": {"type": "woman", "jp": "ミイラ娘",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, pale blonde hair, long hair, violet eyes, light brown skin, healthy smooth skin, body wrapped in clean white bandages, bandages around her chest and hips, loose bandage ends trailing from her arms, skin showing between the bandages, gold anklet, mummy woman, soft curvy feminine body, large breasts",
          "name": "the bandage-wrapped mummy woman with pale blonde hair",
          "pose": "standing straight with one hand holding out a loose end of white bandage, calm serious expression, looking at viewer",
          "neg": SOFT_NEG + ", rotting skin, zombie skin, skull, bones, decay, gore"},
   "boss": {"type": "woman", "jp": "ネフェルラミアス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, red skin, colored skin, silver-white hair, long wavy hair, gold forehead ornament with a red gem, golden eyes, gold necklaces, gold armlets, white egyptian bandeau top, sheer white sash, lamia, dark red snake lower body, long snake tail with a slender tip, soft voluptuous feminine body, huge breasts",
            "name": "the red-skinned lamia with a gold forehead ornament",
            "pose": "rising on her coiled snake body holding a jar of scented oil, gentle inviting smile, looking at viewer, standing beside a second adult lamia woman with brown skin and dark red hair and a third adult lamia woman with red skin and short auburn hair, three adult sisters together",
            "height_note": "she is much taller than him",
            "neg_remove": ["twins", "same face", "multiple girls"],
            "neg": LAMIA_NEG},
 },
 "places": {
   "entrance": "pyramid entrance hall in a sandstorm, a heavy stone door closed behind, sand blowing in, darkness",
   "corridor": "lower corridor of the tomb, flickering torches on the walls, faded wall paintings without text, dry dusty air",
   "bandage":  "chamber lined with stone sarcophagi, shelves stacked with rolls of white bandages, myrrh incense",
   "trap":     "trap passage, tilting floor tiles, streams of fine sand pouring from the walls, soft sand pits",
   "nest":     "wide chamber filled with warm sand, gaps between stone blocks, dim torchlight",
   "well":     "bottom of a deep round stone shaft, cool smooth stones, a tiny circle of light far above",
   "oil":      "chamber of scented oils, rows of oil jars without text, white frankincense smoke, a warm flat stone slab",
   "bath":     "stone bath filled with hot water, rising steam, scented oil floating on the water, stone pillars",
   "treasure": "treasure chamber, heaps of gold, jewels, a golden mask, dazzling torchlight reflections",
   "mural":    "corridor of wall paintings of an ancient king and his guardians without text, torch shadows moving on the walls",
   "vent":     "narrow star-viewing shaft in the pyramid wall, night sky and stars visible through the opening, cold night air, a stone seat",
   "riddle":   "silent riddle chamber, stone floor with carved patterns without text, lion statues, echoing emptiness",
   "summit":   "summit of the pyramid at night, full moon, the whole desert below, a wide stone seat covered with fur rugs, night wind",
   "crypt":    "burial chamber, a royal stone sarcophagus, gold decorations, a bed glossy with scented oil, guardians painted on the walls without text",
   "dune":     "desert sand dunes at night outside the pyramid, cold sand, bright moon, a distant oasis",
 },
 "atk": {
   "m1": ("riddle", "he kneels on the stone floor, the sphinx looms over him with one large soft lion forepaw resting on his shoulder, her fingertip pressing a glowing red mark onto his forehead, his lips parted as he answers, her white wings spread, " + GOLD + ", dazed, trembling"),
   "m2": ("riddle", "he lies on his back on the stone floor, the sphinx crouches over him on her lion body, one hand pinching and rolling his nipple, " + FING + ", a white wing feather brushing his inner thigh, amused smile, " + GOLD),
   "m3": ("summit", "from side, he lies cradled between her lion forelegs in the warm tawny fur, the sphinx bends down and kisses him deeply, tongues, saliva trail, her oiled fingers in his anus, fingering, the tuft of her lion tail stroking his inner thigh, full moon, " + GOLD),
   "e1": ("well", "from side, his legs and hips wrapped in the coils of her black and yellow-green cobra body, the cobra lamia holds him from behind, her large grey gauntlet hands pressing and rolling his nipples, " + TAIL + ", his back arched, " + GOLD),
   "e2": ("nest", "he kneels on the warm sand, the scorpion woman behind him gently holding his wrists up in her large black pincers without squeezing, " + STING + " on his nipple, her fingers pinching his other nipple, smirk, " + GOLD),
   "e3": ("bandage", "he lies on a stone slab " + WRAP + ", the mummy woman leans over him stroking his nipple with her bandaged hand, " + FING + ", calm serious face, a gold anklet over the bandages"),
   "boss": ("oil", "he lies on his back on the warm stone slab glistening with scented oil, the red-skinned lamia leans over him kissing him deeply, tongues, one hand rolling his nipple, " + FING + ", her snake tail wound around his wrists and ankles, incense smoke, " + GOLD),
 },
 "atk_desc": {
   "m1": "the sphinx presses a warm red mark on his forehead that makes him answer whatever she asks.",
   "m2": "the sphinx punishes each wrong answer one step further, from his nipples to her oiled fingers inside.",
   "m3": "the sphinx sinks him into her warm lion fur and seals his lips with a deep kiss while pressing inside.",
   "e1": "the cobra lamia wraps his lower body in her coils and strokes him inside with the tip of her tail.",
   "e2": "the scorpion woman raises his sensitivity with a harmless drop from her tail and pinches his nipples.",
   "e3": "the mummy woman wraps his whole body in soft bandages and teases his nipples and rear.",
   "boss": "the lamia sister teases his lips, nipples and rear all at once on the oil slab.",
 },
 "lose": {
   # スフィンクス 技1（紅の印）
   "btl_m1":     ("riddle", "he kneels on the stone floor with his chest pushed out, the sphinx sits over him with one lion forepaw on his shoulder, a red mark glowing on his forehead, her fingers pinching his nipple, " + FING + ", cum dripping untouched, " + GOLD),
   "onani_m1":   ("vent", "sitting alone on the stone seat beside the star-viewing shaft, pressing two fingers to his own forehead, the other hand stroking his own nipple, hips shifting, penis untouched, a gold bangle on his wrist, starlight, the sphinx watches far away through the opening"),
   "inochi_m1":  ("summit", "he sits on the fur rug looking up, a red mark glowing on his forehead, his lips parted as he answers, the sphinx reclines above him cupping his chin, her other hand rolling his nipple, a white wing curved around his back, full moon, " + GOLD + ", cum dripping"),
   "onedari_m1": ("summit", "he lies on the fur rug with his head on her lion forelegs, the sphinx strokes the glowing red mark on his forehead with her thumb, two oiled fingers of her other hand pressing deep in his anus, fingering, pleased smile, " + GOLD + ", cum on his stomach"),
   # スフィンクス 技2（★謎かけの罰）
   "btl_m2":     ("riddle", "he lies on his back on the stone floor, the sphinx leans over him pressing two oiled fingers deep in his anus, fingering, the two slender jade green snakes from her shoulders licking his ear and his nipple, her white wing covering his legs, a plain gold bangle without text on his wrist, cum on his stomach"),
   "onani_m2":   ("mural", "kneeling alone before the painted wall, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, looking up at the wall paintings without text, penis untouched, a gold anklet, the sphinx watches far away down the corridor"),
   "inochi_m2":  ("riddle", "he stands with his hands on a closed stone door, the sphinx rises behind him, one hand reaching around to pinch his nipple, " + FING + ", her white wings folded around him, " + GOLD + ", legs trembling, cum dripping"),
   "onedari_m2": ("crypt", "he sits leaning back on the lid of the stone sarcophagus, the sphinx stands before him on her four lion legs, both white wings wrapped around his body like a cloak, her fingers rolling his nipple, her other hand between his legs with fingers in his anus, fingering, " + GOLD + ", cum dripping"),
   # スフィンクス 技3（キス・オブ・デス）
   "btl_m3":     ("summit", "from side, he lies cradled between her lion forelegs sunk in the warm fur, the sphinx kisses him deeply, tongues, saliva trail, her oiled fingers in his anus, fingering, her lion tail tuft stroking his inner thigh, a necklace with a tuft of tawny fur on his chest, full moon, cum on his stomach"),
   "onani_m3":   ("dune", "lying alone on the cold sand hugging his rolled-up brown cloak, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, gold bangles glinting in the moonlight, the sphinx watches far away on the dune crest"),
   "inochi_m3":  ("summit", "from side, at dawn, he lies cradled between her lion forelegs under her white wing like a blanket, the sphinx kisses him deeply, tongues, her oiled fingers in his anus, fingering, pale sunrise over the desert behind them, " + GOLD + ", cum on his stomach"),
   "onedari_m3": ("summit", "he sits in the curl of her reclining lion body facing her, arms limp, the sphinx holds the back of his head and kisses him long and deep, tongues, saliva, two oiled fingers of her other hand deep in his anus, fingering, her lion tail around his waist, " + GOLD + ", cum dripping"),
   # コブラ娘（★コブラアナリシア）
   "btl_e1":     ("well", "from side, at the bottom of the well, his whole lower body wrapped tight in her cobra coils, the cobra lamia behind him rolling his nipples with her grey gauntlet fingers, " + TAIL + ", a bracelet of black and yellow-green scales on his wrist, cum dripping untouched"),
   "onani_e1":   ("corridor", "kneeling alone in a dark corner of the torchlit corridor, a sand-colored cloth wound tightly around his hips and thighs, one hand reaching behind with an oiled finger in his own anus, penis untouched, a thin gold chain on his waist, the cobra lamia watches far away in the shadows"),
   "inochi_e1":  ("well", "he clings halfway up the well wall going limp, the cobra lamia rises behind him on her long coiled body, her lips sucking softly on the side of his neck without biting, her snake tail wound around his ankle and thigh, her gauntlet hand on his chest, " + GOLD + ", his grip slipping"),
   "onedari_e1": ("well", "he lies in the center of her coiled cobra body with his waist wrapped, the cobra lamia leans over him kissing his neck, three faint pink kiss marks on his neck, " + TAIL + ", held still deep inside, " + GOLD + ", cum on his stomach"),
   # サソリ娘（★淫毒の針）
   "btl_e2":     ("nest", "he lies on his back on the warm sand, the scorpion woman kneels over him holding his wrists above his head in her black pincers without squeezing, pinching his glistening pink nipple with her fingers, the rounded tip of her tail resting on his inner thigh without piercing, a black carapace charm on his chest, cum on his stomach"),
   "onani_e2":   ("trap", "sitting alone in a corner of the sandy passage, poking his own nipple with one fingertip and his inner thigh with another, penis untouched, gold clip earrings, the scorpion woman watches far away half hidden in the sand"),
   "inochi_e2":  ("trap", "he sits at the bottom of a shallow soft sand pit, sand sliding down around him, the scorpion woman behind him holding his wrists in her pincers without squeezing, " + STING + " on his nipple, grinning at his ear, " + GOLD + ", cum dripping"),
   "onedari_e2": ("nest", "he kneels on the sand offering his chest, his wrists held gently behind his back in her black pincers, the scorpion woman in front of him, " + STING + " on his nipple, her fingers pinching his other nipple, pleased smirk, " + GOLD + ", cum dripping"),
   # ミイラ娘（★ミイラバンデージ）
   "btl_e3":     ("bandage", "he lies on a stone slab " + WRAP + ", the mummy woman kneels beside him stroking his nipple with her bandaged hand, two oiled fingers deep in his anus, fingering, a gold clasp on the bandage end at his chest, cum on the bandages"),
   "onani_e3":   ("bandage", "sitting alone behind a sarcophagus, white bandages wound loosely around his own wrists and chest, one oiled finger in his own anus, penis untouched, a gold anklet, the mummy woman watches far away from an open sarcophagus"),
   "inochi_e3":  ("corridor", "before a bright doorway of daylight at the end of the corridor, he is " + WRAP + ", held against her chest with his back to the light, the mummy woman rubbing his uncovered nipple, her oiled fingers in his anus, fingering, calm face, cum dripping"),
   "onedari_e3": ("bandage", "he lies on a pile of soft bandage rolls " + WRAP + ", the mummy woman lies beside him holding him close, her bandaged fingers rolling his nipple, two oiled fingers of her other hand deep in his anus, fingering, an incense burner smoking, faint smile, cum on the bandages"),
   # ネフェルラミアス（★姉妹の集団責め）※絵は長姉1人
   "btl_boss":   ("oil", "he lies on his back on the warm stone slab glistening with scented oil, the red-skinned lamia leans over him kissing him deeply, tongues, one hand rolling his nipple, " + FING + ", her snake tail wound around his wrists and ankles, three gold anklets on his ankle, cum on his stomach"),
   "onani_boss": ("bath", "kneeling alone at the edge of the steaming stone bath, his chest glistening with scented oil, one hand rolling his own nipple, an oiled finger of the other hand in his own anus, penis untouched, a gold necklace, the red-skinned lamia watches far away through the steam"),
   "inochi_boss":("oil", "he lies face up on the warm stone slab, his whole body glossy with oil, the red-skinned lamia pours oil from a jar onto his chest and spreads it over his nipple, " + FING + ", her snake tail around his ankle, " + GOLD + ", cum dripping"),
   "onedari_boss":("bath", "from side, waist-deep in the steaming bath, he leans back in the coils of her snake body, the red-skinned lamia kisses him deeply, tongues, one hand rolling his nipple, her other hand under the water between his legs fingering his anus, steam, " + GOLD + ", cum in the water"),
 },
 "lose_desc": "keeps him in the royal tomb forever as a cherished burial treasure adorned with twelve gold ornaments.",
 "onanie": {
   "master": ("mural", "kneeling before the painted wall, one hand pinching his own nipple, an oiled finger of the other hand in his own anus, penis untouched"),
   "e1": ("corridor", "kneeling in a dark corner, a cloth wound tightly around his hips and thighs, an oiled finger in his own anus, penis untouched"),
   "e2": ("trap", "sitting on the sand, poking his own nipple and inner thigh with his fingertips, penis untouched"),
   "e3": ("bandage", "sitting behind a sarcophagus, white bandages wound around his own wrists and chest, a finger in his own anus, penis untouched"),
   "boss": ("bath", "kneeling by the steaming bath, chest glistening with oil, one hand rolling his own nipple, a finger of the other hand in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "treasure", "two plain gold bangles without text resting on a stone pedestal, soft warm glow, close-up"),
   "2": ("m", "summit", "raising her chin and letting out a low roar toward the full moon, white wings spread wide, faint sound ripples in the air"),
   "3": (None, "trap", "a stone passage whose floor tiles have tilted open, fine sand streaming down like a waterfall into a soft sand pit, no spikes, torchlight"),
   "4": (None, "oil", "a gold incense burner releasing thick white frankincense smoke, jars of scented oil without text around it, warm lamp light, close-up"),
   "5": (None, "mural", "a wall painting of an ancient king whose eyes glow softly in pale gold, faint sand-colored sigils floating in the air, torchlight, without text"),
 },
}
