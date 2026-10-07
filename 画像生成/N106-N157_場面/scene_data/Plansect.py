# N144 世界樹とプランセクト村（Plansect）画像データ。登場人物は全員20歳以上（植物の魔物は数百歳の大人）。5人とも女性（ふたなりではない）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。下半身は植物（花・植物の体・食虫植物の口・木の根）。
# ワルラウネ：原作は水色の肌・髪・触手 → 髪は pale mint-white、肌は very pale skin、触手は pale mint と書く（青・水色は主人公と紛れるため使わない）。
# 髪色の書き分け：クィーン＝紫／ドローシー＝濃いエメラルド緑／ディーナ＝黒（資料に髪の記述なし。緑の肌と赤い目が目印）／ワルラウネ＝淡いミント白／フォレストドリアード＝明るい黄緑。
# 挿入はクィーンの細い蔦と指、ドローシーの腺毛を束ねた指だけ（どちらも pen なし）。ディーナ・ワルラウネ・フォレストドリアードは後ろに触れない。
# 痛みなし：食虫植物の口は歯がなく消化しない。棘は刺さらない。怖い・グロテスクにしない。主人公の肌には花のつぼみ。
BUDS = "flower buds blooming on his collarbone and wrists"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, gore, sharp teeth, fangs, insect legs"
TRAP_NEG = SOFT_NEG + ", teeth on the plant, digestion, melting, swallowed whole, vore"
HAIRS = "glistening sticky green tendril hairs"
DATA = {
 "code": "Plansect",
 "world": "fantasy forest village of plant monster women at the foot of a colossal world tree, sweet flower haze, drifting golden pollen, dappled sunlight, detailed background",
 "bg": "the top of a colossal world tree above the clouds, wind and open sky, a giant purple flower in full bloom on the crown, a sea of forest and a distant flower village far below, drifting petals, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "クィーンアルラウネ",
         "tags": "adult woman, mature female, mature face, elegant adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, plant girl, alraune, monster girl, purple hair, very long hair, violet eyes, flower crown, dress made of purple petals, her lower body rising from the center of a giant purple flower, large purple petals around her, thin green vines, soft voluptuous feminine body, huge breasts",
         "name": "the purple-haired flower queen in a giant purple flower",
         "pose": "rising from the center of a giant purple flower, one hand held out in invitation, serene gentle smile, looking down at viewer",
         "neg": SOFT_NEG + ", human legs on the woman"},
   "e1": {"type": "woman", "jp": "ディーナ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, plant girl, monster girl, green skin, colored skin, black hair, long straight hair, red eyes, crest marking on her forehead, leaf bandeau top, her lower body emerging from a giant green flytrap plant pod with soft smooth toothless lips, green vines, soft curvy feminine body, large breasts",
          "name": "the green-skinned flytrap woman with red eyes",
          "pose": "emerging from a giant green plant pod, hands folded at her chest, quiet faint smile, looking at viewer with red eyes",
          "neg": TRAP_NEG + ", human legs on the woman"},
   "e2": {"type": "woman", "jp": "ワルラウネ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, plant girl, alraune, monster girl, very pale skin, pale mint-white hair, long hair, large pink flower in her hair, pink eyes, pink petal bandeau top, her lower body rising from a large pink flower, pale mint tentacle vines, soft curvy feminine body, large breasts",
          "name": "the mint-haired flower woman with a pink flower",
          "pose": "rising from a large pink flower, one hand on her hip, twirling her hair with a finger, teasing smirk, looking at viewer",
          "neg": SOFT_NEG + ", human legs on the woman"},
   "e3": {"type": "woman", "jp": "フォレストドリアード",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, dryad, plant girl, monster girl, light yellow-green hair, very long wavy hair, leaf hair ornament, amber eyes, long green dress, her lower body made of black tree roots, green vines, soft curvy feminine body, large breasts",
          "name": "the yellow-green-haired dryad in a green dress",
          "pose": "standing on black tree roots, hands clasped in front of her, soft dreamy smile, head tilted, looking at viewer",
          "neg": SOFT_NEG + ", human legs on the woman"},
   "boss": {"type": "woman", "jp": "ドローシー",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, plant girl, monster girl, dark emerald green hair, very long hair, golden eyes, large red flower petals around her shoulders like a collar, green leaf dress, her lower body a huge green plant with clusters of red berries, glistening sticky green tendril hairs, soft voluptuous feminine body, huge breasts",
            "name": "the emerald-haired village chief with red petals",
            "pose": "rising from a huge green plant with red berries, arms crossed under her breasts, confident big-sisterly smile, looking down at viewer",
            "neg": SOFT_NEG + ", human legs on the woman"},
 },
 "places": {
   "trail":   "forest path, dappled sunlight, creeping vines on the ground, a big tree trunk, sweet haze",
   "gate":    "village entrance, an arch woven of colorful flowers, a wooden lookout seat",
   "plaza":   "village square, a fountain shaped like a large flower, stone pavement scattered with petals",
   "field":   "village vegetable field, dark soil, ripe crops, a fence of vines, a wooden watch hut",
   "manor":   "inside a house grown from a huge plant, clusters of red berries hanging from the ceiling, a soft bed of leaves under the red berries, sticky tendril hairs on the walls",
   "swamp":   "warm shallow swamp, damp earth, large open plant pods, big flowers on the bank, pale green mist",
   "den":     "a room like the inside of a giant plant pod, soft smooth green walls, pale green light",
   "garden":  "flower garden of many colors, pollen drifting in the air, a flat stone in the middle",
   "wflower": "field of pink flowers, pale mint tentacle vines swaying, amber sap glistening on the petals",
   "root":    "the foot of the world tree, giant roots, moss, amber sap, cool shade",
   "hollow":  "a hollow inside the world tree trunk, faint glow, a bed of moss, large green leaves",
   "branch":  "a path along a thick branch of the world tree, wind, a sea of forest far below",
   "spring":  "clear forest spring, black tree roots at the water's edge, light on the water surface",
   "top":     "the top of the world tree, wind and open sky, a giant purple flower in bloom",
   "inside":  "inside a giant purple flower, enclosed by large soft purple petals, golden nectar, pale purple light",
 },
 "atk": {
   "m1": ("top", "he walks unsteadily toward the giant purple flower with a dazed look, the flower queen leans out of the flower holding out both arms to him, sweet purple scent haze drifting from the petals around his face, cheeks flushed, " + BUDS),
   "m2": ("inside", "from side, he is wrapped up to his shoulders in large soft purple petals with only his face showing, the flower queen embraces him from behind, thin green vines curled around his nipples, another thin vine slipped into his anus, nectar dripping, " + BUDS),
   "m3": ("inside", "the flower queen holds his face in both hands and kisses him deeply, golden nectar flowing from her lips into his mouth, tongues, nectar running down his chin, her nectar-wet fingers in his anus, fingering, petals around them, " + BUDS),
   "e1": ("den", "his lower body is enveloped up to the waist in the giant soft green plant pod, the flytrap woman holds his upper body in her arms from the front, her fingers rolling his nipple, soft inner walls squeezing his hips, flushed, " + BUDS),
   "e2": ("wflower", "he lies on his back among pink flowers, the flower woman leans over his hips squeezing his penis between her breasts glossy with amber sap, paizuri, amber sap shining on his nipples, a pale mint tentacle vine stroking his inner thigh, teasing smirk, " + BUDS),
   "e3": ("spring", "he stands with his back against a tree trunk, black roots and green vines wound around his wrists and ankles, the dryad leans close with a gentle smile, soft cup-shaped vine tips sucking his nipples, another soft vine tip covering his penis, " + BUDS),
   "boss": ("manor", "he lies on the bed of leaves, his arms chest waist and legs stuck with " + HAIRS + ", unable to move, the village chief leans over him, sticky hairs tugging his nipples, two sap-wet fingers of bundled hairs in his anus, fingering, grin, " + BUDS),
 },
 "atk_desc": {
   "m1": "the flower queen's scent makes him walk to her flower on his own feet.",
   "m2": "the flower queen wraps him in her petals while thin vines stroke his nipples and inside him.",
   "m3": "the flower queen feeds him nectar with a deep kiss while her fingers loosen him.",
   "e1": "the flytrap woman envelops his lower body in her soft toothless plant pod and holds him close.",
   "e2": "the flower woman makes him sensitive with amber sap and squeezes him between her breasts.",
   "e3": "the dryad binds him to a tree with roots and lets her vine tips suck him.",
   "boss": "the village chief sticks him down with sticky tendril hairs and presses inside with her fingers.",
 },
 "lose": {
   # クィーン 技1（フラワーフレグランス）
   "btl_m1":     ("top", "he stands at the edge of the fully opened giant purple flower, the flower queen pulls him into her arms, large petals closing around his legs and waist, purple scent haze around his face, thin vines stroking his nipples, a necklace of purple petals on his neck, many flower buds blooming on his skin, cum dripping"),
   "onani_m1":   ("garden", "kneeling alone in the shadow of the flat stone, breathing in a flower held to his nose, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, the flower queen watches far away from the sky above"),
   "inochi_m1":  ("branch", "on the thick branch high above the forest, he stands turned back toward the treetop, the flower queen leans down from her flower holding his cheeks, blowing purple scent haze onto his face, thin vines around his waist, knees trembling, cum dripping untouched, " + BUDS),
   "onedari_m1": ("inside", "he kneels with his face pressed to the flower queen's chest, breathing deeply, the flower queen holds his head and strokes his hair, thick purple scent haze around them, thin vines rolling his nipples, cum dripping untouched, many flower buds blooming on his skin"),
   # クィーン 技2（★女王花の抱擁）
   "btl_m2":     ("inside", "from side, he is wrapped up to his shoulders in large soft purple petals, the flower queen embraces him from behind, thin green vines curled around both his nipples, a thin vine in his anus, a glass vial of golden nectar beside them, cum on the petals, many flower buds blooming on his skin"),
   "onani_m2":   ("hollow", "lying alone on the moss bed wrapped in a large green leaf, one hand rubbing his own nipple under the leaf, a finger of the other hand in his own anus, penis untouched, the flower queen watches far above through the opening of the hollow"),
   "inochi_m2":  ("root", "at night between the giant roots, he lies curled on the moss, large purple petals lowered around him like a blanket, the flower queen leans down over him, thin vines stroking his nipples and inner thighs, moonlight, cum dripping, " + BUDS),
   "onedari_m2": ("inside", "he lies on his back in the center of the flower, petals wrapped around his arms and legs, the flower queen leans over him smiling, several thin vines curled around both his nipples, one thin vine in his anus, nectar, cum on his stomach untouched"),
   # クィーン 技3（受粉の口づけ）
   "btl_m3":     ("inside", "the flower queen holds him in her arms kissing him deeply, golden nectar running from the corners of his mouth, petals wrapped around his body, a thin vine in his anus, another vine on his nipple, an amber nectar gem on a cord at his neck, cum dripping"),
   "onani_m3":   ("spring", "kneeling alone at the edge of the spring, sucking two of his own nectar-wet fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, a purple flower reflected on the water, the flower queen watches far away"),
   "inochi_m3":  ("top", "he stands at the edge of the giant flower reaching up, the flower queen bends down holding his chin and kissing him, a thread of nectar between their lips, wind, petals rising around his legs, he clings to her arms, " + BUDS),
   "onedari_m3": ("inside", "in pale purple light inside the closed flower, he sits held against the flower queen facing her, long deep kiss, nectar overflowing from his mouth, her two fingers in his anus, fingering, a thin vine around his nipple, cum dripping"),
   # ディーナ（★ビーナストラップ）
   "btl_e1":     ("den", "his lower body is held up to the waist in the closed soft green plant pod, the flytrap woman embraces his upper body, licking one nipple and rolling the other with her fingers, a leaf-shaped ornament on a cord at his neck, many green flower buds on his skin, he trembles, cum leaking"),
   "onani_e1":   ("swamp", "sitting alone with his lower body inside a large flower at the edge of the swamp, both hands rubbing his own nipples, hips swaying, penis untouched, the flytrap woman watches far away across the water"),
   "inochi_e1":  ("swamp", "he stands in the warm shallow water near the far bank, a soft green plant pod risen from the water closed around his legs up to the waist, the flytrap woman close behind him embracing his chest, her fingers on his nipples, his knees weak, " + BUDS),
   "onedari_e1": ("den", "he leans back against the soft green wall, his lower body held in the closed plant pod, the flytrap woman presses her chest to his, hugging him tightly, one hand stroking his nipple, quiet faint smile, he trembles, cum leaking"),
   # ワルラウネ（★恍惚樹液の胸）
   "btl_e2":     ("wflower", "he lies on his back among pink flowers, the flower woman leans over his hips squeezing his penis between her sap-glossy breasts, paizuri, amber sap on his nipples, a pale mint tentacle vine on his inner thigh, a piece of pale mint vine tied at his wrist, cum on her breasts, smirk"),
   "onani_e2":   ("garden", "crouching alone behind tall flowers, spreading amber sap on his own nipples with his fingertips, circling, penis untouched, the flower woman watches far away with a smirk"),
   "inochi_e2":  ("wflower", "he sits dazed in the middle of the pink flower field, golden pollen drifting, the flower woman leans over him shaking her hair above his face, her finger spreading amber sap on his nipple, smirk, his cheeks flushed, cum dripping untouched"),
   "onedari_e2": ("wflower", "under a large pink flower, he sits leaning back on his hands, the flower woman presses her sap-glossy breasts against his chest, rubbing them over his nipples, threads of amber sap, a pale mint tentacle vine on his inner thigh, cum dripping untouched"),
   # フォレストドリアード（★ツタ吸精）
   "btl_e3":     ("spring", "he stands tied to a tree trunk, black roots and vines wound around his wrists and ankles, the dryad whispers at his ear with her dress neckline open, soft vine tips sucking both his nipples and covering his penis, a bracelet woven of black roots on his wrist, cum dripping"),
   "onani_e3":   ("trail", "sitting alone against a big tree trunk, a fallen vine wound around one wrist, the other hand rubbing his own nipple, penis untouched, the dryad watches far away between the trees"),
   "inochi_e3":  ("root", "at the foot of the giant world tree, he leans back against the trunk, black roots wound around his wrists and ankles, the dryad gently holds his cheek, soft vine tips sucking his nipples, a path of roots behind them, cum dripping, " + BUDS),
   "onedari_e3": ("spring", "he sits at the root of a tree by the spring, wrists bound above his head with vines, the dryad leans over him holding him to her chest, soft vine tips sucking both his nipples, gentle smile, white flower buds on his skin, cum dripping untouched"),
   # ドローシー（★ネバネバ腺毛）
   "btl_boss":   ("manor", "he lies on the bed of leaves under the red berries, his whole body stuck with " + HAIRS + ", the village chief leans over him, sticky hairs stroking both his nipples, two sap-wet fingers of bundled hairs in his anus, fingering, a red berry pendant at his neck, cum on his stomach untouched"),
   "onani_boss": ("field", "sitting alone in the shadow of the watch hut, palms coated with sticky amber sap, pressing a sticky palm to his chest and pulling at his own nipple, threads of sap, penis untouched, the village chief watches far away across the field"),
   "inochi_boss":("plaza", "in the village square with a hoe dropped at his feet, his wrists stuck together with " + HAIRS + ", the village chief holds him from behind laughing, sticky hairs stroking his nipples, petals on the stone pavement, cum dripping, " + BUDS),
   "onedari_boss":("manor", "he lies spread on the bed of leaves, his whole body covered with " + HAIRS + ", the village chief sits close beside him, two fingers in his anus, fingering, sticky hairs on both his nipples, satisfied smile, cum on his stomach untouched"),
 },
 "lose_desc": "keeps him forever in the flower village as the world tree's pollination partner, flower buds blooming on his skin.",
 "onanie": {
   "master": ("hollow", "lying on a moss bed wrapped in a large green leaf, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched"),
   "e1": ("swamp", "sitting with his lower body inside a large flower, both hands rubbing his own nipples, penis untouched"),
   "e2": ("garden", "crouching behind flowers, spreading amber sap on his own nipples with his fingertips, penis untouched"),
   "e3": ("trail", "sitting against a tree trunk, a vine wound around one wrist, the other hand rubbing his own nipple, penis untouched"),
   "boss": ("field", "sitting by a watch hut, pressing a sap-sticky palm to his chest and pulling at his own nipple, penis untouched"),
 },
 "magic": {
   "1": (None, "inside", "a glass vial of glowing golden nectar resting on a purple petal, a single drop of nectar falling, vial without text, close-up"),
   "2": (None, "gate", "an arch woven of colorful flowers over a village path, petals falling, soft welcoming light"),
   "3": ("m", "top", "scattering shimmering golden pollen from her open palm, pollen drifting on the wind, serene gentle smile"),
   "4": (None, "garden", "a swirling cloud of golden pollen above blooming flowers, sparkling dreamy haze"),
   "5": (None, "root", "giant mossy roots of the world tree creeping across the ground, a faint warm glow pulsing along the roots, amber sap beads"),
 },
}
