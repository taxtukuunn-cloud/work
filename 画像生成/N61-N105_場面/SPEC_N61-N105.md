# scene_data/<Code>.py の書き方（N61〜N105 ＋ N17 Scylla・画像プロンプト全52枚前後）

目的：サキュバスデュエル（個人用MOD）の各MODの ComfyUI 用英語プロンプトを作る。N31〜N60 の `scene_data`（例：
`/home/claude/w3/画像生成/N31-N60_場面/scene_data/Oiran.py`・`ShowPub.py`・`Tutor.py`）と同じ形に、立ち絵・魔法・背景・女装娘の項目を足したもの。
共通部分（品質タグ・主人公・ネガティブ・成人タグ）は `build_new.py` が付けるので、**MOD固有の中身だけ**書く。

まず次を読むこと：
1. `/home/claude/w3/画像生成/N31-N60_場面/SPEC_scene_data.md`（場面の書き方の本則。ここに書いてあることはすべて守る）
2. 見本 `/home/claude/w3/画像生成/N31-N60_場面/scene_data/Oiran.py`（女性とNH・女装あり）、`ShowPub.py`、`Tutor.py`
3. `/home/claude/w3/画像生成/N31-N60_場面/build_scenes.py`（場面がどう組み立てられるか）と `/home/claude/w3/画像生成/N61-N105_場面/build_new.py`

## 絶対のルール
- **登場人物は全員20歳以上の成人**。tags には必ず `adult woman, mature female`（男の娘は `adult male, otoko no ko`）と年齢（`24 years old` など。人外は見た目の年齢）を入れる。
  幼さを示す語（child, kid, loli, shota, teen, young girl/boy, little, petite, schoolgirl, school uniform, 1x years old 等）は**書かない**。学園ものは `academy uniform` と書き、`mature female` を付ける。
- 責め手は常に上位。主人公（紺髪の成人男性・160cm・細身）は受け身だけ。主人公が挿入する・責め返す・相手に触れて責める構図は書かない。暴力・流血・アヘ顔・凌辱なし。
- 責め手の髪・瞳に **紺・青・水色系（navy, blue, aqua, cyan, teal）を使わない**（主人公と紛れる）。同じMOD内で髪色を被らせない。
- 3人以上を出さない（その場面の責め手1人＋主人公だけ）。文字・数字が描かれないよう小物には `without text` / `blank`。
- オナニー（lose の onani_*・onanie）は主人公ひとり。その相手の★得意技をなぞる自慰（キャラ設定のオナニー欄どおり）。**ペニスは触らない**（"penis untouched"）。相手は遠くで見ているだけ。

## ファイルの形
```python
# N76 西の鉱山の守護者（Gemini）画像データ。登場人物は全員20歳以上。
DATA = {
 "code": "Gemini",
 "world": "...（MOD全体の世界観タグ。英語）",
 "bg": "...（背景1枚。人のいない代表的な場所の英語タグ。例 'interior of a gem mine at night, glowing crystal veins on rock walls, mine cart rails, hanging lanterns'）",
 "josou": None,   # 女装娘がいるMODだけ、女装させられた男モンスターの衣装タグ（例 "black maid dress, white apron, headdress, no wig"）。無ければ None
 "chars": {
   "m": {"type": "woman", "jp": "ジェミニ", "canon": True, "canon_img": "F24.png",
         "tags": "adult woman, mature female, mature face, 24 years old, adult proportions, beautiful detailed eyes, long legs, ..., huge breasts",
         "name": "the ... in a ...",          # 場面文で使う英語の呼び名（見た目で一意に分かるもの）
         "pose": "resting her heavy breasts on an armrest, gentle droopy-eyed smile, looking at viewer",   # 立ち絵のポーズ・表情（full body 等は自動）
         "neg": ""},                            # 任意：その人物固有のネガ（人魚なら "legs"、ケンタウロスなら "human legs" 等）
   "e1": {...}, "e2": {...}, "e3": {...}, "boss": {...},
 },
 "places": {...},        # 10〜16か所。構成表／brief の場所一覧から
 "atk": {...}, "atk_desc": {...},   # 7つ（m1〜m3＝マスターの技1〜3、e1〜boss＝★得意技）
 "lose": {...}, "lose_desc": "...", # 28（btl_/onani_/inochi_/onedari_ × m1,m2,m3,e1,e2,e3,boss）
 "onanie": {...},                   # 5（master, e1, e2, e3, boss）
 "magic": {                          # 魔法・罠カード5枚の絵（cfg.py の magic の順・名前・効果から）
   "1": ("m", "place_key", "英語の行為文（その人物が魔法を使っている一枚。主人公は出さない）"),
   "2": (None, "place_key", "人物なしの小物の絵のとき（例 a sealed letter with a wax seal without text on a desk）"),
   ...
 },
}
```

