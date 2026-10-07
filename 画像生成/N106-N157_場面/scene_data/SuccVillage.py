# N148 サキュバスの村（SuccVillage）画像データ。登場人物は全員20歳以上（5人とも女性の淫魔。ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（格闘家も曲線のある体つき）。
# モンクサキュバス：原作は青紫の肌 → pale lilac skin に置き換え。髪はマキュバスと被らないよう magenta の短髪（マキュバス＝light pink の長髪）。
# 挿入の絵はない（pen なし）。後ろに触れるのはエルダーとモンクの指だけ。尻尾（テイルドレイン）は主人公のものを包むだけ。
# 騎乗（恍惚のキス・セクシーダンス）は彼女が上に跨る形で、主人公は動かない（RIDE／RIDE_NEG）。
# 掃除機の管は柔らかい吸い口で吸い付くだけ（痛み・傷なし）。寝技は押さえ込むだけ（関節技・打撃なし）。主人公の手の甲にピンクのハートの淫紋。
MARK = "small glowing pink heart-shaped crest marks on the backs of his hands"
RIDE = "her skirt spread over his hips hiding where they join"
RIDE_NEG = "man on top, he thrusts, he holds her hips"
HOSE = "a soft round suction cup at the end of a vacuum hose stuck on his nipple"
HOSE_NEG = "pain, bruise, wound, scary machine"
TAIL = "the tip of her demon tail opened like a soft flower and wrapped around his penis, sucking"
TAIL_NEG = "teeth, thorns, fangs, scary, tail in anus"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
DATA = {
 "code": "SuccVillage",
 "world": "hidden succubus village deep in a forest at night, purple night sky, pink heart-shaped lanterns, cozy houses with pink lit windows, small bats flying, sweet haze, detailed background",
 "bg": "village square of a hidden succubus village at night, a stone fountain in the center, twelve pink heart-shaped lanterns around the square, cozy houses with pink lit windows, purple night sky, small bats flying, dark forest beyond, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "エルダーサキュバス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 33 years old, adult proportions, beautiful detailed eyes, tall, long legs, colored skin, purple skin, red hair, long wavy hair, hair over one eye, curled ram horns, golden eyes, pointy ears, large bat wings, slender demon tail, elegant black and purple long dress with a deep neckline, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the red-haired purple-skinned elder succubus in a black and purple dress",
         "pose": "one hand lifting the hair that hides one eye, the other hand resting on her hip, graceful composed smile, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "マキュバス",
          "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, light pink hair, very long straight hair, violet eyes, pointy ears, small horns, purple bat wings, slender demon tail, sheer lavender dancer outfit with a long sheer skirt, gold bangles, hip chain, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the long pink-haired succubus dancer in sheer veils",
          "pose": "dancing with one arm raised and her hips swayed to one side, sheer veil trailing from her fingers, alluring half-lidded smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "メイキュバス",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, green hair, shoulder-length bob, amber eyes, pointy ears, white frilled maid headband, small bat wings, slender demon tail, black long-sleeved maid dress, white apron, black pantyhose, holding a vacuum cleaner hose with a soft round nozzle, soft curvy feminine body, large breasts",
          "name": "the green-haired succubus maid in a black maid dress",
          "pose": "standing straight with a vacuum cleaner hose held in both hands, polite quiet smile, looking at viewer",
          "neg": SOFT_NEG + ", " + HOSE_NEG},
   "e3": {"type": "woman", "jp": "モンクサキュバス",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, colored skin, pale lilac skin, magenta hair, short hair, short curved horns, orange eyes, pointy ears, small bat wings, slender demon tail, red sleeveless martial arts outfit with side slits, black sash belt, wrist wraps, black boots, soft curvy feminine body, large breasts, wide hips",
          "name": "the short magenta-haired lilac-skinned succubus monk in a red martial arts outfit",
          "pose": "relaxed fighting stance with one open palm forward, frank cheerful grin, looking at viewer",
          "neg": SOFT_NEG + ", biceps, punching, kicking"},
   "boss": {"type": "woman", "jp": "サキュバス",
            "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, very long hair, red eyes, pointy ears, small black horns, black bat wings, long demon tail with a soft heart-shaped tip, purple bikini, black thigh-high boots, black choker, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the long blonde succubus in a purple bikini and black boots",
            "pose": "leaning forward with one hand beckoning, her tail curled up beside her, bright playful smile, looking at viewer",
            "neg": SOFT_NEG + ", " + TAIL_NEG},
 },
 "places": {
   "forest":  "dark forest at night, tall trees, cold dew, distant pink lights between the trunks",
   "gate":    "village entrance, a heart-shaped wooden gate arch, a small gatekeeper's hut beside it, pink lantern",
   "square":  "village square, a stone fountain with a wide rim to sit on, twelve pink heart-shaped lanterns around the square",
   "inn":     "inn corridor, wooden floor, row of guest room doors, a cleaning closet door at the far end, a vacuum cleaner",
   "room":    "inn guest room, canopy bed with clean white sheets, standing mirror, window showing a purple night sky",
   "brothel": "village pleasure house lounge, velvet sofas, pink lights, incense, a small round stage, a front-row seat",
   "private": "private room of the pleasure house, mirrored ceiling, round bed, standing mirror on the wall",
   "dojo":    "training hall, polished plank floor, incense, martial arts equipment on the wall, a folded futon in the corner",
   "onsen":   "village hot spring, thick steam, pink-tinted water, smooth rocks to sit on",
   "tavern":  "village tavern, wooden counter, glasses of sweet wine, a dancer's stage, cushions on a back seat",
   "field":   "village orchard field at night, vines with round sweet fruits, soft soil",
   "mgate":   "black iron gate of the elder's mansion, bat ornaments, a gate lamp",
   "hall":    "great hall of the elder's mansion, red carpet, portraits without text, incense, a tall elder's chair",
   "bedroom": "elder's bedchamber, black and purple canopy, large bed, a shelf lined with perfume bottles",
   "fount":   "inner room of the elder's mansion, a soft wide bed, twelve pink heart-shaped lamps on the wall",
 },
 "atk": {
   "m1": ("hall", "he sits on the red carpet at her feet looking up, the elder succubus sits in the tall chair leaning down, one hand lifting the hair from her hidden eye, glowing golden eye, her other hand under his chin, " + MARK + ", his body limp"),
   "m2": ("bedroom", "he lies on his back across her lap on the large bed, the elder succubus strokes his nipple slowly with one fingertip, two oiled fingers of her other hand in his anus, fingering, the tip of her tail tickling his inner thigh, calm smile, " + MARK),
   "m3": ("bedroom", "from side, he lies on his back on the large bed, the elder succubus straddles his hips sitting on him, cowgirl position, " + RIDE + ", leaning down kissing him deeply, tongues, saliva trail, one hand on his nipple, " + MARK + ", he lies still", {"neg": RIDE_NEG}),
   "e1": ("brothel", "from side, he sits back on the velvet front-row sofa, the succubus dancer straddles his lap, cowgirl position, " + RIDE + ", her hips swaying as if dancing, arms raised with a sheer veil, " + MARK + ", his eyes fixed on her hips, he sits still", {"neg": RIDE_NEG}),
   "e2": ("room", "he sits on the edge of the canopy bed with his shirt opened, the succubus maid kneels in front of him, " + HOSE + ", her other hand stroking his penis gently, handjob, polite calm face, " + MARK),
   "e3": ("dojo", "he lies on his back on the plank floor, the succubus monk pins him down gently from the side with her arm, thigh and chest, her glowing warm palm pressed on his lower belly, grinning, no pain, " + MARK + ", his body limp"),
   "boss": ("square", "he sits on the fountain rim with his trousers opened, the blonde succubus sits beside him kissing him deeply, tongues, " + TAIL + ", her hands behind her back, " + MARK),
 },
 "atk_desc": {
   "m1": "the elder succubus shows her hidden charming eye and he sits at her feet on his own.",
   "m2": "the elder succubus caresses him slowly with practiced hands and presses inside with her fingers.",
   "m3": "the elder succubus seals his lips with a sweet kiss while sitting astride him.",
   "e1": "the succubus dancer keeps dancing on his lap and he cannot look away from her hips.",
   "e2": "the succubus maid cleans him with a vacuum hose sucking on his nipple.",
   "e3": "the succubus monk holds him down painlessly and pours warm energy into his lower belly.",
   "boss": "the blonde succubus drains him with her tail while sealing his lips with a melting kiss.",
 },
 "lose": {
   # エルダー 技1（誘惑の魔眼）
   "btl_m1":     ("hall", "he sits on her lap in the tall chair facing sideways, the elder succubus lifts the hair from her hidden eye, glowing golden eye close to his face, her other hand stroking his nipple, a small horn ornament on a cord around his neck, " + MARK + ", cum dripping untouched"),
   "onani_m1":   ("room", "kneeling alone before the standing mirror, staring at his own reflection, one hand stroking his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + MARK + ", the elder succubus watches far away outside the window"),
   "inochi_m1":  ("gate", "he stands under the heart-shaped gate arch with his back to the dark forest, the elder succubus stands close holding his hand, lifting her hair to show her glowing golden eye, her fingertips stroking the back of his hand, " + MARK + ", his knees giving way"),
   "onedari_m1": ("fount", "he sits on the soft bed looking up, the elder succubus sits facing him holding his face in one hand, glowing golden eye close to his, whispering, her other hand stroking his lower belly, " + MARK + ", cum dripping untouched"),
   # エルダー 技2（★淫魔の手淫と昇天）
   "btl_m2":     ("bedroom", "he lies on his back across her lap on the large bed, the elder succubus strokes his nipple with one hand, two oiled fingers of her other hand pressing deep in his anus, fingering, her tail tip on his inner thigh, a purple ring on his finger, " + MARK + ", cum on his stomach untouched"),
   "onani_m2":   ("onsen", "sitting alone on a smooth rock in the steam, slowly stroking his own nipple with one fingertip, the other hand reaching behind pressing a finger into his own anus, penis untouched, " + MARK + ", the elder succubus watches far away through the steam"),
   "inochi_m2":  ("hall", "he sits on her lap in the tall chair leaning back against her chest, the elder succubus behind him slowly stroking his lower belly with one palm, her other hand on his nipple, calm teaching smile, " + MARK + ", cum dripping untouched"),
   "onedari_m2": ("fount", "he lies on his back in the middle of the soft bed, the elder succubus sits beside him, one fingertip circling his nipple, two oiled fingers of her other hand in his anus, fingering, counting smile, " + MARK + ", cum on his stomach"),
   # エルダー 技3（恍惚のキス）
   "btl_m3":     ("bedroom", "from side, he lies on his back on the large bed, the elder succubus straddles his hips sitting on him, cowgirl position, " + RIDE + ", kissing him deeply, tongues, saliva trail, her hand on his nipple, a small perfume bottle on the pillow, " + MARK + ", cum overflowing, he lies still", {"neg": RIDE_NEG}),
   "onani_m3":   ("tavern", "sitting alone astride a cushion on the back seat, sucking two of his own fingers as if kissing, hips rocking slightly on the cushion, penis untouched, " + MARK + ", the elder succubus watches far away from the counter"),
   "inochi_m3":  ("mgate", "he leans back against the black iron gate under the gate lamp with his mouth open, the elder succubus holds his chin and kisses him deeply, tongues, saliva trail, her other hand stroking his nipple, " + MARK + ", knees trembling"),
   "onedari_m3": ("fount", "from side, he lies on his back on the soft bed, the elder succubus straddles his hips sitting still on him, cowgirl position, " + RIDE + ", kissing him deeply, saliva dripping from his lips, her hand on his nipple, " + MARK + ", cum overflowing", {"neg": RIDE_NEG}),
   # マキュバス（★セクシーダンス）
   "btl_e1":     ("brothel", "from side, he sits back on the velvet front-row sofa, the succubus dancer straddles his lap, cowgirl position, " + RIDE + ", hips swaying as if dancing, her hands held away from him, a blank member tag without text on his chest, " + MARK + ", cum overflowing, he sits still", {"neg": RIDE_NEG}),
   "onani_e1":   ("private", "standing alone before the wall mirror, swaying his hips as if dancing, both hands stroking his own nipples, penis untouched, " + MARK + ", the succubus dancer watches far away reflected in the mirror at the doorway"),
   "inochi_e1":  ("tavern", "from side, he sits on a tavern chair below the dancer's stage, the succubus dancer straddles his lap, cowgirl position, " + RIDE + ", arms raised dancing, sheer veil over his shoulders, a glass of sweet wine on the table, " + MARK + ", cum overflowing", {"neg": RIDE_NEG}),
   "onedari_e1": ("brothel", "from side, he lies back on the velvet sofa, the succubus dancer straddles his hips, cowgirl position, " + RIDE + ", slowly circling her hips, one fingertip rolling his nipple, pleased alluring smile, " + MARK + ", cum overflowing", {"neg": RIDE_NEG}),
   # メイキュバス（★掃除機ドレイン）
   "btl_e2":     ("room", "he lies on his back on the canopy bed with his shirt opened, the succubus maid sits beside him holding two vacuum hoses, soft round suction cups stuck on both his nipples, her hands not touching him, a white frilled ornament on the pillow, " + MARK + ", cum on his stomach untouched"),
   "onani_e2":   ("inn", "crouching alone in the shadow of the corridor with his shirt opened, pressing a small suction-cup toy onto his own nipple, penis untouched, " + MARK + ", the succubus maid watches far away down the corridor with a vacuum cleaner"),
   "inochi_e2":  ("inn", "he stands with his back against a guest room door with his shirt opened, the succubus maid stands close, " + HOSE + ", her other hand stroking his chest, polite calm face, " + MARK + ", knees trembling, cum dripping"),
   "onedari_e2": ("room", "he sits on the canopy bed with his shirt opened, the succubus maid kneels between his knees, his penis in her mouth, fellatio, " + HOSE + ", " + MARK + ", cum"),
   # モンクサキュバス（★寝技と練気）
   "btl_e3":     ("dojo", "he lies on his back on the plank floor, the succubus monk pins him down gently with her arm, thigh and chest, her glowing warm palm on his lower belly, two oiled fingers of her other hand in his anus, fingering, a black sash tied around his wrist, " + MARK + ", cum dripping untouched"),
   "onani_e3":   ("dojo", "lying alone on his side behind the training equipment, one arm wrapped around his own chest as if pinning himself, the other hand reaching behind stroking his own anus, penis untouched, " + MARK + ", the succubus monk watches far away across the hall"),
   "inochi_e3":  ("dojo", "he lies face up on the plank floor after being rolled over, the succubus monk lies across his chest holding him down with her weight and soft chest, grinning, her palm glowing warm on his lower belly, " + MARK + ", his body limp, cum dripping"),
   "onedari_e3": ("dojo", "he lies on his back on the unfolded futon in the corner, the succubus monk pins his shoulders with one arm and her thigh, two oiled fingers of her other hand pressing in his anus, fingering, counting aloud, " + MARK + ", cum on his stomach"),
   # サキュバス（★テイルドレイン）
   "btl_boss":   ("square", "he sits on the fountain rim with his trousers opened, the blonde succubus sits beside him kissing him deeply, tongues, saliva trail, " + TAIL + ", her hands behind her back, a purple ribbon tied on his wrist, all the heart lanterns lit, " + MARK + ", cum overflowing from her tail"),
   "onani_boss": ("gate", "crouching alone behind the gatekeeper's hut, stroking his own inner thigh with a loosened waist cord, penis untouched, " + MARK + ", the blonde succubus watches far away from the top of the gate arch"),
   "inochi_boss":("square", "he stands by the fountain, the blonde succubus hugs his arm cheerfully, her long tail wound around his waist, " + TAIL + ", pointing at the fountain with her free hand, " + MARK + ", knees trembling, cum dripping"),
   "onedari_boss":("square", "he sits on the fountain rim leaning back on his hands, the blonde succubus leans over him kissing him deeply, tongues, " + TAIL + ", delighted smile, " + MARK + ", cum overflowing from her tail"),
 },
 "lose_desc": "keeps him in the village forever as its shared spring, twelve pink heart crests glowing on the backs of his hands.",
 "onanie": {
   "master": ("square", "kneeling in the shadow of the fountain, slowly circling his own nipple with one fingertip, the other hand reaching behind pressing a finger into his own anus, penis untouched, " + MARK),
   "e1": ("private", "standing before the wall mirror, swaying his hips as if dancing, both hands stroking his own nipples, penis untouched, " + MARK),
   "e2": ("inn", "crouching in the corridor shadow with his shirt opened, pressing a small suction-cup toy onto his own nipple, penis untouched, " + MARK),
   "e3": ("dojo", "lying on his side, one arm wrapped around his own chest as if pinning himself, the other hand reaching behind stroking his own anus, penis untouched, " + MARK),
   "boss": ("gate", "crouching behind the gatekeeper's hut, stroking his own inner thigh with a loosened waist cord, penis untouched, " + MARK),
 },
 "magic": {
   "1": (None, "square", "two pink heart-shaped lanterns lighting up side by side on an iron post, soft pink glow spreading, close-up, lantern without text"),
   "2": ("boss", "gate", "waving one hand high and beckoning with the other under the heart-shaped gate arch, bright welcoming smile"),
   "3": (None, "bedroom", "a small pink glass perfume bottle with its stopper removed on a shelf, sweet pink mist drifting out, bottle without text"),
   "4": (None, "tavern", "a glass of pink fruit wine and a bottle without text on the wooden counter, round sweet fruits on a vine beside it, warm light"),
   "5": (None, "fount", "an empty soft wide bed in a quiet room, twelve pink heart-shaped lamps glowing on the wall, incense smoke, the door left open"),
 },
}
