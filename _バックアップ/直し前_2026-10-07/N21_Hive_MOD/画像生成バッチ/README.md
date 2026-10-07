# N21 蜂の女王の巣（Hive）画像一括生成バッチ

N20（Vampire）と同じ仕組み・同じ設定（Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5／seed_base 20260926）。
全51枚を、カードが参照するファイル名のまま `output\Hive\` に保存する（ComfyUI側の `ComfyUI\output\Hive\` にも同じ画像が残る）。登場人物は全員20歳以上。

## 使い方
1. **`gen_hive_all.bat` をダブルクリック**（ComfyUIが起動していなければ起動→51枚を順に生成。止めても再実行で続きから）。1枚約20秒〜2分
2. 撮り直し：`run_hive.bat Hive_atk_m3 --random --batch 4` → `output\Hive\_candidates\` から選んで `run_hive.bat --pick Hive_atk_m3 2`
3. ゲームへ：`install_hive.bat`（引数なしでゲーム本体の Picture\Hive へコピー。本MODの画像だけを入れる）

## 51枚の内訳
立ち絵5（白背景→背景除去）／背景 `Hive_bg`／技CG7／敗北28／オナニー5（`onanie_master` `_e1` `_e2` `_e3` `_boss`。得意技の自慰でペニスには触れない）／魔法・罠5

## 崩れやすそうなもの（候補を出して選ぶ）
- ふたなりの挿入（`atk_m3` `lose_*_m3` `lose_btl/onedari_boss`）：二人のペニスが融合していないか
- 尿道の管（`atk_m1` `lose_*_m1` `atk_boss`）：針や注射器になっていないか（細い金色の管のはず）
- ワスプの4本の腕（`e2` `atk_e2` `lose_*_e2`）：主人公に腕や甲殻が付いていないか
- 乳首舐め（`atk_m2` `lose_btl_m2` `lose_onedari_m2` `lose_*_boss`）：男女が逆（女性の胸がはだけ、主人公が吸う）になっていないか
- オナニー：手がペニスに行っていないか
- プロンプトを直したら `python build_prompts.py` で `hive_prompts.json` を作り直す
