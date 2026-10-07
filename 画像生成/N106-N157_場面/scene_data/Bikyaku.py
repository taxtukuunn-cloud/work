# N141 美脚塔（Bikyaku）画像データ。登場人物は全員20歳以上。6人とも人間の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない。原作の立ち絵は参照していない）。
# 髪色は被らせない：ビリジアン＝深緑のまとめ髪／アイリス（立ち絵の2人目だけ）＝紫の巻き髪／バーミリオン＝赤の長髪／
#   ノワール＝黒髪ロング／カイゼリン＝金髪のウェーブ／ロイヤルバニー＝淡いピンクのボブ。青・水色系の髪・瞳は使っていない
#   （原作で色の分からない部分は役に合う色で決めた）。
# マスターは2人組：立ち絵だけ2人（pose に2人目＝アイリス）。技CG・敗北CGは「ビリジアン1人＋主人公」に置き換え
#   （アイリスの香り・顔の上に座る役は描かず、ビリジアンの脚・口づけ・香水の小瓶で表す。3人以上を出さない）。
# このMODに挿入はない（pen なし。後ろには触れない）。脚・足指・爪先・香りだけ。
# 踏む絵は「乗せるだけ・痛みなし」（resting lightly）。打撃・締め技・電気あんまは描かない。ノワールは肌に触れない。
ANK = "thin gold chain anklets on his ankle"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
STEP_NEG = "pain, crying, bruise, stomping hard, crushing, kicking, sharp stiletto digging into skin, scary"
DATA = {
 "code": "Bikyaku",
 "world": "elegant white marble tower of beautiful ladies by the sea, polished marble floors, red carpets, pillars carved in the shape of slender legs, warm chandelier light, detailed background",
 "bg": "upper landing of a white marble tower, polished marble floor with a long red carpet, a purple door and a green door side by side, pillars carved in the shape of slender legs, an empty velvet bench, a tall window showing the sea, warm chandelier light, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "レディビリジアン（＋レディアイリス）",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, very long legs, dark green hair, elegant updo, emerald green eyes, long emerald green evening dress with a high side slit, sheer pale green silk stockings, green high heels, long gloves, soft curvy feminine body, large breasts, wide hips",
         "name": "the green-dressed lady with an updo and silk stockings",
         "pose": "the back of one hand raised to her mouth in a haughty laugh, one long stockinged leg stepping out of the dress slit, looking down at viewer, standing beside a second adult woman with long curly purple hair in a purple evening dress with huge breasts and wide hips who rests one hand on her hip with a commanding smile",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG + ", " + STEP_NEG},
   "e1": {"type": "woman", "jp": "レディバーミリオン",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, bright red hair, very long straight hair, red eyes, long red evening dress with a side slit, bare legs, glossy red high heels with rounded toes, soft curvy feminine body, large breasts, wide hips",
          "name": "the red-haired lady in a red dress and red high heels",
          "pose": "sitting on the edge of a table with her legs crossed, dangling one red high heel from her toes, teasing playful grin, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", " + STEP_NEG},
   "e2": {"type": "woman", "jp": "メイドノワール",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long straight hair, hime cut, grey eyes, jet black long maid dress, small white apron, white maid headdress, black stockings, black heeled shoes, soft curvy feminine body, large breasts",
          "name": "the black-haired maid in a jet black maid dress and black stockings",
          "pose": "lifting the hem of her long skirt a little with both hands to show her black-stockinged calves, graceful quiet smile, looking at viewer, faint pink scented haze around her",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "マスカレードカイゼリン",
          "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, very long legs, golden blonde hair, long wavy hair, golden eyes, ornate gold masquerade mask covering only her eyes, black and gold empress dress with a high side slit, black stockings, black high heels with gold trim, soft curvy feminine body, large breasts, wide hips",
          "name": "the gold-masked empress in a black and gold dress",
          "pose": "sitting on a throne-like chair with her long legs crossed, chin resting on the back of her hand, composed amused smile, looking down at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", " + STEP_NEG + ", full face mask, mask removed"},
   "boss": {"type": "woman", "jp": "ロイヤルバニー",
            "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale pink hair, short bob, amber eyes, white rabbit ears headband, white and gold bunny suit, strapless leotard, gold bow tie collar, white wrist cuffs, black fishnet tights, white high heels, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the pink-bob bunny in a white and gold bunny suit and fishnet tights",
            "pose": "holding a silver tray with a champagne glass in one hand, the other hand on her chest in a polite bow, courteous smile with a hint of irony, looking at viewer",
            "height_note": "she is much taller than him",
            "neg": SOFT_NEG},
 },
 "places": {
   "beach":    "white sand beach, gentle waves, a white tower far away on the shore",
   "gate":     "tower entrance, a tall marble door, pillars carved in the shape of slender legs, a cool brass handle",
   "hall":     "great hall on the first floor, red carpet, decorative masks on the walls, a throne-like chair, a very high ceiling",
   "anteroom": "dressing anteroom, a large standing mirror, shelves of folded silk stockings, soft light",
   "corridor": "long corridor on the second floor, marble pillars casting shadows, faint pink scented haze, a red carpet runner",
   "black":    "jet black room, black curtains, a black bed, an incense burner with thin pink smoke, a tea set on a small table",
   "red":      "red room, a wardrobe of red dresses, red carpet, a display stand with rows of high heels",
   "bunny":    "casino-like lounge on the third floor, gaming tables with chips, framed pictures of legs in fishnet tights, a reserved booth seat",
   "lounge":   "hospitality room, a deep soft sofa, champagne glasses on a silver tray, soft cushions, warm lamp light",
   "landing":  "landing before two doors, a purple door and a green door side by side, a velvet bench, red carpet",
   "purple":   "purple room, purple curtains, a large sofa, a thick rug, a small perfume bottle on a side table",
   "green":    "green-walled room, a large mirror, shelves of high heels, a polished floor",
   "window":   "tower window nook, a wide window showing the sea, a soft carpet under the window, sea breeze moving the curtain",
   "footrest": "small room between the purple door and the green door, a soft carpet between two facing sofas",
 },
 "atk": {
   "m1": ("landing", "low angle, he kneels on the red carpet with his hands on the floor looking up, the green-dressed lady sits on the velvet bench slowly crossing her long silk-stockinged legs in front of his face, laughing behind the back of her hand, " + ANK),
   "m2": ("purple", "he lies on his back on the thick rug, the green-dressed lady sits on the sofa edge above him, his penis held between her silk-stockinged thighs and knees, thigh job, one stockinged foot stroking his chest, sweet perfume haze, haughty laugh, " + ANK),
   "m3": ("footrest", "he sits on the carpet between the two sofas with his face tilted up, the green-dressed lady leans down from the sofa kissing him deeply, tongues, saliva trail, her silk-stockinged foot stroking his lower belly, a lipstick mark on his neck, " + ANK),
   "e1": ("red", "he lies on his back on the red carpet with his shirt open, the red-haired lady stands over him, the rounded toe of her red high heel gently poking and circling his nipple without pressing, teasing grin, his back arched, " + ANK),
   "e2": ("black", "he kneels with his clothes folded beside him, flushed, leaning his face toward her legs by himself, the maid sits still on the edge of the black bed with her skirt hem raised showing her crossed black-stockinged legs, not touching him, pink scented haze, " + ANK),
   "e3": ("hall", "low angle, he lies on his back on the red carpet at the foot of the throne-like chair, the masked empress sits above him, one high heel resting lightly on his chest, her other shoeless stockinged sole pressing and circling his penis against his belly, footjob, amused smile, " + ANK),
   "boss": ("lounge", "he sits naked on the deep sofa, the bunny sits facing him on a stool, the toes of one fishnet foot gripping his penis, footjob, the toes of her other foot pinching his nipple, lifting his chin with her fingertip, polite ironic smile, a champagne glass, " + ANK),
 },
 "atk_desc": {
   "m1": "the green-dressed lady tames him just by crossing and recrossing her stockinged legs.",
   "m2": "the green-dressed lady clamps him between her silk-stockinged thighs while sweet perfume clouds his head.",
   "m3": "the green-dressed lady seals his lips with a kiss while her stockinged foot keeps stroking his belly.",
   "e1": "the red-haired lady trains his nipples with the rounded toe of her red high heel, painlessly.",
   "e2": "the maid lures him with her sweet scent and her black-stockinged legs without touching him at all.",
   "e3": "the masked empress rests her heel on his chest painlessly and rubs him with her sole.",
   "boss": "the bunny serves him with her dexterous fishnet toes and lifts his chin.",
 },
 "lose": {
   # 双璧 技1（懐柔）
   "btl_m1":     ("landing", "low angle, he lies on his back on the red carpet below the velvet bench, the green-dressed lady sits above him crossing her legs, his penis held between her silk-stockinged calves, one stockinged toe resting on his chest, laughing, twelve " + ANK + ", cum on his stomach"),
   "onani_m1":   ("window", "lying alone face down on the carpet under the window, his chest pressed to the carpet, one hand under his chest stroking his own nipple, " + ANK + ", penis untouched, the green-dressed lady watches far away from a doorway"),
   "inochi_m1":  ("landing", "he kneels on the red carpet between the purple door and the green door looking up, the green-dressed lady sits on the bench before him crossing her silk-stockinged legs, her stockinged foot stroking his penis, footjob, the back of her hand at her laughing mouth, " + ANK + ", cum dripping"),
   "onedari_m1": ("footrest", "he lies on his back on the soft carpet between the two sofas, the green-dressed lady sits on a sofa above him with her legs crossed, her crossed stockinged foot resting lightly on his chest, toe stroking his nipple, pleased laugh, " + ANK + ", cum on his stomach"),
   # 双璧 技2（★双璧の脚）
   "btl_m2":     ("purple", "he lies on his back on the thick rug, the green-dressed lady sits on the sofa edge above him, his penis clamped still between her silk-stockinged thighs, thigh job, her stockinged toes on his nipple, a perfume bottle beside his head, sweet haze, " + ANK + ", cum on her stockings"),
   "onani_m2":   ("green", "lying alone on his back on the polished floor before the large mirror, a cushion over his face, a pillow squeezed between his own thighs, both hands stroking his own nipples, " + ANK + ", penis untouched, the green-dressed lady watches far away reflected in the mirror"),
   "inochi_m2":  ("purple", "at night, he lies drowsy on the large sofa, the green-dressed lady reclines beside him with his hips caught between her long silk-stockinged legs, her thighs squeezing his penis, thigh job, her hand over her smiling mouth, a blanket slipping off, " + ANK + ", cum dripping"),
   "onedari_m2": ("footrest", "he lies on his back on the soft carpet between the two sofas, the green-dressed lady sits above him, his penis clamped between her silk-stockinged knees and held still, thigh job, counting on her gloved fingers, haughty laugh, " + ANK + ", cum on her stockings"),
   # 双璧 技3（貴婦人の口づけ）
   "btl_m3":     ("footrest", "he sits on the carpet between the two sofas, the green-dressed lady leans down from the sofa kissing him deeply, tongues, saliva trail, his penis held between her silk-stockinged calves, lipstick marks on his cheek and neck, " + ANK + ", cum on her stockings"),
   "onani_m3":   ("landing", "sitting alone on the velvet bench before the two doors, sucking two of his own fingers as if kissing, the other hand stroking his own nipple, " + ANK + ", penis untouched, the green-dressed lady watches far away from the green door"),
   "inochi_m3":  ("purple", "in morning light, he sits on the large sofa with his face tilted up, the green-dressed lady holds his chin and kisses him, tongues, her silk-stockinged thigh pressed between his legs against his penis, several lipstick marks on his face, " + ANK + ", cum dripping"),
   "onedari_m3": ("footrest", "he lies on his back in the middle of the soft carpet, the green-dressed lady kneels over him kissing him deeply, her silk-stockinged shin stroking his lower belly and penis, a fresh lipstick mark on his collarbone, " + ANK + ", cum on his stomach"),
   # バーミリオン（★脚での乳首開発）
   "btl_e1":     ("red", "he lies on his back on the red carpet, the red-haired lady sits on a chair above him with one shoe off, her bare toes gently pinching his nipple, the rounded toe of her other red high heel circling his other nipple, teasing grin, a red heel charm on his anklet, cum on his stomach untouched"),
   "onani_e1":   ("corridor", "sitting alone curled up in the shadow of a pillar, hugging one knee, poking his own nipple with the toes of his own foot, " + ANK + ", penis untouched, the red-haired lady watches far away down the corridor"),
   "inochi_e1":  ("red", "he lies on his back on the red carpet pushing his chest up by himself, the red-haired lady stands over him, the rounded toe of her red high heel gently rubbing his erect nipple, her hands on her hips, playful grin, his penis untouched and dripping, " + ANK),
   "onedari_e1": ("red", "he lies on his back on the red carpet, the red-haired lady sits on a low stool with her shoes off, her bare toes pinching his right nipple, the top of her other foot resting on his penis, counting with a raised finger, grin, " + ANK + ", cum on his stomach"),
   # ノワール（★淫香の誘い）
   "btl_e2":     ("black", "he kneels on the floor rubbing his cheek against her black-stockinged shin by himself, the maid sits still on the black bed with her legs crossed and her hands folded on her lap, not touching him, thick pink scented haze, a strip of black stocking tied on his anklet, cum dripping untouched"),
   "onani_e2":   ("corridor", "crouching alone in the shadow of a pillar, holding a perfume bottle without label under his nose, the other hand stroking his own nipple, " + ANK + ", penis untouched, the maid watches far away at the end of the corridor"),
   "inochi_e2":  ("black", "he kneels beside the tea table holding an empty teacup, his cheek resting against her black-stockinged knee by himself, the maid sits still on a chair holding a teapot, not touching him, sweet steam and pink haze, " + ANK + ", cum dripping untouched"),
   "onedari_e2": ("black", "he lies on the black bed with his face pressed to her right black-stockinged thigh by himself, breathing in deeply, his hips rubbing against the sheets, the maid sits still against the headboard with her skirt hem raised, hands folded, pink scented haze, " + ANK + ", cum on the sheets"),
   # カイゼリン（★女帝の踏みつけ）
   "btl_e3":     ("hall", "low angle, he lies on his back at the foot of the throne-like chair, the masked empress sits above him laughing softly, one high heel resting lightly on his chest, her shoeless stockinged sole circling his penis against his belly, footjob, a gold mask charm on his anklet, cum on his stomach"),
   "onani_e3":   ("anteroom", "lying alone on his back before the large mirror with his knees bent, pressing the sole of his own foot against his own lower belly, " + ANK + ", penis untouched, the masked empress watches far away reflected in the mirror"),
   "inochi_e3":  ("hall", "he crouches on all fours on the red carpet kissing the top of her stockinged foot, the masked empress sits on the throne-like chair, the toe of her other high heel resting lightly on his head, a staircase visible far behind, amused smile, " + ANK + ", cum dripping untouched"),
   "onedari_e3": ("hall", "low angle, he lies on his back at the foot of the throne-like chair with his arms open, the masked empress sits above him, her shoeless stockinged foot resting lightly on his chest, her hand at her smiling lips, laughing down at him, " + ANK + ", cum on his stomach untouched"),
   # ロイヤルバニー（★自在なる足指）
   "btl_boss":   ("lounge", "he sits naked on the deep sofa, the bunny sits facing him, the toes of one fishnet foot holding his penis still, footjob, lifting his chin with the toes of her other foot, polite ironic smile, a white and gold rabbit ear charm on his anklet, cum on her fishnet foot"),
   "onani_boss": ("bunny", "sitting alone on the floor behind the reserved booth seat, hugging one knee, stroking his own lower belly with the toes of his other foot, hands on the floor, " + ANK + ", penis untouched, the bunny watches far away beside a gaming table"),
   "inochi_boss":("lounge", "he sits slumped on the deep sofa, the bunny sits beside him tilting a champagne glass to his lips, her fishnet foot in his lap stroking his penis with her toes, footjob, three empty glasses on the silver tray, courteous smile, " + ANK + ", cum dripping"),
   "onedari_boss":("lounge", "he sits on the deep sofa with his head tilted back, the bunny sits on the low table facing him, her fishnet toes gripping his penis without moving, footjob, lifting his chin with her fingertip, three fingers raised on her other hand, " + ANK + ", cum on her fishnet foot"),
 },
 "lose_desc": "keeps him in the tower forever as the ladies' cherished footrest, twelve thin gold anklets on his ankle, never harmed.",
 "onanie": {
   "master": ("landing", "lying on his back in the shadow of a pillar, a cushion over his face, a pillow squeezed between his own thighs, both hands stroking his own nipples, penis untouched"),
   "e1": ("corridor", "curled up hugging one knee, poking his own nipple with the toes of his own foot, penis untouched"),
   "e2": ("corridor", "crouching, smelling a perfume bottle without label, the other hand stroking his own nipple, penis untouched"),
   "e3": ("anteroom", "lying on his back with knees bent, pressing the sole of his own foot against his own lower belly, penis untouched"),
   "boss": ("bunny", "sitting hugging one knee, stroking his own lower belly with the toes of his other foot, hands on the floor, penis untouched"),
 },
 "magic": {
   "1": (None, "landing", "two thin gold chain anklets lying on a red velvet cushion, soft warm glow, delicate links, close-up, without text"),
   "2": ("m", "landing", "the back of her hand raised to her mouth in a loud haughty laugh, head tilted back, faint sound ripples in the air, one stockinged leg stepping forward"),
   "3": (None, "black", "a small black incense burner on a low table, thin sweet pink smoke curling upward, black curtains behind, close-up, without text"),
   "4": ("m", "anteroom", "stretching a sheer silk stocking between both gloved hands in front of her, the silk shimmering, inviting smile"),
   "5": (None, "footrest", "a soft carpet between two facing sofas, one purple and one green, a faint body-shaped hollow in the carpet, a purple door and a green door behind, quiet warm light"),
 },
}
