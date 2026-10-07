# N36 砂漠の後宮（Harem）場面データ。登場人物は全員20歳以上。女性と男の娘の混合・全場面で主人公は踊り子の薄衣（女装）。
HO = "a sheer see-through dancer outfit, a gold-clasped chest piece on his flat chest, a low sheer hip cloth, a belt of tiny gold bells on his waist"
O = {"hero_outfit": HO}
OV = {"hero_outfit": HO + ", a sheer veil draped over his head"}
OA = {"hero_outfit": HO + ", gold bells on his ankles"}
ST = {"hero_outfit": HO, "pen": "strapon"}
CG = {"hero_outfit": HO, "cage": True}
STCG = {"hero_outfit": HO + ", a black sheer shawl over his shoulders", "pen": "strapon", "cage": True}

DATA = {
 "code": "Harem",
 "world": "desert kingdom palace harem at night, white walls and golden domes, sheer silk curtains, golden candlelight, rose and sandalwood incense, detailed background",
 "chars": {
   "m": {"type": "woman",
         "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 33 years old, tall, long legs, both eyes clearly visible, dark skin, black hair, long hair, gold hair ornaments, gold eyes, crimson robe, gold embroidery, sheer veil, queen, large breasts, confident",
         "name": "the dark-skinned black-haired queen in a crimson robe"},
   "e1": {"type": "otoko",
          "tags": "adult male, otoko no ko, trap, very feminine, beautiful feminine face, pretty face, long eyelashes, soft jawline, light makeup, glossy lips, narrow shoulders, slender, elegant adult beauty, adult proportions, long legs, androgynous, delicate features, slim waist, flat chest, no breasts, 22 years old, both eyes clearly visible, dark skin, blonde hair, long hair, green eyes, belly dancer outfit, bells, veil, flat chest, seductive smile",
          "name": "the blonde dark-skinned dancer with bells and a veil"},
   "e2": {"type": "woman",
          "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 26 years old, both eyes clearly visible, red hair, braided hair, amber eyes, many bracelets, orange robe, sewing needle, chatty smile, medium breasts",
          "name": "the red-braided seamstress in an orange robe"},
   "e3": {"type": "otoko",
          "tags": "adult male, otoko no ko, trap, very feminine, beautiful feminine face, pretty face, long eyelashes, soft jawline, light makeup, glossy lips, narrow shoulders, slender, elegant adult beauty, adult proportions, long legs, androgynous, delicate features, slim waist, flat chest, no breasts, 28 years old, both eyes clearly visible, brown hair, long hair, low ponytail, black eyes, white turban, long white robe, censer, polite smile",
          "name": "the brown-haired chamberlain in a white turban"},
   "boss": {"type": "woman",
            "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 40 years old, tall, long legs, both eyes clearly visible, white hair, long hair, red eyes, black and gold robe, gold necklace, key pendant, tall, mature, cold, large breasts, confident",
            "name": "the white-haired dowager queen in black and gold"},
 },
 "places": {
   "shinjo": "harem bedchamber, many layers of sheer silk curtains, floor covered with cushions, golden candlesticks, sweet incense smoke, thick carpet",
   "queen_bed": "queen's bed under a deep crimson silk canopy, gold-embroidered pillows, a round crimson cushion at the foot of the bed",
   "wardrobe": "costume room, colorful rolls of sheer silk, large standing mirror, sewing box, perfume bottles",
   "bath": "white marble bath with shallow waist-deep water, floating rose petals, steam, marble edge",
   "dance": "dance practice hall, polished floor, wall of mirrors, drums in the corner",
   "fountain": "palace courtyard fountain at night, palm trees, moon reflected on the water, cushions by the fountain edge",
   "incense": "cozy incense room, rows of brass incense burners, sandalwood smoke, dim lamp light, cushions",
   "throne": "audience hall, golden pillars, long red carpet, high golden throne",
   "dowager": "dowager's hall, heavy black and gold drapes, cool black marble floor, black cushions",
   "dowager_bed": "black silk bed deep in the dowager's hall, single golden candlestick, heavy dark air",
   "terrace": "palace rooftop terrace, desert starry night sky, golden railing, cushions",
   "jewel": "jewel room, shelves of open jewelry boxes, mirror, gemstones glittering in candlelight",
   "corridor": "long arched palace corridor, hanging brass lamps, marble pillars",
   "tent": "queen's night tent by the fountain, carpets and silk bedding, lamp light through the fabric",
 },
 "atk": {
   "m1": ("shinjo", "he sits among the cushions, the queen sits behind him with her lips at his ear telling a story in a whisper, her hands fastening the gold chest piece on him, the bells on his waist trembling, blush", O),
   "m2": ("wardrobe", "he stands before the tall mirror, the queen behind him ties the belt of gold bells around his waist and drapes sheer silk over his shoulders, her fingers stroking his sides through the silk, his penis under the sheer hip cloth", O),
   "m3": ("queen_bed", "from side, he lies on his back on the crimson bed holding his knees, hip cloth pushed aside, the queen kneels between his legs pegging his anus with her ivory strap-on tied with a crimson sash, anal, the queen licks his nipple beside the pushed-aside chest piece, his own penis separate", ST),
   "e1": ("dance", "they kneel face to face on the polished floor, the dancer holds his cheeks and kisses him through a thin sheer veil, the wet silk clinging to both lips, tongue pressing through the fabric, bells swaying", O),
   "e2": ("wardrobe", "he stands on a round stool with arms raised, the seamstress wraps a measuring tape around his chest and pins sheer silk to his body with needles, a tiny ruby ornament clinging to his nipple", O),
   "e3": ("incense", "he kneels with his hips raised high on a cushion, hip cloth lifted, the chamberlain kneels behind him sliding two oiled fingers into his anus, fingering, the other hand correcting his posture, a censer smoking beside them", O),
   "boss": ("dowager", "he lies back on black cushions, thin gold chains run from his chastity cage to tiny gold rings on his nipples, the dowager stands over him holding the chain and pulling it slowly, cold smile", CG),
 },
 "atk_desc": {
   "m1": "the queen tells a thousand-night story into his ear while dressing him.",
   "m2": "the queen dresses him in a sheer dancer outfit with her own hands.",
   "m3": "the queen takes him on her bed, licking his nipple.",
   "e1": "the dancer kisses him through a sheer veil.",
   "e2": "the seamstress measures and pins sheer silk onto him.",
   "e3": "the chamberlain teaches him harem etiquette with oiled fingers.",
   "boss": "the dowager pulls the golden chain linking his cage and nipples.",
 },
 "lose": {
   "btl_m1": ("shinjo", "he lies sunk into the cushions, the queen lies beside him whispering a story into his ear, one hand stroking his chest through the sheer silk, a gold earring on his right ear, cum on his belly, dazed", O),
   "onani_m1": ("wardrobe", "kneeling alone before the tall mirror, stroking his own thighs and chest through the sheer silk, lips moving as if murmuring a story, bells trembling, penis untouched, the queen reclines on a divan far behind watching", OV),
   "inochi_m1": ("throne", "he kneels on the red carpet before the throne, gold bells on his ankles, the queen stands reading aloud from an unrolled scroll without text, bending to whisper into his ear, a gold signet ring on his finger", OA),
   "onedari_m1": ("terrace", "under the starry desert sky he sits on the queen's lap, leaning back against her, the queen whispers a story into his ear and strokes his chest through the silk, he begs with his mouth open", {"hero_outfit": HO + ", a silver sheer shawl on his shoulders"}),

   "btl_m2": ("queen_bed", "he kneels on the crimson bed, the queen behind him closes the clasp of the gold bell belt on his waist, her hands stroking his chest through the sheer silk, cum on the silk hip cloth, dazed", OV),
   "onani_m2": ("dance", "standing alone in a dance pose before the mirror wall, stroking his own thighs and buttocks through the sheer silk, hips swaying, bells on his waist ringing, penis untouched, the queen sits on a cushion far behind watching", OA),
   "inochi_m2": ("wardrobe", "he stands with his arms through the sleeves of a new violet sheer robe, the queen ties the sash around his waist from behind, her fingers sliding along his sides, an open costume box on the floor", {"hero_outfit": "a violet sheer see-through robe over a gold-clasped chest piece, a belt of tiny gold bells on his waist"}),
   "onedari_m2": ("jewel", "he stands before the mirror, the queen behind him fastens a jewel ornament to his chest piece, her other hand stroking his belly through the silk, open jewelry boxes glittering, he blushes", {"hero_outfit": HO.replace("sheer see-through", "rose-pink sheer see-through")}),

   "btl_m3": ("queen_bed", "from side, he lies on his back on the crimson bed with legs lifted, hip cloth pushed aside, the queen pegs his anus with her ivory strap-on, anal, licking his nipple beside the pushed-aside chest piece, his own penis separate, cum on his belly", ST),
   "onani_m3": ("bath", "sitting alone in the waist-deep marble bath, the wet sheer silk clinging to his skin, rolling his own nipple through the silk, reaching back with an oiled finger at his own anus, penis untouched, the queen stands far away at the bath entrance watching", O),
   "inochi_m3": ("tent", "from side, he lies on his side on the silk bedding, hem lifted, the queen lies behind him pegging his anus with her ivory strap-on, anal, her arm under his head, her lips on his nipple, his own penis separate", {"hero_outfit": "a sheer pale silk night robe, a belt of tiny gold bells on his waist", "pen": "strapon"}),
   "onedari_m3": ("fountain", "he lies back on cushions at the fountain edge holding his knees, a gold anklet, the queen kneels between his legs pegging his anus with her strap-on, anal, licking his nipple, his own penis separate, moonlight", {"hero_outfit": HO + ", a gold anklet", "pen": "strapon"}),

   "btl_e1": ("dance", "he sits on the polished floor leaning back on his hands, the dancer stands over him pressing a belled foot sole on his penis, footjob, the dancer's anklet bells ringing, a veil over his mouth, cum on his belly", O),
   "onani_e1": ("corridor", "hiding alone behind a pillar, a thin veil over his mouth, sucking his own fingers through the cloth, the other wet finger tracing his own nipple, penis untouched, the dancer peeks from far down the corridor", O),
   "inochi_e1": ("terrace", "under the starry sky, the dancer drapes a gold-trimmed veil over his face and kisses him through the sheer cloth, holding his cheeks, his lips pressed to the wet silk, tear tracks on his cheeks", O),
   "onedari_e1": ("incense", "he kneels on a cushion with three layers of sheer veil over his face, the dancer holds his chin and kisses him through the veils, tongue pressing the wet fabric, incense smoke curling", O),

   "btl_e2": ("wardrobe", "he sits on a round stool, tiny rubies clinging to both his nipples through an openwork chest piece, the seamstress flicks one ruby with her fingertip, a measuring tape around her neck, cum on the silk", O),
   "onani_e2": ("shinjo", "sitting alone on the cushions, sliding the sheer silk aside with his fingertips, stroking his own chest and thighs, a tiny gem on his nipple, penis untouched, the seamstress stands far away by the curtain watching", O),
   "inochi_e2": ("throne", "he stands on the red carpet wrapped in three layers of sheer silk, the seamstress behind him pinning another layer on his shoulder, a thick costume ledger without text under her arm, he blushes", {"hero_outfit": "three layers of sheer see-through silk robes over a gold-clasped chest piece, a belt of tiny gold bells on his waist"}),
   "onedari_e2": ("jewel", "he sits before the mirror, the seamstress fastens an emerald on his left nipple and a ruby on his right through a sheer silk chest piece, flicking them with her fingertip, jewelry boxes open", O),

   "btl_e3": ("incense", "from side, he kneels with his hips raised high and his cheek on the cushion, hip cloth lifted, the chamberlain kneels behind him with two fingers deep in his anus pressing his prostate, fingering, a censer smoking, cum dripping", O),
   "onani_e3": ("shinjo", "kneeling alone in a corner with hips raised, reaching back with one oiled finger in his own anus, the other hand gripping a cushion, outfit disheveled, penis untouched, the chamberlain stands far away holding a censer, watching", O),
   "inochi_e3": ("bath", "he lies on his side on a marble couch by the bath, hem lifted, the chamberlain sits behind him sliding one oiled finger into his anus, fingering, a censer smoking beside them, steam, dazed", {"hero_outfit": "a sheer white after-bath robe, a belt of tiny gold bells on his waist"}),
   "onedari_e3": ("corridor", "under hanging lamps he kneels on the corridor floor with hips raised, a white sheer sash tied at his waist, the chamberlain kneels beside him with two fingers deep in his anus, fingering, reciting calmly", {"hero_outfit": HO + ", a white sheer sash tied at his waist"}),

   "btl_boss": ("dowager", "from side, he lies on black cushions with legs lifted, the dowager pegs his anus with her ebony strap-on inlaid with gold, anal, pulling the gold chain that links his chastity cage to rings on his nipples, his own penis separate", STCG),
   "onani_boss": ("terrace", "kneeling alone on the terrace under the stars, a black sheer veil, one hand pinching his own nipple, the other pressing his perineum below his chastity cage, trembling, the dowager watches from far away", {"hero_outfit": HO + ", a black sheer veil", "cage": True}),
   "inochi_boss": ("throne", "he kneels on the red carpet, the dowager stands before him tying a black and gold sash around his waist, holding taut the gold chain from his chastity cage to his nipple rings, key pendant on her necklace", {"hero_outfit": HO + ", a black and gold sash", "cage": True}),
   "onedari_boss": ("dowager_bed", "from side, he lies on his back on the black silk bed holding his knees, the dowager pegs his anus with her ebony strap-on, anal, pulling the gold nipple chain, his own penis separate in a chastity cage, single candle", {"hero_outfit": HO.replace("sheer see-through dancer outfit", "black sheer see-through upper robe"), "pen": "strapon", "cage": True}),
 },
 "lose_desc": "keeps him in the palace harem forever as the queen's consort in sheer silk and gold bells.",
 "onanie": {
   "master": ("dance", "kneeling alone in the sheer dancer outfit, stroking his own thighs and buttocks through the silk, hips swaying so the gold bells ring, one hand on his own chest, penis untouched", O),
   "e1": ("corridor", "a thin veil over his mouth, sucking his own fingers through the cloth, tongue pressing the wet fabric, the other wet finger tracing his own nipple, penis untouched", O),
   "e2": ("wardrobe", "sliding the sheer silk aside one layer at a time, stroking his own chest and thighs, a fingertip flicking a tiny gem on his own nipple, penis untouched", O),
   "e3": ("incense", "kneeling on a cushion with his hips raised high and his cheek down, reaching back with an oiled finger in his own anus, following the etiquette step by step, a censer smoking beside him, penis untouched", O),
   "boss": ("terrace", "kneeling under the stars in a black sheer veil, pinching and lifting his own nipple with one hand, pressing his own perineum with the other, his penis locked in a chastity cage, untouched", {"hero_outfit": HO, "cage": True}),
 },
}