### type（人物の種類）
- `"woman"`：女性・人外の女性・**ふたなり**（ふたなりは着衣の絵では女性と同じ。逆アナルの場面だけ `{"pen": "penis"}` を付けると自動で futanari になる）
- `"nh"`：ニューハーフ（見た目は女性・胸あり・自分のペニスあり）。立ち絵・着衣の場面では服の上のふくらみが自動で付く。tags に newhalf / futanari は書かない
- `"otoko"`：男の娘（平らな胸の女装男性）。このN61〜N105にはほぼいない
- cfg.py の sex が「その他」のキャラは、brief.md／キャラ設定の「性別」欄で ふたなり か NH かを確認する

### tags の作り方
- 新規キャラ：キャラ設定（chara.md／brief.md／キャラクター設定シート）の「画像タグ案」を土台に、`adult woman, mature female, mature face, <年齢> years old, adult proportions, beautiful detailed eyes, long legs` を先頭に足す。胸の大きさ・身長（マスター・上級は `tall`）も入れる。
- **本編キャラ（出典が「本編」・cfg の imgs に画像名がある／brief に「本編」とある）**：本編の立ち絵は見られない。
  1) シナリオ本文（読む用シナリオ集）・構成表・chara.md・brief.md から、髪・瞳・服・体・種族の手がかりを探して使う（grep で「髪」「瞳」「服」「胸」「角」「翼」など）。
  2) 手がかりが無い部分は、役（メイド・侍・バニー・ハーピー等）に合った自然な見た目で決める。
  3) `"canon": True, "canon_img": "<本編の画像名>"` を付ける（あとでユーザーが本編の立ち絵と見比べて直す）。
- 人外の体（ラミアの蛇の下半身、ケンタウロス、ハーピーの翼、アラクネの蜘蛛の下半身、人魚の尾、触手など）は tags に入れる。怖い・グロテスクな描写にしない（虫の脚・骸骨・腐敗などは書かない）。
- 着衣のみ。nude / nipples / pussy / penis は tags に書かない。

### 場面（atk / lose / onanie）
SPEC_scene_data.md のとおり。1本ごとに、その敗北シナリオ（読む用シナリオ集の該当の本）の**クライマックスか結末の一場面**を1枚にする。
シナリオの要約は `python3 /home/claude/w3/digest.py <読む用シナリオ集.txt> 350 1200` で28本の冒頭と終わりが読める（全文を読む必要はない。気になる本だけ本文を grep する）。
- 挿入（ペニバン・逆アナル）は、そのシナリオでその人物が実際に挿入する本だけ。女性の張形は `{"pen": "strapon"}`（道具なら `"toy"`）、ふたなり・NH が自分の体で入れる本は `{"pen": "penis"}`。
- 主人公が女装させられる本（女装娘のあるMODなど）は `{"hero_outfit": "..."}`（N47 Oiran の見本どおり、衣装の文字列を変数にまとめる）。
- 貞操帯の本は `{"cage": True}`。
- 行為文は英語25〜60語、カンマ区切りの短い句。相手は name の一部（"the maid", "the samurai" 等）で呼び、he/she だけで呼ばない。

### magic（5枚）
cfg.py の `magic` リスト（N61〜N75 は CFG['magic']、N76〜は tools/cfg.py の CFG['magic']）の no・名前・説明から、その魔法らしい一枚。
人物が使う魔法はその人物（マスターが多い）を出す。主人公は出さない（場面にしない）。罠や手紙・薬瓶などは人物なし（None）でもよい。

## 確認
書いたら `cd /home/claude/w3/画像生成 && python3 N61-N105_場面/build_new.py <Code> --check` を実行し、★（エラー）が出なくなるまで直す。
件数は 51枚（女装娘ありは52枚）。

## 資料の場所（MODごと）
- `/home/claude/src/N<番号>_<Code>_MOD/`
  - N61〜N75：`tools/cfg.py`（技・魔法・画像名）、`tools/chara.md`（キャラ表・得意技・オナニー）、`tools/plan.md`、`N.._構成表.md`（場所・経路ごとの流れ）、`N.._読む用シナリオ集.txt`
  - N76〜N105：`tools/cfg.py`（`from cfgkit import *` があるので読むだけにする）、`tools/brief.md`（世界観・場所・キャラ表・口調）、`tools/scen/*.txt`、`N.._読む用シナリオ集.txt`、`画像一覧.txt`
- キャラ設定シート全体（外見タグ案・得意技・オナニー）はプロジェクト文書 `claude/キャラクター設定_N61-N75_本編キャラ.md`・`claude/キャラクター設定_N76-N105.md` にもある（Projects ツールがあれば project_read。無ければ chara.md／brief.md で足りる）。
