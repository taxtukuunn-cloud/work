# N135 工房とサキュバスの城（LostF）画像データ。登場人物は全員20歳以上。5人とも大人の女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。
# 人魚姫：原作は青い髪 → lavender hair に置き換え（瞳は光のない灰色、尾は真珠色と薄紫）。
# ダークエルフ姫：原作の本気の姿は青紫の肌 → 絵では lilac-purple の気配（dark violet aura）として描く。立ち絵は白い肌のエルフの姿。
# 挿入扱いはダークエルフ姫の細い暗黒蔦だけ（pen なし）。リーシャ・サキュバスクイーン・フォーチュンは指まで。人魚姫は後ろに触れない。
# サキュバスクイーンのダミー（分身）は「3人以上を出さない」ため本体1人だけで描く（乳首・首筋・後ろを1人と尻尾で）。
# 金輪も蔦も締めつけない。剣は飾りだけ。水の中でも息ができる（苦しそうにしない）。絵には金色の欠片か鐘を必ず一つ入れる。
SHARD = "a glowing pale gold crystal shard on a cord around his neck"
POUCH = "a leather pouch of glowing pale gold crystal shards beside him"
RINGS = "smooth gold rings floating loosely around his wrists and ankles"
VINE = "soft dark violet vines wrapped loosely around his wrists and ankles"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary"
VINE_NEG = SOFT_NEG + ", thorns, tight bondage, rope marks, wound"
MER_NEG = SOFT_NEG + ", legs on the mermaid, human legs, drowning, choking"
DATA = {
 "code": "LostF",
 "world": "fantasy role-playing game world of memory fragments, cozy wooden workshop, adventurer guild town, distant dark castle with heart crests, warm light, floating pale gold crystal shards, detailed background",
 "bg": "interior of a cozy craft workshop, wooden workbench with metal fittings and tools, fireplace with a crackling fire, a brass bell hanging by the window, through the window a town of roofs and a distant dark castle, warm morning light, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "リーシャ",
         "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, long legs, pale skin, pale gold blonde hair, very long straight hair, gentle green eyes, soft kind expression, white and brown workshop dress with an open neckline, cleavage, brown corset, long skirt, soft curvy feminine body, huge breasts",
         "name": "the long pale-gold-haired workshop mistress in a white and brown dress",
         "pose": "both hands held out as if welcoming someone home, gentle caring smile, looking at viewer, a glowing pale gold crystal shard floating above her palm",
         "neg": SOFT_NEG + ", sword swing, weapon attack"},
   "e1": {"type": "woman", "jp": "フォーチュン",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, dark purple hair, long wavy hair, violet eyes, calm composed face, embroidered ethnic dress, sheer veil, gold bangles, a softly glowing crystal ball floating beside her, soft curvy feminine body, huge breasts",
          "name": "the brown-skinned fortune teller in an embroidered ethnic dress",
          "pose": "one hand raised under a floating glowing crystal ball, the other index finger pointing at the viewer, calm quiet smile, looking at viewer",
          "neg": SOFT_NEG},
   "e2": {"type": "woman", "jp": "人魚姫",
          "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, pale skin, lavender hair, very long wavy hair, wet hair, empty dull grey eyes, no highlights in eyes, gentle polite smile, pearl necklace, white shell bikini top, mermaid, fish tail with pearl-white and lilac scales below the waist, soft curvy feminine body, huge breasts",
          "name": "the lavender-haired mermaid princess with empty grey eyes",
          "pose": "sitting on a rock at the water's edge with her fish tail curled, both wet arms reaching out toward the viewer, polite smile with empty eyes, looking at viewer",
          "neg": MER_NEG},
   "e3": {"type": "woman", "jp": "ダークエルフ姫",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, long legs, bare legs, barefoot, pure white skin, silver-white hair, long straight hair, long pointy elf ears, droopy wine-red eyes, gentle droopy-eyed smile, silver circlet, white elven queen gown with a high slit, faint dark violet aura, soft curvy feminine body, large breasts",
          "name": "the silver-white-haired elf queen in a white gown",
          "pose": "holding out a blank rolled parchment without text in one hand, the other hand at her lips, innocent droopy-eyed smile, a thin dark violet vine curling behind her, looking at viewer",
          "neg": VINE_NEG + ", kicking, stomping"},
   "boss": {"type": "woman", "jp": "サキュバスクイーン",
            "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, tall, long legs, dark-skinned female, brown skin, pink hair, long twintails, yellow eyes, playful grin, gold crown, revealing black and pink princess outfit, black thighhighs, gold bracelets, black demon tail with a heart-shaped tip, succubus, soft curvy feminine body, huge breasts",
            "name": "the pink-haired succubus princess with a heart-tipped tail",
            "pose": "spinning a gold ring around one finger, the other hand on her hip, her heart-tipped tail raised, playful teasing grin, looking at viewer",
            "neg": SOFT_NEG + ", kicking"},
 },
 "places": {
   "workshop": "cozy craft workshop, wooden workbench, metal fittings and tools, fireplace, long bench, a brass bell hanging by the window",
   "bedroom":  "workshop bedroom, a single bed with a hand-sewn quilt, window with morning light, hanging dried cloth",
   "guild":    "adventurer guild hall, quest board with blank papers without text, reception counter, wooden floor",
   "forest":   "damp green forest, mossy ground, tree branches, a white elven house far between the trees",
   "manor":    "elven manor guest room, white pillars, a white bed, sweet heavy dark violet haze near the floor",
   "beach":    "seashore, white sand, gentle waves, a warm tide pool among rocks",
   "cove":     "quiet mermaid cove, rocks around still water, a flat rock seat, soft light under the water",
   "town":     "castle town market, rows of roofs, spice stalls, stone pavement",
   "alley":    "back alley behind the market, stacked wooden crates, a tent cloth visible at the end",
   "tent":     "fortune teller tent interior, woven ethnic tapestries, incense smoke, thick rugs, pale glow of a floating crystal ball",
   "gate":     "black castle gate with a heart crest, the beginning of a red carpet",
   "corridor": "castle second-floor corridor, red carpet, stone pillars, wall candles",
   "top":      "castle top floor throne room, a princess throne, red carpet, tall windows",
   "queenbed": "princess bedroom, pink canopy bed, heart-shaped cushions, spotless tidy room, a washbasin with soap",
   "basement": "workshop basement, a floating glowing panel of light without text, a single chair, quiet pale white glow",
   "shrine":   "white room at the back of the workshop, a large bed, a battle dress and a sheathed sword displayed on a stand, soft warm light",
 },
 "atk": {
   "m1": ("basement", "he sits on the chair before the floating glowing panel without text, the workshop mistress stands behind him, one hand touching the panel, her other arm around his chest stroking his nipple, whispering at his ear, his head leaning back on her breasts, " + SHARD),
   "m2": ("shrine", "he lies on the large bed with his face held against her breasts, the workshop mistress embraces him, one hand gently stroking his nipple, two oiled fingers of her other hand in his anus, fingering, caring smile, " + SHARD),
   "m3": ("shrine", "he sits on the workshop mistress's lap on the bed, the workshop mistress with darkened glowing eyes kisses him deeply without letting go, tongues, saliva, her oiled fingers in his anus, fingering, her other hand holding the back of his head, " + SHARD),
   "e1": ("tent", "he kneels on the thick rug with his shirt open, the fortune teller sits before him pointing one fingertip close to his nipple without touching, her crystal ball glowing beside them, calm smile, his body trembling in wait, " + POUCH),
   "e2": ("cove", "he sits waist-deep in the still water, the mermaid princess wraps her wet arms around his neck, pressing his face between her breasts, breast smother, her fish tail curled around him, kissing the top of his head, " + SHARD),
   "e3": ("manor", "he stands with his arms raised, " + VINE + ", toes barely touching the floor, the elf queen sits before him stroking his chest with her bare foot, toes on his nipple, a thin smooth vine in his anus, dark violet haze, " + SHARD),
   "boss": ("top", "he stands on the red carpet, " + RINGS + ", the succubus princess presses against his back stroking both his nipples, her heart-tipped tail caressing his cheek, playful grin, his knees trembling, " + SHARD),
 },
 "atk_desc": {
   "m1": "the workshop mistress rewrites his settings on a glowing panel while holding him close.",
   "m2": "the workshop mistress cares for him in a dependent embrace, his face in her breasts, her fingers pressing deep.",
   "m3": "the workshop mistress in her darker form seals his lips with an endless kiss while her fingers press inside.",
   "e1": "the fortune teller foretells the exact moment and place he will come, and it always comes true.",
   "e2": "the mermaid princess clings to him and wraps his face in her breasts, calling him her prince.",
   "e3": "the elf queen hangs him in soft dark vines, strokes his chest with her bare foot and slips a thin vine inside.",
   "boss": "the succubus princess holds him still with magic gold rings and strokes him all over.",
 },
 "lose": {
   # リーシャ 技1（管理者権限＋★一つになりましょう）
   "btl_m1":     ("basement", "he sits on the workshop mistress's lap on the chair before the floating glowing panel without text, the workshop mistress holds his face to her breasts, one hand rolling his nipple, two oiled fingers in his anus, fingering, cum dripping untouched, " + SHARD),
   "onani_m1":   ("bedroom", "lying alone on the bed under the quilt, one hand rubbing his own nipple, a wet finger of the other hand in his own anus, lips murmuring, penis untouched, " + POUCH + ", the workshop mistress watches far away from the doorway"),
   "inochi_m1":  ("guild", "behind the empty reception counter, he leans back in the workshop mistress's arms, the workshop mistress holds a blank quest paper without text in one hand, her other hand under his open shirt stroking his nipple, gentle smile, his knees giving way, " + SHARD),
   "onedari_m1": ("shrine", "he lies on the large bed looking up, the workshop mistress sits beside him holding him to her chest, a floating glowing panel without text above them, her finger touching it, her other hand with oiled fingers in his anus, fingering, cum on his stomach, " + SHARD),
   # リーシャ 技2（★一つになりましょう）
   "btl_m2":     ("shrine", "he lies undressed on the large bed, his face buried in the workshop mistress's breasts, the workshop mistress holds him tightly, stroking his nipple with one hand, two oiled fingers pressing deep in his anus, fingering, a warm cloth and a comb beside them, cum on his stomach, " + SHARD),
   "onani_m2":   ("bedroom", "lying alone on the bed hugging a pillow with his face buried in it, one hand gently stroking his own nipple, the other hand reaching behind with a finger in his own anus, penis untouched, " + POUCH + ", the workshop mistress watches far away from the doorway"),
   "inochi_m2":  ("workshop", "on the long bench beside the workbench, he lies with his head on the workshop mistress's lap, the workshop mistress combs his hair with one hand, her other hand inside his open shirt rolling his nipple, his coat folded on her arm, fireplace glow, " + SHARD),
   "onedari_m2": ("shrine", "he sits curled in the workshop mistress's arms on the bed, the workshop mistress hugging him from the front, his cheek on her breasts, two oiled fingers of her hand in his anus, fingering, her other hand stroking his nipple, cum dripping, " + SHARD),
   # リーシャ 技3（降魔の口づけ＋★一つになりましょう）
   "btl_m3":     ("shrine", "he lies on his back on the large bed, the workshop mistress with darkened glowing eyes lies over him kissing him deeply, tongues, saliva trail, her oiled fingers in his anus, fingering, a sword ornament cord tied on his wrist, cum on his stomach, " + SHARD),
   "onani_m3":   ("basement", "sitting alone on the chair before the flickering glowing panel without text, sucking two of his own fingers as if kissing, the other hand reaching behind pressing a finger in his own anus, penis untouched, " + POUCH + ", the workshop mistress watches far away from the stairs"),
   "inochi_m3":  ("workshop", "he stands pressed back against the workbench, the workshop mistress with darkened glowing eyes holds his face in one hand kissing him deeply, tongues, her other hand behind him with oiled fingers in his anus, fingering, the brass bell swinging by the window, cum dripping"),
   "onedari_m3": ("shrine", "he lies on one half of the large bed on his side facing the workshop mistress, the workshop mistress kisses him deeply holding the back of his head, tongues, saliva, her arm around his waist with oiled fingers in his anus, fingering, cum dripping, " + SHARD),
   # フォーチュン（★必ず当たる占い）
   "btl_e1":     ("tent", "he lies on his back on the thick rug with his shirt open, the fortune teller kneels beside him touching his nipple with one fingertip at the foretold moment, her crystal ball glowing above, calm smile, cum on his stomach untouched, a crystal orb pendant on his neck"),
   "onani_e1":   ("alley", "crouching alone behind the stacked wooden crates, a wet finger of one hand in his own anus, counting under his breath, hips trembling, penis untouched, " + POUCH + ", the fortune teller watches far away at the end of the alley"),
   "inochi_e1":  ("tent", "he kneels on the rug in the tent behind the market, the fortune teller sits behind him, one hand lifting his chin toward the glowing crystal ball, the fingertip of her other hand on his nipple, calm smile, cum dripping untouched, " + SHARD),
   "onedari_e1": ("tent", "he sits before the floating crystal ball with his shirt open, the fortune teller sits close beside him holding up three fingers, her other fingertip circling his nipple, his back arched, cum dripping untouched, incense smoke, " + SHARD),
   # 人魚姫（★ずっと大切にします）
   "btl_e2":     ("cove", "underwater in the calm cove, he floats relaxed in the mermaid princess's arms, the mermaid princess presses his face between her breasts, breast smother, kissing his forehead, her fish tail coiled around his legs, bubbles, a glowing shell necklace on his neck, cum drifting in the water"),
   "onani_e2":   ("beach", "sitting alone in the warm tide pool, hugging a pillow to his chest with his face buried in it, rubbing his nipples against the pillow, hips shifting, penis untouched, " + POUCH + ", the mermaid princess watches far away from the waves"),
   "inochi_e2":  ("cove", "in the shallows of the cove, he kneels in the water, the mermaid princess clings to him from the front with wet arms around his neck, kissing him, her breasts pressed to his chest, her fish tail around his waist, cum dripping untouched, " + SHARD),
   "onedari_e2": ("cove", "underwater on a bed of soft seaweed, he lies in the mermaid princess's embrace, the mermaid princess kisses him on the lips, his cheek pressed against her swaying breasts, her fish tail curled around him, bubbles, cum drifting in the water, " + SHARD),
   # ダークエルフ姫（★暗黒蔦拘束）
   "btl_e3":     ("manor", "he hangs upright with arms raised, " + VINE + ", toes barely touching the floor, the elf queen sits on the white bed stroking his nipple with her bare toes, a thin smooth vine in his anus, dark violet haze, a dark leaf ornament on his neck, cum dripping untouched"),
   "onani_e3":   ("forest", "standing alone under a tree, one wrist hung loosely in a cord looped over a branch, a wet finger of the other hand in his own anus, penis untouched, " + POUCH + ", the elf queen watches far away between the trees"),
   "inochi_e3":  ("manor", "he hangs with arms raised, " + VINE + ", the elf queen stands close holding up a blank parchment without text before his face, a thin smooth vine in his anus, sweet dark violet haze around his head, teasing smile, cum dripping untouched, " + SHARD),
   "onedari_e3": ("manor", "he lies on his back on the white bed with his wrists lifted above his head by soft dark violet vines, the elf queen sits beside him stroking his chest with her bare foot, a thin smooth vine deep in his anus, dark violet haze, cum on his stomach, " + SHARD),
   # サキュバスクイーン（★集団の王女遊び）
   "btl_boss":   ("top", "he stands before the throne, " + RINGS + ", the succubus princess behind him stroking his nipple with one hand, two fingers of her other hand in his anus, fingering, her heart-tipped tail caressing his neck, playful grin, cum dripping untouched, " + SHARD),
   "onani_boss": ("corridor", "standing alone hidden behind a stone pillar, his wrists bound loosely together with his own coat sleeve, his fingertips stroking his own nipple, penis untouched, " + POUCH + ", the succubus princess watches far away down the red carpet"),
   "inochi_boss":("queenbed", "under the pink canopy, he lies on his back among heart-shaped cushions, " + RINGS + ", the succubus princess leans over him stroking both his nipples, her heart-tipped tail stroking his inner thigh, holding a glowing pale gold crystal shard out of his reach, cum on his stomach"),
   "onedari_boss":("queenbed", "he lies sunk in heart-shaped cushions, the succubus princess lies beside him rolling his nipple with one hand, two fingers of her other hand in his anus, fingering, her heart-tipped tail stroking his other nipple, laughing, cum on his stomach, " + SHARD),
 },
 "lose_desc": "keeps him in this world forever as her cherished protagonist, twelve pale gold crystal shards glowing as the workshop bell rings.",
 "onanie": {
   "master": ("bedroom", "lying on the bed hugging a pillow with his face buried in it, one hand stroking his own nipple, a wet finger of the other hand in his own anus, penis untouched, " + POUCH),
   "e1": ("alley", "crouching behind wooden crates, a wet finger in his own anus, counting under his breath, penis untouched, " + POUCH),
   "e2": ("beach", "sitting in the warm tide pool hugging a pillow, face buried in it, rubbing his nipples against it, penis untouched, " + POUCH),
   "e3": ("forest", "standing under a tree with one wrist hung loosely in a cord over a branch, a wet finger of the other hand in his own anus, penis untouched, " + POUCH),
   "boss": ("corridor", "standing behind a pillar with his wrists bound loosely by his coat sleeve, fingertips stroking his own nipple, penis untouched, " + POUCH),
 },
 "magic": {
   "1": (None, "workshop", "a leather drawstring pouch lying open on the wooden workbench, two crystal shards inside glowing pale gold, soft warm glow, close-up, no text"),
   "2": (None, "guild", "a blank parchment quest paper without text pinned on a wooden quest board, a wax seal without text, warm lamp light, close-up"),
   "3": ("boss", "top", "spinning a glowing gold ring on her fingertip, more gold rings floating in the air around her, playful teasing grin"),
   "4": ("e3", "manor", "breathing out a sweet heavy dark violet haze from her open palm, the haze drifting low between white pillars, gentle droopy-eyed smile"),
   "5": (None, "workshop", "a brass bell hanging under the workshop eave by the window, gently swinging, faint rings of pale gold light spreading from it, evening sky"),
 },
}
