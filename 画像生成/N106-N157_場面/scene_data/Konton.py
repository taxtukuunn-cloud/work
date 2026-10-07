# N117 混沌種の劇場（Konton）画像データ。登場人物は全員20歳以上。5人とも女性（ふたなり・NH なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。筋肉の線は描かない。
# 原作は青／水色：5人とも青い肌 → pale lilac skin に置き換え。カーテンコールの髪は白〜水色 → white hair fading to pale mint。
#   テオマッハの翼は水色・尻尾は青 → pale lilac-white wings／violet tail。瞳は 赤・琥珀・黄・金・ピンクで青系なし。
# 髪色の書き分け：カーテンコール＝白〜淡いミント／エピアクロス＝黒／テオマッハ＝淡い灰（ash-grey）／タワン＝ワインレッド／候補生A＝ピンク。
# 挿入はカーテンコールの尻尾の先（m3 の本）だけ。体なので pen なし。ほかは指・髪の手の指まで。候補生Aは後ろに触れない。
# 氷の剣は斬らない（刃の腹を当てるだけ）。観客は描かない（暗い客席）。台本・名札・書類に文字は描かない。
# カーテンコールの本（m1〜m3 の敗北CG。オナニー敗北を除く）は主人公が「サキュバス役」の衣装（hero_outfit。体は変えない）。
OUT = {"hero_outfit": "a short starry-sky-patterned cape open at the front over his bare chest, a short matching waist wrap, black thighhighs and a headband with fake horns"}
SOFT_NEG = "muscular female, abs, broad shoulders on the woman, scary"
SWORD_NEG = "cut, sword wound, stabbing, blood on the blade"
BOOK = "a thin blank script booklet without text"
LIGHT = "a bright white spotlight beam on him"
DATA = {
 "code": "Konton",
 "world": "grand theater of a chaos tribe on a paradise island at night, red velvet curtains, spotlights, dark empty-looking audience seats, starry-sky-patterned ceiling, detailed background",
 "bg": "stage of a grand old theater seen from the center aisle, heavy red velvet curtain half open, a single white spotlight circle on the wooden stage floor, rows of dark red seats, starry-sky-patterned domed ceiling, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "カーテンコール",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, colored skin, pale lilac skin, white hair fading to pale mint at the tips, very long hair, red eyes, dark violet starry-sky-patterned witch hat, dark violet starry-sky-patterned jacket and trousers, white shirt, red necktie, staff with a round spiral tip, long segmented tail with a smooth rounded tip, soft voluptuous feminine body, huge breasts, wide hips",
         "name": "the witch-hatted producer in a starry suit",
         "pose": "holding a staff with a spiral tip in one hand, the other hand extended as if inviting someone onto a stage, elegant confident smile, looking down at viewer with red eyes",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "テオマッハ",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, colored skin, pale lilac skin, pale ash-grey hair, medium wavy hair, yellow eyes, black witch hat, black witch dress, pale lilac-white bat-like wings, slim violet tail, a large crystal cauldron beside her, soft curvy feminine body, large breasts",
          "name": "the grey-haired witch with a crystal cauldron",
          "pose": "leaning one elbow on a large bubbling crystal cauldron, one finger at her lips, teasing mocking grin, looking at viewer",
          "neg": SOFT_NEG + ", boiling a person, person inside the cauldron"},
   "e2": {"type": "woman", "jp": "タワンホートナチャ",
          "tags": "adult woman, mature female, mature face, 28 years old, adult proportions, beautiful detailed eyes, tall, colored skin, pale lilac skin, six arms, wine-red hair, long hair, golden eyes, white draped dress, sitting on a large soft white jellyfish-like creature with round red eyes and soft white tentacles, soft voluptuous feminine body, huge breasts, wide hips",
          "name": "the six-armed lady on a white jellyfish creature",
          "pose": "all six arms opened wide as if offering a hug, gentle motherly smile, looking at viewer",
          "neg": SOFT_NEG + ", insect legs, hairy spider, scary creature, fangs",
          "neg_remove": ["extra arms"]},
   "e3": {"type": "woman", "jp": "アイドル候補生A",
          "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, colored skin, pale lilac skin, pink hair, very long hair, black curled horns, pink eyes, bat wings, black idol stage dress, black thighhighs, sword with a clear ice blade, slender curvy feminine body, medium breasts",
          "name": "the pink-haired idol with an ice sword",
          "pose": "one hand on her hip, resting a clear ice sword on her shoulder, proud smug smile, looking at viewer",
          "neg": SOFT_NEG + ", " + SWORD_NEG},
   "boss": {"type": "woman", "jp": "エピアクロス",
            "tags": "adult woman, mature female, mature face, sharp adult features, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, colored skin, pale lilac skin, black hair, floor-length hair, hair ends spreading into many slender black hands, amber eyes, expressionless, black business suit, black pencil skirt, red necktie, soft curvy feminine body, large breasts",
            "name": "the black-suited executive with floor-length black hair",
            "pose": "standing straight holding a blank clipboard without text, her floor-length hair spreading on the floor into many slender black hands, blank calm expression, looking at viewer",
            "neg": SOFT_NEG + ", horror, strangling, hair covering her face"},
 },
 "places": {
   "front":    "front of the theater at night, a starry-sky-patterned signboard without text, pale lantern light, large double doors",
   "counter":  "reception counter covered in red velvet, blank tickets without text, a small brass bell",
   "lobby":    "theater lobby, crystal chandelier, framed paintings, thick red carpet",
   "seats":    "audience seating, rows of red velvet seats in the dark, only the stage is bright far ahead",
   "stage":    "center of the wooden stage, hot spotlight circle, red velvet curtain behind, dark audience seats beyond the footlights",
   "pit":      "trap room under the stage, dark wooden beams, stage lift machinery, a thin beam of stage light from above, dust in the air",
   "wing":     "stage wing behind the side curtain, props and ropes, a thin strip of stage light on the floor, a practice mirror",
   "dressing": "dressing room, a large mirror framed with warm light bulbs, makeup table, face powder, costumes on a rack",
   "costume":  "costume room, racks of starry-sky-patterned costumes, fake horns and black thighhighs on shelves, a tall mirror, a water jug",
   "cauldron": "cauldron chamber, a huge crystal cauldron bubbling, sweet pale violet steam filling the room, warm stone floor",
   "beach":    "beach behind the theater at night, glowing pale violet waves, soft seaweed like ribbons, smooth rocks",
   "nest":     "nest of white jellyfish creatures, soft white jelly-like floor, dim pearly light, damp sea air",
   "office":   "plain meeting room, a long desk with stacks of blank papers without text, office chairs, a wall clock without numbers",
   "gallery":  "long corridor with a ceiling full of stars, polished floor reflecting the stars, endless perspective",
   "producer": "producer's office, piles of blank script booklets without text, a velvet chaise longue, a large window overlooking the lit stage, ink bottle and quill",
 },
 "atk": {
   "m1": ("stage", "he stands in the spotlight with his back arched, the producer stands close behind him holding an open " + BOOK + " before his face, her lips at his ear whispering lines, her other hand on his chin, his lips parted as if reciting, knees trembling"),
   "m2": ("stage", "he stands in the center of the spotlight with his shirt open, the producer beside him tracing his nipple with the round spiral tip of her staff, her segmented tail stroking his inner thigh, two fingers of her other hand in his anus, fingering, his penis untouched, " + LIGHT),
   "m3": ("wing", "from side, behind the falling red curtain, he leans back in her arms, the producer kisses him deeply, tongues, saliva trail, the smooth rounded tip of her segmented tail in his anus, her hand holding the curtain rope, his own penis separate"),
   "e1": ("cauldron", "he has sunk to his knees limp in sweet pale violet steam, the witch crouches beside him laughing, the tip of her violet tail flicking his nipple, two wet fingers of her hand in his anus, fingering, the crystal cauldron bubbling behind them"),
   "e2": ("nest", "he is held against her chest from behind, the six-armed lady embraces him with all six arms, two hands pinching his nipples, two hands stroking his inner thighs, two hands at his rear with fingers in his anus, fingering, gentle smile"),
   "e3": ("wing", "he stands with his shirt open against a prop crate, the idol presses the flat side of her clear ice sword against his chest without cutting, her other hand pinching his chilled nipple with warm fingers, smug smile, he shivers"),
   "boss": ("office", "he stands lifted slightly by her hair, the executive stands still in front of him with a blank face, many slender black hair hands stroking his ears, neck, nipples, sides and inner thighs at once, one hair hand with fingers in his anus, fingering"),
 },
 "atk_desc": {
   "m1": "the producer reads the script into his ear and makes him speak the lines.",
   "m2": "the producer puts him under the spotlight, traces his nipple with her staff and presses inside with her fingers.",
   "m3": "the producer kisses him deeply as the curtain falls, the tip of her tail inside him.",
   "e1": "the witch weakens him with sweet cauldron steam and teases his nipple and rear.",
   "e2": "the six-armed lady embraces him and caresses six places at once.",
   "e3": "the idol chills his skin with the flat of her ice sword and warms his nipple with her fingers.",
   "boss": "the executive strokes his whole body with dozens of black hair hands.",
 },
 "lose": {
   # カーテンコール 技1（大黒幕＋★トップライト）
   "btl_m1":     ("stage", "he stands posing in the spotlight with one hand on his hip, the producer behind him holding a finished " + BOOK + " open before him, the round tip of her staff tracing his nipple, two fingers of her other hand in his anus, fingering, cum dripping untouched", OUT),
   "onani_m1":   ("dressing", "sitting alone before the bulb-framed mirror, holding " + BOOK + " in one hand and whispering, the other hand rubbing his own nipple then reaching behind to stroke his own anus, penis untouched, the producer watches far away reflected in the mirror"),
   "inochi_m1":  ("front", "he stands before the large double doors in a circle of pale light like a spotlight, the producer behind him pinching his nipple, two fingers of her other hand in his anus, fingering, " + BOOK + " in his hand, legs trembling, cum dripping", OUT),
   "onedari_m1": ("producer", "he sits on the velvet chaise longue reading from " + BOOK + ", the producer sits beside him writing in the air with a quill, her other hand rolling his nipple, her segmented tail around his thigh, stage light from the window, cum dripping", OUT),
   # カーテンコール 技2（★トップライト）
   "btl_m2":     ("stage", "he sits on the stage floor in the spotlight with his legs spread toward the dark seats, the producer kneels behind him rolling his nipple, two oiled fingers of her other hand deep in his anus, fingering, her tail stroking his inner thigh, cum on his stomach", OUT),
   "onani_m2":   ("dressing", "sitting alone on a stool before the bulb-framed mirror with his legs open, an oiled finger in his own anus, warm bulb light on his skin, penis untouched, the producer watches far away from the half-open door"),
   "inochi_m2":  ("stage", "he stands in the spotlight looking down at one empty red seat in the dark audience, the producer behind him with her staff tip on his nipple, her fingers in his anus, fingering, his knees bent, cum dripping", OUT),
   "onedari_m2": ("stage", "he stands on a taped cross mark on the stage floor under a red spotlight, the producer in front tracing his nipple with her staff tip, two fingers of her other hand in his anus, fingering, pleased smile, cum dripping", OUT),
   # カーテンコール 技3（ヒューマニズムフィナーレ）
   "btl_m3":     ("stage", "from side, behind the lowered red curtain, he clings to her shoulders, the producer holds his waist and kisses him deeply, tongues, saliva trail, the smooth rounded tip of her segmented tail deep in his anus, his own penis separate, cum on his stomach", OUT),
   "onani_m3":   ("wing", "kneeling alone in the shadow of the side curtain, sucking two of his own fingers as if kissing, the other hand reaching behind with a finger in his own anus, penis untouched, the producer watches far away from the stage"),
   "inochi_m3":  ("gallery", "from side, under the ceiling of stars, he bows forward with her arm around his waist, the producer lifts his chin and kisses him deeply, the tip of her segmented tail in his anus, starlight gathering on them like a spotlight, his own penis separate", OUT),
   "onedari_m3": ("producer", "from side, he lies on his back on the velvet chaise longue, the producer leans over him kissing him deeply, tongues, the tip of her segmented tail in his anus, stage light from the window, his own penis separate, cum on his stomach", OUT),
   # テオマッハ（★魔女の大釜）
   "btl_e1":     ("cauldron", "he lies limp on the warm stone floor in thick sweet steam, the witch sits beside him laughing, the tip of her violet tail circling his nipple, two wet fingers of her hand deep in his anus, fingering, a crystal shard on a cord around his neck, cum dripping untouched"),
   "onani_e1":   ("dressing", "sitting alone at the makeup table, holding a steaming teacup near his face and breathing the steam, the other hand pinching his own nipple, penis untouched, the witch watches far away from the doorway"),
   "inochi_e1":  ("cauldron", "he kneels inside a faintly shimmering transparent box of barrier walls filled with sweet steam, his palms on the invisible wall, the witch outside reaches her violet tail through to flick his nipple, mocking grin, he trembles on the edge"),
   "onedari_e1": ("cauldron", "he kneels on a wooden step stool before the huge crystal cauldron breathing its steam, the witch behind him, her tail tip flicking his nipple, her fingers in his anus, fingering, holding up three fingers, cum dripping"),
   # タワンホートナチャ（★六本の腕の抱擁）
   "btl_e2":     ("nest", "he lies back against her on the soft white floor, the six-armed lady holds him with all six arms, two hands rolling his nipples, two on his inner thighs, two fingers in his anus, fingering, a white jellyfish plush doll beside them, cum on his stomach"),
   "onani_e2":   ("beach", "sitting alone on a smooth rock by the glowing waves, hugging himself with one arm and pinching his own nipple, the other hand reaching behind to his own anus, penis untouched, the six-armed lady watches far away from the surf"),
   "inochi_e2":  ("beach", "he sleeps half awake lying on a smooth rock bed by the waves, the six-armed lady lies behind him holding him with all six arms, one hand on his nipple, one finger in his anus, fingering, gentle smile, cum dripping"),
   "onedari_e2": ("nest", "in the middle of the white nest, he is hugged tightly face to face, the six-armed lady wraps all six arms around him, hands on his back, nipples, thighs and rear at once, soft white tentacles around his ankles, cum dripping"),
   # アイドル候補生A（★妖美促進）
   "btl_e3":     ("wing", "he sits against a prop crate with his shirt open in a strip of stage light, the idol kneels over his legs, the flat side of her ice sword resting on his collarbone without cutting, her warm fingers pinching his chilled nipple, a folded practice outfit beside them, cum dripping untouched"),
   "onani_e3":   ("costume", "kneeling alone between the costume racks, dipping his fingers in a water jug and pinching his own nipple with cold wet fingers, shivering, penis untouched, the idol watches far away from the door"),
   "inochi_e3":  ("wing", "he holds a dance pose with one arm raised, the idol hugs him from behind, both her hands pinching his nipples, her chin on his shoulder, smug smile, stage light and curtain beyond, his legs trembling, cum dripping untouched"),
   "onedari_e3": ("wing", "he stands before a practice mirror with his shirt open, the idol behind him touching the flat of her ice sword to one nipple without cutting, her warm fingers pinching the other nipple, counting, cum dripping untouched"),
   # エピアクロス（★くねくねくねくね）
   "btl_boss":   ("office", "he lies on the long desk among blank papers, the executive stands over him with a blank face, dozens of black hair hands stroking his ears, neck, nipples, sides and thighs, hair hand fingers in his anus, fingering, a strand of black hair tied around his wrist, cum on his stomach"),
   "onani_boss": ("pit", "kneeling alone in the dark trap room, long strips of cloth draped over his shoulders, brushing them over his own neck, nipples and inner thighs, penis untouched, a thin beam of light from above, the executive watches far away in the shadows"),
   "inochi_boss":("office", "he sits at the desk gripping a pen over blank papers without text, the executive stands behind his chair, many black hair hands stroking his chest, nipples and thighs under the desk, hair hand fingers in his anus, fingering, a wall clock, cum dripping"),
   "onedari_boss":("office", "he stands with his arms held out by her hair, the executive faces him holding a blank clipboard, ten black hair hands stroking his nipples, sides, inner thighs and rear at once, hair hand fingers in his anus, fingering, cum dripping untouched"),
 },
 "lose_desc": "keeps him in the chaos theater forever as its cherished star performer, applause rising from the dark seats.",
 "onanie": {
   "master": ("dressing", "sitting before the bulb-framed mirror with his legs open, an oiled finger in his own anus, the other hand rubbing his own nipple, penis untouched"),
   "e1": ("dressing", "breathing the steam of a teacup held near his face, the other hand pinching his own nipple, penis untouched"),
   "e2": ("beach", "sitting on a rock hugging himself with one arm and pinching his own nipple, the other hand reaching behind to his own anus, penis untouched"),
   "e3": ("costume", "kneeling, pinching his own nipple with fingers chilled in cold water, shivering, penis untouched"),
   "boss": ("pit", "kneeling with long strips of cloth draped over his shoulders, brushing them over his own neck, nipples and inner thighs, penis untouched"),
 },
 "magic": {
   "1": (None, "producer", "a white quill pen with pale violet ink resting on an open blank script booklet without text, two faint glowing lines of light on the page, close-up"),
   "2": (None, "counter", "a polished brass hand bell ringing on the velvet counter, faint sound ripples in the air, close-up"),
   "3": ("m", "stage", "pointing her spiral-tipped staff upward, a bright white spotlight beam falling onto an empty spot on the stage, elegant smile"),
   "4": ("e1", "cauldron", "lifting the lid of her huge crystal cauldron, sweet pale violet steam pouring out toward the viewer, teasing grin"),
   "5": (None, "stage", "a heavy red velvet curtain fully lowered across the stage, gold tassels, soft light leaking under the hem, empty dark seats"),
 },
}
