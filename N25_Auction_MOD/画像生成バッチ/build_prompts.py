# -*- coding: utf-8 -*-
"""N25 オークションハウス（Auction）画像プロンプト生成 → auction_prompts.json（52枚）
N23 Heels の build_prompts.py を元に作成。登場人物は全員20歳以上の成人。個人利用のみ。
責め手は男の娘（中性的な成人男性・胸は平ら・服を着たまま）。主人公は出品衣装（女装）を着せられた後の姿で描く。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, watermark, signature, text, "
            "letters, sign, logo, numbers, price tag with text, child, loli, shota, young, teenage, underage, muscular, abs"
            ", pectorals, bara, hairy, broad shoulders, manly, 1girl, girl, female, woman, breasts, large breasts, medium b"
            "reasts, cleavage, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, eyes visib"
            "le on the navy-haired man, vaginal, pussy, vagina, merged bodies, blood, injury, whip, whipping, crying in pai"
            "n, childlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, s"
            "mall body, petite male, young boy, kid")
# 女装モード：主人公も女物を着るので、2人とも男の娘。責め手の髪色を主人公に移さない
NEG_SCENE = (", yuri, 2girls, breasts on the man, long hair on the navy-haired man, wig, "
             "blonde hair on the navy-haired man, white hair on the navy-haired man, red hair on the navy-haired man, black hair on the navy-haired man, purple hair on the navy-haired man, "
             "navy hair on the attacker, blue hair on the attacker, white chiffon dress on the attacker, red ribbon choker on the attacker, garter stockings on the attacker")
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, strap-on"
NEG_NOPEN = ", penis on the attacker, exposed penis on the attacker, strap-on, dildo"
NEG_ONANI = (", someone touching him, hand on penis, holding penis, stroking penis, handjob, penis grab, attacker masturbati"
             "ng, attacker in foreground, attacker touching him, hand on crotch, hand near penis, touching penis")

HOUSE = "underground auction house, dark velvet, gold trim, spotlight, dim audience seats in the background"

PROT_BODY = ("1boy, male, adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult bu"
             "ild, lean, not muscular, defined jawline, adam's apple, collarbones, flat male chest, faceless male, navy blue"
             " hair, short hair, hair over eyes, bangs covering eyes, flat chest, smooth pale skin, blush, height difference"
             ", ordinary human man, he is a head shorter than the other man")
OUTFIT = ("crossdressing, otoko no ko, trap, he wears a sheer white chiffon dress with an open chest and open back, "
          "white thigh-high garter stockings, a red ribbon choker on his neck, thin gold chains on his wrists, flat male chest")

OTOKO = ("1boy, adult male, mature face, sharp adult features, 25 years old, adult proportions, long legs, otoko no ko, "
         "androgynous, very feminine, delicate features, slim waist, flat chest, no breasts, taller than the navy-haired"
         " man")

CH = {
    "m": dict(seed="LUCIEN",
              tags=OTOKO + ", blonde hair, long hair, low ponytail, both purple eyes clearly visible, black tailcoat, white gloves, black half mask covering the upper half of his face, holding a wooden gavel, elegant smile",
              name="the blonde ponytailed auctioneer in a black tailcoat and half mask"),
    "e1": dict(seed="YURI",
               tags=OTOKO + ", white hair, short hair, both red eyes clearly visible, appraiser's dark vest over a white shirt, monocle, white gloves, calm expression",
               name="the white short-haired appraiser in a dark vest, monocle and white gloves"),
    "e2": dict(seed="KANATA",
               tags=OTOKO + ", red hair, wolf cut, both gold eyes clearly visible, black work vest, black gloves, smirk",
               name="the red wolf-cut display handler in a black work vest"),
    "e3": dict(seed="MIKOTO",
               tags=OTOKO + ", black hair, bob cut, both red eyes clearly visible, usher vest, white shirt, necktie, black short shorts, black knee socks, cheerful smile",
               name="the black bob-haired usher in a vest, necktie and short shorts"),
    "boss": dict(seed="SERAPH",
                 tags=OTOKO + ", tall, light purple hair, long hair, both gold eyes clearly visible, white noble clothes, white cloak with gold trim, arrogant smile",
                 name="the tall light-purple-haired nobleman in white noble clothes and a cloak"),
}

PL = {
    "stage":    "auction stage, round rotating display platform, bright spotlight, gavel stand, dark audience seats with masked silhouettes, detailed background",
    "stage_empty": "auction stage at night after closing, empty seats, a single spotlight, detailed background",
    "backroom": "backstage dressing room, open wardrobe trunk, tall standing mirror, velvet chair, detailed background",
    "mirrors":  "backstage corridor lined with mirrors, dim gold lamps, detailed background",
    "loading":  "back loading entrance of the auction house at night, iron door, lantern, wrapped parcel, detailed background",
    "tailor":   "dressing room with a tailor's platform, tape measure, bolts of pale fabric, dress form, detailed background",
    "wing":     "stage wing, heavy velvet curtain, ropes, glimpse of the lit stage, detailed background",
    "office":   "auctioneer's private room, shelves of ledgers and wine bottles, leather sofa, lamp, detailed background",
    "aisle":    "aisle between dark audience seats leading to the stage, red carpet, exit door far away, detailed background",
    "appraisal": "appraisal room, white padded examination table, magnifying lamp, trays of instruments, detailed background",
    "vault":    "storage vault, velvet-lined shelves, wax-sealed boxes, cool light, detailed background",
    "appr_door": "appraisal room doorway, white examination table behind, detailed background",
    "chair":    "appraisal room, white leather examination chair with leg rests, detailed background",
    "display":  "exhibition room, glass display case, padded display table with velvet-lined cuffs, detailed background",
    "toolshelf": "back of the exhibition room, shelves of glass instruments and cases, detailed background",
    "elevator": "freight elevator with a metal grille, dim lamp, detailed background",
    "center":   "exhibition room, central padded display table, spotlights, detailed background",
    "front":    "front edge of the auction stage, footlights, dark audience with masked faces, detailed background",
    "lobby":    "auction house lobby, reception counter, brass bell, chandelier, masked guests in the background, detailed background",
    "lobby_door": "auction house lobby, tall exit doors, brass lock, detailed background",
    "ushers":   "small usher's waiting room beside the stage wing, small table, mirror, detailed background",
    "private":  "buyer's private booth, velvet walls, chaise longue, small table with a wine glass, detailed background",
    "carriage": "inside a luxurious carriage at night, velvet seats, window with passing street lamps, detailed background",
    "bedroom":  "nobleman's bedroom, huge canopy bed, white and gold, candlelight, detailed background",
}

CLOTHED = "the attacker keeps his clothes on, only the navy-haired man is dressed in the sheer white dress"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Auction_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, pen=False, insert=False, onani=False):
    """pen=責め手自身のペニスで貫く場面／insert=器具の挿入（融合防止のネガティブ）"""
    c = CH[who]
    body = PROT_BODY + ", " + OUTFIT
    if onani:
        pos = ", ".join([Q, "explicit", "1boy, solo focus, male focus", body,
                         "the navy-haired young man in a sheer white dress is the main subject in the foreground, he pleasures himself without touching his penis, both of his hands are clearly away from his penis, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         HOUSE, PL[place], desc])
    else:
        att = c["tags"] + (", his own penis exposed from his opened trousers" if pen else "")
        pos = ", ".join([Q, "explicit, cmnm, 2boys, duo, two people, yaoi",
                         "THE ATTACKER (taller, standing over him): " + att,
                         "THE NAVY-HAIRED MAN (smaller, clearly visible in the picture): " + body, action, CLOTHED, HOUSE, PL[place], desc])
    neg = NEG_BASE + NEG_SCENE + (NEG_INSERT if pen else NEG_NOPEN) + (", merged, fused" if insert else "") + (NEG_ONANI if onani else "")
    if pen:
        neg = neg.replace(", dildo, strap-on", "")
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "standing, raising the gavel in one hand, other hand on his chest, looking down at viewer, from below, elegant smile"),
    "e1": ("e1", "standing, holding a magnifying lens up toward viewer, other gloved hand raised, calm"),
    "e2": ("e2", "standing, twirling a small egg vibrator on a cord in one hand, smirk, other hand in his pocket"),
    "e3": ("e3", "standing, one hand cupped beside his mouth as if calling to the audience, winking, other hand waving"),
    "boss": ("boss", "standing tall, holding a small silver key on a chain toward viewer, looking down at viewer, from below, arrogant smile"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "full body, simple background, white background"]), NEG_BASE, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", "underground auction house stage, round display platform under a spotlight, gavel stand, "
                           "dark velvet audience seats, gold trim, detailed background"]), NEG_BASE)

# ---- 女装娘カード（出品衣装の男モンスター。主人公とは別人：茶髪の成人男性）
add("josou", "JOSOU", ", ".join([Q, "safe, solo, 1boy, adult male, adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, adam's apple, collarbones, flat male chest, crossdressing, otoko no ko, brown messy short hair, embarrassed, blush, looking away, "
                                 "sheer white chiffon dress, white garter stockings, red ribbon choker, gold chains on his wrists, holding down his skirt hem, full body, simple background, white background"]),
    NEG_BASE + ", 1girl, breasts", rembg=True)

# ---- 技CG
scene("atk_m1", "m", "stage",
      "he sits on the edge of the rotating display platform with the neckline of his dress pulled down, the auctioneer bends over him and licks his nipple, tongue out, one gloved hand holding his other nipple, spotlight",
      "the auctioneer tastes the merchandise in front of the audience.")
scene("atk_m2", "m", "backroom",
      "the auctioneer stands behind him fastening a red ribbon choker around his neck, the man is half dressed in the sheer white dress in front of the standing mirror, white stocking half rolled up his thigh, trembling",
      "the auctioneer dresses him in the exhibition outfit piece by piece.")
scene("atk_m3", "m", "stage",
      "from side, he lies on his back on the display platform with legs raised, neckline pulled down, small pink egg vibrators tied to his nipples with ribbons, the auctioneer stands between his legs and penetrates his anus with his own penis, anal sex, gavel in the auctioneer's hand",
      "the auctioneer tastes the merchandise before the final bid.", pen=True)
scene("atk_e1", "e1", "appraisal",
      "from side, he lies on his back on the white examination table with his skirt lifted and knees held up, the appraiser inserts two gloved fingers into his anus, anal fingering, other hand adjusting his monocle, calm",
      "the appraiser examines the merchandise's prostate.", insert=True)
scene("atk_e2", "e2", "display",
      "from side, he is strapped on the padded display table with velvet cuffs, skirt lifted, a beaded urethral sound inserted in his penis, urethral insertion, a thin glass rod in his anus, the handler holds the rod with a smirk",
      "the display handler plugs both holes for the exhibition.", insert=True)
scene("atk_e3", "e3", "front",
      "the usher stands at the front of the stage holding the navy-haired man's chin and kissing him deeply toward the audience, french kiss, tongues, saliva string, the man's neckline pulled open, the usher's other hand raised to the audience",
      "the usher shows the audience a kiss.")
scene("atk_boss", "boss", "private",
      "from side, he kneels on the chaise longue with his skirt lifted, a flat silver chastity disc on his crotch with a thin belt around his waist, the nobleman holds a small silver key on a chain and presses it to the man's lips, arrogant smile",
      "the nobleman marks his purchase with a chastity belt.")

# ---- 敗北28（主人公と主役の責め手）
L = [
 ("btl_m1", "m", "stage", "the auctioneer licks his nipple while he sits on the display platform with his neckline down, cum on his own thigh, a gold ribbon tied on his chest, spotlight, masked audience", {}),
 ("onani_m1", "m", "backroom", "he sits in front of the standing mirror rubbing his own nipples with wet fingers, the auctioneer stands behind him licking his other nipple over his shoulder, a red ribbon tied on the mirror frame", {}),
 ("inochi_m1", "m", "wing", "behind the velvet curtain the auctioneer holds him from behind, one gloved hand on his chin, tongue licking his nipple through the open neckline, a gold ribbon replacing the red one on his neck, gavel on a stand", {}),
 ("onedari_m1", "m", "office", "the auctioneer sits on the leather sofa with the man on his lap facing away, licking his nipple over his shoulder, a leather-bound ledger open on the table, the man begging", {}),
 ("btl_m2", "m", "backroom", "the auctioneer stands behind him tying the red ribbon choker, one gloved hand caressing his chest through the sheer chiffon, he trembles and climaxes in the mirror, open wardrobe trunk with a small key", {}),
 ("onani_m2", "m", "mirrors", "in the mirrored corridor he leans against a mirror rubbing his own nipples through the sheer dress, the auctioneer stands close behind him licking his neck, three reflections", {}),
 ("inochi_m2", "m", "loading", "at the iron back door the auctioneer holds out a newly unwrapped sheer dress, the man stands in another sheer dress hugging himself, a wax-sealed parcel on the floor, lantern", {}),
 ("onedari_m2", "m", "tailor", "he stands on the tailor's platform in a basted pale purple chiffon dress, the auctioneer wraps a tape measure around his chest and licks his exposed nipple, tape measure, dress form", {}),
 ("btl_m3", "m", "stage", "from side, he lies on his back on the rotating platform with legs raised, egg vibrators ribboned to his nipples, the auctioneer penetrates his anus with his own penis, anal sex, cum, a small black half mask on the man's face", {"pen": True}),
 ("onani_m3", "m", "stage_empty", "night, empty seats, from side, he lies on the platform under a single spotlight, the auctioneer kneels between his legs penetrating his anus with his own penis, anal sex, egg vibrators on his nipples, gold chains from his wrists to a ring on the platform", {"pen": True}),
 ("inochi_m3", "m", "aisle", "from side, in the aisle between the seats he is bent over a seat back with his skirt lifted, the auctioneer stands behind him with two oiled fingers in his anus, anal fingering, egg vibrators on his nipples, the exit door far away", {"insert": True}),
 ("onedari_m3", "m", "stage", "from side, beside the gavel stand he lies on his back begging, the auctioneer penetrates him deeply with his own penis, anal sex, egg vibrators on his nipples, the auctioneer raising the gavel", {"pen": True}),
 ("btl_e1", "e1", "appraisal", "from side, he lies on the white examination table with his skirt lifted and knees up, the appraiser presses two gloved fingers deep into his anus, anal fingering, magnifying lamp, cum on his belly, a wax seal on a document beside him", {"insert": True}),
 ("onani_e1", "e1", "vault", "from side, among velvet-lined shelves he kneels on the floor with his skirt lifted reaching back to finger his own anus, the appraiser stands behind him guiding his hand with a gloved hand, a white ribbon tied on a shelf", {"insert": True}),
 ("inochi_e1", "e1", "appr_door", "from side, in the doorway he leans on the frame with his skirt lifted, the appraiser kneels behind him with gloved fingers in his anus, anal fingering, a sealed document in the appraiser's other hand", {"insert": True}),
 ("onedari_e1", "e1", "chair", "from front, he sits in the white examination chair with his legs spread on the leg rests, skirt lifted, the appraiser between his legs with three gloved fingers in his anus, anal fingering, the man begging, a ribbon-tied appointment card", {"insert": True}),
 ("btl_e2", "e2", "display", "from side, he is cuffed on the padded display table, egg vibrator on his nipple, a beaded urethral sound in his penis, urethral insertion, a glass rod in his anus, the handler leaning on the glass case with a smirk, cum", {"insert": True}),
 ("onani_e2", "e2", "toolshelf", "from side, in front of the instrument shelves he kneels pressing his own perineum with one hand while his other fingers are in his anus, the handler crouches beside him holding out a beaded urethral sound, a small instrument case", {"insert": True}),
 ("inochi_e2", "e2", "elevator", "from side, in the freight elevator he leans against the grille with his skirt lifted, the handler kneels behind him inserting a thin glass rod into his anus, a beaded sound in his penis, urethral insertion, floor indicator lamp", {"insert": True}),
 ("onedari_e2", "e2", "center", "from side, he lies on the central display table begging, both holes plugged: a beaded urethral sound and a glass rod, the handler holds up a thicker rod with a smirk, spotlights", {"insert": True}),
 ("btl_e3", "e3", "front", "at the front of the stage the usher kisses him deeply toward the audience, french kiss, saliva, the man's neckline pulled open, the usher's knee-socked foot rubbing the man's crotch under the lifted skirt, footjob, a matching necktie on the man", {}),
 ("onani_e3", "e3", "lobby", "the navy-haired man sits on the reception counter sucking his own two fingers with his tongue out, other wet hand on his nipple, the usher stands beside the counter ringing a brass bell and grinning at the masked guests", {}),
 ("inochi_e3", "e3", "lobby_door", "at the tall exit door the usher pulls him back by the red ribbon choker and kisses him, french kiss, saliva string, the man's hand still on the brass door handle, a key on a chain around the usher's neck", {}),
 ("onedari_e3", "e3", "ushers", "in the small usher's room he sits on the table wearing a black usher vest over his sheer dress, the usher holds his chin and kisses him with tongue, the man holding a sheet of paper, mirror", {}),
 ("btl_boss", "boss", "private", "from side, he kneels on the chaise longue with his skirt lifted, silver chastity disc on his crotch, the nobleman penetrates his anus with his own penis while kissing him over his shoulder, anal sex, french kiss, a small key on a chain around the nobleman's neck", {"pen": True}),
 ("onani_boss", "boss", "private", "from side, he lies on the chaise longue with his skirt lifted, silver chastity disc on his crotch, his own two fingers in his anus, the nobleman sits at the head of the chaise holding his chin and kissing him, a velvet collar on the man's neck", {"insert": True}),
 ("inochi_boss", "boss", "carriage", "inside the carriage at night, he sits on the nobleman's lap facing away with his skirt lifted, silver chastity disc on his crotch, the nobleman penetrates his anus with his own penis, anal sex, holding a small key in front of the man's eyes, street lamp light through the window", {"pen": True}),
 ("onedari_boss", "boss", "bedroom", "on the canopy bed he lies on his back with legs raised, a new silver chastity disc with a gold crest on his crotch, the nobleman penetrates his anus with his own penis while kissing him, anal sex, french kiss, candlelight", {"pen": True}),
]
for key, who, place, action, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him his property.", **opt)

# ---- オナニーCG（その責め手の★得意技に合わせた自慰。ペニスには触れない）
ON = {
    "master": ("m", "backroom", "sitting in front of the standing mirror with his neckline pulled down, licking his own wet fingers and rubbing both nipples, not touching his penis, flushed, eyes closed"),
    "e1": ("e1", "appraisal", "from side, lying on the white examination table with his skirt lifted and knees up, two of his own fingers in his anus pressing forward, not touching his penis, flushed"),
    "e2": ("e2", "display", "from side, kneeling on the display table with his skirt lifted, one hand pressing up on his own perineum, other hand with fingers in his anus, not touching his penis, trembling"),
    "e3": ("e3", "front", "kneeling at the front of the stage sucking his own two fingers with his tongue out, other wet hand rubbing his nipple through the open neckline, not touching his penis, flushed"),
    "boss": ("boss", "private", "from side, kneeling on the chaise longue with his skirt lifted, a silver chastity disc on his crotch, one hand pressing his perineum and two fingers of the other hand in his anus, not touching his penis, drooling"),
}
for k, (who, place, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone in the attacker's style while the attacker watches from afar.", onani=True)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "raising the gavel high, other hand gesturing to the audience, looking at viewer, spotlight", "stage"),
    ("magic_2", "m", "holding up a sheer white chiffon dress and a red ribbon choker toward viewer, elegant smile", "backroom"),
    ("magic_3", "e3", "ringing a small brass bell with one hand and beckoning toward the stage wing with the other, cheerful", "wing"),
    ("magic_4", "e2", "leaning on the padded display table, snapping a velvet-lined cuff shut with one hand, smirk, looking at viewer", "display"),
    ("magic_5", "m", "standing at the gavel stand under a spotlight, masked silhouettes raising bidding paddles in the dark audience, looking at viewer", "stage"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", HOUSE, PL[place]]), NEG_BASE)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Auction", "images": images}, open(os.path.join(here, "auction_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
