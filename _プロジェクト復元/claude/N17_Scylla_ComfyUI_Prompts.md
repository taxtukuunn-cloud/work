# N17 スキュラの海底神殿（Scylla）ComfyUI プロンプト（全53枚）

> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版の日時：2026-09-24 10:31 JST）。本文は元の版そのまま。末尾の「付録」だけ復元時に追加（撮り直し後の build_prompts.py との差分。現行の全文はPCの `Downloads\N17_Scylla_画像生成バッチ\build_prompts.py`）。

作成：2026-09-24。登場人物は全員20歳以上。個人利用のみ。

## 生成のしかた
- バッチ：ユーザーのPCの `Downloads\\N17_Scylla_画像生成バッチ\\`（N15と同じ単独バッチ方式。Anima 3ローダー・832×1216・er_sde・simple・36step・CFG4.5・seed_base 20260924）
- `gen_scylla_all.bat` をダブルクリック → ComfyUIが起動していなければ起動し、53枚を `output\\Scylla\\` にゲームで使う名前のまま保存（`--skip-existing` なので途中からの再開も可）
- 撮り直し：`run_scylla.bat <キー> --random --batch 4` → `run_scylla.bat --pick <キー> <番号>`
- ゲームへ：`install_scylla.bat "<ゲーム>\\Picture"`
- 状態（2026-09-24）：**53枚生成・目視確認済み**。男女の入れ替わりなど14枚は候補4枚ずつ撮り直して選定（`reroll_scylla.bat`）
- オナニー系12枚は責め手の得意技に合わせた自慰（ペニスを握らない）で撮り直した。見物人は短い説明だけにして主人公を主役に固定（女性のタグを全部入れると女性にペニスが付いた）
- 残る気になる点：メルティナ系のオナニー画像4枚で主人公が貝殻の胸当てを着けて見える（真珠の乳首飾りの指定が効きすぎ）
- カードが参照する53ファイルとプロンプトのキーが一致することを確認済み

## 崩れやすそうなもの
atk_m3・lose_btl_m3（3か所同時）／クラーケのふたなり（atk_boss・lose_btl_boss・lose_inochi_boss）／メドゥの尿道の糸（atk_e3・lose_btl_e3）

