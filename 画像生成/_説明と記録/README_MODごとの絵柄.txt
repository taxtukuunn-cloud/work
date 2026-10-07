MODごとの絵柄（2026-09-29）
==========================

目的：MODごとに絵柄（絵柄LoRA）を変える。主人公も、そのMODの絵柄で学習した主人公LoRAを使い、
      イベント画像と主人公の絵柄をそろえる。

■ しくみ
・絵柄割当.csv の「絵柄」列に絵柄名（ATRex・Mosouko など）を書いたMODは、
  - 本編の絵柄LoRA（sdduel_style_xl）の代わりに、その絵柄LoRA
  - 共通の主人公LoRA（sdduel_hero_xl）の代わりに、その絵柄で学習した主人公LoRA
      sdduel_hero_xl_<絵柄>-000008.safetensors
  を使って撮ります。保存先は ComfyUI\output\<MOD>_WAI_<絵柄>\（今までの <MOD>_WAI\ とは別）。
・空欄のMODは今までどおり（<MOD>_WAI\）。
・その絵柄の主人公LoRAがまだ無いときは、主人公LoRAなしで撮ります（別の絵柄の主人公LoRAは混ぜません）。
・主人公LoRAは、主人公がひとりの絵（立ち絵・オナニー）は 0.8、2人の場面（イベント）は 0.5（2026-09-29 変更。前は 0）。
  model.json の mod_style.hero_scene_strength で変更可。イベントの敵キャラLoRAは Lora用\chara\README_キャラLoRA.txt
・完成フォルダへ集める.bat も、割当に従って <MOD>_WAI_<絵柄>\ から集めます。

■ 手順（絵柄1つにつき）
1. 画像生成\絵柄割当.bat … 使える絵柄の一覧を見て、絵柄割当.csv に書く（Excel/メモ帳。UTF-8のまま保存）
   ※一覧は 絵柄比較 と同じ候補（gen.py の STYLE_CANDS）。
2. Lora用\hero\S1_絵柄別_学習画像を撮る.bat … 絵柄名を入れる → ComfyUI\output\hero_ds_xl_<絵柄>\ に111枚
   （学習画像は MODのイベント画像と同じ絵柄LoRA・同じ強さで撮る＝絵柄がそろう）
3. hero_ds_xl_<絵柄> を見て、崩れた画像・幼く見える／老けて見える画像を消す（20枚以上残す）
4. Lora用\hero\S2_絵柄別_学習データ作成.bat … 絵柄名を入れる
5. ComfyUI を閉じて Lora用\hero\S3_絵柄別_学習.bat … 絵柄名を入れる（30分ほど。終わると loras へ自動コピー）
6. （任意）画像生成\主人公絵柄別比較.bat … エポックの見比べ
7. 画像生成\生成.bat で、そのMODを撮る（全部撮り直し）

■ ランダム割当（2026-09-29 追加）
・生成.bat／一括生成_全MOD.bat の最初に「MODの絵柄をランダムに割り当てる？」と聞きます。
    y ＝ 絵柄が空欄のMODだけランダムに決める
    a ＝ 対象のMODを全部振り直す（前の絵柄で撮った画像は <MOD>_WAI_<前の絵柄>\ に残ります）
    Enter ＝ しない
・決めた絵柄は 絵柄割当.csv に保存（メモ列に「ランダム 日時」）。次回からはその絵柄のまま
  （撮り直しても同じMODの中で絵柄が混ざらない）。気に入らなければ CSV を直すか、a で振り直し。
・なるべく偏らないよう、使われている数が少ない絵柄から選びます。
・選ばない絵柄：model.json の mod_style.random_exclude（既定：本編v2強・matureBody〈体型LoRA〉・DHIBI〈白黒漫画〉）。
  "random_hero_only": true にすると、主人公LoRA（絵柄別）を作り終えた絵柄だけから選びます。
・コマンド：gen.py <MOD|all> --random-style [all] --assign-only

■ 細かい調整（model.json の "mod_style" → "styles"）
  "styles": {
    "ATRex": {"strength": 0.7, "hero_lora": "sdduel_hero_xl_ATRex-000006.safetensors", "hero_strength": 0.7}
  }
  strength＝絵柄LoRAの強さ（イベントと主人公の学習画像の両方に効く。変えたら主人公LoRAも撮り直し推奨）
  hero_lora／hero_strength＝使う主人公LoRAのエポック・強さ
  一覧に無い絵柄LoRAも "lora": "絵柄\\ファイル名.safetensors", "trigger": "..." を書けば足せます。

■ gen.py のオプション
  --style-list     絵柄の一覧・主人公LoRAの有無（○×）・MODごとの割当を表示
  --style 絵柄名    CSV を無視してその絵柄で撮る（お試し用。保存先は <MOD>_WAI_<絵柄>）
  --no-mod-style   CSV を使わない（今までどおり）
  --no-hero        絵柄別の主人公LoRAも外す

■ 変更前のファイル
  画像生成\gen_MOD別絵柄前.py ／ collect_MOD別絵柄前.py ／ model_MOD別絵柄前.json
  Lora用\hero\make_hero_ds_xl_MOD別絵柄前.py ／ prep_hero_xl_MOD別絵柄前.py
  （H1〜H4 の bat は変えていません）
