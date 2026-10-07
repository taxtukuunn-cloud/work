N80_Queen_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
夜の女王の玉座（淫魔女王　リリスティア）

■ 内容
- CSV\Card\  カード（Queen_master／mons_e1〜e3・mons_boss／magic_1〜5／Queen_recall＝回想の栞）
- CSV\Eventlist\Quest\Queen.txt  クエスト登録（通常＋【回想バトル】の2行）
- N80_Queen_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 51枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Queen_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Queen.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Queen\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「跪礼」：主人公 相手プレイヤー.$跪礼（12で敗北）、男モンスター 相手.$跪礼（6で敵側へ寝返り（コントロール変更））。
  ★得意技だけ加算：淫魔女王　リリスティア「跪礼の言霊」+3／侍女長　ロザンヌ「作法の耳打ち」+2／近衛隊長　グラディス「近衛の羽交い絞め」+2／宮廷楽師　セレスタ「竪琴の指」+2／宰相　メフィスタ「詔の吐息」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：近衛隊長　グラディス「近衛の検め」・宰相　メフィスタ「宰相の裁き」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N80_Queen_MOD\Card Queen
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