## build_prompts.py（全文）
```python
# -*- coding: utf-8 -*-
"""N17 スキュラの海底神殿（Scylla）画像プロンプト生成 → scylla_prompts.json（53枚）
登場人物は全員20歳以上の成人。個人利用のみ。
"""
import json, os

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, "
            "child, loli, shota, young, teenage, underage, petite female, flat chest female, muscular, abs, pectorals, bara, hairy, "
            "collar, choker, leash, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the man, 2boys, vaginal, penetration by male, nude female, female nudity, topless female, merged bodies")
NEG_NOFUTA = ", futanari"
NEG_SCENE = ", pussy, vagina, breasts on the man, long hair on the man, human legs on the octopus woman, blue hair on the woman"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis, dildo, sex toy, strap-on"
NEG_ONANI = ", woman touching him, hetero sex"

UW = "underwater, air bubbles, floating hair, light rays through water, green-tinted teal light, caustics"

PROT = ("1boy, faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult male, androgynous, "
        "feminine body, petite, short, slender, narrow shoulders, narrow waist, thin arms, flat chest, smooth pale skin, "
        "no muscles, blush, height difference, nude male, completely naked, penis")

CH = {
    "m": dict(seed="MELTINA",
              tags="1girl, scylla, octopus girl, monster girl, mature female, adult woman, light purple hair, wavy hair, very long hair, "
                   "gold eyes, seashell hair ornament, pearl necklace, seashell bra, sheer lavender shawl, "
                   "eight purple octopus tentacles instead of legs, suction cups, large breasts",
              name="the light-purple-haired octopus woman in a seashell bra with purple tentacles"),
    "e1": dict(seed="SEIRE",
               tags="1girl, mermaid, monster girl, adult woman, blonde hair, very long hair, green eyes, pearl bra, pearl hair ornament, "
                    "golden fish tail instead of legs, fins, gentle smile, medium breasts",
               name="the blonde mermaid in a pearl bra"),
    "e2": dict(seed="ANEMO",
               tags="1girl, sea anemone girl, monster girl, adult woman, pink hair, short hair, thin pink tentacles in her hair, red eyes, "
                    "coral red sleeveless top, frilly pink tentacle skirt, playful smile, medium breasts",
               name="the pink-haired anemone woman in a coral red top and a pink tentacle skirt"),
    "e3": dict(seed="MEDU",
               tags="1girl, jellyfish girl, monster girl, adult woman, mature face, tall, white hair, translucent hair, very long hair, "
                    "pale pink eyes, half-closed eyes, expressionless, translucent jellyfish umbrella dress, "
                    "long thin transparent threads hanging from the hem, small breasts",
               name="the tall white-haired jellyfish woman in a translucent umbrella dress"),
    "boss": dict(seed="KRAKE",
                 tags="1girl, kraken girl, monster girl, mature female, very tall, crimson hair, very long hair, black eyes, gold tiara, "
                      "black scale armor dress, huge dark red tentacles instead of legs, suction cups, regal, smirk, large breasts",
                 name="the tall crimson-haired kraken queen in black scale armor with huge dark red tentacles"),
}

PL = {
    "temple": "sunken temple hall, broken white marble pillars covered in coral and seaweed, coral throne, detailed background",
    "pearl":  "underwater bedchamber, giant open clam shell bed lined with pearls, curtains of pearl strings, soft glow, detailed background",
    "ink":    "dark underwater cave filled with drifting clouds of purple ink, faint glow, detailed background",
    "corr":   "half-flooded stone corridor of a sunken temple, light shaft from a crack in the ceiling, seaweed, detailed background",
    "cove":   "underwater rock dome cave, mermaid cove, glowing seashells on the walls, sunlight from an opening above, detailed background",
    "rocks":  "warm underwater rocky reef, many small pink sea anemones on the rocks, detailed background",
    "jelly":  "open deep water full of countless softly glowing pink and white jellyfish, detailed background",
    "trench": "deep sea trench, black rocks, dark abyss, faint red bioluminescent light, huge black rock throne, detailed background",
    "ship":   "cabin of a sunken wooden sailing ship underwater, captain's chair, old wooden table, rusty lanterns, small fish, detailed background",
    "shaft":  "vertical underwater shaft rising to a bright water surface far above, ruined stone walls, detailed background",
    "sand":   "round hollow in white sand on the sea floor surrounded by glowing jellyfish, detailed background",
    "vow":    "deep sea trench wall with glowing red carved patterns without letters, full moon light shining down through the water, detailed background",
}

CLOTHED = "clothed female, the woman keeps her seashell bra and ornaments on, only the man is naked"
CLOTHED_G = "the woman keeps her clothes on, only the man is naked"

images = []


def add(key, seed, pos, neg, rembg=False):
    images.append({"key": "Scylla_" + key, "seed_char": seed, "rembg": rembg, "positive": pos, "negative": neg})


def scene(key, who, place, action, desc, futa=False, insert=False, onani=False):
    c = CH[who]
    rating = "explicit"
    clothed = CLOTHED if who == "m" else CLOTHED_G
    if onani:
        # 女性のタグを全部入れると女性が主役になり、女性にペニスが付くことがあった → 見物人は短い説明だけにする
        pos = ", ".join([Q, rating, "1boy, solo focus, male focus", PROT,
                         "erection, the naked navy-haired young man is the main subject in the foreground, he pleasures himself, " + action,
                         "a small distant figure in the background watching him: " + c["name"] + ", fully clothed, tiny in frame, not touching him",
                         UW, PL[place], desc])
    else:
        pos = ", ".join([Q, rating, c["tags"] + (", futanari, large penis on the woman" if futa else ""), PROT,
                         "erection", action, clothed, UW, PL[place], desc])
    neg = NEG_BASE + ("" if futa else NEG_NOFUTA) + NEG_SCENE + (NEG_INSERT if (insert or futa) else "") + (NEG_ONANI if onani else "")
    if onani:
        neg += ", hand on penis, holding penis, stroking penis, handjob, penis on the woman, woman masturbating, girl masturbating, girl in foreground, white hair on the man, pink hair on the man, purple hair on the man"
    add(key, c["seed"], pos, neg)


# ---- 立ち絵
STAND = {
    "master": ("m", "floating upright, one hand beckoning, tentacles spread out, sly smile"),
    "e1": ("e1", "floating, hands clasped at her chest, singing, open mouth, lonely smile"),
    "e2": ("e2", "sitting on a rock, waving one hand, tentacle skirt spread around her, cheerful grin"),
    "e3": ("e3", "drifting, arms loosely at her sides, threads trailing below, blank stare"),
    "boss": ("boss", "floating tall, arms crossed, huge tentacles spread wide, looking down at viewer"),
}
for k, (w, pose) in STAND.items():
    c = CH[w]
    add(k, c["seed"], ", ".join([Q, "safe, solo", c["tags"], pose, "looking at viewer, full body, simple background, white background"]),
        NEG_BASE + NEG_NOFUTA, rembg=True)

# ---- 背景
add("bg", "BG", ", ".join([Q, "safe, no humans, scenery", UW,
                           "sunken ancient temple on the sea floor, broken white marble pillars covered in coral and seaweed, "
                           "coral throne at the far end, rays of green-teal light from the surface, schools of small fish, detailed background"]),
    NEG_BASE + NEG_NOFUTA)

# ---- 技CG
scene("atk_m1", "m", "pearl",
      "from front, he floats in front of her, her purple tentacles coil around his arms and waist, two tentacle tips with suction cups sucking on his nipples, erect nipples",
      "the octopus woman caresses his nipples with the suction cups of her tentacles.")
scene("atk_m2", "m", "ink",
      "she blows a cloud of purple ink toward his face, he inhales the ink, dazed, open mouth, drooling, trembling, hands-free, she does not touch him",
      "the octopus woman makes him climax in his head only with the sweet purple ink.")
scene("atk_m3", "m", "temple",
      "from side, he is lifted in the air by her tentacles, legs spread, a thick purple tentacle pushed into his anus, anal, "
      "a very thin purple tentacle inserted into the tip of his penis, urethral insertion, suction cups on both of his nipples",
      "the octopus woman uses three tentacles at once on his nipples, his anus and his urethra.", insert=True)
scene("atk_e1", "e1", "cove",
      "she hugs him from behind, girl behind boy, her lips at his ear, singing, musical notes floating in the water, he is limp and entranced, open mouth",
      "the mermaid sings into his ear and melts his mind.")
scene("atk_e2", "e2", "rocks",
      "from side, he sits on her pink tentacle skirt, thin pink tentacles pushed into his anus from below, anal, her hands pinching his nipples, trembling",
      "the anemone woman seats him on her tentacle skirt and opens his anus.", insert=True)
scene("atk_e3", "e3", "jelly",
      "she wraps him inside her translucent umbrella dress, thin transparent threads coiled around his nipples, "
      "one thin transparent thread inserted into the tip of his penis, urethral insertion, glowing threads, paralyzed",
      "the jellyfish woman numbs him with her threads from inside.", insert=True)
scene("atk_boss", "boss", "trench",
      "from side, her huge tentacles hold him up in the air, she penetrates his anus from behind with her futanari penis, anal, "
      "her tentacle tips suck on his nipples, his own erect penis is separate in front",
      "the kraken queen mates with him while her tentacles suck his nipples.", futa=True)

# ---- 敗北28
L = [
 ("btl_m1", "m", "pearl", "he lies on his back on the pearl clam bed, her tentacles wrapped around his whole body, purple ring-shaped suction marks around his nipples, cum floating as white clouds in the water, exhausted, tears of pleasure", "", {}),
 ("onani_m1", "m", "corr", "he stands waist-deep, nipple play, both hands pinching and pulling his own erect nipples, pearl nipple ornaments, his penis untouched, precum, flushed, sweat, several shadowy sea women silhouettes watching around him", "", {"onani": True}),
 ("inochi_m1", "m", "shaft", "he swims upward toward the bright surface, a long purple tentacle coils around his chest and pulls him back down, suction cups on his nipples, small seashell-shaped mark on his chest, desperate", "", {}),
 ("onedari_m1", "m", "ship", "he sits naked in the captain's chair, her tentacles hold his wrists to the armrests, suction cups on both of his nipples, she holds a large seashell board studded with rows of pearls without letters, he begs, open mouth", "", {}),
 ("btl_m2", "m", "ink", "he floats in a thick purple ink cloud, hands-free orgasm, cum floating as white clouds, arched back, dazed, she hovers above him whispering, she does not touch him", "", {}),
 ("onani_m2", "m", "temple", "kneeling, hands-free, he holds a small pearl bottle to his nose and inhales purple ink smoke, his fingertips stained violet, head tilted back, twitching, his penis untouched, precum, a huge curtain of purple ink between the pillars reflects his figure", "", {"onani": True}),
 ("inochi_m2", "m", "shaft", "he climbs a spiral path of purple ink toward the bright surface, he trembles and climaxes halfway, cum floating, sinking back, she waits below with open arms", "", {}),
 ("onedari_m2", "m", "pearl", "he kneels on the clam bed, she holds a small pearl bottle of purple ink under his nose, he inhales deeply, begging, eager, drooling", "", {}),
 ("btl_m3", "m", "temple", "from side, in front of the coral throne he is cradled in all eight tentacles like a cradle, a thick tentacle in his anus, anal, a very thin tentacle inserted into his penis tip, urethral insertion, suction cups on his nipples, cum", "", {"insert": True}),
 ("onani_m3", "m", "pearl", "from side, he kneels on the clam bed behind pearl curtains, one hand reaching behind him fingering his own anus, other hand pinching his own nipple, his penis untouched, one purple tentacle coiled around his ankle, shadowy sea women silhouettes peeking through the pearl curtains", "", {"onani": True}),
 ("inochi_m3", "m", "corr", "from side, he floats up the light shaft, purple tentacles wrapped around his waist pull him down, a tentacle pushed into his anus, anal, purple tentacle marks on his waist", "", {"insert": True}),
 ("onedari_m3", "m", "ship", "from side, he lies on the old wooden table, he holds up fingers counting, begging, six purple tentacles on his body, tentacles on his nipples, a tentacle in his anus, anal", "", {"insert": True}),
 ("btl_e1", "e1", "cove", "she holds him in her arms, singing into his ear, musical notes floating, he climaxes, cum floating as white clouds, limp, entranced", "", {}),
 ("onani_e1", "e1", "corr", "he kneels in the center of a ring of shadowy mermaid silhouettes slapping the water with their tails in rhythm, he sucks two fingers of one hand, other hand pinching his own nipple, his penis untouched, precum, flushed", "", {"onani": True}),
 ("inochi_e1", "e1", "shaft", "near the bright water surface she kisses him mouth to mouth, giving him breath, kiss, her tail coils around his legs, pulling him back down", "", {}),
 ("onedari_e1", "e1", "pearl", "inside a giant clam shell she holds a conch shell to his ear, three small conch shells white pink and gold hang on a cord around his neck, he begs", "", {}),
 ("btl_e2", "e2", "rocks", "from side, he sits on her tentacle skirt, pink tentacles pushed into his anus, anal, pink heart-shaped mark above his buttocks, cum floating, trembling", "", {"insert": True}),
 ("onani_e2", "e2", "rocks", "from side, he hides behind a rock, he sits on a soft pink sea anemone and grinds his hips on it, both hands pinching his own nipples, pink sting marks on his nipples, his penis untouched, sea anemones blooming around him", "", {"onani": True}),
 ("inochi_e2", "e2", "corr", "he tries to swim away, a long pink tentacle from her skirt coiled around his ankle pulls him back, pink ring on his ankle, she smiles on a rock", "", {}),
 ("onedari_e2", "e2", "rocks", "from side, on top of the rock he sits on her tentacle skirt, pink tentacles in his anus, anal, a spot of sunlight moves over a circle of white anemones like a clock, he begs", "", {"insert": True}),
 ("btl_e3", "e3", "jelly", "1girl and 1boy both clearly visible, the naked navy-haired young man is embraced inside her translucent umbrella dress, she hugs him from behind, many transparent threads on his body, a thread inserted into his penis tip, urethral insertion, glowing, paralyzed, cum floating", "", {"insert": True}),
 ("onani_e3", "e3", "sand", "he lies on the sand, one hand pressing his lower belly, right index finger with a thin transparent thread ring touching his own nipple, trembling as if numb, frustrated, his penis untouched, glowing jellyfish around him", "", {"onani": True}),
 ("inochi_e3", "e3", "shaft", "he lies limp on top of her translucent umbrella floating toward the bright surface, transparent threads stuck to his nipples, paralyzed, sinking", "", {}),
 ("onedari_e3", "e3", "ship", "he kneels, she hands him a tiny transparent jellyfish in a small glass bottle, transparent threads on his nipples, he begs", "", {}),
 ("btl_boss", "boss", "trench", "from side, on the black rock throne she holds him with her tentacles and penetrates his anus with her futanari penis, anal, tentacles on his nipples, black scale mark on his lower belly, his own penis separate, cum", "", {"futa": True}),
 ("onani_boss", "boss", "trench", "from side, on all fours on a rock ledge at the edge of the trench, one hand reaching behind him fingering his own anus with glowing red jelly on his fingers, his penis untouched, faint red glow inside his lower belly", "", {"onani": True}),
 ("inochi_boss", "boss", "trench", "from side, a thin dark red tentacle collar around his neck, she drags him down from the bright surface into the abyss while penetrating his anus with her futanari penis, anal, his own penis separate", "", {"futa": True}),
 ("onedari_boss", "boss", "vow", "from side, he kneels on all fours in front of the carved wall, begging, her tentacle tip pours glowing red jelly into his anus, anal, red jelly", "", {"insert": True}),
]
for key, who, place, action, _, opt in L:
    scene("lose_" + key, who, place, action, CH[who]["name"] + " makes him her captive of the sea.", **opt)

# ---- オナニーCG
# オナニーCGは責め手の得意技に合わせる（ペニスは触らない。2026-09-24 決定）
ON = {
    "m": ("temple", "m", "floating, both hands pinching and pulling his own erect nipples, his penis untouched, precum, flushed, sweat, trembling"),
    "e1": ("cove", "e1", "floating, he covers one ear with his hand as if listening to a song, sucking two fingers of his other hand, his penis untouched, precum, flushed, trembling"),
    "e2": ("rocks", "e2", "from side, he sits on a soft pink sea anemone on a rock and grinds his hips on it, pinching his own nipples, his penis untouched, flushed, trembling"),
    "e3": ("jelly", "e3", "floating, one hand pressing his lower belly, fingertip of the other hand touching his own nipple, trembling as if numb, his penis untouched, precum"),
    "boss": ("trench", "boss", "from side, kneeling, one hand reaching behind him fingering his own anus, other hand on his lower belly, his penis untouched, flushed, trembling"),
}
for k, (place, who, act) in ON.items():
    scene("onanie_" + k, who, place, act, "he pleasures himself alone underwater in her style while she watches.", onani=True)

# ---- 命乞い・おねだり（メルティナ単独）
m = CH["m"]
add("inochigoi", m["seed"], ", ".join([Q, "sensitive, solo", m["tags"], "hands clasped in front of her chest, pleading, teary eyes, sly smile, "
                                        "tentacles curled, looking at viewer, pov, upper body", UW, PL["temple"]]), NEG_BASE + NEG_NOFUTA)
add("onedari", m["seed"], ", ".join([Q, "sensitive, solo", m["tags"], "leaning toward viewer, one tentacle reaching toward viewer, finger on her lips, "
                                      "seductive smile, half-closed eyes, looking at viewer, pov", UW, PL["pearl"]]), NEG_BASE + NEG_NOFUTA)

# ---- 魔法・罠
MG = [
    ("magic_1", "m", "raising both arms, the sea water rising and swirling around her, bubbles, tide", "temple"),
    ("magic_2", "m", "a huge whirlpool spinning in front of her, her tentacles spread, commanding gesture", "temple"),
    ("magic_3", "e1", "sitting on a rock, singing, musical notes and glowing sound ripples spreading through the water", "cove"),
    ("magic_4", "m", "holding a large glowing conch shell to her lips, calling, many glowing lights approaching from the distance", "temple"),
    ("magic_5", "m", "blowing a thick cloud of purple ink toward viewer, pov, playful smile", "ink"),
]
for key, who, act, place in MG:
    c = CH[who]
    add(key, c["seed"], ", ".join([Q, "safe, solo", c["tags"], act, "looking at viewer", UW, PL[place]]), NEG_BASE + NEG_NOFUTA)

here = os.path.dirname(os.path.abspath(__file__))
json.dump({"code": "Scylla", "images": images}, open(os.path.join(here, "scylla_prompts.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(len(images), "images")
```

