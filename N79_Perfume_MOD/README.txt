N79_Perfume_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
夜香の調香室（調香師　ミュスカ）

■ 内容
- CSV\Card\  カード（Perfume_master／mons_e1〜e3・mons_boss／magic_1〜5／Perfume_recall＝回想の栞／Perfume_josou＝女装娘（デッキ外））
- CSV\Eventlist\Quest\Perfume.txt  クエスト登録（通常＋【回想バトル】の2行）
- N79_Perfume_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 52枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Perfume_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Perfume.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Perfume\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「香りの層」：主人公 相手プレイヤー.$香りの層（12で敗北）、男モンスター 相手.$香りの層（6で敵側へ寝返り（コントロール変更））。
  ★得意技だけ加算：調香師　ミュスカ「調合した吐息」+3／試香係　ベルガ「試香紙の先」+2／調香助手　ムスク「耳の後ろの一滴」+2／着付け係　イランイラン「香りの着付け」+2／香の主　アンブル「琥珀の口づけ」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：調香助手　ムスク「麝香の奥」・香の主　アンブル「最後の香り」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N79_Perfume_MOD\Card Perfume
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
