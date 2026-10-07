# N27 騎士団（Knight）画像一括生成バッチ

N20（Vampire）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）。
全51枚を、カードが参照するファイル名のまま `output\Knight\` に保存する。登場人物は全員20歳以上（責め手は男の娘の騎士）。

## 使い方
1. **`gen_knight_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動→51枚を順に生成。止めても再実行で続きから）
2. 撮り直し：`run_knight.bat Knight_atk_m3 --random --batch 4` → `output\Knight\_candidates\` から選んで `run_knight.bat --pick Knight_atk_m3 2`
3. ゲームへ：`install_knight.bat`（引数なしでゲーム本体の Picture\Knight へコピー）
4. プロンプトを直したら `python build_prompts.py` で `knight_prompts.json` を作り直す

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Knight_bg`／技CG7／敗北28／オナニー5（得意技の自慰でペニスには触れない）／魔法・罠5

## 崩れやすそうなもの（候補を出して選ぶ）
- 男の娘の責め手が「責められる側」に描かれる／裸にされる（`2boys`＋`cmnm`。責め手は鎧のまま、主人公は紺髪で裸）
- 挿入（`atk_m3` `lose_*_m3` `lose_inochi_boss`）：二人のペニスが融合していないか。尿道の珠つなぎ（`urethral insertion`）
- 貞操帯（`atk_e3` `lose_*_e3` `onanie_e3`）：平たい小さな錠で勃起していないか
- 光の縄（`atk_e2` `lose_*_e2`）：エルシーが主人公に触れていないか
- 主人公の髪（紺）と責め手の髪（金・茶・緑・赤・白）が入れ替わっていないか

## 2026-09-26 見直し
- `comfy_batch.py` は別の作業で本編絵柄LoRA（`sdduel_style-000006`・強さ0.6・`Downloads\Lora用\lora_settings.json`）に対応済み。外すときは `--no-lora`。
- プロンプトを見直した：責め手に `trap`・`both eyes clearly visible`、場面のネガティブに `3boys`・`navy hair on the knight`・`the knight undressed`・`knight without armor` を追加。挿入の場面は `two separate penises`。オナニーCGは `2boys, solo focus on the small navy-haired man`。立ち絵・魔法は `solo, 1boy`。
- 敗北28枚の場所・小道具はシナリオ本文に合わせて確認済み（尋問室・地下牢・武具庫・稽古場・書庫・見張り台・城壁・礼拝堂・叙任の間・執務室・寝室・衛兵詰所）。
- 撮り直しの目安：まず `run_knight.bat Knight_atk_m2` の1枚で、主人公の体格（小柄・非筋肉質）がLoRAで崩れないか確認。崩れたら `--lora-strength 0.5`。
