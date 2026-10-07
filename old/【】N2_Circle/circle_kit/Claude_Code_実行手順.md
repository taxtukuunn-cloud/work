# N2 Circle 画像生成キット：実行手順（Claude Code／手動どちらでも）

## 中身
- `Circle_prompts.json` … 52枚ぶんのプロンプト（ファイル名・安全タグ・シード群・背景除去の有無）
- `run_circle_batch.py` … ComfyUI の API に直接投げる実行スクリプト（Python標準ライブラリのみ）
- `run_circle.bat` … Windows 用の起動バッチ（ComfyUI 同梱の python を使う）
- `N2_Circle_画像制作シート_改訂版.md` … 確認用の一覧

## 準備（最初の1回）
1. このフォルダを ComfyUI のフォルダ（`python_embeded` がある階層）の中に `circle_kit` などの名前で置く。
   - 例：`ComfyUI_windows_portable\circle_kit\run_circle.bat`
2. すでに動いている Rosetta 用の **API形式** ワークフロー `Rosetta_workflow_api.json` を、このフォルダにコピーする。
   - ひな形として使い、プロンプト・シード・サイズ・保存名だけを差し替える。モデル・サンプラー・ステップ数はそのまま引き継ぐ。
   - 画面用の `Rosetta_workflow.json` は使えない（エラーで知らせる）。無い場合は ComfyUI の画面で「Save (API Format)」で書き出す。
3. ComfyUI を通常の bat から起動しておく（`http://127.0.0.1:8188`）。

## 実行
```
run_circle.bat --list                         一覧
run_circle.bat Circle_e3                      1枚だけ試す（まずこれで動作確認）
run_circle.bat                                52枚すべて
run_circle.bat atk --batch 3 --random         攻撃CGを候補3枚ずつ
run_circle.bat lose_btl_m1 --seed 12345       シードを指定して作り直す
run_circle.bat --game "D:\Games\SuccubusDuel"   できた1枚目をゲームの Picture\Circle に置く
```
- 結果は `candidates\<ファイル名>\<ファイル名>_s<シード>.png`。良いものを選んで `ゲームフォルダ\Picture\Circle\<ファイル名>.png` にリネームして置く。
- `--game` を付けると1枚目を自動で置く。既にある画像は `--overwrite` を付けない限り上書きしない。
- 同じキャラの画像は同じシードになる（見た目をそろえるため）。気に入らない1枚だけ `--random` か `--seed` で作り直す。

## Claude Code に頼むときの指示例
> `circle_kit` フォルダで `run_circle.bat Circle_e3` を実行して、`candidates` にできた画像を確認して。問題なければ `run_circle.bat --game "<ゲームのパス>"` で全52枚を作って。途中でエラーが出たら内容を教えて。

## よくあるエラー
| 症状 | 対処 |
|---|---|
| `ワークフローがありません` | `Rosetta_workflow_api.json` をこのフォルダに置く、または `--workflow パス` を指定 |
| `画面用のワークフローです` | ComfyUI で「Save (API Format)」した JSON を使う |
| `KSampler が見つかりません` | ひな形のワークフローが別物。Rosetta の API 形式を使う |
| 接続できない | ComfyUI が起動しているか、`--server` の URL を確認 |
| `missing_node_type InspyrenetRembg` | `--no-rembg`（立ち絵が白背景のままになる） |
| `out of memory` | ひな形の設定で動くはずだが、出る場合は ComfyUI を再起動 |
| 責める側と責められる側が逆・融合する | その1枚だけ `--random --batch 3` で候補を増やして選ぶ |

## 配置後の確認
ゲームで N2 のバトルを開始し、カードの絵・攻撃時の画像・敗北後の画像が出るかを見る。出ない画像があれば、`Picture\Circle\` の中のファイル名がシートの名前と一致しているか確認する。
