# サキュバスデュエル MOD制作 — ナレッジ

## 0. ユーザー環境
- OS：Windows。ComfyUI ポータブル版：`C:\Users\taku2\Downloads\ComfyUI_windows_portable`（同梱Python：`python_embeded\python.exe`。システムのPythonは未導入）。
- 画像生成：ComfyUI ＋ **WAI-Anima**（Anima系）。追加ノード：ComfyUI-Inspyrenet-Rembg（背景除去）。
- ユーザーはMOD制作初心者。個人利用のみ。

## 1. ゲームとMODの仕組み
- Unity製のカードバトル。カード・イベント・敵マスターは**テキストスクリプト**で定義。
- フォルダ：`Card/`（カード・敵マスター）、`Eventlist/`（イベント登録）、`Picture/<MOD名>/`（画像）、`CSV/…`（本体データ）、`BGM/`、`SE/`。
- **イベント登録**（`Eventlist/*.txt` の1行）：`表示名,Card/<ファイル名(拡張子なし)>,クエストイベント`（またはイベント）。
- 敵の**デッキ**：`デッキ設定,<Cardファイル名>,…`（同名を複数書くと複数枚）。
- 画像指定：`#フォルダ/ファイル.png`（例：`#Rosetta/Elsa.png`）。

## 2. スクリプト書式（既存MOD「kuruMOD メスイキ」「ディアナ」等で確認済み）
**ファイル構造**：1行目 `default`／`@初期設定`／`@効果`／`@効果_街バトル`（`イベント実行,効果`）／敵マスターは `@クエストイベント` と戦闘フック。
**@初期設定**：`&カード名` `&カード画像` `属性設定` `タイプ設定`（悪魔／通常魔法／永続魔法／装備魔法／通常罠 等）`レベル設定` `攻撃力設定` `最大HP設定` `レアリティ設定` `性別設定` `攻撃エフェクト設定` `効果設定,ID,種別,説明`（種別：通常／play／強制誘発／永続効果／explain）`誘発効果設定,ID,タイミング`（通常召喚時／エンドフェイズ開始時／メインフェイズ開始時／onOtherSummon）`効果条件設定` `永続効果設定,自分,seal攻撃宣言,(true)`。
**敵マスターのフック**：`@試合開始` `@戦闘`（攻撃宣言時）`@戦闘後` `@ターン終了宣言` `@オナニー` `@終了時一言` `@相手特殊召喚後`。
**主なコマンド（確認済み）**
- 表示：`セリフ` `説明` `話者,自分/相手/相手プレイヤー/自分プレイヤー/%変数` `画像,ファイル,位置` `画像削除` `画像全削除` `背景変更` `BGM` `SE` `フラッシュ,ピンク` `エフェクト,名前,対象` `エフェクト拡大表示,名前,サイズ` `フェードアウト/フェードイン` `技名表示/技名削除` `アラート` `選択肢生成`
- 戦闘：`イベントダメージ,対象,値` `とどめダメージ` `ループダメージ,対象,値,間隔,SE` `ループダメージ停止` `イベントヒール` `状態異常付与,対象,名前[,ターン]` `状態異常解除` `攻撃タイプ変更` `攻撃エフェクト変更` `攻撃力加算` `HP加算` `射精`
- カード操作：`効果除外` `効果破壊` `特殊召喚,%カード,味方（＝敵側）/相手所属（＝主人公側）` `効果生成デッキ内,&ID,味方` `%x,=,自分デッキ.?ID:&ID` `外部カードイベント実行,イベント名,%カード` `カードランダム抜き出し,相手モンスター,1,%x` `カード抜き出し`
- 制御：`if / else / while / switch,case` `乱数生成,1,N` 変数（`$`グローバル・`%`ローカル・`&`文字列・`対象.$変数`）
- 敵イベント：`デッキ設定` `デッキ報酬設定,金,経験,ランク経験` `バトル設定,相手先攻` `バトル開始,背景,BGM` `if,is敗北,==,true`
**状態異常（確認済み）**：寸止め（HPを1で止める＝HP0判定に使う）／魅了／発情／ぬるぬる／攻撃不能／攻撃指示不能／魔法使用不能／隠密／メロメロ／おっぱいに弱い。
**素材キー**：背景 `&&街背景` `&&路地裏背景` `&&豪華な寝室背景`／BGM `&&戦闘BGM` `&&敗北BGM` `&&南の村BGM`／SE `&&怪しい光SE` `&&行為SE` `&&行為はげしめSE` `&&服を脱がすSE`／エフェクト `&&セクシーエフェクト` `&&セクシーエフェクト2` `&&フェロモンエフェクト` `&&ハートスタンプエフェクト` `&&魔法攻撃エフェクト`。
**参照した既存ファイル**：`Card/夢見咲.txt`（モンスター）`Card/催眠香.txt`（永続魔法）`Card/dianatest.txt`（敵イベント）／`kuruMOD_Mesuiki_master.txt`（クエスト敵マスターの手本）`…_trap_TrapDildo`（罠）`…_mons_FallenIntoGirl`（堕ちたキャラの特殊召喚）。※kuruMODの「少女」系カードは成人条件に合わないため流用しない。

