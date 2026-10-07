N61〜N105 ＋ N17 Scylla の画像プロンプト（2026-09-29）
=====================================================

■ 作ったもの
・prompts\<コード>.json … 46MOD・2,352件（1MODあたり 立ち絵5・背景1・技CG7・敗北CG28・オナニーCG5・魔法5、女装娘のあるMODは＋1）
  N61〜N75：Konoha Eruru Exam Sister Flower Tavern Octa Patra Cammy Neneko Eiraira Yatsume Musashi Necro SEruru
  N76〜N105：Gemini Sylvia Kiss Perfume Queen Inn Ranch Tengu Centaur Labyrinth Military Atelier Tea Bride General
             Underworld Spirit Moth Werewolf Smith Clock Mirror Beach Medusa Sphinx Valkyrie Pawn Amazon Shrine Sky
  N17：Scylla（前の画像生成バッチが無くなっていたため、シナリオから作り直した）
  女装娘あり：Sister Tavern Perfume Atelier Bride Shrine
・N61-N105_場面\scene_data\<コード>.py … 中身（人物の見た目・場所・場面の英文）。ここを直して
  画像プロンプトを作り直す_N61-N105.bat を実行すると、そのMODの JSON だけ作り直せる。
・N61-N105_場面\build_new.py … 組み立て（場面の部分は N31-N60_場面\build_scenes.py と同じ関数＝主人公・成人タグ・逆転防止ネガが共通）
・生成_N61-N105.bat … 46MODをまとめて撮る（絵柄のランダム割当も選べる）。1MODずつなら 生成.bat にコードを入れる。

■ 本編キャラの見た目は仮（要確認）
本編の立ち絵はゲームのデータの中にあって見られないため、シナリオの文章の手がかり（服・胸・種族など）と役柄から
見た目を決めた。髪・瞳の色はほぼ推測。N61-N105_場面\本編キャラ外見_要確認.csv に57人の一覧（本編の画像名と今のタグ）がある。
→ ゲームで立ち絵を見て、違っていれば scene_data\<コード>.py の chars の tags を直し、画像プロンプトを作り直す_N61-N105.bat。
  （本編キャラの立ち絵はゲームの画像を使うので、<コード>_master.png などを撮っても使わない。キャラLoRAの学習用には使える）

■ 場面を選んだ基準
各敗北シナリオ（28本）のクライマックスか結末の一場面。挿入の絵は、その本で実際に挿入する人物だけ（指でほぐした後）。
オナニーは主人公ひとり・相手の得意技をなぞる自慰・ペニスに触れない・相手は遠くで見ているだけ。
3人以上は出さない（原作で複数人の場面は、1人の瞬間を選んだ）。

■ 作るときに直した点（build_new.py）
・ケンタウロス・アラクネ・タコ・人魚・ラミアなど人外の下半身のキャラは、共通ネガの extra legs / three legs / four legs を外す
・ペニバンの色・形をキャラごとに（シスター＝白い革、スフィンクスの女王＝黄金、戦乙女＝光、など chars の "strap"）

■ 確認済み
・46MODとも件数どおり（51／52件）、年齢を示す語なし、場面に主人公あり、オナニー場面は全部 penis untouched、
  相手の髪・瞳に紺・青系なし
・gen.py の dry-run で46MOD・2,352件（約13時間）を認識。敵キャラLoRAの判定（atk_m1→master 等）も動く
・実機ではまだ撮っていない
