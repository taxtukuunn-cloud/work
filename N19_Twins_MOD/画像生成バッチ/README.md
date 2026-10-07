# N19 サキュバス双子の寝所（Twins）画像一括生成バッチ

N17（Scylla）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5／seed_base 20260924）。
全51枚を、カードが参照するファイル名のまま `output\Twins\` に保存する（ComfyUI側の `ComfyUI\output\Twins\` にも同じ画像が残る）。登場人物は全員20歳以上。

## 使い方
1. **`gen_twins_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動→51枚を順に生成。止めても再実行で続きから）。1枚約2分×51枚 ≒ 1時間40分
2. 撮り直し：`run_twins.bat Twins_atk_m3 --random --batch 4` → `output\Twins\_candidates\` から選んで `run_twins.bat --pick Twins_atk_m3 2`
3. ゲームへ：`install_twins.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Twins_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`）／魔法・罠5

## 崩れやすそうなもの（候補を出して選ぶ）
- 双子＋主人公の3人の場面（`atk_m1〜m3`、`lose_*_m1〜m3`、立ち絵 `master`）：二人が同じ髪色・同じ服になっていないか（姉＝桃のロング・黒い服・黒い翼／妹＝薄紫のツインテール・白い服・白い翼）
- ふたなり（`atk_m3` `lose_btl_m3` `lose_inochi_m3` `lose_onedari_m3` `lose_btl_boss` `lose_onedari_boss`）
- ピクシの二股の尻尾（`atk_e3` `lose_btl_e3` `lose_onedari_e3`）
