# N26 妖狐（Kitsune）画像一括生成バッチ

N23（Heels）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）。
全51枚を、カードが参照するファイル名（`Kitsune_atk_m1.png` など）のまま `output\Kitsune\` に保存する。登場人物は全員20歳以上。

## 使い方
1. **`gen_kitsune_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動し、準備を待ってから51枚を順に生成。1枚約20秒・全部で約20分。途中で止めても、もう一度実行すれば続きから）
2. 崩れた画像の撮り直し：`run_kitsune.bat Kitsune_atk_m3 --random --batch 4` → `output\Kitsune\_candidates\` から選んで `run_kitsune.bat --pick Kitsune_atk_m3 2`
3. ゲームへ：`install_kitsune.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`（`Picture\Kitsune\` にコピー）

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Kitsune_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 見た目
- 主人公：紺色の短髪・前髪で目が隠れた顔なし、小柄で華奢（150cm）・非筋肉質。場面の画像では裸（狐耳・尾なし）。
- ハクエン：金のロング・金の狐耳・九本の金の尾・紅い瞳・白と紅の狩衣
- クダ：灰の短髪・小さな狐耳・首に巻けるほど長く細い灰の尾・金の瞳・白装束
- シラユキ：白のロング・白い狐耳と尾・紫の瞳・紅白の巫女装束
- アカネ：赤のショート・赤い狐耳と尾・金の瞳・丈の短い赤い着物・素足
- ギンカ：銀のロング・銀の狐耳と尾・金の瞳・白無垢と綿帽子
- 責め手は男の娘（胸は平ら）。挿入はハクエン技③（m3）とギンカの本番の場面だけ責め手の性器を出す。ほかはネガティブで除外。
- オナニーCGは責め手の得意技に合わせた自慰（ペニスには触れない）。責め手は奥で小さく見ているだけ。

## 崩れやすそうなもの（候補を出して選ぶ）
- 主人公に狐耳・尾が生える／責め手が裸になる（ネガティブに入れてあるが崩れたら `--random --batch 4`）
- 九本の尾（本数が合わない・触手に見える）：`Kitsune_atk_m2` `Kitsune_lose_*_m2`
- 尿道責め（`Kitsune_atk_e1` `Kitsune_lose_*_e1`）：光る細い尾の先が描かれないことがある
- 狐玉（アナルパール）の珠の大きさ・数
- 淫紋（下腹部の狐の紋）が服や背中に付く

## プロンプトを直すとき
`build_prompts.py` を書き換えて実行 → `kitsune_prompts.json` が作り直される。撮り直す画像は `output\Kitsune\` から消すか `--random` を付ける（同じシードだとComfyUIが新しく保存しない）。

## LoRA（本編の絵柄）について（2026-09-26 追記）
- `comfy_batch.py` は `Downloads\Lora用\lora_settings.json` を読み、`enabled: true` なら `sdduel_style-000006`（強さ0.6）を自動で入れ、プロンプト先頭に `sdduel style` を付ける（実行時に「LoRA: …」と表示）。
- 外す：`run_kitsune.bat Kitsune_atk_m2 --no-lora`／強さを変える：`run_kitsune.bat Kitsune_atk_m2 --lora-strength 0.5`
- **手順**：1. `test_kitsune.bat`（立ち絵・技CG・敗北CG・オナニーCGの4枚を試し撮りして `output\Kitsune_sheet.jpg` にまとめる）→ 主人公の体格（小柄・非筋肉質・紺髪）と狐の見た目（男の娘・胸は平ら・耳と尾）を確認 → 崩れるなら強さ0.5で撮り直す。2. 問題なければ `gen_kitsune_all.bat`（残り47枚。生成済みは飛ばす）。3. `sheet_kitsune.bat` で全51枚の一覧を作って確認（`sheet_kitsune.bat Kitsune_lose` で敗北CGだけ）。4. 崩れた分を `run_kitsune.bat <キー> --random --batch 3` → `--pick`。5. `install_kitsune.bat "<ゲーム>\Picture"`。
- 撮り直すと同名の画像は上書きされる。残したい画像は先にコピーしておく。
