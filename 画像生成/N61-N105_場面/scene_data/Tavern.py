# N66 妖精の酒場（Tavern）画像データ。登場人物は全員20歳以上。全員女性。帳簿・伝票・コースター・点検表は文字なし。
# 本編キャラ（ミレーヌ・カクテルフェアリー・グレープ／シトラス・踊り子サキュバス）は本編の立ち絵を見ずに、本文の手がかり
# （ミレーヌ＝妖精の店長・とても大きな胸／グレープ＝薄紫の羽・葡萄／シトラス＝レモン・気だるげ／踊り子＝薄衣のサキュバス）と役から決めた見た目。
# カクテルフェアリーはミレーヌの魔法で人間大に実体化した成人の妖精（小さく描かない）。
# 敗北28本は主人公が黒のエプロンドレス（白エプロン・白ヘッドドレス）の給仕娘のまま。給仕長ベティは緑のドレスで紛れないようにする。
MAID = "a black long-sleeved dress with a flared knee-length skirt, a white frilled apron tied with a big bow at the back, a white headdress, white stockings"
MAID_UP = MAID + ", the skirt hem lifted"
MAID_CHEST = MAID + ", the front buttons opened showing his flat chest"
MAID_BOTH = MAID + ", the front buttons opened showing his flat chest, the skirt hem lifted"
M = {"hero_outfit": MAID}
MU = {"hero_outfit": MAID_UP}
MC = {"hero_outfit": MAID_CHEST}
MB = {"hero_outfit": MAID_BOTH}
FAIRY_NEG = "minigirl, tiny fairy, size difference, doll-sized"

