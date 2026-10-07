N15 常識改変の社員寮（コード Dorm）  2026-09-23
個人利用のみ。登場人物は全員20歳以上。

■入れ方
- Card/ の中身 → ゲームの CSV/Card/
- EventList/FieldFaces/Dorm.txt → CSV/EventList/FieldFaces/（街モルゲンに寮母サクラが出ます）
- 画像 → Saveと同じ階層の Picture/Dorm/ （install_images.bat Dorm "<ゲーム>\Picture"）
  ※画像は未生成（49枚）。ファイル名はカード内の参照と一致させてください。
  立ち絵5：Dorm_master / Dorm_e1 / Dorm_e2 / Dorm_e3 / Dorm_boss
  技CG7：Dorm_atk_m1〜m3 / Dorm_atk_e1〜e3 / Dorm_atk_boss
  魔法5：Dorm_magic_1〜5　特殊3：Dorm_inochigoi / Dorm_onanie / Dorm_onedari　背景：Dorm_bg
  敗北28：Dorm_lose_<btl|onani|inochi|onedari>_<m1|m2|m3|e1|e2|e3|boss>

■ゲージ
常識改変度 0〜24（減らない）。マスター攻撃+2／下級+1／上級+2。24で敗北。
段階：1〜5 規則を渡される／6〜11 着付けが始まる／12〜17 点呼が日課に／18〜23 当たり前

■敗北シナリオ
28本（各5,500〜6,400字、合計約15.8万字）。Dorm_敗北シナリオ集_読む用.txt で通読できます（ゲームには入れない）。

■tools/
brief.md（執筆ブリーフ）、scen/（台本の元データ）、lines/（攻撃セリフ）、gen.py（カード生成）、check.py（台本チェック）、lint.py（構文チェック）
台本を直したら python3 gen.py で Card/ を作り直せます。
