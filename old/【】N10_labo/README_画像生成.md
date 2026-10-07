# N10 開発ラボ 画像生成ツール

カード（`N10_Lab_MOD.zip`）が使う画像49枚を、ComfyUI で一括生成してゲームに入れるツールです。登場人物は全員20歳以上。個人利用のみ。

## 1. 準備（最初の1回）
1. ComfyUI に WAI-Anima の3ファイルを置く（ロゼッタMODと同じ）
   - `models\diffusion_models\waiANIMA_v10Base10.safetensors`（名前が違っても、生成前に実在するモデルへ自動で合わせます）
   - `models\text_encoders\qwen_3_06b_base.safetensors`
   - `models\vae\qwen_image_vae.safetensors`
2. 背景除去ノード「Inspyrenet Rembg」を ComfyUI-Manager から入れる（立ち絵5枚用。入れない場合は `--no-rembg`）
3. 書き換えは不要。batが ComfyUI の Python を自動で探します。見つからないときだけ、ComfyUI のフォルダを画面にドラッグして Enter（場所は `tools\comfy_path.txt` に保存され、次回から聞かれません）

## 2. 生成
ComfyUI を**通常の起動bat**で起動してから：
| やりたいこと | コマンド |
|---|---|
| 全49枚 | `gen_Lab_all.bat`（または `run_lab.bat all`） |
| 1枚だけ撮り直す（候補4枚） | `run_lab.bat Lab_atk_m2 --random --batch 4` |
| まとめて（名前の一部） | `run_lab.bat lose` ／ `run_lab.bat _e2` ／ `run_lab.bat atk` |
| 一覧を見る | `run_lab.bat --list` |
| モデル名を確認 | `run_lab.bat --list-models` |

- 候補は `tools\candidates\<キー名>\` に保存されます。同じ画像を撮り直すと前の候補は消えます（残すなら `--keep`）。
- シードはキャラ単位で固定（同じキャラは同じシード）。見た目を揃えるためです。変えたいときだけ `--random` か `--seed 番号`。

## 3. ゲームに入れる
`install_lab.bat "D:\ゲーム\Picture"`
- Saveフォルダと同じ階層の `Picture` を指定すると、`Picture\Lab\` に正しい名前（`Lab_master.png` など）でコピーします。
- 気に入った候補がある場合は、`tools\picks\` に `キー名.png`（例：`Lab_atk_m2.png`）の名前で置くと、そちらが優先されます。無ければ一番新しい候補が入ります（立ち絵は背景除去版）。
- 足りない画像があると一覧で表示します。**画像が1枚でも無いと、その場面でゲームが止まる可能性があります。**

## 4. 自分のワークフローを使う
いつも使っているワークフローがあれば、ComfyUI の「Save (API)」で書き出して `--workflow 自分の.json` を付けます。ツールは KSampler につながったプロンプト・潜在画像・保存ノードを探して書き換えるので、LoRA などを足したワークフローでも使えます。

## 5. 画像のルール（プロンプトに入れてあるもの）
- 主人公：黒髪・前髪で目が隠れた顔なし・二十代の小柄で華奢な成人男性。場面では常に裸。責め手の髪色（銀・薄灰・濃紺・白）と被らない。
- 責め手：常に服を着る（白衣）。シオリ＝銀髪ショート・赤目・ゴーグル／ミナセ＝薄灰ボブ・タブレット／クロエ＝濃紺ショート・黒手袋・革ベルト／ハク＝白髪ポニーテール・クリップボード／LX-01＝人型でない白い試作機・複数アーム・赤いレンズ。
- 拡張機はクスコ型、アナル責めは側面構図。数字や文字の出る小物（札・タグの番号・画面の数字）は描かない（ネガティブに `text, letters, numbers`）。
- LX-01の場面は人間を主人公1人だけにし、女性や人型ロボットが出ないようにしている。

## 6. うまくいかないとき
| 症状 | 対処 |
|---|---|
| `Python was not found` | ComfyUI の Python が見つかっていない → `tools\comfy_path.txt` を消して、もう一度 bat を実行し、ComfyUI のフォルダをドラッグ |
| ComfyUI に接続できません | ComfyUI を起動してから実行。ポートが違う場合は `--server http://127.0.0.1:ポート` |
| `missing_node_type InspyrenetRembg` | ノードを入れる、または `--no-rembg` |
| `qwen_image`／`er_sde` のエラー | ComfyUI を更新（`update_comfyui.bat`） |
| モデル名のエラー | 通常は自動で合わせます。合わないときは `--list-models` で名前を見て、`Lab_workflow_api.json` の名前を書き換える |
| out of memory | `--batch 1`（既定） |
| 責める側と責められる側が逆・体が混ざる | `--random --batch 4` で候補を出して選ぶ |

## 7. ファイル
- `tools\run_lab_batch.py`：本体（標準ライブラリのみ）
- `tools\Lab_prompts.json`：49枚のプロンプト（`positive` を直せば絵が変わる）
- `tools\build_prompts.py`：プロンプトを組み立て直すスクリプト（キャラの見た目や部屋をまとめて変えたいとき）
- `tools\Lab_workflow_api.json`：標準のワークフロー
- `Lab_ComfyUI_Prompts.md`：読む用の一覧
