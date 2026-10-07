# N127 カルゴス団の女幹部（Kargos1）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない。
# キュゲラ：原作は青緑の髪 → jade green hair に置き換え（触手も jade green）。海辺の洞窟の「青い光」は pale green glow と書く。
# リリーポムの髪色は資料に無いので pink に決めた（5人で髪色を分ける：紫／黒／ピンク／金／翡翠）。
# 挿入はキュゲラの触手の先だけ（触手なので pen なし）。ギルギアは指だけ。ヘビヒメ・リリーポム・ハニークインは後ろに触れない。
# ムチは叩かない（房で撫でるだけ）。毒は痛みなし。ヘビヒメの牙の術は歯を立てない。蛇のマスクは外さない。
# 主人公の左腕に「町の守り手」の腕章（白い星と黒いカタツムリの紋。文字なし）。町の人・戦闘員・ほかの幹部は描かない。
ARM = "an armband with white stars and black snail crests without text on his left arm"
COLLAR = "a soft black leather collar on his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
WHIP_NEG = "whipping, whip marks, bruise, wound, pain"
TENT_NEG = "scary, grotesque, slime monster, wound, stinger"
DATA = {
 "code": "Kargos1",
 "world": "city secretly ruled by an evil organization of seductive women, night, neon lights, black banners with a snail crest without text, detailed background",
 "bg": "main street of a city at night, neon lights, building walls with black banners bearing a snail crest without text, cafe terrace seats, rocky wasteland mountain far away, night wind, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ギルギア",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, purple hair, very long straight hair, violet eyes, cold expression, dark purple sorceress robe with gold trim, wide sleeves, high collar, crystal ball in her hand, soft curvy feminine body, large breasts",
         "name": "the purple-haired sorceress in a dark robe",
         "pose": "holding a glowing crystal ball in one palm, the other hand at her chin, cold faint smile, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ヘビヒメ",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, long low ponytail, amber eyes, ornate snake mask covering the upper half of her face, black and purple kunoichi outfit, open neckline, cleavage, fishnet undershirt, obi sash with a snake crest, soft voluptuous feminine body, gigantic breasts, wide hips",
          "name": "the snake-masked kunoichi in black and purple",
          "pose": "one hand forming a ninja hand sign, the other arm under her heavy breasts, composed haughty smile, looking at viewer",
          "neg": SOFT_NEG + ", unmasked face, snake lower body"},
   "e2": {"type": "woman", "jp": "リリーポム",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, wavy bob hair, magenta eyes, pink clown makeup, pink heart mark on her cheek, red and white striped jester leotard, puffy ruff collar, two-pointed jester hat with round bells, round bells on her fingertips, white gloves, soft curvy feminine body, huge breasts, wide hips, large hips",
          "name": "the pink-haired clown in a red and white jester costume",
          "pose": "leaning forward with her hands on her knees, bouncing breasts, hat bells jingling, laughing with an open mouth, looking at viewer",
          "neg": SOFT_NEG + ", white face paint, creepy clown, red nose"},
   "e3": {"type": "woman", "jp": "ハニークイン",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, long curly hair, drill curls, golden eyes, pale white skin, black and gold bondage-style leotard, gold buckles, black long gloves, black thigh-high boots, soft tassel whip glistening with honey in her hand, soft curvy feminine body, huge breasts, thick thighs",
          "name": "the blonde queen in black and gold leather",
          "pose": "one hand on her hip, holding a honey-coated tassel whip loosely against her shoulder, confident queenly smile, looking down at viewer",
          "neg": SOFT_NEG + ", " + WHIP_NEG},
   "boss": {"type": "woman", "jp": "キュゲラ",
            "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, jade green hair, long wavy hair, yellow eyes, translucent jellyfish-bell headdress, glossy dark green and white bodysuit, frilled translucent collar, many long smooth jade green tentacles extending from her back, glistening, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the jade-haired tentacle woman with a jellyfish headdress",
            "pose": "both fists on her hips, chest puffed out, tentacles spread wide behind her, boastful big grin, looking at viewer",
            "neg": SOFT_NEG + ", " + TENT_NEG},
 },
 "places": {
   "street":   "main street at night, neon lights, posters without text, cafe terrace with a round table and chairs",
   "cavegate": "entrance of a damp cave, wet rocks, darkness inside, dripping water, moss",
   "summit":   "summit of a rocky wasteland, red rocks, a black banner with a snail crest without text flapping in the wind, dry earth",
   "plaza":    "town plaza at dusk, a stone fountain, wooden benches, street lamps, empty",
   "circus":   "inside a red and white striped circus tent, round stage with spotlights, sawdust floor, empty rows of seats, hanging bells",
   "backdoor": "hidden wooden door in a forest, moss, tree roots, faint incense smoke from the gap",
   "bath":     "large underground cypress bath, thick steam, wet wooden boards, paper lanterns",
   "hall":     "large japanese hall of an underground mansion, tatami mats, hanging scroll with a snake crest without text, incense smoke, paper lanterns, floor cushions",
   "beach":    "beach at night, white sand, rocks, gentle waves, wet sand, moonlight",
   "seacave":  "seaside cave, tide pools, slick rocks, pale green glow on the water, salt mist",
   "spring":   "clear spring under the moon, water surface shining like crystal, cold flat stones at the edge",
   "command":  "command room of a secret base, wall of monitors without text, map table, an empty throne, a black leather armchair, dim light",
   "crystal":  "stone chamber with a large floating crystal, purple light, magic circle on the floor, black cloth spread on the stone floor",
   "underpass":"narrow underground passage, neon sign glow without text, pipes on the walls, a heavy door at the end",
   "vip":      "VIP room of a secret club, red sofa, canopy bed with cage-like bars, a brass bell hanging, dim light, soft carpet",
 },
 "atk": {
   "m1": ("crystal", "he sits on the black cloth with his shirt open, the sorceress crouches behind him holding the glowing crystal ball before his face, her cold fingertip tracing his nipple, her lips near his ear, calm cold smile, " + ARM + ", trembling"),
   "m2": ("command", "he is on all fours on the floor before the empty throne, the sorceress bends over him whispering into his ear, one hand stroking his back, cold eyes, his elbows shaking, " + ARM),
   "m3": ("crystal", "they sit on the black cloth, the sorceress holds his chin and kisses him deeply, tongues, saliva trail, purple crystal light shining on his bare chest, two fingers of her other hand in his anus, fingering, " + ARM),
   "e1": ("hall", "he kneels on the tatami, the kunoichi kneels facing him pulling his face deep between her gigantic breasts, both arms squeezing them around his head, one hand stroking his nipple, incense smoke, his arms hanging limp, " + ARM),
   "e2": ("circus", "he sits on the stage floor staring up, the clown leans over him swaying her huge breasts side to side before his face, hat bells ringing, her belled fingertip flicking his nipple, laughing, his mouth open repeating words, " + ARM),
   "e3": ("summit", "he sits on a red rock with his shirt open, the blonde queen stands over him brushing the honey-coated tassel of her whip softly around his nipple, her other hand pinching the other nipple, honey glistening on his chest, whispering, " + ARM, {"neg": WHIP_NEG}),
   "boss": ("seacave", "from side, he floats in the air above the tide pool, jade green tentacles coiled around his wrists and ankles, thin tentacles sucking his nipples, a smooth round tentacle tip in his anus, anal, the tentacle woman grins beside him, his own penis separate, " + ARM, {"neg": TENT_NEG}),
 },
 "atk_desc": {
   "m1": "the sorceress reads his mind with her crystal and touches the place before he can hide the thought.",
   "m2": "the sorceress whispers that men cannot beat women until he drops to all fours by himself.",
   "m3": "the sorceress seals his lips with a long cold kiss while crystal light and her fingers undo him.",
   "e1": "the kunoichi traps his face between her breasts and swells his desire with her art.",
   "e2": "the clown hypnotizes him with swaying breasts, bells and repeated words.",
   "e3": "the queen strokes him with a honeyed whip tassel that never strikes and pinches his tingling nipples.",
   "boss": "the tentacle woman lifts him into the air and drains him with her tentacles.",
 },
 "lose": {
   # ギルギア 技1（★心読みの水晶）
   "btl_m1":     ("crystal", "he lies on his back on the black cloth the sorceress kneels beside him holding the crystal ball over his face, two wet fingers of her other hand deep in his anus, fingering, a crystal shard pendant on his neck, cum on his stomach untouched, " + ARM),
   "onani_m1":   ("command", "kneeling alone in the shadow of the empty throne, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched, armband glowing faintly black, the sorceress watches far away by the monitors"),
   "inochi_m1":  ("underpass", "he stands with both hands on the passage wall, the sorceress close behind him holding the crystal ball beside his face, one finger pressing in his anus, fingering, a heavy door ahead, his legs trembling, cum dripping, " + ARM),
   "onedari_m1": ("vip", "he lies on the canopy bed with his shirt open, the sorceress sits beside him, one cold hand rolling his nipple, two fingers of her other hand in his anus, fingering, crystal ball resting on the pillow, his mouth open speaking, cum dripping"),
   # ギルギア 技2（男は女に勝てない）
   "btl_m2":     ("command", "he is on all fours before the black leather armchair, the sorceress crouches beside him fastening " + COLLAR + ", whispering into his ear, her fingers in his anus, fingering, cum dripping on the floor, " + ARM),
   "onani_m2":   ("summit", "on all fours alone under the flapping black banner, lips moving in a murmur, one hand reaching back stroking his own anus, penis untouched, armband glowing faintly black, the sorceress watches far away behind the banner pole"),
   "inochi_m2":  ("plaza", "he bends forward with both hands on the rim of the fountain, the sorceress stands behind him whispering into his ear, holding the crystal ball at his cheek, her fingertip on his nipple, his knees buckling, cum dripping, " + ARM),
   "onedari_m2": ("vip", "he is on all fours on the soft carpet wearing " + COLLAR + ", the sorceress sits on the red sofa holding the thin chain of his collar loosely, leaning down to his ear, her other hand with fingers in his anus, fingering, cum dripping"),
   # ギルギア 技3（裏切りの口づけ）
   "btl_m3":     ("crystal", "he lies on his back on the black cloth, the sorceress leans over him kissing him deeply, tongues, saliva trail, crystal light on his nipples, her fingers in his anus, fingering, a gold clasp in his hand, cum on his stomach, " + ARM),
   "onani_m3":   ("spring", "kneeling alone at the edge of the moonlit spring, sucking two of his own fingers as if kissing, the other hand behind pressing a finger into his own anus, penis untouched, armband glowing faintly black, the sorceress watches far away across the water"),
   "inochi_m3":  ("command", "in a back room behind the monitors, he stands pressed against the closed door, the sorceress pins him kissing him coldly and deeply, tongues, one hand on his nipple, her fingers in his anus, fingering, his knees giving way, " + ARM),
   "onedari_m3": ("crystal", "he sits on the sorceress's lap on the black cloth facing her, a long deep kiss, saliva trail, purple crystal light on his nipple, her fingers deep in his anus, fingering, his arms around her neck, cum dripping, " + ARM),
   # ヘビヒメ（★蛇忍法 乳誘い）
   "btl_e1":     ("hall", "he kneels on the tatami, the kunoichi sits before him pressing his whole face between her gigantic breasts, one palm glowing on his lower belly, her other hand stroking his nipple, a snake-crest sash clip in his hand, cum dripping untouched, " + ARM),
   "onani_e1":   ("bath", "sitting alone in a corner of the changing area, pressing a rolled towel against both sides of his own face, one hand stroking his own nipple, penis untouched, armband glowing faintly black, the kunoichi watches far away through the steam"),
   "inochi_e1":  ("hall", "he stands at the opened sliding door, the kunoichi stands waiting and pulls his face into her gigantic breasts, her arms around his head, one palm glowing on his lower belly, lanterns, his arms falling limp, cum dripping, " + ARM),
   "onedari_e1": ("hall", "he sits on a floor cushion before her knees, the kunoichi leans over squeezing his face between her gigantic breasts and swaying them, her masked face lowered to his neck, lips softly sucking his neck without teeth, her finger on his nipple, cum dripping"),
   # リリーポム（★魅惑の催眠術）
   "btl_e2":     ("circus", "he kneels on the stage in the spotlight with vacant happy face, the clown crouches before him swaying her huge breasts, flicking both his nipples with belled fingertips, a two-pointed jester hat with bells placed on his head, cum dripping untouched, " + ARM),
   "onani_e2":   ("plaza", "crouching alone in the shadow behind a bench, lips moving repeating a word, flicking his own nipple with a fingertip, penis untouched, armband glowing faintly black, the clown watches far away from beside the fountain"),
   "inochi_e2":  ("circus", "he stands dazed in the center of the stage under the spotlight, the clown stands behind him ringing a hand bell by his ear, her huge breasts pressed against his back, his mouth open repeating words, empty seats around, cum dripping untouched, " + ARM),
   "onedari_e2": ("circus", "he sits in the front row seat looking up, the clown bends over the stage edge swaying her huge breasts before his eyes, counting on her fingers, her belled fingertip flicking his nipple, laughing, cum dripping untouched, " + ARM),
   # ハニークイン（★ハニートラップ）
   "btl_e3":     ("summit", "he lies on his back on the dry earth under the black banner, the blonde queen sits astride his hips clamping them with her thick thighs, pinching both his honey-coated nipples, a single whip tassel tied to his wrist, cum on his stomach, " + ARM, {"neg": WHIP_NEG}),
   "onani_e3":   ("cavegate", "sitting alone behind a wet rock, a jar of honey without text beside him, stroking his own nipple with honey-coated fingers, penis untouched, armband glowing faintly black, the blonde queen watches far away from the cave entrance"),
   "inochi_e3":  ("street", "he sits at the cafe terrace table beside the blonde queen, the queen leans close blowing a sweet pink breath onto his face, her thick thigh over his lap under the table, her honeyed fingertip on his nipple, his body slack, " + ARM, {"neg": WHIP_NEG}),
   "onedari_e3": ("summit", "he kneels on a seat of flat rock under the banner looking up, the blonde queen stands over him brushing the honeyed whip tassel softly over his nipple, her other hand lifting his chin, his mouth open calling her name, cum dripping untouched, " + ARM, {"neg": WHIP_NEG}),
   # キュゲラ（★触手ドレイン）
   "btl_boss":   ("seacave", "from side, he floats high in the air, jade green tentacles coiled around his wrists and ankles, thin tentacles sucking both nipples, a smooth round tentacle tip deep in his anus, anal, the tentacle woman laughs proudly, his own penis separate, cum dripping, " + ARM, {"neg": TENT_NEG}),
   "onani_boss": ("beach", "lying alone behind a rock on the sand, thin cords wound around his own wrists and ankles, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched, armband glowing faintly black, the tentacle woman watches far away at the waterline"),
   "inochi_boss":("seacave", "from side, he is lifted above the tide pool, jade green tentacles around his limbs, a thin tentacle sucking his nipple, a round tentacle tip in his anus, anal, the tentacle woman grins hiding a glowing pale green orb behind her back, his own penis separate, " + ARM, {"neg": TENT_NEG}),
   "onedari_boss":("seacave", "from side, he floats face up in the air held by five jade green tentacles, two thin tentacles sucking his nipples, a smooth round tentacle tip deep in his anus, anal, the tentacle woman leans over his face beaming with joy, his mouth open calling her, his own penis separate, cum on his stomach", {"neg": TENT_NEG}),
 },
 "lose_desc": "keeps him forever in the secret club under the city as the cherished pet of the organization, every star on his armband turned into a black snail crest.",
 "onanie": {
   "master": ("command", "kneeling in the shadow of the throne, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched, armband glowing faintly black"),
   "e1": ("hall", "sitting on the tatami, pressing a floor cushion against both sides of his own face, one hand stroking his own nipple, penis untouched, armband glowing faintly black"),
   "e2": ("circus", "crouching behind the seats, lips moving repeating a word, flicking his own nipple with a fingertip, penis untouched, armband glowing faintly black"),
   "e3": ("summit", "sitting behind a red rock, stroking his own nipple with honey-coated fingers, a honey jar without text beside him, penis untouched"),
   "boss": ("seacave", "lying on a flat rock, thin cords wound around his own wrists and ankles, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "crystal", "a cloth armband lying on black cloth, two of its white stars turning into black snail crests with a faint dark glow, close-up, without text"),
   "2": ("m", "command", "sitting in the black leather armchair with legs crossed, one hand raised toward a wall of glowing monitors without text, crystal ball on her lap, cold composed expression"),
   "3": (None, "summit", "a soft tassel whip glistening with golden honey coiled on a red rock, honey dripping slowly from the tassels, sweet haze, close-up"),
   "4": (None, "seacave", "a round glass vial of glossy pale green liquid on a wet rock, a single drop falling from a smooth jade green tentacle tip above it, soft glow, vial without text"),
   "5": (None, "vip", "a brass bell hanging from a red cord, faint sound ripples in the air, dim red light, canopy bed in the background, close-up"),
 },
}
