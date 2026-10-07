# N131 魔族領と雪原（Moon1）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（エイルも曲線のある体つき）。
# 原作に青・水色の髪や瞳のキャラはいない。氷の洞の光は青を避けて pale icy white glow と書く。
# 挿入扱いはエイルの呪具の触手の先だけ（触手なので pen なし）。クロノム・スノウは指、リヤは魔力の黒い手の指まで。ナンシーは後ろに触れない。
# リヤの魔力の手は何本でも「本体1人＋主人公」で描く（黒い魔力の手は人物ではなく、もやから伸びる手の形）。
# 凍結は痛みなし（手首・足首を包む透明な氷の輪。凍傷・傷なし）。スノウの刀は抜かない（鞘に収めたまま柄で触れる）。
MARK = "small softly glowing sigils on the back of his left hand"
CHAIN = "soft thin silver chains loosely linking his wrists and ankles"
ICE = "smooth clear rings of ice around his wrists"
TENT = "smooth glossy dark violet tentacles from her bracelet"
HANDS = "many smooth black hands made of dark magic mist"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, biceps, scary, fangs"
TENT_NEG = SOFT_NEG + ", grotesque, slimy monster, teeth, suckers with teeth, horror"
ICE_NEG = SOFT_NEG + ", frostbite, wound, drawn sword, bare blade, blood"
DATA = {
 "code": "Moon1",
 "world": "fantasy demon territory beyond a snowfield, purple sky, black earth, a distant great clock tower, cold air, detailed background",
 "bg": "wide snowfield leading to a demon territory, purple twilight sky, black earth beyond the snow, a fence of hanging chains, a huge clock tower far away on the horizon, drifting snow, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "クロノム",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, silver hair with purple streaks, very long hair, violet eyes, curved black demon horns, pocket watch necklace, long black dress with gear ornaments, black gloves, soft curvy feminine body, large breasts, narrow waist",
         "name": "the silver-and-purple-haired horned demoness in a black gear dress",
         "pose": "holding up a pocket watch on its chain in one hand, the other hand at her chin, calm quiet smile, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "リヤ",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, red hair, long hair, red eyes, black demon lord outfit, high collar black cape, wisps of black magic mist clinging to her skin, soft curvy feminine body, large breasts",
          "name": "the red-haired woman in a black demon lord outfit",
          "pose": "arms crossed under her chest, chin raised, smug confident grin, black magic mist forming hand shapes around her, looking down at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "ナンシー",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, long legs, chestnut hair, long wavy hair, amber eyes, low-cut cream blouse, cleavage, long dark skirt, silver pendulum pendant, soft voluptuous feminine body, huge breasts",
          "name": "the chestnut-haired hypnotist in a low-cut blouse",
          "pose": "dangling a silver pendulum pendant from her fingers, the other hand on her chest, gentle smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "エイル",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, wide hips, dark brown hair, short hair, sharp golden wolf-like eyes, brown leather adventurer armor, dull glowing cursed bracelet on her left wrist, a patch of dark violet skin on her left arm, soft curvy feminine body, large breasts",
          "name": "the short-haired adventurer in leather armor with a cursed bracelet",
          "pose": "one hand on her hip, raising her left wrist with the dull glowing bracelet, friendly open grin, looking at viewer",
          "neg": TENT_NEG},
   "boss": {"type": "woman", "jp": "スノウ",
            "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, white hair, very long straight hair, silver-grey eyes, pale skin, white kimono-style swordswoman outfit, white hakama, sheathed katana at her hip, yuki-onna, soft curvy feminine body, large breasts",
            "name": "the white-haired swordswoman in a white kimono outfit",
            "pose": "standing straight with one hand resting on the hilt of her sheathed katana, expressionless cool gaze, cold mist at her feet, looking at viewer",
            "neg": ICE_NEG},
 },
 "places": {
   "tavern":  "town tavern interior, wooden tables, large beer mugs, warm lamp light, roast meat on plates",
   "eilhome": "adventurer's house interior, straw bed, fireplace, rice bales stacked by the wall, adventuring gear on shelves",
   "forest":  "leafless winter forest at the edge of town, log rest shelter, thin snow, cold wind",
   "snow1":   "open snowfield, footprints in the snow, white breath, grey sky",
   "snow2":   "snowfield in a blizzard, ice-covered rocks, swirling snow",
   "icecave": "ice cave, hanging icicles, pale icy white glow, frozen lake, fur rugs spread on the ice",
   "gate":    "entrance of the demon territory, purple sky, black earth, a fence of hanging chains",
   "cushion": "soft room full of large cushions, a swinging pendulum, sweet incense smoke, dim warm lamps",
   "clock":   "hall under a great clock, huge gears turning, clock hands, a bed beneath the clock face",
   "castle":  "demon lord castle throne room, black throne, tall windows, black carpet, stone pillars",
   "feast":   "castle banquet hall, long table lined with large beer mugs, candelabras",
   "tower":   "top of a clock tower, behind a giant clock face without numerals, stopped clock hands, shadows of gears, wind",
   "room":    "silent room of stopped time, shelves lined with hourglasses, stopped clocks without numerals, a soft wide bed",
 },
 "atk": {
   "m1": ("clock", "he kneels on the floor looking up, the horned demoness stands over him swinging a pocket watch before his face, her other hand stroking his chest through his open shirt, dazed, swaying, " + MARK),
   "m2": ("room", "he lies on his back on the soft bed, " + CHAIN + ", the horned demoness sits beside him, one gloved hand stroking his nipple, two oiled fingers of her other hand in his anus, fingering, frozen hourglasses floating in the air, calm smile, " + MARK),
   "m3": ("tower", "he sits on the floor against the clock face, the horned demoness kneels over his lap holding his cheek, kissing him slowly and deeply, tongues, saliva trail, her other hand reaching under him with a finger in his anus, fingering, " + MARK),
   "e1": ("castle", "he lies on the black carpet before the throne, " + HANDS + " stroking his whole body, pinching both his nipples, one thin black finger in his anus, the red-haired woman stands over him with her arms crossed, smug grin, " + MARK),
   "e2": ("cushion", "he lies sunk in the cushions, limp and relaxed, the hypnotist kneels beside him swinging a silver pendulum over his face, her other hand slowly stroking his nipple, whispering, gentle smile, " + MARK),
   "e3": ("eilhome", "he lies on his back on the straw bed, " + TENT + " wrapped loosely around his wrists and ankles, two tentacle tips sucking his nipples, one thin tentacle tip in his anus, the adventurer stands over the bed with sharp golden eyes, grinning, " + MARK),
   "boss": ("snow2", "he kneels in the snow, " + ICE + ", unable to move, the swordswoman kneels on one knee before him pinching his nipple with cold pale fingers, her other hand reaching behind him with a finger in his anus, fingering, frost mist, expressionless, " + MARK),
 },
 "atk_desc": {
   "m1": "the demoness swings her pocket watch and makes one second feel like an hour.",
   "m2": "the demoness stops time, chains him softly and stores up pleasure in his nipples and inside him.",
   "m3": "the demoness slows time into an endless kiss while slowly pressing inside him with her finger.",
   "e1": "the red-haired woman only watches with crossed arms while her black magic hands caress his whole body.",
   "e2": "the hypnotist relaxes him with her pendulum and soft suggestions while stroking his nipple.",
   "e3": "the adventurer's cursed bracelet binds him with smooth tentacles that suck his nipples and enter him.",
   "boss": "the swordswoman freezes his wrists and teases him with cold fingers as the ice melts.",
 },
 "lose": {
   # クロノム 技1（順応催眠）
   "btl_m1":     ("clock", "he kneels under the great clock, " + CHAIN + ", the horned demoness crouches before him swinging a pocket watch at his face, her other hand pinching his nipple, he leans toward her begging, cum dripping untouched, " + MARK),
   "onani_m1":   ("tower", "sitting alone behind the giant clock face, one hand rubbing his own nipple, a finger of the other hand in his own anus, head tilted listening to the ticking, penis untouched, the horned demoness watches far away among the gear shadows, " + MARK),
   "inochi_m1":  ("gate", "he sits on the black earth by the chain fence, the horned demoness kneels behind him holding a pocket watch before his face, her other gloved hand stroking his nipple under his open coat, purple sky, dazed, cum dripping, " + MARK),
   "onedari_m1": ("room", "he lies on the soft bed looking up, the horned demoness sits at his side swinging a pocket watch over his face, two fingers of her other hand in his anus, fingering, hourglasses on the shelves, pleading expression, cum on his stomach, " + MARK),
   # クロノム 技2（★時間空間展開）
   "btl_m2":     ("room", "he lies on his back on the soft bed, " + CHAIN + ", the horned demoness leans over him stroking his nipple, two oiled fingers deep in his anus, fingering, hourglasses with frozen sand floating around, a thin chain bracelet on his wrist, cum on his stomach, " + MARK),
   "onani_m2":   ("clock", "crouching alone in the shadow of the huge gears, holding perfectly still, one hand on his own nipple, a wet finger of the other hand pressing in his own anus, penis untouched, the horned demoness watches far away under the clock face, " + MARK),
   "inochi_m2":  ("clock", "he sits on the bed beneath the great clock without getting up, " + CHAIN + ", the horned demoness sits behind him, one hand pinching his nipple, the fingers of her other hand in his anus, fingering, stopped clock hands above, cum dripping, " + MARK),
   "onedari_m2": ("room", "he lies on a bed with soft chains at its four posts, wrists chained loosely above his head, the horned demoness kneels between his legs with two fingers in his anus, fingering, her other hand raised to snap her fingers, calm smile, cum on his stomach, " + MARK),
   # クロノム 技3（スロウの口づけ）
   "btl_m3":     ("tower", "under the stopped clock hands, he lies back in the horned demoness's arm, she kisses him slowly and deeply, tongues, saliva trail, two fingers of her other hand in his anus, fingering, a brass gear on a cord around his neck, cum dripping, " + MARK),
   "onani_m3":   ("castle", "sitting alone behind a stone pillar of the throne room, slowly sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, the horned demoness watches far away by the tall window, " + MARK),
   "inochi_m3":  ("gate", "at dawn by the chain fence, he stands on tiptoe held in the horned demoness's arms, an endless slow kiss, tongues, saliva, her hand under his coat behind him with fingers in his anus, fingering, his knees giving way, " + MARK),
   "onedari_m3": ("room", "he lies on one half of the wide soft bed, the horned demoness lies beside him holding his face, kissing him very slowly, tongues, saliva trail, her other hand between his legs with fingers deep in his anus, fingering, cum on his stomach, " + MARK),
   # リヤ（★魔王の魔力）
   "btl_e1":     ("castle", "he lies on the black carpet before the black throne, " + HANDS + " caressing his whole body, pinching both his nipples, two thin black fingers in his anus, the red-haired woman stands over him with arms crossed, triumphant grin, a black crystal on a cord at his neck, cum on his stomach, " + MARK),
   "onani_e1":   ("feast", "sitting alone on the floor behind the long table, a beer mug beside him, flushed, both his own hands stroking his chest and reaching behind to his own anus, penis untouched, the red-haired woman watches far away at the end of the hall, " + MARK),
   "inochi_e1":  ("tavern", "he sits slumped on a tavern bench, drunk and flushed, the red-haired woman sits on his lap feeding him ale mouth to mouth, kiss, ale dripping from his lips, black magic hands stroking his nipples under his shirt, empty mugs on the table, " + MARK),
   "onedari_e1": ("castle", "he kneels beside the black throne, ten " + HANDS[5:] + " wrapped around his body, pinching his nipples, the red-haired woman sits on the throne with her legs crossed looking down, smug grin, cum dripping untouched, " + MARK),
   # ナンシー（★強制催眠）
   "btl_e2":     ("cushion", "he lies limp in the cushions with his shirt open, the hypnotist kneels over him swinging a silver pendulum, her other hand slowly stroking his penis with her palm, whispering at his ear, a pendulum pendant around his neck, cum on his stomach, " + MARK),
   "onani_e2":   ("cushion", "lying alone buried in the cushions, breathing deeply, lips moving as he whispers to himself, one limp hand slowly stroking his own nipple, penis untouched, the hypnotist watches far away from the doorway, " + MARK),
   "inochi_e2":  ("cushion", "he sits on the cushions unable to stand, the hypnotist kneels behind him massaging his shoulders, her lips at his ear, one hand sliding down to stroke his nipple, an open door in the background, relaxed dazed face, cum dripping, " + MARK),
   "onedari_e2": ("cushion", "he lies with his head on the hypnotist's lap, she whispers into his ear and strokes his nipple slowly with her fingertips, a pendulum swinging above, a blank name tag without text on a ribbon at his neck, cum dripping untouched, " + MARK),
   # エイル（★呪具の搾取）
   "btl_e3":     ("eilhome", "he lies on his back on the straw bed, " + TENT + " around his wrists and ankles, tentacle tips sucking both his nipples, one thin tentacle tip in his anus, the adventurer leans over him with sharp golden eyes, wild grin, a blank notebook page without text beside them, cum on his stomach, " + MARK),
   "onani_e3":   ("forest", "sitting alone behind the log shelter, his wrists loosely tied with a cord, one finger in his own anus, penis untouched, breath white in the cold, the adventurer watches far away between the bare trees, " + MARK),
   "inochi_e3":  ("eilhome", "by the fireplace, he lies on the straw bed wrapped loosely in " + TENT + ", a tentacle tip sucking his nipple, one thin tip in his anus, the adventurer sits on the bed edge with her hand on his thigh, grinning, rice bales behind, cum dripping, " + MARK),
   "onedari_e3": ("eilhome", "on a bedding beside the rice bales, he lies with legs spread, three " + TENT + " around him, two tips sucking his nipples, one tip deep in his anus, the adventurer kneels beside him holding his knee, pleased grin, cum on his stomach, " + MARK),
   # スノウ（★瞬間凍結）
   "btl_boss":   ("snow2", "in the blizzard, he kneels with " + ICE + " and ankles, the swordswoman kneels behind him pinching his nipple with cold fingers, two fingers of her other hand in his anus, fingering, meltwater dripping from the ice, a snowflake crystal ornament at his collar, cum dripping, " + MARK),
   "onani_boss": ("icecave", "crouching alone behind an icicle pillar, pinching his own nipple with snow-chilled fingers, the other hand reaching behind with a finger in his own anus, penis untouched, white breath, the swordswoman watches far away across the frozen lake, " + MARK),
   "inochi_boss":("snow1", "he stands in a sword stance holding a wooden training sword, " + ICE + ", the swordswoman stands close pressing the hilt of her sheathed katana against his nipple, her cold fingers pinching the other, his knees trembling, cum dripping untouched, " + MARK),
   "onedari_boss":("icecave", "he lies on a fur rug on the ice, " + ICE + " slowly melting, held above his head, the swordswoman kneels beside him pinching his nipple with cold fingers, her other hand between his legs with a finger in his anus, fingering, meltwater, cum on his stomach, " + MARK),
 },
 "lose_desc": "keeps him forever in the room of stopped time as its resident, twelve glowing sigils covering the back of his left hand.",
 "onanie": {
   "master": ("clock", "crouching in the shadow of the gears, holding still, one hand on his own nipple, a wet finger pressing in his own anus, penis untouched, " + MARK),
   "e1": ("feast", "sitting behind the long table with a beer mug, both hands stroking his own chest and reaching behind to his own anus, penis untouched, " + MARK),
   "e2": ("cushion", "lying in the cushions breathing deeply, whispering to himself, slowly stroking his own nipple, penis untouched, " + MARK),
   "e3": ("forest", "sitting behind the log shelter, wrists loosely tied with a cord, a finger in his own anus, penis untouched, " + MARK),
   "boss": ("icecave", "crouching behind an icicle, pinching his own nipple with snow-chilled fingers, a finger in his own anus, penis untouched, " + MARK),
 },
 "magic": {
   "1": (None, "gate", "a white glove lying on black earth, above it five softly glowing sigils floating in the air, a heart, a spiral, a snowflake, a chain link and an hourglass, warm glow, close-up, without text"),
   "2": (None, "clock", "a huge bronze bell hanging beneath a great clock face without numerals, sound ripples in the air, turning gears, purple sky through an arch"),
   "3": (None, "icecave", "a row of long clear icicles hanging from the cave ceiling, pale icy white glow, cold mist drifting down, glittering frost"),
   "4": ("e2", "cushion", "holding out a swinging silver pendulum pendant toward the viewer, her other hand at her lips, gentle inviting smile"),
   "5": (None, "room", "a silent bedroom lined with hourglasses whose sand has stopped in midair, stopped clocks without numerals, a soft empty bed, soft thin silver chains on the pillow"),
 },
}
