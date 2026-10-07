# ロゼッタMOD 画像制作シート（WAI-Anima / Anima系用）

保存先はすべて `Picture/Rosetta/`。全24枚。登場人物は全員成人。
主人公は描かず、**POV（主人公視点）**で、ロゼッタ側だけを描く構図にしています。

## 1. 必要なファイル（Anima系は3つに分かれています）
| 種類 | ファイル | 置き場所（`ComfyUI\models\` の下） |
|---|---|---|
| モデル本体 | `waiANIMA_v10.safetensors`（WAI-Anima） | `diffusion_models\` |
| テキストエンコーダ | `qwen_3_06b_base.safetensors` | `text_encoders\` |
| VAE | `qwen_image_vae.safetensors` | `vae\` |
- テキストエンコーダとVAEは公式リポジトリ（circlestone-labs/Anima）の `split_files/` の中にあります。
- 置いたら**ComfyUIを再起動**。ComfyUI が古いと Anima が動かないので、先に更新してください（`update` フォルダの `update_comfyui.bat`）。

## 2. 生成設定（公式推奨）
- 解像度：832×1216（512²〜1536²の範囲で可）／ステップ：30〜50／CFG：4〜5
- サンプラー：`er_sde`（標準）／スケジューラ：`simple`。柔らかい線なら `euler_a`。
- 読み込みノード：UNETLoader ＋ CLIPLoader（**type は `qwen_image`**）＋ VAELoader。

## 3. プロンプトの書き方（Anima の作法）
- **Danbooruタグ**（小文字・スペース区切り・アンダースコアなし。`score_7` だけ例外）。
- 順番：`[品質/安全タグ] [人数] [キャラ] [一般タグ]`。品質タグは `masterpiece, best quality, score_7`。
- **安全タグ**：`safe` / `sensitive` / `nsfw` / `explicit`。各画像に合わせて指定済み。
- ネガティブは共通（品質低下・透かし・未成年除外語を含む）。
- 一貫性：シード固定＋キャラのタグを毎回同じにする（下の「キャラタグ」を使う）。

## 4. キャラタグ（各プロンプトに含まれています）

- **ROSETTA**：`1girl, solo, mature female, tall, large breasts, long hair, wavy hair, black hair, purple eyes, small horns, demon tail, black dress, gothic, rose, smirk`
- **ELSA**：`1girl, solo, adult, large breasts, brown hair, low ponytail, yellow eyes, black flower, hair flower, maid, gentle smile`
- **VIVIAN**：`1girl, solo, mature female, silver hair, hair bun, glasses, semi-rimless eyewear, labcoat, white coat, black dress, gloves, serious`
- **SLAVE**：`1boy, solo, adult male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, crossdressing, black lingerie, black collar, leash, blush, submissive`

## 5. 背景除去（立ち絵7枚）
対象：`Rosetta_master` / `Elsa` / `Vivian` / `Mireille` / `Rosetta_mons_Slave` `_2` `_3`。
- ワークフローに背景除去（InspyrenetRembg）を組み込み済み。プロンプトも `white background` で切り抜きやすくしています。
- 導入：ComfyUI-Manager →「Inspyrenet Rembg」→ インストール →再起動（無い場合は `--no-rembg`）。
- 手動（`Rosetta_workflow.json`）：⑥が背景あり、⑦が背景除去（立ち絵用）の保存先。

## 6. 画像ごとのプロンプト
各行のプロンプトの前に、品質タグ・安全タグ・キャラタグが付いた完成形は `Rosetta_prompts.json` の `positive` にあります。

### A. ロゼッタ（マスター）— 攻撃時・シーン用
| ファイル | いつ表示されるか | 安全 / キャラ / シーンタグ |
|---|---|---|
| `Rosetta_master.png` | 通常立ち絵／イベント導入／勝利時／カード画像 | `safe` / ROSETTA / `standing, hand on hip, looking at viewer, simple background, white background, full body` |
| `Rosetta_nipple.png` | 乳首責め攻撃時（H） | `explicit` / ROSETTA / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, pov, topless male, nipples, lying on back, on bed, leaning over, nipple tweak, licking nipple, saliva, clothed female, cfnm, seductive smile, looking at viewer, femdom` |
| `Rosetta_prostate.png` | 前立腺責め攻撃時（H：尻尾でアナル責め／横からの構図） | `explicit` / ROSETTA / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, nude male, erection, penis, precum, from side, side view, lying on back, on bed, legs raised, legs up, spread legs, tail insertion, demon tail, anal, lotion, kneeling, clothed female, cfnm, smirk, looking down at him, femdom` |
| `Rosetta_pegging.png` | ペニバン攻撃時／罠発動時／敗北シーン／調教ペニバンのカード画像（H：横からの構図） | `explicit` / ROSETTA / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, nude male, erection, penis, precum, from side, side view, lying on back, on bed, legs raised, legs up, spread legs, pegging, strap-on, waist harness, anal, penetration, kneeling, clothed female, cfnm, sweat, smirk, looking down at him, femdom` |
| `Rosetta_complete.png` | メス堕ち完成／敗北後シーン | `sensitive` / ROSETTA / `pov, from below, looking down at viewer, chin grab, smile, bedroom` |
| `Rosetta_convert.png` | メス奴隷への変換時（ロゼッタが首輪をつける側） | `sensitive` / ROSETTA / `pov, reaching towards viewer, holding leash, leash pulled toward viewer, from below, smirk, looking at viewer, bedroom` |
| `Rosetta_beg.png` | ロゼッタの命乞い演出（HPが尽きた時：膝をついて誘惑しながら命乞いをする） | `sensitive` / ROSETTA / `pov, kneeling, looking up at viewer, pleading expression, hands clasped, leaning forward, cleavage, teasing smile, half-closed eyes, bedroom, from above` |

