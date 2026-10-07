N70 路地裏の猫使い（Neneko）MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
マスター・配下の多くはゲーム本編のキャラクター（口調・性格は本編に合わせ、身長・スリーサイズ・得意技はMOD設定）。

■ 内容
- CSV\Card\  11枚：Neneko_magic_1／Neneko_magic_2／Neneko_magic_3／Neneko_magic_4／Neneko_magic_5／Neneko_master／Neneko_mons_boss／Neneko_mons_e1／Neneko_mons_e2／Neneko_mons_e3／Neneko_recall
- CSV\Eventlist\Quest\Neneko.txt  クエスト登録（通常＋【回想バトル】）
- N70_Neneko_構成表.md  カード・効果・敗北シナリオ28本
- N70_Neneko_読む用シナリオ集.txt  敗北シナリオ28本を読みやすくしたもの
- tools\  生成キット（cfg.py・gen_v5.py・patch_recall_ui.py・check4000.py・check_lines.py・lines\5本・scen\28本）

■ 画像
- 本編キャラの立ち絵は本編の画像名をそのまま指定（master=F18.png／e1=EU42.png／e2=EU45.png／boss=EU41.png）。
  背景は &&路地裏背景（本編内蔵）。※MODから本編の画像を呼べるかは実機で要確認。
- 新しく作る画像（Picture\Neneko\）：技CG（atk_m1〜m3・atk_e1〜boss）、敗北CG28（lose_<経路>_<責め手>）、オナニー5（onanie_*）、魔法5（magic_1〜5）、新規キャラの立ち絵（e3）。
  画像が無いと画像の行で止まる可能性があります。

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Neneko_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Neneko.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Neneko\ へ
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「鈴」：主人公 相手プレイヤー.$鈴（12で敗北＝ネネコの猫）、男モンスター 相手.$鈴（6でネネコの飼い猫）。
  ★得意技だけ加算（マスター・上級+3、下級+2）。セリフは受けた側の段階で4段階×主人公向け／モンスター向け。
- 挿入技は受けた側の $ほぐし が2未満なら指ほぐしに置き換わる。
- 固有効果【祟り】：主人公の鈴6以上・自ターン終了時、男モンスター1体にメロメロ2ターンと鈴+1（6でネネコの飼い猫として敵側へ）。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>（1本 約4,000字・本編の文体）。

■ 実機未確認の点
本編の立ち絵・背景をMODから呼べるか／クエスト一覧の表示／受けた側ごとのスタック／女装娘の特殊召喚