## 3. 現在の成果物：黒薔薇の館（ロゼッタ）MOD（`Rosetta_MOD.zip`）
- 敵マスター：**黒薔薇の調教師ロゼッタ**（26）。従者：**エルザ**（24）＝**乳首責め**（指と舌）、**ヴィヴィアン**（28）＝**指で前立腺診察（アナル責め）**、**ミレーユ**（27・洗脳担当）＝目隠し＋乳首とアナルの器具同時責め＋耳元で洗脳。
- デッキ（3枚ずつ24枚）：従者エルザ／調教医ヴィヴィアン／洗脳調教師ミレーユ／黒薔薇のオイル／調教ペニバン（罠）／女王の命令／黒薔薇の調教部屋（永続）／メス堕ち完成の儀。
- 進行：主人公の `$メス堕ち度` が 1〜6 乳首（指と舌）／7〜13 前立腺（**ロゼッタは尻尾**）／14〜19 ペニバン／20 完成（即敗北）。
- モンスター優先：対象を `カードランダム抜き出し,相手モンスター` で決定。モンスターごとに `$メス堕ち度`。8以上、またはHP≦1（寸止めで維持）で `♥メス奴隷♥`（`Rosetta_mons_Slave`）を敵側に特殊召喚（元の攻撃力・HPを引継ぎ）。
- メス奴隷：性別＝男。攻撃・守備不可。ロゼッタのターン開始時に精気を吸われ、ロゼッタHP+300。
- メス堕ち台詞：ロゼッタ／エルザ／ヴィヴィアン／ミレーユで別々。変換画像も別（`Rosetta_convert` `Elsa_convert` `Vivian_convert` `Mireille_convert`）。
- **敗北ルート**：第一の躾け（乳首）→第二（尻尾で前立腺・断面図）→第三（ペニバン・断面図）→**第四（ミレーユの洗脳・断面図）**→メス堕ち完成→GAME OVER。
- **断面図**：アナル責めの場面（ロゼッタの尻尾／ペニバン／ヴィヴィアンの指／ミレーユの器具・罠のペニバン）で、責める部位が前立腺を圧迫している断面図に切り替えて表示（`画像` → `説明` → 元の画像）。
- ファイル：`Card/Rosetta_master.txt`／`Rosetta_mons_Elsa/Vivian/Mireille/Slave.txt`／`Rosetta_magic_RoseOil/QueenCommand/TrainingRoom/FinalDrop.txt`／`Rosetta_trap_PeggingTrap.txt`／`Eventlist/Rosetta.txt`。
- 画像（`Picture/Rosetta/`・全27枚）：Rosetta_master／nipple／prostate／**prostate_xsec**／pegging／**pegging_xsec**／complete／convert／oil／command／room／final／slave_drain、Elsa／**Elsa_nipple**／Elsa_convert、Vivian／Vivian_exam／**Vivian_exam_xsec**／Vivian_convert、**Mireille／Mireille_double／Mireille_double_xsec／Mireille_convert**、Rosetta_mons_Slave／_2／_3。（`*_xsec` が断面図）
  - 攻撃時・カード効果発動時・変換時に画像を表示し、処理後に消去。
  - カード画像の流用：エルザ＝Elsa／ヴィヴィアン＝Vivian／メス奴隷＝Rosetta_mons_Slave／オイル＝Rosetta_oil／女王の命令＝Rosetta_command／調教部屋＝Rosetta_room／完成の儀＝Rosetta_final／調教ペニバン＝Rosetta_pegging。
- 未検証：実機テスト未実施。変換処理・画像位置・数値（閾値8、ダメージ、回復300）は仮。

