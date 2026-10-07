# N23 足の女王様（Heels）ComfyUI 画像（全52枚）

> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版の日時：2026-09-24、画像生成後に project_write した版）。本文は会話内の全文どおり。プロンプトの全文は PC の `Downloads\MOD\N23_Heels_MOD\画像生成バッチ\build_prompts.py`（最終版）にある。

作成：2026-09-24。登場人物は全員20歳以上。個人利用のみ。

## 状態
- **52枚すべて生成済み**：ユーザーのPC `Downloads\MOD\N23_Heels_MOD\画像生成バッチ\output\Heels\`（カードが参照する名前のまま）。候補は `_candidates\`。
- ゲームへはまだ入れていない：`install_heels.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"`。

## バッチ（N22と同じ方式・設定：Anima 3ローダー／832×1216／er_sde・simple／36step／CFG4.5）
- `gen_heels_all.bat`（全52枚・続きから）、`run_heels.bat <キー> --random --batch 4`、`--pick <キー> <番号>`、`install_heels.bat`
- `fix_heels.bat`（20枚を3候補ずつ撮り直し）、`pick_heels.bat`・`pick2_heels.bat`（採用した候補を反映）
- プロンプトは `build_prompts.py` → `heels_prompts.json`

## 見た目の決まり
- 主人公：紺の短髪・前髪で目が隠れる顔なし・150cm・非筋肉質。**場面では侍女のドレス姿**（黒い膝丈ドレス・白い襟とエプロン・黒いガーターストッキング）。責める所だけめくる・ずらす。
- クラウディア：黒のストレートロング・**眉の上で切りそろえた前髪で赤い両目を見せる**・黒ラテックスのボンデージドレスに**赤いコルセットベルト**・黒のロンググローブ・赤い靴底のピンヒール
- ミナ：金のボブ・緑の瞳・黒い侍女服・黒ストッキング／ザラ：赤のショート・横に流した前髪・金の瞳・黒革のボディスーツ・乗馬鞭／リタ：茶のロング・焦げ茶のロングの侍女服／アウグスタ：白金の巻き髪・紫のドレス・王冠
- オナニーCGは得意技の自慰（ペニスに触れない）、責め手は奥で小さく見ているだけ。

## 生成で分かったこと（次のMODにも効く）
- 主人公の `hair over eyes` と侍女服のタグが責め手に移りやすい（クラウディアの目が前髪で隠れる・クラウディアやザラがエプロンを着ける・主人公が画面から消える）。
- 対策（効いた）：プロンプトを「THE WOMAN: …」「THE MAN (smaller, clearly visible): …」に分け、先頭に `1girl, 1boy, duo, two people`。責め手に目が見える前髪（blunt bangs above eyebrows／side-swept bangs）と服の差し色（赤いコルセット）を入れ、侍女服でない責め手のネガティブに `apron on the woman, maid headdress on the woman, hair over eyes on the woman, solo`。ポジティブに「no apron」と書くのは逆効果になりうるので書かない。
- 役が入れ替わる構図（机に座る人と立つ人など）は、誰がどこにいるかを文で書く（「赤髪の女が机の奥に座り、机の前に紺髪の男が立つ」）。
- 立ち絵 `Heels_master` は修正前のプロンプト（赤いコルセットなし）。気になれば `run_heels.bat Heels_master --random --batch 4` で撮り直す。
