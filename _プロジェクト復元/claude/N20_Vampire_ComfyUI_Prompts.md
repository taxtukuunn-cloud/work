# N20 吸血鬼の館（Vampire）画像生成メモ（2026-09-24）

> 【復元メモ】2026-09-24 にプロジェクト消失のため、この会話で書いた版から復元。プロンプトの全文はPCの `Downloads\MOD\N20_Vampire_MOD\画像生成バッチ\build_prompts.py`。

- **51枚すべて生成・目視確認済み**。完成画像はユーザーのPCの `Downloads\MOD\N20_Vampire_MOD\Picture\Vampire\`（51枚）。ゲームへは `画像生成バッチ\install_vampire.bat`（引数なしでゲーム本体の `Picture\Vampire` にコピー）。**ゲームへのコピーはまだ**。
- バッチ：`Downloads\MOD\N20_Vampire_MOD\画像生成バッチ\`（N19 Twins と同じ単独バッチ方式。Anima 3ローダー・832×1216・er_sde・simple・36step・CFG4.5・seed_base 20260925）。`gen_vampire_all.bat`（全枚数）／`run_vampire.bat <キー> --random --batch 4`→`--pick`／`retake_vampire.bat`（今回の撮り直し11枚分）。プロンプトは `build_prompts.py`（直したら実行して `vampire_prompts.json` を作り直す）。
- 1枚約18秒（51枚で約16分）。

## キャラのタグ（要点）
ノクティア＝銀の長髪・紅い瞳・牙・黒と赤のゴシックドレス／リリア＝黒ボブ・吸血鬼メイド服／ピピ＝紫ショート・紫のコウモリの翼・黒いチューブトップとショートパンツ／セレス＝赤いロング・黒い喪服とヴェール・黒タイツ・銀の鍵／ヴァレンシア＝白金の長髪・真紅のドレスとマント。主人公は紺髪・顔なし・150cm・非筋肉質（共通タグ）。牙跡は「two tiny pink fang marks, no blood」、ネガティブに blood・wound。

## 1回目で崩れた11枚と対策（候補3枚から選定済み）
- **男女の逆転（女性の胸がはだけ、主人公が女性の胸を吸う）**：乳首舐めの場面（atk_m2・lose_btl_m2・atk_boss・lose_btl_boss・lose_inochi_boss）。対策＝場面文を「he lies on his back… she bends down and licks the nipple on his flat male chest」にし、`cover`（her dress fully covers her chest and legs）＋ネガティブ（exposed breasts, breasts out, man sucking breast, woman nude from the waist down）。巨乳タグのキャラで起きやすい。
- **ピピ（腕が翼）が主人公と融合・逆さ吊りが崩れる・ピピにペニス**：atk_e2・lose_btl_e2・lose_onedari_e2。対策＝逆さ吊りをやめ「背後から抱きしめて翼の先で乳首」に。ネガティブに purple skin/purple hair on the man。
- **オナニーで手がペニスに**：lose_onani_m1・lose_onani_m3。対策＝「右手は口元で指を咥える、左手は胸、両手とも胸より上、ペニスは触れずに立っているだけ」と明記。
- **女性の下半身が裸**：lose_onedari_m3 → cover を付けて撮り直し。
- 選定：atk_boss c1／atk_e2 c2／atk_m2 c2／lose_btl_boss c3／lose_btl_e2 c1／lose_btl_m2 c2／lose_inochi_boss c1／lose_onani_m1 c2／lose_onani_m3 c3／lose_onedari_e2 c2／lose_onedari_m3 c1。

## 気になるが採用したもの
- ピピの立ち絵は「腕が翼」ではなく腕＋背中の翼になった（キャラ設定と少し違う）。
- セレスは修道女風のヴェール姿。onani_e3 では髪が短く描かれた。
- 鏡に映らない演出（lose_onedari_m2）はノクティアが鏡に映っている。
- 気になる時は `run_vampire.bat Vampire_<キー> --random --batch 4` で撮り直し。
