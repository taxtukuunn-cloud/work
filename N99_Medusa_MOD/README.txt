N99_Medusa_MOD  2026-09-28
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
石化の瞳（ゴルゴンの長姉　リティア）

■ 内容
- CSV\Card\  カード（Medusa_master／mons_e1〜e3・mons_boss／magic_1〜5／Medusa_recall＝回想の栞）
- CSV\Eventlist\Quest\Medusa.txt  クエスト登録（通常＋【回想バトル】の2行）
- N99_Medusa_読む用シナリオ集.txt  敗北シナリオ28本（本編の書き方・1本約4,000字、合計 約107千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 51枚（まだありません。ComfyUIで作る）
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
1. CSV\Card\*.txt → ゲームの CSV\Card\（Medusa_recall.txt も必ず一緒に）
2. CSV\Eventlist\Quest\Medusa.txt → ゲームの CSV\EventList\Quest\
3. 画像ができたら ゲームの Picture\Medusa\ へ（画像が無いと画像の行で止まる可能性あり）
4. 回想の栞の共通画像 MOD\_共通ツール\Picture\RecallUI\recall_panel.png を Picture\RecallUI\ へ（1回だけ）
   （ゲーム本体は D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル。本MODのファイル以外は書き換えない）

■ 仕組み
- 累積スタック「石の指」：主人公 相手プレイヤー.$石の指（12で敗北）、男モンスター 相手.$石の指（6で破壊）。
  ★得意技だけ加算：ゴルゴンの長姉　リティア「石化の眼差し」+3／ゴルゴンの次姉　ペトラ「石の唇」+2／動く石像　カリアティ「石像の抱擁」+2／彫刻家　ロダナ「彫り出す指」+2／ゴルゴンの末妹　メドゥナ「石の揺りかご」+3。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：ゴルゴンの末妹　メドゥナ「石の揺りかご」 は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
tools の中で  python common/gen_v4.py .  →  python common/patch_recall_ui.py out\N99_Medusa_MOD\Card Medusa
（cfg.py 先頭の sys.path を tools\common に書き換えてから）

■ 実機未確認の点
クエスト一覧の表示／受けた側ごとのスタックの積み上がりと6での処理／性別「その他」のカード／フェードアウト・SE の行
