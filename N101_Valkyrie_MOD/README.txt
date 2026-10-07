N101_Valkyrie_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
戦乙女の選定（戦乙女の長　ヘルヴォラ）

■ 内容
- CSV\Card\  カード（Valkyrie_master／mons_e1〜e3・mons_boss／magic_1〜5／Valkyrie_recall＝回想の栞）
- CSV\Eventlist\Quest\Valkyrie.txt  クエスト登録（通常＋【回想バトル】の2行）
- N101_Valkyrie_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 51枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Valkyrie_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Valkyrie.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Valkyrie\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「選定の羽根」：主人公 相手プレイヤー.$選定の羽根（12で敗北）、男モンスター 相手.$選定の羽根（6で破壊）。
  ★得意技だけ加算：戦乙女の長　ヘルヴォラ「選定の口づけ」+3／盾の戦乙女　ルーネ「盾の内側」+2／天馬番　スヴァナ「羽根ぼうき」+2／蜜酒の給仕　ミードラ「蜜酒の谷間」+2／戦乙女の副長　エイラヴィル「魂の抱擁」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：戦乙女の副長　エイラヴィル「光の槍」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N101_Valkyrie_MOD\Card Valkyrie
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
