# N133 偽りのエリュシオン（REso）画像データ。登場人物は全員20歳以上。女性のみ（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。髪色：銀と黒／黒ボブ／金／灰茶／桃で被りなし。
# 挿入扱いはラダマンテュスの魔吸触手だけ（体の一部ではない触手なので pen なし）。サキは指まで。メイド・ラップガール・エリザは後ろに触れない。
# 触手は滑らかで淡く光る柔らかいもの（怖くしない・締めつけない）。ラップは顔に巻かない（息ができる）。名簿・札・カードは文字なし。
# 絵には必ず「左の手のひらの銀の画」「名簿」「鐘」のどれかを入れる。責め手が複数になる絵は無い（本体1人＋主人公）。
PALM = "a faint silver glowing mark on his left palm"
TENT = "smooth soft pale violet glowing tentacles"
HOLD = TENT + " loosely wrapped around his wrists and ankles lifting him into the air"
SUCK = "soft suction-tipped tentacles on his nipples"
IN = "a smooth round-tipped tentacle in his anus, anal"
WRAP = "clear plastic wrap wound tightly around his torso arms and legs, his face uncovered"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
TENT_NEG = SOFT_NEG + ", scary tentacles, teeth, eyes on tentacles, tight strangling, slimy monster, gore"
WRAP_NEG = SOFT_NEG + ", plastic wrap over the face, covered mouth, covered nose, suffocation, blade, knife"
DATA = {
 "code": "REso",
 "world": "a false paradise at the edge of the underworld, too-perfect flower fields under a grey sky, cold black stone halls, silent stone town with a pink neon shop, detailed background",
 "bg": "a too-perfect artificial-looking flower field in full bloom, beyond it a grey sky and a cold black stone judgment hall with a stone gate, a still river, a bell tower far away, eerie calm, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ラダマンテュス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, two-tone hair, silver hair, black streaked hair, very long straight hair, silver-grey eyes, androgynous calm face, black judge robe with silver trim, silver scales necklace, " + TENT + " rising behind her, soft curvy feminine body, huge breasts, wide hips",
         "name": "the silver-and-black-haired judge in a black robe",
         "pose": "holding a closed black leather register without text in one arm and a silver pen in the other hand, calm analytical faint smile, looking down at viewer",
         "neg": TENT_NEG},
   "e1": {"type": "woman", "jp": "サキュバスメイド",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, black hair, bob cut, red eyes, serious cool expression, black maid dress, white apron, maid headdress, white gloves, thin black succubus tail, soft curvy feminine body, large breasts",
          "name": "the black-bob maid with a thin tail",
          "pose": "standing straight holding a mop upright at her side, the other gloved hand on her apron, serious deadpan face, looking at viewer",
          "neg": SOFT_NEG + ", kicking, stepping on him"},
   "e2": {"type": "woman", "jp": "ラップガール",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, dark-skinned female, tan skin, blonde hair, long wavy hair, amber eyes, gyaru makeup, long glossy nails, layers of glossy clear plastic wrap wound like a tight tube dress over a black bikini, soft curvy feminine body, large breasts, wide hips",
          "name": "the tan blonde gyaru in a plastic-wrap dress",
          "pose": "holding a giant roll of clear plastic wrap on her shoulder, the other hand raised ready to snap her fingers, playful grin, looking at viewer",
          "neg": WRAP_NEG},
   "e3": {"type": "woman", "jp": "エリザ・リドル",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, pale skin, ash brown hair, long wavy hair, violet eyes, frail gentle look, white one-piece dress with cleavage, purple bracelet, faint purple glowing patterns on her skin, soft voluptuous feminine body, huge breasts",
          "name": "the ash-brown-haired lady in a white dress",
          "pose": "both hands clasped at her chest, a glowing purple bracelet on her wrist, shy blushing smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "サキ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, pink hair, very long hair, pink eyes, glowing eyes, black curved horns, succubus tail, flashy red and gold dress with a deep slit, gold jewelry, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the pink-haired succubus shop owner in a flashy dress",
            "pose": "one finger raised as if giving an order, the other hand on her hip, sweet lazy smile, looking at viewer with glowing pink eyes",
            "neg": SOFT_NEG},
 },
 "places": {
   "church":  "behind a church at night, moonlight, cold stone wall, a narrow stone bench, dewy grass",
   "flowers": "too-perfect flower field, countless flawless flowers, petals swaying without wind, soft soil, grey sky above",
   "gazebo":  "white gazebo, white pillars, lace curtains, a white long bench, tea cups with steam, flowers around",
   "town":    "silent stone-paved street, lit windows without people, echoing alley",
   "shop":    "succubus parlor lobby, pink neon light, reception counter, waiting sofa, sweet perfume haze",
   "room":    "private parlor room, round bed, wall mirror, a brass call bell on a side table, pink indirect lighting",
   "mshop":   "black-walled club room, pillars wound with plastic wrap, strong spotlights, a shelf of cardboard wrap cores",
   "wraproom":"room whose floor and walls are covered with clear plastic wrap, glossy reflections of the lights",
   "gate":    "entrance of the underworld, grey sky, cold stone gate, a still river, a stone seat at the ferry landing",
   "hall":    "mansion corridor, polished floor, long row of identical doors, a bucket of water, silence",
   "parlor":  "mansion guest parlor, upholstered chair, tea set, a tall grandfather clock, blank memo sheets without text",
   "court":   "judgment hall, high ceiling, black throne, a lectern with an open blank register without text, a silver pen",
   "clocks":  "corridor of stopped time, clocks with motionless hands, dust motes frozen in mid-air, frozen lamp flames",
   "garden":  "garden of " + TENT + " growing from the ground, warm faint light, dark stone path",
   "bedroom": "judge's bedchamber, a bed woven of soft tentacles, underworld lamps, a desk with a closed black register and an ink bottle",
 },
 "atk": {
   "m1": ("court", "he kneels before the black throne looking up, the judge sits above him with an open blank register without text on her knee, pointing a silver pen at him, calmly explaining, her silver scales necklace tilting, " + PALM + ", his knees trembling"),
   "m2": ("garden", "from side, " + HOLD + ", his shirt open, " + SUCK + ", " + IN + ", the judge stands close below him watching and holding a silver pen, faint smile, " + PALM + ", his own penis separate"),
   "m3": ("clocks", "he stands frozen, the judge holds his face in both hands and kisses him deeply, tongues, saliva, dust motes frozen in the air around them, a thin tentacle pressing at his anus from behind, " + PALM),
   "e1": ("parlor", "he sits in the upholstered chair with his shirt open, the maid kneels beside him, one white-gloved hand pinching his nipple, the other gloved hand holding the base of his penis still, handjob stopped, deadpan face, " + PALM + ", he trembles on the edge"),
   "e2": ("wraproom", "he stands unable to move, " + WRAP + ", a torn hole in the wrap over his nipples, the gyaru traces his nipple with a long glossy nail, her other hand raised snapping her fingers, grin, " + PALM),
   "e3": ("gazebo", "he sits on the white bench, the lady in the white dress clings to him from the front, her huge breasts pressed against his chest, her leg hooked over his, kissing his neck, her fingers on his nipple, her purple bracelet glowing, " + PALM),
   "boss": ("room", "he lies motionless on his back on the round bed, the succubus shop owner leans over him licking his nipple, gazing up with glowing pink eyes, two lotion-wet fingers of her other hand in his anus, fingering, a brass bell beside them, " + PALM),
 },
 "atk_desc": {
   "m1": "the judge calmly reasons him into staying, one argument at a time.",
   "m2": "the judge lifts him with her soft tentacles, sucking his nipples and stroking deep inside.",
   "m3": "the judge kisses him inside stopped time while a tentacle presses behind.",
   "e1": "the maid serves him with careful gloved hands and stops just before he comes.",
   "e2": "the gyaru wraps him in plastic wrap and traces his nipples while time is stopped.",
   "e3": "the lady clings to him with glowing patterns, kissing his neck and never letting go.",
   "boss": "the shop owner freezes him with an order and gives him her usual course.",
 },
 "lose": {
   # ラダマンテュス 技1（審判）
   "btl_m1":     ("court", "from side, before the black throne, " + HOLD + ", " + SUCK + ", " + IN + ", the judge stands beside him writing in an open blank register without text with a silver pen, a tiny silver scales charm on his collar, cum dripping untouched, his own penis separate"),
   "onani_m1":   ("gate", "sitting alone in the shadow of the stone gate, one hand rubbing his own nipple, a finger of the other hand in his own anus, lips moving as if reasoning, penis untouched, " + PALM + ", the judge watches far away by the river"),
   "inochi_m1":  ("flowers", "from side, among the flawless flowers, " + HOLD + ", " + SUCK + ", " + IN + ", the judge stands close with one finger raised as if asking for a counterargument, her scales necklace tilted, " + PALM + ", cum dripping untouched"),
   "onedari_m1": ("bedroom", "he kneels on the tentacle bed beside the register desk, the judge sits behind him holding his chin, writing in a blank register without text, " + SUCK + ", " + IN + ", his mouth open speaking, " + PALM + ", cum dripping"),
   # ラダマンテュス 技2（★魔吸触手拘束）
   "btl_m2":     ("garden", "from side, " + HOLD + " with his legs spread, " + SUCK + ", " + IN + ", the judge stands below him smiling loosely with one fist raised cheering, a soft tentacle ring like a bracelet on his wrist, " + PALM + ", cum dripping untouched, his own penis separate"),
   "onani_m2":   ("hall", "sitting alone behind a corridor pillar, a cord loosely looped around his own wrists and ankles, one hand stroking his nipple, the other hand reaching behind to his anus, penis untouched, " + PALM + ", the judge watches far down the corridor"),
   "inochi_m2":  ("garden", "at the garden exit, he floats just above the stone path, " + TENT + " around his ankles and wrists, " + SUCK + ", " + IN + ", the judge stands at the exit arch with her arms folded, " + PALM + ", cum dripping untouched"),
   "onedari_m2": ("bedroom", "from side, above the tentacle bed, six of the " + TENT + " hold him in the air, " + SUCK + ", " + IN + ", the judge sits on the bed edge counting on her fingers, a closed black register on the desk, cum dripping untouched"),
   # ラダマンテュス 技3（時刻超越の口づけ）
   "btl_m3":     ("clocks", "under the motionless clocks, " + TENT + " hold his wrists and waist, the judge holds his face and kisses him deeply, tongues, saliva trail, " + IN + ", dust motes frozen in mid-air, a clock hand tied on a cord around his neck, cum dripping untouched"),
   "onani_m3":   ("parlor", "kneeling alone behind the grandfather clock, holding his breath with one hand over his own mouth, a finger of the other hand pressing into his own anus, penis untouched, " + PALM + ", the judge watches far away from the doorway"),
   "inochi_m3":  ("clocks", "he sits on the corridor floor under a clock with motionless hands, the judge kneels over him kissing him deeply, tongues, " + SUCK + ", " + IN + ", frozen lamp flames, " + PALM + ", cum dripping untouched"),
   "onedari_m3": ("bedroom", "he lies on his back on the tentacle bed, the judge lies over him kissing him deeply, tongues, saliva, " + IN + ", a soft tentacle around his wrist, frozen lamp flames, a closed black register on the desk, cum on his stomach"),
   # サキュバスメイド（★メイドの嗜み）
   "btl_e1":     ("parlor", "he sits in the upholstered chair with his shirt open, the maid stands bending over him, one white-gloved hand rolling his nipple, the other gloved hand stroking his penis, handjob, a maid headdress ribbon pinned on his collar, " + PALM + ", cum on her glove"),
   "onani_e1":   ("hall", "crouching alone at the corridor corner, carefully stroking his own nipple under his shirt then lifting his fingers away, penis untouched, " + PALM + ", the maid watches far down the corridor holding a mop"),
   "inochi_e1":  ("hall", "he lies on his back on the polished corridor floor, the maid stands over him resting the mop handle lightly on his chest, her gloved hand lowered to roll his nipple, deadpan face, a bucket beside them, " + PALM + ", cum dripping untouched"),
   "onedari_e1": ("parlor", "he sits at the tea table with his shirt open, the maid stands behind him reaching around, both white-gloved hands rolling his nipples, counting calmly, tea cups with steam, blank memo sheets without text, " + PALM + ", cum dripping untouched"),
   # ラップガール（★ラップ拘束）
   "btl_e2":     ("wraproom", "he lies on the wrap-covered floor, " + WRAP + ", torn holes over his nipples and his penis, the gyaru crouches over him tracing his nipple with a long glossy nail, her other hand snapping her fingers, a cardboard wrap core without text beside him, " + PALM + ", cum on the wrap"),
   "onani_e2":   ("mshop", "sitting alone behind a black pillar, a strip of clear plastic wrap wound around his own chest, tracing his nipple through a torn hole with a fingertip, penis untouched, " + PALM + ", the gyaru watches far away under the spotlights"),
   "inochi_e2":  ("wraproom", "he lies on the floor in many layers, " + WRAP + ", the gyaru sits on a stool above him stroking his chest and lower belly with her bare tan foot, footjob, holding a roll of wrap, laughing, " + PALM + ", cum on the wrap"),
   "onedari_e2": ("wraproom", "in the middle of the room he stands upright, " + WRAP + ", a torn hole over his nipples, the gyaru presses close tracing both his nipples with her nails, three fingers raised, dust and light frozen in the air, " + PALM + ", cum dripping untouched"),
   # エリザ（★もう我慢できません）
   "btl_e3":     ("gazebo", "he lies on the white long bench, the lady in the white dress lies on top of him clinging, her huge breasts pressed to his chest, her thighs clamped around his penis, kissing his neck, kiss marks on his neck, matching purple bracelets on both their wrists, " + PALM + ", cum on her thighs"),
   "onani_e3":   ("church", "sitting alone on the narrow stone bench, hugging a white shirt to his chest, tracing his own neck with a fingertip, penis untouched, " + PALM + ", the lady in the white dress watches far away by the church wall in the moonlight"),
   "inochi_e3":  ("flowers", "he sits among the flawless flowers, the lady in the white dress hugs him tightly from the side with her arms and legs around him, kissing his neck, her fingers on his nipple, her purple bracelet glowing, " + PALM + ", cum dripping untouched"),
   "onedari_e3": ("gazebo", "he sits on the white bench, the lady in the white dress straddles his lap hugging his head to her huge breasts, her dress slipped off one shoulder, kissing his neck, many kiss marks, lace curtains, " + PALM + ", cum dripping"),
   # サキ（★命令ひとつめ）
   "btl_boss":   ("room", "he lies motionless on his back on the round bed, the succubus shop owner between his legs licking his nipple, glowing pink eyes, two lotion-wet fingers in his anus, fingering, a brass bell ringing on the side table, a blank pink card without text on his chest, " + PALM + ", cum on his stomach"),
   "onani_boss": ("shop", "sitting alone stiff and still at the end of the waiting sofa, only his fingertips rolling his own nipple, lips whispering, penis untouched, " + PALM + ", the succubus shop owner watches far away from the reception counter"),
   "inochi_boss":("room", "he kneels motionless on the round bed, the succubus shop owner behind him, her huge breasts against his back, licking his nipple from the side, two lotion-wet fingers in his anus, fingering, ringing the brass bell with her tail, " + PALM + ", cum dripping untouched"),
   "onedari_boss":("room", "he sits motionless against the headboard, the succubus shop owner presses his penis between her huge breasts, paizuri, gazing up with glowing pink eyes, her fingers in his anus, fingering, a blank gold tag without text on the pillow, " + PALM + ", cum on her breasts"),
 },
 "lose_desc": "keeps him in the false paradise forever as a permanent resident, his name fully written in the underworld register.",
 "onanie": {
   "master": ("hall", "sitting behind a pillar with a cord loosely looped around his own wrists and ankles, one hand stroking his nipple, the other hand reaching behind to his anus, penis untouched, " + PALM),
   "e1": ("hall", "crouching at the corridor corner, carefully stroking his own nipple then lifting his fingers away, penis untouched, " + PALM),
   "e2": ("mshop", "a strip of clear plastic wrap wound around his own chest, tracing his nipple through a torn hole, penis untouched, " + PALM),
   "e3": ("church", "sitting on the stone bench hugging a white shirt to his chest, tracing his own neck with a fingertip, penis untouched, " + PALM),
   "boss": ("shop", "sitting stiff and still on the waiting sofa, only his fingertips rolling his own nipple, penis untouched, " + PALM),
 },
 "magic": {
   "1": (None, "court", "a closed black leather register without text on a lectern, a silver pen resting on it, two faint silver strokes of light floating above, close-up"),
   "2": (None, "gate", "a large old bronze bell hanging in a stone arch under a grey sky, faint sound ripples in the air"),
   "3": (None, "town", "a pink neon tube sign shaped like a heart without text glowing above a shop door, pink light on the wet stone pavement"),
   "4": (None, "mshop", "a giant roll of clear plastic wrap standing on the floor, a loose shining sheet pulled out, spotlight reflections, roll without text"),
   "5": ("m", "garden", "raising one hand, soft glowing tentacles rising from the ground around her feet, calm faint smile"),
 },
}