### B. ロゼッタのカード効果 — 発動時
| ファイル | いつ表示されるか | 安全 / キャラ / シーンタグ |
|---|---|---|
| `Rosetta_oil.png` | 黒薔薇のオイル発動時／カード画像 | `sensitive` / ROSETTA / `pov, pouring oil, oil on hands, glossy skin, seductive smile, rose petals, looking at viewer` |
| `Rosetta_command.png` | 女王の命令発動時／カード画像 | `safe` / ROSETTA / `sitting, throne, pointing down, from below, looking at viewer, pov` |
| `Rosetta_room.png` | 黒薔薇の調教部屋（毎ターン）／カード画像 | `safe` / ROSETTA / `standing, dim room, black rose, incense, smoke, purple lighting, pink lighting, looking at viewer` |
| `Rosetta_final.png` | メス堕ち完成の儀発動時／カード画像 | `nsfw` / ROSETTA / `pov, waist harness, black leather, chin grab, triumphant smile, glowing, pink light, rose petals, from below` |

### C. 従者（エルザ／ヴィヴィアン／ミレーユ）・メス奴隷
| ファイル | いつ表示されるか | 安全 / キャラ / シーンタグ |
|---|---|---|
| `Elsa.png` | エルザ召喚時／イベント／カード画像 | `safe` / ELSA / `standing, bowing slightly, own hands together, looking at viewer, simple background, white background, full body` |
| `Elsa_nipple.png` | エルザの効果発動時（H：乳首責め） | `explicit` / ELSA / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, pov, topless male, nipples, lying on back, on bed, leaning over, nipple tweak, licking nipple, saliva, clothed female, cfnm, gentle smile, looking at viewer` |
| `Elsa_convert.png` | エルザによるメス奴隷への変換時 | `sensitive` / ELSA / `pov, reaching towards viewer, holding leash, leash pulled toward viewer, from below, gentle smile, looking at viewer, bedroom` |
| `Vivian.png` | ヴィヴィアン召喚時／イベント／カード画像 | `safe` / VIVIAN / `standing, holding clipboard, looking at viewer, simple background, white background, full body` |
| `Vivian_exam.png` | ヴィヴィアンの効果発動時（H：指で前立腺診察／横からの構図） | `explicit` / VIVIAN / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, nude male, erection, penis, precum, from side, side view, lying on back, examination table, legs raised, legs up, spread legs, anal fingering, fingering, gloved fingers, lotion, standing, clothed female, fully clothed, cfnm, serious, looking down at him, examination room` |
| `Vivian_convert.png` | ヴィヴィアンによるメス奴隷への変換時 | `sensitive` / VIVIAN / `pov, reaching towards viewer, holding leash, leash pulled toward viewer, from below, serious, looking at viewer, examination room` |
| `Mireille.png` | ミレーユ召喚時／イベント／カード画像（洗脳担当） | `safe` / MIREILLE / `standing, looking at viewer, hands together, simple background, white background, full body` |
| `Mireille_double.png` | ミレーユの効果発動時（H：背後から抱きしめて耳元で洗脳＋目隠し＋ニップルドーム＋アナルパール（太め）） | `explicit` / MIREILLE / `1boy, faceless male, androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, adult male, height difference, nude male, erection, penis, precum, from front, front view, sitting, on bed, leaning back, spread legs, knees up, hug from behind, girl behind boy, whispering, mouth near ear, blindfold, covered eyes, nipple stimulator, nipple suction, white nipple cups, cone-shaped nipple cups, pink accents, opaque white cups, anal beads, thick anal beads, large anal beads, beads string, pull ring, sex toy, clothed female, cfnm, soft smile` |
| `Mireille_convert.png` | ミレーユによるメス奴隷への変換時 | `sensitive` / MIREILLE / `pov, reaching towards viewer, holding blindfold, holding leash, leash pulled toward viewer, from below, soft smile, looking at viewer, bedroom` |
| `Rosetta_slave_drain.png` | メス奴隷のターン開始時（ロゼッタが精気を吸う） | `sensitive` / ROSETTA / `pov, from below, looking down at viewer, holding leash, hand on viewer's chin, glowing, pink light, magic circle, smile` |
| `Rosetta_mons_Slave.png` | メス奴隷カード画像／立ち絵①（主人公側の男性・中性的で小柄） | `sensitive` / SLAVE / `standing, looking at viewer, shy smile, simple background, white background, full body` |
| `Rosetta_mons_Slave_2.png` | メス奴隷 立ち絵② | `sensitive` / SLAVE / `sitting, hugging own legs, blush, looking up, simple background, white background, full body` |
| `Rosetta_mons_Slave_3.png` | メス奴隷 立ち絵③ | `sensitive` / SLAVE / `standing, hand on collar, looking to the side, simple background, white background, full body` |

