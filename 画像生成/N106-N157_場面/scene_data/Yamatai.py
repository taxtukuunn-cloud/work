# N109 ヤマタイの妖（Yamatai）画像データ。登場人物は全員20歳以上（責め手は数百年生きている妖の成人女性）。女性のみ（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない。
# 原作で青／水色の部分：雪女の髪・瞳は青みのある銀 → lavender-silver hair／silver-grey eyes に置き換え。氷の座敷の「青い光」は pale white cold light と書く。
# オロチ：八つの首は構図が難しいので、絵は「本体の首ひとつ（黒髪の女の上半身＋灰と緑の蛇の胴）」を主にし、同じ胴から伸びる首を2本だけ添える（合わせて3本まで。別人ではなく同じ体の首）。
# 挿入はオロチの尾の先・皇女の糸の紐だけ（どちらも体の一部／糸なので pen なし）。雪女・くのいちは指まで、濡れ女は入れない。
# 札・符は文字なし（朱の丸い印だけ）。影縫いの針は床や壁の影に打つ（体には刺さらない）。糸は食い込まない。痛み・傷の絵は書かない。
TAG = "a blank white wooden tag with round red seal marks and no text hanging from his neck"
NECKS = "two more of her long serpent necks with identical black-haired heads rising from the same coiled body"
TAIL = "the slim smooth tip of her snake tail in his anus"
CORDIN = "a slim white silk cord of twisted thread in his anus"
KIMONO = "his plain white men's kimono opened at the front"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs, horror"
NEEDLE_NEG = "needle piercing skin, stabbed, wound"
WEB_NEG = "insect face, hairy spider legs, thread cutting into skin, rope marks"
DATA = {
 "code": "Yamatai",
 "world": "hidden japanese mountain village and its deep damp cave, wet rocks and moss, rows of paper lanterns, vermilion torii, incense haze, old japanese folklore mood, detailed background",
 "bg": "inside a deep damp cave, wet rocks and moss, a row of glowing paper lanterns, a moss-covered vermilion torii gate, a still pool of sake glimmering in the back, strings of small bells hanging, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "ヤマタノオロチ",
         "tags": "adult woman, mature female, mature face, sharp adult features, 32 years old, adult proportions, beautiful detailed eyes, tall, black hair, very long hair, horn-shaped hair ornaments, golden eyes, slit pupils, black and red kimono off her shoulders, lamia, giant grey and green snake lower body, long coiled snake tail, soft voluptuous feminine body, huge breasts",
         "name": "the black-haired serpent goddess with a grey and green snake body",
         "pose": "rising tall on her coiled snake body, holding a vermilion sake cup in one hand, bold hearty grin, looking down at viewer",
         "height_note": "she is much taller than him",
         "neg_remove": ["twins", "same face"],
         "neg": SOFT_NEG + ", legs on the lamia, snake head, monster face"},
   "e1": {"type": "woman", "jp": "雪女",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, lavender-silver hair, very long straight hair, silver-grey eyes, very pale white skin, white kimono, white obi, faint frost on her sleeves, slender curvy feminine body, large breasts, yuki-onna",
          "name": "the silver-haired snow woman in a white kimono",
          "pose": "one pale hand raised with cold white mist drifting from her fingertips, quiet faint smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "くのいちエルフ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, blonde hair, high ponytail, green eyes, pointy ears, elf, long red scarf, dark grey sleeveless ninja outfit, fishnet undershirt, black tabi socks, slender curvy feminine body, large breasts, kunoichi",
          "name": "the blonde elf kunoichi with a red scarf",
          "pose": "one hand on her hip, the other hand holding a thin needle between two fingers, confident breezy grin, looking at viewer",
          "neg": SOFT_NEG + ", " + NEEDLE_NEG},
   "e3": {"type": "woman", "jp": "濡れ女",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, dark green hair, extremely long wet hair spreading and curling like snakes, black hair tips, amber eyes, wet skin, purple kimono, lamia, white snake lower body, white snake tail, soft curvy feminine body, large breasts",
          "name": "the green-haired wet woman in a purple kimono",
          "pose": "rising from dark water on her white snake body, wet hair spreading around her, one sleeve at her lips, moist alluring smile, looking at viewer",
          "neg": SOFT_NEG + ", legs on the lamia, snake head"},
   "boss": {"type": "woman", "jp": "蜘蛛之皇女",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, deep purple hair, very long hair, ornate gold hair ornaments, red eyes, a third eye on her forehead, white and black layered kimono, arachne, black spider lower body, sleek black spider legs, white silk threads between her fingers, soft curvy feminine body, large breasts",
            "name": "the purple-haired spider princess in a white and black kimono",
            "pose": "standing high on her black spider legs, holding a blank paper talisman without text between two fingers, haughty cold smile, looking down at viewer",
            "height_note": "she is much taller than him",
            "neg": SOFT_NEG + ", " + WEB_NEG},
 },
 "places": {
   "entrance": "cave entrance, cold wind, a moss-covered vermilion torii gate, dripping water, daylight outside",
   "passage":  "wet rock passage in the cave, puddles on the floor, slick glistening rocks, a single paper lantern",
   "lake":     "underground lakeside, black still water reflecting paper lanterns, a flat wet rock at the shore, cool air",
   "hidden":   "narrow hidden side tunnel, rope ladder, wooden trap boards, a small candle",
   "ninja":    "ninja guard room, tatami mats, shuriken target on the wall, candles, long shadows on the floor",
   "snow":     "snow cave, snow blowing in through an opening, icicles, white fur spread on the ground, white breath",
   "ice":      "ice parlor, folding screen made of ice, cold tatami mats, pale white cold light",
   "gate":     "village gate, vermilion lacquered gate, a row of paper lanterns, night",
   "hearth":   "old farmhouse room with a sunken hearth, glowing embers, a pot hanging over the fire, sooty beams",
   "shrine":   "old lonely wooden shrine, glittering spider webs, blank paper talismans without text on the pillars",
   "silk":     "thread chamber, white silk threads stretched all over from the ceiling, soft white glow",
   "festival": "festival square at night, wooden festival tower, many paper lanterns, sake barrels",
   "brewery":  "sake storehouse, rows of large wooden sake barrels, warm dim air, a wooden ladle",
   "litter":   "inside a swaying wooden palanquin, white hanging curtains, lantern light through the cloth",
   "den":      "vast rock cavern of the serpent goddess, a glowing pool of sake, wide smooth stone floor, strings of small bells along the walls",
 },
 "atk": {
   "m1": ("den", "he sits slumped beside the pool of sake, the serpent goddess bends down holding his chin, feeding him sacred sake mouth to mouth, kiss, sake dripping from his lips, a vermilion sake cup in her hand, her coils around his waist, flushed dizzy face, " + TAG),
   "m2": ("den", "he lies on his back on her coils with his shirt open, the serpent goddess sucks his nipple, " + NECKS + " licking his ear and his other nipple, " + TAIL + ", his penis untouched, " + TAG),
   "m3": ("den", "from side, he is held up in her coils, the serpent goddess kisses him deeply, tongues, saliva trail, one more of her long serpent necks with an identical black-haired head sucking his nipple, " + TAIL + ", his penis untouched, " + TAG),
   "e1": ("ice", "he lies on the cold tatami in the snow woman's arms, the snow woman pinches his nipple with pale cold fingers, two fingers of her other hand in his anus, fingering, cold white mist, his skin flushed warm where she touches, " + TAG),
   "e2": ("ninja", "he stands frozen with thin needles pinned into his shadow on the tatami, the kunoichi sits on a low table in front, one tabi-socked foot rubbing his chest, toes pinching his nipple, her other sole pressing his lower belly, grin, " + TAG, {"neg": NEEDLE_NEG}),
   "e3": ("lake", "he stands knee-deep at the shore, the wet woman's long wet dark hair coiled around his wrists, ankles and chest, slick hair tips stroking his nipples, her white snake tail around his waist pulling him toward the water, " + TAG),
   "boss": ("silk", "he hangs spread in the air held by soft white silk threads on his wrists and ankles, the spider princess below him looking up with her third eye, " + CORDIN + ", her finger plucking a taut thread, a blank paper talisman on his chest, " + TAG),
 },
 "atk_desc": {
   "m1": "the serpent goddess makes him drunk with sacred sake fed mouth to mouth.",
   "m2": "the serpent goddess licks and sucks him in many places at once while her tail tip strokes him inside.",
   "m3": "the serpent goddess seals his lips with endless kisses while another head sucks his nipple.",
   "e1": "the snow woman chills his nipple and presses inside with her cold fingers.",
   "e2": "the kunoichi pins his shadow and teases him with her feet.",
   "e3": "the wet woman binds him with her wet hair and strokes his nipples with its tips.",
   "boss": "the spider princess hangs him in a bed of threads and makes a silk cord tremble inside him.",
 },
 "lose": {
   # オロチ 技1（御神酒の酔い）
   "btl_m1":     ("den", "he kneels beside the pool of sake, " + KIMONO + " by his own hands, the serpent goddess holds his chin feeding him sake mouth to mouth, kiss, one more of her long serpent necks with an identical black-haired head sucking his nipple, a vermilion sake cup, cum dripping untouched, " + TAG),
   "onani_m1":   ("festival", "sitting alone in the shadow of the festival tower, a sake cup beside him, his kimono front opened, one hand stroking his own chest, the other hand reaching behind to stroke his own anus, penis untouched, the serpent goddess watches far above from the tower, " + TAG),
   "inochi_m1":  ("brewery", "he sits slumped against a large sake barrel, the serpent goddess leans over him feeding him sake mouth to mouth, kiss, sake running down his chest, her tongue-wet fingers on his nipple, " + TAIL + ", a wooden ladle, cum dripping untouched, " + TAG),
   "onedari_m1": ("den", "he sits up on her coils looking up with his mouth open, the serpent goddess pours sake from her lips into his mouth, " + NECKS + " each holding a small sake cup, her hand on his nipple, cum dripping untouched, " + TAG),
   # オロチ 技2（★八つの首の責め）
   "btl_m2":     ("den", "he lies on his back on her coils with arms open, the serpent goddess sucks his nipple, " + NECKS + " licking his ear and his inner thigh, " + TAIL + ", a braided cord of many colors tied around his neck, cum on his stomach untouched"),
   "onani_m2":   ("hearth", "kneeling alone before the sunken hearth, one hand stroking his own ear and neck, the other hand rubbing his own nipple then sliding to his inner thigh, penis untouched, the serpent goddess watches far above through the smoke hole in the roof, " + TAG),
   "inochi_m2":  ("litter", "he sits inside the swaying palanquin with his clothes opened, the serpent goddess leans in through the white curtains licking his ear, her hand rolling his nipple, the tip of her snake tail sliding along his inner thigh, he grips the curtain, cum dripping untouched, " + TAG),
   "onedari_m2": ("den", "he lies on the stone floor holding his own knees open, the serpent goddess licks his nipple, " + NECKS + " licking both his ears, " + TAIL + ", teasing grin, cum on his stomach untouched, " + TAG),
   # オロチ 技3（八つの口づけ）
   "btl_m3":     ("den", "from side, he is wrapped in her coils up to his chest, the serpent goddess kisses him deeply holding his face, tongues, saliva trail, one more of her long serpent necks with an identical black-haired head waiting close to his lips, " + TAIL + ", cum dripping untouched, " + TAG),
   "onani_m3":   ("lake", "kneeling alone on the flat rock by the black water, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, the serpent goddess watches far away from the dark water, " + TAG),
   "inochi_m3":  ("festival", "at dawn under the festival tower, he stands on tiptoe held up by her coils, the serpent goddess kisses him deeply, tongues, her hand rubbing his nipple, the tip of her snake tail stroking between his buttocks, fading lanterns, cum dripping untouched, " + TAG),
   "onedari_m3": ("den", "from side, he lies on his side cuddled in her coils as if sleeping together, the serpent goddess kisses him deeply from above, tongues, saliva trail, her fingers rolling his nipple, " + TAIL + ", cum on his stomach untouched, " + TAG),
   # 雪女（★氷の手撫）
   "btl_e1":     ("ice", "he is held in the snow woman's arms on the cold tatami, his back against her chest, the snow woman pinches his nipple with pale cold fingers, two fingers of her other hand deep in his anus, fingering, cold mist, an ice hairpin in his hair, cum on his stomach untouched, " + TAG),
   "onani_e1":   ("snow", "kneeling alone in the snow cave, pinching his own nipple with snow-chilled fingers, the other snow-chilled hand reaching behind to his own anus, white breath, penis untouched, the snow woman watches far away among the icicles, " + TAG),
   "inochi_e1":  ("snow", "he lies on the white fur hugged tightly from the front by the snow woman, his face against her chest, her cold hand reaching behind him with a finger in his anus, fingering, faint warm glow flowing from his body into hers, blowing snow outside, he clings to her, " + TAG),
   "onedari_e1": ("ice", "he lies on his back on the cold tatami before the ice screen, the snow woman kneels over him pressing two cold fingers in his anus, fingering, her other cold fingertip circling his nipple, faint frost flowers on his chest, quiet smile, a small silver key on a cord, cum dripping untouched"),
   # くのいちエルフ（★影縫い）
   "btl_e2":     ("ninja", "he sits frozen on the tatami with his legs open, thin needles pinned into his shadow on the floor, the kunoichi sits on a low table before him, her tabi-socked toes pinching his nipple, her other sole pressing and circling on his lower belly, cum dripping untouched, " + TAG, {"neg": NEEDLE_NEG}),
   "onani_e2":   ("hidden", "standing alone in the narrow tunnel with one foot braced against the wall, pressing and circling the sole of his own other foot on his lower belly, awkward frozen pose, penis untouched, the kunoichi watches far away from the rope ladder, " + TAG),
   "inochi_e2":  ("gate", "he stands frozen in the middle of the village street under the lanterns, the kunoichi stands on his shadow with one foot, her other tabi-socked foot raised rubbing his chest and nipple, red scarf fluttering, playful grin, his knees trembling, " + TAG, {"neg": NEEDLE_NEG}),
   "onedari_e2": ("ninja", "he lies face down pinned on the tatami, the kunoichi lies over his back locking his arm between her thighs in a grappling hold, two fingers of her free hand in his anus, fingering, a needle pinned into the shadow of his hand, cum dripping untouched, " + TAG, {"neg": NEEDLE_NEG}),
   # 濡れ女（★濡れ髪の巻きつき）
   "btl_e3":     ("lake", "he floats waist-deep in the black water held against the wet woman, her long wet dark hair wound around his wrists and chest, slick hair tips stroking both his nipples, her white snake tail coiled around his waist, a bracelet of braided dark hair on his wrist, cum in the water untouched"),
   "onani_e3":   ("passage", "leaning alone against the wet rock wall, holding a wet lock of his own hair and brushing its tip over his own nipple, shirt open, penis untouched, the wet woman watches far away from a puddle on the floor, " + TAG),
   "inochi_e3":  ("entrance", "just before the mossy torii with daylight beyond, he stands wrapped from shoulders to ankles in the wet woman's long wet dark hair, the wet woman embraces him from behind, hair tips stroking his nipples, he leans back into her, cum dripping untouched, " + TAG),
   "onedari_e3": ("lake", "he lies on the flat rock at the shore, the wet woman's wet dark hair wound around his wrists and chest, a bundle of hair pinching and rubbing his nipple, the tip of her white snake tail stroking the outside of his anus without entering, a folded white kimono beside them, cum on his stomach"),
   # 蜘蛛之皇女（★糸の褥）
   "btl_boss":   ("silk", "he hangs spread in the air held gently by soft white silk threads on his wrists and ankles, wearing a thin white silk under-kimono opened at the front, the spider princess looks down at him with her third eye, " + CORDIN + ", her fingers plucking taut threads, a blank paper talisman on his chest, cum dripping untouched"),
   "onani_boss": ("shrine", "kneeling alone by a shrine pillar, his wrists loosely tied to the pillar with his own cloth sash, a finger of one hand reaching behind in his own anus, penis untouched, the spider princess watches far above from the ceiling beams, " + TAG),
   "inochi_boss":("shrine", "he stands frozen at the shrine doorway with many fine white threads stuck to his arms and legs, blank paper talismans on his chest, the spider princess behind him tracing his chest with the tip of one sleek spider leg, " + CORDIN + ", cum dripping untouched, " + TAG),
   "onedari_boss":("silk", "he lies on a hammock-like bed of white silk threads with his wrists bound above his head by threads, three blank paper talismans on his chest and belly, the spider princess leans over him, " + CORDIN + ", plucking a single thread with one fingertip, cold smile, cum on his stomach untouched"),
 },
 "lose_desc": "keeps him forever in the cave as the cherished offering of the serpent goddess, twelve round red seals on the blank white wooden tag at his neck.",
 "onanie": {
   "master": ("den", "kneeling, one hand stroking his own ear and neck, the other hand rubbing his own nipple then his inner thigh, both hands moving without rest, penis untouched"),
   "e1": ("snow", "kneeling in the snow cave, pinching his own nipple with snow-chilled fingers, the other chilled hand reaching behind to his own anus, penis untouched"),
   "e2": ("hidden", "standing with one foot braced against the wall, pressing and circling the sole of his own other foot on his lower belly, penis untouched"),
   "e3": ("passage", "leaning against the wet rock, brushing the wet tip of a lock of his own hair over his own nipple, penis untouched"),
   "boss": ("shrine", "kneeling by a pillar, wrists loosely tied to it with his own cloth sash, a finger reaching behind in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "shrine", "a round vermilion seal stamp and a red ink pad beside a blank white wooden tag with one round red seal mark, without text, soft lantern glow, close-up"),
   "2": (None, "den", "a string of small golden bells hanging in the dark cavern, one bell ringing with faint sound ripples, sake pool glimmering behind"),
   "3": ("e2", "ninja", "throwing a thin needle toward a long shadow on the tatami, red scarf fluttering, sharp confident smile"),
   "4": ("m", "den", "raising a vermilion sake cup filled with glowing sacred sake to her lips, licking her lips, bold inviting grin"),
   "5": (None, "festival", "a wooden festival tower with rows of glowing paper lanterns, sake barrels and a white-curtained palanquin waiting below, night, blank lanterns without text"),
 },
}
