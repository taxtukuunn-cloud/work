# N30 忍びの隠れ里（Ninja）画像一括生成バッチ

N26（Kitsune）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5。LoRA は `Downloads\Lora用\lora_settings.json` があれば自動で使う）。
全51枚を、カードが参照するファイル名（`Ninja_atk_m1.png` など）のまま `output\Ninja\` に保存する。登場人物は全員20歳以上。

## 使い方
1. **`gen_ninja_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動し、準備を待ってから51枚を順に生成。1枚約20秒・全部で約20分。途中で止めても、もう一度実行すれば続きから）
2. 崩れた画像の撮り直し：`run_ninja.bat Ninja_atk_m3 --random --batch 4` → `output\Ninja\_candidates\` から選んで `run_ninja.bat --pick Ninja_atk_m3 2`
3. ゲームへ：`install_ninja.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`（`Picture\Ninja\` にコピー）

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Ninja_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 見た目
- 主人公：紺色の短髪・前髪で目が隠れた顔なし、小柄で華奢（150cm）・非筋肉質。場面の画像では裸。縄の場面は柔らかい紅い縄（痛みなし）。
- カゲロウ：黒のロング・高いポニーテール・紅い瞳・黒装束・首元に下げた口布
- ハヤブサ：灰の短髪・金の瞳・袖なしの薄灰の下忍装束・腰に紅い縄
- シグレ：紫のボブ・灰の瞳・袖の長い紫の装束・小さな香炉
- ツムギ：茶の三つ編み・緑の瞳・緑の薬師装束と白い前掛け・背に薬箱
- オボロ：白のロング・紅い瞳・濃灰の上忍装束・額当て（金具は無地）
- 責め手は男の娘（胸は平ら）。挿入の場面（m3・オボロの本番）だけ責め手の性器を出す。
- **分身の術の場面**（atk_m3・atk_boss・lose_*_m3・lose_btl_boss・lose_onani_boss・lose_inochi_boss・lose_onedari_boss）は同じ顔の忍びが2〜3人並ぶ。この場面だけネガティブの「twins・same face・3boys」を外してある。
- オナニーCGは責め手の得意技に合わせた自慰（ペニスには触れない）。責め手は奥で小さく見ているだけ。

## 崩れやすそうなもの（候補を出して選ぶ）
- 分身の場面：人数が合わない／分身の髪色が変わる／主人公が忍び装束を着てしまう
- 縄（胸縄）の形、木人（練習用の人形）に括る構図 `Ninja_atk_e1` `Ninja_lose_btl_e1`
- 尿道責め（細い管・影針）：`Ninja_atk_e3` `Ninja_atk_boss` `Ninja_lose_*_e3`
- 房中術（触れずに達する）`Ninja_atk_m2` `Ninja_lose_*_m2`：掌が股間に行ってしまう
- 額当てに文字や紋が入る（ネガティブに入れてある）

## プロンプトを直すとき
`build_prompts.py` を書き換えて実行 → `ninja_prompts.json` が作り直される。撮り直す画像は `output\Ninja\` から消すか `--random` を付ける（同じシードだとComfyUIが新しく保存しない）。
