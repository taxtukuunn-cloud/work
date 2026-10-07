# N25 オークションハウス（Auction）画像一括生成バッチ

N23（Heels）と同じ仕組み・同じ設定（comfy_batch.py は 2026-09-25 に絵柄LoRA読み込みを追加した版。元は comfy_batch_LoRA前.py）（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）。
全52枚を、カードが参照するファイル名（`Auction_atk_m1.png` など）のまま `output\Auction\` に保存する。登場人物は全員20歳以上。

## 使い方
0. **まず `test_auction.bat`**（立ち絵・技CG・敗北の3枚を候補2枚ずつ生成 → `output\Auction\_candidates\` を見て、絵柄LoRA（sdduel_style 0.6。`Downloads\Lora用\lora_settings.json` で全MOD共通）で主人公の体格が崩れないか・責め手と主人公が入れ替わっていないかを確認。崩れるなら `run_auction.bat <キー> --lora-strength 0.5` や `--no-lora` で比べる）
1. **`gen_auction_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動し、準備を待ってから52枚を順に生成。1枚約20秒・全部で約20分。途中で止めても、もう一度実行すれば続きから）
2. 崩れた画像の撮り直し：`run_auction.bat Auction_atk_m3 --random --batch 4` → `output\Auction\_candidates\` から選んで `run_auction.bat --pick Auction_atk_m3 2`
3. ゲームへ：`install_auction.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`（`Picture\Auction\` にコピー）

## 52枚の内訳
立ち絵5（白背景→背景除去）／女装娘カード `Auction_josou`（背景除去）／背景 `Auction_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 見た目
- 主人公：紺色の短髪・前髪で目が隠れた顔なし、小柄で華奢（150cm）・非筋肉質。**場面の画像では出品衣装姿**（薄い白のシフォンドレス・白いガーターストッキング・赤いリボンのチョーカー・手首の金鎖）。責める所だけ胸元をずらす／スカートをめくる。
- 責め手は全員男の娘（cmnm・2boys・胸は平ら・服を着たまま）。自分のペニスで貫くのはルシアン技③とセラフ技②の場面だけ（`pen=True`）。ほかはネガティブで除外。
- ルシアン：金の長髪一つ結び・紫の瞳・黒い燕尾服・半仮面・木槌
- ユリ：白の短髪・赤い瞳・鑑定士のベスト・片眼鏡・白手袋
- カナタ：赤のウルフカット・金の瞳・黒い作業ベスト
- ミコト：黒のボブ・赤い瞳・案内係のベスト・ネクタイ・ショートパンツ
- セラフ：薄紫の長髪・金の瞳・白い貴族服と外套
- オナニーCGは責め手の得意技に合わせた自慰（ペニスには触れない）。責め手は奥で小さく見ているだけ。

## 崩れやすそうなもの（候補を出して選ぶ）
- 主人公と責め手の取り違え（両方男の娘なので髪色と衣装で見分ける。崩れたら `--random --batch 4`）
- `Auction_atk_e2` `Auction_lose_*_e2`（尿道ブジー＋後ろの器具の同時）
- `Auction_atk_m3` `Auction_lose_*_m3` `Auction_lose_*_boss`（責め手自身の挿入。ペニスが融合しやすい→側面構図）
- 半仮面（ルシアン）の形、木槌

## プロンプトを直すとき
`build_prompts.py` を書き換えて実行 → `auction_prompts.json` が作り直される。撮り直す画像は `output\Auction\` から消すか `--random` を付ける（同じシードだとComfyUIが新しく保存しない）。
