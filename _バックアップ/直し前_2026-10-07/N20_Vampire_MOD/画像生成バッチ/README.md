# N20 吸血鬼の館（Vampire）画像一括生成バッチ

N19（Twins）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5／seed_base 20260925）。
全51枚を、カードが参照するファイル名のまま `output\Vampire\` に保存する（ComfyUI側の `ComfyUI\output\Vampire\` にも同じ画像が残る）。登場人物は全員20歳以上。

## 使い方
1. **`gen_vampire_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動→51枚を順に生成。止めても再実行で続きから）。1枚約2分×51枚 ≒ 1時間40分
2. 撮り直し：`run_vampire.bat Vampire_atk_m3 --random --batch 4` → `output\Vampire\_candidates\` から選んで `run_vampire.bat --pick Vampire_atk_m3 2`
3. ゲームへ：`install_vampire.bat`（引数なしでゲーム本体の Picture\Vampire へコピー。本MODの画像だけを入れる）

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Vampire_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`。得意技の自慰でペニスには触れない）／魔法・罠5

## 崩れやすそうなもの（候補を出して選ぶ）
- ふたなりの挿入（`atk_m3` `atk_boss` `lose_*_m3` `lose_btl/inochi/onedari_boss`）：二人のペニスが融合していないか
- ピピの腕が羽（`e2` `atk_e2` `lose_*_e2` `magic_3`）：主人公に羽が付いていないか、逆さ吊りが崩れていないか
- 貞操帯（`atk_e3` `lose_*_e3` `onanie_e3`）：平たい小さな檻で勃起していないか
- 鏡に映らない（`lose_onani_m1` `lose_onedari_m2`）：ノクティアが鏡に映ってしまうことが多い。気になれば撮り直し
- 主人公の髪（紺）とリリアの髪（黒）が入れ替わっていないか
- プロンプトを直したら `python build_prompts.py`（ComfyUI同梱のpythonで可）で `vampire_prompts.json` を作り直す