## カード画像の扱い（専用のカード画像は作りません）
- **モンスターカード**：各キャラの立ち絵を使用 → 従者エルザ＝`Elsa.png`／調教医ヴィヴィアン＝`Vivian.png`／メス奴隷＝`Rosetta_mons_Slave.png`
- **魔法・罠カード**：そのシーンの画像を使用 → 黒薔薇のオイル＝`Rosetta_oil.png`／女王の命令＝`Rosetta_command.png`／黒薔薇の調教部屋＝`Rosetta_room.png`／メス堕ち完成の儀＝`Rosetta_final.png`／調教ペニバン＝`Rosetta_pegging.png`

## 描き分けの注意
- **首輪をつけられるのは主人公側（メス奴隷）だけ**。ロゼッタ・エルザ・ヴィヴィアンの画像には首輪を出さない（ネガティブに `collar, choker` を入れてあります）。ロゼッタは首輪・リードを**つける側**（`Rosetta_convert`／`Rosetta_slave_drain`）。
- **メス奴隷は成人の男性**：**中性的・小柄・華奢・筋肉質でない**（女装・首輪・ランジェリー）。ネガティブで `1girl`／`muscular`／`abs`／`broad shoulders`／ひげ／体毛を除外し、未成年を除外する語も入れてあります。
- **前提：主人公サイドが女性に挿入する描写は存在しません**（画像・テキストとも）。ネガティブに `vaginal` / `vaginal sex` / `cowgirl position` / `pussy` / `nude female` / `futanari` などを入れて、女性側が裸になる・挿入される絵を避けています。
- **H描写の画像**（`Rosetta_nipple`／`Rosetta_prostate`／`Rosetta_pegging`／`Elsa_nipple`／`Vivian_exam`／`Mireille_double`）：**責めるのは敵の女性（服を着たまま）、責められるのは被責め側の男性（裸・勃起）**。顔は描かない。安全タグは `explicit`。
  - 責める内容：ロゼッタ＝乳首責め（指と舌）／前立腺責め（**尻尾**）／ペニバン／**エルザ＝乳首責め**／**ヴィヴィアン＝指でアナル責め（前立腺診察）**／**ミレーユ＝目隠し＋ニップルドーム（白い円錐形）とアナルパール（太め）の同時責め＋耳元で洗脳**。
  - 肛門責めの場面（`Rosetta_prostate`／`Rosetta_pegging`／`Vivian_exam`）は、**被責め側の側面から見た構図**（`from side, side view`）。ペニスは勃起し、他と接触・融合しないよう指定。
  - **`Mireille_double`＝背後から抱きしめて耳元で洗脳**：ミレーユが被責め側の**背後**に座って抱きしめ（`hug from behind, girl behind boy`）、耳元で囁く（`whispering, mouth near ear`）。被責め側は目隠し・**ニップルドーム**（**白い不透明の円錐形のカップ＋ピンクのアクセント**を両乳首に被せて**吸引しながら舐め回す**。透明なドームや乳首クリップにならないよう、ネガティブに `clear dome, transparent dome, bubble, nipple clamps`）・**アナルパール（太め）**（引き輪をミレーユが持つ）。**正面から撮る構図**（`from front`）。ネガティブに `boy behind girl, man hugging from behind` を入れて、男女の役割が逆にならないようにしています。
  - **誰の動作か**を英語の文で明記（例：「her fingers are inside HIS ass」「only the small slim man is undressed」）。主語のない姿勢タグ（`legs up` 等）は女性側に付くことがあるため。
