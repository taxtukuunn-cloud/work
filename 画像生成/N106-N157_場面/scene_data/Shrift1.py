# N129 香神市の悪魔（Shrift1）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# セイレーン：原作は青い長髪 → lavender hair／violet eyes に置き換え。陸の場面（舞台・楽屋）は二本の脚で描く（人魚の尾は描かない）。
# トオロドン：髪色は資料に無いため blonde の短髪に決めた（5人の髪色を被らせない：pink／pale green／lavender／blonde／black）。
# 挿入はローズのスライム（m3）とトオロドンの尻尾の先（e2）だけ＝どちらも pen なし。カハクは指まで。張形・ふたなりの絵は無い。
# 責めは痛みなし（鉤爪は傷つけない・踏みつけは重みだけ・スライムは溶かさない）。絵にはロザリオか薔薇の花びらを必ず一つ入れる。名札は無地。
ROS = "a rosary with dark clouded beads around his neck"
PETAL = "red rose petals scattered around"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs, blood, wound"
SLIME_NEG = SOFT_NEG + ", melting skin, dissolving clothes, green slime, monster face"
DATA = {
 "code": "Shrift1",
 "world": "rainy harbor city at night haunted by beautiful demons, neon lights reflected on wet streets, a white hospital on a hill, faint scent of roses, detailed background",
 "bg": "harbor city at night in the rain, a narrow wet alley in the foreground, neon signs without text glowing in the distance, puddles reflecting pink light, a white hospital building on a hill far away, red rose petals drifting, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ローズ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, slime woman, pink hair, very long hair, red rose hair ornament, gold crown, pink eyes, glowing eyes, long dress made of translucent pink slime, glossy pink slime flowing from the hem of her dress, bare shoulders, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the pink-haired demon queen in a slime dress",
         "pose": "sitting cross-legged on a throne-like chair, one finger raised to her chin, cruel elegant smile, looking down at viewer with glowing pink eyes, a red rose in a vase beside her",
         "neg": SLIME_NEG},
   "e1": {"type": "woman", "jp": "セイレーン",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, lavender hair, very long wavy hair, seashell hair ornament, violet eyes, fin-shaped ears, thin white stage dress with an open neckline, pearl necklace, soft curvy feminine body, huge breasts",
          "name": "the lavender-haired songstress in a white stage dress",
          "pose": "standing on a stage with one hand on her chest and the other reaching out, singing gently, kind big-sisterly smile, looking at viewer, musical notes of light floating",
          "neg": SOFT_NEG + ", mermaid tail, fish tail"},
   "e2": {"type": "woman", "jp": "トオロドン",
          "tags": "adult woman, mature female, mature face, sharp adult features, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, lizard woman, green scaly skin, glossy wet scales, short messy blonde hair, golden eyes, slit pupils, thick green lizard tail, smooth rounded claws, black leather jacket, black shorts, soft curvy feminine body, large breasts, wide hips",
          "name": "the green-scaled lizard woman in a black jacket",
          "pose": "leaning against an alley wall with her arms crossed, tail swaying, cocky delinquent grin, looking at viewer with golden eyes",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", sharp claws cutting skin, reptile head, snout"},
   "e3": {"type": "woman", "jp": "ケットシー",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, wide hips, cat woman, black hair, medium hair, black cat ears, long black cat tail, yellow eyes, cat paw hands with pink paw pads, black fur on her forearms and lower legs, bell collar, black crop top, black shorts, soft curvy feminine body, large breasts",
          "name": "the black-cat-eared woman with a bell collar",
          "pose": "crouching on a roof tile with one paw hand raised beside her cheek, tail curled up, smug playful grin, looking at viewer, full moon behind her",
          "neg": SOFT_NEG + ", flat chest"},
   "boss": {"type": "woman", "jp": "カハク",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, moth woman, pale green hair, very long straight hair, feathery moth antennae, large pale green moth wings with eye patterns, amber eyes, thin sheer pale gown, shimmering scale powder drifting around her, fluffy moth abdomen tail, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the pale-green-haired moth spirit with large wings",
            "pose": "standing with her large wings spread wide, both hands held out as if receiving an offering, quiet gentle smile, looking at viewer, pale pink powder falling",
            "neg": SOFT_NEG + ", insect face, insect legs, mandibles"},
 },
 "places": {
   "shrine":   "small shinto shrine at night, torii gate, a shrine bell with a thick rope, wet stone pavement",
   "disco":    "night disco floor, neon lights, mirror ball light specks, empty dance floor",
   "alley":    "rainy back alley, trash bins, puddles reflecting distant neon",
   "roof":     "old tiled rooftop at night, full moon, a pile of stolen jackets pillows and blankets",
   "hangout":  "deep end of the back alley, damp walls, an old sofa, a slowly turning ventilation fan",
   "stage":    "stage of an old theater, hot spotlight, dusty red curtain, rows of empty seats",
   "dressing": "theater dressing room, large mirror with light bulbs, costume rack, a long bench with a pillow",
   "grave":    "foggy public cemetery at night, old gravestones, damp earth, drifting scale powder",
   "grove":    "sacred tree garden, a huge ancient tree, white silk cocoons hanging, moss, glittering powder in the air",
   "lobby":    "hospital reception at night, white walls, empty waiting benches, a number ticket machine without text",
   "hall":     "hospital corridor at night, a long bench, rose petals on the floor, faintly glowing pink slime trails, a window",
   "office":   "hospital director's office, a big vase of red roses, a throne-like chair, a window with city lights",
   "garden":   "glass greenhouse on the hospital rooftop, roses in full bloom, warm humid air, rain running down the glass",
   "hotel":    "hotel room at night, a bed, a tall standing mirror, a window with the white hospital far away",
   "special":  "top-floor hospital suite, canopy bed, red roses, a cradle made of pink slime, a blank nameplate without text on the door",
 },
 "atk": {
   "m1": ("office", "he kneels on the carpet with his shirt opened, the demon queen stands over him lifting his chin with one finger, staring down into his face with glowing pink eyes, pink slime creeping up his legs, he holds out his rosary with both hands, " + ROS),
   "m2": ("garden", "he floats above the roses, his wrists ankles and waist wrapped in translucent pink slime, the demon queen cradles his face against her breasts, slime tendrils sucking his nipples under his open shirt, a slime finger in his anus, fingering, " + ROS),
   "m3": ("special", "from side, he lies sunk in a cradle of pink slime, the demon queen leans over him kissing him deeply, tongues, saliva trail, a soft slime tendril from her dress in his anus, slime wrapped around his body, his own penis separate, " + ROS + ", " + PETAL),
   "e1": ("stage", "under the spotlight, he kneels with his knees weak, the songstress holds his head and buries his face between her breasts, singing into his ear, her fingertip stroking his nipple through his open shirt, glowing musical notes, " + ROS),
   "e2": ("hangout", "from side, by the damp wall, the lizard woman hugs him tightly face to face with her glossy slimy arms, a drop of green liquid on his neck, her rounded claw tracing his nipple, the tip of her tail in his anus, white slime on his shirt, " + ROS),
   "e3": ("roof", "under the moon, he sits on the roof tiles, the cat-eared woman pounces and wraps his face in her breasts, sniffing his neck, her paw pad pressing his nipple, her black tail stroking his inner thigh, her bell ringing, " + ROS),
   "boss": ("grove", "under the ancient tree, he lies with his wrists and ankles wrapped in soft white silk, the moth spirit kneels over him with wings spread, her long thin tongue sucking his nipple, her honey-wet finger in his anus, fingering, pale pink powder falling, " + ROS),
 },
 "atk_desc": {
   "m1": "the demon queen makes him undress and kneel with her obedient gaze.",
   "m2": "the demon queen wraps him in warm pink slime and lifts him off the ground while cradling his face.",
   "m3": "the demon queen rocks him in a slime cradle with a deep kiss while her slime enters him.",
   "e1": "the songstress wraps his face in her breasts while singing a charm song into his ear.",
   "e2": "the lizard woman embraces him with her slimy body and strokes inside him with the tip of her tail.",
   "e3": "the cat woman wraps his face in her breasts, sniffs his neck and presses his nipple with her paw pad.",
   "boss": "the moth spirit showers him with powder, wraps him in silk and draws his energy from his nipple.",
 },
 "lose": {
   # ローズ 技1（私を見なさい＋スライム拘束）
   "btl_m1":     ("office", "he kneels before the throne-like chair with his shirt open, holding up his rosary in both hands, the demon queen holds his chin and stares into his face with glowing pink eyes, pink slime wrapping his legs and sucking his nipples, a red rose ornament in his hair, cum dripping untouched, the last rose petal falling"),
   "onani_m1":   ("hotel", "kneeling alone before the tall standing mirror, staring at his own reflection, one hand rubbing his own nipple, the other hand reaching behind to his anus, penis untouched, " + ROS + " glowing black, the demon queen's pink eyes watch from inside the mirror far away"),
   "inochi_m1":  ("office", "he sits on an examination stool with his shirt off, the demon queen leans close staring into his eyes with glowing pink eyes, a strand of pink slime pressed to his chest like a stethoscope sucking his nipple, her slime finger in his anus, fingering, " + ROS + ", cum dripping"),
   "onedari_m1": ("special", "he sits on the canopy bed looking up, the demon queen sits facing him holding his face in both hands, glowing pink eyes close to his, pink slime wrapping his whole body up to his chest, a slime finger in his anus, " + ROS + ", " + PETAL + ", cum dripping"),
   # ローズ 技2（★スライム拘束）
   "btl_m2":     ("garden", "he floats above the blooming roses wrapped in translucent pink slime at wrists ankles and waist, the demon queen presses his face into her breasts, slime sucking both his nipples, two slime fingers in his anus, fingering, a glass vial of pink slime in his hand, " + ROS + ", cum dripping untouched"),
   "onani_m2":   ("hall", "sitting alone on the corridor bench, his body glossy with lotion, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched, " + ROS + " glowing black, the demon queen rises from a pink slime trail far down the corridor watching"),
   "inochi_m2":  ("garden", "he kneels among the roses holding pruning scissors, pink slime climbing from his feet to his chest and sucking his nipples, the demon queen stands behind him with her hand on his shoulder, her slime finger in his anus, fingering, " + ROS + ", rose petals on his knees, cum dripping"),
   "onedari_m2": ("special", "he lies in a cradle of pink slime wrapped up to his neck, the demon queen sits on the edge smiling down, holding up three fingers, three slime fingers in his anus, fingering, slime sucking his nipples, " + ROS + ", " + PETAL + ", cum on his stomach"),
   # ローズ 技3（溶心の揺り籠＋スライム拘束）
   "btl_m3":     ("special", "from side, he lies sunk in the swaying cradle of pink slime, the demon queen over him kissing him deeply, tongues, saliva trail, a soft slime tendril in his anus, slime sucking his nipples, a blank nameplate without text on the bedside, his own penis separate, " + ROS + ", cum on his stomach"),
   "onani_m3":   ("hotel", "curled up alone on the bed wrapped in a blanket, rocking his body, sucking two of his own fingers, the other hand behind him with a finger in his own anus, penis untouched, " + ROS + " glowing black, the demon queen watches far away at the window"),
   "inochi_m3":  ("hall", "from side, at the end of the corridor, he lies in a cradle of pink slime, the demon queen bends over him giving a soft kiss, her hand rocking the cradle, a slime tendril in his anus, his arms limp, rose petals on the floor, " + ROS + ", his own penis separate, cum dripping"),
   "onedari_m3": ("special", "from side, by the window, he lies in the slime cradle with his arms around her neck, the demon queen kisses him deeply while rocking him slowly, a slime tendril deep in his anus, city lights outside, " + ROS + ", " + PETAL + ", his own penis separate, cum on his stomach"),
   # セイレーン（★歌姫抱胸）
   "btl_e1":     ("stage", "under the spotlight, he sits on the stage floor leaning into her, the songstress holds his face between her breasts, singing with her lips at his ear, one hand stroking his nipple, her other hand resting on his penis, a seashell ornament in his hair, " + ROS + ", cum dripping"),
   "onani_e1":   ("dressing", "lying alone on the long bench with his face buried in a pillow, humming, one hand under his shirt rubbing his own nipple, penis untouched, " + ROS + " glowing black, the songstress watches far away reflected in the mirror"),
   "inochi_e1":  ("stage", "he sits in the front row seat, the songstress leans over him from the stage edge, holding his head to her breasts, her lips sucking his nipple through his open shirt, glowing musical notes, the curtain still open, " + ROS + ", cum dripping"),
   "onedari_e1": ("stage", "he kneels on the stage with his shirt open, the songstress sits on a chair holding him against her chest, sucking his nipple, singing softly, her hand stroking his hair, glowing musical notes around them, " + ROS + ", " + PETAL + ", cum dripping untouched"),
   # トオロドン（★粘毒抱擁）
   "btl_e2":     ("hangout", "from side, against the damp wall, the lizard woman hugs him tightly face to face, glossy white slime between their bodies, a drop of green liquid on his neck, her rounded claw tracing his nipple, the tip of her tail in his anus, a green scale earring on his ear, " + ROS + ", cum dripping untouched"),
   "onani_e2":   ("alley", "crouching alone behind a trash bin in the rain, one lotion-wet hand stroking his own neck, a wet finger of the other hand in his own anus, penis untouched, " + ROS + " glowing black, the lizard woman watches far away at the alley mouth"),
   "inochi_e2":  ("hangout", "from side, on the old sofa, he sits on the lizard woman's lap facing her, hugged tight in her slimy arms, his shirt soaked with white slime, the tip of her tail in his anus, her golden eyes grinning, " + ROS + ", cum dripping"),
   "onedari_e2": ("hangout", "from side, on the old sofa, he lies on top of the lizard woman held hard in her arms, her fingertip dropping green liquid on his neck, her tail curled around and its tip deep in his anus, his arms clinging to her, " + ROS + ", " + PETAL + ", cum dripping"),
   # ケットシー（★豊胸猫吸）
   "btl_e3":     ("roof", "under the full moon, he lies on the pile of blankets, the cat-eared woman lies on him wrapping his face in her breasts, sniffing his armpit, one paw pad pressing his nipple, her other paw hand stroking his penis, her tail on his thigh, a bell collar on his neck, " + ROS + ", cum on his stomach"),
   "onani_e3":   ("alley", "sitting alone in the shadows with his face buried in his own pillow, breathing in, pressing his own nipple with a fingertip under his shirt, penis untouched, " + ROS + " glowing black, the cat-eared woman watches far away from a roof edge"),
   "inochi_e3":  ("alley", "in the alley, he stands holding a folded blanket, the cat-eared woman has dropped from the roof onto his back hugging him, her nose under his raised arm sniffing, her paw pad pressing his nipple through his open shirt, " + ROS + ", knees trembling, cum dripping"),
   "onedari_e3": ("roof", "on the rooftop bedding, he sits with his shirt open and his neck offered, the cat-eared woman sniffs his neck, counting with one raised paw finger, her other paw pad pressing his nipple, her bell ringing, tail swaying, " + ROS + ", " + PETAL + ", cum dripping untouched"),
   # カハク（★怪人蛾の吸精）
   "btl_boss":   ("grove", "under the ancient tree, he lies wrapped in soft white silk at wrists and ankles, the moth spirit over him with wings spread, her long thin tongue sucking his nipple, two honey-wet fingers in his anus, fingering, a glass ball of glittering powder beside his hand, " + ROS + ", cum dripping untouched"),
   "onani_boss": ("grave", "sitting alone against a gravestone in the fog, breathing in pale pink drifting powder, shirt open, rubbing his own flushed nipples with his fingertips, penis untouched, " + ROS + " glowing black, the moth spirit watches far away in the fog"),
   "inochi_boss":("grove", "he sits leaning his back against the ancient tree, limp, pale gold powder falling, the moth spirit kneels between his legs, her long tongue sucking his nipple, her finger in his anus, fingering, leaves rustling above, " + ROS + ", cum dripping"),
   "onedari_boss":("grove", "he lies in a bed of white silk cocoon, breathing deep pale pink powder, flushed, the moth spirit bends over him with wings folded around them, her long thin tongue sucking his nipple, her hand on his chest, " + ROS + ", " + PETAL + ", cum dripping untouched"),
 },
 "lose_desc": "keeps him forever as the cherished patient of the hospital's top-floor suite, all twelve beads of his rosary clouded black.",
 "onanie": {
   "master": ("hall", "kneeling in the shadow of a pillar, his chest glossy with lotion, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched, " + ROS),
   "e1": ("dressing", "face buried in a pillow on the bench, humming, rubbing his own nipple under his shirt, penis untouched, " + ROS),
   "e2": ("alley", "crouching in the rain, a lotion-wet hand stroking his own neck, a finger of the other hand in his own anus, penis untouched, " + ROS),
   "e3": ("alley", "face buried in his own pillow, pressing his own nipple with a fingertip, penis untouched, " + ROS),
   "boss": ("grave", "sitting against a gravestone, breathing in pale pink powder, rubbing his own flushed nipples, penis untouched, " + ROS),
 },
 "magic": {
   "1": (None, "shrine", "a rosary of twelve beads lying on wet stone, two beads turned cloudy black and faintly glowing warm, a single red rose petal beside it, close-up"),
   "2": (None, "shrine", "a shrine bell with a thick braided rope swaying by itself at night, faint sound ripples in the air, wet stone pavement, a red rose petal on the ground"),
   "3": ("m", "office", "blowing a handful of red rose petals from her palm toward the viewer, petals swirling in the air, elegant cruel smile"),
   "4": (None, "hangout", "a glass vial of glowing green liquid without text on the arm of an old sofa, one drop falling from its lip, sweet haze, a red rose petal beside it"),
   "5": (None, "special", "an empty top-floor hospital suite, canopy bed, red roses in a vase, a softly swaying cradle of pink slime, a blank nameplate without text on the door, quiet moonlight"),
 },
}
