# プロジェクト「サキュバスデュエルMOD作成」復元フォルダ（2026-09-24）

プロジェクトが消えた（開くと404）ため、Claude（Cowork）の会話内に残っていた内容から書き出したもの。
フォルダ構成は元のプロジェクトと同じ（`claude/` 付きの名前は `claude\` フォルダの中）。
新しいプロジェクトを作ったら、`00_プロジェクト指示_最新版.md` の中身をプロジェクトの指示欄に貼り、残りのファイルをアップロードする（またはClaudeに登録を頼む）。

## 復元できたもの
| ファイル | 状態 |
|---|---|
| 00_プロジェクト指示_最新版.md | **全文**（2026-09-24 時点） |
| 00_プロジェクト指示_旧版_2026-09-23.md | 全文（参考） |
| MOD制作_進捗とルールまとめ.md | **全文**（2026-09-23 10:30 版。09-24 01:30 の更新分は未反映） |
| Project_Knowledge.md | **全文** |
| claude/新MOD企画書_N16-N30_v4.md | **全文**（各MOD節の末尾の定型3行だけ、一覧の下にまとめた） |
| claude/新MOD企画書_N16-N30_v3.md | v4との差分だけ（v3はv4で置き換え済みの参考資料） |
| claude/キャラクター設定_N16-N23_女性.md | 全文（09-23 版）＋ N19・N20 の得意技表。N16〜N18・N21〜N23 の得意技表は未復元（企画書v4から作り直せる） |
| claude/N12_Salon_執筆ブリーフとツール.md | **全文**（brief.md・check.py・gen.py） |
| claude/N17_Scylla_設計メモ.md | **全文**（2026-09-24 v4対応・撮り直し後の最終版に差し替え。前の版は `claude/N17_Scylla_設計メモ_旧.md`） |
| claude/N17_Scylla_ComfyUI_Prompts.md | **全文**（2026-09-24 10:31 版＋撮り直し後の差分を付録に） |
| claude/N19_Twins_設計メモ.md | **全文** |
| claude/N20_Vampire_設計メモ.md | **全文**（最新） |
| claude/N20_Vampire_ComfyUI_Prompts.md | **全文**（最新） |
| claude/実機確認_話者変更と画像表示.md | ほぼ全文（抜粋から） |
| claude/実機確認_敗北シナリオの呼び方.md | 一部（前半〜原因の候補2まで） |
| claude/N16_Alraune_設計メモ.md | ほぼ全文（09-23 版の抜粋から） |
| claude/N6_Puppet_設計メモ.md | 一部（中ほどが欠け） |
| claude/N12_Salon_設計メモ.md | 一部（冒頭と実機確認の項が欠け） |
| claude/N15_Dorm_設計メモ.md | 断片のみ |

## 復元できなかったもの（この会話では開いていない）
- claude/キャラクター設定_N24-N30_男の娘.md
- claude/N18_Lamia_設計メモ.md、claude/N18_Lamia_執筆ブリーフ.md
- claude/N21_Hive_設計メモ.md、claude/N22_Prison_設計メモ.md、claude/N23_Heels_進捗メモ.md
- claude/N2_Circle_完成メモ.md、claude/N3_Inma_完成メモ.md、claude/N4_Android_設計メモ.md、claude/N5_Witch_設計メモ.md、claude/N8_Esthe_設計メモ.md、claude/N11_Slime_設計メモ.md、claude/N11_Slime_執筆ブリーフ.md、claude/N13_CrossCafe_設計メモ.md、claude/N14_Idol_設計メモ.md
- claude/N6_Puppet_執筆ブリーフとツール.md
- 各MODの ComfyUI プロンプト集（N2・N5・N6・N11・N16・N22・N23。N8・N12・N15・N17 は登録済み）
- claude/新MOD企画書_N16-N25.md（旧案）
- MOD企画書_15種_v2.md、詳細企画_A〜D、キャラクター設定_A〜D
- Project_Instructions.md、Project_Instructions_追記.md、Rosetta_ComfyUI_Prompts.md

### 取り戻す手がかり
- **各MODのフォルダ（`Downloads\MOD\`）**：README（修正履歴）・tools（執筆ブリーフ・生成スクリプト・シナリオ本文）・画像生成バッチ（build_prompts.py＝プロンプト全文）が残っている。設計メモとComfyUIプロンプト集は、ここから作り直せる。
- **ほかのClaudeの会話**：上のファイルを読み込んだ会話が残っていれば、その会話で「○○の全文を書き出して」と頼むと取り戻せる可能性がある。
- **Googleドライブの元ファイルのフォルダ**：企画書・キャラ設定をアップロードしていれば残っている可能性がある。
