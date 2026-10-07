# N47 朧廓の花魁（Oiran）場面データ。登場人物は全員20歳以上。女性とニューハーフの混合（コノハ・ヒスイ・シロタエ＝NH）。敗北28本は主人公が緋色の振袖のまま。
FURI = "a scarlet furisode kimono with long sleeves and a wide gold obi, red nagajuban underneath, white tabi"
FURI_OPEN = FURI + ", the kimono hem opened"
FURI_CHEST = FURI + ", the collar pulled open showing his flat chest, the hem opened"
DATA = {
 "code": "Oiran",
 "world": "misty otherworldly edo-period pleasure quarter at night, red lanterns, vermilion lattices, drifting fog, detailed background",
 "chars": {
   "m":    {"type": "woman", "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, long legs, black hair, date hyogo hairstyle, few kanzashi, red eyes, red lipstick, lavish purple and black uchikake kimono, obi tied in front, large breasts",
            "name": "the black-haired oiran in a purple and black uchikake"},
   "e1":   {"type": "nh", "tags": "adult woman, mature female, mature face, sharp adult features, 21 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, pink hair, shimada hairstyle, brown eyes, furisode kimono with gold threads, small breasts",
            "name": "the pink-haired shinzo in a gold-thread furisode"},
   "e2":   {"type": "woman", "tags": "adult woman, mature female, mature face, sharp adult features, 26 years old, adult proportions, beautiful detailed eyes, long legs, brown hair, yoko hyogo hairstyle, green eyes, black kimono with iris pattern, white tabi, large breasts",
            "name": "the brown-haired courtesan in a black iris kimono"},
   "e3":   {"type": "nh", "tags": "adult woman, mature female, mature face, sharp adult features, 25 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, green hair, tsubushi shimada hairstyle, gold eyes, white kimono with jade green accents, shamisen, medium breasts",
            "name": "the green-haired geisha in a white kimono"},
   "boss": {"type": "nh", "tags": "adult woman, mature female, mature face, sharp adult features, 34 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, white hair, very long hair tied in a large traditional style, gold eyes, white and gold uchikake over a scarlet nagajuban, large breasts",
            "name": "the white-haired tayu in a white and gold uchikake"},
 },
 "places": {
   "zashiki":  "oiran's tatami parlor, andon paper lamp light, tokonoma alcove with a hanging scroll without text, lacquered tray, red futon",
   "byobu":    "narrow red futon enclosed by a six-panel gold folding screen painted with autumn grasses, andon lamp light",
   "harimise": "harimise display room behind vermilion wooden lattice bars, tatami inside, red lanterns and misty street outside",
   "street":   "misty pleasure quarter street at night, red lanterns, the great black gate faint in the fog",
   "keiko":    "plain lesson room, thin futon on tatami, pillow, warmed oil pot, oil lamp",
   "ozashiki": "geisha banquet room, zabuton cushions, sake cups on low trays, shamisen, gold fusuma doors",
   "kitsuke":  "dressing room, tall black lacquered mirror stand, kimono racks with colorful furisode, folded obi",
   "tayu":     "luxurious tayu chamber, white and gold fusuma, thick red futon, silk bedding, incense smoke",
   "shinshitsu": "oiran's bedroom, silk futon, paper lamp, folded uchikake on a stand",
 },
 "atk": {
   "m1": ("zashiki", "he lies with his head on the oiran's lap, the oiran holds a long kiseru pipe above his face and blows thick purple smoke onto his lips, no hands on him, back arched, toes curled"),
   "m2": ("shinshitsu", "he lies on the silk futon, the oiran leans over him kissing him deeply, tongues, saliva trail, her thigh pressed between his legs, red lipstick"),
   "m3": ("byobu", "from side, he lies on his back on the red futon behind the gold screen with legs lifted, the oiran kneels between his legs pegging his anus with her strap-on, anal, licking his nipple, his own penis separate", {"pen": "strapon"}),
   "e1": ("kitsuke", "he stands before the tall mirror stand, the shinzo stands behind him tightening the obi around his waist, her hand slipped inside his long sleeve pinching his nipple, flushed, trembling", {"hero_outfit": FURI}),
   "e2": ("keiko", "from side, he lies on his side on the thin futon holding his knees, the courtesan kneels behind him with two oiled fingers in his anus, fingering, calm expression, oil pot beside"),
   "e3": ("ozashiki", "he kneels in seiza on a zabuton with hands on his knees, the geisha sits close beside him playing the shamisen, singing into his ear, his body swaying to the song, trembling, blush"),
   "boss": ("tayu", "he is held against the tayu inside the hem of her scarlet nagajuban, the tayu pinches his nipple with one hand, two fingers of her other hand in his anus, fingering, gentle smile"),
 },
 "atk_desc": {
   "m1": "the oiran blows kiseru smoke until his mind turns white.",
   "m2": "the oiran gives him the bedroom kiss of a regular guest.",
   "m3": "the oiran takes him behind the gold folding screen.",
   "e1": "the shinzo dresses him in a scarlet furisode.",
   "e2": "the courtesan teaches him the bedroom lesson.",
   "e3": "the geisha sings a parlor song that rewrites his common sense.",
   "boss": "the tayu embraces him in her scarlet nagajuban.",
 },
 "lose": {
   # 花魁 技1（煙管の煙）
   "btl_m1":     ("zashiki", "he lies with his head on the oiran's lap, the oiran holds the long kiseru and blows thick purple smoke onto his face, no hands on him, back arched, cum soaking the scarlet hem, twelve blank vermilion tokens without text beside", {"hero_outfit": FURI_OPEN}),
   "onani_m1":   ("harimise", "kneeling alone in seiza outside the lattice with hands on his knees, head tilted back breathing in drifting purple smoke, trembling, penis untouched, the oiran sits far behind the lattice holding a kiseru, watching", {"hero_outfit": FURI}),
   "inochi_m1":  ("zashiki", "he kneels on the tatami with his mouth open, a red thumbprint on a blank paper without text beside him, the oiran bends down blowing kiseru smoke into his mouth, no hands on him, trembling", {"hero_outfit": FURI}),
   "onedari_m1": ("zashiki", "he kneels before the oiran with his mouth open begging, a blank written pledge without text on the tatami, the oiran exhales purple smoke from the kiseru over his face, trembling, drool", {"hero_outfit": FURI}),
   # 花魁 技2（床入りの口吸い）
   "btl_m2":     ("shinshitsu", "he lies on the silk futon, the oiran leans over him kissing him deeply, tongues, saliva trail, her thigh pressed against his crotch, cum soaking the scarlet hem", {"hero_outfit": FURI_OPEN}),
   "onani_m2":   ("harimise", "sitting alone by a lattice pillar, sucking two of his own fingers deeply as if kissing, the other wet hand slipped into his collar rubbing his nipple, penis untouched, the oiran watches from behind the lattice", {"hero_outfit": FURI}),
   "inochi_m2":  ("zashiki", "he kneels with red lipstick on his lips, the oiran holds his face and kisses him deeply, tongues, a silver saliva thread mixed with red rouge, a blank paper with a red lip print without text on the tatami", {"hero_outfit": FURI}),
   "onedari_m2": ("shinshitsu", "he lies on the silk futon with his lips parted, the oiran lies over him kissing him deeply, her hand under his collar pinching his nipple, saliva trail, blush", {"hero_outfit": FURI_CHEST}),
   # 花魁 技3（屏風の陰で・ペニバン）
   "btl_m3":     ("byobu", "from side, he lies on his back on the red futon with legs lifted, the oiran kneels between his legs pegging his anus with her strap-on, anal, licking his nipple, his own penis separate, cum on his chest", {"pen": "strapon", "hero_outfit": FURI_CHEST}),
   "onani_m3":   ("harimise", "on all fours alone on the tatami behind the lattice with his hips raised, one arm reaching behind with two of his own fingers in his own anus, the other hand in his collar on his nipple, penis untouched, the oiran watches from the gold screen", {"hero_outfit": FURI_OPEN}),
   "inochi_m3":  ("byobu", "from side, he lies on his back on the red futon, the oiran over him pegging his anus with her strap-on, anal, sucking his nipple, his own penis separate, cum on the scarlet silk", {"pen": "strapon", "hero_outfit": FURI_CHEST}),
   "onedari_m3": ("byobu", "from side, he lies on the red futon holding his knees up begging, the oiran pegging his anus with her strap-on, anal, sucking his nipple, his own penis separate, a blank written pledge without text by the pillow", {"pen": "strapon", "hero_outfit": FURI_CHEST}),
   # 新造 コノハ（振袖を着せる）
   "btl_e1":     ("kitsuke", "he stands before the tall mirror stand with red lipstick, the shinzo kneels behind him hugging him, her hand inside his sleeve pinching his nipple, her other hand rubbing his crotch through the red silk, cum stain on the hem", {"hero_outfit": FURI}),
   "onani_e1":   ("harimise", "standing alone leaning on a lattice pillar, hugging himself over the tight obi, stroking his own thighs and bottom through the silk, knees trembling, penis untouched, the shinzo watches from behind the lattice", {"hero_outfit": FURI}),
   "inochi_e1":  ("street", "he kneels on the misty street clinging to the shinzo's arm, the great gate far behind in the fog, the shinzo's hand inside his long sleeve pinching his nipple, trembling, flushed", {"hero_outfit": FURI}),
   "onedari_e1": ("kitsuke", "he lies on a futon tightly bound by the obi, the shinzo kneels beside him wrapping his penis in her gold-thread sleeve and stroking it, cum on the silk, a blank pledge paper without text", {"hero_outfit": FURI_OPEN}),
   # 遊女 アヤメ（床の指南）
   "btl_e2":     ("keiko", "from side, he lies on his back on the thin futon holding his knees, the courtesan kneels with two oiled fingers in his anus, her white tabi foot pressing his penis, cum soaking the tabi", {"hero_outfit": FURI_OPEN}),
   "onani_e2":   ("harimise", "crouching alone in the shadow beside the lattice, one arm reaching behind with two of his own oiled fingers in his own anus, knees trembling, penis untouched, the courtesan watches calmly from behind the lattice", {"hero_outfit": FURI_OPEN}),
   "inochi_e2":  ("keiko", "from side, he lies on his back on the futon with his knees spread, the courtesan kneels between his knees with two fingers in his anus, fingering, her tabi feet holding his knees apart, cum on the scarlet hem, a blank certificate without text on the pillar", {"hero_outfit": FURI_OPEN}),
   "onedari_e2": ("keiko", "he lies face down on the futon with a pillow under his hips, the courtesan kneels beside him with two fingers in his anus, fingering, calm face, oil pot, a blank pledge paper without text", {"hero_outfit": FURI_OPEN}),
   # 芸者 ヒスイ（お座敷の小唄）
   "btl_e3":     ("ozashiki", "he kneels on a zabuton with his back arched and hands on his knees, the geisha sits beside him plucking the shamisen and singing into his ear, his long sleeves swaying, cum soaking the scarlet hem, no hands on him", {"hero_outfit": FURI_OPEN}),
   "onani_e3":   ("harimise", "sitting alone against a lattice pillar with both hands on his knees, mouthing the words of a song, hips floating, trembling, penis untouched, the geisha watches from behind the lattice with the shamisen", {"hero_outfit": FURI}),
   "inochi_e3":  ("ozashiki", "he kneels on a zabuton singing with tears in his eyes, a blank travel pass without text on the tatami, the geisha plucks the shamisen string right beside his ear, his body arched, trembling", {"hero_outfit": FURI}),
   "onedari_e3": ("ozashiki", "he kneels on a zabuton holding a blank pledge paper without text, the geisha sits beside him singing into his ear and plucking the shamisen, his hips floating, cum soaking the hem", {"hero_outfit": FURI_OPEN}),
   # 太夫 シロタエ（緋襦袢の抱擁）
   "btl_boss":   ("tayu", "he is held against the tall tayu inside the hem of her scarlet nagajuban, the tayu pinches his nipple, two fingers of her other hand in his anus, her thigh pressing his crotch, cum soaking the scarlet silk", {"hero_outfit": FURI_CHEST}),
   "onani_boss": ("harimise", "sitting alone wrapped in a scarlet cloth, one hand pinching his own nipple, the other hand reaching behind with fingers in his own anus, penis untouched, the tayu watches from the high seat behind the lattice", {"hero_outfit": FURI_CHEST}),
   "inochi_boss":("tayu", "from side, he lies on his back on the thick red futon, the tayu over him penetrating his anus with her own penis, anal, pinching his nipple, wrapping him in her scarlet nagajuban, his own penis separate, cum on the silk", {"pen": "penis", "hero_outfit": FURI_CHEST}),
   "onedari_boss":("tayu", "he sits inside the tayu's scarlet nagajuban with his back to her, the tayu hugs him from behind pinching his nipple, two fingers in his anus, her thigh lifting his crotch, cum soaking the silk, a blank pledge paper without text", {"hero_outfit": FURI_CHEST}),
 },
 "lose_desc": "keeps him in the pleasure quarter in a scarlet furisode forever.",
 "onanie": {
   "master": ("zashiki", "kneeling in seiza with hands on his knees, head tilted back breathing in drifting purple smoke, mouth open, hips twitching, penis untouched"),
   "e1": ("kitsuke", "standing before the mirror stand, tightening an obi around his own waist, stroking his own thighs through red silk, penis untouched", {"hero_outfit": FURI}),
   "e2": ("keiko", "lying on his side on the thin futon holding one knee, two of his own oiled fingers in his own anus, penis untouched"),
   "e3": ("ozashiki", "kneeling on a zabuton with both hands on his knees, singing a song to himself, body swaying, hips floating, penis untouched"),
   "boss": ("tayu", "wrapped in a scarlet cloth, one hand pinching his own nipple, the other hand reaching behind with fingers in his own anus, penis untouched"),
 },
}
