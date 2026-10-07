# N15_Dorm v4 画像生成（絵柄LoRA対応）

v4 の敗北シナリオ・キャラ設定に合わせて作り直したプロンプト（47枚分）と、生成ツール一式です。
ファイル名はすべて v4 のカードtxt が参照する名前と一致しているので、カード側の修正は不要です。

## 使い方
1. ComfyUI を起動しておく。
2. このフォルダで `run_mod.bat Dorm all`（全47枚）。1枚だけなら `run_mod.bat Dorm atk_boss` のようにキー指定。
   - 別の絵が欲しいときは `--random` か `--seed N` を付ける。キー一覧は `run_mod.bat Dorm --list-keys`。
3. 画像は ComfyUI の output フォルダに `Dorm_<キー>_00001_.png` の名前で出ます。
4. 気に入ったら `install_images.bat Dorm "<ゲーム>\Picture"` で `Picture\Dorm\` にカードどおりの名前でコピー（既存は `--overwrite` を付けたときだけ上書き）。

## 絵柄LoRA
`run_mod_batch.py` は `Downloads\Lora用\lora_hook.py` を読み込み、sdduel_style（強さ0.6、トリガー "sdduel style"）を自動で挿します。
LoRA を外したいときは run_mod_batch.py 冒頭の「絵柄LoRA」の5行を消してください。

## 中身
- prompts\Dorm_prompts.json … 生成に使うプロンプト（v4版）
- v4_src\spec.py / scenes.json … プロンプトの元データ（キャラの見た目タグと場面文）。直したいときはここを見れば、どの絵に何を書いたか分かります。
- 主人公は全MOD共通で「紺色の髪で目が隠れた、責め手より頭ひとつ背の低い成人男性」として描きます。