- **被責め側（主人公側の男性）は中性的・小柄・華奢・筋肉なし**：`androgynous, feminine, petite, short, slender, thin, skinny, delicate, narrow shoulders, narrow waist, thin arms, thin legs, smooth skin, no muscles, height difference`。ネガティブに `muscular, abs, pectorals, broad shoulders, thick arms, bara, big body, tall man, huge penis`。ロゼッタより小さく細く見えるよう、英語の文でも明記。
- **胸**：ロゼッタ・エルザ・ミレーユは `large breasts`（ネガティブに `small breasts, flat chest`）。
- **敵ごとに変換画像が別**：ロゼッタ＝`Rosetta_convert`／エルザ＝`Elsa_convert`／ヴィヴィアン＝`Vivian_convert`／ミレーユ＝`Mireille_convert`。
- 責められるのは主人公側のみ。ロゼッタ側が責められる場面の画像は作りません。
- 画面（`Rosetta_workflow.json`）で手動生成する時は、ネガティブ欄を `Rosetta_prompts.json` のその画像の `negative` に差し替えてください（ワークフロー初期値はロゼッタ側用。**メス奴隷の画像だけ**は男性を保つため別のネガティブです）。

## 表示の流れ（メモ）
- ロゼッタの**攻撃宣言時**：責めの種類に応じて A の nipple／prostate／pegging を表示。攻撃後に消去。
- **カード効果発動時**：B／C の該当画像を表示し、処理後に消去。
- **メス奴隷化**：`Rosetta_convert.png` を表示 → 変換後に消去。
