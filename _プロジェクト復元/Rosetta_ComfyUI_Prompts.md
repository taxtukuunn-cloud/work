# Rosetta_ComfyUI_Prompts.md（復元・抜粋）

> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版の日時：2026-09-23 の版）。
> 【復元メモ・一部のみ】元のパスは `Rosetta_ComfyUI_Prompts.md`。この会話では検索結果の抜粋しか見ていない。見えたのは 1〜5章と6章Aの表の一部だけ。 下の各抜粋は原文どおりで、抜粋と抜粋の間・前後は欠けている（順番も元の並びと違う可能性がある）。

---

## 抜粋1（取得：2026-09-23 01:07 UTC）

# ロゼッタMOD 画像制作シート（WAI-Anima / Anima系用）

保存先はすべて `Picture/Rosetta/`。全23枚。登場人物は全員成人。
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

### A.

---

## 抜粋2（取得：2026-09-23 01:07 UTC）

背景除去（立ち絵7枚）
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

### B.