## 4. 画像生成（ComfyUI / WAI-Anima）
- 必要ファイル（`ComfyUI\models\`）：`diffusion_models\waiANIMA_v10.safetensors`／`text_encoders\qwen_3_06b_base.safetensors`／`vae\qwen_image_vae.safetensors`。ComfyUIは最新に更新。
- ノード：UNETLoader ＋ CLIPLoader（**type=qwen_image**）＋ VAELoader。KSampler：`er_sde`／`simple`／30〜50step／CFG 4〜5／832×1216。
- プロンプト：Danbooruタグ（小文字・スペース）。先頭 `masterpiece, best quality, score_7` ＋安全タグ（safe/sensitive/nsfw/explicit）＋キャラ＋シーン。ネガティブに未成年除外語。
- ロゼッタ・エルザ・ミレーユは `large breasts`（ネガティブに `small breasts, flat chest`）。
- 被責め側の男性：`1boy, faceless male, androgynous, slender, petite, adult male, nude male, erection, penis`。ネガティブに `muscular, abs, broad shoulders, beard, body hair`。敵側のネガティブには `collar, choker`。
- **H画像の構図ルール**（実際に出た失敗から）：
  - 主語のない姿勢タグ（`legs up` `spread legs` 等）は**女性側に付く**ことがある（エルザ・ヴィヴィアンが自分で挿入される絵になった）→ 英語の文で「her fingers are inside HIS ass」「only the man is undressed」と明記し、責める側は `clothed female, cfnm`。
  - 正面POVだと被責め側のペニスと敵のペニバンが**融合**した → アナル責めは**側面（`from side, side view`）**で、勃起したペニスは別に立たせる。ネガティブに `merged, fused, overlapping, penis touching strap-on`。
  - 前立腺責め（ロゼッタ）は**尻尾**。**断面図は別画像**で作る（`1boy, lower body, cross-section, x-ray, internal view, prostate`＋「責める部位が外から入って前立腺を圧迫」）。断面図が**男側の挿入に見える失敗**が出た → 人物を描かず、ネガティブに `penis in anus, penis insertion, male penetrating`、プロンプトで「勃起したペニスは体の外」と明記。
  - **主人公サイドが女性に挿入する絵は作らない**：ネガティブに `vaginal, vaginal sex, cowgirl position, pussy, nude female, futanari`。
- 背景除去：立ち絵6枚（Rosetta_master／Elsa／Vivian／Slave×3）は白背景で生成→InspyrenetRembg。
- 付属ツール（`tools/`）：`Rosetta_workflow.json`（画面用）／`Rosetta_workflow_api.json`／`Rosetta_prompts.json`／`run_rosetta_batch.py`／`run_rosetta.bat`。実行：`run_rosetta.bat 名前 [--random|--seed N|--batch 1|--no-rembg|--list-models]`。結果は `tools\candidates\`。

## 5. 判明したトラブルと対処
| 症状 | 原因・対処 |
|---|---|
| `Python was not found` | Pythonなし → ComfyUI同梱の `python_embeded\python.exe` を使う（batに設定済み） |
| `missing_node_type InspyrenetRembg` | ノード未導入 → Manager導入、または `--no-rembg` |
| `clip input is invalid: None` | Anima系は一体型ではない → UNET＋CLIP＋VAEの3ローダーを使う |
| H画像で責める側と責められる側が逆／融合する | 上の「H画像の構図ルール」を参照。プロンプトで主語を明記し、側面構図にする |
| 画像が更新されない | 固定シード＋キャッシュ → `--random` / `--seed N`。スクリプトは旧候補を掃除 |
| `qwen_image`／`er_sde` のエラー | ComfyUIが古い → `update_comfyui.bat` |
| `out of memory` | `--batch 1` |
| `Errno 22` | ComfyUIを通常のbatから起動（バックグラウンド起動だと出る） |

## 6. 今後の予定・未決事項
- 次のMOD候補：**洗脳系**（主人公を洗脳）／**ルーインド→潮吹き系**（寸止め回数を溜め、解放カードで潮吹き）。いずれもM向け・主人公側のみ被責め。
- 未決：ロゼッタの効果の対象を**男性モンスターのみ**に限定するか（現状は男女問わず）。
- 実機テストの結果（エラー内容）を受けて、コマンド・画像位置・数値を調整する。
