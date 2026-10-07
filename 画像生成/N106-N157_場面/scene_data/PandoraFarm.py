# N114 パンドラ牧場（PandoraFarm）画像データ。登場人物は全員20歳以上。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。女性の責め手に筋肉の線は描かない。
# 髪色の書き分け：パンドラ＝deep magenta-purple／メロエ＝light pink／従業淫B＝pale lavender／従業淫A＝pale mint／応援警備淫＝black。
# 従業淫A：原作は青い髪 → pale mint hair に置き換え（瞳は amber）。
# イゼヴェル：原作は青いボブ・青い尻尾 → 立ち絵の添え書きでは pale turquoise-white bob と書き、尻尾は書かない。
# 応援警備淫：原作は青い制帽 → 主人公の紺髪と紛れないよう slate-grey の制帽にした（髪は黒）。
# boss は2人で1枚のカード。主になる1人は挿入役のメロエ（ピンクの長髪・黒いベレー帽・鞭）。立ち絵だけイゼヴェルを横に描く。
#   技CG・敗北CGは「3人以上を出さない」ため、メロエ1人が淫針（刺さらない注射器）・冷たい霧・化粧・鞭まで受け持つ形に置き換えた。
# ふたなりの挿入（pen: penis）は パンドラの災厄の抽送（atk m3・btl_m3・onedari_m3）と メロエの躾ピストン（atk boss・btl_boss・onedari_boss）だけ。
#   検品・女装魔法・確保は指まで（pen なし）。全身愛撫魔法の見えない手は入口を撫でるだけ。警棒は服の上からつつくだけ。
# 淫針は刺さらない（丸い先が触れるだけ）、鞭は撫でるだけ、冷たい霧は冷えるだけ、手錠は内側が柔らかい。傷・流血なし。
# 主人公の女装は hero_outfit（体は変えない・平らな胸）。首には黒い天鵞絨の首輪（宝石）。名札・記録・肖像画に文字は描かない。
P = "penis"
COL = "a black velvet choker set with colorful gems around his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
NEEDLE = "a glass syringe with a soft round tip touching his nipple without piercing"
NEEDLE_NEG = "needle piercing skin, injection, stabbed, wound, whip marks, welts, bruise, scary"
HANDS = "many translucent hands made of pale magic light"
CUFF = "his wrists held behind his back in soft padded cuffs"


def O(outfit, **kw):
    d = {"hero_outfit": outfit}
    d.update(kw)
    return d


