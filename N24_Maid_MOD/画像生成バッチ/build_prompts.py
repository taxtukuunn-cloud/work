# -*- coding: utf-8 -*-
"""N24 メイド長の屋敷（Maid）画像プロンプト生成 → maid_prompts.json（52枚）
N23 Heels の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
責め手は全員「男の娘」のメイド／執事（1boy）。主人公は見習いメイドにされた後の姿（黒いミニ丈メイド服）で描く。
責め手は常に服を着たまま。逆アナル（責め手の挿入）は m3・boss の場面だけ。主人公が挿入する構図は作らない。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"

# ---- ネガティブ ------------------------------------------------------------
# 指定タグ（胸・筋肉・幼さ・双子・余分な手足・文字）＋ Heels からの共通分
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, extra fingers, text, letters"
            ", sign, logo, numbers, watermark, signature, large breasts, medium breasts, breasts, cleavage, muscular, broad"
            " shoulders, masculine, manly, abs, pectorals, bara, hairy, beard, child, loli, shota, young, teenage, underage"
            ", twins, same face, same hair color, extra legs, three legs, four legs, extra arms, merged bodies, 1girl, 2gir"
            "ls, female, woman, girl, futanari, vaginal, pussy, vagina, blood, injury, whip, whipping, crying in pain, chil"
            "dlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, small bo"
            "dy, petite male, young boy, kid")
# 場面共通：主人公（小さい方）だけが目隠れ・紺髪。ウィッグなし。主人公の挿入は絶対に描かない
NEG_SCENE = (", eyes visible on the smaller man, long hair on the smaller man, wig, black hair on the smaller man, "
             "the smaller man penetrating, the smaller man on top, the smaller man inserting, penetration by the smaller man, "
             "the smaller man licking the taller one, the smaller man sucking, fellatio, the smaller man touching the taller one's penis, "
             "the taller maid naked, the taller maid undressed, nude, fully nude, the smaller man fully naked, yaoi kiss between equals, solo")
# 挿入のない場面：責め手の性器は見せない・性交なし
NEG_NOSEX = ", anal sex, sex, penis in anus, penetration, exposed penis of the taller maid, pants down, strap-on, dildo"
# 挿入の場面：2本のペニスを融合させない
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, double penis, strap-on, dildo"
# 主人公がメイド服を着せられた後なので、責め手（メイド）と取り違えないように
NEG_TALL = ", hair over eyes on the taller maid, the taller maid with hidden eyes, dark blue hair on the taller maid, navy hair on the taller maid"
# オナニーCG
NEG_ONANI = (", masturbation with hand on penis, handjob, hand on penis, holding penis, stroking penis, penis grab, the othe"
             "r person touching him, sex, anal sex, penetration by another, someone else's hand, 2boys in foreground, the wa"
             "tcher in foreground, the watcher naked, hand on crotch, hand near penis, touching penis")

MANSION = "old western mansion interior, victorian style, dark wood, warm candlelight"

# ---- 主人公 -----------------------------------------------------------------
PROT_BODY = ("1boy, adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, l"
             "ean, not muscular, defined jawline, adam's apple, collarbones, flat male chest, faceless male, dark blue hair,"
             " navy blue hair, short hair, hair over eyes, bangs covering eyes, flat chest, smooth pale skin, blush, trembli"
             "ng, height difference, a head shorter than the other, ordinary human man, he is a head shorter than the other "
             "man")
MAID = ("crossdressing, forced to wear a black short maid dress, white frilled apron, white maid headdress, white thighhighs, garter straps, "
        "black strap shoes, no wig, his own short dark blue hair, flat male chest under the dress")
MAID_MITSUKI = ("crossdressing, forced to wear a black short maid dress, white frilled apron, white maid headdress, "
                "white lace garter belt, white stockings, garter clips on his thighs, black strap shoes, no wig, his own short dark blue hair, flat male chest under the dress")
HALF_M2 = ("crossdressing, half dressed, being dressed, white thighhighs and garter straps already on, black short maid dress pulled up to his shoulders but the back buttons still open, "
           "white apron not yet tied, no headdress yet, no wig, his own short dark blue hair, flat male chest")
HALF_E2 = ("crossdressing, half dressed, being dressed, black short maid dress on but apron not yet tied, white lace garter belt around his waist, "
           "one white stocking fully on with the garter clip fastened, the other white stocking rolled halfway up his leg, no headdress yet, no wig, his own short dark blue hair, flat male chest")

# ---- 責め手（全員 男の娘・成人） -------------------------------------------------
BOY = ("1boy, adult male, mature face, sharp adult features, 25 years old, adult proportions, long legs, otoko no ko, "
       "androgynous, very feminine, delicate features, slim waist, flat chest, no breasts")
CH = {
    "m": dict(seed="SHION",
              tags=BOY + ", tall, black hair, long hair, half updo, purple eyes, both eyes clearly visible, calm cold polite smile, "
                   "long classic black maid dress, floor-length skirt, white apron, white gloves, white maid headdress, key ring at the waist",
              name="the tall black long-haired otoko no ko head maid in a long black maid dress with white gloves"),
    "e1": dict(seed="KOHAKU",
               tags=BOY + ", amber hair, short hair, amber eyes, both eyes clearly visible, cheerful smile, "
                    "short black maid dress, white apron, white maid headdress, black thighhighs",
               name="the amber short-haired otoko no ko maid in a short black maid dress"),
    "e2": dict(seed="MITSUKI",
               tags=BOY + ", pink hair, medium hair, green eyes, both eyes clearly visible, gentle soft smile, half-closed eyes, "
                    "black maid outfit, white apron, white maid headdress, white pantyhose, rolled up sleeves",
               name="the pink medium-haired otoko no ko laundry maid in a maid outfit and white pantyhose"),
    "e3": dict(seed="NAZUNA",
               tags=BOY + ", green hair, twin braids, gold eyes, sleepy eyes, half-closed eyes, relaxed expression, "
                    "white chef hat, black apron dress, white apron, long sleeves",
               name="the green twin-braided otoko no ko kitchen maid in a chef hat and apron dress"),
    "boss": dict(seed="REIN",
                 tags=BOY + ", very tall, silver hair, short hair, slicked back hair, grey eyes, both eyes clearly visible, cold courteous expression, "
                      "butler, black tailcoat, white gloves, white shirt, black necktie, black trousers, pocket watch chain",
                 name="the very tall silver-haired otoko no ko butler in a black tailcoat with white gloves"),
}

# ---- 部屋（brief.md の部屋一覧） -------------------------------------------------
PL = {
    "hall":      "grand entrance hall, grand staircase, chandelier, polished marble floor, tall front doors, detailed background",
    "office":    "head maid's office, ebony desk, wall of locked cabinets with many small doors, candlestick, detailed background",
    "wardrobe":  "wardrobe room, black maid dresses hanging in a row from short to long, low platform, full-length mirror, detailed background",
    "sewing":    "sewing room, measuring platform, three-panel mirror, hanging paper patterns, tape measure, pins, detailed background",
    "corridor":  "long dim corridor at night, full-length mirror against the wall, candle sconces, carpet runner, detailed background",
    "lounge":    "servants' break room, old leather sofa, small tea table with a teapot, duty roster board on the wall, detailed background",
    "attic":     "attic servant's room, tiny bed with white sheets, low wooden beams, small window, single candle, detailed background",
    "linen":     "linen room, tall shelves, piles of folded white sheets, afternoon light from a window, detailed background",
    "laundry":   "laundry room, wooden wash tubs, soap bubbles, wet stone floor, wicker baskets, steam, detailed background",
    "yard":      "back garden drying yard, white stockings and aprons hanging on clotheslines, sunny afternoon, grass, detailed background",
    "iron":      "ironing room, ironing board with a hot iron, neatly folded stockings, warm window light, detailed background",
    "kitchen":   "large mansion kitchen, big wooden worktable, brick stove with fire, copper pots, detailed background",
    "pantry":    "food storeroom, wooden shelves with jars, hanging dried herbs, barrels of apples, small high window, detailed background",
    "backdoor":  "kitchen back door half open, evening garden outside, herb pots, wicker lunch basket on a table, detailed background",
    "dining":    "long dining hall, very long table, silver candelabra, high-backed chairs, detailed background",
    "punish":    "underground punishment room, rough stone walls, black iron bed frame with a thin mattress, candlesticks on the wall, detailed background",
    "punishdoor": "underground stone corridor, heavy iron door with a small brass name plate, stone steps, candlelight, detailed background",
    "masterbed": "master bedroom, large canopy bed with heavy drapes, closed curtains, dim light, dust sheets, detailed background",
    "study":     "butler's study, floor-to-ceiling bookshelves, large polished desk, leather sofa, green desk lamp, detailed background",
    "private":   "butler's plain private room, small fireplace, leather armchair, simple bed, writing desk with a leather ledger, detailed background",
    "porch":     "carriage porch in front of the mansion entrance, black horse carriage with lit lanterns, gravel, sunset, detailed background",
    "gate":      "back garden iron gate with a big padlock, rose bushes, hill road and town lights beyond, sunset, detailed background",
    "backentry": "back service entrance, packed earth floor, stone step, old wooden door open to the night garden, detailed background",
    "dressing":  "servants' morning dressing room, wall mirror, shelf with combs and hairpins, spare aprons on hooks, morning light, detailed background",
}

OUTDOOR = {"yard", "gate", "porch"}


def bg(place):
    return PL[place] if place in OUTDOOR else MANSION + ", " + PL[place]


CLOTHED = "the taller one keeps his uniform on, fully clothed, only the smaller man's outfit is disturbed"
CAGE = "small flat metal chastity cage covering only his crotch, one thin metal belt around his waist, tiny padlock"
BEADS = "string of ten large black anal beads, black anal beads, thick glossy black beads"
JELLY = "small glass jar of light blue translucent jelly"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Maid_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, sex=False, anal=False, onani=False, outfit=None):
    """sex=責め手の挿入（m3・bossのみ）／anal=指・珠・ゼリーなど挿入物あり（責め手の性器は出さない）"""
    c = CH[who]
    if outfit is None:
        outfit = MAID_MITSUKI if who == "e2" else MAID
    body = PROT_BODY + ", " + outfit
    if onani:
        pos = ", ".join([Q, "explicit", "solo focus, male focus, 1boy in the foreground",
                         "THE NEW MAID (main subject, large in the foreground): " + body,
                         "the dark blue-haired shorter adult man in a black maid dress pleasures himself without touching his penis, both of his hands are clearly away from his penis, " + action,
                         "a small distant figure far in the background only watching, not touching him: " + c["name"] + ", fully clothed, tiny in frame, standing at the doorway",
                         bg(place), desc])
        neg = (NEG_BASE + NEG_SCENE + NEG_TALL).replace(", solo", "") + NEG_ONANI
    else:
        pos = ", ".join([Q, "explicit", "2boys, duo, two people, height difference",
                         "THE SENIOR (taller, dominant, standing or bending over him): " + c["tags"],
                         "THE NEW MAID (a head shorter adult man, submissive, clearly visible): " + body,
                         action, CLOTHED, bg(place), desc])
        neg = NEG_BASE + NEG_SCENE + NEG_TALL + (NEG_INSERT if sex else NEG_NOSEX)
        if anal and not sex:
            # 指・珠・ゼリーの挿入は許す（責め手の性器と性交だけ除外）
            neg = neg.replace(", anal sex, sex, penis in anus, penetration, ", ", anal sex, sex, penis in anus, ")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵5（白背景→背景除去） -------------------------------------------------
STAND = {
    "master": ("m", "standing straight, hands folded in front of the apron, looking down at viewer, from below, calm cold smile, key ring at the waist"),
    "e1": ("e1", "standing, hands behind back, leaning forward slightly, cheerful smile, one eye closed wink"),
    "e2": ("e2", "standing, holding a folded white stocking against his chest with both hands, soft gentle smile, head tilt"),
    "e3": ("e3", "standing, holding a wooden ladle, sleepy half-closed eyes, small yawn, relaxed"),
    "boss": ("boss", "standing tall, one white-gloved hand on chest in a butler's bow, holding a pocket watch in the other hand, looking down at viewer, from below, cold courteous"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, standing, simple background, white background"]), NEG_BASE + ", 2boys", rembg=True)

# ---- 背景（人物なし） -----------------------------------------------------------
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "old western mansion, grand entrance hall with a crystal chandelier, long corridor stretching into the distance, "
                           "polished wooden floor, carpet runner, tall windows with white lace curtains, wall sconces, white lilies in a vase, detailed background"]),
    NEG_BASE + ", 1boy, 2boys, people, person")

# ---- 女装娘カード（見習いメイドにされた成人男性。主人公とは別人：茶髪） -------------------
add("josou", "JOSOU", ", ".join([Q, "safe, solo, 1boy, adult male, adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, adam's apple, collarbones, flat male chest, crossdressing, otoko no ko, brown messy short hair, embarrassed, blush, looking down, head down, "
                                 "black short maid dress, white frilled apron, white maid headdress, white thighhighs, garter straps, black strap shoes, holding down his skirt hem, "
                                 "flat chest, slim, full body, standing, simple background, white background"]),
    NEG_BASE + ", 2boys, dark blue hair, hair over eyes", rembg=True)

# ---- 技CG7 --------------------------------------------------------------------
scene("atk_m1", "m", "office",
      "the smaller man sits on a wooden chair in front of the ebony desk, the head maid stands and bends down to him, deep kiss, french kiss, tongue kiss, saliva trail, "
      "one white-gloved hand slipped inside his pulled-aside apron neckline pinching his nipple, his hands limp on his lap, from side",
      "the head maid teaches him the order of the disciplinary kiss.")
scene("atk_m2", "m", "wardrobe",
      "the smaller man stands on a low platform in front of the full-length mirror being dressed, the head maid stands behind him buttoning the back of the maid dress, "
      "the senior's other gloved hand caressing his flat chest through the black fabric, the senior's lips at his neck, his reflection in the mirror, black maid dresses hanging on the wall",
      "the head maid dresses him in the maid uniform piece by piece.", outfit=HALF_M2)
scene("atk_m3", "m", "punish",
      "from side, the smaller man lies on his back on the iron bed with his legs raised, maid dress neckline and apron pulled down exposing his flat chest, "
      "the head maid stands at the edge of the bed with the senior's long skirt lifted in one hand, penetrating his anus with the senior's own penis, anal, "
      "bending down and licking his nipple, tongue out, the senior's gloved hand holding his thigh, bottle of lotion on the floor",
      "the head maid punishes him with the senior's tongue on his chest while taking him.", sex=True)
scene("atk_e1", "e1", "lounge",
      "the smaller man sits on the old leather sofa, his apron and dress neckline pulled aside exposing his flat chest, the amber-haired maid stands bending over him, "
      "licking his nipple, tongue circling the nipple, one hand cupping his ear as the senior whispers, his hands gripping the sofa, from side",
      "the junior maid teaches him the service with the senior's tongue.")
scene("atk_e2", "e2", "laundry",
      "the smaller man sits on a low wooden stool in the middle of being dressed, the pink-haired maid kneels on one knee in front of him fastening the garter clip "
      "of the white lace garter belt to his white stocking, the senior's other hand stroking his inner thigh, his skirt pushed up, wicker basket of white stockings beside them, from side",
      "the laundry maid puts the garter on him, clip by clip.", outfit=HALF_E2)
scene("atk_e3", "e3", "kitchen",
      "from behind and side, the smaller man bends over the big wooden worktable with his elbows on it, maid skirt flipped up over his back, white thighhighs, "
      "the green-braided kitchen maid kneels behind him and licks his anus, anilingus, tongue out, chef hat, the senior's hands spreading his buttocks, " + JELLY + " on the table",
      "the kitchen maid calls it cleaning and cleans him with the senior's tongue.")
scene("atk_boss", "boss", "study",
      "from side, the smaller man stands bent over the large desk with both hands flat on it, maid skirt flipped up over his back, " + CAGE + ", "
      "the silver-haired butler stands behind him with his trousers opened, penetrating his anus with his own penis, anal, white-gloved hand holding the smaller man's waist, "
      + BEADS + " lying on the desk beside his hand, bottle of lotion",
      "the butler takes him with the lock still on.", sex=True)

# ---- 敗北28 -------------------------------------------------------------------
L = [
 # m1 シオン・躾の口づけ
 ("btl_m1", "m", "office", "from side, the smaller man sits on a wooden chair in front of the ebony desk, the head maid bends down over him in a deep tongue kiss, saliva trail between their lips, the senior's gloved fingers pinching his nipple inside the pulled-aside apron neckline, his skirt tented, white lace choker with a tiny silver pin on his neck", {}),
 ("onani_m1", "m", "attic", "from side, the smaller man sits on the edge of the tiny attic bed under low beams, the head maid stands bending over him holding his chin, deep kiss with tongue, the senior's other gloved hand inside his neckline pinching his nipple, a small silver bell on the pillow, single candle", {}),
 ("inochi_m1", "m", "hall", "from side, at the foot of the grand staircase the smaller man kneels on the marble floor, three sheets of blank paper on the lowest step, the head maid bends down holding his jaw and kisses him deeply, saliva, the senior's gloved hand pinching his nipple through the opened neckline, chandelier above", {}),
 ("onedari_m1", "m", "dining", "from side, the smaller man sits on a high-backed chair at the end of the long table, the head maid stands beside him bending down in a deep tongue kiss, an open blank notebook and a black fountain pen on the table, the senior's gloved hand inside his apron neckline on his nipple, silver candelabra", {}),
 # m2 シオン・メイド服の着付け
 ("btl_m2", "m", "wardrobe", "the smaller man stands on the low platform in front of the full-length mirror in the finished maid dress, the head maid stands behind him tying the white apron ribbon, the senior's lips on his neck, the senior's other gloved hand caressing his chest through the dress, he trembles and climaxes, wet spot, a small locked wooden box with a key on the floor", {}),
 ("onani_m2", "m", "corridor", "the smaller man stands facing the full-length mirror in his maid dress, one of his own hands rubbing his chest through the dress, the head maid stands close behind him gripping his wrist, kissing him over his shoulder, tongue, both reflected in the mirror, night corridor, candle sconces", {}),
 ("inochi_m2", "m", "backentry", "the smaller man stands on the earth floor half wrapped into a second black maid dress, the head maid stands behind him pulling the dress closed and buttoning it, kissing him from behind, two more white cloth bundles on the stone step, the old wooden door open to the night garden", {}),
 ("onedari_m2", "m", "sewing", "the smaller man stands on the measuring platform in a basted maid dress with white thighhighs, the head maid stands behind him wrapping a tape measure around his chest, the senior's lips at his mouth over his shoulder, tongue kiss, the senior's gloved fingers brushing his nipple, three-panel mirror reflections, pins and chalk", {}),
 # m3 シオン・お仕置き（乳首舐め＋逆アナル）
 ("btl_m3", "m", "punish", "from side, the smaller man lies on his back on the iron bed with legs raised, maid neckline pulled down, the head maid stands at the bed with the senior's long skirt lifted, penetrating his anus with the senior's own penis, anal, licking his right nipple, cum on his belly, an old iron key hanging on a wall hook, candles", {"sex": True}),
 ("onani_m3", "m", "punish", "night, from side, the smaller man lies on the iron bed with his wrists tied together above his head with a white apron ribbon, the head maid stands at the bed with skirt lifted and penetrates his anus with the senior's own penis, anal, bending down licking his nipple, candle flames, stone wall", {"sex": True}),
 ("inochi_m3", "m", "punishdoor", "from side, just inside the heavy iron door with a small blank brass name plate, the smaller man kneels on all fours on the edge of the iron bed in his maid dress with his skirt flipped up, the head maid stands behind him with the senior's long skirt lifted, penetrating his anus with the senior's own penis, anal, reaching around to pinch his nipple through the opened neckline, candle", {"sex": True}),
 ("onedari_m3", "m", "punish", "from side, the smaller man lies on his back on the iron bed with his mouth open reciting, neckline pulled down, the head maid stands with the senior's skirt lifted penetrating his anus deeply with the senior's own penis, anal, the senior's tongue on his left nipple, the senior's key ring placed by the pillow, candles", {"sex": True}),
 # e1 コハク・ご奉仕の乳首舐め
 ("btl_e1", "e1", "lounge", "from side, the smaller man sits on the old leather sofa with apron and neckline pulled aside, the amber-haired maid stands bent over him licking his nipple, tongue out, the senior's fingers pinching his other nipple, cum stain on his skirt, a blank handwritten sheet on the tea table", {}),
 ("onani_e1", "e1", "linen", "from above and side, the smaller man lies on his back on a pile of white folded sheets in his maid dress with the neckline pulled open, his own wet fingers still near his chest, the amber-haired maid kneels over him on the sheets licking his nipple, tongue out, sunlight", {}),
 ("inochi_e1", "e1", "gate", "sunset, the smaller man sits on the grass with his back against the padlocked iron gate in his maid dress, neckline pulled aside, the amber-haired maid kneels in front of him leaning over and licking his nipple, tongue out, the senior's hand at his ear, roses", {}),
 ("onedari_e1", "e1", "dressing", "morning, the smaller man sits on a low chair in front of the wall mirror in his maid dress with the neckline pulled open, the amber-haired maid stands bending down licking his right nipple, tongue out, holding a small notepad and a pencil in one hand, spare aprons on hooks", {}),
 # e2 ミツキ・ガーターを着せる／ストッキングの足
 ("btl_e2", "e2", "laundry", "from side, the smaller man sits on a low wooden stool with his maid skirt pushed up showing his white lace garter belt and white stockings, the pink-haired maid stands on one foot and presses the sole of the senior's white pantyhose foot against his crotch, footjob with stockinged foot, the senior's hand on his shoulder, wooden tubs, steam", {}),
 ("onani_e2", "e2", "yard", "from side, among white stockings hanging on clotheslines the smaller man kneels on the grass with his skirt pushed up, his own hand on his garter-clipped thigh, the pink-haired maid stands over him bending down and fastening a garter clip on his thigh, the senior's other hand stroking his inner thigh, sunny", {}),
 ("inochi_e2", "e2", "laundry", "sunset light through the open back door of the laundry room, the smaller man stands in the doorway in his maid dress with his skirt held up, the pink-haired maid kneels on one knee fastening a new white garter clip to his stocking, his small hand pressing down on the senior's hand, a white garter ring on his other thigh", {}),
 ("onedari_e2", "e2", "iron", "from side, the smaller man sits on a chair beside the ironing board with his skirt pushed up, three folded garter sets on the board: white, black and lace, the pink-haired maid stands and presses the senior's white pantyhose foot on his lap, footjob with stockinged foot, holding a small blank white card and a pencil", {}),
 # e3 ナズナ・お掃除（アナル舐め）／媚薬ゼリー
 ("btl_e3", "e3", "kitchen", "from behind and side, the smaller man bends over the big wooden worktable with his skirt flipped up, white thighhighs, the green-braided kitchen maid kneels behind him licking his anus, anilingus, tongue out, chef hat, " + JELLY + " open on the table, a tiny wooden chair in the corner by the stove", {}),
 ("onani_e3", "e3", "pantry", "from side, the smaller man stands with both hands on a wooden shelf and his skirt flipped up, white thighhighs, the green-braided kitchen maid kneels behind him licking his anus, anilingus, tongue out, jars and dried herbs, barrel of apples", {}),
 ("inochi_e3", "e3", "backdoor", "from side, the smaller man bends over holding the frame of the half-open kitchen back door with his skirt flipped up, the green-braided kitchen maid kneels behind him pushing a lump of light blue translucent jelly into his anus with two fingers, anal fingering, " + JELLY + " in the senior's other hand, wicker lunch basket on the table, evening garden", {"anal": True}),
 ("onedari_e3", "e3", "kitchen", "from behind and side, the smaller man kneels on a tiny wooden chair by the brick stove with his skirt flipped up, the green-braided kitchen maid kneels behind him licking his anus, anilingus, tongue out, a small brass hand bell on the floor, blank black slate on the wall", {}),
 # boss レイン・躾のアナルパール／鍵をかけたまま
 ("btl_boss", "boss", "study", "from side, the smaller man stands bent over the large desk with both hands flat on it, skirt flipped up, " + CAGE + ", the silver-haired butler stands behind him with his trousers opened, penetrating his anus with his own penis, anal, white-gloved hand on the smaller man's waist, " + BEADS + " glistening on the desk, a small key on the butler's pocket watch chain", {"sex": True}),
 ("onani_boss", "boss", "masterbed", "from side, the smaller man kneels on all fours on the canopy bed in his maid dress with his skirt flipped up, the silver-haired butler stands beside the bed bending over him and pushing a large black anal bead into his anus with white-gloved fingers, " + BEADS + " half inserted, half of the string hanging, dim light, closed curtains", {"anal": True}),
 ("inochi_boss", "boss", "porch", "sunset, from side, the smaller man kneels on the gravel holding the step of the black carriage with his skirt flipped up, the silver-haired butler stands behind him bending down and inserting large black anal beads into his anus one by one with white-gloved fingers, " + BEADS + ", carriage lantern light", {"anal": True}),
 ("onedari_boss", "boss", "private", "from side, the smaller man lies on his back on the simple bed with his legs raised, skirt up, " + CAGE + " locked, a white ribbon tied around his wrist, the silver-haired butler stands at the bed with his trousers opened, penetrating his anus with his own penis, anal, white gloves on the smaller man's thighs, open blank leather ledger on the writing desk, small fireplace", {"sex": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him a maid of the manor forever.", **opt)

# ---- オナニーCG5（責め手の★得意技に合わせた自慰。ペニスに触れない。責め手は奥で見ているだけ） -----
ON = {
    "master": ("m", "attic", "sitting on the edge of the tiny attic bed in his maid dress, two of his own fingers deep in his mouth, sucking his fingers, tongue around his fingers, "
                             "his other hand inside the pulled-aside apron neckline pinching his own nipple, legs pressed together, skirt tented, not touching his penis, flushed"),
    "e1": ("e1", "linen", "sitting on a pile of white sheets in his maid dress with the neckline pulled open, rubbing his own nipple in circles with a saliva-wet fingertip, "
                          "other hand at his other nipple, arching his back, not touching his penis, flushed, sunlight"),
    "e2": ("e2", "yard", "kneeling on the grass among hanging stockings in his maid dress with the skirt pushed up, both hands stroking his own inner thighs over the white lace garter belt and white stockings, "
                         "fingertips under the garter clip, one hand pressing his rear through the skirt, not touching his penis, flushed"),
    "e3": ("e3", "pantry", "from behind and side, kneeling on the floor facing the shelves in his maid dress with the skirt flipped up, reaching back and circling his own anus with a wet finger, "
                           "tracing the entrance, face turned aside, not touching his penis, flushed"),
    "boss": ("boss", "masterbed", "from side, kneeling on all fours on the canopy bed in his maid dress with the skirt flipped up, reaching back and sinking two of his own fingers into his anus, anal fingering, "
                                  "counting on his lips, not touching his penis, flushed, closed curtains"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in the senior's style while the senior only watches from far away.", onani=True)

# ---- 魔法・罠5 ------------------------------------------------------------------
MG = [
    ("magic_1", "m", "hall", "morning light, standing close, reaching toward viewer with both white-gloved hands to straighten the viewer's collar, pov, looking down at viewer, from below, calm inspecting gaze"),
    ("magic_2", "m", "wardrobe", "holding out a neatly folded black short maid dress with a white apron and white headdress on top toward viewer with both gloved hands, looking at viewer, slight smile"),
    ("magic_3", "m", "dining", "holding up a small silver hand bell with one gloved hand, about to ring it, looking at viewer, calm smile, long table"),
    ("magic_4", "e1", "corridor", "walking toward viewer carrying a round silver tray with a silver cloche on it, cheerful smile, looking at viewer, daylight corridor"),
]
for key, who, place, act in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, bg(place)]), NEG_BASE + ", 2boys")
add("magic_5", "BG", ", ".join([Q, "safe, no humans, scenery", "underground punishment room, rough stone walls, black iron bed frame with a thin white mattress, iron chain on the wall, "
                                "lit candlesticks, stone steps leading up, heavy iron door ajar, cold dramatic light, detailed background"]),
    NEG_BASE + ", 1boy, 2boys, people, person")

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Maid", "images": images}, open(os.path.join(here, "maid_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
