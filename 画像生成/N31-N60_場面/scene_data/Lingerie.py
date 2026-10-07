# N49 会員制ランジェリー（Lingerie）場面データ。登場人物は全員20歳以上。女性とニューハーフの混合（ヴィオレ・ジゼル＝NH）。敗北28本は主人公が黒いレースの下着姿のまま。
LACE = "black lace lingerie, black lace bra, black lace panties, black garter belt, black thighhigh stockings"
LACE_BACK = LACE + ", the back of the panties pulled aside"
CORSET = LACE + ", a tight black corset laced around his waist"
CORSET_BACK = CORSET + ", the back of the panties pulled aside"
DATA = {
 "code": "Lingerie",
 "world": "exclusive members-only lingerie boutique in a back alley at night, lace and silk, roses, soft warm light, detailed background",
 "chars": {
   "m":    {"type": "nh", "tags": "adult woman, mature female, mature face, sharp adult features, 40 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, light purple hair, long wavy hair, gold eyes, light purple silk dress, tape measure around neck, large breasts",
            "name": "the light-purple-haired designer in a silk dress"},
   "e1":   {"type": "woman", "tags": "adult woman, mature female, mature face, sharp adult features, 23 years old, adult proportions, beautiful detailed eyes, long legs, pink hair, twintails, brown eyes, white shop uniform, tape measure around neck, large breasts",
            "name": "the pink-twintailed fitter in a white shop uniform"},
   "e2":   {"type": "nh", "tags": "adult woman, mature female, mature face, sharp adult features, 25 years old, adult proportions, beautiful detailed eyes, tall, elegant, feminine body, long legs, blonde hair, long wavy hair, green eyes, gold satin blouse, tight skirt, medium breasts",
            "name": "the blonde saleswoman in a gold satin blouse"},
   "e3":   {"type": "woman", "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, long legs, brown hair, tied up hair, amber eyes, wine red apron dress, pincushion bracelet, medium breasts",
            "name": "the brown-haired seamstress in a wine red apron dress"},
   "boss": {"type": "woman", "tags": "adult woman, mature female, mature face, sharp adult features, 42 years old, adult proportions, beautiful detailed eyes, long legs, black hair, long hair, red eyes, black corset dress, long gloves, very large breasts, voluptuous",
            "name": "the black-haired owner in a black corset dress"},
 },
 "places": {
   "fitting":  "fitting room with a tall gold-framed full-length mirror, velvet curtain, cushioned chair, lingerie on hangers",
   "triple":   "fitting room surrounded by a three-way mirror, velvet chaise longue, soft carpet",
   "atelier":  "atelier with dress forms and torsos, bolts of silk, lace samples, a basket of folded clothes",
   "counter":  "shop counter with rolls of silk fabric, a ledger without text, a fountain pen, rose vase",
   "measure":  "bright white measuring room, round mirror, round measuring stool, measurement board without text",
   "floor":    "boutique sales floor after closing, velvet round stool, lingerie displays, mannequins in lace",
   "repair":   "basement alteration room, spools of thread, fabric scissors, wooden worktable, wall mirror",
   "salon":    "second-floor private salon, crimson velvet walls, black leather sofa, candlelight",
   "window":   "display window stage behind heavy curtains, round pedestal, glass pane, soft spotlight",
 },
 "atk": {
   "m1": ("fitting", "he sits on the cushioned chair before the tall mirror blindfolded with a light purple silk scarf, the designer stands behind him whispering into his ear, the silk scarf sliding over his chest, trembling"),
   "m2": ("atelier", "he stands among the torsos, the designer stands behind him fastening a black lace bra on his chest, a faint gold glow from her fingertips, pinching his nipple through the lace, flushed", {"hero_outfit": LACE}),
   "m3": ("fitting", "from side, he sits on the designer's lap facing the tall mirror, the designer penetrates his anus with her own penis from below, anal, kissing him from behind, his own penis separate, precum", {"pen": "penis", "hero_outfit": LACE_BACK}),
   "e1": ("measure", "he stands with his chest out, the fitter wraps a white tape measure around his nipple and pulls it tight, the other nipple pinched by her fingers, swollen red nipples, trembling"),
   "e2": ("floor", "he sits on the velvet round stool, the saleswoman kneels before him clipping a garter clasp onto his stocking with a snap, her hand stroking his inner thigh, trembling", {"hero_outfit": LACE}),
   "e3": ("repair", "he is on all fours on the wooden worktable, the seamstress stands behind him with two fingers in his anus, fingering, her other hand pressing his back down, pincushion bracelet, calm face"),
   "boss": ("salon", "he lies back on the black leather sofa, the owner pulls the corset laces tight with one hand, her lips sucking his nipple, pulling a string of black anal beads from his anus", {"pen": "toy", "hero_outfit": CORSET_BACK}),
 },
 "atk_desc": {
   "m1": "the designer whispers in silk and unties his thoughts.",
   "m2": "the designer dresses him in black lace lingerie.",
   "m3": "the designer takes him in front of the full-length mirror.",
   "e1": "the fitter tightens her tape measure around his nipples.",
   "e2": "the saleswoman snaps the garter clasps on his stockings.",
   "e3": "the seamstress alters him on the inside with her fingers.",
   "boss": "the owner laces his corset and pulls the anal beads out.",
 },
 "lose": {
   # デザイナー 技1（シルクの囁き）
   "btl_m1":     ("fitting", "he sits in the chair before the tall mirror blindfolded with a light purple silk scarf, the designer behind him whispering into his ear, her fingers pinching his nipple through the lace, cum soaking the lace panties", {"hero_outfit": LACE}),
   "onani_m1":   ("fitting", "standing alone before the tall mirror, stroking his own chest over the lace, one hand behind pressing his bottom through the panties, dazed, penis untouched, the designer watches from the curtain", {"hero_outfit": LACE}),
   "inochi_m1":  ("counter", "he leans against the shop counter, the designer behind him whispering into his ear, a roll of silk wound around his crotch over the lace panties, a signed slip without text on the counter, cum stain", {"hero_outfit": LACE}),
   "onedari_m1": ("fitting", "he stands before the mirror with his lips parted, the designer hugs him from behind whispering into his ear, her palm gliding over the front of his lace panties, cum stain on the lace", {"hero_outfit": LACE}),
   # デザイナー 技2（ランジェリーの着付け）
   "btl_m2":     ("atelier", "he stands among the torsos with his clothes folded in a basket, the designer pinches both of his nipples through the lace bra, her knee pressing the front of his panties, stockings trembling, cum on the lace", {"hero_outfit": LACE}),
   "onani_m2":   ("fitting", "sitting alone on the carpet before the mirror, pulling a black stocking up his own leg, stroking his own thigh up to the garter, flushed, penis untouched, the designer watches through the curtain gap", {"hero_outfit": LACE}),
   "inochi_m2":  ("atelier", "he stands with black ribbons tied in bows on his lace bra and panties, the designer tugs the ribbon bows tight, his cotton shirt fallen on the floor, cum on the lace", {"hero_outfit": LACE + ", ribbon bows"}),
   "onedari_m2": ("atelier", "he stands in the arms of the designer among the torsos, the designer pinches both of his nipples through the embroidered lace bra from behind, her knee lifting the front of his panties, trembling", {"hero_outfit": LACE}),
   # デザイナー 技3（姿見の前で・NH）
   "btl_m3":     ("fitting", "from side, he lies on the carpet before the tall gold-framed mirror with legs lifted, the designer over him penetrating his anus with her own penis, anal, kissing him deeply, his own penis separate, cum in the lace", {"pen": "penis", "hero_outfit": LACE_BACK}),
   "onani_m3":   ("fitting", "kneeling alone before the tall mirror with his hips raised, one arm reaching behind with two of his own fingers in his own anus through the pulled-aside panties, penis untouched, the designer watches from behind the curtain", {"hero_outfit": LACE_BACK}),
   "inochi_m3":  ("fitting", "from side, he lies on a chaise before the tall mirror with his arms around the designer, the designer penetrates his anus with her own penis, anal, kissing him deeply, his own penis separate, cum on the lace", {"pen": "penis", "hero_outfit": LACE_BACK}),
   "onedari_m3": ("triple", "from side, he is held with his legs lifted high inside the three-way mirror, the designer penetrates his anus with her own penis, anal, kissing him, his own penis separate, reflections of the two", {"pen": "penis", "hero_outfit": LACE_BACK}),
   # 採寸係 ルル（メジャーの締めつけ）
   "btl_e1":     ("measure", "he stands with his chest out, the lace bra cup pulled down, the fitter slides a white tape measure across both of his nipples like a bowstring, swollen red nipples, cum soaking the lace panties", {"hero_outfit": LACE}),
   "onani_e1":   ("measure", "standing alone before the round mirror, a thin satin ribbon wrapped around his own chest, pulling it tight over his nipples, knees trembling, penis untouched, the fitter peeks from the door", {"hero_outfit": LACE}),
   "inochi_e1":  ("measure", "he sits on the round stool, the fitter sits on his lap with a white tape measure looped around both of his nipples, tugging it, kissing him, a measurement slip without text", {"hero_outfit": LACE}),
   "onedari_e1": ("measure", "he lies on a measuring bench wearing an open-cup lace bra, the fitter leans over kissing him, a white tape measure tied tight around his nipple, cum on the lace panties", {"hero_outfit": LACE + ", open-cup bra"}),
   # 販売員 ジゼル（ガーターを留める）
   "btl_e2":     ("floor", "he slumps on the velvet sofa with his legs open, the saleswoman kneels before him unclasping and clasping his garter clasp with a snap, no other touch, his stockinged legs twitching", {"hero_outfit": LACE}),
   "onani_e2":   ("fitting", "sitting alone on the chair before the mirror, unclasping and clasping his own garter clasp, stroking his own inner thigh, hips sinking, penis untouched, the saleswoman watches from the curtain with a tea tray", {"hero_outfit": LACE}),
   "inochi_e2":  ("fitting", "he sits cornered on the fitting room sofa, the saleswoman sits opposite pressing the front of his lace panties with her beige stocking soles, footjob, her fingers pinching his garter clasp, cum on the lace", {"hero_outfit": LACE}),
   "onedari_e2": ("floor", "he sits on the velvet round stool wearing a six-strap garter belt, the saleswoman sits before him squeezing his crotch through the lace with her stocking toes, footjob, snapping his garter clasps", {"hero_outfit": LACE + ", six-strap garter belt"}),
   # お直し係 ノエル（お直しの指）
   "btl_e3":     ("repair", "he is on all fours on the wooden worktable, the seamstress stands behind him with two fingers in his anus through a slit cut in his panties, her other hand on his back, cum dripping into the lace", {"hero_outfit": LACE_BACK}),
   "onani_e3":   ("repair", "kneeling alone before the wall mirror, one arm reaching behind with two of his own fingers in his own anus, the panties pulled aside, penis untouched, the seamstress watches from the shelves holding a spool", {"hero_outfit": LACE_BACK}),
   "inochi_e3":  ("repair", "he lies on his back on the worktable holding his knees, the seamstress holds his ankle up with one hand, two fingers of her other hand in his anus, staring at his face, cum in the lace", {"hero_outfit": LACE_BACK}),
   "onedari_e3": ("repair", "he leans on a dress form with his hips out, a lace window opened on the back of his panties, the seamstress behind him with two fingers in his anus, holding his hip, cum dripping", {"hero_outfit": LACE_BACK}),
   # オーナー ベアトリス（コルセットの紐）
   "btl_boss":   ("salon", "he lies back on the black leather sofa, the owner pulls the corset laces tight, sucking his nipple, pulling a string of black anal beads out of his anus, cum bursting into the lace", {"pen": "toy", "hero_outfit": CORSET_BACK}),
   "onani_boss": ("salon", "kneeling alone before a gold-framed mirror, a black satin sash tied tight around his own waist, one wet finger on his nipple, the other hand reaching behind with fingers in his own anus, penis untouched, the owner watches from the door", {"hero_outfit": LACE_BACK}),
   "inochi_boss":("window", "he stands on the round pedestal with both hands on the glass, bent forward, the owner behind him pulling the corset laces tight and sucking his nipple, black anal beads in his anus", {"pen": "toy", "hero_outfit": CORSET_BACK}),
   "onedari_boss":("salon", "he kneels across the lap of the owner seated on the sofa, the owner pulls his corset laces, sucking his nipple, pulling black anal beads from his anus, cum in the lace", {"pen": "toy", "hero_outfit": CORSET_BACK}),
 },
 "lose_desc": "keeps him in black lace as a mannequin of the boutique.",
 "onanie": {
   "master": ("fitting", "standing before the tall mirror, stroking his own chest and thighs with a silk scarf, head tilted as if listening to a whisper, dazed, penis untouched"),
   "e1": ("measure", "a thin satin ribbon looped around his own chest, pulling it tight over both of his nipples, swollen nipples, penis untouched"),
   "e2": ("fitting", "sitting on the chair, snapping his own garter clasp on his black stocking, stroking his own inner thigh, penis untouched", {"hero_outfit": LACE}),
   "e3": ("repair", "kneeling on the worktable with his hips raised, one arm reaching behind with two of his own fingers in his own anus, penis untouched"),
   "boss": ("salon", "a black satin sash tied tight around his own waist, one wet finger rubbing his nipple, the other hand reaching behind with fingers in his own anus, penis untouched"),
 },
}
