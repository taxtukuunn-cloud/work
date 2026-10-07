PAIR = "1girl, 1boy, cfnm, femdom, hetero"
PRON = "her"
PRON_SUBJ = "she"
SOLO = "1girl"
PLACE = "deep slime cave, glossy glowing slime on walls and floor, slime stalactites, dripping water, faint green light"
def _adult(age):
    return f"mature female, adult woman, {age} years old, mature face, adult proportions, long legs"
ADULT = _adult(25)
CHARS = {
 "master": dict(phrase="the teal-haired woman wearing a deep green slime dress", outfit="deep green slime dress",
                tags=_adult(27) + ", slime woman, semi-transparent glossy skin, teal gradient hair, very long hair, yellow-green eyes, deep green slime dress, small gold crown, large breasts, gentle sweet smile, half-closed eyes, wet glossy look"),
 "e1": dict(phrase="the blue-haired woman wearing a light blue slime dress", outfit="light blue slime dress",
            tags=_adult(24) + ", slime woman, blue translucent slime body, blue translucent hair, medium hair, blue eyes, thin light blue slime one-piece dress, medium breasts, cheerful friendly smile, glossy"),
 "e2": dict(phrase="the red-haired woman wearing a crimson slime china dress", outfit="crimson slime china dress",
            tags=_adult(25) + ", slime woman, red translucent slime body, red translucent hair, long hair, red eyes, crimson slime china dress, side slit, medium breasts, confident passionate grin, steam rising from skin, glossy"),
 "e3": dict(phrase="the pink-haired woman wearing a pink slime apron dress", outfit="pink slime apron dress",
            tags=_adult(23) + ", slime woman, pink translucent thick slime body, pink translucent hair, wavy hair, pink eyes, pink slime apron dress, medium breasts, clingy sweet smile, glossy"),
 "boss": dict(phrase="the long purple-haired woman wearing a long purple slime robe", outfit="long purple slime robe",
              tags=_adult(35) + ", ancient slime woman, deep purple translucent slime body, very long flowing purple hair, gold eyes, long purple slime robe, rippling texture, large breasts, tall, calm majestic smile, glossy"),
}
