# N22 女看守の監獄（Prison）画像一括生成バッチ

N17（Scylla）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）。
全51枚を、カードが参照するファイル名（`Prison_atk_m1.png` など）のまま `output\Prison\` に保存する（ComfyUI の `output\Prison\` にも同じ名前で残る）。登場人物は全員20歳以上。

## 使い方
1. **`gen_prison_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動し、準備を待ってから51枚を順に生成。途中で止めても、もう一度実行すれば続きから）
2. 崩れた画像の撮り直し：`run_prison.bat Prison_atk_m3 --random --batch 4` → `output\Prison\_candidates\` から選んで `run_prison.bat --pick Prison_atk_m3 2`
3. ゲームへ：`install_prison.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`（`Picture\Prison\` にコピー）

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Prison_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 見た目
- 主人公：紺色の短髪・前髪で目が隠れた顔なし、小柄（150cm。プロンプトでは「相手より頭ひとつ低い成人男性」）・非筋肉質、裸に平たい金属の貞操帯（檻の中は勃起なし）。ドーラの尿道検査の場面だけ貞操帯なし。
- イザベル：黒髪のまとめ髪・灰の瞳・黒い看守長の制服と制帽・白手袋・鍵束（懲罰の場面だけ制服の上からペニバン）
- ケイ：茶のショート・茶の瞳・灰色の看守の制服・手帳
- ドーラ：金のシニヨン・緑の瞳・白衣・赤い腕章・黒のゴム手袋
- ヴィオラ：紫のウェーブロング・紫の瞳・濃紫のスーツ・膝までの黒いブーツ
- マグダレーナ：灰の長髪・黒の瞳・深緑の軍服風の制服・黒い外套・黒革の手袋
- オナニーCGは責め手の得意技に合わせた自慰（ペニスには触れない）。責め手は奥で小さく見ているだけ。

## 崩れやすそうなもの（候補を出して選ぶ）
- `Prison_atk_m3` と懲罰の敗北4枚（ペニバン＋尿道ブジー）
- 貞操帯（勃起してしまう・形が崩れる）
- `Prison_atk_e2` `Prison_lose_btl_e2`（尿道とアナルの同時）

## プロンプトを直すとき
`build_prompts.py` を書き換えて実行 → `prison_prompts.json` が作り直される。撮り直す画像は `output\Prison\` から消すか `--random` を付ける（同じシードだとComfyUIが新しく保存しない）。

## 2026-09-26 見直し（成人の体つき修正）
- N21 で主人公が幼く見えた対策を N22 にも入れた（`成人の体つき修正_2026-09-26.txt`）。直す前の版は `build_prompts_旧.py`・`prison_prompts_旧.json`。
- `comfy_batch.py` は本編絵柄LoRA（`Downloads\Lora用\lora_settings.json`）対応版。外すときは `--no-lora`、弱めるときは `--lora-strength 0.5`。
- 撮り直しは **`gen_prison_成人修正.bat`**（前回の51枚は `output\Prison_旧_2026-09-24` に残す）。
