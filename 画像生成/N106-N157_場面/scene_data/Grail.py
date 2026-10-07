# N137 女王封印の間（Grail）画像データ。登場人物は全員20歳以上。5人とも大人の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。原作に青・水色のキャラはいない（瞳は青系を避けて決めた）。
# 髪色：サディラス＝銀／ティア＝金／クレオパティス＝黒／パンシー＝橙がかった豹柄／タイムウィッチ＝茶。被りなし。
# 挿入技はない。後ろに入れるのは指だけ（サディラスとティア）なので pen は付けない。尻尾（パンシー）も撫でるだけ。
# ティアの斧は壁に立てかけてあるだけ（振るわない。tags には入れず、地下牢の場所タグに置く）。炎は熱くない（火傷・痛みなし）。
# ステージの男性ファンは描かない（3人以上を出さない。歓声は絵にしない）。絵には金の聖杯か胸元の印を必ず一つ入れる。
MARK = "a glowing golden chalice-shaped mark on his bare chest"
GRAIL = "a golden chalice"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary, fangs"
FIRE_NEG = "burn, burning skin, scorched, pain, " + SOFT_NEG
STAGE_NEG = "crowd, audience, multiple boys, " + SOFT_NEG
DATA = {
 "code": "Grail",
 "world": "dark fantasy kingdom ruled by a succubus queen, white castle under a dim sky, golden holy grail motif, faint golden glow, detailed background",
 "bg": "interior of a vast dark throne hall deep in a castle, a black throne on a stepped dais, a golden chalice shining on a stone pedestal beside the throne, shadows shaped like black wings on the floor, tall pillars, faint golden light, sweet haze, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "サディラス",
         "tags": "adult woman, mature female, mature face, sharp adult features, 30 years old, adult proportions, beautiful detailed eyes, tall, long legs, very long silver hair, straight hair, golden crown, crimson eyes, white and gold royal dress with the hem stained black, long gloves, large black feathered wings, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the silver-haired queen with black wings",
         "pose": "holding a golden chalice in one hand, the other hand on her hip, black wings half spread, haughty smirk, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "ティア",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, long blonde hair, straight hair, green eyes, silver bikini armor, metal pauldrons, metal gauntlets, armored boots, bare midriff, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the blonde warrior in bikini armor",
          "pose": "both arms open as if to embrace, chin raised, polite condescending smile, looking down at viewer",
          "neg": SOFT_NEG + ", swinging an axe, weapon raised"},
   "e2": {"type": "woman", "jp": "クレオパティス",
          "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, blunt bob cut, blunt bangs, golden circlet crown, amber eyes, eyeliner, sheer white egyptian dress, gold collar necklace, gold bracelets, golden staff, soft curvy feminine body, large breasts, wide hips",
          "name": "the black-bob ruin queen in a sheer dress",
          "pose": "sitting on an ancient stone chair with her legs crossed, holding a golden staff with a gentle flame at its tip, sly regal smile, looking down at viewer",
          "neg": FIRE_NEG},
   "e3": {"type": "woman", "jp": "パンシー",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, tall, long legs, orange-tan hair with dark leopard spots, medium wavy hair, leopard ears, yellow eyes, leopard tail, dancer outfit, leopard print bandeau top, sheer hip scarf with gold coins, gold anklets, bare midriff, slender curvy feminine body, large breasts, wide hips",
          "name": "the leopard-eared dancer",
          "pose": "dancing with one hand above her head and her hips swayed to the side, leopard tail curled, cheeky grin, winking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "タイムウィッチ",
            "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, light brown hair, loose wavy long hair, violet eyes, droopy eyes, purple witch hat, purple witch robe, white gloves, staff topped with a round clock ornament without numbers, soft voluptuous feminine body, large breasts, wide hips",
            "name": "the brown-haired witch with a clock staff",
            "pose": "holding a clock-topped staff loosely in both hands, head tilted, sleepy gentle smile, looking at viewer",
            "neg": SOFT_NEG},
 },
 "places": {
   "forest":    "entrance of a misty forest, dappled sunlight through the trees, damp earth, ferns",
   "stage":     "wooden stage built in a forest clearing at night, warm stage lights, mist, empty front row seat",
   "backstage": "inside a dressing tent, leopard print cloths hanging, a mirror with lamps, costumes on a rack",
   "ruin_gate": "entrance of desert ruins, sand, broken stone pillars, a few fallen feathers, dusk sky",
   "ruin_throne": "throne room of ancient ruins, an old stone chair, flame braziers, sheer curtains, incense haze",
   "ruin_under": "underground chamber of ancient ruins, cold stone walls with faded murals without text, candles",
   "bridge":    "long bridge over a deep mountain valley, wind, clouds, distant clock tower silhouette",
   "tent":      "cluttered tent on a mountain summit, many clocks without numbers on the shelves, floor cushions, tea set, warm lamp light",
   "castle_front": "front gate of a white castle, banners overlaid with a black crest without text, stone pillars, cold wind",
   "audience":  "castle audience chamber, an empty royal throne, red carpet, tall windows",
   "dungeon":   "castle dungeon, iron bars, cold stone floor, a soft straw bed, a battle axe leaning untouched against the wall, a ring of keys on a hook",
   "stairs":    "stone stairway outside a castle dungeon, torchlight, shadowed alcove, cold stone wall",
   "bedroom":   "royal bedroom of a castle, luxurious bed, a grand piano and piano bench, moonlight through a window",
   "grail_room": "hidden treasure chamber, a golden chalice on a stone pedestal, soft golden light, sweet haze",
   "seal":      "dark throne hall, black throne on a stepped dais, a golden chalice on a pedestal, shadows of black wings on the floor",
   "bed":       "canopy bed beside a black throne, dark silk sheets, a golden chalice on a bedside stand, golden glow",
 },
 "atk": {
   "m1": ("seal", "he kneels on the steps below the black throne holding " + GRAIL + " up in both hands, the queen sits on the throne above looking down at him, one finger pointing at the floor, his shirt open, " + MARK + ", knees trembling"),
   "m2": ("seal", "he stands before the throne wrapped in one black wing, the queen kisses him deeply, tongues, one gloved hand pinching his nipple, her other hand holding " + GRAIL + " against his lower belly, his shirt open, " + MARK + ", his legs trembling"),
   "m3": ("bed", "from side, he lies on the bed enclosed in both black wings, the queen leans over him kissing him deeply, tongues, saliva, two fingers of her hand in his anus, fingering, " + MARK + ", his hands gripping her feathers"),
   "e1": ("dungeon", "he stands in the cell hugged tightly from the front, the blonde warrior presses his face into her breasts, cold armor against his bare chest, one of her oiled fingers in his anus, fingering, he shivers, " + MARK + ", her smile looking down"),
   "e2": ("ruin_throne", "he sits sideways on the lap of the ruin queen on the stone chair, staring at the gentle flame at the tip of her staff, the ruin queen whispers in his ear, her fingers stroking his nipple, his shirt open, " + MARK + ", flushed skin"),
   "e3": ("stage", "he sits on the front row seat with his hands clasped behind his back, the dancer dances right in front of him with swaying hips, her leopard tail stroking his nipple, his shirt open, " + MARK + ", he stares up unable to look away", {"neg": STAGE_NEG}),
   "boss": ("tent", "he sits frozen on a floor cushion, the witch kneels beside him raising her clock staff, a faint glowing clock circle without numbers in the air, her white-gloved fingers stroking his nipple and his penis, " + MARK + ", sleepy gentle smile"),
 },
 "atk_desc": {
   "m1": "the queen makes him kneel and hold up the grail with a single command from her throne.",
   "m2": "the queen kisses him inside her wing and catches his release in the golden grail.",
   "m3": "the queen seals his lips inside her black wings while pressing inside him with her fingers.",
   "e1": "the warrior hugs him against her cold armor and warm breasts and does not let go.",
   "e2": "the ruin queen makes him stare into her painless flame and whispers that he belongs to her.",
   "e3": "the dancer forbids him to touch and teases him with her tail while she dances.",
   "boss": "the witch stops time and strokes him while he cannot finish.",
 },
 "lose": {
   # サディラス 技1（エビルテンプテーション）
   "btl_m1":     ("seal", "he kneels deeply on the steps holding " + GRAIL + " up in both hands, the queen stands over him with wings spread, one hand lifting his chin, her other hand pinching his nipple, a gold chalice pendant on his neck, " + MARK + ", cum dripping into the chalice"),
   "onani_m1":   ("grail_room", "kneeling alone before the pedestal with one palm held out as an offering, the other hand stroking his own nipple, shirt open, " + MARK + ", penis untouched, the queen watches far away from a hidden doorway"),
   "inochi_m1":  ("audience", "he stands on the red carpet with his knees giving way, the queen holds " + GRAIL + " at his hips with one hand, her other hand stroking his penis, handjob, her lips at his ear, " + MARK + ", cum dripping into the chalice"),
   "onedari_m1": ("seal", "he kneels low on the step beside the black throne holding " + GRAIL + " up, the queen sits on the throne leaning down to kiss him, her fingers rolling his nipple, " + MARK + ", his eyes hidden, trembling, cum dripping"),
   # サディラス 技2（★聖杯への献上）
   "btl_m2":     ("seal", "he stands wrapped in a black wing before the throne, the queen kisses him deeply, tongues, one hand holding " + GRAIL + " under his penis, two fingers of her other hand in his anus, fingering, " + MARK + ", cum dripping into the chalice"),
   "onani_m2":   ("bedroom", "sitting alone on the piano bench hugging a plain metal cup to his chest, one hand stroking his own nipple, the other hand reaching behind to touch his own anus, " + MARK + ", penis untouched, the queen watches far away by the piano"),
   "inochi_m2":  ("grail_room", "he kneels at the pedestal holding a polishing cloth, the queen kneels behind him with one wing around him, kissing his neck, her fingers in his anus, fingering, her other hand pinching his nipple, " + GRAIL + " before him, " + MARK + ", cum dripping"),
   "onedari_m2": ("bed", "he lies on his back on the canopy bed with knees raised, the queen sits beside him, two fingers in his anus, fingering, her other hand rolling his nipple, " + GRAIL + " on the stand beside them, " + MARK + ", counting smirk, cum on his stomach"),
   # サディラス 技3（黒翼の抱擁）
   "btl_m3":     ("bed", "from side, he lies on the bed fully enclosed in black wings, the queen over him kissing him deeply, tongues, saliva trail, two fingers in his anus, fingering, " + GRAIL + " held at his hips, a black feather in his hand, " + MARK + ", cum dripping"),
   "onani_m3":   ("castle_front", "sitting alone behind a gate pillar wrapped in his cloak, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, " + MARK + ", penis untouched, the queen watches far above in the sky"),
   "inochi_m3":  ("seal", "morning light, he lies curled beside the black throne inside half-open black wings, the queen holds him from behind kissing his cheek, her fingers in his anus, fingering, " + GRAIL + " on the pedestal, " + MARK + ", sleepy and flushed"),
   "onedari_m3": ("bed", "from side, he lies on one half of the canopy bed wrapped tightly in black wings, the queen embraces him kissing him deeply, her hand between his legs from behind with fingers in his anus, fingering, " + GRAIL + " on the stand, " + MARK + ", cum dripping"),
   # ティア（★抱き着き攻撃）
   "btl_e1":     ("dungeon", "he stands in the cell hugged tightly from the front, the blonde warrior presses his face into her breasts, two oiled fingers in his anus, fingering, cold armor on his bare chest, an armor clasp on a cord around his neck, " + MARK + ", cum dripping untouched"),
   "onani_e1":   ("stairs", "crouching alone in the shadowed alcove, pressing a cold flat piece of armor plate against his bare chest, rubbing his own nipple with it, shivering, " + MARK + ", penis untouched, the blonde warrior watches far away from the top of the stairs"),
   "inochi_e1":  ("dungeon", "he reaches one hand toward a ring of keys, the blonde warrior hugs him from the front holding the keys behind her back, his face against her breasts, her finger in his anus, fingering, " + MARK + ", his other arm around her waist"),
   "onedari_e1": ("dungeon", "he lies on the soft straw bed, the blonde warrior lies over him hugging him tightly, his face buried in her breasts, two oiled fingers in his anus, fingering, " + MARK + ", her smile looking down, cum dripping"),
   # クレオパティス（★ブレインウォッシュ）
   "btl_e2":     ("ruin_throne", "he sits on the lap of the ruin queen on the stone chair, staring into the gentle flame of her staff, the ruin queen whispers in his ear and rolls his nipple, a gold crown charm on his neck, " + MARK + ", flushed skin, cum dripping untouched", {"neg": FIRE_NEG}),
   "onani_e2":   ("ruin_under", "sitting alone before the mural, staring into a candle flame, stroking his own nipple with his fingertips, shirt open, " + MARK + ", penis untouched, the ruin queen watches far away from the dark corridor"),
   "inochi_e2":  ("ruin_gate", "he stands among the broken pillars staring at the flame of her staff, the ruin queen sits on a fallen pillar beside him, one hand holding the staff, her other hand stroking his nipple, " + MARK + ", his feet not moving, dusk", {"neg": FIRE_NEG}),
   "onedari_e2": ("ruin_throne", "he sits on the floor at the foot of the stone chair leaning back against her knees, the ruin queen sits above whispering down to him, her fingers pinching his nipple, the staff flame before his face, " + MARK + ", cum dripping untouched", {"neg": FIRE_NEG}),
   # パンシー（★セクシーダンス）
   "btl_e3":     ("stage", "he kneels on the wooden stage with his hands clasped behind his back, the dancer dances close grinding her hip against his thigh, her leopard tail stroking his nipple, a leopard print ribbon tied on his wrist, " + MARK + ", cum dripping untouched", {"neg": STAGE_NEG}),
   "onani_e3":   ("backstage", "sitting alone behind a hanging leopard print cloth with his hands clasped behind his back, swaying his hips without touching himself, " + MARK + ", penis untouched, the dancer watches far away at the tent entrance"),
   "inochi_e3":  ("stage", "he sits on the front row seat clapping his hands, the dancer leans down from the stage edge, her leopard tail stroking his nipple, her finger on her lips, stage lights, his shirt open, " + MARK + ", dazed smile", {"neg": STAGE_NEG}),
   "onedari_e3": ("stage", "he sits on the front row seat with his hands clasped behind his back, the dancer spins fast in front of him, motion blur on her scarf, her leopard tail flicking his nipple quickly, " + MARK + ", cum dripping untouched", {"neg": STAGE_NEG}),
   # タイムウィッチ（★時間差射精）
   "btl_boss":   ("tent", "he sits on a floor cushion arching his back, the witch kneels beside him swinging her clock staff forward, a glowing clock circle without numbers spinning in the air, her gloved hand around his penis, handjob, " + MARK + ", a lot of cum, a clock hand charm on his wrist"),
   "onani_boss": ("bridge", "crouching alone at the foot of the bridge, staring at a pocket watch without numbers in one hand, the other hand reaching behind with a finger pressed at his own anus, " + MARK + ", penis untouched, the witch watches far away on the bridge"),
   "inochi_boss":("tent", "he sits frozen on a cushion at a low tea table, the witch sits beside him holding a teacup in one hand, her other gloved finger stroking his nipple, a glowing clock circle without numbers above them, " + MARK + ", steam of tea stopped in the air"),
   "onedari_boss":("tent", "he sits on a cushion before a large clock without numbers, the witch hugs him from behind, her gloved fingers rolling both his nipples, her staff leaning on her shoulder, a glowing clock circle in the air, " + MARK + ", a lot of cum untouched"),
 },
 "lose_desc": "keeps him beside the queen's throne forever as the one who fills the golden grail, the chalice mark on his chest shining full gold.",
 "onanie": {
   "master": ("seal", "kneeling, hugging a plain metal cup to his chest, one hand stroking his own nipple, the other hand reaching behind to touch his own anus, " + MARK + ", penis untouched"),
   "e1": ("stairs", "crouching, pressing a cold flat armor plate to his bare chest and rubbing his own nipple, shivering, " + MARK + ", penis untouched"),
   "e2": ("ruin_under", "sitting, staring into a candle flame while stroking his own nipple, " + MARK + ", penis untouched"),
   "e3": ("backstage", "sitting with his hands clasped behind his back, swaying his hips without touching himself, " + MARK + ", penis untouched"),
   "boss": ("bridge", "crouching, staring at a pocket watch without numbers, a finger of the other hand pressed at his own anus, " + MARK + ", penis untouched"),
 },
 "magic": {
   "1": (None, "grail_room", "a glowing golden chalice-shaped emblem floating in the air, filled two thirds with golden light from the bottom, soft sparkles, close-up"),
   "2": ("m", "seal", "sitting on the black throne with her legs crossed, laughing proudly with her head tilted back, one hand raised, black wings spread"),
   "3": ("e2", "ruin_throne", "sitting on the stone chair, raising her golden staff, a gentle warm painless flame swirling softly around her like a veil, sly smile"),
   "4": (None, "stage", "an empty wooden stage in a forest clearing at night, warm spotlights crossing in the mist, a sheer scarf with gold coins left on the stage floor"),
   "5": (None, "seal", "a golden chalice shining on a stone pedestal, a single golden drop falling into it, sweet golden haze, black feathers on the floor, close-up"),
 },
}
