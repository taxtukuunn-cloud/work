# N12 乳首開発サロン（Salon）ComfyUI プロンプト（全51枚）

> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版：この会話で 2026-09-23T11:02 に登録した全文）

作成：2026-09-23。登場人物は全員20歳以上。個人利用のみ。

## 生成のしかた
- ツール：ユーザーのPCの `Downloads\tools`（共通の画像一括生成ツール）。
- `gen_Salon_all.bat` をダブルクリック → ComfyUIが起動していなければ起動し、51枚を投入。出力は `ComfyUI\output`。
- 全部できたら `install_images.bat Salon "<ゲーム>\Picture"` で `Picture\Salon\` に正しい名前で入る。
- 撮り直し：`run_mod.bat Salon <キー> --random --batch 4`。
- プロンプトの正本：`prompts\Salon_prompts.json`（`scene_overrides.py` の `SL` を `apply_scene_overrides.py Salon` で組み立てたもの）。
- 状態：**プロンプト登録済み・生成はまだ**（ユーザーがバッチを実行する）。

## 見た目（char_data.py に反映済み）
| 人物 | 髪・瞳 | 服装 |
|---|---|---|
| カレン（マスター） | 赤茶のウェーブ・琥珀 | 黒いタイトなサロンドレス＋白い短いジャケット |
| エマ（下級1） | 金髪ボブ・青 | 白い施術服＋薄手の白手袋 |
| ココ（下級2） | ピンクブラウンのツインテール・紫 | 淡いピンクの施術服 |
| ルル（下級3） | 紫のロングストレート・灰 | 黒いサロン制服＋黒手袋 |
| セラ（上級） | 深紅のまとめ髪・金 | 黒いイブニングドレス＋銀の鍵束の鎖 |
| 主人公 | 紺の短髪（前髪で目が隠れた顔なし） | 場面では常に裸 |

- 責めは乳首（指・舌・吸引カップ・クリップ・鍵）だけ。全場面に「彼のペニスには触れない」。貞操帯は股間だけの平たい檻（勃起なし）。
- 1枚に描くのは主人公と主役の責め手の2人だけ。文字の出る小物（カルテ・会員証の文字）は描かない。

## scene_overrides.py に追加した定義（全文）
```python
# N12 乳首開発サロン（Salon）…シナリオ（会員制サロン ヴェルヴェット）準拠
#   責め手は女性スタッフ5人。常に服を着たまま。責めは乳首（指・舌・吸引カップ・クリップ）と
#   貞操帯（股間だけの平たい檻）・鍵での焦らし。主人公のペニスには触れない。文字の出る小物は使わない。
# ===============================================================
SALON_PLACE = {
    "reception": "reception and waiting room of an exclusive members-only salon, deep purple walls, soft warm lamps, "
                 "brown leather sofa, vase of lavender, dim elegant lighting",
    "counsel":   "bright white counseling room of a beauty salon, round white table, white chairs, sheer curtains, soft daylight",
    "treat":     "treatment room of a luxury salon, white reclining treatment table, large full-length mirror on the wall, "
                 "soft warm indirect lighting, ivory walls, towels folded on a side table",
    "tools":     "equipment room of a salon, glass shelves lined with small transparent suction cups, nipple clamps and small metal chastity devices, "
                 "leather treatment chair in the center, cool soft lighting",
    "manager":   "manager's private room of a luxury salon, deep crimson walls and carpet, large canopy bed with sheer crimson curtains, "
                 "candlelight, gold ornaments",
    "keys":      "dim salon back room, a black wooden wall covered with rows of hooks holding many small silver keys, "
                 "high-backed leather chair, warm lamp light",
}
PROTAG["Salon"] = "short messy navy blue hair, bangs covering his eyes, faceless"

SL_CUPS = "small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, thin tube to a small hand pump"
SL_CLIPS = "small silver nipple clamps with tiny adjustment screws pinching both of his nipples"
SL_CAGE = "small flat metal chastity cage on his crotch"
SL_KEY = "a small silver key held between her fingertips"