DATA = {
 "code": "PandoraFarm",
 "world": "grand mansion deep in a forest, polished floors and red carpets, crystal chandeliers, floating colorful gems, perfume haze, soft purple and gold light, detailed background",
 "bg": "vast entrance hall of a grand mansion deep in a forest, high open atrium, a huge crystal chandelier, a long red carpet over a polished floor, a grand staircase, tall windows with dark trees outside, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "パンドラ＝ナハト",
         "tags": "adult woman, mature female, mature face, elegant adult features, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, deep magenta-purple hair, very long hair, purple hairband, yellow curled horns, red eyes, pink ball gown dress, long purple gloves, soft purple tentacle-like tails behind her, colorful gems floating around her, soft curvy feminine body, huge breasts, wide hips",
         "name": "the horned lady in a pink dress",
         "pose": "holding an ornate jewel box in both gloved hands, graceful gentle smile, looking at viewer with red eyes",
         "neg": SOFT_NEG + ", scary, slimy"},
   "e1": {"type": "woman", "jp": "従業淫B",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, pale lavender hair, medium hair, violet eyes, black witch hat, black robe, swirling violet smoke magic around her hands, soft curvy feminine body, large breasts",
          "name": "the lavender-haired witch in a black robe",
          "pose": "twirling with one hand raised and the hem of her robe flaring, violet smoke curling from her fingertips, bright cheerful open smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "従業淫A",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale mint hair, medium hair, amber eyes, glasses, black witch hat, black jacket, black skirt, bat wings, slender red tail, holding a broom, slender curvy feminine body, large breasts",
          "name": "the bespectacled witch in a black jacket",
          "pose": "adjusting her glasses with one finger, an open blank book without text in her other hand, a broom leaning on her shoulder, polite gentle smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "応援警備淫",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, black hair, medium hair, grey eyes, slate-grey police cap with dog ears, police officer uniform, thin white gloves, baton with a round tip at her belt, dog tail, slender curvy feminine body, medium breasts",
          "name": "the black-haired officer in a police cap",
          "pose": "standing straight, one hand resting on the baton at her belt, the other hand holding soft padded cuffs, quiet expressionless face, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "メロエ（＆イゼヴェル）",
            "tags": "adult woman, mature female, mature face, sharp adult features, 25 years old, adult proportions, beautiful detailed eyes, tall, long legs, light pink hair, very long straight hair, black beret, red eyes, black bolero jacket, black corset dress, fishnet tights, long black boots, slender demon tail, holding a riding whip, slender curvy feminine body, large breasts",
            "name": "the pink-haired trainer in a black beret",
            "pose": "holding a coiled riding whip in one hand, calm flat expression, looking at viewer, standing beside a second adult woman with a pale turquoise-white bob, lavender skin, pointed ears, a nurse cap and a pink nurse dress who holds a glass syringe and smirks",
            "neg": SOFT_NEG + ", " + NEEDLE_NEG},
 },
 "places": {
   "entrance": "mansion entrance hall, high atrium, crystal chandelier, red carpet, marble wall",
   "guard":    "guard station beside the entrance hall, a plain wooden chair, a desk, a key rack without text, warm lamp",
   "corridor": "long mansion corridor, rows of framed portraits without text, thick red carpet, wall lamps, perfume haze",
   "clinic":   "mansion infirmary, white curtains, a white bed, shelves of glass medicine bottles without labels, soft daylight",
   "dining":   "open dining hall, a long table with sweets and tea sets, tall candlesticks, white tablecloth",
   "staff":    "staff floor dressing area, tall mirrors, a vanity table with makeup, a velvet chair, broom stand",
   "wardrobe": "wardrobe room, long racks of dresses, shelves of silk lingerie and stockings, a tall standing mirror, soft fabric everywhere",
   "gallery":  "painting gallery corridor, ornate gilded frames, spotlights, polished floor",
   "showroom": "quiet exhibition room, glass display cases, a round velvet pedestal under a spotlight, a blank nameplate without text",
   "auction":  "auction hall, tiers of empty seats, an auction stand with a wooden gavel, red curtains",
   "hall":     "second floor central hall, a grand staircase, balustrade, faint music box melody in the air",
   "exec":     "third floor private corridor, thin red sensor light beams, a vanity table with a mirror, racks of soft whips, dim violet lamps",
   "training": "training room, a padded restraint bench, mirrored walls, a rack of soft riding whips, pink lamp light",
   "pandora":  "top floor chamber, purple curtains around a wide bed, gems floating in the air, a jeweled music box, crystal walls, a glass display stand",
   "box":      "alcove with a large ornate treasure box on a dais, purple drapes, faint pink glow leaking from the lid",
   "balcony":  "night balcony overlooking a dark forest, stone balustrade, a cushioned chair, moonlight, night breeze",
 },
 "atk": {
   "m1": ("pandora", "he kneels on the carpet before the purple curtains, the horned lady bends over him holding an ornate jewel box opened a crack under his face, sweet pink vapor drifting into his nose and mouth, her gloved hand lifting his chin, gems floating around them, " + COL + ", dazed, knees trembling"),
   "m2": ("showroom", "he lies on his back on the velvet pedestal, the horned lady leans over him pinching and rolling his nipple with purple-gloved fingers, two oiled bare fingers of her other hand in his anus, fingering, her soft purple tail stroking his inner thigh, appraising smile, " + COL),
   "m3": ("pandora", "from side, he lies on his back on the bed inside the purple curtains with legs spread, the horned lady between his legs holding him, her penis in his anus, anal, kissing him deeply, tongues, saliva, her soft purple tail brushing his nipple, his own penis separate, " + COL, {"pen": P}),
   "e1": ("wardrobe", "he stands before the tall mirror wrapped in swirling violet smoke, the witch stands close behind him, stroking his nipple through the dress with one hand, her other hand under his skirt with fingers in his anus, fingering, cheerful grin, " + COL,
          O("a frilled white dress with silk lingerie and white stockings, the skirt lifted at the back")),
   "e2": ("clinic", "he lies on his back on the white bed, " + HANDS + " caress his ear, neck, nipples, sides, inner thighs and the entrance of his anus all at once, avoiding his penis, the bespectacled witch stands beside the bed without touching him, writing in a blank book without text, " + COL),
   "e3": ("entrance", "he stands pressed chest-first against the marble wall, " + CUFF + ", the officer presses against his back, one hand rubbing his nipple through his shirt, the gloved fingers of her other hand in his anus, fingering, expressionless, " + COL),
   "boss": ("training", "from side, he lies face down over the padded restraint bench, wrists in soft cuffs, the pink-haired trainer stands behind him, her penis in his anus, anal, reaching around with " + NEEDLE + ", cool white mist on his wrists, his own penis separate, " + COL, {"pen": P}),
 },
 "atk_desc": {
   "m1": "the horned lady opens her box a crack and lets him breathe the sweet vapor that melts his resistance.",
   "m2": "the horned lady inspects him like a gem, rolling his nipple and polishing deep inside with oiled fingers.",
   "m3": "the horned lady takes him from the front inside the curtains while sealing his lips with a deep kiss.",
   "e1": "the witch changes his clothes into a dress with smoke magic and teases him through it.",
   "e2": "the bespectacled witch has invisible hands caress his whole body at once while she only takes notes.",
   "e3": "the officer cuffs his hands behind him, pins him to the wall and searches him thoroughly.",
   "boss": "the trainer disciplines him from behind on the bench while a harmless syringe tip teases his nipple.",
 },
 "lose": {
   # パンドラ 技1（パンドラウイルス＋検品）
   "btl_m1":     ("pandora", "he kneels on the carpet leaning back against the horned lady, the open jewel box held under his face, pink vapor filling his breath, her gloved fingers pinching his nipple, two oiled fingers in his anus under the lifted skirt, fingering, gems floating, " + COL + ", cum dripping untouched",
                  O("a pink ball gown dress matching hers with white silk lingerie, the hem lifted")),
   "onani_m1":   ("corridor", "kneeling alone under the portraits, holding a perfume bottle to his nose and breathing it in, the other hand stroking his own nipple and reaching behind to his anus, penis untouched, " + COL + " glowing, the horned lady watches far away down the corridor"),
   "inochi_m1":  ("balcony", "he sits on the cushioned chair facing the dark forest, the horned lady stands behind the chair holding the open box near his face, pink vapor in the night breeze, her gloved hand inside the nightgown on his nipple, her soft purple tail between his thighs, " + COL + ", dazed",
                  O("a white lace nightgown and white stockings")),
   "onedari_m1": ("pandora", "he sits at a tea table looking up, the horned lady sits beside him holding the box wide open before his face, thick pink vapor, her fingers under his skirt in his anus, fingering, teacups, gems floating, " + COL + ", cum dripping",
                  O("a pale purple tea dress, the skirt lifted on one side")),
   # パンドラ 技2（★宝石の検品）
   "btl_m2":     ("showroom", "he lies on his back on the velvet pedestal under the spotlight, the horned lady leans over him rolling his nipple with gloved fingers, two oiled fingers pressing deep in his anus, fingering, her soft purple tail stroking his side, a blank nameplate without text on the pedestal, " + COL + ", cum on his stomach",
                  O("a white display dress with silk lingerie, the bodice opened and the hem lifted")),
   "onani_m2":   ("staff", "sitting alone on the velvet chair before a tall mirror, tracing the gems of his choker with one fingertip, the other hand rubbing his own nipple in slow circles, hips shifting, penis untouched, the horned lady reflected far away in the mirror watching"),
   "inochi_m2":  ("gallery", "he stands with his hands on the wall beside a gilded frame, the horned lady behind him pinching his nipple through the opened bodice, her oiled fingers in his anus under the lifted skirt, fingering, a portrait of a figure in a red dress without text, " + COL + ", legs trembling, cum dripping",
                  O("a deep red dress matching the portrait frames, the bodice opened")),
   "onedari_m2": ("pandora", "he lies on his back on the wide bed with arms open, the horned lady sits beside him, both gloved hands on his nipples, her soft purple tail pressing into his anus, one more tail stroking his thigh, counting smile, morning light, " + COL + ", cum on his stomach",
                  O("a thin lace dress and lace lingerie, the lingerie pulled aside")),
   # パンドラ 技3（災厄の抽送）
   "btl_m3":     ("pandora", "from side, he lies on his back on the bed inside the purple curtains with legs lifted, the horned lady over him holding his waist, her penis in his anus, anal, kissing him deeply, tongues, saliva trail, her tail on his nipple, a large purple gem in the center of his choker, his own penis separate, cum on his stomach",
                  O("a purple evening gown, the long skirt rolled up to his waist", pen=P)),
   "onani_m3":   ("wardrobe", "kneeling alone between the racks of dresses, biting the hem of the dress he wears, one hand reaching behind with a finger deep in his own anus, penis untouched, " + COL + " glowing, the horned lady watches far away from between the dresses",
                  O("a borrowed pale dress, the hem held in his teeth")),
   "inochi_m3":  ("box", "he sits on the horned lady's lap before the large ornate box, the horned lady holding him from behind, one gloved hand on his nipple, two oiled fingers in his anus, fingering, his own hand reaching out to lift the lid of the box, pink glow, " + COL + ", cum dripping",
                  O("a black lace dress and long black gloves, the skirt lifted")),
   "onedari_m3": ("pandora", "from side, he lies on his back on the bed inside the purple curtains, his arms around the horned lady's neck, the horned lady over him, her penis deep in his anus, anal, kissing him deeply, lips sealed, his own penis separate, cum on his stomach, " + COL,
                  O("a white silk nightgown, the hem rolled up", pen=P)),
   # 従業淫B（★女装魔法）
   "btl_e1":     ("wardrobe", "he stands before the tall mirror holding his own skirt hem, violet smoke swirling, the witch behind him stroking his nipple through the dress, her other hand under the skirt with two fingers in his anus, fingering, a witch hat ornament pinned on the dress, " + COL + ", cum dripping under the skirt",
                  O("a frilled white dress with silk lingerie and white stockings")),
   "onani_e1":   ("wardrobe", "standing alone before the tall mirror after a twirl, the skirt still flaring, one hand reaching under his own skirt behind to his anus, penis untouched, " + COL + " glowing, the witch peeks far away from behind a rack of dresses",
                  O("a light blue dress he put on by himself")),
   "inochi_e1":  ("dining", "he stands beside the long table gripping its edge, violet smoke fading around the dress, the witch behind him rolling his nipple through the dress, her fingers under his skirt in his anus, fingering, sweets and teacups on the table, " + COL + ", knees trembling, cum dripping",
                  O("a pink dress with a full skirt and white stockings")),
   "onedari_e1": ("wardrobe", "he sits on a cushioned stool looking up, the witch dances close in front of him with her robe hem flaring, bending to stroke his nipple through the dress, her other hand under his skirt with fingers in his anus, fingering, laughing, " + COL + ", cum dripping",
                  O("a pink dress with matching lingerie and stockings")),
   # 従業淫A（★全身愛撫魔法）
   "btl_e2":     ("clinic", "he lies on his back on the white bed arching, " + HANDS + " caress his ears, neck, nipples, sides, inner thighs and the entrance of his anus at once, avoiding his penis, the bespectacled witch stands beside the bed adjusting her glasses and writing in a blank book without text, " + COL + ", cum on his stomach untouched",
                  O("a thin white nightdress and silk lingerie, the hem lifted")),
   "onani_e2":   ("clinic", "lying alone on the white bed behind the curtain, one hand stroking his own ear, the other hand rubbing his own nipple, legs shifting restlessly, penis untouched, " + COL + " glowing, the bespectacled witch watches far away through a gap in the white curtain"),
   "inochi_e2":  ("clinic", "he lies on the white bed, " + HANDS + " stroking his whole body, a soft green healing glow from the bespectacled witch's raised palm over his belly, she holds a blank book without text, he trembles on the edge, " + COL,
                  O("a white lace nightdress and white stockings, the hem lifted")),
   "onedari_e2": ("clinic", "he lies on his side on the white bed, ten " + HANDS[5:] + " covering his ear, nipples and the entrance of his anus, avoiding his penis, the bespectacled witch sits on a stool beside the bed with a pen and a blank book without text, gentle smile, " + COL + ", cum dripping untouched",
                  O("a pale sky-colored nightdress, the hem lifted")),
   # 応援警備淫（★確保）
   "btl_e3":     ("entrance", "he stands pressed chest-first against the marble wall, " + CUFF + ", the officer presses against his back, one hand on his nipple over the dress, two gloved fingers of her other hand in his anus under the lifted skirt, fingering, expressionless, " + COL + ", cum dripping",
                  O("a plain black one-piece dress and white lingerie, the skirt lifted at the back")),
   "onani_e3":   ("corridor", "standing alone in the shadow of a pillar, both hands clasped behind his own back, pressing his chest and hips against the wall, rubbing his nipples on the wall through his shirt, penis untouched, " + COL + " glowing, the officer watches far away down the corridor"),
   "inochi_e3":  ("entrance", "he walks unsteadily along the red carpet toward a closed door, the officer walks behind him prodding his rear lightly over the dress with the round tip of her baton, her other hand on his shoulder, " + CUFF + ", " + COL + ", knees trembling",
                  O("a black dress worn like a cloak")),
   "onedari_e3": ("guard", "he sits on the plain wooden chair leaning forward, " + CUFF + ", the officer stands behind the chair, one gloved hand searching his nipple over the dress, two gloved fingers of her other hand in his anus, fingering, a ring of keys at her belt, " + COL + ", cum dripping",
                  O("a uniform-style one-piece dress with a collar, the skirt lifted at the back")),
   # イゼヴェル＆メロエ（★調教師の二人がかり）— 絵はメロエ1人
   "btl_boss":   ("training", "from side, he lies face down over the padded restraint bench, wrists in soft cuffs, the pink-haired trainer stands behind him holding his hips, her penis in his anus, anal, " + NEEDLE + ", cool white mist on his wrists, makeup on his face, a silver whip-shaped charm on his choker, his own penis separate, cum dripping",
                  O("a black babydoll and garter stockings, lipstick and blush on his face", pen=P)),
   "onani_boss": ("exec", "sitting alone at the vanity table, clumsy lipstick smeared on his own lips, staring at himself in the mirror, one hand rubbing his own nipple, the other hand reaching behind to his anus, penis untouched, thin red sensor light on his shoulder, the pink-haired trainer watches far away from the corridor"),
   "inochi_boss":("exec", "he stands frozen mid-step among thin red light beams, cool white mist around his legs, the pink-haired trainer stands behind him stroking his back softly with the riding whip, her other hand holding " + NEEDLE + ", " + COL + ", hips raised, trembling",
                  O("a black bolero, a short skirt and fishnet tights matching hers")),
   "onedari_boss":("training", "from side, he kneels on all fours on the padded bench facing a mirrored wall, the pink-haired trainer kneels behind him, her penis in his anus, anal, counting calmly, two glass syringes with soft round tips resting against his nipples without piercing, his own penis separate, cum dripping, " + COL,
                  O("a black and pink dress, the skirt flipped up, lipstick and blush on his face", pen=P)),
 },
 "lose_desc": "keeps him in the mansion forever as a cherished jewel on display, a black velvet choker set with twelve gems around his neck.",
 "onanie": {
   "master": ("corridor", "kneeling in the shadow of a portrait, tracing the gems of his choker with one fingertip, the other hand rubbing his own nipple in slow polishing circles, an oiled finger reaching behind to his own anus, penis untouched"),
   "e1": ("wardrobe", "standing before the tall mirror in a dress after a twirl, one hand reaching under his own skirt behind to his anus, penis untouched", O("a light blue dress he put on by himself")),
   "e2": ("clinic", "lying on the white bed, one hand stroking his own ear, the other hand rubbing his own nipple, trying to touch everywhere at once, penis untouched"),
   "e3": ("corridor", "standing with both hands clasped behind his own back, pressing his chest and hips against the wall, hips rocking, penis untouched"),
   "boss": ("exec", "sitting at the vanity table with lipstick on his own lips, looking into the mirror, one hand rubbing his own nipple, the other hand reaching behind to his anus, penis untouched"),
 },
 "magic": {
   "1": (None, "pandora", "a black velvet choker set with two freshly glowing gems resting on a purple cushion, soft sparkles, close-up"),
   "2": (None, "auction", "a polished wooden auction gavel and its sound block on the auction stand, a faint ripple of sound in the air, close-up, stand without text"),
   "3": (None, "exec", "thin red light beams crossing a dim corridor, cool white mist drifting down from the ceiling, sparkling frost-like glitter in the air"),
   "4": (None, "clinic", "a glass syringe with a very fine soft tip filled with honey-pink liquid lying on a silver tray, one glistening drop, close-up, bottles without labels"),
   "5": ("m", "pandora", "winding the key of a jeweled music box held in her gloved hands, gems floating around her, musical sparkles, gentle smile"),
 },
}
