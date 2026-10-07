> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版：2026-09-23 昼（JST）にこの会話で project_write した全文）

# N2 男の娘サークルの先輩（Circle）MOD 画像制作シート

> **2026-09-23 画像生成 済み。** 採用した52枚を `Downloads\N2_Circle\Picture\Circle\` に正しい名前で配置（カードの参照名と一致）。ゲームの `Picture\Circle\` へフォルダごとコピーすれば使える。
> 生成は共通ツール（`Downloads\tools`）。場面定義は `tools\scene_overrides.py` の `O["Circle"]`、プロンプトは `tools\prompts\Circle_prompts.json`（53枚。`Circle_bg` はカード未使用）。旧 `N2_Circle\circle_kit` は使わない。

## 生成の記録（2026-09-23）
- 全53枚を1回生成 → 目視で11枚が不良（主に**ハルカの場面で服と裸が入れ替わる**：主人公がパーカーを着て、ハルカが裸になる）。
- ハルカの場面文を「black hoodie」に統一（立ち絵と同じ黒パーカー）してから、不良11枚を候補4枚ずつ撮り直して採用。`lose_onani_m1` は構図を「スツールに座る」→「立って屈んでキス」に変えて再撮影。
- 採用した撮り直し：atk_e1 #1／atk_m1 #1／atk_m3 #3／lose_btl_m1 #3／lose_btl_m3 #3／lose_inochi_e1 #3／lose_inochi_m2 #3／lose_onani_m1（reroll2）#7／lose_onani_m3 #2／lose_onedari_e2 #2／lose_onedari_m3 #3（ComfyUI の `output\Circle_reroll\`・`Circle_reroll2\`）。
- 教訓：小柄で可愛い責め手（ハルカ）はフード付きの服が主人公に移りやすい。責め手の服の色を場面文で固定し、主人公を座らせ／寝かせ、責め手を立たせる構図が安定。
- ワンクリック用：`tools\gen_Circle_all.bat`（ComfyUIが起動していなければ起動→全枚数を投入）、`tools\reroll_Circle.bat`（上の11枚を候補4枚で撮り直し）。

## 手順（作り直すとき）
```
cd C:\Users\taku2\Downloads\tools
run_mod.bat Circle all                              ← 全53枚
run_mod.bat Circle <キー> --random --batch 4        ← 崩れた1枚を候補4枚で撮り直す
install_images.bat Circle "<ゲームフォルダ>\Picture"   ← _00001_ を外して Picture\Circle\ へ（同じキーは一番新しい画像）
```

## 場面定義の要点（シナリオ準拠）
- 主人公：`short messy dark green hair, bangs covering his eyes, faceless`。場面では常に裸。
- 責め手は常に服を着たまま。責め手自身のペニスは描かない（指とアナルパールのみ）。
- 場所：部室のソファ（夕日）／ブラインドを下ろした部室（タオルとローション）／手鏡のある部室／ミオの隅（シール付きロッカー）／ツバサの隅（トレーニングマット）／カイトの窓際の椅子／カードを広げた机／シズクの背もたれの高い椅子と机／居酒屋の個室（魔法1・4）。
- 文字の出る小物は描かない。シズクの敗北は構図を分けた（戦闘＝椅子の前でキス、オナニー＝砂時計、命乞い＝鍵のネックレス、おねだり＝机に伏せてアナルパール）。
- `inochigoi` と `onedari` もカードに定義があるため生成対象に含めた。

## カード側の修正（2026-09-23・済）
- おねだり負け m2・m3 を書き直し（5,318字／5,102字）。if の重ね書き（マスター16・下級上級各1）に { } を付けた。詳細は `N2_Circle\README_N2_Circle.md`。

## 未対応（要判断）
- ゲージがマスターのローカル変数 `$キス度` で、`@ターン終了宣言` で −1 される（共通ルールと違う）。実機で見てから判断。
- 実機での画像表示確認（カード画像・攻撃時・敗北時）。
