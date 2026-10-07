# N123 ドミナルク帝城攻略（Dominia1）画像データ。登場人物は全員20歳以上。5人とも人間の成人女性（ふたなり・NH・女装なし）。
# 見た目は設計メモ・brief の文章の目印から作成（作品名・キャラ名は tags に書かない）。髪色は5人で被らせない（黒／オレンジ／ワインレッド／プラチナブロンド／茶）。
# 挿入（pen: strapon）はレイゼンダールの「隊長の叙任」（m3）の本だけ。ほかは指だけなので pen なし。
# メイスは振るわない（床に突く・立てかける・柄で顎を上げるだけ）。猫耳は作り物のカチューシャ（本物の耳ではない）。
# グレイスは大人の女性（25歳）として描く。観客は描かない（責め手1人＋主人公だけ）。書類・許可証・手帳・名簿の文字は描かない。
S = {"pen": "strapon"}
PERMIT = "a blank entry permit card without text with red round stamp marks"
EARS = "a cat ear headband on his head"
SOFT_NEG = "muscular female, abs, broad shoulders on the woman"
MACE_NEG = SOFT_NEG + ", swinging weapon, hitting, wound, scary"
CAT_NEG = SOFT_NEG + ", real animal ears, tail, crowd"
DATA = {
 "code": "Dominia1",
 "world": "grand imperial castle of a matriarchal empire, white marble floors, red carpets, crystal chandeliers, imperial banners without text, tall windows, detailed background",
 "bg": "great hall of an imperial castle, polished white marble floor, long red carpet, crystal chandeliers, imperial banners without text on the walls, a wide staircase to the main tower at the back, no humans",
 "josou": None,
 "chars": {
   "m": {"type": "woman", "jp": "レイゼンダール",
         "tags": "adult woman, mature female, mature face, sharp adult features, 29 years old, adult proportions, beautiful detailed eyes, tall, long legs, black hair, very long straight hair, amber eyes, white and gold military uniform, gold epaulettes, long white boots, steel gauntlets with soft leather palms, soft curvy feminine body, huge breasts, wide hips",
         "name": "the black-haired captain in a white and gold uniform",
         "pose": "one gauntleted hand on her hip, the other hand raised lightly as if giving an order, relaxed confident smile, looking down at viewer",
         "neg": SOFT_NEG},
   "e1": {"type": "woman", "jp": "エステラ",
          "tags": "adult woman, mature female, mature face, sharp adult features, 28 years old, adult proportions, beautiful detailed eyes, long legs, wine red hair, shoulder-length hair, grey eyes, black official cap, black official uniform jacket, black tight skirt, black pantyhose, black high heels, large ornate mace, slender curvy feminine body, beautiful legs, large breasts",
          "name": "the wine-red-haired administrator in a black tight skirt",
          "pose": "standing with the handle of her large mace planted on the floor, the other hand on her hip, legs crossed at the ankle, cold haughty smirk, looking down at viewer",
          "neg": MACE_NEG},
   "e2": {"type": "woman", "jp": "テレザリア",
          "tags": "adult woman, mature female, mature face, 27 years old, adult proportions, beautiful detailed eyes, tall, long legs, platinum blonde hair, hair bun, violet eyes, black long maid dress, white starched apron, white maid headdress, soft voluptuous feminine body, huge breasts",
          "name": "the platinum-blonde head maid in a white apron",
          "pose": "holding a silver tray with a teacup in one hand, a blank notebook without text in the other, polite sarcastic smile, looking at viewer",
          "neg": SOFT_NEG},
   "e3": {"type": "woman", "jp": "イザベラ",
          "tags": "adult woman, mature female, mature face, 26 years old, adult proportions, beautiful detailed eyes, long legs, brown hair, low ponytail, hazel eyes, dark green inspector uniform, peaked cap, white gloves, leather pouch of stamps at her belt, slender feminine body, medium breasts",
          "name": "the brown-ponytail inspector in a peaked cap",
          "pose": "holding a red stamp in one white-gloved hand, the other hand held out palm up as if asking for papers, stern unsmiling face, looking at viewer",
          "neg": SOFT_NEG},
   "boss": {"type": "woman", "jp": "グレイス",
            "tags": "adult woman, mature female, mature face, 25 years old, adult proportions, beautiful detailed eyes, long legs, orange hair, bob cut, green eyes, cat ear headband, festival happi coat over a white blouse, armband without text on her right arm, black shorts, slender curvy feminine body, large breasts",
            "name": "the orange-bob chairwoman in a festival happi coat",
            "pose": "showing the armband on her right arm with one hand, the other hand holding a spare cat ear headband, bright businesslike smile, looking at viewer",
            "neg": CAT_NEG},
 },
 "places": {
   "gate":      "huge iron gate of the imperial castle, stone pillars, imperial banners without text, evening sky",
   "exam":      "entry inspection room, a low wooden inspection platform with a rail, a desk with stamps and stacks of blank papers, quiet lamp light",
   "hall":      "great hall of the castle, white marble floor, red carpet, crystal chandelier, portraits on the walls",
   "maidroom":  "maids' station, tea cart, silver trays, porcelain teapot, starched white linens on shelves",
   "bedroom":   "waiting bedroom, a neatly made bed with white sheets, a wall clock without numbers, bedside table with a bottle of oil",
   "office":    "administration office, a large dark wooden desk, stacks of blank documents, a mace rack on the wall",
   "interro":   "interrogation room, a single wooden chair under a lamp, a clerk's desk, bare stone walls",
   "festival":  "festival stage inside the tower, spotlights, falling confetti, hanging banners without text, red curtains",
   "backstage": "backstage dressing area, costume racks, a large dressing mirror with bulbs, a box of cat ear headbands, costume trunks",
   "command":   "garrison command room, a map table, displayed weapons and armor, medals in a glass case",
   "armory":    "armory, racks of polished armor and gauntlets, weapon stands, wooden display stands, smell of oil, warm lantern light",
   "stairs":    "spiral stone staircase of the main tower, a stone landing, a narrow window showing the city below",
   "balcony":   "castle balcony at night, stone railing, night view of the imperial city, banners in the night wind",
   "private":   "captain's private chamber on the top floor, weapons and armor displayed on the walls, a large bed with white and gold sheets, red carpet",
   "quarters":  "a male subject's room in the castle, an imperial banner without text on the wall, a simple clean bed, a window",
   "belfry":    "bell tower at the top of the main tower, a large bronze bell, stone arches, sky",
 },
 "atk": {
   "m1": ("hall", "he kneels on the marble floor with his back straight and shirt open, the captain stands over him pointing one finger down at him, giving an order, relaxed smile, his hands unbuttoning his own shirt, " + PERMIT + " in his chest pocket, knees trembling"),
   "m2": ("armory", "he stands leaning back against an armor rack, the captain close in front of him, her cold steel gauntlet resting on his neck, her other hand in a thin leather glove pinching and rolling his nipple, appraising smile, his back arched, polished armor around them"),
   "m3": ("private", "from side, he lies on his back on the large bed with legs lifted, the captain between his legs holding his thighs, pegging his anus with her white leather strap-on, anal, kissing him deeply, tongues, saliva trail, his own penis separate", S),
   "e1": ("interro", "he sits on the single wooden chair, the administrator stands over him lifting his chin with the handle of her mace, one high-heeled foot raised, the toe of her shoe stroking his chest through his shirt, looking down coldly, lamp light"),
   "e2": ("bedroom", "he lies on his back on the neat bed, the head maid sits beside him, one hand stroking his nipple, two oiled fingers of her other hand in his anus, fingering, sarcastic sweet smile, a blank notebook without text on the bedside table, he trembles on the edge"),
   "e3": ("exam", "he stands shirtless on the low inspection platform with his arms out to the sides, the inspector stands in front examining his chest, white-gloved fingers pinching his nipple, stern face, his folded clothes on the desk, " + PERMIT + " on the desk"),
   "boss": ("festival", "on the stage under spotlights and falling confetti, he kneels with " + EARS + ", the chairwoman kneels behind him hugging him, both her hands playing with his nipples, her breasts pressed against his back, cheerful smile"),
 },
 "atk_desc": {
   "m1": "the captain's light commands make his body obey before he can think.",
   "m2": "the captain inspects him like a piece of her collection with gauntlet and leather glove.",
   "m3": "the captain knights him on her bed with a deep kiss while taking him from the front.",
   "e1": "the administrator interrogates him from above with her mace handle and her beautiful legs.",
   "e2": "the head maid manages his release, pressing inside and never giving permission.",
   "e3": "the inspector examines every part of his body on the inspection platform.",
   "boss": "the chairwoman turns him into a festival show wearing cat ears on stage.",
 },
 "lose": {
   # レイゼンダール 技1（隊長命令＋★武具の検分）
   "btl_m1":     ("private", "he kneels on the red carpet with his back straight and hands behind his back, the captain crouches behind him, one leather-gloved hand pinching his nipple, two oiled fingers of her other hand in his anus, fingering, a gold garrison badge on a ribbon around his neck, cum dripping untouched"),
   "onani_m1":   ("stairs", "kneeling alone on the stone landing with his back straight as if obeying an order, one hand pinching his own nipple, the other hand reaching behind with a finger in his own anus, penis untouched, the captain watches far above from the top of the stairs"),
   "inochi_m1":  ("balcony", "he stands with both hands on the stone railing, the captain behind him, her steel gauntlet stroking his chest, oiled fingers of her other hand in his anus, fingering, night view of the city, " + PERMIT + " on the railing, legs trembling, cum dripping"),
   "onedari_m1": ("private", "he lies still on his back on the large bed with arms at his sides, the captain sits beside him, leather-gloved fingers pinching his nipple, two oiled fingers of her other hand pressing in his anus, fingering, calm amused smile, cum on his stomach"),
   # レイゼンダール 技2（★武具の検分）
   "btl_m2":     ("armory", "he leans back against an armor rack with legs apart, the captain kneels on one knee before him, leather-gloved hand rolling his nipple, two oiled fingers of her other hand in his anus, fingering, her breath near his untouched penis, polished armor around, cum dripping"),
   "onani_m2":   ("armory", "sitting alone on the floor between armor racks, wearing a pair of thin leather gloves, one gloved hand stroking his own chest and nipple, a gloved finger of the other hand in his own anus, penis untouched, the captain watches far away from the doorway"),
   "inochi_m2":  ("command", "he bends over the map table holding a polishing cloth, the captain behind him stroking his side with a polished steel gauntlet, oiled fingers of her other hand in his anus, fingering, gauntlets and medals on the table, cum dripping"),
   "onedari_m2": ("armory", "he lies on his back on a wooden display stand, the captain leans over him, leather-gloved fingers pinching his nipple, three oiled fingers of her other hand in his anus, fingering, a brass key on a chain at her belt, teasing smile, cum on his stomach"),
   # レイゼンダール 技3（隊長の叙任）
   "btl_m3":     ("private", "from side, he lies on his back on the large bed with legs lifted, the captain between his legs, pegging his anus with her white leather strap-on, anal, kissing him deeply, tongues, saliva trail, her leather-gloved hand pinching his nipple, his own penis separate, cum on his stomach", S),
   "onani_m3":   ("balcony", "leaning alone against the stone railing in the night wind, sucking two of his own fingers, the other hand reaching behind with a finger deep in his own anus, penis untouched, the captain watches far away from the balcony doorway"),
   "inochi_m3":  ("private", "from side, he kneels on all fours on the large bed, the captain kneels behind him pegging his anus with her white leather strap-on, anal, the flat of a ceremonial sword resting gently on his shoulder, his own penis separate, cum dripping", S),
   "onedari_m3": ("private", "from side, he sits on the captain's lap facing her on the bed, her white leather strap-on in his anus, anal, kissing him deeply, tongues, her arms around his waist, his arms around her neck, his own penis separate, cum dripping", S),
   # エステラ（★権力の尋問）
   "btl_e1":     ("interro", "he sits on the single wooden chair, the administrator sits on the desk edge in front of him, lifting his chin with the handle of her mace, her stockinged thighs and calves clamped around his hips squeezing his penis between her legs, looking down coldly, cum on her pantyhose"),
   "onani_e1":   ("office", "sitting alone on a chair with one knee drawn up, pressing the toe of his own shoe against his lower belly, hips shifting, penis untouched, the administrator watches far away from behind the large desk"),
   "inochi_e1":  ("office", "he sits at the large desk stamping blank papers without text, the administrator sits across from him, her stockinged feet under the desk rubbing his penis, footjob, stacks of blank documents, his hand trembling on the stamp, cum on her feet"),
   "onedari_e1": ("interro", "he sits on the chair with hands on his knees, the administrator sits facing him on the desk with her legs extended, her stockinged toes pinching his nipple, the sole of her other foot pressing his lower belly, high heels on the floor, mace leaning on the wall, cum dripping untouched"),
   # テレザリア（★射精管理）
   "btl_e2":     ("bedroom", "he lies on his back on the neat bed, the head maid sits beside him with her dress open at the chest, one hand stroking his nipple, two oiled fingers of her other hand in his anus, fingering, a blank notebook without text on the bedside table, he trembles on the edge, precum"),
   "onani_e2":   ("maidroom", "crouching alone behind a tea cart, an oiled finger in his own anus, his other hand clenched on his own thigh holding back, penis untouched, the head maid watches far away from the doorway holding a silver tray"),
   "inochi_e2":  ("maidroom", "he sits sideways on the head maid's lap on a chair, the head maid holds a teacup to his lips, her other hand stroking his chest and nipple, his back against her huge breasts, silver tray and teapot beside them, precum dripping"),
   "onedari_e2": ("bedroom", "he lies on the bed with knees raised, the head maid kneels between his legs, her thumb and finger ringed tightly around the base of his penis, two fingers of her other hand in his anus, fingering, sweet sarcastic smile, he trembles on the edge"),
   # イザベラ（★入国審査）
   "btl_e3":     ("exam", "he stands on the low inspection platform with his hands on the rail, the inspector behind him, white-gloved fingers pinching his nipple, two oiled gloved fingers of her other hand in his anus, fingering, his folded clothes on the desk, " + PERMIT + ", cum dripping untouched"),
   "onani_e3":   ("gate", "standing alone in the shadow of a gate pillar, shirt off and folded at his feet, running his fingertips over his own neck and nipple as if inspecting himself, penis untouched, the inspector watches far away at the gate"),
   "inochi_e3":  ("exam", "he stands on the inspection platform with his arms raised to the sides, the inspector in front of him examining his chest, white-gloved fingers pinching both his nipples, stern face, a red stamp in the pouch at her belt, his knees trembling, precum"),
   "onedari_e3": ("exam", "he bends over the inspection desk, the inspector stands beside him holding an open blank book without text in one hand, reading aloud, two white-gloved fingers of her other hand in his anus, fingering, cum dripping"),
   # グレイス（★エロック・フェス）
   "btl_boss":   ("festival", "on the stage under spotlights and falling confetti, he kneels with " + EARS + ", the chairwoman kneels behind him, one hand pinching his nipple, two oiled fingers of her other hand in his anus, fingering, her breasts pressed on his back, cum dripping untouched"),
   "onani_boss": ("backstage", "kneeling alone before the dressing mirror with " + EARS + ", one hand pinching his own nipple, the other hand reaching behind with a finger in his own anus, penis untouched, the chairwoman watches far away from behind a costume rack"),
   "inochi_boss":("festival", "on the stage in falling confetti, he stands with " + EARS + " and his hands behind his head, the chairwoman stands behind him with her arms around him, twisting both his nipples, the armband on her right arm shown, hanging banners without text, cum dripping untouched"),
   "onedari_boss":("backstage", "he lies back on a costume trunk with " + EARS + ", the chairwoman leans over him pinching his nipple, two oiled fingers of her other hand in his anus, fingering, a blank armband without text tied on his arm, pleased businesslike smile, cum on his stomach"),
 },
 "lose_desc": "registers him as a male subject of the empire, kept and cared for in the castle forever, his entry permit filled with twelve red stamps.",
 "onanie": {
   "master": ("armory", "sitting on the floor wearing thin leather gloves, one gloved hand pinching his own nipple, a gloved finger of the other hand in his own anus, penis untouched"),
   "e1": ("office", "sitting on a chair with one knee drawn up, pressing the toe of his own shoe against his lower belly, penis untouched"),
   "e2": ("maidroom", "crouching behind a tea cart, an oiled finger in his own anus, the other hand clenched on his thigh holding back, penis untouched"),
   "e3": ("gate", "standing by a gate pillar with his shirt folded at his feet, tracing his own neck and nipple with his fingertips as if inspecting himself, penis untouched"),
   "boss": ("backstage", "kneeling before a dressing mirror with a cat ear headband on his head, pinching his own nipple, a finger of the other hand in his own anus, penis untouched"),
 },
 "magic": {
   "1": (None, "exam", "a red stamp with a wooden handle and a warm red ink pad on a desk, two fresh round red stamp marks on a blank card without text, soft glow, close-up"),
   "2": (None, "belfry", "a large bronze bell ringing in the tower, faint sound ripples in the air, the imperial city far below"),
   "3": ("e1", "hall", "planting the handle of her large mace on the marble floor with a dull ring, a ripple spreading across the floor, looking down coldly, the mace held upright and not swung"),
   "4": ("e2", "maidroom", "holding out a steaming teacup on a silver tray, sweet pink steam rising, polite sarcastic smile"),
   "5": (None, "hall", "a blank entry permit card without text with rows of empty boxes and a few red round stamp marks, lying on a red carpet, soft red glow, close-up"),
 },
}
