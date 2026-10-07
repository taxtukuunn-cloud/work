N77_Sylvia_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
学園首席の練習台（学園首席　シルヴィア）

■ 内容
- CSV\Card\  カード（Sylvia_master／mons_e1〜e3・mons_boss／magic_1〜5／Sylvia_recall＝回想の栞）
- CSV\Eventlist\Quest\Sylvia.txt  クエスト登録（通常＋【回想バトル】の2行）
- N77_Sylvia_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 47枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Sylvia_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Sylvia.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Sylvia\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「正の字」：主人公 相手プレイヤー.$正の字（12で敗北）、男モンスター 相手.$正の字（6で敵側へ寝返り（コントロール変更））。
  ★得意技だけ加算：学園首席　シルヴィア「基本技術」+3／光の先導者「導きの光」+2／聖盾の騎士「盾の檻」+2／寮監　ヘンリエッタ「消灯後の見回り」+2／実技主任　オーレリア「模範演技」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：寮監　ヘンリエッタ「門限破りの罰」・実技主任　オーレリア「教本の最終章」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N77_Sylvia_MOD\Card Sylvia
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
