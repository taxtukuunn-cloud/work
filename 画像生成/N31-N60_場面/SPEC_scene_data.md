# scene_data/<Code>.py の書き方（N31〜N60 画像生成・場面プロンプト）

目的：サキュバスデュエル（個人用MOD）の各MODに、ComfyUI（waiANIMA／anima系、Danbooruタグ＋英語の短文）で撮る
「技CG7・敗北CG28・オナニーCG5」＝40場面の英語プロンプトを作る。共通部分（品質タグ・主人公・ネガティブ）は
`build_scenes.py` が自動で付けるので、scene_data には **MOD固有の中身だけ** を書く。

**登場人物は全員20歳以上の成人**。主人公は紺髪（navy blue hair）で目が前髪で隠れた成人男性（160cm・細身・非筋肉質）。
責め手は常に上位で、主人公は受け身だけ（主人公が挿入する・責め返す・相手に触れて責める構図は絶対に書かない）。
暴力・流血・アヘ顔・凌辱なし。幼さを示す語（boy, girl単体, young, small, petite, little, kid など）は書かない。

## ファイルの形（Python。`DATA = {...}` だけ）

```python
# N31 湯守の宿（Onsen）場面データ。登場人物は全員20歳以上。
DATA = {
 "code": "Onsen",
 "world": "japanese hot spring inn in the mountains at night, rising steam, paper lanterns, detailed background",
 "chars": {
   # type: "woman"（女性・人外の女性）／"nh"（ニューハーフ＝見た目は女性で胸あり・自分のペニスあり）／"otoko"（男の娘＝平らな胸の女装男性）
   # tags: 既存の prompts\<Code>.json の立ち絵（<Code>_master / _e1 / _e2 / _e3 / _boss）の positive から、
   #       品質タグ・safe・solo・1girl/1boy と ポーズ・視線・full body・背景 を除いた「人物の見た目」部分をそのまま写す
   #       （女性/NH は "1girl" を含めない。男の娘は "adult male, otoko no ko, ..." を残し "woman"/"1girl" は書かない）
   # name: 場面文で使う短い呼び名（見た目で一意に分かる英語。例 the black-haired okami in a wisteria kimono）
   # neg:  （任意）その人物に固有のネガティブ（人魚なら "legs on the mermaid" など、立ち絵のネガから必要な物）
   "m":   {"type": "woman", "tags": "adult woman, mature female, ..., black hair, updo, red eyes, wisteria kimono, white apron, okami, large breasts",
           "name": "the black-haired okami in a wisteria kimono"},
   "e1":  {"type": "otoko", "tags": "adult male, otoko no ko, trap, ..., brown hair, short bob, amber eyes, green kimono, tasuki, nakai",
           "name": "the brown-bob nakai in a green kimono"},
   "e2": {...}, "e3": {...}, "boss": {...},
 },
 "places": {   # 場所キー → 英語の場所タグ（シナリオに出てくる場所。10〜16個）
   "roten": "rocky open-air hot spring, flat rock at the edge of the bath, river and red maple leaves, steam",
   "arai":  "washing area, wooden bath stool, wooden bucket, soap foam, steamed-up mirror",
   ...
 },
 # 技CG（そのキャラの技を受けている絵）。m1/m2/m3 はマスターの技1/2/3（cfg.py の master.techs の順）、
 # e1/e2/e3/boss は各モンスターの ★得意技（1つ目の技）。
 "atk": {
   "m1": ("roten", "he sits in the hot water leaning back against the rock, the okami kneels behind him whispering a song into his ear, her lips at his ear, his eyes hidden, trembling"),
   "m2": ("roten", "they sit in the bath, the okami holds his face and kisses him deeply, tongues, saliva trail"),
   "m3": ("okami_room", "from side, he lies on his back on the futon holding his knees, the okami kneels between his legs pegging his anus with her strap-on, anal, her other hand rubbing his nipple", {"pen": "strapon"}),
   ...
 },
 "atk_desc": {"m1": "the okami sings a thousand-night song into his ear.", ...},   # 7つ。場面を一言で（英語1文）
 # 敗北CG28：キーは btl_/onani_/inochi_/onedari_ × m1,m2,m3,e1,e2,e3,boss
 #  btl＝戦闘敗北／onani＝オナニー敗北（主人公が一人で相手の得意技をなぞる自慰。相手は遠くで見ているだけ）／
 #  inochi＝命乞い／onedari＝おねだり（主人公が自分からねだる）。それぞれのシナリオ（scen/<経路>_<責め手>.txt）の
 #  いちばん印象的な一場面（クライマックスまたは結末）を1枚の絵にする。
 "lose": {
   "btl_m1": ("roten", "...", {}),
   "onani_m1": ("guest_room", "kneeling alone on the futon, both hands covering his own ears, rocking, hips twitching, penis untouched, the okami sits by the shoji watching"),
   ...
 },
 "lose_desc": "makes him the inn's live-in husband.",   # 「<name> + この文」が敗北CGの最後に付く（MODの結末を英語一文で）
 # オナニーCG5（カードバトル中の自慰の立ち絵的な1枚）。相手の得意技に合わせた自慰。
 "onanie": {
   "master": ("roten", "kneeling in the shallow water, sucking two of his own fingers deeply as if kissing, the other hand rubbing his own nipple, penis untouched"),
   "e1": (...), "e2": (...), "e3": (...), "boss": (...),
 },
}
```

