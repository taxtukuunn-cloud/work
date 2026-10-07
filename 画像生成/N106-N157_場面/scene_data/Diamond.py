# N120 ダイアモンドタウンの夜（Diamond）画像データ。登場人物は全員20歳以上。6人とも女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない。原作の立ち絵は参照していない）。
# 髪色は被らせない：シスター＝淡い金／見習い（立ち絵の2人目だけ）＝灰／お嬢様＝栗色の巻き髪／リナ＝赤毛のポニーテール／メイド＝黒髪ロング／ナース＝濃い紫。
# 青・水色系の髪・瞳は使っていない（原作の色が不明な部分は役に合う色で決めた）。
# マスターは2人組：立ち絵だけ2人（pose に2人目）。技CG・敗北CGは「シスター1人＋主人公」に置き換え（見習いの役＝キス・乳首もシスターが行う）。
# 後ろに入れるのは指だけ（pen なし）。ナースの騎乗位は彼女が上で迎える技（スカートで隠す。後ろの挿入ではない）ので、
# ナースだけ共通ネガの vaginal 系を外す（neg_remove）。点滴に針は描かない。札・手紙・ネームプレートは文字なし。
PURSE = "a leather coin purse with warm glowing gold coins beside him"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
NURSE = "her white skirt covering where they join"
BREAST = "the sister's habit opened at the chest"
DATA = {
 "code": "Diamond",
 "world": "old european town at night that shows another face after dark, gas lamps, cobblestones, a church spire with a bell over the roofs, warm candlelight, detailed background",
 "bg": "church nave at night, tall stained glass windows, many lit candles, rows of wooden pews, an old wooden offering box, a stone altar, gas lamps and cobblestones seen through a side window, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "シスター（＋見習いシスター）",
         "tags": "adult woman, mature female, mature face, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, nun, pale blonde hair, long hair, golden eyes, black nun habit, long black veil, white collar, silver cross necklace, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the blonde sister in a black habit and long veil",
         "pose": "hands clasped in prayer under her chest, serene gentle smile, looking at viewer, standing beside a second adult woman with short ash-grey hair in a black nun habit with a short veil who covers her mouth with one hand and smirks",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "お嬢様（ヤンデレ娘）",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, chestnut brown hair, long curly hair, drill curls, hazel eyes, white lace dress with frills, white lace gloves, ribbon choker, slender curvy feminine body, medium breasts",
          "name": "the chestnut-curled lady in a white lace dress",
          "pose": "both lace-gloved hands pressed to her cheeks, a sealed letter without text tucked under her arm, dreamy lovestruck smile, looking at viewer",
          "neg": SOFT_NEG + ", knife, weapon, scary"},
   "e2": {"type": "woman", "jp": "リナ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, bright red hair, high ponytail, sparkling emerald green eyes, gem-like eyes, open short brown jacket, black lace bralette, black shorts, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the red-ponytail barmaid in an open jacket",
          "pose": "leaning forward with one hand held out as if to hold hands, the other hand raised counting on her fingers, bright friendly grin, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "メイド",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, black hair, very long straight hair, grey eyes, white frilled headband, black long maid dress, white apron, soft curvy feminine body, large breasts",
          "name": "the black-haired maid in a white apron",
          "pose": "holding a folded white sheet over one arm, the other hand at her lips hiding a soft giggle, polite smile, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "看護師（ナース）",
            "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark purple hair, hair bun, violet eyes, glasses, white nurse cap, white nurse dress, white pantyhose, soft voluptuous feminine body, large breasts, wide hips",
            "name": "the bespectacled nurse in a white uniform",
            "pose": "holding a blank clipboard without text against her chest, adjusting her glasses with one finger, cool businesslike faint smile, looking at viewer",
            "neg": SOFT_NEG + ", syringe, needle",
            "neg_remove": ["vaginal", "penis inside the woman", "sex with the woman"]},
 },
 "places": {
   "street":      "main street at night, gas lamps, wet cobblestones, dark shop windows",
   "gate":        "iron gate of a mansion at night, trimmed garden, lit windows",
   "salon":       "mansion drawing room, sofa, tea set, grandfather clock, fireplace with a rug in front",
   "bedroom":     "mansion bedroom, large bed with white sheets, a tray with cleaning cloths and an oil bottle",
   "tavern":      "back door of a tavern at night, wooden door, stacked barrels, warm light from the windows",
   "backroom":    "snug back room behind a tavern counter, oil lamp, low couch, bottles of amber liquor without labels",
   "alley":       "narrow moonlit alley, stone walls, a cat on a ledge, full moon",
   "ladyroom":    "a lady's private room, lace curtains, a pile of sealed letters without text on a desk, perfume bottles, canopy bed",
   "plaza":       "town fountain plaza at night, stone fountain, wooden bench, gas lamps",
   "reception":   "hospital reception at night, white walls, a counter, quiet empty hallway",
   "ward":        "hospital room at night, white bed, drawn curtain, an IV stand with a bag of pink liquid and no needle",
   "duty":        "cramped night-duty nap room, narrow cot, a white coat on a hanger",
   "churchfront": "front of a stone church at night, spire with a bell, stone steps, heavy wooden doors",
   "nave":        "church nave at night, stained glass windows, many lit candles, wooden pews, an offering box, an altar",
   "confess":     "wooden confessional booth, lattice window, velvet kneeler, a single candle",
   "well":        "back yard of a church at night, old stone well, wooden bucket, moonlight",
 },
 "atk": {
   "m1": ("confess", "he kneels on the velvet kneeler with his head bowed, the sister sits close beside him in the booth, one hand lifting his chin, whispering forgiveness into his ear, her other hand resting on his chest, candlelight, he trembles and blushes, " + PURSE),
   "m2": ("nave", "he lies on a pew with his head on the sister's lap, " + BREAST + ", he suckles her bare breast, her fingers rolling his nipple, her other hand slowly stroking his lower belly, gentle smile, candles, " + PURSE),
   "m3": ("nave", "he kneels before the altar leaning back in the sister's arm, the sister kisses him deeply, tongues, saliva trail, two oiled fingers of her other hand in his anus, fingering, a glass vial of warm holy oil without label on the floor, candles"),
   "e1": ("ladyroom", "he sits on the edge of the canopy bed, the lady hugs him tightly from behind, her lips at his ear whispering, her white lace-gloved hand gripping his penis, handjob, perfume bottles, he shivers, " + PURSE),
   "e2": ("backroom", "he lies back on the low couch, the barmaid kneels between his legs with her jacket open, his penis squeezed between her breasts in the lace bralette, paizuri, both her hands holding his hands with fingers interlocked, bright grin, counting aloud, oil lamp"),
   "e3": ("bedroom", "he kneels on all fours on the white sheets, the maid kneels behind him, one hand reaching under to stroke his penis, two oiled fingers of her other hand in his anus, fingering, soft giggle, an oil bottle on the bed"),
   "boss": ("ward", "he lies on his back on the white hospital bed, the nurse straddles his hips in cowgirl position, pinning both his wrists to the bed above his head, " + NURSE + ", leaning over him with a flushed hungry grin, the IV stand swaying"),
 },
 "atk_desc": {
   "m1": "the sister makes him confess his hidden desires and forgives each one.",
   "m2": "the sister lays his head on her lap and lets him suckle her breast while rolling his nipple.",
   "m3": "the sister purifies him with a deep kiss and holy-oiled fingers at the same time.",
   "e1": "the lady whispers fate into his ear while her lace glove strokes him.",
   "e2": "the barmaid holds his hands and counts down, never reaching zero.",
   "e3": "the maid serves him on all fours, front and rear in turn.",
   "boss": "the nurse suddenly pins his wrists to the bed and rides him at her own pace.",
 },
 "lose": {
   # シスター組 技1（告解＋★授乳のお布施）
   "btl_m1":     ("confess", "he kneels on the velvet kneeler, the lattice window opened, the sister leans through holding his head to her bare breast, " + BREAST + ", he suckles, her lips at his ear whispering forgiveness, a silver rosary around his neck, cum dripping untouched, candle"),
   "onani_m1":   ("churchfront", "kneeling alone in the shadow of the stone steps, lips moving in a whisper, one hand rubbing his own nipple, the other hand reaching behind to stroke his own anus, penis untouched, the sister watches far away from the open church door"),
   "inochi_m1":  ("nave", "he has slid from a pew to his knees, the sister sits on the pew pressing her bare breast to his lips, " + BREAST + ", one finger raised as if to say tomorrow, rows of candles, incense haze, cum dripping untouched, " + PURSE),
   "onedari_m1": ("confess", "he kneels on the velvet kneeler looking up, the sister embraces his head, " + BREAST + ", he suckles her breast, her lips whispering at his ear, a row of lit candles along the lattice, cum dripping, " + PURSE),
   # シスター組 技2（★授乳のお布施）
   "btl_m2":     ("nave", "he lies on the front pew with his head on the sister's lap, suckling her bare breast, " + BREAST + ", her fingers rolling his nipple, her other hand resting on his lower belly without stroking, a black ribbon tied around his neck, cum on his stomach, many candles"),
   "onani_m2":   ("nave", "lying alone on the floor behind a pew, hugging a white pillow to his face, mouthing the pillow, one hand rolling his own nipple, penis untouched, the sister watches far away from the aisle"),
   "inochi_m2":  ("nave", "he lies on bedding laid before the altar, the sister lies beside him holding his head to her bare breast, " + BREAST + ", he suckles, her hand on his lower belly, gold coins dropping into the offering box, cum on his stomach"),
   "onedari_m2": ("nave", "he sits across the sister's lap on a pew cradled in her arms, suckling her bare breast, " + BREAST + ", her hand slowly stroking his lower belly, candlelight, her black habit filling the frame, cum dripping, " + PURSE),
   # シスター組 技3（聖水の清め＋★授乳のお布施）
   "btl_m3":     ("nave", "he kneels before the altar with his face held against the sister's bare breasts, " + BREAST + ", he suckles, her arm around his head, two oiled fingers of her other hand in his anus, fingering, a glass vial of holy oil without label, cum dripping untouched"),
   "onani_m3":   ("well", "kneeling alone beside the old stone well, a wet hand reaching behind with a finger in his own anus, the other hand gripping the edge of the well, penis untouched, the sister watches far away from the church back door"),
   "inochi_m3":  ("churchfront", "he kneels on the top stone step facing the open church doors, the sister kneels with him kissing him deeply, tongues, saliva, two oiled fingers in his anus, fingering, the bell swinging in the spire above, candlelight spilling from the doors, cum dripping"),
   "onedari_m3": ("confess", "he kneels bent forward on the velvet kneeler, the sister behind him with two oiled fingers held still deep in his anus, fingering, her other arm drawing his head back to her bare breast, " + BREAST + ", he suckles, candle flickering through the lattice, cum dripping"),
   # お嬢様（★運命の囁き）
   "btl_e1":     ("ladyroom", "he sits on the canopy bed among scattered sealed letters without text, the lady clings to his back, her lips touching his earlobe whispering, her lace-gloved hand squeezing his penis, handjob, cum on her white glove, a single lace glove laid on his thigh"),
   "onani_e1":   ("plaza", "sitting alone on the fountain bench, tracing his own ear with a fingertip, lips moving, the other hand rubbing his own nipple, penis untouched, the lady watches far away from behind the fountain with clasped hands"),
   "inochi_e1":  ("alley", "he stands in the moonlit alley with weak knees, the lady hugs his arm tightly against her chest, her lips at his ear whispering, her lace-gloved hand stroking his penis, handjob, full moon, mansion gate at the end of the alley, cum dripping"),
   "onedari_e1": ("ladyroom", "he lies on the canopy bed inside the lace curtains, the lady lies against his side, her lips on his ear whispering, counting on the fingers of one hand, her other lace-gloved hand gripping his penis tightly, handjob, blissful smile, cum spurting"),
   # リナ（★カウントダウン）
   "btl_e2":     ("backroom", "he lies back on the low couch, the barmaid between his legs with her jacket open, his penis squeezed between her breasts, paizuri, her fingers interlocked with both his hands, gazing up with sparkling eyes, a blank wooden menu tag without text on the table, cum on her chest"),
   "onani_e2":   ("tavern", "sitting alone hidden behind the stacked barrels, one hand pinching his own nipple, the other hand raised with fingers folding down as if counting, lips moving, penis untouched, the barmaid watches far away leaning in the doorway"),
   "inochi_e2":  ("backroom", "he sits slumped on the low couch staring up dazed, the barmaid leans over him holding his cheek, her sparkling emerald eyes close to his face, his penis between her breasts, paizuri, one finger raised counting, a glass of amber liquor, cum on her chest"),
   "onedari_e2": ("backroom", "he lies on the low couch, the barmaid lies against him holding both his hands with fingers interlocked, her lips at his ear counting, her jacket open, his penis twitching untouched, a brass key on the table, cum dripping untouched"),
   # メイド（★四つん這いの奉仕）
   "btl_e3":     ("bedroom", "he kneels on all fours on the white sheets, the maid kneels behind him, one hand stroking his penis from behind, two oiled fingers of her other hand in his anus, fingering, soft giggle, a white frilled headband ornament beside his hand, cum on the sheets"),
   "onani_e3":   ("salon", "kneeling alone on all fours on the rug before the fireplace, reaching behind with a finger in his own anus, hips raised, penis untouched, the maid watches far away by the door holding a tea tray"),
   "inochi_e3":  ("bedroom", "he kneels on all fours on the bed, the maid behind him wiping his back with a white cloth in one hand, two oiled fingers of her other hand in his anus, fingering, his folded clothes on a chair, soft giggle, cum dripping untouched"),
   "onedari_e3": ("bedroom", "from side, he kneels on all fours on the white sheets with his hips raised, the maid kneels behind him, one hand on his penis, two oiled fingers of her other hand in his anus, fingering, her white apron swaying, counting quietly, cum on the sheets"),
   # ナース（★押さえつけ騎乗位）
   "btl_boss":   ("ward", "he lies on his back on the white hospital bed, the nurse straddles his hips in cowgirl position, both her hands pinning his wrists above his head, " + NURSE + ", flushed hungry grin, a blank nameplate without text at the head of the bed, the IV stand swaying, cum overflowing"),
   "onani_boss": ("duty", "lying alone on his back on the narrow cot, both wrists crossed above his head pressed into the pillow, hips rocking upward, penis untouched, the nurse watches far away from the doorway holding her glasses in one hand"),
   "inochi_boss":("ward", "he lies on the hospital bed, the nurse straddles his hips in cowgirl position, one hand pinning his wrists above his head, two fingers of her other hand on his neck taking his pulse, " + NURSE + ", a blank chart without text on the bedside table, cum overflowing"),
   "onedari_boss":("ward", "behind the drawn curtain, he lies on his back on the bed, the nurse straddles his hips riding fast in cowgirl position, both hands pinning his wrists hard to the bed, " + NURSE + ", sweat, ecstatic grin, glasses slipping, cum overflowing, " + PURSE),
 },
 "lose_desc": "offers him to the night church of the town forever, his coin purse full of warm gold coins while the church bell rings.",
 "onanie": {
   "master": ("nave", "sitting on the floor behind a pew, hugging a white pillow to his face, one hand rolling his own nipple, penis untouched"),
   "e1": ("plaza", "sitting on the fountain bench, tracing his own ear with a fingertip, the other hand rubbing his own nipple, penis untouched"),
   "e2": ("tavern", "sitting behind the barrels, one hand pinching his own nipple, the other hand counting down on its fingers, penis untouched"),
   "e3": ("salon", "kneeling on all fours on the rug before the fireplace, reaching behind with a finger in his own anus, penis untouched"),
   "boss": ("duty", "lying on his back on the narrow cot, both wrists crossed above his head, hips rocking upward, penis untouched"),
 },
 "magic": {
   "1": (None, "street", "an open leather coin purse on the cobblestones with two gold coins glowing warmly inside, plain coins without text, close-up"),
   "2": (None, "churchfront", "a large bronze church bell swinging in the spire at night, faint sound ripples in the air, the moon behind it"),
   "3": (None, "backroom", "a glass of sweet amber liquor glowing under the oil lamp, a bottle without label beside it, faint pink vapor rising from the glass"),
   "4": ("m", "nave", "holding up a glass vial of warm holy oil in both hands, a single drop falling from the tilted vial, serene gentle smile"),
   "5": (None, "nave", "an old wooden offering box with its lid open, gold coins glowing inside, candles around it, plain box without text"),
 },
}
