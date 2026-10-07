# N45 夜行寝台列車（Train）場面データ。登場人物は全員20歳以上。女装ありMOD：全場面で主人公は臙脂の乗務員の制服（ウィッグなし）。ミチル・リコ・ツバメは女性（ペニバン）、カイ・ハクは男の娘。
NB = "blue theme, blue light, daylight outside the window"
UNI = "a maroon train attendant uniform with a maroon jacket, white blouse, maroon tight skirt, black pantyhose, thin maroon scarf and maroon garrison cap, no wig"
UNI_OPEN = UNI + ", the blouse unbuttoned showing his flat chest"
UNI_LIFT = UNI + ", the skirt hiked up to his waist and the pantyhose pulled down to his thighs"
UNI_OL = UNI + ", the blouse unbuttoned showing his flat chest, the skirt hiked up to his waist and the pantyhose pulled down to his thighs"
UNI_APRON = UNI + ", a black apron over the skirt"
DATA = {
 "code": "Train",
 "world": "night sleeper train interior, dark wood paneling and brass fittings, orange lights streaming past the windows, night, detailed background",
 "chars": {
   "m": {"type": "woman",
         "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 32 years old, tall, long legs, both eyes clearly visible, black hair, long hair, low bun, red eyes, black conductor uniform, peaked cap, white gloves, ticket punch, polite smile, large breasts",
         "name": "the black-haired conductor in a black uniform and peaked cap", "neg": NB},
   "e1": {"type": "otoko",
          "tags": "adult male, otoko no ko, trap, very feminine, beautiful feminine face, pretty face, long eyelashes, soft jawline, light makeup, glossy lips, narrow shoulders, slender, elegant adult beauty, adult proportions, long legs, androgynous, delicate features, slim waist, flat chest, no breasts, 23 years old, both eyes clearly visible, brown hair, short bob, green eyes, attendant vest, slacks, scarf, friendly smile",
          "name": "the brown-bob attendant in a vest and slacks", "neg": NB + ", skirt on the attendant"},
   "e2": {"type": "woman",
          "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 25 years old, both eyes clearly visible, blonde hair, side ponytail, brown eyes, black vendor uniform, apron, bright smile, large breasts",
          "name": "the blonde side-ponytail vendor in a black uniform and apron", "neg": NB},
   "e3": {"type": "otoko",
          "tags": "adult male, otoko no ko, trap, very feminine, beautiful feminine face, pretty face, long eyelashes, soft jawline, light makeup, glossy lips, narrow shoulders, slender, elegant adult beauty, adult proportions, long legs, androgynous, delicate features, slim waist, flat chest, no breasts, 24 years old, both eyes clearly visible, pink hair, medium hair, purple eyes, white attendant jacket, sleepy smile",
          "name": "the pink-haired berth attendant in a white jacket", "neg": NB + ", skirt on the berth attendant"},
   "boss": {"type": "woman",
            "tags": "adult woman, mature female, beautiful detailed eyes, adult proportions, 39 years old, tall, long legs, both eyes clearly visible, white hair, short hair, gold eyes, black train driver uniform, pocket watch, tall, mature, stoic, large breasts",
            "name": "the white-haired train driver in a black uniform", "neg": NB},
 },
 "places": {
   "single":      "single sleeper compartment, wood-paneled walls, brass handrail and lamp, narrow berth, night window",
   "double":      "two-berth sleeper compartment, upper and lower bunks, ladder, curtain, ceiling close above the upper bunk",
   "nextroom":    "compartment next to the conductor's office, brass call bell, wider berth",
   "shasho":      "conductor's office, wall clock, bell cord, brass gauges, cap hook",
   "corridor":    "narrow train corridor, thin carpet, folding seat by the window",
   "dining":      "dining car, white tablecloths, table lamps, silverware, steam from soup",
   "pantry":      "dining car pantry, stacked plates, narrow counter, brass lamp",
   "lounge":      "lounge car, maroon sofa, large windows, dim lights, glasses on a side table",
   "crew":        "crew locker room, uniforms hanging in lockers, full-length mirror, stool",
   "linen":       "linen room, shelves of folded blankets and pillows, soft piles of cloth",
   "vending":     "snack preparation room, snack cart, candy jars, caramel boxes, paper bags",
   "deck":        "vestibule between cars, bellows connection, door with a window, handrail",
   "washroom":    "tiny washroom, mirror, brass faucet, steam, tiles",
   "observation": "rear observation car, glass wall showing receding rails and orange lights, low sofa",
   "cab":         "locomotive cab, glowing gauges, whistle cord, assistant seat, dark rails ahead, orange signal",
   "nap":         "crew nap room, one narrow bunk, thin blanket, pocket watch on the wall",
   "stop":        "sleeper compartment during a silent night stop, empty platform lamp outside the window",
   "crewnook":    "tiny crew room past the coupling, narrow bench, one lamp",
 },
 "atk": {
   "m1": ("single", "he sits on the berth, the conductor stands behind him, one white-gloved hand pinching his nipple through the blouse, the brass ticket punch in her other hand, blushing, trembling", {"hero_outfit": UNI}),
   "m2": ("crew", "he stands before the full-length mirror, the conductor kneels pulling black pantyhose up his thigh with white-gloved hands, his blouse half buttoned, the garrison cap waiting on the stool, blushing", {"hero_outfit": "a white blouse half buttoned, a maroon tight skirt and black pantyhose being pulled up his thighs, no wig"}),
   "m3": ("nextroom", "from side, he leans with both hands on the berth, bent forward, the conductor stands behind him pegging his anus with her strap-on, anal, she turns his face and kisses him deeply, his own penis separate", {"pen": "strapon", "hero_outfit": UNI_LIFT}),
   "e1": ("linen", "he stands among shelves of blankets, the attendant stands behind him tying the maroon scarf at his neck, the other hand measuring his waist like a tailor, smiling, blushing", {"hero_outfit": UNI}),
   "e2": ("vending", "he sits on the floor beside the snack cart, the vendor kneels holding his face and kisses him deeply, passing melted candy mouth-to-mouth, tongues, sweet saliva trail", {"hero_outfit": UNI_APRON}),
   "e3": ("double", "he lies on his back on the upper bunk, the berth attendant leans over him taping brass egg vibrators to his nipples under the unbuttoned blouse, whispering sleepily into his ear", {"hero_outfit": UNI_OPEN}),
   "boss": ("cab", "he sits in the assistant seat of the cab, a thin tube inserted into the urethra of his penis, a slim vibrator in his anus, brass egg vibrators on his nipples, the driver standing and pulling the whistle cord, sounding", {"pen": "toy", "hero_outfit": UNI_OL}),
 },
 "atk_desc": {
   "m1": "the conductor inspects his nipples like punching a ticket.",
   "m2": "the conductor dresses him in a crew uniform piece by piece.",
   "m3": "the conductor takes him with her strap-on in the swaying compartment.",
   "e1": "the attendant fits him into a crew uniform with praise.",
   "e2": "the vendor feeds him melting candy mouth to mouth.",
   "e3": "the berth attendant tapes vibrators to his nipples and lulls him.",
   "boss": "the driver sets three toys on him and pulls the whistle.",
 },
 "lose": {
   # m1 検札の指
   "btl_m1": ("single", "he sits on the narrow berth, the conductor sits behind him, her white-gloved fingers pinching and rolling his nipples through the blouse, a punched ticket without text in his breast pocket, orange station lights passing, trembling", {"hero_outfit": UNI}),
   "onani_m1": ("crew", "standing alone before the full-length mirror, pinching his own nipples through the white blouse, penis untouched, the conductor stands far away by the lockers holding the ticket punch, watching", {"hero_outfit": UNI}),
   "inochi_m1": ("corridor", "he sits on the folding seat by the window, the conductor stands beside him pinching his nipple with white-gloved fingers through the unbuttoned blouse, holding up a ticket without text, orange lights passing", {"hero_outfit": UNI_OPEN}),
   "onedari_m1": ("shasho", "he stands with his blouse opened pushing his chest out, begging, the conductor pinches both his nipples with white-gloved fingers, the brass call bell on the wall, wall clock", {"hero_outfit": UNI_OPEN}),
   # m2 乗務員の制服
   "btl_m2": ("crew", "he stands before the full-length mirror, the conductor stands behind him buttoning his blouse and brushing his nipple with a white-gloved finger, her other hand stroking his thigh over the skirt, a locker key on her belt, flushed", {"hero_outfit": UNI}),
   "onani_m2": ("double", "kneeling alone on the lower bunk, stroking his own thighs and buttocks over the tight skirt, hips swaying with the train, penis untouched, the conductor stands far away in the doorway watching", {"hero_outfit": UNI}),
   "inochi_m2": ("washroom", "he stands before the mirror, the conductor stands behind him tying the maroon scarf at his neck, her white-gloved hand stroking his chest through the blouse, steam on the mirror", {"hero_outfit": UNI}),
   "onedari_m2": ("observation", "he stands before the rear window, the conductor kneels pulling black pantyhose up his thigh with white-gloved hands, his skirt lifted, receding rails and orange lights behind the glass", {"hero_outfit": "a white blouse, a maroon tight skirt lifted, black pantyhose being pulled up his thighs, a thin maroon scarf, no wig"}),
   # m3 揺れる個室で
   "btl_m3": ("nextroom", "from side, he leans with both hands on the berth, bent forward, the conductor stands behind him pegging his anus with her strap-on, anal, she turns his face and kisses him deeply, the garrison cap on his head, his own penis separate", {"pen": "strapon", "hero_outfit": UNI_LIFT}),
   "onani_m3": ("deck", "leaning alone against the vestibule door, pressing his own buttocks through the skirt, sucking two fingers, hips lowering with the sway, penis untouched, the conductor stands far away at the other door watching", {"hero_outfit": UNI}),
   "inochi_m3": ("dining", "from side, he kneels on a dining chair gripping its back, the conductor stands behind him pegging his anus with her strap-on, anal, kissing his neck, white tablecloth and lamps, his own penis separate", {"pen": "strapon", "hero_outfit": UNI_LIFT}),
   "onedari_m3": ("lounge", "from side, the conductor sits on the maroon sofa with him on her lap facing away, pegging his anus with her strap-on from below, anal, gripping his waist and turning his face to kiss him, his own penis separate", {"pen": "strapon", "hero_outfit": UNI_LIFT}),
   # e1 カイ
   "btl_e1": ("linen", "he stands bent forward gripping a linen shelf, the attendant stands behind him lifting the skirt and pushing a slim maroon vibrator into his anus, anal, smiling, the scarf neatly tied at his neck", {"hero_outfit": UNI_LIFT}),
   "onani_e1": ("washroom", "standing alone before the mirror, stroking down from his own neck to his chest over the blouse and scarf, penis untouched, the attendant stands far away at the washroom door watching", {"hero_outfit": UNI}),
   "inochi_e1": ("corridor", "he grips the handrail by the window, bent forward, the attendant stands behind him lifting the skirt and pushing a slim maroon vibrator into his anus, orange station lights streaming past", {"hero_outfit": UNI_LIFT}),
   "onedari_e1": ("pantry", "from side, he bends over the narrow counter, the attendant stands behind him penetrating his anus with his own penis, anal, the slim maroon vibrator lying on the counter, the navy-haired man's penis separate", {"pen": "penis", "hero_outfit": UNI_LIFT}),
   # e2 リコ
   "btl_e2": ("vending", "he sits on the floor behind the snack cart, the vendor kneels kissing him deeply, passing melted candy mouth-to-mouth, her black-stockinged foot pressing his crotch over the skirt, sweet saliva", {"hero_outfit": UNI_APRON}),
   "onani_e2": ("single", "sitting alone on the berth, sucking a candy-sweet finger deeply as if kissing, the other wet finger tracing his own nipple through the opened blouse, penis untouched, the vendor stands far away in the doorway watching", {"hero_outfit": UNI_OPEN}),
   "inochi_e2": ("corridor", "at the end of the corridor he sits on the folding seat, the vendor bends down holding his chin and passing a caramel mouth-to-mouth, deep kiss, tongues, the snack cart beside them", {"hero_outfit": UNI_APRON}),
   "onedari_e2": ("crew", "he sits on the stool, the vendor stands kissing him mouth-to-mouth with melted chocolate, her black-stockinged foot on his penis under the lifted skirt, footjob, sweet saliva", {"hero_outfit": UNI_LIFT}),
   # e3 ハク
   "btl_e3": ("double", "he lies on his back on the upper bunk with the blouse open, brass egg vibrators taped to both nipples, the berth attendant lies beside him whispering sleepily into his ear, the ceiling close above", {"hero_outfit": UNI_OPEN}),
   "onani_e3": ("linen", "lying alone on a pile of blankets, trembling fingertips pressed to his own nipples through the opened blouse, penis untouched, the berth attendant stands far away holding a pillow, watching", {"hero_outfit": UNI_OPEN}),
   "inochi_e3": ("single", "he lies on the narrow berth under a blanket up to his waist, blouse open, brass egg vibrators on his nipples, the berth attendant sits at the bedside reading a paper without text, orange lights", {"hero_outfit": UNI_OPEN}),
   "onedari_e3": ("stop", "he sits by the window with his blouse open, the berth attendant sits behind him pressing brass egg vibrators to his nipples and whispering into his ear, empty platform outside", {"hero_outfit": UNI_OPEN}),
   # boss ツバメ
   "btl_boss": ("cab", "he sits in the assistant seat with his legs apart, a thin tube inserted into the urethra of his penis, a slim vibrator in his anus, brass egg vibrators on his nipples, the driver pulls the whistle cord, glowing gauges", {"pen": "toy", "hero_outfit": UNI_OL}),
   "onani_boss": ("nap", "sitting alone on the narrow bunk with his legs apart, one hand pressing his own perineum with a finger in his own anus, the other trembling fingertip on his nipple, penis untouched, the driver stands far away in the doorway watching", {"hero_outfit": UNI_OL}),
   "inochi_boss": ("observation", "from side, he kneels on the low sofa gripping its back, the driver stands behind him pegging his anus with her strap-on, anal, brass egg vibrators on his nipples, receding rails and orange lights, his own penis separate", {"pen": "strapon", "hero_outfit": UNI_OL}),
   "onedari_boss": ("crewnook", "from side, he lies on his back on the narrow bench holding his knees, the driver kneels between his legs pegging his anus with her strap-on, anal, a thin tube in the urethra of his penis, egg vibrators on his nipples", {"pen": "strapon", "hero_outfit": UNI_OL}),
 },
 "lose_desc": "keeps him aboard the endless night train as a crew member in a maroon uniform.",
 "onanie": {
   "master": ("single", "sitting alone on the berth wearing only the white blouse, pinching his own nipples through the fabric, rolling them to the rhythm of the rails, penis untouched", {"hero_outfit": "only the white blouse of the maroon attendant uniform, no wig"}),
   "e1": ("washroom", "standing before the mirror, stroking down from his own neck to his chest over the blouse and scarf as if fixing the scarf, penis untouched", {"hero_outfit": UNI}),
   "e2": ("vending", "sitting by the snack cart, sucking a candy-sweet finger as if kissing, the other wet finger tracing his own nipple through the opened blouse, penis untouched", {"hero_outfit": UNI_OPEN}),
   "e3": ("double", "lying on his back on the bunk, trembling fingertips pressed to his own nipples through the opened blouse in rhythm with the rails, penis untouched", {"hero_outfit": UNI_OPEN}),
   "boss": ("nap", "sitting on the bunk with his legs apart, one hand pressing his perineum with a finger in his own anus, the other trembling fingertip on his nipple, penis untouched", {"hero_outfit": UNI_OL}),
 },
}
