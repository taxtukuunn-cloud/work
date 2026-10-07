# N18 ラミアの神殿（Lamia）画像一括生成バッチ

N16（アルラウネ）と同じ仕組み・同じ設定（Anima：waiANIMA_v10Base10＋qwen_3_06b_base＋qwen_image_vae、832×1216、er_sde・simple、36step、CFG4.5）。
全52枚を、カードが参照するファイル名（`Lamia_atk_m1.png` など）で `output\Lamia\` に保存する。登場人物は全員20歳以上。

## 使い方
1. **`gen_Lamia_all.bat` をダブルクリック**：ComfyUIが起動していなければ起動し、準備ができるのを待ってから52枚を生成（途中で止めても、もう一度実行すれば続きから）。1枚20秒前後。
2. 確認だけ：`run_lamia.bat --check`
3. 一部だけ：`run_lamia.bat Lamia_lose_btl`（名前がこれで始まるもの全部）
4. 崩れた画像の撮り直し：`run_lamia.bat Lamia_atk_m3 --random --batch 4` → `output\Lamia\_candidates\` を見て `run_lamia.bat --pick Lamia_atk_m3 3`
5. ゲームへ：`install_lamia.bat "C:\…\ゲームのフォルダ\Picture"`（`Picture\Lamia\` にコピー）

## 52枚の内訳
立ち絵5（白背景→背景除去）／背景1／マスター技3／モンスター技4／魔法・罠5／命乞い1／オナニー5（onanie_m・e1・e2・e3・boss）／敗北28。
（N18のカードはおねだりCGを使わないので、N16より1枚少ない）

## 描き分けのルール
- 主人公：**紺髪**・前髪で目が隠れた顔なし、身長150cmの小柄で華奢な青年。場面では常に裸（cfnm）。責め手より頭ひとつ以上小さい。
- 責め手は衣装を着たまま。髪色と鱗の色：シェスカ＝緑／ヴィペラ＝黄／コブラ＝黒／リングァ＝赤／ウロボラ＝白金の髪・白い鱗。
- 下半身は蛇（ネガティブに「人の脚」）。主人公側に鱗・尾が付かないようネガティブで除外。丸呑み・流血はネガティブで除外。
- 舌の責め：anilingus（アナル舐め）・nipple licking（乳首舐め）＋ long forked tongue。
- **ふたなりの場面（atk_m3・lose_*_m3・lose_btl_boss・lose_inochi_boss の7枚）**：側面構図で、責め手と主人公のペニスを別々に描く指定。崩れやすいので、真っ先に確認して `--random --batch 4` で選ぶ。
- 文字の出る小物は使わない（日誌は閉じた本、名札は木札）。
- `build_prompts.py` を直して実行すると `lamia_prompts.json` と `N18_Lamia_ComfyUI_Prompts.md` が作り直される。
