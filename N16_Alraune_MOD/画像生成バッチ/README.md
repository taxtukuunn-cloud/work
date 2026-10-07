# N16 アルラウネの温室（Alraune）画像一括生成バッチ

N15（社員寮）と同じ仕組み・同じ設定（Anima：waiANIMA_v10Base10＋qwen_3_06b_base＋qwen_image_vae、832×1216、er_sde・simple、36step、CFG4.5）。
全53枚を、カードが参照するファイル名（`Alraune_atk_m1.png` など）で `output\Alraune\` に保存する（ComfyUI側の `ComfyUI\output\Alraune\` にも番号付きで残る）。登場人物は全員20歳以上。

## 使い方
1. **`gen_Alraune_all.bat` をダブルクリック**：ComfyUIが起動していなければ起動し、準備ができるのを待ってから53枚を生成（途中で止めても、もう一度実行すれば続きから）。
2. 確認だけ：`run_alraune.bat --check`
3. 一部だけ：`run_alraune.bat Alraune_lose_btl`（名前がこれで始まるもの全部）
4. 崩れた画像の撮り直し：`run_alraune.bat Alraune_atk_e3 --random --batch 4` → `output\Alraune\_candidates\` を見て `run_alraune.bat --pick Alraune_atk_e3 3`
5. ゲームへ：`install_alraune.bat "C:\…\ゲームのフォルダ\Picture"`（`Picture\Alraune\` にコピー）

## 53枚の内訳
立ち絵5（白背景→背景除去）／背景1／マスター技3／モンスター技4／魔法・罠5／命乞い・おねだり2／オナニー5（onanie_m・e1・e2・e3・boss）／敗北28。

## 描き分けのルール
- 主人公：**紺髪**・前髪で目が隠れた顔なし、身長150cmの小柄で華奢な青年。場面では常に裸（cfnm）。責め手より頭ひとつ以上小さい。
- 責め手は服（葉・花弁・樹皮のドレス、エプロン）を着たまま。髪色：フローラ＝緑／アイビー＝茶／ポレン＝黄／ネペンテ＝赤紫／ユグ＝白。
- 蔦・根は責め手の体から伸びているものとして描く。器具（ディルド等）は出さない（ネガティブで除外）。
- 文字の出る小物は使わない（作業日誌は blank page）。
- `build_prompts.py` を直して実行すると `alraune_prompts.json` と `N16_Alraune_ComfyUI_Prompts.md` が作り直される。
