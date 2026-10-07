# N23 足の女王様（Heels）画像一括生成バッチ

N22（Prison）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）。
全52枚を、カードが参照するファイル名（`Heels_atk_m1.png` など）のまま `output\Heels\` に保存する。登場人物は全員20歳以上。

## 使い方
1. **`gen_heels_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動し、準備を待ってから52枚を順に生成。1枚約20秒・全部で約20分。途中で止めても、もう一度実行すれば続きから）
2. 崩れた画像の撮り直し：`run_heels.bat Heels_atk_m3 --random --batch 4` → `output\Heels\_candidates\` から選んで `run_heels.bat --pick Heels_atk_m3 2`
3. ゲームへ：`install_heels.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`（`Picture\Heels\` にコピー）

## 52枚の内訳
立ち絵5（白背景→背景除去）／女装娘カード `Heels_josou`（背景除去）／背景 `Heels_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 見た目
- 主人公：紺色の短髪・前髪で目が隠れた顔なし、小柄で華奢（150cm）・非筋肉質。**場面の画像では侍女のドレス姿**（黒い膝丈のドレス・白い襟とエプロン・黒いガーターストッキング・ストラップの靴）。責める所だけスカートをめくる／胸元をずらす。
- クラウディア：黒のロング・赤い瞳・黒いボンデージドレス・靴底の赤いピンヒール
- ミナ：金のボブ・緑の瞳・黒い侍女服・黒ストッキング
- ザラ：赤のショート・金の瞳・黒革の調教師服・手袋・乗馬鞭（指し示すだけ）
- リタ：茶のロング・茶の瞳・焦げ茶のロングの侍女服
- アウグスタ：白金の巻き髪・紫の瞳・紫と白金のドレス・王冠
- ペニバンはクラウディア技③・アウグスタの場面だけ。ほかはネガティブで除外。
- オナニーCGは責め手の得意技に合わせた自慰（ペニスには触れない）。責め手は奥で小さく見ているだけ。

## 崩れやすそうなもの（候補を出して選ぶ）
- 主人公と侍女（ミナ・リタ）の取り違え（服が似ているので髪色で見分ける。崩れたら `--random --batch 4`）
- `Heels_atk_m3` `Heels_lose_*_m3`（ペニバン＋ヒールで乳首）
- アウグスタの同時技（`atk_boss` `lose_btl/inochi/onedari_boss`：3人の女性＋主人公）
- 足の指・ヒールの形

## プロンプトを直すとき
`build_prompts.py` を書き換えて実行 → `heels_prompts.json` が作り直される。撮り直す画像は `output\Heels\` から消すか `--random` を付ける（同じシードだとComfyUIが新しく保存しない）。

## LoRA（本編の絵柄）で撮り直す（2026-09-26 準備）
- LoRA は `Downloads\Lora用\lora_settings.json`（sdduel_style-000006・強さ0.6）を `comfy_batch.py` が自動で読む。起動時に「LoRA: …」と表示される。外すなら `--no-lora`、強さを変えるなら `--lora-strength 0.5`。
- **主人公タグを直した**：`petite, short, androgynous, narrow shoulders` の組み合わせは幼く見える（N21で発生）ため、成人男性の体つき（`adult man, mature male, 25 years old, adult proportions, adam's apple` など）に変え、小柄さは「相手より頭ひとつ低い」で表すようにした。ネガティブに `childlike, child body, baby face, petite male, boy` などを追加。`otoko no ko, trap` も外した。直す前の版は `build_prompts_LoRA前.py`・`heels_prompts_LoRA前.json`。
- 手順
  1. **`test_heels_lora.bat`**：今の画像を `output\Heels_LoRA前\` にバックアップしてから、4枚（オナニー・足コキ・ペニバン・立ち絵）を候補2枚ずつ試し撮り → `output\Heels\_candidates\`（完成画像は上書きしない）。
  2. 主人公が成人に見えるか・体格が崩れていないかを確認。崩れる場合は強さ0.5で試す。
  3. **`gen_heels_lora_all.bat`**：52枚を撮り直して `output\Heels\` を上書き（強さを変えるなら `gen_heels_lora_all.bat --lora-strength 0.5`）。
  4. 全枚数を目で確認 → 崩れた分だけ `run_heels.bat <キー> --random --batch 4` → `--pick`。
- 元に戻すとき：`output\Heels_LoRA前\` の中身を `output\Heels\` に戻す。
