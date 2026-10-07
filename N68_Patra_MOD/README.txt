N68 砂の蛇使い（Patra）MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
マスター・配下の多くはゲーム本編のキャラクター（口調・性格は本編に合わせ、身長・スリーサイズ・得意技はMOD設定）。

■ 内容
- CSV\Card\  11枚：Patra_magic_1／Patra_magic_2／Patra_magic_3／Patra_magic_4／Patra_magic_5／Patra_master／Patra_mons_boss／Patra_mons_e1／Patra_mons_e2／Patra_mons_e3／Patra_recall
- CSV\Eventlist\Quest\Patra.txt  クエスト登録（通常＋【回想バトル】）
- N68_Patra_構成表.md  カード・効果・敗北シナリオ28本
- N68_Patra_読む用シナリオ集.txt  敗北シナリオ28本を読みやすくしたもの
- tools\  生成キット（cfg.py・gen_v5.py・patch_recall_ui.py・check4000.py・check_lines.py・lines\5本・scen\28本）

■ 画像
- 本編キャラの立ち絵は本編の画像名をそのまま指定（master=F16.png／e1=EU37.png／e2=EU38.png／boss=EU39.png）。
  背景は &&闘技場背景（本編内蔵）。※MODから本編の画像を呼べるかは実機で要確認。
- 新しく作る画像（Picture\Patra\）：技CG（atk_m1〜m3・atk_e1〜boss）、敗北CG28（lose_<経路>_<責め手>）、オナニー5（onanie_*）、魔法5（magic_1〜5）、新規キャラの立ち絵（e3）。
  画像が無いと画像の行で止まる可能性があります。

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Patra_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Patra.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Patra\ へ
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「毒牙の痕」：主人公 相手プレイヤー.$毒牙の痕（12で敗北＝蛇の巣の番）、男モンスター 相手.$毒牙の痕（6で蛇笛の吹き手）。
  ★得意技だけ加算（マスター・上級+3、下級+2）。セリフは受けた側の段階で4段階×主人公向け／モンスター向け。
- 挿入技は受けた側の $ほぐし が2未満なら指ほぐしに置き換わる。
- 固有効果【蛇の巣】：主人公の毒牙の痕6以上・自ターン終了時、男モンスター1体に麻痺2ターンと毒牙の痕+1（6で蛇笛の吹き手として敵側へ）。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>（1本 約4,000字・本編の文体）。

■ 実機未確認の点
本編の立ち絵・背景をMODから呼べるか／クエスト一覧の表示／受けた側ごとのスタック／女装娘の特殊召喚
