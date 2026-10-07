# N143 吸血鬼の魔城（VampCastle）画像データ。登場人物は全員20歳以上（吸血鬼は何百年も生きている大人。見た目の年齢で書く）。5人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない（剣士・騎士も曲線のある体つき）。
# エルダーとコンキスタはどちらも原作は金髪 → 同じMOD内で髪色が被らないよう、エルダー＝platinum blonde（長いストレート）／コンキスタ＝honey blonde（低い位置の一つ結び）に分けた。
# 瞳に青・水色は使わない（赤・すみれ色・琥珀・金）。ヴァンパイアの肌は紫（pale purple skin）。
# 吸血は痛くない：牙は肌を破らない。唇を当てて甘く吸うだけ。血・傷・噛み跡は描かない。主人公の首筋には小さな赤い点が二つ一組の印。
# 挿入はエルダーの柔らかいピンクの触手と指だけ（必ずほぐした後。触手なので pen なし）。ほかの4人は後ろに触れない。剣・太刀は抜かない。
# ヴェンデッタは赤い椅子から立たない（どの絵も座ったまま。主人公が足元に来る）。コンキスタのコウモリは小さく丸い（噛まない）。
MARK = "pairs of tiny red dots on his neck"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, blood, bite wound, biting, bleeding, wound, scary, horror"
TENT = "soft smooth pink tentacles"
TENT_NEG = "scary tentacles, spikes, thorns, slimy monster, teeth on tentacles, gore"
DATA = {
 "code": "VampCastle",
 "world": "gothic vampire castle in a land of cold mist at night, stone walls, red carpets and black curtains, flickering candles, red moon through tall windows, detailed background",
 "bg": "empty throne room of a gothic vampire castle at night, a vacant ornate throne with a red mantle draped over it, long red carpet, black curtains, silver candelabra with lit candles, tall arched windows showing a red moon and drifting mist, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "エルダーヴァンパイア",
         "tags": "adult woman, mature female, mature face, sharp adult features, 32 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, platinum blonde hair, very long straight hair, bat wing hair ornaments, red eyes, pointy ears, long black cloak with a high collar, black gothic dress, several soft smooth pink tentacles extending from behind her back, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the platinum-blonde elder vampire in a black cloak",
         "pose": "arms crossed under her chest, chin raised, pink tentacles swaying gently behind her, haughty faint smile, looking down at viewer with red eyes",
         "height_note": "she is much taller than him",
         "neg": SOFT_NEG + ", " + TENT_NEG},
   "e1": {"type": "woman", "jp": "コンキスタ",
          "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, honey blonde hair, low ponytail, amber eyes, pointy ears, white dress shirt, grey skirt, black cape with red lining, black knee boots, sheathed sword at her hip, small round black bats flying around her, soft curvy feminine body, large breasts",
          "name": "the honey-blonde vampire knight in a black and red cape",
          "pose": "standing straight with one hand resting on the hilt of her sheathed sword, a small bat perched on her shoulder, stern composed face, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG + ", drawn sword, bare blade"},
   "e2": {"type": "woman", "jp": "ヴェンデッタ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, black hair, long wavy hair, glowing purple eyes, pointy ears, long black gothic dress with a wide trailing hem, black lace, fishnet pantyhose, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the black-haired vampire sorceress in a long black dress",
          "pose": "sitting in a red velvet armchair with her legs crossed, chin resting on one hand, an open spellbook without text on her lap, cool appraising smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "ヴァンパイア",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, colored skin, pale purple skin, ash grey hair, medium hair, golden eyes, pointy ears, black evening dress with a deep neckline, black choker, soft voluptuous feminine body, huge breasts",
          "name": "the purple-skinned grey-haired vampire gatekeeper in a black dress",
          "pose": "leaning forward with both arms open as if to embrace, a large iron key hanging at her waist, cheerful inviting smile, looking at viewer",
          "height_note": "she is much taller than him",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "カーミラ",
            "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, pale skin, pink hair, very long hair, violet eyes, pointy ears, black bat wings on her back, long night-colored black cloak, black bodysuit, sheathed katana at her hip, soft voluptuous feminine body, huge breasts, wide hips",
            "name": "the pink-haired vampire swordswoman in a night-colored cloak",
            "pose": "holding one side of her dark cloak open with one hand, the other hand resting on her sheathed katana, gentle calm smile, looking at viewer",
            "height_note": "she is much taller than him",
            "neg": SOFT_NEG + ", drawn sword, bare blade"},
 },
 "places": {
   "mist":     "wasteland of cold thick mist at night, bare dead trees, a distant castle spire, unseen path",
   "gate":     "castle gate at night, tall iron gate, stone gargoyle statues, drifting mist, a small gatehouse beside it",
   "hall":     "castle entrance hall, red carpet, crystal chandelier, portraits of women on the walls, a long upholstered bench",
   "dining":   "castle dining hall, a very long table, silver candelabra, glasses of red wine, a chair at the far end of the table",
   "study":    "sorcery study, shelves of old spellbooks, candles, a red velvet armchair, ink bottles, scattered parchment without text",
   "library":  "old castle library, towering bookshelves, a wooden ladder, shadowy aisle between shelves, books without text",
   "knight":   "knights' hall, suits of armor on stands, decorative swords on the wall, a red rug on the cold stone floor, small bats under the ceiling",
   "dojo":     "sword training room, stone floor, moonlight through a tall window, wooden practice swords on a rack, a bed in the corner",
   "balcony":  "castle balcony at night, huge red moon, night wind, sea of mist below, a single chair",
   "garden":   "rose garden at night, black roses and white roses, night dew, a gazebo with black curtains",
   "throne":   "queen's throne room, an empty ornate throne with a red mantle draped over it, red carpet, black curtains, silence",
   "clock":    "inside a great clock tower, huge brass gears, a swinging pendulum, a large bell, a spiral staircase",
   "stairs":   "stone stairway leading underground, cold stone steps, candles in wall niches, a small landing",
   "crypt":    "underground crypt, rows of elegant closed coffins used as beds, cool still air, candlelight",
   "chamber":  "underground bedchamber, a bed of black velvet under a red canopy, red tassels, many candles",
 },
 "atk": {
   "m1": ("throne", "he kneels before the empty throne, tilting his head to offer his neck, the elder vampire stands over him lifting his chin with one finger, whispering into his ear, haughty smile, his shirt collar opened, " + MARK + ", dazed, knees trembling"),
   "m2": ("crypt", "from side, he is held in the air wrapped in " + TENT + ", the elder vampire presses her lips softly to his neck from behind, thin tentacle tips sucking his nipples, a smooth round tentacle tip in his anus, anal, his own penis separate, " + MARK, {"neg": TENT_NEG}),
   "m3": ("chamber", "he lies on his back on the black velvet bed, the elder vampire leans over him kissing him deeply, tongues, saliva trail, two of her wet fingers in his anus, fingering, a pink tentacle curled around his thigh, " + MARK),
   "e1": ("knight", "he kneels on the red rug leaning back on his hands, the vampire knight stands over him with one boot off, her stockinged sole pressing and circling on his lower belly and penis, footjob, small bats brushing his neck and side with their wings, stern face, " + MARK),
   "e2": ("study", "he kneels at the foot of the red velvet armchair, the seated sorceress spreads the wide hem of her black dress over his body up to his chest, the cloth clinging to his skin, her glowing purple eyes looking down, his mouth open without a voice, " + MARK),
   "e3": ("gate", "he stands with his knees giving way, the vampire gatekeeper hugs him tightly, his face buried between her large breasts, her lips pressed softly to the side of his neck, sucking gently, his arms hanging limp, " + MARK),
   "boss": ("dojo", "she wraps her dark cloak around him, he stands inside the cloak held against her chest, his face nestled in her breasts, the swordswoman pressing her lips softly to his neck, her fingers rolling his nipple, moonlight outside the cloak, " + MARK),
 },
 "atk_desc": {
   "m1": "the elder vampire repeats that he is an offering to her queen until he offers his own neck.",
   "m2": "the elder vampire sucks gently at his neck while her soft pink tentacles caress him inside and out.",
   "m3": "the elder vampire seals his mouth with a cold kiss while her fingers loosen him.",
   "e1": "the vampire knight teaches him a knight's courtesy with the weight of her foot and the wings of her bats.",
   "e2": "the seated sorceress covers him with the hem of her dress, which drains him wherever it touches.",
   "e3": "the vampire gatekeeper buries his face in her chest and sucks gently at his neck until his strength leaves him.",
   "boss": "the swordswoman wraps him in her night-colored cloak and shelters his face in her chest.",
 },
 "lose": {
   # エルダー 技1（女王への忠義）
   "btl_m1":     ("throne", "he kneels before the empty throne with his head tilted, offering his neck, the elder vampire bends down pressing her lips to his neck, " + TENT + " wrapped around his chest and thighs, a black ribbon tied around his wrist, cum dripping untouched, " + MARK, {"neg": TENT_NEG}),
   "onani_m1":   ("stairs", "kneeling alone on the stair landing in the shadow of a candle, tracing his own neck with a fingertip, the other hand rubbing his own nipple, lips murmuring, penis untouched, the red dots on his neck glowing, the elder vampire watches far below on the stairs"),
   "inochi_m1":  ("gate", "he sits against the inside of the iron gate with his back to the outside, the elder vampire kneels over him pressing her lips to his neck, a pink tentacle tip sucking his nipple, his eyes turned away from the mist, " + MARK + ", cum dripping", {"neg": TENT_NEG}),
   "onedari_m1": ("chamber", "he sits on the black velvet bed baring the right side of his neck with his own hand, the elder vampire sits beside him sucking softly at the offered neck, her hand on his chest pinching his nipple, pleased haughty smile, " + MARK + ", cum dripping"),
   # エルダー 技2（★吸血吸精ワーム）
   "btl_m2":     ("crypt", "from side, he floats above the coffins wrapped in " + TENT + ", the elder vampire behind him with her lips on his neck, ring-shaped tentacle tips sucking both nipples, a smooth round tentacle tip deep in his anus, anal, his own penis separate, cum dripping, " + MARK, {"neg": TENT_NEG}),
   "onani_m2":   ("dining", "sitting alone on the floor behind the chair at the far end of the long table, a long cord wound around his own chest and waist, one hand pressing his neck, the other hand reaching behind to stroke his own anus, penis untouched, the elder vampire watches far away at the head of the table"),
   "inochi_m2":  ("clock", "from side, on the spiral staircase beside the great bell, he is pulled back by " + TENT + " around his waist and ankles, the elder vampire holding him from behind with her lips on his neck, a round tentacle tip in his anus, anal, his own penis separate, the pendulum swinging, " + MARK, {"neg": TENT_NEG}),
   "onedari_m2": ("chamber", "from side, he lies on his back on the black velvet bed cradled by six " + TENT + ", two tentacle tips sucking his nipples, one round tentacle tip deep in his anus, anal, the elder vampire leans over sucking softly at his neck, his own penis separate, cum on his stomach", {"neg": TENT_NEG}),
   # エルダー 技3（最古参の口づけ）
   "btl_m3":     ("chamber", "from side, under the red canopy, he lies on his back on the black velvet, the elder vampire over him kissing him deeply, tongues, saliva trail, a smooth pink tentacle tip in his anus, anal, another tentacle sucking his nipple, a red tassel beside his hand, his own penis separate, cum on his stomach", {"neg": TENT_NEG}),
   "onani_m3":   ("balcony", "crouching alone behind the chair under the red moon, sucking two of his own fingers as if kissing, the other hand reaching behind pressing a finger to his own anus, penis untouched, the red dots on his neck glowing, the elder vampire watches far away from the balcony door"),
   "inochi_m3":  ("throne", "he stands before the empty throne on tiptoe, the elder vampire holds his chin and kisses him deeply, tongues, saliva, her other hand behind him with two fingers in his anus, fingering, his knees giving way, " + MARK + ", cum dripping"),
   "onedari_m3": ("chamber", "from side, on the bed at dawn with candles burning low, he lies in the elder vampire's arms, a long deep kiss, tongues, a smooth pink tentacle tip deep in his anus, anal, " + TENT + " around his waist, his own penis separate, cum on his stomach", {"neg": TENT_NEG}),
   # コンキスタ（★吸血鬼の足躙り）
   "btl_e1":     ("knight", "he lies on his back on the red rug, the vampire knight stands over him with one boot off, her stockinged sole pressing and circling on his penis against his lower belly, footjob, small bats brushing his neck and side with their wings, a cape clasp placed on his chest, cum on his stomach, " + MARK),
   "onani_e1":   ("library", "sitting alone under the wooden ladder, one knee drawn up, pressing the sole of his own foot against his own lower belly, penis untouched, the red dots on his neck glowing, the vampire knight watches far away at the end of the aisle"),
   "inochi_e1":  ("knight", "he kneels on the red rug kissing the top of her bare foot, the vampire knight stands with her other foot resting on his shoulder, a small bat touching his hair with its wing, stern faint smile, " + MARK + ", cum dripping untouched"),
   "onedari_e1": ("knight", "beside a suit of armor, he lies on his back on the stone floor, the vampire knight sits on a bench with her bare sole pressing slowly on his chest, a small bat tickling his side with its wing, his back arched, " + MARK + ", cum dripping"),
   # ヴェンデッタ（★吸精ドレス）
   "btl_e2":     ("study", "he kneels at the foot of the red velvet armchair, the seated sorceress has covered him to the neck with the wide hem of her black dress, the cloth clinging to his body, her fishnet leg stroking him under the cloth, his mouth open without a voice, black lace on his wrist, " + MARK),
   "onani_e2":   ("library", "crouching alone between the bookshelves, his jacket pulled over his head, biting back his voice, one hand under the cloth rubbing his own nipple, penis untouched, the red dots on his neck glowing, the sorceress watches far away seated in her red armchair"),
   "inochi_e2":  ("study", "he kneels before the red velvet armchair holding an open spellbook without text, dazed and confused, the seated sorceress looks down with glowing purple eyes, the hem of her black dress wrapped around his legs and waist, turning a page with one finger, " + MARK + ", cum dripping"),
   "onedari_e2": ("study", "at the foot of the red velvet armchair, only his face shows above the black dress hem that covers his whole body, the seated sorceress rests her hand on his head, her fingers under the cloth on his nipple, cool approving smile, his mouth open without a voice, cum dripping"),
   # ヴァンパイア（★ヴァンパイアバスト）
   "btl_e3":     ("gate", "before the iron gate, he sags in the gatekeeper's arms with his knees bent, his face sunk between her large breasts, the vampire gatekeeper sucking softly at his neck, her hand stroking his penis, handjob, an iron key ornament hung on his neck, cum dripping, " + MARK),
   "onani_e3":   ("hall", "sitting alone behind the long bench, hugging a pillow to his chest with his face buried in it, one fingertip slowly tracing his own neck, penis untouched, the red dots on his neck glowing, the vampire gatekeeper watches far away at the door"),
   "inochi_e3":  ("mist", "in the thick mist with the castle gate looming behind them, he leans on the vampire gatekeeper unable to walk, she hugs his face into her large breasts, her lips on his neck, sucking softly, his hand still held in hers, " + MARK + ", cum dripping untouched"),
   "onedari_e3": ("gate", "inside the small gatehouse on a simple bed, he lies in the gatekeeper's arms, his face held between her large breasts, the vampire gatekeeper sucking his nipple with her lips, her fingers on his neck, happy smile, " + MARK + ", cum on his stomach"),
   # カーミラ（★カーミラの夜衣）
   "btl_boss":   ("dojo", "in the moonlit training room, he stands wrapped inside her dark cloak, his face nestled between her large breasts, the swordswoman pressing her lips softly to his neck, her fingers rolling his nipple, her thigh between his legs, a scrap of dark cloth tied on his wrist, cum dripping, " + MARK),
   "onani_boss": ("garden", "sitting alone in the gazebo wrapped from head to toe in a black curtain, one hand rubbing his own nipple, the other hand stroking his own neck in the dark, penis untouched, the red dots on his neck glowing, the swordswoman watches far away among the black roses"),
   "inochi_boss":("dojo", "a wooden practice sword dropped on the stone floor, he stands with empty hands inside her dark cloak, the swordswoman holds him against her chest, her lips on his neck, her katana still sheathed at her hip, gentle smile, " + MARK + ", cum dripping untouched"),
   "onedari_boss":("dojo", "on the bed in the corner of the training room, he lies completely covered by her dark cloak with only his neck showing, the swordswoman lies over him sucking softly at his neck, his face against her large breasts, her fingers on his nipple, cum dripping"),
 },
 "lose_desc": "keeps him in the castle forever as a cherished offering for her queen, twelve pairs of tiny red marks on his neck.",
 "onanie": {
   "master": ("stairs", "kneeling in the candle shadow, a long cord wound around his own chest, one hand pressing his own neck, the other hand rubbing his own nipple, penis untouched"),
   "e1": ("library", "sitting under a ladder, pressing the sole of his own foot against his own lower belly, penis untouched"),
   "e2": ("library", "crouching between bookshelves with his jacket over his head, rubbing his own nipple under the cloth, penis untouched"),
   "e3": ("hall", "sitting behind a long bench hugging a pillow to his chest, tracing his own neck with a fingertip, penis untouched"),
   "boss": ("garden", "wrapped in a black curtain in the gazebo, rubbing his own nipple and stroking his own neck in the dark, penis untouched"),
 },
 "magic": {
   "1": ("m", "throne", "leaning forward with her lips softly pursed as if to kiss a neck, one finger raised to her lips, a faint pair of red dots of light floating before her, haughty smile"),
   "2": (None, "clock", "a huge bell and a swinging brass pendulum among great gears, ripples of sound in the air, clock face without numbers, candlelight"),
   "3": ("e2", "study", "sitting in a red velvet armchair, one hand raised beside her face, her purple eyes glowing brightly, a finger held to her lips for silence, cool smile"),
   "4": (None, "garden", "a single black rose in full bloom wet with night dew, a faint sweet haze rising from its petals, white roses blurred behind, red moonlight, close-up"),
   "5": (None, "chamber", "an empty bed of black velvet under a red canopy with red tassels, many lit candles around it, a pillow neatly placed, quiet warm glow"),
 },
}
