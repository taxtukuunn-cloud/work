N82_Ranch_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
ミルク牧場（牧場主　ダリア）

■ 内容
- CSV\Card\  カード（Ranch_master／mons_e1〜e3・mons_boss／magic_1〜5／Ranch_recall＝回想の栞）
- CSV\Eventlist\Quest\Ranch.txt  クエスト登録（通常＋【回想バトル】の2行）
- N82_Ranch_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 51枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Ranch_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Ranch.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Ranch\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「搾乳瓶」：主人公 相手プレイヤー.$搾乳瓶（12で敗北）、男モンスター 相手.$搾乳瓶（6で敵側へ寝返り（コントロール変更））。
  ★得意技だけ加算：牧場主　ダリア「乳搾りの手ほどき」+3／乳搾り係　ミルカ「乳枕」+2／牧羊犬　シェパ「毛づくろい」+2／チーズ職人　ブリエ「味見の口移し」+2／大乳牛　ボヴィーナ「母牛の抱擁」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：牧場主　ダリア「締め搾り」・大乳牛　ボヴィーナ「牛舎の奥で」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N82_Ranch_MOD\Card Ranch
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