_K = "the auburn-haired woman in a black tight salon dress and short white jacket"
_EM = "the blonde bob-haired woman in a white esthetician uniform and thin white gloves"
_CO = "the pink brown twintailed woman in a pale pink esthetician uniform"
_LU = "the long purple-haired woman in a black salon uniform and black gloves"
_SE = "the dark red-haired woman in a black evening dress with a bundle of small silver keys on a chain"

SL = {}

# --- 技CG（攻撃時） ---
SL["atk_m1"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on the white reclining treatment table with the backrest half raised, chest arched, "
          + _K + " stands at his side and bends over him, licking his left nipple with the tip of her tongue "
          "while circling his right nipple with her fingertip, she does not touch his penis, the small slim man biting his lip, blushing")
SL["atk_m2"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man reclines on the white treatment table, " + SL_CUPS + ", " + _K + " stands beside the table, "
          "calmly squeezing the small hand pump and watching his face with a business smile, she does not touch his penis, "
          "the small slim man gasping, chest pushed up")
SL["atk_m3"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on the edge of the treatment table facing the large mirror, " + SL_CAGE + ", "
          + _K + " stands close behind him and reaches around from behind, fingertips rolling both of his nipples, "
          "her chin near his shoulder, she does not touch his penis, the small slim man squirming, reflection in the mirror")
SL["atk_e1"] = dict(who="e1", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on the white treatment table, " + _EM + " stands beside the table and leans over him, "
          "pinching both of his nipples lightly between gloved thumb and finger and twisting them, focused expert expression, "
          "she does not touch his penis, the small slim man arching his back")
SL["atk_e2"] = dict(who="e2", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on the white treatment table, " + _CO + " kneels on the floor beside the table with her face at his chest, "
          "sticking out her pink tongue and licking his nipple, playful smirk, looking up at him, saliva, she does not touch his penis, "
          "the small slim man blushing, trembling")
SL["atk_e3"] = dict(who="e3", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in the leather treatment chair, " + SL_CUPS + ", " + _LU + " stands beside the chair "
          "holding the hand pump in her black gloved hand, reading a small round pressure gauge with a cool expressionless face, "
          "she does not touch his penis, the small slim man squirming")
SL["atk_boss"] = dict(who="boss", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on the edge of the canopy bed, " + SL_CAGE + ", " + _SE + " stands in front of him and bends down, "
          "dangling " + SL_KEY + " in front of his face while her other hand pinches his nipple, whispering into his ear, "
          "she does not touch his penis, the small slim man trembling, flustered")

# --- オナニーCG（主人公が一人で。責め手は奥で離れて見ているだけ） ---
SL["onanie_master"] = dict(who="master", place="reception", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits alone on the leather sofa and secretly pinches his own nipples with both hands, " + SL_CAGE + ", "
          "blushing, ashamed, " + _K + " stands in the far background by the reception counter with a clipboard, watching with a knowing smile")
SL["onanie_e1"] = dict(who="e1", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits alone on the treatment table and rolls his own nipples with his fingertips, " + SL_CAGE + ", "
          "trembling, blushing, " + _EM + " stands in the far background near the door with gloved hands folded, watching calmly")
SL["onanie_e2"] = dict(who="e2", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits alone on a white chair and pinches his own wet nipples, " + SL_CAGE + ", flushed, panting, "
          + _CO + " leans against the far wall in the background, sticking out her tongue teasingly, watching")
SL["onanie_e3"] = dict(who="e3", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits alone in the leather chair and presses both hands on his own locked chastity cage, " + SL_CAGE + ", "
          "frustrated, pinching own nipple, " + _LU + " stands in the far background beside the glass shelves, watching coolly")
SL["onanie_boss"] = dict(who="boss", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man kneels alone on the crimson carpet and pinches his own nipples, " + SL_CAGE + ", desperate, blushing, "
          + _SE + " sits far away in an armchair in the background, legs crossed, twirling the key chain, watching")