## 付録：2026-09-24 12:40 撮り直し後の変更（build_prompts.py の差分）
- lose_onani_m2・lose_onani_m3：吸盤の真似で自分の乳首をつまむ自慰に変更
- lose_onani_e1・onanie_e1：手を使わず歌って達する自慰に変更
- オナニー系のネガティブに「bikini, swimsuit, crop top, seashell bra on the man, bra on the man, nipple covers」を追加（主人公が胸当てを着けて見える対策。lose_onani_m1・onanie_m は旧画像のまま）

```diff
--- build_prompts.py（上の全文）
+++ build_prompts.py（撮り直し後・現行）
@@ -85,7 +85,7 @@
                          "erection", action, clothed, UW, PL[place], desc])
     neg = NEG_BASE + ("" if futa else NEG_NOFUTA) + NEG_SCENE + (NEG_INSERT if (insert or futa) else "") + (NEG_ONANI if onani else "")
     if onani:
-        neg += ", hand on penis, holding penis, stroking penis, handjob, penis on the woman, woman masturbating, girl masturbating, girl in foreground, white hair on the man, pink hair on the man, purple hair on the man"
+        neg += ", bikini, swimsuit, crop top, seashell bra on the man, bra on the man, nipple covers, hand on penis, holding penis, stroking penis, handjob, penis on the woman, woman masturbating, girl masturbating, girl in foreground, white hair on the man, pink hair on the man, purple hair on the man"
     add(key, c["seed"], pos, neg)
 
 
@@ -141,15 +141,15 @@
  ("inochi_m1", "m", "shaft", "he swims upward toward the bright surface, a long purple tentacle coils around his chest and pulls him back down, suction cups on his nipples, small seashell-shaped mark on his chest, desperate", "", {}),
  ("onedari_m1", "m", "ship", "he sits naked in the captain's chair, her tentacles hold his wrists to the armrests, suction cups on both of his nipples, she holds a large seashell board studded with rows of pearls without letters, he begs, open mouth", "", {}),
  ("btl_m2", "m", "ink", "he floats in a thick purple ink cloud, hands-free orgasm, cum floating as white clouds, arched back, dazed, she hovers above him whispering, she does not touch him", "", {}),
- ("onani_m2", "m", "temple", "kneeling, hands-free, he holds a small pearl bottle to his nose and inhales purple ink smoke, his fingertips stained violet, head tilted back, twitching, his penis untouched, precum, a huge curtain of purple ink between the pillars reflects his figure", "", {"onani": True}),
+ ("onani_m2", "m", "temple", "kneeling, bare flat chest with nothing worn on it, his fingertips pinching and pulling his own bare erect nipples, purple ink mist drifting around his face and he inhales it, his penis untouched, precum, a huge curtain of purple ink between the pillars reflects his figure", "", {"onani": True}),
  ("inochi_m2", "m", "shaft", "he climbs a spiral path of purple ink toward the bright surface, he trembles and climaxes halfway, cum floating, sinking back, she waits below with open arms", "", {}),
  ("onedari_m2", "m", "pearl", "he kneels on the clam bed, she holds a small pearl bottle of purple ink under his nose, he inhales deeply, begging, eager, drooling", "", {}),
  ("btl_m3", "m", "temple", "from side, in front of the coral throne he is cradled in all eight tentacles like a cradle, a thick tentacle in his anus, anal, a very thin tentacle inserted into his penis tip, urethral insertion, suction cups on his nipples, cum", "", {"insert": True}),
- ("onani_m3", "m", "pearl", "from side, he kneels on the clam bed behind pearl curtains, one hand reaching behind him fingering his own anus, other hand pinching his own nipple, his penis untouched, one purple tentacle coiled around his ankle, shadowy sea women silhouettes peeking through the pearl curtains", "", {"onani": True}),
+ ("onani_m3", "m", "pearl", "he kneels on the clam bed behind pearl curtains, both hands pinching and pulling his own erect nipples like suction cups, one purple tentacle coiled around his ankle and another purple tentacle creeping up his thigh, his penis untouched, precum, shadowy sea women silhouettes peeking through the pearl curtains", "", {"onani": True}),
  ("inochi_m3", "m", "corr", "from side, he floats up the light shaft, purple tentacles wrapped around his waist pull him down, a tentacle pushed into his anus, anal, purple tentacle marks on his waist", "", {"insert": True}),
  ("onedari_m3", "m", "ship", "from side, he lies on the old wooden table, he holds up fingers counting, begging, six purple tentacles on his body, tentacles on his nipples, a tentacle in his anus, anal", "", {"insert": True}),
  ("btl_e1", "e1", "cove", "she holds him in her arms, singing into his ear, musical notes floating, he climaxes, cum floating as white clouds, limp, entranced", "", {}),
- ("onani_e1", "e1", "corr", "he kneels in the center of a ring of shadowy mermaid silhouettes slapping the water with their tails in rhythm, he sucks two fingers of one hand, other hand pinching his own nipple, his penis untouched, precum, flushed", "", {"onani": True}),
+ ("onani_e1", "e1", "corr", "he floats upright with both arms spread limp in the water, his hands not touching his body, singing with open mouth, musical notes floating around him, arched back, hips twitching, his penis untouched, precum, a ring of shadowy mermaid silhouettes slapping the water with their tails", "", {"onani": True}),
  ("inochi_e1", "e1", "shaft", "near the bright water surface she kisses him mouth to mouth, giving him breath, kiss, her tail coils around his legs, pulling him back down", "", {}),
  ("onedari_e1", "e1", "pearl", "inside a giant clam shell she holds a conch shell to his ear, three small conch shells white pink and gold hang on a cord around his neck, he begs", "", {}),
  ("btl_e2", "e2", "rocks", "from side, he sits on her tentacle skirt, pink tentacles pushed into his anus, anal, pink heart-shaped mark above his buttocks, cum floating, trembling", "", {"insert": True}),
@@ -172,7 +172,7 @@
 # オナニーCGは責め手の得意技に合わせる（ペニスは触らない。2026-09-24 決定）
 ON = {
     "m": ("temple", "m", "floating, both hands pinching and pulling his own erect nipples, his penis untouched, precum, flushed, sweat, trembling"),
-    "e1": ("cove", "e1", "floating, he covers one ear with his hand as if listening to a song, sucking two fingers of his other hand, his penis untouched, precum, flushed, trembling"),
+    "e1": ("cove", "e1", "floating, both arms limp at his sides, his hands not touching his body, singing softly with open mouth, musical notes floating around him, hips twitching, his penis untouched, precum, flushed, trembling"),
     "e2": ("rocks", "e2", "from side, he sits on a soft pink sea anemone on a rock and grinds his hips on it, pinching his own nipples, his penis untouched, flushed, trembling"),
     "e3": ("jelly", "e3", "floating, one hand pressing his lower belly, fingertip of the other hand touching his own nipple, trembling as if numb, his penis untouched, precum"),
     "boss": ("trench", "boss", "from side, kneeling, one hand reaching behind him fingering his own anus, other hand on his lower belly, his penis untouched, flushed, trembling"),
```