## 各場面の値
`(場所キー, 行為の英語, オプション辞書)` — オプションは省略可。
- `{"pen": "strapon"}`：女性がペニバンでお尻に挿入する絵（女性キャラのみ。ニューハーフは原則 "penis"）。
- `{"pen": "penis"}`：ニューハーフ／男の娘が自分のペニスで主人公のお尻に挿入する絵（逆アナル）。シナリオでそのキャラが自分の体で挿入するときだけ。
- `{"pen": "toy"}`：女性がバイブ・ディルド・アナルビーズ等の道具をお尻に入れる絵（ネガティブの strap-on/dildo を外すため）。
- 指・舌・管・ローター・触手など体以外は pen なしでよい（女性の道具は "toy"）。
- `{"cage": True}`：主人公のペニスが貞操帯（小さな銀のケージ）に入っている絵。
- `{"hero_outfit": "a scarlet furisode kimono with an obi, the kimono hem opened"}`：主人公が女装させられている絵（女装させられるシナリオのときだけ。書くと自動で crossdress 扱い）。
- `{"neg": "..."}`：その場面だけの追加ネガティブ。

## 行為文（action）の書き方 ― ここが品質を決める
- 英語で 25〜60語。**カンマ区切りの短い句**（Knight の例に合わせる）。
- 順序：`(from side など構図)`, 主人公の姿勢と場所, 相手の位置と何をしているか, 具体的な部位と道具, 小物, 表情/体液。
- 主語をはっきり：主人公は "he"、相手は name の一部（"the okami", "the nakai" 等）で呼ぶ。**相手を "he/she" だけで呼ばない**（役の入れ替わり防止）。
- 挿入の絵は必ず「主人公が受け（lies/kneels/bent over）、相手が上・後ろ」と書き、"his own penis separate" などで主人公のペニスが別にあることを示す。
- ペニバン・逆アナルは技の説明どおり（挿入は指でほぐした後＝絵ではほぐしは描かなくてよい）。
- 相手は服を着たまま（build 側でも付くが、脱いでいる描写を書かない）。人外（蜘蛛・ラミア・人魚・竜など）の体の特徴は tags にあれば自動で入る。糸・尻尾・触手で縛る等はOK。
- 主人公の目は前髪で隠れている（"eyes closed" 等は書かない）。
- **onani（敗北のオナニー経路）と onanie（オナニーCG）**：主人公が一人で、その相手の得意技をなぞる自慰（乳首・お尻に指・自分の指をしゃぶる・耳をふさぐ・足裏で自分を… 等）。**ペニスは触らない**（"penis untouched"）。相手は遠くで見ているだけ。安易に手でしごく絵にしない。
- 数字・文字・看板・ラベルは描かれないように "without text" を付ける（本・帳面・札・カードなど）。
- 3人以上を出さない（その場面の責め手1人＋主人公だけ）。

## 手順
1. `cfg.py`（技名・タイプ・得意技）、`brief.md` または `*_構成表.md`（世界観・場所・キャラ・経路ごとの流れ）を読む。
2. `*_読む用シナリオ集.txt`（28本）を各本ざっと読み（導入400字＋クライマックス付近）、1本ごとに1場面を決める。
   N46〜N60 は `tools/scen/<経路>_<責め手>.txt` も同じ内容。
3. 立ち絵の tags は `prompts_in/<Code>.json` から写す。
4. `python build_scenes.py <Code> --check` がエラーなく 40件 を出すことを確認（build は /home/claude/w/tool で動かす）。
