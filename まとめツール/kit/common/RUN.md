# 担当ごとの手順（N106〜N157）
成人向け（M男向け）カードゲーム「サキュバスデュエル」の個人用MOD。登場人物は全員20歳以上の成人。個人利用のみ。
依頼文に「役割」と「MOD（番号・コード）」が書いてある。`K=/home/claude/work/kit106`、`M=$K/mods/<コード>`。途中で止めず最後までやり、報告は短く（本文は貼らない）。

## 役割 setup（骨組み）
`$K/common/SETUP_TASK.md` を最初から最後まで（末尾の補足も）読み、設計メモ `$K/ref/design/N<番号>_<コード>.md` から `$M/cfg.py` と `$M/brief.md` を作る。cfg の sys.path は `$K/common`、outdir は `N<番号>_<コード>_MOD`。完成例 `$K/mods/Genji/cfg.py`（stack と mstack の書き分け）も見る。補足の「通し確認」まで必ず行う。報告：通し確認の可否と、決めたカード効果の要点を5行以内。

## 役割 scenA（敗北シナリオ btl＋onani の14本）／scenB（inochi＋onedari の14本）
`$K/common/WRITER_TASK.md` を読み、その指示どおりに書く。scenA は btl_ と onani_ × m1 m2 m3 e1 e2 e3 boss、scenB は inochi_ と onedari_ × 同じ7つ。保存先 `$M/scen/<経路>_<key>.txt`。14本すべて check4000.py がOKになるまで直す。調子の見本が要る時は `$K/mods/Genji/scen/btl_m2.txt` を読んでよい（内容はまねない）。報告：check の結果の行だけ。

## 役割 lines（カードのセリフ5本）
`$K/common/lines_spec.md` を読み、`$M/lines/m.json・e1.json・e2.json・e3.json・boss.json` を書く。見本は `$K/mods/Genji/lines/`（形だけ）。5本とも check_lines.py がOKになったら、`mkdir -p $K/tmp/<コード>_lines/t && cd $_ && cp $M/cfg.py . && cp -r $M/lines . && cp -r $K/ref/sample_Medusa/scen . && python3 $K/common/gen_v4.py .` でカード生成が最後まで通ることを確かめる（通らなければ lines を直す。cfg.py は直さず、cfg 側の問題なら報告する）。報告：check と生成の可否だけ。

## 役割 img（画像プロンプト）
`$K/common/IMG_TASK.md` を最後の補足まで読み、`$K/画像生成/N106-N157_場面/scene_data/<コード>.py` を書いて check を通し、`prompts/<コード>.json` を作る。見本は同じフォルダの `Genji.py`。報告：check の結果の1行だけ。

## 役割 aux（lines → img を続けて）
同じMODについて、上の「役割 lines」を最後までやり、続けて「役割 img」を最後までやる。報告：lines の check と生成の可否、img の check の1行。

## 役割 setup3（骨組みを複数MOD）
依頼文に並んだMODを、1本ずつ順に「役割 setup」の手順で作る（1本終えて通し確認が通ってから次へ）。報告：各MODの通し確認の可否を1行ずつ。
