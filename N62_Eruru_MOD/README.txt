N62 格下のF級マスター（Eruru）MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
マスター・配下の多くはゲーム本編のキャラクター（口調・性格は本編に合わせ、身長・スリーサイズ・得意技はMOD設定）。

■ 内容
- CSV\Card\  11枚：Eruru_magic_1／Eruru_magic_2／Eruru_magic_3／Eruru_magic_4／Eruru_magic_5／Eruru_master／Eruru_mons_boss／Eruru_mons_e1／Eruru_mons_e2／Eruru_mons_e3／Eruru_recall
- CSV\Eventlist\Quest\Eruru.txt  クエスト登録（通常＋【回想バトル】）
- N62_Eruru_構成表.md  カード・効果・敗北シナリオ28本
- N62_Eruru_読む用シナリオ集.txt  敗北シナリオ28本を読みやすくしたもの
- tools\  生成キット（cfg.py・gen_v5.py・patch_recall_ui.py・check4000.py・check_lines.py・lines\5本・scen\28本）

■ 画像
- 本編キャラの立ち絵は本編の画像名をそのまま指定（master=F6_Eruru.png／e1=EU17_Carol.png／boss=EU70.png）。
  背景は &&ギルド背景（本編内蔵）。※MODから本編の画像を呼べるかは実機で要確認。
- 新しく作る画像（Picture\Eruru\）：技CG（atk_m1〜m3・atk_e1〜boss）、敗北CG28（lose_<経路>_<責め手>）、オナニー5（onanie_*）、魔法5（magic_1〜5）、新規キャラの立ち絵（e2・e3）。
  画像が無いと画像の行で止まる可能性があります。

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Eruru_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Eruru.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Eruru\ へ
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「格下印」：主人公 相手プレイヤー.$格下印（12で敗北＝エルルの格下）、男モンスター 相手.$格下印（6でエルルの荷物持ち）。
  ★得意技だけ加算（マスター・上級+3、下級+2）。セリフは受けた側の段階で4段階×主人公向け／モンスター向け。
- 挿入技は受けた側の $ほぐし が2未満なら指ほぐしに置き換わる。
- 固有効果【戦利品】：主人公の格下印9以上・1試合1回、男モンスター1体をエルルの荷物持ちとして敵側へ。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>（1本 約4,000字・本編の文体）。

■ 実機未確認の点
本編の立ち絵・背景をMODから呼べるか／クエスト一覧の表示／受けた側ごとのスタック／女装娘の特殊召喚
