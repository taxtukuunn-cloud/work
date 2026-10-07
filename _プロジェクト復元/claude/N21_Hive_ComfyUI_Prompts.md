> 【復元メモ】2026-09-24 にプロジェクト消失のため、会話内に残っていた内容から復元（元の版の日時：2026-09-24 夜にこの会話で登録しようとした全文。プロジェクトが消えていて登録できなかったため、元のプロジェクトには一度も入っていない新規の資料）

# N21 蜂の女王の巣（Hive）画像生成メモ（2026-09-24）

- **51枚すべて生成・目視確認済み**。完成画像：`Downloads\MOD\N21_Hive_MOD\Picture\Hive\`（カードが参照する名前のまま）。ゲームへは `画像生成バッチ\install_hive.bat`（引数なしでゲーム本体の `Picture\Hive` にコピー。**まだコピーしていない**）。
- ComfyUIの出力：`ComfyUI\output\Hive\`（`_00001_` 付き。主人公の出る40枚は最終版で上書き済み）、`Hive_v2\`・`Hive_rt\`（撮り直しと候補）、`Hive_test\`。
- 設定：N20と同じ（Anima 3ローダー・832×1216・er_sde・simple・36step・CFG4.5・seed_base 20260926）。プロンプトは `画像生成バッチ\build_prompts.py` → `hive_prompts.json`。
- 生成方法（今回）：PCのシェルが使えないため、アプリ内ブラウザで `http://127.0.0.1:8188` を開き、`ComfyUI\input\` に置いたワークフローJSON（`hive_workflows.json` など）を `/view?type=input` で読み込んで `/prompt` に投入した。バッチ（`gen_hive_all.bat`）でも同じものが作れる。1枚約18秒。

## 1回目で見つかった問題と対策（重要・全MOD共通の教訓）
- **主人公が幼く見える体つきで描かれた**（特にオナニー系の一人の場面）。原因は `petite, short, androgynous, feminine body, narrow shoulders, thin arms` の組み合わせ。成人の性的な画像として不適切なので、**主人公の出る40枚をすべて作り直し、古い画像は上書きした**。
  - 対策後の主人公タグ：`adult man, mature male, 25 years old, adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, adam's apple, collarbones, flat male chest … he is a head shorter than her`（小柄さは「相手より頭ひとつ低い」で表し、petite 等は使わない）。
  - ネガティブに `childlike, child body, youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, small body, petite male, boy` を追加。
  - **他のMODのプロンプトにも `petite, short, androgynous, feminine body` の主人公タグが残っていれば、同じ直しを入れること。**
- 主人公に触角が付く（ふたなりの場面など）→ 主人公タグに `ordinary human man with no antennae and no wings`。候補3枚から選び直し：atk_boss c3／atk_m3 c3／lose_btl_boss c3／lose_inochi_m3 c3／lose_onani_m3 c1／lose_onedari_boss c3／lose_onedari_m3 c1／onanie_master c3。
- オナニーで手がペニスに行く → `both of his hands are clearly away from his penis` とネガティブ `hand on crotch` 等。

## 気になるが採用したもの
- ワスプの腕は立ち絵・場面とも2本に見えるものが多い（4本の設定は画像では弱い）。
- 尿道の管（atk_m1・lose_*_m1）は、細い管がはっきり見えない絵がある。
- 気になる時は `run_hive.bat Hive_<キー> --random --batch 4` → `--pick`。
