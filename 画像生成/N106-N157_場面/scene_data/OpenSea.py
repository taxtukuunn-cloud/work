# N151 外海の魔物（OpenSea）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（武人も曲線のある体つき）。
# 水龍娘：原作は青い長髪・青い竜の尾 → 髪は pale turquoise-white、尾は jade green に置き換え（瞳は金）。
# イッカク娘：原作は紺色の髪 → dark purple hair に置き換え（瞳は silver-grey）。
# シーアネモネ：原作は水色の長髪・青緑の触手 → 髪は lavender、触手は emerald green に置き換え。
# 挿入扱いはシーアネモネの触手（体の一部なので pen なし）だけ。水龍娘は指だけ。イッカク娘・マンタ娘・ヒトデ娘は後ろに触れない。
# 水の中は竜の加護で息ができる（溺れる・苦しむ絵にしない。穏やかな顔と泡）。巻きつきは苦しくない。イッカクの角は丸い先で触れるだけ（突かない）。
WET = "his white shirt wet and clinging"
OAR = "an oar wrapped in dark green kelp"
CALM = "calm relaxed face, rising bubbles"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs, monster face, drowning, choking, struggling, pain"
TAIL_NEG = SOFT_NEG + ", human legs on the woman"
HORN_NEG = TAIL_NEG + ", stabbing, horn piercing skin, wound, sharp horn tip, frostbite"
DATA = {
 "code": "OpenSea",
 "world": "vast open sea far from land, rolling swells, sea spray, deep clear water, drifting bubbles, soft light through the water, detailed background",
 "bg": "open sea in daytime with no land in sight, large gentle swells, a wooden rowboat rocking on the waves, an oar wrapped in dark green kelp, a distant black reef, the long shadow of a sea dragon under the waves, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "水龍娘",
         "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, pale turquoise-white hair, very long straight hair, curved dragon horns, fin ears, golden eyes, slit pupils, blush, white scale bikini top, pearl necklace, gold armlets, very long jade green sea dragon tail instead of legs, smooth scales, soft voluptuous feminine body, huge breasts, wide hips, sea dragon woman",
         "name": "the horned sea dragon woman with a jade green tail",
         "pose": "upright on her coiled jade green dragon tail, fidgeting with her fingertips together in front of her chest, shy blushing face, glancing at viewer",
         "height_note": "she is much taller than him",
         "neg": TAIL_NEG},
   "e1": {"type": "woman", "jp": "マンタ娘",
          "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale lilac skin, black hair, long straight hair, violet eyes, huge manta ray fins spreading from her arms and back like a wide cape, dark violet outside and white silky inside, thin manta tail, dark violet leotard, soft curvy feminine body, large breasts, manta ray woman",
          "name": "the lilac-skinned manta woman with cape-like fins",
          "pose": "spreading her wide manta fins like an opening cape, chin raised, haughty relaxed smirk, looking down at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "シーアネモネ",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, lavender hair, very long wavy hair, amber eyes, pearl hair ornament, green shell bikini top, lower body of a large sea anemone with many emerald green feathery soft tentacles, glossy wet skin, soft curvy feminine body, large breasts, sea anemone woman",
          "name": "the lavender-haired sea anemone woman with green feathery tentacles",
          "pose": "one finger on her lips, a feathery green tentacle curling beside her cheek, sultry gentle smile, looking at viewer",
          "neg": TAIL_NEG + ", stinging, needles"},
   "e3": {"type": "woman", "jp": "ヒトデ娘",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, purple skin, pink hair, short hair, yellow eyes, magenta starfish-shaped hood, magenta bikini top, five large magenta starfish arms spreading from her back, countless soft pale tube feet on the underside of the starfish arms, soft curvy feminine body, large breasts, wide hips, starfish woman",
          "name": "the purple-skinned starfish woman in a magenta hood",
          "pose": "both arms reaching forward as if to cling, starfish arms spread wide behind her, sweet clingy smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "イッカク娘",
            "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, dark purple hair, long hair, high ponytail, single long white spiral horn on her forehead with a smooth rounded tip, silver-grey eyes, white fur stole, silver chest wrap, long thick white narwhal tail instead of legs, smooth white skin on the tail, mermaid, soft voluptuous feminine body, large breasts, wide hips",
            "name": "the one-horned narwhal woman with a white tail",
            "pose": "upright on her thick white narwhal tail, arms crossed under her breasts, stern proud expression, looking down at viewer",
            "height_note": "she is much taller than him",
            "neg": HORN_NEG},
 },
 "places": {
   "boat":    "wooden rowboat rocking on the open sea, folded canvas sail, an oar wrapped in dark green kelp, sea wind",
   "sea":     "surface of the open sea, large gentle swells, no land in sight, a long shadow under the waves",
   "reef":    "black rocky reef, sea spray, a quiet tide pool in the shade of the rocks, seabirds far away",
   "shallow": "warm sunny shallows, soft sand under clear water, magenta starfish scattered on the sand",
   "anemone": "underwater sea anemone field, many green feathery tentacles swaying on soft sand, glossy warm slime",
   "coral":   "underwater coral forest, colorful coral branches, swaying seaweed, schools of fish",
   "manta":   "underwater deep quiet water, slow current, light from the far surface, a wide shadow gliding",
   "ice":     "cold sea with drifting ice floes, white breath, pale sky",
   "icecave": "ice cave, ceiling of ice, pale glowing light, a warm bed of white furs at the back",
   "wreck":   "sunken ship captain's cabin underwater, tilted bed, treasure chest, hanging seaweed",
   "cave":    "underwater sea cave, rising bubbles, a bed of softly glowing seaweed",
   "whirl":   "outer edge of a wide slow whirlpool, gently turning water, soft foam",
   "gate":    "entrance of a deep sea abyss seen from the surface, glinting dragon scales far below, a rowboat above",
   "abyss":   "quiet deep sea abyss, soft glowing light, a dragon nest, a long jade green tail coiled around",
   "bed":     "bottom of the abyss, pearl-white bed with pearl-colored bedding, enclosed by coils of a jade green tail",
 },
 "atk": {
   "m1": ("gate", "he kneels in the rowboat gripping the gunwale, leaning far over and staring down into the water, the sea dragon woman's blushing face rises just below the surface under him, the tip of her jade green tail lifting toward him, ripples from a low rumble, " + OAR + ", " + WET),
   "m2": ("abyss", "underwater, he floats wrapped from ankles to chest in the coils of her jade green tail, the sea dragon woman holds him from behind, timidly rolling his nipple with one hand, two fingers of her other hand in his anus, fingering, blowing a warm stream of water on his neck, shy blush, " + CALM),
   "m3": ("bed", "underwater on the pearl-white bed, he lies wrapped in the coils of her jade green tail, the sea dragon woman leans over him kissing him shyly, tongues, her eyes shut tight with a deep blush, two fingers of her hand in his anus, fingering, " + CALM),
   "e1": ("manta", "underwater, the manta woman glides through the deep water holding him wrapped inside her wide fins, his face pressed between her breasts, the silky white inside of her fins stroking his back and thighs, flowing water, haughty smile, " + CALM),
   "e2": ("anemone", "underwater, he is wrapped up to the chest in her green feathery tentacles, glossy warm slime on his skin, the sea anemone woman embraces him from behind, feathery tentacle tips brushing his nipples, a smooth slender tentacle in his anus, anal, his own penis separate, " + CALM),
   "e3": ("shallow", "he sits in the warm shallows, the starfish woman clings to his back, her five magenta starfish arms wrapped around his chest, waist and thighs, countless soft tube feet sucking on his nipples and inner thighs, her cheek against his, clingy smile, " + WET),
   "boss": ("icecave", "he is wrapped from the waist in the coils of her thick white narwhal tail, the narwhal woman bows her head and traces the side of his neck with the smooth rounded tip of her horn, touching only, her fingers pinching his nipple, white breath, warm embrace"),
 },
 "atk_desc": {
   "m1": "the sea dragon woman calls him over the side of the boat with a low rumble from the deep.",
   "m2": "the sea dragon woman coils him in her tail and timidly teases his nipple and presses inside with her fingers.",
   "m3": "the sea dragon woman kisses him shyly while keeping him coiled in her tail.",
   "e1": "the manta woman wraps him in her fins and glides through the sea with his face between her breasts.",
   "e2": "the sea anemone woman wraps him in slick feathery tentacles and strokes him deep inside.",
   "e3": "the starfish woman clings to his back and caresses his whole body with countless tube feet.",
   "boss": "the narwhal woman squeezes him in her warm white tail and traces his neck with her horn.",
 },
 "lose": {
   # 水龍娘 技1（竜の唸り）
   "btl_m1":     ("gate", "underwater just below the rowboat, he has climbed over the gunwale into the sea, the sea dragon woman catches him in the coils of her jade green tail, timidly stroking his nipple, two fingers of her other hand in his anus, fingering, a dragon scale necklace on his neck, cum drifting, " + CALM),
   "onani_m1":   ("boat", "alone in the rowboat, lying over the gunwale staring down into the sea, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, " + OAR + ", the sea dragon woman watches far below under the water"),
   "inochi_m1":  ("sea", "he sits in the rowboat with the oars stopped, bent forward and trembling, both hands on the boat bottom, the sea dragon woman rises beside the boat resting her arms on the gunwale, blushing, her jade green tail circling under the boat, ripples from a low rumble, " + OAR + ", cum dripping untouched"),
   "onedari_m1": ("bed", "underwater on the pearl-white bed, he lies wrapped tightly in many coils of her jade green tail, the sea dragon woman holds his head to her chest, her lips at his ear humming a low rumble, shy pleased blush, pearl-colored bedding, cum drifting untouched, " + CALM),
   # 水龍娘 技2（★水龍の抱擁）
   "btl_m2":     ("abyss", "underwater, he floats wrapped from ankles to chest in the coils of her jade green tail, the sea dragon woman faces him, timidly pinching his nipple, two fingers of her other hand pressing deep in his anus, fingering, a glowing pearl-colored light on his chest, cum drifting, " + CALM),
   "onani_m2":   ("wreck", "alone on the tilted bed in the sunken cabin, his wet cloak wrapped tightly around his body, one hand rubbing his own nipple, a finger of the other hand in his own anus, penis untouched, kelp on his ankle, the sea dragon woman watches far away through a crack in the hull"),
   "inochi_m2":  ("whirl", "at the edge of the slow whirlpool, he reaches out his hand toward her, the sea dragon woman pulls him back by the waist with a coil of her jade green tail, her hand stroking his nipple, blushing, gently turning water around them, cum drifting, " + CALM),
   "onedari_m2": ("bed", "underwater on the pearl-white bed, his whole body wrapped in many coils of her jade green tail, the sea dragon woman leans over him blowing a warm stream of water on his nipple, two fingers in his anus, fingering, shy blush, cum drifting, " + CALM),
   # 水龍娘 技3（竜の口づけ）
   "btl_m3":     ("bed", "underwater on the pearl-white bed, he lies wrapped in the coils of her jade green tail, the sea dragon woman kisses him deeply with a deep blush, tongues, two fingers of her hand pressing in his anus, fingering, a piece of dragon horn on a cord at his neck, cum drifting, " + CALM),
   "onani_m3":   ("cave", "alone on the bed of glowing seaweed in the sea cave, sucking two of his own wet fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, kelp on his wrist, the sea dragon woman watches far away from the cave entrance"),
   "inochi_m3":  ("abyss", "underwater, he floats with his arms around her neck, the sea dragon woman holds his face in both hands kissing him for a long time, her eyes shut tight, deep blush, her jade green tail coiling around his waist and legs, cum drifting untouched, " + CALM),
   "onedari_m3": ("bed", "underwater on the pearl-white bed, he lies on his side wrapped tightly in her jade green tail, the sea dragon woman kisses him deeply, tongues, saliva, two fingers deep in his anus, fingering, her other hand holding his cheek, cum drifting, " + CALM),
   # マンタ娘（★マンタバスト）
   "btl_e1":     ("manta", "underwater, the manta woman glides down through the deep water with him wrapped completely inside her wide fins, his face buried between her breasts, the silky white inside of her fins stroking his lower belly, a manta-shaped charm on his neck, cum drifting, " + CALM),
   "onani_e1":   ("boat", "alone in the rowboat wrapped in the canvas sail like a cloak, both hands under the canvas rubbing his own nipples, penis untouched, " + OAR + ", the wide shadow of the manta woman watches far below under the boat"),
   "inochi_e1":  ("manta", "underwater, he rides on the manta woman's back holding her shoulders, her wide fins folding up around him from both sides, the silky white inside stroking his sides and thighs, the surface light far above, diving deeper, smirk, cum drifting untouched, " + CALM),
   "onedari_e1": ("manta", "underwater, the manta woman swims slowly holding him against her chest inside her closed fins, his face squeezed between her breasts, her fingers rolling his nipple, flowing water, satisfied haughty smile, cum drifting, " + CALM),
   # シーアネモネ（★アネモネホールド）
   "btl_e2":     ("anemone", "underwater, he is wrapped up to the shoulders in her green feathery tentacles, glossy warm slime all over him, the sea anemone woman holds him from behind, tentacle tips curled around his nipples, a smooth slender tentacle deep in his anus, anal, his own penis separate, cum drifting untouched, " + CALM),
   "onani_e2":   ("coral", "alone in the shade of a coral branch, strands of seaweed wrapped around his chest and waist, a wet finger in his own anus, penis untouched, kelp on his ankle, the sea anemone woman watches far away beyond the coral"),
   "inochi_e2":  ("anemone", "underwater in the middle of the anemone field, he kneels on the soft sand, green feathery tentacles reaching from all sides spreading glossy slime over his chest and thighs, the sea anemone woman embraces him from the front, smiling, cum drifting untouched, " + CALM),
   "onedari_e2": ("anemone", "underwater, he lies back wrapped entirely in all her green feathery tentacles, glossy slime, the sea anemone woman leans over him, tentacle tips on both his nipples, a smooth slender tentacle deep in his anus, anal, his own penis separate, cum drifting, " + CALM),
   # ヒトデ娘（★管足全身愛撫）
   "btl_e3":     ("shallow", "he lies on his side in the warm shallows, the starfish woman clings to his back, her five magenta starfish arms wrapped around his chest, waist and thighs, countless soft tube feet sucking on his nipples, neck and inner thighs, a magenta starfish charm on his neck, cum on his stomach"),
   "onani_e3":   ("reef", "sitting alone in a tide pool in the shade of the rocks, stroking his own chest, sides and inner thighs with light fingertips, poking his own nipple, penis untouched, the starfish woman watches far away from the top of the rock"),
   "inochi_e3":  ("boat", "morning in the rowboat, he sits holding her starfish arm against his own chest with both hands, the starfish woman clings to his back with all five arms, tube feet on his nipples, her cheek on his shoulder, happy smile, " + OAR + ", cum dripping untouched"),
   "onedari_e3": ("shallow", "he kneels in the middle of the warm shallows with his arms open, the starfish woman clings to his back, starfish arms around his chest and thighs, countless soft tube feet sucking his nipples and stroking his whole body, laughing sweetly, cum dripping"),
   # イッカク娘（★氷海の締め上げ）
   "btl_boss":   ("icecave", "on the bed of white furs, he is wrapped from waist to chest in the coils of her thick white narwhal tail, the narwhal woman traces a circle around his nipple with the smooth rounded tip of her horn, touching only, water drops on his skin, a horn-shaped charm on his neck, cum on the white tail"),
   "onani_boss": ("ice", "kneeling alone on an ice floe, wet with cold seawater, hugging his own chest tightly with both arms, rubbing his nipples against his forearms, shivering, penis untouched, the narwhal woman watches far away, her horn showing from a gap in the ice"),
   "inochi_boss":("ice", "on the last ice floe, he stands looking back over his shoulder, the narwhal woman rises behind him and wraps her thick white tail around his waist and chest, her arms holding him warm, white breath, steam rising from his cold skin, cum dripping untouched"),
   "onedari_boss":("icecave", "deep in the ice cave, he is squeezed tightly in the coils of her thick white narwhal tail with his chin raised, the narwhal woman slowly traces down his neck with the smooth rounded tip of her horn, touching only, stern approving smile, cum on the white tail"),
 },
 "lose_desc": "keeps him in the open sea forever, never to return to land, an oar wrapped in twelve strands of kelp left behind.",
 "onanie": {
   "master": ("boat", "sitting in the rowboat with his wet cloak wrapped tightly around his body, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, penis untouched"),
   "e1": ("boat", "wrapped in the canvas sail like a cloak, both hands rubbing his own nipples under the canvas, penis untouched"),
   "e2": ("coral", "strands of seaweed wrapped around his chest and waist, a wet finger in his own anus, penis untouched"),
   "e3": ("reef", "sitting in a tide pool, stroking his own chest, sides and inner thighs with light fingertips, penis untouched"),
   "boss": ("ice", "kneeling on an ice floe, hugging his own chest tightly with both arms, nipples rubbing against his forearms, penis untouched"),
 },
 "magic": {
   "1": (None, "boat", "a wooden oar with two fresh strands of dark green kelp winding around its shaft, water dripping, close-up, soft ripples"),
   "2": (None, "sea", "several large and slender shadows of sea creatures gathering under the waves around an empty rowboat, the current turning, gentle ripples"),
   "3": (None, "whirl", "a wide slow whirlpool of warm clear water seen from above, soft foam rings turning gently, calm and inviting"),
   "4": ("m", "abyss", "blowing a warm glowing stream of water from her pursed lips, one hand raised beside her mouth, shy blushing face, bubbles"),
   "5": (None, "abyss", "a quiet deep sea abyss with soft light at the bottom, a long jade green dragon tail coiled around a nest of pearls, faint sound ripples rising"),
 },
}