DATA = {
 "code": "Tavern",
 "world": "cozy fantasy fairy tavern at night, warm lamp light, wooden beams, rows of bottles on shelves, glowing fairy lights floating, detailed background",
 "bg": "interior of a cozy fantasy fairy tavern, long wooden bar counter with high stools, shelves of colorful bottles, upside-down glasses on the counter, round tables, warm lamps and floating fairy lights",
 "josou": "black apron dress with long sleeves, white frilled apron, white headdress, white stockings, no wig, holding a round tray to his chest",
 "chars": {
   "m": {"type": "woman", "jp": "ミレーヌ", "canon": True, "canon_img": "F13.png",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, long legs, tall, fairy, pointed ears, large translucent fairy wings, honey brown hair, long wavy hair, amber eyes, red lipstick, burgundy corset bodice, off-shoulder white blouse, long dark skirt, tavern owner, huge breasts",
         "name": "the honey-haired fairy tavern owner in a burgundy corset",
         "pose": "leaning on the counter edge with a cocktail glass in one hand, the other hand under her chest, relaxed alluring smile, looking at viewer"},
   "e1": {"type": "woman", "jp": "カクテルフェアリー・グレープ", "canon": True, "canon_img": "EU35.png",
          "tags": "adult woman, mature female, mature face, 22 years old, adult proportions, human-sized adult fairy, beautiful detailed eyes, long legs, pointed ears, light purple translucent fairy wings, purple hair, wavy medium hair, grape vine hair ornament, violet eyes, purple cocktail dress with a grape pattern, mischievous smile, medium breasts",
          "name": "the purple-haired grape fairy with light purple wings",
          "pose": "leaning forward with a finger at her lips, tongue slightly out, mischievous smile, looking at viewer",
          "neg": FAIRY_NEG},
   "e2": {"type": "woman", "jp": "カクテルフェアリー・シトラス", "canon": True, "canon_img": "EU36.png",
          "tags": "adult woman, mature female, mature face, 23 years old, adult proportions, human-sized adult fairy, beautiful detailed eyes, long legs, pointed ears, pale yellow translucent fairy wings, lemon yellow hair, short messy hair, lemon slice hair clip, orange eyes, half-closed eyes, loose yellow camisole dress, bored sleepy expression, medium breasts",
          "name": "the lemon-haired citrus fairy in a loose yellow dress",
          "pose": "yawning with one hand over her mouth, the other index finger raised lazily, sleepy half-closed eyes, looking at viewer",
          "neg": FAIRY_NEG},
   "e3": {"type": "woman", "jp": "給仕長 ベティ",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, long legs, red hair, hair bun, green eyes, green tavern dress, white apron, white headdress, rolled-up sleeves, holding a round tray, confident grin, large breasts",
          "name": "the red-haired head waitress in a green dress",
          "pose": "one hand on her hip, the other holding a round tray on her shoulder, confident grin, looking at viewer"},
   "boss": {"type": "woman", "jp": "踊り子サキュバス", "canon": True, "canon_img": "EU84.png",
            "tags": "adult woman, mature female, mature face, sharp adult features, 25 years old, adult proportions, beautiful detailed eyes, long legs, tall, succubus, curved black horns, bat wings, heart-tipped demon tail, pink hair, very long hair, gold eyes, belly dancer costume, sheer veils, gold jewelry, bare midriff, large breasts",
            "name": "the pink-haired dancer succubus in sheer veils",
            "pose": "dancing pose with one arm raised over her head, hips swayed to the side, veils flowing, sultry smile, looking at viewer"},
 },
 "places": {
   "counter":   "long wooden bar counter with high round stools, row of upside-down empty glasses, bottles on the backbar shelves, lamp light",
   "sink":      "tavern washing sink with rising steam, drying rack of upside-down glasses, cloths, wooden tub",
   "fireplace": "back room of the tavern, crackling fireplace, fur rug, upside-down glasses on the mantel, snowy night outside the window",
   "rooftop":   "rooftop lookout of the tavern at night, starry sky, wooden railing with upside-down glasses, lantern, town lights below",
   "blend":     "cocktail workroom and wine cellar, workbench with fruit baskets and small vials, wine barrels, dim warm light",
   "pantry":    "attic storeroom of the tavern, piled burlap sacks, narrow cot, dusty shelf with upside-down glasses, small window",
   "staff":     "staff changing room, lockers, row of hanging uniforms, tall standing mirror, wooden bench",
   "hall":      "tavern main hall, large round wooden table in the center, warm stage lights, bottles and glasses on the tables",
   "stage":     "small tavern stage with a wooden chair in the middle, musical instruments at the back, spotlight, red curtain",
   "office":    "tavern owner's private room upstairs, plush long sofa, desk with an open ledger without text, window with shelves of glasses",
   "booth":     "curtained sofa booth by a moonlit window, velvet curtain, low table with cocktail glasses and blank coasters without text",
   "terrace":   "starlit terrace behind the tavern, long wooden bench, railing with upside-down glasses, night sky",
   "yard":      "sunny backyard of the tavern, laundry swaying on lines, hammock in the tree shade, grass, tree stump",
   "dressing":  "backstage dressing room, vanity mirror surrounded by lamps, costumes on a rack, rug on the floor",
 },
 "atk": {
   "m1": ("counter", "he sits on a bar stool leaning back against the counter, the tavern owner kneels before him wrapping his erection in her huge breasts, clothed paizuri through her low neckline, soft slow squeezing, precum, blush"),
   "m2": ("fireplace", "he kneels on the fur rug, the tavern owner pours pink cocktail from a glass into her deep cleavage and pulls his face into it, he drinks from her cleavage, face buried in her breasts, liquor dripping, dazed"),
   "m3": ("counter", "he sits on the counter top, the tavern owner kisses him mouth to mouth feeding him honey liquor, tongues, liquor dripping from their lips, her fingers pinching both of his nipples, lamp light"),
   "e1": ("blend", "he sits on a stool at the workbench, the grape fairy leans on his back with her light purple wings spread, licking inside his ear, ear licking, her fingertips tickling his other ear, flushed, trembling", {"neg": FAIRY_NEG}),
   "e2": ("pantry", "he leans back against the burlap sacks, the citrus fairy lies lazily beside him propped on one elbow, flicking his nipple with one fingertip, bored sleepy face, his hips jerking", {"neg": FAIRY_NEG}),
   "e3": ("staff", "he stands before the tall standing mirror holding down his skirt hem, the head waitress stands behind him tying the apron bow at his back, sparkles of dressing magic around him, flushed, trembling", M),
   "boss": ("hall", "he sits on a chair beside the round table, the dancer succubus dances on the table above him, bending down to pinch both of his nipples and blow a warm breath into his ear, veils swaying, trembling"),
 },
 "atk_desc": {
   "m1": "the tavern owner squeezes him in her soft fluffy breasts.",
   "m2": "the tavern owner serves her special cocktail from her cleavage.",
   "m3": "the tavern owner feeds him liquor mouth to mouth after closing time.",
   "e1": "the grape fairy plays a prank on his ear with her tongue.",
   "e2": "the lazy citrus fairy flicks his nipple with one finger.",
   "e3": "the head waitress dresses him in the waitress uniform with magic.",
   "boss": "the dancer succubus performs a table dance on his nipples and ears.",
 },
 "lose": {
   # ミレーヌ 技1（とろふわの）
   "btl_m1":     ("sink", "he stands at the steaming sink holding a glass and a cloth, the tavern owner stands behind him resting her huge breasts on the backs of his hands, no hands on his penis, cum stain spreading on the front of his skirt", M),
   "onani_m1":   ("counter", "sitting alone on a stool at the counter, face buried in a soft folded cloth, one hand stroking his own chest over the apron, knees trembling, penis untouched, the tavern owner watches from the far end of the counter", M),
   "inochi_m1":  ("office", "he lies on the long sofa, the tavern owner lies over him pressing her huge breasts onto his chest in slow circles, no hands on his penis, cum on the white apron", MU),
   "onedari_m1": ("counter", "he sits on a stool at the counter in morning light, the tavern owner kneels before him squeezing his penis between her huge breasts under his lifted skirt, clothed paizuri, cum on her cleavage, blush", MU),
   # ミレーヌ 技2（特製カクテル）
   "btl_m2":     ("fireplace", "he kneels on the fur rug, the tavern owner hugs his face into her deep cleavage filled with pink cocktail, he drinks from her cleavage, liquor dripping down his chin, cum stain on his skirt", M),
   "onani_m2":   ("counter", "sitting alone on a high stool at the counter on a rainy night, a wet napkin pressed to his face, breathing in deeply, one hand stroking his own chest, penis untouched, the tavern owner watches from across the counter", M),
   "inochi_m2":  ("booth", "he lies on the booth sofa, the tavern owner holds his face close to her liquor-wet cleavage, he breathes in its sweet scent, no hands on his penis, cum dripping under his lifted skirt", MU),
   "onedari_m2": ("office", "he lies with his head on the tavern owner's lap on the long sofa, the tavern owner guides his face into her cleavage to sip the last drops of red liquor, cum dripping under his skirt, dazed", MU),
   # ミレーヌ 技3（閉店後の口移し）
   "btl_m3":     ("rooftop", "he sits on the tavern owner's lap on the rooftop lookout under the stars, the tavern owner kisses him mouth to mouth feeding him honey liquor, tongues, her fingers pinching both of his nipples, cum stain on his skirt", MC),
   "onani_m3":   ("counter", "standing alone at the dark counter lit by one lamp, sucking two of his own fingers as if kissing, the other hand pinching his own nipple through the opened dress, penis untouched, the tavern owner watches from the shadows", MC),
   "inochi_m3":  ("counter", "he sits on the dim counter top with a small key on a cord around his neck, the tavern owner stands between his knees kissing him deeply, tongues, liquor dripping from their lips, cum under his skirt", MC),
   "onedari_m3": ("booth", "he sits on the booth sofa by the moonlit window, the tavern owner bends down letting liquor flow from her lips onto his nipple and licking it, cum dripping, a stack of blank coasters without text", MB),
   # グレープ（いたずらの耳舐め）
   "btl_e1":     ("blend", "he sits on a stool at the workbench, the grape fairy hugs him from behind with her light purple wings spread, her tongue deep in his ear, ear licking, cum stain on his skirt, fruit baskets and vials", {"hero_outfit": MAID, "neg": FAIRY_NEG}),
   "onani_e1":   ("counter", "sitting alone at the counter, wet fingertips wiggling inside both of his own ears, head tilted, shoulders shivering, penis untouched, the grape fairy watches from the far end of the counter", {"hero_outfit": MAID, "neg": FAIRY_NEG}),
   "inochi_e1":  ("blend", "he slumps on the floor between wine barrels, the grape fairy leans on his back blowing a breath into his wet ear, her wings glittering, cum dripping under his skirt, trembling", {"hero_outfit": MAID_UP, "neg": FAIRY_NEG}),
   "onedari_e1": ("terrace", "he sits on the long bench of the starlit terrace with a grape leaf pinned to his headdress, the grape fairy presses her lips to his ear whispering, cum stain under his skirt, glittering wings", {"hero_outfit": MAID, "neg": FAIRY_NEG}),
   # シトラス（めんどくさがりの乳首いじり）
   "btl_e2":     ("pantry", "he leans back against the burlap sacks with his dress opened, the citrus fairy lies asleep beside him with one fingertip resting on his nipple, cum on the white apron, dusty upside-down glasses on the shelf", {"hero_outfit": MAID_CHEST, "neg": FAIRY_NEG}),
   "onani_e2":   ("counter", "lying alone on his back on a rug before the counter with his dress opened, lazily flicking his own nipple with one finger, limp and relaxed, penis untouched, the citrus fairy watches lying on the counter with her chin in her hand", {"hero_outfit": MAID_CHEST, "neg": FAIRY_NEG}),
   "inochi_e2":  ("pantry", "he lies on the narrow cot with his dress unbuttoned, the citrus fairy lies beside him with eyes closed flicking his nipple with one finger, yawning, cum dripping under his skirt", {"hero_outfit": MAID_BOTH, "neg": FAIRY_NEG}),
   "onedari_e2": ("yard", "he kneels on the grass beside the hammock with his dress opened, the citrus fairy lies in the hammock flicking his nipple with a wet fingertip, laundry swaying, cum stain under his skirt", {"hero_outfit": MAID_CHEST, "neg": FAIRY_NEG}),
   # ベティ（給仕服の着付け）
   "btl_e3":     ("staff", "he stands before the tall standing mirror, the head waitress stands behind him refastening one button at the back of his dress, his body jolting, cum stain on his skirt, lockers and hanging uniforms", M),
   "onani_e3":   ("counter", "standing alone by the counter with a mop leaning beside him, stroking his own thighs and bottom over the skirt, knees trembling, penis untouched, the head waitress watches holding a blank checklist without text", M),
   "inochi_e3":  ("staff", "he stands before the tall mirror lifting his skirt hem, the head waitress stands behind him retying his apron bow tight at the waist, his headdress tilted, cum soaking the white apron", MU),
   "onedari_e3": ("counter", "he stands behind the counter holding a tray, the head waitress sits on a stool beside him sliding her shoe under his lifted skirt, footjob, a glass of cider on the counter, cum dripping", MU),
   # 踊り子サキュバス（テーブルダンス）
   "btl_boss":   ("hall", "he sits on top of the round table, the dancer succubus hugs him from behind pinching both of his nipples through his opened dress and blowing into his ear, veils swaying, cum on the tabletop", MB),
   "onani_boss": ("stage", "standing alone on the small stage, swaying his hips to music and pinching both of his own nipples through the opened dress, head tilted as if breath were on his ear, penis untouched, the dancer succubus watches sitting far away on the counter", MC),
   "inochi_boss":("stage", "he sits on the wooden chair in the middle of the stage, the dancer succubus sits on his lap facing him, pinching his nipples and breathing into his ear, veils over them, cum under his skirt", MB),
   "onedari_boss":("dressing", "he sits on the rug before the lamp-lit vanity mirror, the dancer succubus sways her hips right in front of his face with honey liquor pooled in her navel, no hands on him, cum dripping under his skirt", MU),
 },
 "lose_desc": "keeps him in the fairy tavern as its poster waitress in a black apron dress.",
 "onanie": {
   "master": ("counter", "sipping sweet liquor from a glass, then burying his face in a damp cloth breathing in, one hand stroking his own chest, penis untouched"),
   "e1": ("blend", "wet fingertips tickling inside his own ears, head tilted, shoulders shivering, penis untouched", {"neg": FAIRY_NEG}),
   "e2": ("pantry", "lying on his back on the burlap sacks, lazily flicking his own nipple with one finger, limp, penis untouched", {"neg": FAIRY_NEG}),
   "e3": ("staff", "standing before the mirror in the waitress dress, stroking his own thighs and bottom over the skirt, penis untouched", M),
   "boss": ("hall", "swaying his hips as if to music, pinching both of his own nipples, head tilted as if breath were on his ear, penis untouched"),
 },
 "magic": {
   "1": ("m", "counter", "the tavern owner holds out a glowing pink cocktail glass across the counter, today's recommendation, wink"),
   "2": (None, "staff", "a folded black dress with a white frilled apron and a white headdress laid neatly on a wooden bench, tied with a ribbon, soft light"),
   "3": ("e1", "blend", "the grape fairy spreads her glittering light purple wings, sparkling purple illusion dust swirling around her, mischievous smile"),
   "4": (None, "counter", "a small silver service bell on the counter glowing with fairy light, tiny sparkles rising"),
   "5": ("m", "hall", "the tavern owner opens her arms in welcome in the warmly lit tavern hall, glowing glasses floating around her, fairy lights"),
 },
}