# --- 敗北CG（シナリオの絶頂・屈服の場面） ---
SL["lose_btl_m1"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a white reclining treatment table, backrest half raised, chest arched, large full-length mirror at the foot of the table, the auburn-haired woman in a black tight salon dress and short white jacket stands at his side and bends over him, licking his left nipple with the tip of her tongue while pinching his right nipple between bare fingers, she does not touch his penis, hands-free orgasm, trembling, soft amber indirect light")
SL["lose_btl_m2"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man reclines on a white reclining treatment table facing a large mirror, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, thin tubes to a small hand pump, the auburn-haired woman in a black tight salon dress and short white jacket stands beside the table in white gloves and slowly twists one cup with her fingertips, she does not touch his penis, back arching, hands-free orgasm, silver tray of cups nearby")
SL["lose_btl_m3"] = dict(who="master", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a white reclining treatment table, small flat metal chastity cage on his crotch, the auburn-haired woman in a black tight salon dress and short white jacket sits on a stool beside him, brushing his right nipple with a soft feather brush while gently rolling his left nipple between finger and thumb, she does not touch his penis, toes curling, hands-free orgasm, large mirror on the wall, warm orange light")
SL["lose_onani_m1"] = dict(who="master", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a chair at a round white table in a bright counseling room, both palms pressed flat on the tabletop, chest pushed forward, the auburn-haired woman in a black tight salon dress and short white jacket leans across the table from the opposite side, sucking his left nipple and pinching his right nipple with her fingertips, she does not touch his penis, he trembles in orgasm, hands stay on the table, clean white walls")
SL["lose_onani_m2"] = dict(who="master", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a small leather treatment chair in an equipment room, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, he squeezes the small hand pump himself, the auburn-haired woman in a black tight salon dress and short white jacket stands beside the chair, her white gloved fingers gently shaking one cup, she does not touch his penis, shelves of cups and clamps behind, afternoon light glinting on glass, hands-free orgasm")
SL["lose_onani_m3"] = dict(who="master", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a leather chair with his wrists buckled to the armrests, small flat metal chastity cage on his crotch, the auburn-haired woman in a black tight salon dress and short white jacket stands in front of him and bends forward, tracing the serrated tip of a small silver key across his right nipple while her other fingers pinch his left nipple, she does not touch his penis, trembling orgasm, bright afternoon light from a high window")
SL["lose_inochi_m1"] = dict(who="master", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a tall white treatment chair in an equipment room, small flat metal chastity cage on his crotch, the auburn-haired woman in a black tight salon dress and short white jacket kneels on the floor beside the chair with her sleeves rolled up, licking his right nipple while pinching and lifting his left nipple with her fingers, she does not touch his penis, he arches back, shelves of suction cups and small silver keys in the background")
SL["lose_inochi_m2"] = dict(who="master", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a chair at a white table in a counseling room, wrists strapped to the armrests with soft leather bands, small flat metal chastity cage on his crotch, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, the auburn-haired woman in a black tight salon dress and short white jacket kneels beside the chair, tapping one cup with a small silver key, she does not touch his penis, hands-free orgasm, morning light through lace curtains")
SL["lose_inochi_m3"] = dict(who="master", place="keys", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a low leather bench in front of a wall of hooks hung with rows of small silver keys, small flat metal chastity cage on his crotch, the auburn-haired woman in a black tight salon dress and short white jacket stands in front of him, bending down to pinch and slowly roll both of his nipples with her fingertips, she does not touch his penis, he leans back limp in quiet orgasm, dim lamp light glinting on the keys")
SL["lose_onedari_m1"] = dict(who="master", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a white-sheeted canopy bed in a deep crimson room lit by candles, the auburn-haired woman in a black tight salon dress and short white jacket sits on the edge of the bed and leans over him, sucking his left nipple while pinching his right nipple between her fingers, she does not touch his penis, his back arches off the sheets, hands-free orgasm, sheer crimson canopy drapes")
SL["lose_onedari_m2"] = dict(who="master", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a canopy bed in a crimson room, large transparent suction cups covering both of his nipples and areolae, nipples sucked up and swollen inside the cups, the auburn-haired woman in a black tight salon dress and short white jacket sits on the edge of the bed, holding both cups with white gloved hands and slowly rocking them, she does not touch his penis, back arched, hands-free orgasm, candlelight")
SL["lose_onedari_m3"] = dict(who="master", place="reception", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits deep in a large brown leather sofa in a waiting room with morning light from high windows, small flat metal chastity cage on his crotch, the auburn-haired woman in a black tight salon dress and short white jacket sits sideways right beside him on the sofa, pinching and rolling both of his oil-glossed nipples with her fingertips, she does not touch his penis, chest pushed out, he trembles in orgasm, lavender flowers on a side table")
SL["lose_btl_e1"] = dict(who="e1", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man reclines on a white reclining treatment table in front of a large full-length mirror, small flat metal chastity cage on his crotch, the blonde bob-haired woman in a white esthetician uniform and thin white gloves stands beside the table and leans over him, pressing both of his nipples down with her gloved fingertips at the same time, she does not touch his penis, back arched like a bow, hands-free orgasm, soft indirect light")
SL["lose_onani_e1"] = dict(who="e1", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a backless round stool in an equipment room, small flat metal chastity cage on his crotch, small silver nipple clamps with tiny screws pinching both of his nipples, his right hand rests palm up on a silver tray beside him, the blonde bob-haired woman in a white esthetician uniform and thin white gloves stands at his side turning the screw of one clamp with her fingertips, she does not touch his penis, orange evening sunlight, knees trembling, orgasm")
SL["lose_inochi_e1"] = dict(who="e1", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a white armchair at a round white table at midnight, gripping the armrests, small flat metal chastity cage on his crotch, the blonde bob-haired woman in a white esthetician uniform and thin white gloves stands behind the chair and reaches over his shoulders, pinching both of his nipples and gently pulling them forward, she does not touch his penis, a small silver key lies on the table, he arches back in orgasm")
SL["lose_onedari_e1"] = dict(who="e1", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a canopy bed in a crimson room, small flat metal chastity cage on his crotch, thin small silver nipple clamps pinching both of his nipples, a tiny bell hanging from each clamp, the blonde bob-haired woman in a white esthetician uniform and thin white gloves sits on the edge of the bed and leans over him, circling one clamped nipple tip with her gloved fingertip, she does not touch his penis, hands-free orgasm")
SL["lose_btl_e2"] = dict(who="e2", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man reclines on a white reclining treatment table, wrists tied to the armrests with soft cloth straps, large mirror on the wall, the pink brown twintailed woman in a pale pink esthetician uniform stands beside the table and bends over his chest, flicking his right nipple with her long pink tongue while her fingertip circles his wet left nipple, she does not touch his penis, tongue out, saliva shine, hands-free orgasm, back arching")
SL["lose_onani_e2"] = dict(who="e2", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a high-backed treatment chair in a dim equipment room at midnight, wrists tied to the armrests with pink ribbons, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, the pink brown twintailed woman in a pale pink esthetician uniform kneels beside the chair, licking the swollen skin around the rim of one cup and holding a round pink hand pump, she does not touch his penis, hands-free orgasm")
SL["lose_inochi_e2"] = dict(who="e2", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies back on a long white sofa in a counseling room in orange evening light, small flat metal chastity cage on his crotch, a small silver key on a thin pink cord resting wet on his chest, the pink brown twintailed woman in a pale pink esthetician uniform kneels on the floor beside the sofa, licking his nipple and the wet key together with her pink tongue, she does not touch his penis, trembling orgasm")
SL["lose_onedari_e2"] = dict(who="e2", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a canopy bed with crimson sheets, morning light through a gap in heavy curtains, the pink brown twintailed woman in a pale pink esthetician uniform kneels on the bed beside him and bends down sucking his right nipple, a small transparent suction cup on his left nipple, nipple sucked up and swollen inside the cup, she squeezes a round pink pump, she does not touch his penis, hips lifting, hands-free orgasm")
SL["lose_btl_e3"] = dict(who="e3", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on a white reclining treatment table, wrists buckled with soft leather belts, large mirror on the wall, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, tubes to a hand pump with a round pressure gauge, the long purple-haired woman in a black salon uniform and black gloves stands beside the table pressing the top of one cup with a black fingertip, she does not touch his penis, expressionless, hands-free orgasm")
SL["lose_onani_e3"] = dict(who="e3", place="tools", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a chair in an equipment room, small flat metal chastity cage on his crotch, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, hands on his knees, the long purple-haired woman in a black salon uniform and black gloves stands in front of him, holding up a small silver key while twisting one cup, she does not touch his penis, hands-free orgasm")
SL["lose_inochi_e3"] = dict(who="e3", place="keys", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a tall leather armchair facing a wall of small silver keys, small flat metal chastity cage on his crotch with an extra ring lock, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, the long purple-haired woman in a black salon uniform and black gloves stands beside the chair flicking the rim of one cup with her fingertip, she does not touch his penis, he grips the armrests")
SL["lose_onedari_e3"] = dict(who="e3", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on the edge of a canopy bed in a crimson room, small flat metal chastity cage on his crotch, a small transparent suction cup on his left nipple, nipple sucked up and swollen inside the cup, the long purple-haired woman in a black salon uniform and black gloves stands in front of him and pinches his swollen right nipple directly with her black gloved fingers, holding the hand pump in her other hand, she does not touch his penis, trembling orgasm")
SL["lose_btl_boss"] = dict(who="boss", place="manager", nude=True, penis=False, safety="explicit",
    scene="the small slim man lies on his back on a large canopy bed in a deep crimson room, small flat metal chastity cage on his crotch, the dark red-haired woman in a black evening dress with a bundle of small silver keys on a chain sits on the edge of the bed, dangling one small silver key just above his chest while her other hand pinches his left nipple, she does not touch his penis, hands-free orgasm, sheer canopy drapes, warm lamplight")
SL["lose_onani_boss"] = dict(who="boss", place="treat", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a chair facing a tall full-length mirror, hands clasped on his knees, small flat metal chastity cage on his crotch, the dark red-haired woman in a black evening dress with a bundle of small silver keys on a chain stands behind the chair and reaches over his shoulder, touching the tip of a small silver key to his right nipple while her other hand pinches his left nipple, she does not touch his penis, orgasm reflected in the mirror")
SL["lose_inochi_boss"] = dict(who="boss", place="keys", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits in a high-backed leather chair facing a black wooden wall of hooks hung with hundreds of small silver keys, small flat metal chastity cage on his crotch with a second small padlock, a small silver key rests on his open trembling palm, the dark red-haired woman in a black evening dress with a bundle of small silver keys on a chain stands beside the chair, rolling both of his nipples between her fingers, she does not touch his penis, red sunset light, hands-free orgasm")
SL["lose_onedari_boss"] = dict(who="boss", place="counsel", nude=True, penis=False, safety="explicit",
    scene="the small slim man sits on a chair at a round white table in a bright white counseling room, morning sun through the window, small flat metal chastity cage on his crotch, chest pushed forward, the dark red-haired woman in a black evening dress with a bundle of small silver keys on a chain sits across the table and leans forward, reaching over it to roll both of his nipples between her fingertips, she does not touch his penis, a small silver key lies on the table, hands-free orgasm")

# --- 魔法・罠 ---
SL["magic_1"] = dict(who="master", place="reception", nude=None, penis=False, safety="general",
    scene=_K + " holds out a plain black membership card with gold edges toward the viewer, no text on the card, business smile, pov, looking at viewer")
SL["magic_2"] = dict(who="e3", place="tools", nude=None, penis=False, safety="general",
    scene=_LU + " holds up a small flat metal chastity device and a small silver padlock in her black gloved hands, "
          "cool expressionless face, looking at viewer")
SL["magic_3"] = dict(who="master", place="treat", nude=None, penis=False, safety="general",
    scene=_K + " stands beside the empty white reclining treatment table and gestures toward it with an open hand, "
          "inviting, soft smile, looking at viewer")
SL["magic_4"] = dict(who="master", place="counsel", nude=None, penis=False, safety="general",
    scene=_K + " sits at the round white table holding a pen over a blank notebook, leaning forward with a gentle smile, "
          "pov, across the table, looking at viewer")
SL["magic_5"] = dict(who="boss", place="keys", nude=None, penis=False, safety="general",
    scene=_SE + " stands in front of the wall of small silver keys and holds one small silver key up to her lips, "
          "teasing refusal, half-closed eyes, looking at viewer")

# --- 背景 ---
SL["bg"] = dict(who=None, place="treat", nude=None, penis=False, safety="general",
    scene="no humans, scenery, interior, background")
O["Salon"] = SL
```

## 組み立て後のプロンプトの例（lose_btl_e3。ほかは prompts\Salon_prompts.json）
```
masterpiece, best quality, score_7, explicit, 1girl, 1boy, cfnm, femdom, two different characters, the purple-haired woman wearing black salon uniform, black gloves is the one doing everything to the naked navy blue-haired small slim man, the naked navy blue-haired small slim man only receives, the naked navy blue-haired small slim man never touches the purple-haired woman wearing black salon uniform, black gloves, the naked navy blue-haired small slim man lies on a white reclining treatment table, wrists buckled with soft leather belts, large mirror on the wall, small transparent suction cups on both of his nipples, nipples sucked up and swollen inside the cups, tubes to a hand pump with a round pressure gauge, the long purple-haired woman in a black salon uniform and black gloves stands beside the table pressing the top of one cup with a black fingertip, she does not touch his penis, expressionless, hands-free orgasm, the purple-haired woman wearing black salon uniform, black gloves: adult woman, purple hair, long straight hair, grey eyes, black salon uniform, black gloves, composed, medium breasts, fully clothed, both of her eyes clearly visible, dominant confident attitude, taller than the naked man, the naked navy blue-haired small slim man: faceless male, hair over eyes, short messy navy blue hair, bangs covering his eyes, faceless, eyes completely covered by hair, no visible eyes, bare hands, no gloves, embarrassed flustered expression, blushing, adult male in his twenties, adult body proportions, small delicate build, slender, thin, narrow shoulders, smooth skin, no muscles, flat male chest, submissive, weak, the one being dominated, the smallest person in the scene, completely naked, erection, penis, precum, much smaller and shorter than the purple-haired woman wearing black salon uniform, black gloves, the naked navy blue-haired small slim man wears no clothing at all, not wearing black salon uniform, black gloves, treatment room of a luxury salon, white reclining treatment table, large full-length mirror on the wall, soft warm indirect lighting, ivory walls, towels folded on a side table, detailed background, indoors, clothed female, cfnm, his erect penis never penetrates her, he does not insert into her, she never has his penis inside her, he only receives penetration, she remains fully in control, femdom power dynamic, one-directional
```

## ネガティブの例（lose_btl_e3）
```
lowres, worst quality, low quality, watermark, text, signature, child, loli, shota, young, teenage, underage, immature, muscular, abs, pectorals, broad shoulders, thick arms, bara, big body, tall man, collar, choker, leash, vaginal, vaginal sex, cowgirl position, pussy, nude female, futanari, boy behind girl, 1girl on the receiving end, penis in vagina, penis inside her, sex with her, heterosexual sex, male on top, missionary position, male penetrating, male thrusting into her, boy penetrating, boy inserting, boy holding her hips, male dominant position, he penetrates her, love making, face fucking, irrumatio, male gripping her head, reverse roles, role reversal, receiver penetrating, receiver inserting, receiver on top, receiver dominant, small slim man penetrating, small slim man inserting, protagonist penetrating, protagonist inserting, receiver thrusting, small man on top, bottom on top, merged, fused, overlapping, penis touching penis, penis touching strap-on, giant dildo, oversized dildo, comically large dildo, excessively large dildo, tiny anal beads, thin anal beads, small anal beads, deeply inserted urethral sound, fully inserted urethral sound, urethral sound buried inside, urethral sound not inserted, urethral sound fully outside, bulging chastity cage, large chastity cage, tightly closed anus, barely open, small gape, thin watery liquid, clear liquid, runny lubricant, attacker masturbating, woman masturbating, attacker touching herself, attacker touching himself, attacker embarrassed, attacker submissive, attacker blushing, attacker vulnerable, attacker aroused and helpless, dominant character receiving, dominant character being pleasured, attacker on the receiving end, attacker pleasuring herself, huge penis, extra legs, three legs, four legs, extra arms, extra limbs, extra hands, bad anatomy, deformed, fused legs, tangled limbs, disembodied limb, floating limbs, twins, identical twins, clones, same face, same hairstyle, same hair color, duplicate character, two of the same person, visible eyes on the small slim man, smiling small slim man, child, childlike body, two penises, multiple penises, penis on both characters, bottomless attacker, handjob, holding penis, hand on penis, nude female, naked woman, topless woman, female chastity belt, woman wearing chastity belt, third person, extra person, more than two people, duplicate woman, two women
```