N65 ギルドの胞子調査（Flower）MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
マスター・配下の多くはゲーム本編のキャラクター（口調・性格は本編に合わせ、身長・スリーサイズ・得意技はMOD設定）。

■ 内容
- CSV\Card\  11枚：Flower_magic_1／Flower_magic_2／Flower_magic_3／Flower_magic_4／Flower_magic_5／Flower_master／Flower_mons_boss／Flower_mons_e1／Flower_mons_e2／Flower_mons_e3／Flower_recall
- CSV\Eventlist\Quest\Flower.txt  クエスト登録（通常＋【回想バトル】）
- N65_Flower_構成表.md  カード・効果・敗北シナリオ28本
- N65_Flower_読む用シナリオ集.txt  敗北シナリオ28本を読みやすくしたもの
- tools\  生成キット（cfg.py・gen_v5.py・patch_recall_ui.py・check4000.py・check_lines.py・lines\5本・scen\28本）

■ 画像
- 本編キャラの立ち絵は本編の画像名をそのまま指定（master=F11_Stand.png／e1=EU32.png）。
  背景は &&森背景（本編内蔵）。※MODから本編の画像を呼べるかは実機で要確認。
- 新しく作る画像（Picture\Flower\）：技CG（atk_m1〜m3・atk_e1〜boss）、敗北CG28（lose_<経路>_<責め手>）、オナニー5（onanie_*）、魔法5（magic_1〜5）、新規キャラの立ち絵（e2・e3・boss）。
  画像が無いと画像の行で止まる可能性があります。

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Flower_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Flower.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Flower\ へ
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「胞子の芽」：主人公 相手プレイヤー.$胞子の芽（12で敗北＝苗の眠り）、男モンスター 相手.$胞子の芽（6で茸の森で眠る）。
  ★得意技だけ加算（マスター・上級+3、下級+2）。セリフは受けた側の段階で4段階×主人公向け／モンスター向け。
- 挿入技は受けた側の $ほぐし が2未満なら指ほぐしに置き換わる。
- 固有効果【苗床の眠り】：主人公の胞子の芽6以上・自ターン終了時（1試合2回まで）、男モンスター1体に麻痺1ターンと胞子の芽+2（6で茸の森で眠り破壊）。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>（1本 約4,000字・本編の文体）。

■ 実機未確認の点
本編の立ち絵・背景をMODから呼べるか／クエスト一覧の表示／受けた側ごとのスタック／女装娘の特殊召喚
