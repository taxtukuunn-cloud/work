# N142 淫界の王座（Daydream）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作に青・水色の髪や瞳のキャラはいない（瞳はこのMOD用に青系を避けて決めた）。
# イリアスは他MODの同名の女神とは別人として、波打つ金髪の片側三つ編み・金の瞳・光の冠にした。
# 後ろに入れるのはティラミスの指だけ（pen なし）。ティラミスの「本番」は彼女が上に跨って迎える形（主人公は仰向けで動かない。女性は着衣のまま、ドレスの裾で隠す）。
# 胸で挟む場面も女性は着衣のまま（胸元の谷間で挟む）。責めはすべて痛みなし。主人公の胸には桃色に光る淫紋。
MARK = "a glowing pink crest mark on his chest"
CARDS = "blank playing cards without text"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
RIDE = "her long dress skirt spread over his hips hiding where they join"
RIDE_NEG = "man on top, he thrusts, he holds her hips"
DATA = {
 "code": "Daydream",
 "world": "fantasy town taken over by succubi and the pink-hazed succubus realm beyond it, sweet pink mist in the air, soft glowing light, detailed background",
 "bg": "throne room of the succubus realm, thick pink haze in the air, a black and pink throne on a dais, a round card table with two chairs before it, a large canopy bed in the back, black pillars, pink lamps, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ティラミス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, very long dark brown hair, black curved horns, magenta eyes, black and pink queen dress with a deep neckline, long skirt, black tiara, large black bat wings, black succubus tail with a heart-shaped tip, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the dark-brown-haired succubus queen with black wings",
         "pose": "one hand on her hip, the other hand holding a fan of blank playing cards without text, black wings half spread, cheerful playful laugh, looking at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "マカロン",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, fluffy pink hair, long wavy hair, short black horns, pink eyes, frilled pink dress with an open neckline, pink ribbon, thin pink succubus tail, pink mist drifting around her, soft curvy feminine body, huge breasts",
          "name": "the fluffy-pink-haired succubus in a pink dress",
          "pose": "one finger at her lips, the other hand casting a pink magic circle, sweet lazy smile, pink mist around her, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "女神",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, very long straight silver hair, violet eyes, black goddess robe with silver trim, black feathered wings, glossy fair skin, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the silver-haired fallen goddess in a black robe",
          "pose": "both arms open as if inviting an embrace, calm composed smile, black feathered wings folded, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ディーラー",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, black hair, hair bun, short black horns, amber eyes, droopy eyes, black dealer vest, white shirt, red bow tie, black pencil skirt, black thin succubus tail, soft curvy feminine body, large breasts",
          "name": "the black-bun succubus dealer in a black vest",
          "pose": "fanning out blank playing cards without text in one hand, the other hand at her cheek, relaxed sleepy smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "イリアス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 32 years old, adult proportions, beautiful detailed eyes, tall, long legs, long wavy blonde hair, single side braid, golden eyes, haughty eyes, white and gold goddess robe, crown of light floating above her head, large white feathered wings, soft voluptuous feminine body, huge breasts",
            "name": "the blonde goddess with white wings and a crown of light",
            "pose": "chin raised, one hand on her chest, the other hand raised with soft white light in her palm, proud haughty smile, looking down at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "inn":      "inn bedroom in the town, soft white sheets, thick futon blanket, bedside lamp, sweet pink haze",
   "base":     "plain rented room at night, a wooden desk with a lamp, a simple bed, a window with a curtain",
   "hospital": "town hospital room, white curtains, clean bed, quiet corridor beyond the door",
   "entrance": "casino entrance hall, crystal chandelier, red carpet, casino chips on a counter, large doors",
   "poker":    "casino poker room, green felt card table, chips, champagne glasses, warm low lamps",
   "resto":    "casino restaurant, white tablecloths, sweets and wine, a secluded booth seat in the back",
   "chapel":   "church nave, stained glass windows, incense smoke, wooden pews, an altar",
   "confess":  "confession booth, wooden lattice window, velvet kneeler, dim candle light",
   "door":     "glowing door at the back of the church, white light spilling over the threshold, stone steps",
   "hall":     "castle hall, red carpet, pink haze, a long table full of sweets and cakes",
   "castle":   "castle throne room, an ornate pink throne, sweet pink mist, heaps of pink cushions, a canopy bed in the back",
   "garden":   "sky garden of heaven, white light, clouds, flowers, white garden chairs",
   "heaven":   "goddess hall of heaven, white throne, pillars of light, smooth white stone floor",
   "gate":     "gate of the succubus realm, tall black gate, thick pink haze, a soft bed nook just inside the gate",
   "throne":   "throne room of the succubus realm, black and pink throne, a round card table, a large canopy bed, thick pink haze",
 },
 "atk": {
   "m1": ("throne", "he sits at the card table with his shirt open, the queen leans across the table tracing " + MARK + " with one fingertip, her other hand holding " + CARDS + ", laughing, his jacket dropped on the floor, he trembles"),
   "m2": ("throne", "from side, he lies on his back on the canopy bed, the queen straddles his hips sitting on him, " + RIDE + ", her hands rolling his nipples, black wings spread, " + MARK + ", he lies still", {"neg": RIDE_NEG}),
   "m3": ("throne", "he sits on the throne wrapped inside her black wings, the queen kisses him deeply, tongues, saliva trail, one of her hands behind him with two wet fingers in his anus, fingering, " + MARK + ", his hands limp"),
   "e1": ("castle", "he lies on pink cushions, the pink-haired succubus kneels between his legs, his penis squeezed in the deep cleavage of her dress, paizuri, blowing pink mist toward his face, sweet lazy smile, " + MARK + ", dazed"),
   "e2": ("chapel", "he sits on a pew, the fallen goddess kneels before him hugging his waist, his penis squeezed in the deep cleavage of her black robe, paizuri, looking up with a calm smile, he nods, " + MARK),
   "e3": ("poker", "he sits on a chair at the green felt table with his shirt open, the dealer sits sideways on his lap, one fingertip stroking his nipple, her other hand stroking his penis lightly with a dealing motion, handjob, " + CARDS + " on the table, " + MARK),
   "boss": ("heaven", "he sits on the white floor in a pillar of light, the goddess kneels before him, his penis squeezed in the deep cleavage of her robe, paizuri, soft white light from her palm shining on his nipples, haughty smile, " + MARK),
 },
 "atk_desc": {
   "m1": "the queen makes losing at cards fun, tracing his crest every time he loses.",
   "m2": "the queen gets serious, wrapping him in her soft body and taking him in while he lies still.",
   "m3": "the queen seals his lips inside her black wings while her fingers press inside him.",
   "e1": "the pink succubus makes him dizzy with sweet pink mist and squeezes him between her breasts.",
   "e2": "the fallen goddess invites him to become her believer, squeezing tighter each time he nods.",
   "e3": "the dealer deals touches like cards, alternating between his nipples and his penis.",
   "boss": "the goddess makes his skin sensitive with heavenly light and squeezes him between her breasts at her own pace.",
 },
 "lose": {
   # ティラミス 技1（女王の気まぐれ）
   "btl_m1":     ("throne", "from side, he lies on his back on the card table among scattered " + CARDS + ", the queen straddles his hips sitting on him, " + RIDE + ", holding one card up between two fingers, laughing, " + MARK + ", cum", {"neg": RIDE_NEG}),
   "onani_m1":   ("base", "sitting alone at the desk with his shirt open, turning over " + CARDS + " with one hand, the other hand stroking his own nipple, " + MARK + ", penis untouched, the queen watches far away from the doorway"),
   "inochi_m1":  ("gate", "he sits on the bed nook inside the black gate holding a few " + CARDS + ", the queen embraces him from behind, her arms and black wings around him, one hand on his nipple, whispering in his ear, " + MARK + ", cum dripping"),
   "onedari_m1": ("throne", "he sits on a chair beside the throne, the queen sits on his lap facing him, pressing her body to his, one hand tracing " + MARK + ", " + CARDS + " scattered on the side table, laughing, cum dripping"),
   # ティラミス 技2（★女王の本気）
   "btl_m2":     ("throne", "from side, he lies on his back on the canopy bed, the queen straddles his hips sitting on him, " + RIDE + ", leaning down with her arms and black wings wrapped around him, a black feather on the sheet, " + MARK + ", cum", {"neg": RIDE_NEG}),
   "onani_m2":   ("inn", "lying alone wrapped in the thick futon blanket, one hand stroking his own nipple, the other hand reaching behind to stroke his own anus, " + MARK + " glowing through the blanket, penis untouched, the queen watches far away by the door"),
   "inochi_m2":  ("castle", "he lies on his side on the canopy bed, the queen lies behind him holding him in her arms and thighs, one hand on his nipple, two wet fingers of her other hand in his anus, fingering, morning light, " + MARK + ", cum on the sheet"),
   "onedari_m2": ("throne", "he lies on his back on the canopy bed with his knees up, the queen lies over him covering him with her body, two wet fingers in his anus, fingering, her tail tip dripping honey, licking his nipple, " + MARK + ", cum on his stomach"),
   # ティラミス 技3（女王の口づけ）
   "btl_m3":     ("throne", "from side, he sits on the queen's lap on the throne, wrapped inside her black wings, the queen kisses him deeply, tongues, saliva trail, two wet fingers in his anus, fingering, a pink crest-shaped pendant on his neck, cum dripping"),
   "onani_m3":   ("gate", "kneeling alone in the shadow of the black gate, sucking two of his own fingers as if kissing, the other hand reaching behind pressing a finger into his own anus, " + MARK + ", penis untouched, the queen watches far away inside the gate"),
   "inochi_m3":  ("throne", "he stands before the closed black doors, the queen holds his face in both hands kissing him deeply, tongues, her black wings closing around him, her tail curled around his thigh, " + MARK + ", his knees giving way"),
   "onedari_m3": ("throne", "he lies on half of the canopy bed, the queen lies beside him with one black wing covering him, kissing him deeply, tongues, saliva, two wet fingers deep in his anus, fingering, " + MARK + ", cum on his stomach"),
   # マカロン（★桃色の淫気）
   "btl_e1":     ("castle", "he lies on pink cushions before the pink throne, the pink-haired succubus kneels between his legs, his penis squeezed in the deep cleavage of her dress, paizuri, blowing pink mist over him, a pink ribbon tied on his wrist, " + MARK + ", cum on her cleavage"),
   "onani_e1":   ("hall", "crouching alone behind the table of sweets, holding a pastry to his nose and sniffing it, the other hand stroking his own nipple, " + MARK + ", penis untouched, the pink-haired succubus watches far away across the hall"),
   "inochi_e1":  ("castle", "he sits on the pink throne dazed, the pink-haired succubus leans over him hugging his head to her chest, pinching and rolling his nipple, breathing pink mist on his face, " + MARK + ", cum dripping untouched"),
   "onedari_e1": ("castle", "he lies on a heap of pink cushions, the pink-haired succubus lies on him hugging him, his penis squeezed in the deep cleavage of her dress, paizuri, he breathes in thick pink mist, " + MARK + ", cum on her cleavage"),
   # 女神（★信徒への勧誘）
   "btl_e2":     ("chapel", "he sits on a pew under the stained glass, the fallen goddess kneels before him hugging his waist, his penis squeezed in the deep cleavage of her black robe, paizuri, he nods, a strip of black cloth tied on his wrist, " + MARK + ", cum on her cleavage"),
   "onani_e2":   ("confess", "kneeling alone on the velvet kneeler, hugging a pillow to his chest, lips moving in a murmur, one hand inside his shirt stroking his own nipple, " + MARK + ", penis untouched, the fallen goddess watches far away through the lattice window"),
   "inochi_e2":  ("chapel", "he kneels before the altar with his hands clasped in prayer, the fallen goddess embraces him from behind, her glossy arms around his chest, one hand stroking his nipple, her black wings around them, " + MARK + ", cum dripping untouched"),
   "onedari_e2": ("chapel", "he lies on the front pew, the fallen goddess lies over his legs hugging his hips, his penis squeezed in the deep cleavage of her black robe, paizuri, calm smile, he raises one hand as if swearing an oath, " + MARK + ", cum"),
   # ディーラー（★ディーラーの手）
   "btl_e3":     ("poker", "he sits at the green felt table with his shirt open, the dealer sits sideways on his lap, both her hands working at once, one rolling his nipple, one stroking his penis, handjob, " + CARDS + " on the table, a red bow tie around his neck, " + MARK + ", cum"),
   "onani_e3":   ("resto", "sitting alone in the back booth with his shirt open, stroking his own right nipple then left with a card-dealing motion, " + MARK + ", penis untouched, the dealer watches far away between the tables"),
   "inochi_e3":  ("entrance", "he sits on a bench under the chandelier, the dealer sits on his lap hugging him, shuffling " + CARDS + " beside his ear, her fingertip circling his nipple, relaxed smile, " + MARK + ", cum dripping untouched"),
   "onedari_e3": ("poker", "he sits in the best chair of the poker room with his chest pushed out, the dealer leans over the table laying a blank card on his nipple with two fingers, her other fingertip stroking his other nipple, five " + CARDS + ", " + MARK + ", cum dripping untouched"),
   # イリアス（★天界の光と胸）
   "btl_boss":   ("heaven", "he sits on the white floor in a pillar of light, the goddess kneels before him, his penis squeezed in the deep cleavage of her robe, paizuri, haughty smile, a shard of glowing light on a cord around his neck, " + MARK + ", cum on her cleavage"),
   "onani_boss": ("garden", "sitting alone behind a white garden chair with his shirt open, a ray of light through the clouds falling on his chest, stroking his own nipple, " + MARK + ", penis untouched, the goddess watches far away among the flowers"),
   "inochi_boss":("door", "he sits on the stone steps before the glowing door, the goddess sits beside him talking with one finger raised, soft white light from her other palm shining on his nipples, " + MARK + ", he trembles, cum dripping untouched"),
   "onedari_boss":("heaven", "he kneels at the foot of the white throne with his chest pushed out, the goddess sits on the throne looking down, a beam of white light from her fingertip shining on his nipple, proud smile, " + MARK + ", cum dripping untouched"),
 },
 "lose_desc": "keeps him in the succubus realm forever as the queen's cherished card partner, a pink crest of twelve strokes glowing on his chest.",
 "onanie": {
   "master": ("inn", "lying wrapped in a blanket, one hand stroking his own nipple, the other hand reaching behind to stroke his own anus, " + MARK + ", penis untouched"),
   "e1": ("hall", "crouching behind a table of sweets, sniffing a pastry, the other hand stroking his own nipple, " + MARK + ", penis untouched"),
   "e2": ("confess", "kneeling, hugging a pillow, murmuring, one hand stroking his own nipple, " + MARK + ", penis untouched"),
   "e3": ("resto", "sitting in a booth, stroking his own nipples left and right with a card-dealing motion, " + MARK + ", penis untouched"),
   "boss": ("garden", "sitting with his shirt open, a ray of light on his chest, stroking his own nipple, " + MARK + ", penis untouched"),
 },
 "magic": {
   "1": (None, "throne", "a glowing pink crest emblem made of curved strokes floating in the air above a round card table, one stroke shining brighter, soft pink sparkles, emblem without text, close-up"),
   "2": ("m", "throne", "sitting on the black and pink throne with her legs crossed, head tilted back laughing cheerfully, one hand at her mouth, black wings spread"),
   "3": ("e1", "castle", "blowing a cloud of sweet pink mist from her palm, the mist swirling and filling the room, sweet lazy smile"),
   "4": (None, "poker", "a tall slender glass of pale pink sparkling champagne on the green felt table, fine bubbles, an unlabeled bottle without text in an ice bucket, warm lamp light, close-up"),
   "5": (None, "gate", "a tall black gate standing half open, thick pink haze flowing out through the gap, soft pink glow from inside, quiet and inviting"),
 },
}
