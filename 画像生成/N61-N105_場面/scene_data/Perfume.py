# N79 夜香の調香室（Perfume）画像データ。登場人物は全員20歳以上。女性＋ニューハーフ（NH＝ムスク・アンブル）。女装あり。
# 敗北28本はすべて主人公が「香りの服」（白いブラウス・薄紫のロングスカート・サテンのリボン）のまま。香水瓶のラベル・帳面は文字なし。香りは pink perfume mist で見せる。
BL = ("a white blouse with thin frills at the chest, a long lavender skirt, a lavender satin ribbon at the neck, "
      "a small perfume bottle charm on his wrist, thin white socks")
BL_OPEN = BL + ", the blouse unbuttoned showing his flat chest"
BL_UP = BL + ", the skirt hem lifted"
BL_BOTH = BL + ", the blouse unbuttoned showing his flat chest, the skirt hem lifted"
O = {"hero_outfit": BL}
OO = {"hero_outfit": BL_OPEN}
OU = {"hero_outfit": BL_UP}
OB = {"hero_outfit": BL_BOTH}
NHP = {"pen": "penis", "hero_outfit": BL_BOTH}   # ムスク・アンブルの逆アナル（指でほぐした後だけ）

DATA = {
 "code": "Perfume",
 "world": "hidden perfumery on a perfume street in a fantasy town at night, glass perfume bottles, pale purple light, drifting pink perfume mist, detailed background",
 "bg": "perfumery room at night, a wall of shelves with colorful glass perfume bottles without labels, pale purple lamplight, a low leather testing chair, faint pink mist",
 "josou": "white blouse with thin frills at the chest, long lavender skirt, lavender satin ribbon at the neck, small perfume bottle charm on the wrist, thin white socks, no wig",
 "chars": {
   "m": {"type": "woman", "jp": "ミュスカ",
         "tags": "adult woman, mature female, mature face, 34 years old, adult proportions, beautiful detailed eyes, tall, long legs, crimson hair, long wavy hair, green eyes, black slit dress, white perfumer's coat draped over her shoulders, perfume bottle pendant, languid sensual smile, large breasts",
         "name": "the crimson-haired perfumer in a black slit dress",
         "pose": "holding a glass perfume atomizer near her lips, languid half-lidded eyes, looking at viewer"},
   "e1": {"type": "woman", "jp": "ベルガ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, bob cut, green eyes, short white lab-style jacket, bundle of white perfume test strips, curious bright smile, medium breasts",
          "name": "the pink-bobbed scent tester in a short white jacket",
          "pose": "holding up a fan of white perfume test strips, curious bright smile, looking at viewer"},
   "e2": {"type": "nh", "jp": "ムスク",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, dark brown hair, long wavy hair, amber eyes, black shirt dress, leather apron, belt lined with small perfume bottles, sultry smile, large breasts",
          "name": "the dark-brown-haired perfume assistant in a leather apron",
          "pose": "dabbing a drop of perfume behind her own ear, sultry smile, looking at viewer"},
   "e3": {"type": "woman", "jp": "イランイラン",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, black hair, twin braids, brown eyes, yellow floral apron dress, tape measure around her neck, pins on her sleeve, gentle smile, large breasts",
          "name": "the black-braided dresser in a yellow floral apron dress",
          "pose": "holding up a white frilled blouse on a hanger, gentle smile, looking at viewer"},
   "boss": {"type": "nh", "jp": "アンブル",
            "tags": "adult woman, mature female, mature face, 38 years old, adult proportions, beautiful detailed eyes, very tall, elegant, feminine body, long legs, amber hair, long curly hair, gold eyes, amber satin long dress, black fur cape, calm enveloping smile, large breasts",
            "name": "the amber-haired mistress of scent in an amber satin dress",
            "pose": "holding a small bottle of amber oil to her lips, calm enveloping smile, looking at viewer"},
 },
 "places": {
   "lab": "perfumery room, a wall of shelves of colorful glass perfume bottles without labels, pale purple light, drifting pink perfume mist",
   "chair": "perfume testing seat, low leather chair with cold armrests, bundle of white test strips, a mirror in front, pink mist",
   "street": "perfume street at night, cobblestones, gas lamps, sweet scent drifting from shop fronts",
   "shop": "perfume shop front after closing, glass display shelves of bottles without labels, a door with a bell, tall mirror",
   "still": "distillation room, copper alembic still, steam, simmering petals, dripping essential oil",
   "store": "spice and resin storehouse, barrels and burlap sacks, dried resin and fragrant wood, cool darkness",
   "attic": "attic drying room, bundles of dried flowers hanging from the beams, moonlight through a skylight",
   "dressing": "dressing room, tall full-length mirror, dress form, piles of fabric, a box of pins",
   "musk": "small musk room, black curtains, low chaise longue, warm dim light",
   "bath": "perfumed oil bath, steam, marble bath edge glossy with oil, mirror",
   "greenhouse": "herb greenhouse at night, night-blooming flowers, damp soil, moonlight through glass",
   "amber": "amber room, amber-colored lamplight, black fur rug, resin incense smoke",
   "bedroom": "luxurious bedroom, canopy bed with silk sheets, incense burner by the pillow",
   "inner": "small inner room of the perfumery, a single testing chair, closed door, dim light, thick pink mist",
 },
 "atk": {
   "m1": ("chair", "he sits on the low testing chair, the perfumer stands over him hugging his face deep into her cleavage, breast smother, a puff of pink perfume mist from the atomizer in her hand, trembling"),
   "m2": ("lab", "he sits on a stool before the bottle shelves, the perfumer holds his chin and blows a sweet pink breath onto his nose, pink mist, no hands below, dazed, breathing in"),
   "m3": ("chair", "he sits on the testing chair, the perfumer hugs his head under her raised arm pressing his face to her armpit, her other hand stroking his penis, handjob, pink mist", OU),
   "e1": ("chair", "he sits on the testing chair with his blouse unbuttoned, the scent tester traces circles around his nipple with the tip of a white test strip, pink mist rising, curious smile", OO),
   "e2": ("musk", "he sits on the low chaise longue, the perfume assistant dabs a drop of perfume behind his ear and licks it off, tongue in his ear, flushed, trembling", O),
   "e3": ("dressing", "he stands before the tall mirror, the dresser hugs him from behind buttoning the white blouse onto him, her hands stroking his chest over the fabric, flushed", O),
   "boss": ("amber", "he sits on the black fur rug, the mistress of scent kisses him deeply, tongues, passing amber oil, her fingers pinching his nipple through the open blouse", OO),
 },
 "atk_desc": {
   "m1": "the perfumer buries his face in her perfumed cleavage.",
   "m2": "the perfumer blows her blended aphrodisiac breath onto his nose.",
   "m3": "the perfumer makes him smell her armpit while stroking him.",
   "e1": "the scent tester traces his nipples with a perfumed test strip.",
   "e2": "the perfume assistant licks a drop from behind his ear.",
   "e3": "the dresser hugs him as she dresses him in scented clothes.",
   "boss": "the mistress of scent gives him an amber kiss.",
 },
 "lose": {
   # ミュスカ 技1（谷間の香り）
   "btl_m1": ("chair", "he sits collapsed on the testing chair, the perfumer stands over him pressing his face into her cleavage, breast smother, cheeks squeezed between her breasts, pink mist, cum soaking the lavender skirt", OU),
   "onani_m1": ("bedroom", "lying alone on the canopy bed with his face buried in a perfumed cloth, breathing deeply, hands away from his body, penis untouched, the perfumer watches far away at the opened door", O),
   "inochi_m1": ("street", "he kneels on the cobblestones in the dark beside a gas lamp, the perfumer bends down hugging his face into her cleavage, breast smother, a drop of perfume on her chest, pink mist, trembling", O),
   "onedari_m1": ("lab", "he kneels before the bottle shelves, the perfumer holds his face deep in her cleavage and blows breath onto his nose as he lifts his face, pink mist, a bottle without a label in his hand, cum dripping", OU),
   # ミュスカ 技2（★調合した吐息）
   "btl_m2": ("lab", "he sits before the bottle shelves with his chin lifted, the perfumer blows a sweet pink breath onto his nose, pink mist, no hands on him, dazed, cum soaking the lavender skirt", OU),
   "onani_m2": ("chair", "sitting alone on the testing chair, holding his own wrist to his nose and breathing in deeply, a perfumed cloth in his lap, hands away from his crotch, penis untouched, the perfumer watches far away", O),
   "inochi_m2": ("still", "he sits beside the copper alembic in the steam, the perfumer blows a pink breath along his neck and chest, oil dripping from the still, no hands on him, dazed, cum dripping", OO),
   "onedari_m2": ("attic", "he kneels under hanging dried flowers holding up a bottle without a label, the perfumer holds his chin and blows a sweet pink breath into his open mouth, pink mist, moonlight", O),
   # ミュスカ 技3（脇の香り）
   "btl_m3": ("chair", "he sits on the testing chair, the perfumer hugs his head under her raised arm with his face to her armpit, her other hand stroking his penis under the lifted skirt, handjob, pink mist, cum dripping", OU),
   "onani_m3": ("dressing", "sitting alone before the mirror, hugging his own head with one arm, a perfumed cloth held under his own armpit to his nose, penis untouched, the perfumer watches far away beside the dress form", O),
   "inochi_m3": ("store", "he stands in the dark among barrels, the perfumer hugs his head under her raised arm with his face to her armpit, breathing onto his hair, pink mist, trembling", O),
   "onedari_m3": ("bedroom", "he lies on the canopy bed, the perfumer lies beside him hugging his head under her arm with his face to her armpit, her other hand stroking his penis, handjob, cum on the silk", OU),
   # ベルガ（★試香紙の先）
   "btl_e1": ("chair", "he sits on the testing chair with his blouse unbuttoned, the scent tester traces his nipple with the tip of a white test strip, his penis clamped between her perfumed thighs, thighjob, pink mist, cum dripping", OB),
   "onani_e1": ("shop", "sitting alone behind the glass display shelves, tracing his own nipple with the tip of a white test strip, the blouse opened, penis untouched, the scent tester watches far away from the door", OO),
   "inochi_e1": ("greenhouse", "he sits among night flowers, the scent tester rubs the tip of a test strip over his nipple through the blouse fabric, pink mist, trembling, flushed", O),
   "onedari_e1": ("lab", "he sits on a stool with his blouse unbuttoned, the scent tester traces his left and right nipples in turn with a perfumed test strip, a bottle without a label beside, pink mist, cum on the skirt", OO),
   # ムスク（★耳の後ろの一滴／麝香の奥・NH）
   "btl_e2": ("musk", "from side, he lies on his back on the low chaise longue with legs lifted, the perfume assistant penetrates his anus with her own penis, anal, licking behind his ear, his own penis separate, pink mist", NHP),
   "onani_e2": ("store", "sitting alone on a burlap sack, a drop of perfume behind his ear, tracing the rim of his own ear with that finger, penis untouched, the perfume assistant watches far away between the barrels", O),
   "inochi_e2": ("bath", "from side, he lies on his back on the oily marble bath edge, the perfume assistant penetrates his anus with her own penis, anal, dropping perfume behind his ear, his own penis separate, steam", NHP),
   "onedari_e2": ("street", "he leans against a wall in the dark perfume street, the perfume assistant dabs perfume behind his ear and licks his ear, whispering, a bottle without a label in his hand, trembling", O),
   # イランイラン（★香りの着付け）
   "btl_e3": ("dressing", "he stands before the tall mirror in the white blouse and lavender skirt, the dresser hugs him tightly from behind, rubbing her hips against his bottom through the skirt, cum stain on the skirt", O),
   "onani_e3": ("chair", "sitting alone on the testing chair in the white blouse, hugging himself and stroking his own chest over the fabric, penis untouched, the dresser watches far away holding a sleeve", O),
   "inochi_e3": ("attic", "he stands under the hanging dried flowers, the dresser hugs him from behind tying the lavender satin ribbon at his neck, flushed, trembling, moonlight", O),
   "onedari_e3": ("shop", "he stands before the tall mirror of the shop front, the dresser hugs him from behind smoothing the white blouse on him, pink perfume mist, his knees trembling, cum stain on the skirt", O),
   # アンブル（★琥珀の口づけ／最後の香り・NH）
   "btl_boss": ("amber", "from side, he lies on his back on the black fur rug with legs lifted, the mistress of scent penetrates his anus with her own penis, anal, kissing him deeply, pinching his nipple, his own penis separate", NHP),
   "onani_boss": ("inner", "sitting alone on the testing chair, a perfumed cloth at his mouth, sucking his own fingers, the other hand pinching his own nipple through the open blouse, penis untouched, the mistress of scent watches far away at the door", OO),
   "inochi_boss": ("bedroom", "from side, he lies on his back on the silk sheets, the mistress of scent penetrates his anus with her own penis, anal, kissing him deeply passing amber oil, his own penis separate, incense", NHP),
   "onedari_boss": ("still", "he sits beside the copper alembic holding a bottle of amber oil, the mistress of scent kisses him deeply, amber oil glossy on his lips, pinching his nipple, steam, cum on the skirt", OO),
 },
 "lose_desc": "keeps him in the perfumery as a testing seat, dressed in scented clothes forever.",
 "onanie": {
   "master": ("chair", "holding a perfumed cloth over his nose and mouth, breathing in and out deeply, hands away from his body, dazed, penis untouched"),
   "e1": ("chair", "tracing his own nipple in small circles with the tip of a perfumed white test strip, penis untouched"),
   "e2": ("musk", "a drop of perfume behind his ear, slowly tracing the rim of his own ear with that finger, penis untouched"),
   "e3": ("dressing", "wearing the scented white blouse, hugging himself and stroking his own chest over the fabric, penis untouched", O),
   "boss": ("inner", "a perfumed cloth at his mouth, sucking his own fingers, the other hand pinching his own nipple, penis untouched"),
 },
 "magic": {
   "1": ("m", "lab", "spraying pink perfume mist from a small glass atomizer, languid smile"),
   "2": (None, "lab", "a perfume formula paper without text on a desk beside small glass bottles without labels and a dropper"),
   "3": (None, "street", "a lingering pink perfume mist drifting over the empty cobblestones under a gas lamp"),
   "4": (None, "dressing", "a white frilled blouse and a long lavender skirt on a dress form, a lavender satin ribbon, pink perfume mist"),
   "5": (None, "bedroom", "an ornate incense burner by the pillow releasing sweet pink smoke"),
 },
}
