# -*- coding: utf-8 -*-
"""MOD画像 一括生成ツール（2026-09-26 改：sdduel_style-000006 を直接組み込み／全MOD一括）
使い方:
  python gen.py <MODコード|all|コード,コード,...> [all|名前の一部,名前の一部...] [オプション]
    例) python gen.py all                 … 全MOD・全画像（撮り済みは飛ばす）
        python gen.py Host,Heels          … 2つのMODの全画像
        python gen.py Host lose_btl --random --redo  … Host の lose_btl を撮り直し
  オプション:
    --random          シードをランダムにする（撮り直し用）
    --batch N         1回に N 枚ずつ候補を作る
    --redo            撮り済みの画像も撮り直す（既定は撮り済みを飛ばす）
    --no-lora         LoRA を使わない
    --lora-strength X 絵柄LoRAの強さ（既定は lora.json の値）
    --no-hero         主人公LoRAを使わない
    --dry-run         送らずに件数だけ表示
    --hero-strength X 主人公LoRAの強さ（0で外す）
    --no-face-fix     相手の顔を見せるタグを自動で足さない
    --face-level 1/2/3 相手の顔の対策（1=顔タグ 2=＋目の色・分けた前髪〈既定〉 3=＋ネガに hair over eyes）
    --eyes-text keep  主人公の目隠れを文字でも書く（旧方式。既定 strip は主人公LoRAに任せる）
    --seed N / --out 名前   シード固定・保存先フォルダ名（比較用）
    --hero-age mature 主人公の年齢を旧方式で（既定 fresh＝老け顔対策：20歳・fresh face に言い換え＋ネガに老け顔）
    --model wai|anima 使うモデル（既定は model.json。wai＝waiIllustriousSDXL_v170／anima＝waiANIMA_v10Base10）
    --sdxl-lora-strength X  wai で重ねる LoRA（anime_screencap-IL-NOOB_v3 など）の強さを一時的に変える（0で外す）
    --add-lora 名前:強さ[:トリガー]  wai に LoRA を一時的に足す（例 sdduel_style_xl-000006:0.6:sdduel style）
    --no-pose         構図LoRA（model.json の pose_loras）を一時的に外す
    --pose-scale X    構図LoRAの強さを一時的に X 倍にする
    --pose-report     ComfyUI に送らず、割当結果を 構図LoRA_割当.csv に書き出して件数を表示
    --pose-sample N   構図LoRAごとに場面を N 件選び、同じシードで「あり／なし」を output\構図LoRA比較\<id>\ に撮る
    --style-compare   本編の絵柄LoRAを候補（STYLE_CANDS の6条件）に差し替えて、4枚×2シードを output\絵柄比較\<条件>\ に撮り、
                      撮り終わったら一覧画像（一覧_1_立ち絵.png など）を作る。model.json の標準設定は変えない
    --style-grid      絵柄比較の一覧画像だけ作り直す
    --style 名前      絵柄割当.csv を無視してこの絵柄で撮る（例 --style ATRex）。保存先 <MOD>_WAI_<絵柄>
    --style-list      使える絵柄・絵柄別の主人公LoRAの有無・MODごとの割当を表示
    --no-mod-style    絵柄割当.csv を使わない（今までどおり <MOD>_WAI）
    --no-chara / --chara-strength X  イベントの敵キャラLoRA（loras\キャラ\chr_<MOD>_<キャラ>_<絵柄>-000008）を外す／強さを変える
・LoRAの使い分け（2026-09-29）：立ち絵＝絵柄LoRA（＋主人公の立ち絵は主人公LoRA）。
  イベント（2人の場面）＝絵柄LoRA＋主人公LoRA（hero_scene_strength 0.5）＋相手の敵キャラLoRA（chara_scene_strength 0.6）＋構図LoRA。
    --random-style [all]  絵柄割当.csv が空欄のMODに絵柄をランダムに割り当てて保存（all＝対象MODを全部振り直す）
・MODごとの絵柄（2026-09-29）：絵柄割当.csv の「絵柄」列に絵柄名（ATRex など）を書いたMODは、
  本編の絵柄LoRAの代わりにその絵柄LoRA、主人公LoRAの代わりに その絵柄で学習した sdduel_hero_xl_<絵柄>-000008 を使い、
  output\<MOD>_WAI_<絵柄>\ に撮る（主人公LoRAがまだ無い絵柄は主人公LoRAなし）。中身は mod_style.py／model.json の mod_style
・構図LoRA（2026-09-28）：2人の場面だけ、最終プロンプトを pose_loras の when で判定して
  action を1つ（上から最初に当てはまったもの）＋ look を1つまで LoraLoader で足す。
  トリガーは受け攻めタグの直後、neg はネガの末尾。立ち絵・背景・オナニー（主人公ひとり）には入れない。
・モデル切替（2026-09-27）：model.json の "model" で決まる。wai（SDXL）のときは
  - 出力は ComfyUI\output\<MODコード>_WAI\（Anima の <MODコード>_自作\ とは別。撮り済み判定も別）
  - sdduel_style / sdduel_hero の LoRA は Anima 用なので使わない（SDXL では効かない）
  - プロンプトの score_9/8/7 を外し、安全タグ safe を general に言い換え、品質ネガを足す
・プロンプト: prompts\<MODコード>.json  → 出力: ComfyUI\output\<MODコード>_自作\
・LoRA は同じフォルダの lora.json（sdduel_style-000006・0.6 ＋ 主人公が出る絵だけ sdduel_hero-000004・0.8）。
  Downloads\Lora用\lora_settings.json（共通設定）が bbishop 等に切り替わっていても影響を受けない。
・ComfyUI のキューに一度に全部は積まず、少しずつ送る（ウィンドウを閉じれば止まる。次回は続きから）。
・登場人物はすべて成人。幼く見える絵を避けるタグを毎回ネガティブに必ず足す（このツールでは外せない）
"""
import argparse, hashlib, json, os, random, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:   # ComfyUI 付属の Python は gen.py のフォルダを探さない（mod_style.py・solo_onanie.py を読むため）
    sys.path.insert(0, HERE)
SERVER = "http://127.0.0.1:8188"
OUTROOT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
ADULT_NEG = ("child, loli, shota, young boy, young girl, kid, teenage, underage, immature, childlike, child body, "
             "youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, flat-chested child")
ADULT_POS = "adult male, mature face, adult proportions"
# 2026-09-29 主人公は 160cm・20歳以上の成人（2026-10-02 年齢点検で「19歳」の書き間違いを直した）（ユーザー決定）。プロンプトには年齢の数字を書かない（10代の見た目に寄るため）→ 「若い成人・大人の顔」で表す
# 2026-09-29 成人強化（裸の場面で子どもの体型に寄ったため）：大人の顔・骨格・体つきをはっきり書く。細さの重ね書きはしない
ADULT_POS_FRESH = ("adult male, mature adult face, defined jawline, adam's apple, adult male body, adult body proportions, "
                   "slim adult build, not muscular")   # 2026-09-29「筋肉質すぎ」→ lean toned body・defined collarbones を外す
ADULT_BODY_NEG = ("petite, small body, skinny, underdeveloped body, child proportions, short torso, large head, "
                  "boyish body, hairless child body")
# 主人公と一緒の場面：主人公の「目隠れ」が相手にうつるのを防ぐ（2026-09-26）
FACE_POS = ("the other character's face is fully visible, the other character's eyes are clearly visible and open, "
            "detailed eyes on the other character")
FACE_NEG = ("faceless female, faceless attacker, both characters faceless, hidden eyes on the other character, "
            "bangs covering eyes on the woman, bangs covering eyes on the attacker, eyes out of frame, "
            "head out of frame, face cropped, face turned away completely")
# 長いプロンプトでは後ろの指定が効きにくいので、場面の要点を先頭に短く入れる（2026-09-26 Android で
# 男の娘が胸の大きい女性になる／主人公が相手の白衣やボディスーツを着る／髪色が入れ替わる、が出たため）
FEMBOY_POS = ("the dominant one is a feminine adult man (otoko no ko) with a completely flat male chest and no breasts, "
              "fully clothed in his own outfit")
FEMBOY_NEG = "1girl, woman, female body, breasts, large breasts, cleavage"
NAKED_POS = ("the navy-haired man is completely naked and wears nothing, "
             "the naked navy-haired man is the one being touched and lies back passively, "
             "the other character is fully dressed, looks at him with open eyes and does all the touching")
NAKED_NEG = ("the other character naked, the other character undressed, the other character's bare chest, "
             "the navy-haired man clothed, the navy-haired man touching the other character, clothes on the naked man, the naked man wearing a lab coat, the naked man wearing a bodysuit, "
             "the naked man wearing a uniform, the naked man wearing the other character's clothes")
HERO_POS = "the navy-haired man is a grown adult man in his mid twenties with an adult male build, navy blue hair"
HERO_POS_FRESH = ("the navy-haired man is an adult man with a mature adult face, defined jawline, adam's apple and a slim, not muscular adult male body, "
                  "navy blue hair")
HERO_NEG = "navy blue hair on the other character, both with the same hair color, black hair on the navy-haired man"
# 相手の目が前髪で隠れる対策 その3（2026-09-26 Android_atk_e1 の緑髪で再発）：
# 相手の目の色をプロンプトから拾って先頭に書き、前髪を分けておでこを見せる
COLORS = ("red|crimson|scarlet|pink|magenta|purple|violet|lavender|blue|light blue|aqua|cyan|teal|green|emerald|"
          "yellow|gold|golden|amber|orange|brown|grey|gray|silver|black|white|heterochromia")
EYE_RE = re.compile(r"\b((?:glowing |bright |deep |pale |light |dark )?(?:%s) eyes)\b" % COLORS)
BANGS_POS = "the other character has parted bangs with the forehead visible"
EYES_NEG_HARD = "hair over eyes, bangs covering eyes, eyes hidden by hair"
FACE_LEVEL = 2   # 0=相手の顔タグなし 1=顔タグのみ 2=＋目の色・分けた前髪（既定） 3=＋ネガに hair over eyes
# 主人公が女装させられる場面：服が相手と入れ替わるのを防ぐ（2026-09-26 Auction_lose_onedari_e1 で入れ替わり）
DRESS_POS = ("only the navy-haired man is crossdressed, the other character keeps their own outfit on and never wears his clothes, "
             "the navy-haired man is the one being dressed up and handled")
DRESS_NEG = ("clothing swap, swapped outfits, both wearing dresses, the other character wearing the navy-haired man's outfit, "
             "the navy-haired man wearing the other character's outfit, the other character in a sheer dress, "
             "the other character wearing garter stockings")
# 主人公の「目隠れ」を文字で書くと相手に移る（2026-09-26 Maid_lose_onedari_m2 の比較で確認：
# 主人公LoRAなしだと主人公の目は見え、相手の目が隠れた）→ 主人公LoRAを使うときは文字の指定を外してLoRAに任せる
import re as _re
HIDE_RE = _re.compile(r",\s*(faceless male|hair over (?:his )?eyes|bangs covering (?:his )?eyes|eyes completely covered by hair|no visible eyes)(?=\s*,|\s*$)")
# ネガティブの「主人公の目が見える」（visible eyes on the shorter man 等・全場面の約1,100件）は
# 「見える目」そのものを打ち消し、相手の目まで隠していた（2026-09-26 Android_atk_e1 比較3で3方式とも失敗）→ 外す
NEG_EYES_RE = _re.compile(r",\s*(?:visible eyes|eyes visible) on (?:the )?(?:shorter |small |smaller |navy-haired )?man(?=\s*,|\s*$)")
# 主人公の「目を閉じる」も相手に移るので外す（主人公の目は前髪で見えないため不要）
SHUT_RE = _re.compile(r",\s*(?:eyes squeezed shut|eyes closed|closed eyes)(?=\s*,|\s*$)")
EYES_TEXT = "strip"   # strip＝文字の目隠れ指定を外す／keep＝そのまま（旧方式）
# 主人公の顔を描く（2026-09-28 ユーザー決定）：目隠れの指定を外し、水色の目（他キャラと被りにくい色）・目にかからない前髪にする。
# model.json の "hero_face": {"show": false} で旧方式（目を隠す）に戻せる。
HERO_FACE = {"show": True, "eyes": "aqua eyes", "bangs": "short bangs above the eyes",
             # 2026-09-28 「ちょっとごつい」→ 細い体つきを足す（成人の指定はそのまま）
             # 2026-09-29 160cm・20歳以上の成人（2026-10-02 年齢点検で「19歳」の書き間違いを直した）：幼く見えやすい語（bishounen・delicate features・thin arms）を外す
             # 2026-09-29 成人強化：細さの重ね書き（slender・narrow shoulders・slim waist）と、大人の骨格を消すネガ（manly・square jaw 等）をやめる
             "build": "slim adult male build, adult male body, not muscular",   # 2026-09-29「筋肉質すぎ」で調整
             "build_neg": "muscular, abs, pectorals, toned body, thick arms, thick neck, stocky, bulky muscles, bara",
             # 2026-09-28 「肌が色白すぎ」→ プロンプトの smooth pale skin（主人公の人物ブロック・約1,700件）を言い換え
             "skin": "natural healthy skin tone, warm skin color",
             "skin_neg": "pale skin on the navy-haired man, pasty white skin on the navy-haired man"}   # 敵キャラ（吸血鬼・雪女など）の白い肌は消さないよう主人公だけに限定
FACE_HIDE_RE = _re.compile(r"([,:])\s*(?:faceless male|faceless man|hair over (?:his )?eyes|bangs covering (?:his )?eyes|"
                           r"eyes completely covered by hair|no visible eyes|eyes not visible|eyes hidden(?: by bangs)?)(?=\s*,|\s*$)")
FACE_HIDE_INLINE_RE = _re.compile(r"\s*with (?:his )?eyes hidden(?: by bangs)?")
HERO_HAIR_RE = _re.compile(r"\b(navy blue hair|dark blue hair)\b")
# 主人公が老けて見える対策（2026-09-27）：プロンプト中の主人公の年齢の書き方を、実行時に若い成人向けに言い換える。
# 全MODの prompts\*.json はそのまま（ファイルは書き換えない）。--hero-age mature で旧方式（言い換えなし）。
# 成人であることは変えない（25→20歳〈プロジェクト設定の下限〉・幼さを防ぐネガティブ ADULT_NEG はそのまま毎回付く）。
HERO_AGE = "fresh"
AGE_SUBS = [
    # 主人公の人物ブロック（全MODで共通の書き方・約2,200件）
    # 2026-09-29 160cm・20歳以上の成人（2026-10-02 年齢点検で「19歳」の書き間違いを直した）（年齢の数字は書かず「若い成人・大人の顔」）
    (re.compile(r"adult man, mature male, 25 years old, adult male body,"),
     "adult man, mature adult face, handsome face, defined jawline, adam's apple, adult male body,"),
    (re.compile(r"(slim adult build, lean, not muscular, (?:no muscles, )?)defined jawline"), r"\1slim smooth jawline"),
    # 場面の最後に付く主人公の年齢（約630件）
    (re.compile(r"adult male, 20s, mature face, adult proportions"), "adult male, young adult man, adult face, adult proportions"),
    # 女装娘の立ち絵（Oiran・Lingerie・Revue の _josou）
    (re.compile(r"adult man, 20s, mature face,"), "adult man, young adult man, adult face, handsome face,"),
]
def age_face(s):
    """2026-09-29 若めの大人（20代前半）：model.json の hero_face の age_face／age_jaw で、主人公の顔の年齢の書き方
    （mature adult face／defined jawline）を差し替える。無ければ今までどおり。大人の目印（adam's apple・adult male body）と
    子どもの体型を避けるネガ（ADULT_NEG・ADULT_BODY_NEG）はそのまま"""
    f, j = HERO_FACE.get("age_face"), HERO_FACE.get("age_jaw")
    if f:
        s = s.replace("mature adult face", f)
    if j:
        s = s.replace("defined jawline", j)
    return s


AGE_NEG = ("old man, middle-aged man, aged face, older face on the navy-haired man, wrinkles, crow's feet, nasolabial folds, "
           "eye bags, dark circles under eyes, tired face, sunken cheeks, receding hairline, grey hair on the navy-haired man, stubble on the navy-haired man, beard, mustache")
DEFAULT_LORA = {
    "style": {"enabled": True, "lora_name": "sdduel_style-000006.safetensors", "strength": 0.6, "trigger": "sdduel style"},
    "hero": {"enabled": True, "lora_name": "sdduel_hero-000004.safetensors", "strength": 0.8, "trigger": "sdduel_hero",
             "when_text_contains": "navy"},
}
QUEUE_MAX = 6   # ComfyUI に積んでおく最大数
# 受け攻めの入れ替わり対策（2026-09-28 ユーザー指摘「相手キャラが受けになっている構図が多い」）：
# SDXL は長い英文の役割指定が効きにくいので、Danbooru の短いタグで「相手が攻め・主人公が受け」を一番先頭に置く。
# model.json の "role_fix": false で外せる。
ROLE_FIX = True
ROLE_POS = {
    "woman": "femdom, dominant woman, submissive man, the woman is in control, the navy-haired man is on the receiving end",
    "newhalf": "femdom, dominant newhalf, submissive man, the newhalf is in control, the navy-haired man is on the receiving end",
    "femboy": "dominant otoko no ko, submissive man, the otoko no ko is in control, the navy-haired man is on the receiving end",
}
ROLE_NEG = ("maledom, male dominant, submissive woman, submissive girl, woman being dominated, woman on the receiving end, "
            "the navy-haired man on top, the navy-haired man in control, the navy-haired man pinning, "
            "the navy-haired man touching the other character, the other character lying under the navy-haired man, "
            "the other character embarrassed and submissive, role reversal")
SKIP_ONANIE = False  # 2026-09-29 ユーザー決定：オナニー場面（画像名に onani を含む）は当面撮らない。model.json の skip_onanie で切り替え
SOLO_ONANIE = True   # オナニー場面は主人公ひとり（2026-09-28 ユーザー決定：相手が遠くで見ている構図をやめる）。solo_onanie.py で変換
# ---- 構図LoRA（2026-09-28）。設定は model.json の "pose_lora" と "pose_loras" ----
POSE_CFG = {"enabled": False, "max_action": 1, "allow_look_extra": True, "apply_to": ["scene"], "override": {}}
POSE_LIST = []           # model.json の pose_loras（when は正規表現にしておく）
NO_POSE = False          # --no-pose
POSE_SCALE = 1.0         # --pose-scale
POSE_HAVE = None         # ComfyUI の LoRA 一覧（/object_info で確認後。None なら確認しない）
POSE_MISSING = set()     # ComfyUI に無かった構図LoRA
LAST_POSE = {}           # 直前の wf() の割当（--pose-report 用）


def load_pose(mj):
    """model.json の pose_lora / pose_loras を読む。when の正規表現が壊れていたらその項目だけ外す。"""
    global POSE_LIST
    if isinstance(mj.get("pose_lora"), dict):
        POSE_CFG.update(mj["pose_lora"])
    out = []
    for p in mj.get("pose_loras") or []:
        if not isinstance(p, dict) or not p.get("id"):
            continue
        if not p.get("file") and p.get("enabled") is not False:   # 下書きだけの判定項目（無効・file なし）は読む
            continue
        try:
            p = dict(p, _when=[re.compile(w, re.I) for w in p.get("when") or []],
                     _extra=[dict(x, _rx=re.compile(x["when"], re.I)) for x in p.get("extra") or []])
        except re.error as ex:
            print("(構図LoRA %s の when が正規表現として読めないので外します: %s)" % (p.get("id"), ex)); continue
        out.append(p)
    POSE_LIST = out


def pose_match(p, text):
    """when をすべて満たせば当てはまった語の一覧、満たさなければ None。"""
    if not p["_when"]:
        return None
    hits = []
    for rx in p["_when"]:
        m = rx.search(text)
        if not m:
            return None
        hits.append(m.group(0))
    return hits


def pick_pose(name, text):
    """場面の最終プロンプトから構図LoRAを選ぶ。戻り値 [(項目, 当てはまった語), ...]（action → look の順）"""
    if NO_POSE or not truthy(POSE_CFG.get("enabled")) or not POSE_LIST:
        return []
    ov = (POSE_CFG.get("override") or {}).get(name)
    if ov:
        if str(ov).lower() == "none":
            return []
        for p in POSE_LIST:
            if p["id"] == ov:
                return [(p, ["override"])]
        print("  (override の構図LoRA id「%s」が pose_loras にありません: %s)" % (ov, name))
        return []
    picked = []
    for kind, limit in (("action", int(POSE_CFG.get("max_action", 1))),
                        ("look", 1 if truthy(POSE_CFG.get("allow_look_extra", True)) else 0)):
        n = 0
        for p in POSE_LIST:
            if n >= limit:
                break
            if p.get("kind", "action") != kind or p.get("enabled") is False:
                continue
            if any(q["file"] == p["file"] for q, _ in picked):
                continue
            hits = pose_match(p, text)
            if hits:
                picked.append((p, hits)); n += 1
    return picked


def pose_file(p):
    """ComfyUI の一覧に出る形（区切り \\ か /）に合わせたファイル名。無ければ None。"""
    f = p["file"]
    if POSE_HAVE is None:
        return f
    for c in (f, f.replace("\\", "/"), f.replace("/", "\\")):
        if c in POSE_HAVE:
            return c
    return None


def partner_kind(p):
    """場面の相手の種類（女性／ニューハーフ／男の娘）。判定できなければ woman。"""
    if "newhalf" in p:
        return "newhalf"
    if ("femboy" in p or "otoko no ko" in p) and "1girl" not in p and "woman" not in p:
        return "femboy"
    return "woman"
# ---- モデル設定（2026-09-27 追加）。model.json で上書きできる ----
MODELS = {
    "anima": {"label": "WAI-Anima（waiANIMA_v10Base10）", "loader": "unet", "unet_name": "waiANIMA_v10Base10.safetensors",
              "clip_name": "qwen_3_06b_base.safetensors", "vae_name": "qwen_image_vae.safetensors",
              "steps": 36, "cfg": 4.5, "sampler": "er_sde", "scheduler": "simple", "out_suffix": "_自作", "lora": True},
    "wai": {"label": "WAI-Illustrious SDXL v17（waiIllustriousSDXL_v170）", "loader": "ckpt",
            "ckpt_name": "waiIllustriousSDXL_v170.safetensors", "clip_skip": -2,
            "steps": 28, "cfg": 6.0, "sampler": "euler_ancestral", "scheduler": "normal", "out_suffix": "_WAI", "lora": False,
            "quality_pos": "masterpiece, best quality, amazing quality",
            "quality_neg": "bad quality, worst quality, worst detail, sketch, censor",
            # 2.5次元っぽさを消してアニメ塗りに寄せる（2026-09-27）
            "style_pos": "anime screencap, anime coloring, cel shading, flat color",
            "artist": "",   # 好みの絵師名タグ（1〜2個・カンマ区切り）。空なら入れない
            "style_neg": "realistic, photorealistic, 3d, semi-realistic, lips, nose shine, detailed skin, skin texture",
            "neg_remove": ["flat color", "thick outline"],   # アニメ寄せの邪魔になるのでネガから外す
            # SDXL（Illustrious/Noob）用の LoRA を重ねる（2026-09-27）。strength=モデル側、clip_strength=CLIP側
            "loras": [{"lora_name": "anime_screencap-IL-NOOB_v3.safetensors", "strength": 0.8, "clip_strength": 0.8, "trigger": ""}]},
}
MODEL = MODELS["wai"]
SCORE_RE = re.compile(r",\s*score_\d(?:_up)?(?=\s*,|\s*$)")


def load_model(name=None):
    """model.json（{"model": "wai"} など）を読む。--model があればそちらを優先。"""
    u = {}
    try:
        u = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    except FileNotFoundError:
        pass
    except Exception as e:
        print("(model.json が読めないので wai を使います:", e, ")")
    key = (name or u.get("model") or "wai").strip().lower()
    if key not in MODELS:
        print("[中止] model は wai か anima を指定してください（今の値: %s）" % key); sys.exit(1)
    m = dict(MODELS[key]); m["key"] = key
    if isinstance(u.get(key), dict):
        m.update(u[key])
    return m


SDXL_LORA_STRENGTH = None   # --sdxl-lora-strength で一時的に上書き（0 で外す）
ADD_LORAS = []              # --add-lora ファイル名:強さ[:トリガー[:hero]] で一時的に足す（比較用）
CUR_TEXT = None             # 今組み立て中の画像の positive（when_text_contains の判定用。None なら判定しない）
CUR_SCENE = False           # 今組み立て中の画像が2人の場面か（scene_strength の判定用）
HERO_SCENE_STRENGTH = None  # --hero-scene-strength で一時的に上書き
# ---- 絵柄LoRAの差し替え比較（2026-09-28）。--style-compare で本編の絵柄LoRA（sdduel_style*）を外して候補1枚に差し替える ----
STYLE_SWAP = None           # None＝model.json のまま／{"lora_name": ..., "strength": ..., "trigger": ...}／{}＝絵柄なし
STYLE_BASE = "sdduel_style"  # 差し替えで外す本編の絵柄LoRA（lora_name の先頭）
STYLE_CANDS = [   # (フォルダ名, LoRA ファイル, 強さ, トリガー)。トリガーは モデル\一覧.txt で確認したもの
    ("1_現行", "sdduel_style_xl-000008.safetensors", 0.5, "sdduel style"),
    ("2_絵柄なし", None, 0, ""),
    ("3_ATRex", "絵柄\\ATRex_style-12V2Rev.safetensors", 0.6, "trexstyle"),
    ("4_Mosouko", "絵柄\\[Style] Mosouko [Illustrious-XL].safetensors", 0.6, "mo85ko"),
    ("5_GEN", "絵柄\\GEN(illust) 0.2v.safetensors", 0.6, ""),
    ("6_IFL", "絵柄\\IFL_v1.0_IL.safetensors", 0.6, ""),
    # 2026-09-29：本編の絵柄LoRAを、年齢に関わる自動タグの17枚を除いて学習し直した版（Lora用\3_学習_SDXL_v2.bat）
    ("7_本編v2", "sdduel_style_xl_v2-000008.safetensors", 0.5, "sdduel style"),
    ("8_本編v2強", "sdduel_style_xl_v2-000008.safetensors", 0.8, "sdduel style"),
    # 2026-09-29 追加分（モデル\一覧.txt で確認：どれも学習タグに年齢系なし・トリガーあり）
    ("9_Bose", "絵柄\\Bose__Loose_-_Femdom_Style.safetensors", 0.6, "bose"),
    ("10_Hisano", "絵柄\\Hisano_-_Femdom_Style.safetensors", 0.6, "hisano"),
    ("11_Minamoto", "絵柄\\Minamoto_Mutton_-_Femdom_Style.safetensors", 0.6, "minamoto"),
    ("12_Otochichi", "絵柄\\Otochichi_2019_-_Femdom_Style_Illustrious.safetensors", 0.6, "otochichi_(modern)"),
    ("13_DHIBI", "絵柄\\DHIBI_Style_IL.safetensors", 0.6, "dh1b1"),   # 白黒漫画の絵柄（monochrome 910/932枚）
    ("14_Dishwasher", "絵柄\\Dishwasher_1910_Style-IL.safetensors", 0.6, "pkdish"),
    ("15_DishwasherLoHa", "絵柄\\dishwasher1910XL_il_loha_V8340.safetensors", 0.6, ""),   # LoHa 形式・トリガーなし
    ("16_ahemaru", "絵柄\\ahemaru_777.safetensors", 0.6, ""),   # トリガーなし。学習タグに shota 2/282枚
    # 2026-09-29 追加分その3（モデル\一覧.txt。navier haruka は shota 系が 12〜20% のため入れない）
    ("17_WadaArco", "絵柄\\Wada Arco[style]-Illus.safetensors", 0.6, "wada arco style"),   # aged down 5・child 4 /750
    ("18_KNAI", "絵柄\\K NAI Style.safetensors", 0.6, ""),   # loli 5・onee-shota 1 /745
    ("19_matureBody", "絵柄\\mature body.safetensors", 0.6, "mature body"),   # 絵柄ではなく体型（大人の体つき）LoRA
    ("20_DishwasherV2", "絵柄\\Dishwasher1910-v2.safetensors", 0.6, ""),   # メタデータなし
    ("21_hews", "絵柄\\hews_style_ilxl_goofy.safetensors", 0.6, ""),   # 学習タグなし
    ("22_Shexyo", "絵柄\\Shexyo_-_Illustrious_2025_style-000014.safetensors", 0.6, ""),
    ("23_BlueGK", "絵柄\\Artist_StyleBlue_GK__illustrious.safetensors", 0.6, "blue_gk"),
    ("24_ToLoveRuD", "絵柄\\toloverudarkness_illustrious_msp-000020.safetensors", 0.6, ""),   # トリガーは masterpiece（品質タグで常に入る）。loli 18 等 /2162
    ("25_Yabuki", "絵柄\\Yabuki Kentarou_v3_illustriousXL.safetensors", 0.6, "yabuki kentarou style"),   # child 8・loli 8 等 /2509
    # 2026-09-29 追加分その4（shinjiro は shota 系が 16〜28% のため入れない）
    ("26_Toridamono", "絵柄\\ToridamonoIL.safetensors", 0.6, ""),   # トリガーなし。reisalin stout 72/115 とキャラに寄る恐れ
    ("27_ebora", "絵柄\\ebora_style2-000070.safetensors", 0.6, ""),   # LoKr 形式・トリガーなし。loli 15・onee-shota 3・shota 2 /238
    # 2026-09-29 追加分その5（どれも年齢系は boy on top＝体位のタグのみ）
    ("28_YoukosoElf", "絵柄\\Youkoso_Sukebe_Elf_No_Mori_E.safetensors", 0.6, "youkoso_elfstyle"),   # elf・pointy ears 393/528 → 耳がとがる恐れ
    ("29_cgelRichy", "絵柄\\cgel-style-richy-v1_ixl.safetensors", 0.6, ""),   # アイライン強めの画風・トリガーなし
    ("30_Raita", "絵柄\\Raita.safetensors", 0.6, "r41t4sknsfw"),
    ("31_HGK", "絵柄\\HGK_Style.safetensors", 0.6, "hgk"),
]
# ---- MODごとの絵柄（2026-09-29）。絵柄割当.csv で MOD ごとに絵柄LoRA＋その絵柄で学習した主人公LoRA を使う（mod_style.py） ----
CUR_STYLE = None     # 今組み立て中の画像の絵柄（mod_style の preset。None＝model.json のまま）
NO_STYLE_HERO = False  # --no-hero で絵柄別の主人公LoRAも外す
# 敵キャラLoRA（2026-09-29）：イベント（2人の場面）だけ、その場面の相手キャラのLoRAを入れる（立ち絵は絵柄LoRAだけ）
CUR_CHARA = None       # 今組み立て中の画像の相手キャラLoRA（mod_style.chara_lora の dict）
NO_CHARA = False       # --no-chara
CHARA_STRENGTH = None  # --chara-strength
STYLE_PICS = [("1", "立ち絵"), ("2", "ペニバン"), ("3", "キス"), ("4", "主人公")]
STYLE_DIR = "絵柄比較"


def sdxl_loras():
    """wai（SDXL）で重ねる LoRA の一覧。strength が 0 以下のものは使わない。
    "when_text_contains": "navy" があれば、その語を含む絵（主人公が出る絵）だけに使う。
    "role": "hero" は主人公LoRA（使う場面では主人公の目隠れの文字指定を外して LoRA に任せる）。"""
    if MODEL.get("loader") != "ckpt":
        return []
    out = []
    base = list(MODEL.get("loras") or [])
    if CUR_STYLE:   # MODごとの絵柄：本編の絵柄LoRA・共通の主人公LoRA を外して、その絵柄の LoRA と主人公LoRA に差し替える
        base = [x for x in base if isinstance(x, dict) and not (str(x.get("lora_name", "")).startswith(STYLE_BASE)
                                                                or x.get("role") == "hero")]
        if CUR_STYLE.get("lora"):
            base.append({"lora_name": CUR_STYLE["lora"], "strength": CUR_STYLE["strength"],
                         "clip_strength": CUR_STYLE["strength"], "trigger": CUR_STYLE.get("trigger", "")})
        if CUR_STYLE.get("hero_ok") and not NO_STYLE_HERO:
            # 2026-09-30 2人の場面は hero_scene_lora（浅いエポック）があればそちらを使う（女性キャラが主役・主人公は投影用）
            hl = CUR_STYLE["hero_scene_lora"] if (CUR_SCENE and CUR_STYLE.get("hero_scene_ok")) else CUR_STYLE["hero_lora"]
            base.append({"lora_name": hl, "strength": CUR_STYLE["hero_strength"],
                         "clip_strength": CUR_STYLE["hero_strength"], "trigger": CUR_STYLE.get("hero_trigger", "sdduel_hero"),
                         "when_text_contains": "navy", "role": "hero", "scene_strength": CUR_STYLE.get("hero_scene_strength")})
    if CUR_CHARA and CUR_CHARA.get("ok") and (CUR_SCENE or CUR_CHARA.get("stand")) and not NO_CHARA and not (CUR_SCENE and CUR_CHARA.get("scene_lora") is False):   # scene_lora false＝場面では使わない（2026-10-02）   # イベントの相手キャラLoRA（chara_map は立ち絵にも）
        st = CHARA_STRENGTH if CHARA_STRENGTH is not None else (CUR_CHARA.get("scene_strength", CUR_CHARA["strength"]) if CUR_SCENE else CUR_CHARA["strength"])
        base.append({"lora_name": CUR_CHARA["lora_name"], "strength": st, "clip_strength": st,
                     "trigger": CUR_CHARA.get("trigger", ""), "role": "chara"})
    for L in base:
        if not isinstance(L, dict) or not L.get("lora_name") or L.get("enabled") is False:
            continue
        L = dict(L)
        if SDXL_LORA_STRENGTH is not None:
            L["strength"] = SDXL_LORA_STRENGTH; L["clip_strength"] = SDXL_LORA_STRENGTH
        # 2人の場面では主人公LoRAを弱める（2026-09-28「場面で主人公と相手の顔が同じになる」対策：
        # LoRA は画面全体に効くので、強いと相手の顔まで主人公の顔になる。立ち絵は単独なので起きない）
        if CUR_SCENE and L.get("role") == "hero":
            ss = HERO_SCENE_STRENGTH if HERO_SCENE_STRENGTH is not None else L.get("scene_strength")
            if ss is not None:
                L["strength"] = float(ss); L["clip_strength"] = float(ss)
        if float(L.get("strength", 0.8)) <= 0:
            continue
        w = L.get("when_text_contains")
        if w and CUR_TEXT is not None and w.lower() not in CUR_TEXT.lower():
            continue
        out.append(L)
    if STYLE_SWAP is not None:   # --style-compare：本編の絵柄LoRAを外して候補に差し替える（anime_screencap・主人公はそのまま）
        out = [x for x in out if not x["lora_name"].startswith(STYLE_BASE)]
        if STYLE_SWAP.get("lora_name"):
            out.append({"lora_name": STYLE_SWAP["lora_name"], "strength": STYLE_SWAP["strength"],
                        "clip_strength": STYLE_SWAP["strength"], "trigger": STYLE_SWAP.get("trigger", "")})
    names = {L["lora_name"] for L in out}
    for L in ADD_LORAS:
        if L["lora_name"] in names:   # 同じものが model.json にあれば置き換える
            out = [x for x in out if x["lora_name"] != L["lora_name"]]
        if float(L["strength"]) > 0:
            out.append(dict(L))
    return out


def adapt_prompt(pos, neg):
    """SDXL（Illustrious）向けにプロンプトを少し直す。prompts\*.json は書き換えない。"""
    if MODEL["key"] != "wai":
        return pos, neg
    pos = SCORE_RE.sub("", ", " + pos)[2:]   # 先頭の ", " を足して外す（先頭にある score_ も外れる）
    pos = re.sub(r"(^|,\s*)safe(?=\s*,)", r"\1general", pos, count=1)
    # SDXL は先頭ほど効くので「品質 → 絵柄（アニメ塗り）→ 絵師」を先頭に（重複しても害はない）
    trig = ", ".join(L["trigger"] for L in sdxl_loras() if (L.get("trigger") or "").strip())
    head = [x for x in (trig, MODEL.get("quality_pos"), MODEL.get("style_pos"), MODEL.get("artist")) if x and x.strip()]
    if head:
        pos = ", ".join(head) + ", " + pos
    neg = SCORE_RE.sub("", ", " + neg)[2:]
    for t in MODEL.get("neg_remove") or []:
        neg = re.sub(r"(^|,)\s*" + re.escape(t) + r"\s*(?=,|$)", r"\1", neg)
        neg = re.sub(r",\s*,", ",", neg).strip(", ")
    for x in (MODEL.get("quality_neg"), MODEL.get("style_neg")):
        if x and x.strip():
            neg = neg.rstrip(", ") + ", " + x
    return scene_safety(pos, neg)


SAFETY = {}   # model.json の "scene_safety"（load_scene_safety で読む）
HAIR_COLOR_RE = re.compile(r"\b(silver white|platinum blonde|light blue|silver|white|blonde|golden|orange|red|crimson|pink|purple|violet|"
                           r"lavender|green|emerald|black|brown|grey|gray|aqua|teal)(?:-| )hair(?:ed)?\b", re.I)


def load_scene_safety(mj=None):
    if mj is None:
        try:
            mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
        except Exception:
            mj = {}
    SAFETY.clear()
    SAFETY.update(mj.get("scene_safety") or {})
    SAFETY["_subs"] = [(re.compile(a, re.I), b) for a, b in SAFETY.get("subs", [])]
    SAFETY["_neg_subs"] = [(re.compile(a, re.I), b) for a, b in SAFETY.get("neg_subs", [])]


def _add_terms(text, add):
    """カンマ区切りの語を、まだ入っていないものだけ足す"""
    have = {t.strip().lower() for t in text.split(",")}
    new = [t.strip() for t in add.split(",") if t.strip() and t.strip().lower() not in have]
    return (text.rstrip(", ") + ", " + ", ".join(new)) if new else text


def scene_safety(pos, neg):
    """2026-10-02 確認撮影の点検で出た問題の対策（model.json の scene_safety）。prompts\\*.json は書き換えない。
    1) 幼く見えやすい語の言い換え（学校風の服・男の娘の細さの重ね書き など）
    2) 相手の髪色が主人公に移る対策：相手の髪色を拾って『その色の髪の主人公』をネガへ、主人公の紺髪を強める
    3) 相手の獣耳・尻尾が主人公に移る対策
    4) 相手が男の娘のとき、主人公まで女性的・小柄にならないよう"""
    if not truthy(SAFETY.get("enabled", True)):
        return pos, neg
    for rx, b in SAFETY.get("_subs", []):
        pos = rx.sub(b, pos)
    pos = re.sub(r"(,\s*){2,}", ", ", pos)
    if "navy" not in pos:
        return pos, neg
    # 2026-10-02 その4：LoRAなしでも主人公が幼く出た → 主人公が出る絵だけ、ネガの『男らしさ』消しを外し、子ども体型のネガと大人の体の一文を足す
    for rx, b in SAFETY.get("_neg_subs", []):
        neg = rx.sub(b, neg)
    neg = re.sub(r"(,\s*){2,}", ", ", neg)
    if SAFETY.get("hero_neg"):
        neg = _add_terms(neg, SAFETY["hero_neg"])
    hp = (SAFETY.get("hero_pos") or "").strip()
    if hp and hp not in pos:
        pos = pos.rstrip(", ") + ", " + hp
    adds = []
    cols = []
    for m in HAIR_COLOR_RE.finditer(pos):
        c = m.group(1).lower()
        for x in (c, c.split()[-1]):   # silver white → white も
            if x not in cols:
                cols.append(x)
    for c in cols:
        adds.append("%s hair on the navy-haired man" % c)
    w = SAFETY.get("hero_hair_weight")
    if cols and w and "(navy blue hair:" not in pos:
        pos = pos.replace("navy blue hair", "(navy blue hair:%s)" % w, 1)
    for rx, ng in SAFETY.get("partner_trait_neg", []):   # 相手の肌の色などが主人公に移る対策（2026-10-02 DarkElf：主人公が褐色に）
        if re.search(rx, pos, re.I):
            adds.append(ng)
    if re.search(SAFETY.get("animal_rx") or r"$^", pos, re.I) and "crossdress" not in pos:   # 女装（バニー等）は主人公の耳・尻尾が衣装なので外さない
        adds.append(SAFETY.get("animal_neg", ""))
    if re.search(r"otoko no ko|femboy|newhalf|\btrap\b", pos, re.I):
        adds.append(SAFETY.get("femboy_neg", ""))
        fp = (SAFETY.get("femboy_pos") or "").strip()
        if fp:
            pos = pos + ", " + fp
    adds = [a for a in adds if a and a.strip() and a not in neg]
    if adds:
        neg = neg.rstrip(", ") + ", " + ", ".join(adds)
    return pos, neg
FACE_FIX = True


def truthy(v):
    if isinstance(v, str):
        return v.strip().lower() in ("true", "1", "yes", "y")
    return bool(v)


def load_lora(a):
    c = json.loads(json.dumps(DEFAULT_LORA))
    p = os.path.join(HERE, "lora.json")
    try:
        u = json.load(open(p, encoding="utf-8"))
        for k in ("style", "hero"):
            if isinstance(u.get(k), dict):
                c[k].update(u[k])
    except FileNotFoundError:
        pass
    except Exception as e:
        print("(lora.json が読めないので既定値を使います:", e, ")")
    if a.no_lora:
        c["style"]["enabled"] = False; c["hero"]["enabled"] = False
    if a.no_hero:
        c["hero"]["enabled"] = False
    if getattr(a, "no_style", False):
        c["style"]["enabled"] = False
    if a.lora_strength is not None:
        c["style"]["strength"] = a.lora_strength
    if a.hero_strength is not None:
        c["hero"]["strength"] = a.hero_strength
        if a.hero_strength <= 0:
            c["hero"]["enabled"] = False
    return c


def wf(e, seed, batch, prefix, lora, use_rmbg, name="", no_pose=False):
    pos = e["positive"]
    fresh = HERO_AGE == "fresh"
    hero_pic = "navy" in pos.lower() or ("dark blue hair" in pos and "crossdress" in pos)   # 主人公（または女装娘）が出る絵
    if fresh and hero_pic:
        for rx, rep in AGE_SUBS:
            pos = rx.sub(age_face(rep), pos)   # 2026-09-29 若めの大人：age_face
    if "navy" in pos.lower() and "mature face" not in pos and "fresh face" not in pos:
        pos = pos.rstrip(", ") + ", " + (age_face(ADULT_POS_FRESH) if fresh else ADULT_POS)
    neg = e["negative"].rstrip(", ") + ", " + ADULT_NEG
    if hero_pic:   # 2026-09-29 成人強化：主人公が出る絵は子どもの体型に寄らないよう毎回足す
        neg = neg + ", " + ADULT_BODY_NEG
    if fresh and hero_pic:
        neg = neg + ", " + AGE_NEG
    scene = ", solo," not in e["positive"] and "navy" in e["positive"].lower()
    hero_on = truthy(lora["hero"].get("enabled")) and lora["hero"].get("when_text_contains", "navy").lower() in e["positive"].lower()
    global CUR_TEXT, CUR_SCENE
    CUR_TEXT = e["positive"]
    CUR_SCENE = scene
    if any(L.get("role") == "hero" for L in sdxl_loras()):   # wai の主人公LoRA（sdduel_hero_xl）
        hero_on = True
    if scene and hero_on and EYES_TEXT == "strip":
        pos = HIDE_RE.sub("", pos)
        pos = SHUT_RE.sub("", pos)
        neg = NEG_EYES_RE.sub("", neg)
    if HERO_FACE.get("show") and HERO_HAIR_RE.search(e["positive"]):   # 主人公の髪（navy blue hair / 女装娘の dark blue hair）が描かれる絵だけ
        # 主人公の顔を見せる：目隠れの文字を外し、髪色の直後に目の色と前髪を入れる（先頭の HERO_POS にも入る）
        pos = FACE_HIDE_RE.sub(lambda m: "" if m.group(1) == "," else ":", pos)
        pos = _re.sub(r":\s*,\s*", ": ", pos)
        pos = FACE_HIDE_INLINE_RE.sub("", pos)
        skin = HERO_FACE.get("skin", "")
        if skin:
            pos = pos.replace("smooth pale skin", "smooth skin")
        # 2026-09-30 2人の場面では主人公の目の色を書かない（hero_face.scene_eyes false）：目の色が相手に移るため。主人公の目元は生成後に隠す方針
        hero_eye = HERO_FACE.get("eyes", "aqua eyes") if (not scene or HERO_FACE.get("scene_eyes", True)) else ""
        eyes = ", ".join(x for x in (hero_eye, HERO_FACE.get("bangs", "short bangs above the eyes"),
                                     HERO_FACE.get("build", ""), skin) if x)
        pos = HERO_HAIR_RE.sub(lambda m: m.group(1) + ", " + eyes, pos, count=1)
        neg = NEG_EYES_RE.sub("", neg)
        neg = neg + (", hair over eyes on the navy-haired man, bangs covering eyes on the navy-haired man, faceless male, "
                     "%s on the other character, ahegao, rolling eyes, cross-eyed, empty eyes" % HERO_FACE.get("eyes", "aqua eyes"))
        if HERO_FACE.get("build_neg"):
            neg = neg + ", " + HERO_FACE["build_neg"]
        if HERO_FACE.get("skin_neg"):
            neg = neg + ", " + HERO_FACE["skin_neg"]
    if FACE_FIX and scene:
        # 長いプロンプトの後ろだと効きにくいので、品質タグの直後（先頭近く）に入れる
        fp = FACE_POS
        if FACE_LEVEL >= 2:
            m = EYE_RE.search(e["positive"])
            if m:
                fp += ", the other character's " + m.group(1) + " are clearly visible"
            fp += ", " + BANGS_POS
        pos = fp + ", " + pos
        neg = neg + ", " + FACE_NEG
        if FACE_LEVEL >= 3:
            neg = neg + ", " + EYES_NEG_HARD
    if FACE_FIX and scene:
        P0 = e["positive"]
        hp = age_face(HERO_POS_FRESH) if fresh else HERO_POS
        if HERO_FACE.get("show") and HERO_FACE.get("scene_eyes", True):
            hp += ", %s, his face and eyes are visible, slim adult male body, not muscular" % HERO_FACE.get("eyes", "aqua eyes")
        elif HERO_FACE.get("show"):
            hp += ", his face is visible, slim adult male body, not muscular"
        head, tail = [hp], [HERO_NEG]
        if ("femboy" in P0 or "otoko no ko" in P0) and "1girl" not in P0 and "woman" not in P0:
            head.append(FEMBOY_POS); tail.append(FEMBOY_NEG)
        if "naked navy" in P0 and "crossdress" not in P0:
            head.append(NAKED_POS); tail.append(NAKED_NEG)
        pos = ", ".join(head) + ", " + pos
        neg = neg + ", " + ", ".join(tail)
    if FACE_FIX and scene and "crossdress" in e["positive"]:
        pos = DRESS_POS + ", " + pos
        neg = neg + ", " + DRESS_NEG
    if ROLE_FIX and scene:
        # 一番先頭（トリガー・品質タグの直後）に「相手が攻め・主人公が受け」
        pos = ROLE_POS[partner_kind(e["positive"])] + ", " + pos
        neg = neg + ", " + ROLE_NEG
    if scene and HERO_FACE.get("show"):
        # 顔の混ざり対策：2人は別の顔（相手の髪色・目の色は FACE_POS で先頭に入っている）
        pos = pos.replace("the navy-haired man is an adult man", "the navy-haired man has his own different face, he is an adult man", 1)
        neg = neg + ", same face, identical faces, twins, clones, both characters with the same face, the other character with aqua eyes, the other character with navy blue hair"
        if not HERO_FACE.get("scene_eyes", True):
            # 2026-09-30 主人公の目の色を書かない場面：相手の目が主人公の目の色にならないよう、その色自体をネガに（相手が同じ色の目のときは入れない）
            he = HERO_FACE.get("eyes", "aqua eyes")
            m = EYE_RE.search(e["positive"])
            if he and not (m and he.split()[0] in m.group(1)):
                neg = neg + ", " + he
            # 主人公の舌出し・よだれ（相手の「長い舌」などが移る。本編はアへ顔なし）
            neg = neg + ", the navy-haired man with his tongue out, the navy-haired man drooling"
    model = ["3", 0]
    used = []
    for key, nid in (("style", "20"), ("hero", "21")):
        L = lora[key]
        if not truthy(L.get("enabled")):
            continue
        w = L.get("when_text_contains")
        if w and w.lower() not in e["positive"].lower():
            continue
        used.append(key)
        model_in = model
        model = [nid, 0]
        L["_node"] = {"class_type": "LoraLoaderModelOnly",
                      "inputs": {"lora_name": L["lora_name"], "strength_model": float(L["strength"]), "model": model_in}}
    # トリガー語はプロンプトの先頭に（絵柄 → 主人公の順）
    for key in reversed(used):
        t = lora[key].get("trigger")
        if t and t not in pos:
            pos = t + ", " + pos
    pos, neg = adapt_prompt(pos, neg)
    # 構図LoRA：既存の変換をすべて済ませた最終プロンプトで判定（2人の場面・SDXL のときだけ）
    global LAST_POSE
    pose = []
    LAST_POSE = {"scene": scene, "picked": [], "missing": [], "text": pos, "control": None}
    LORA_ALT["hit"] = None
    CTRL_HIT["ref"] = None
    if scene and "scene" in (POSE_CFG.get("apply_to") or ["scene"]) and MODEL.get("loader") == "ckpt" and not no_pose:
        alt = (POSE_CONTROL.get("lora_alt") or {}) if (LORA_ALT["on"] or truthy(POSE_CONTROL.get("lora_alt_on"))) and not NO_CONTROL else {}
        if not alt and not NO_CONTROL:   # lora_alt_force：この構図LoRA だけは常に下書き（元絵の組）に置き換える（2026-10-01 耳責め・パイズリ）
            alt = {k: [r for r in v if str(r[1]).startswith("set:")] for k, v in (POSE_CONTROL.get("lora_alt") or {}).items()
                   if k in (POSE_CONTROL.get("lora_alt_force") or [])}   # 常に置き換えるのは元絵の組だけ（無ければ構図LoRA のまま）
        for p, hits in pick_pose(name, pos):
            if p.get("kind", "action") == "action" and p["id"] in alt and LORA_ALT["hit"] is None:
                cid = pick_control(alt[p["id"]], pos, name)
                if cid:   # 構図LoRA は使わず、下書き＋その LoRA のトリガー語（行為のタグ）で撮る
                    LORA_ALT["hit"] = (p, cid)
                    continue
            f = pose_file(p)
            LAST_POSE["picked"].append((p, hits))
            if f is None:
                LAST_POSE["missing"].append(p["file"])
                POSE_MISSING.add(p["file"])
                print("  (構図LoRA %s が ComfyUI にないので、この画像は外して撮ります: %s)" % (p["file"], name))
                continue
            pose.append((p, f))
        if pose:
            adds, negs = [], []
            for p, f in pose:
                adds.append(p.get("trigger", ""))
                for x in p.get("_extra") or []:
                    if x["_rx"].search(pos):
                        adds.append(x.get("pos", "")); negs.append(x.get("neg", ""))
                negs.insert(0, p.get("neg", ""))
            ins = ", ".join(x for x in adds if x and x.strip())
            if ins:
                role = ROLE_POS[partner_kind(e["positive"])] if ROLE_FIX else ""
                i = pos.find(role) if role else -1
                if i >= 0:   # 受け攻めタグの直後
                    j = i + len(role)
                    pos = pos[:j] + ", " + ins + pos[j:]
                else:
                    pos = ins + ", " + pos
            for x in negs:
                if x and x.strip():
                    neg = neg.rstrip(", ") + ", " + x
    M = MODEL
    if M["loader"] == "ckpt":
        # SDXL：チェックポイント1つにモデル・CLIP・VAE が入っている
        w = {
         "3": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": M["ckpt_name"]}},
        }
        m_out, c_out = ["3", 0], ["3", 1]
        for i, L in enumerate(sdxl_loras()):
            nid = str(30 + i)
            w[nid] = {"class_type": "LoraLoader", "inputs": {"model": m_out, "clip": c_out, "lora_name": L["lora_name"],
                      "strength_model": float(L.get("strength", 0.8)),
                      "strength_clip": float(L.get("clip_strength", L.get("strength", 0.8)))}}
            m_out, c_out = [nid, 0], [nid, 1]
            used.append(L["lora_name"].replace(".safetensors", "") + "@%s" % L.get("strength", 0.8))
        # 構図LoRA は既存の連結（anime_screencap・絵柄・主人公）の後ろ。ノードは 50 番台（既存と重ならない）
        for i, (p, f) in enumerate(pose):
            nid = str(50 + i)
            st = round(float(p.get("strength", 0.7)) * POSE_SCALE, 3)
            w[nid] = {"class_type": "LoraLoader", "inputs": {"model": m_out, "clip": c_out, "lora_name": f,
                      "strength_model": st, "strength_clip": st}}
            m_out, c_out = [nid, 0], [nid, 1]
            used.append("構図:%s@%s" % (p["id"], st))
        model = m_out
        w["4"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": c_out, "stop_at_clip_layer": int(M.get("clip_skip", -2))}}
        vae = ["3", 2]
    else:
        w = {
         "3": {"class_type": "UNETLoader", "inputs": {"unet_name": M["unet_name"], "weight_dtype": "default"}},
         "4": {"class_type": "CLIPLoader", "inputs": {"clip_name": M["clip_name"], "type": "qwen_image"}},
         "5": {"class_type": "VAELoader", "inputs": {"vae_name": M["vae_name"]}},
        }
        vae = ["5", 0]
    w.update({
     "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["4", 0]}},
     "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 0]}},
     "8": {"class_type": "EmptyLatentImage", "inputs": {"width": int(e.get("width", 832)), "height": int(e.get("height", 1216)), "batch_size": batch}},
     "9": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": int(M["steps"]), "cfg": float(M["cfg"]),
           "sampler_name": M["sampler"], "scheduler": M["scheduler"],
           "denoise": 1.0, "model": model, "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0]}},
     "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": vae}},
     "11": {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": prefix}},
    })
    for key, nid in (("style", "20"), ("hero", "21")):
        if key in used:
            w[nid] = lora[key].pop("_node")
    CTRL_HIT["id"] = None
    ctrl = None if no_pose else control_image_for(name, pose if M["loader"] == "ckpt" else [], LAST_POSE.get("text"), scene)
    LAST_POSE["control"] = ctrl
    if ctrl:   # 構図の下書き（ControlNet OpenPose）：KSampler の条件付けを下書きつきに差し替える
        tg = control_tags(CTRL_HIT.get("id")) if not FORCE_CONTROL else ""
        if tg:   # 行為のタグを受け攻めタグの直後（構図LoRA のトリガーと同じ位置）へ
            t6 = w["6"]["inputs"]["text"]
            role = ROLE_POS[partner_kind(e["positive"])] if ROLE_FIX else ""
            i6 = t6.find(role) if role else -1
            w["6"]["inputs"]["text"] = (t6[:i6 + len(role)] + ", " + tg + t6[i6 + len(role):]) if i6 >= 0 else (tg + ", " + t6)
            used.append("行為タグ:%s" % CTRL_HIT.get("id"))
        if not FORCE_CONTROL and is_pov_ref():   # POV の下書き：主人公は見ている側（画面に顔を出さない）に書き換える（2026-10-01）
            w["6"]["inputs"]["text"], w["7"]["inputs"]["text"] = pov_prompt(w["6"]["inputs"]["text"], w["7"]["inputs"]["text"])
            PF = POSE_CONTROL.get("pov_fix") or {}
            hs = PF.get("hero_lora_strength")
            if hs is not None:   # 主人公LoRA は顔を描かせる方へ引っぱるので弱める
                for nd in w.values():
                    if nd.get("class_type") == "LoraLoader" and "hero" in str(nd["inputs"].get("lora_name", "")):
                        nd["inputs"]["strength_model"] = nd["inputs"]["strength_clip"] = float(hs)
            used.append("POV書き換え")
        regs = region_texts(w["6"]["inputs"]["text"], ctrl)
        pp, nn = add_pose_control(w, ["6", 0], ["7", 0], ctrl, regions=regs, clip=["4", 0])
        if regs:
            used.append("人物の範囲:%s" % "+".join(regs))
        # 2026-10-02 キャラLoRA（chara_map）は相手の範囲だけにかける（主人公の髪が黒くなる・相手の特徴が移る対策）。
        # 画面全体のキャラLoRAは hook_global まで弱め、相手の文を読むCLIPに LoRAフックを付ける（ComfyUI のフック機能）
        if regs and regs.get("partner") and CUR_CHARA and CUR_CHARA.get("mapped") and CUR_CHARA.get("hook", True) and HOOK_OK and CUR_SCENE:
            enc = str(80 + list(regs).index("partner") * 4)
            for nid, nd in list(w.items()):
                if enc in w and nd.get("class_type") == "LoraLoader" and nd["inputs"].get("lora_name") == CUR_CHARA["lora_name"]:
                    hs = float(nd["inputs"]["strength_model"])
                    gs = float(CUR_CHARA.get("hook_global", 0.2))
                    nd["inputs"]["strength_model"] = nd["inputs"]["strength_clip"] = gs
                    w["90"] = {"class_type": "CreateHookLora", "inputs": {"lora_name": CUR_CHARA["lora_name"],
                               "strength_model": hs, "strength_clip": hs}}
                    w["91"] = {"class_type": "SetClipHooks", "inputs": {"clip": w[enc]["inputs"]["clip"], "apply_to_conds": True,
                               "schedule_clip": False, "hooks": ["90", 0]}}
                    w[enc]["inputs"]["clip"] = ["91", 0]
                    used.append("キャラLoRAは相手の範囲だけ@%s（全体 %s）" % (hs, gs))
                    break
        w["9"]["inputs"]["positive"], w["9"]["inputs"]["negative"] = pp, nn
        _pi = (POSE_CONTROL.get("per_image") or {}).get(ctrl) or (POSE_CONTROL.get("ref_control") if str(ctrl).startswith("depthref_") else None) or {}
        used.append("下書き:%s@%s〜%s" % (ctrl, CONTROL_CLI["strength"] or _pi.get("strength", POSE_CONTROL["strength"]),
                                               CONTROL_CLI["end"] or _pi.get("end", POSE_CONTROL["end"])))
    if CUR_SCENE and CUR_CHARA and CUR_CHARA.get("mapped") and re.search(r"fully clothed female|keeps (?:all )?her clothes on|clothed female", e["positive"], re.I):
        # 2026-10-02 キャラLoRA は露出の多い衣装で学習したものが多く、着衣のはずの相手の胸が出る（Oiran）→ 着衣の場面だけネガに足す
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + ", the woman's bare breasts, the woman's exposed nipples, breasts out, topless woman, open kimono showing her breasts"
    if CUR_CHARA and CUR_CHARA.get("mapped") and re.search(r"\b(?:medium|large|huge|big) breasts\b", e["positive"], re.I):
        # 2026-10-02 キャラLoRAで胸が平らに出た（Clinic）→ 胸の大きさを指定している相手はネガに平らな胸を足す
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + ", flat chest on the woman, small breasts on the woman"
    if CUR_SCENE and not is_pov_ref() and "pov" not in w["6"]["inputs"]["text"].lower():
        # 2026-10-02 添い寝の下書きで、画面手前に3人目（見ている側の男の股間）が出た（Amazon・Inn）→ POV でない場面はネガに足す
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + ", pov, pov crotch, third person, extra man in the foreground, extra penis in the foreground, 3 people"
    if CUR_SCENE and CUR_CHARA and CUR_CHARA.get("mapped") and "crossdress" not in e["positive"].lower():
        # 2026-10-02 キャラLoRA の眼鏡・服が主人公に移った（Studio・アニス）→ 主人公の眼鏡と服をネガに
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + ", glasses on the navy-haired man, eyewear on the man, the navy-haired man wearing a shirt, the navy-haired man wearing pants, the woman's outfit on the man"
    if CUR_SCENE and CUR_CHARA and CUR_CHARA.get("mapped"):
        # 2026-10-02 キャラLoRA（男女の普通の性行為で学習）に引っぱられて、相手が男に奉仕する・主人公がごつい別人になった（Masque・Library・Clinic）
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + (", the woman kneeling before the man, the woman sucking his penis, fellatio, the man grabbing her head, "
            "the man dominant, the man penetrating the woman, muscular man, old man, ugly man, bastard man, black-haired man, brown-haired man, short black hair on the man, "
            "the man's eyes visible, child, boy, shota, young boy, small boy, childlike man")
    if not CUR_SCENE and CUR_CHARA and CUR_CHARA.get("mapped"):
        # 2026-10-02 立ち絵でキャラLoRA（男と一緒の絵で学習）が男を抱いた姿で出た（Ranch・カウペンス）→ 1人だけにする
        w["7"]["inputs"]["text"] = w["7"]["inputs"]["text"].rstrip(", ") + ", 1boy, man, male, hugging a man, holding a person, another person, 2 people"
    img = ["10", 0]
    if face_detail_on():   # 顔の描き直し（2人の場面は両方の顔を描き直す）
        img = add_face_detail(w, img, model, ["4", 0], vae, ["6", 0], ["7", 0], seed, M)
        w["11"]["inputs"]["images"] = img
        used.append("顔描き直し@%s" % FACE_DETAIL["denoise"])
    if use_rmbg and truthy(e.get("rmbg")):
        w["12"] = {"class_type": "InspyrenetRembg", "inputs": {"image": img, "torchscript_jit": "default"}}
        w["11"]["inputs"]["images"] = ["12", 0]
    return w, used


# ---- 顔の描き直し（FaceDetailer・2026-09-29「目元がよく崩れる」対策）。model.json の "face_detail" で設定 ----
# 全身の絵では顔が 100px ほどしかなく目が崩れやすいので、顔を見つけて拡大し、弱いノイズで描き直して戻す。
# ComfyUI に Impact Pack（FaceDetailer）と Impact Subpack（UltralyticsDetectorProvider）、models\ultralytics\bbox\face_yolov8m.pt が要る。
FACE_DETAIL = {"enabled": True, "model": "bbox/face_yolov8m.pt", "denoise": 0.4, "steps": 20, "guide_size": 512,
               "max_size": 1024, "bbox_threshold": 0.5, "bbox_dilation": 10, "bbox_crop_factor": 3.0, "feather": 5}
NO_FACE_DETAIL = False   # --no-face-detail
FD_OK = True             # ComfyUI に FaceDetailer があるか（main で確認。無ければ描き直しなしで撮る）
HOOK_OK = True           # 2026-10-02 ComfyUI に CreateHookLora・SetClipHooks（LoRAフック）があるか。あればキャラLoRAを相手の範囲だけにかける


def load_face_detail(mj=None):
    """model.json の face_detail を読む（make_hero_ds_xl.py からも使う）"""
    if mj is None:
        try:
            mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
        except Exception:
            mj = {}
    if isinstance(mj.get("face_detail"), dict):
        FACE_DETAIL.update({k: v for k, v in mj["face_detail"].items() if not k.endswith("memo")})
    return FACE_DETAIL


def face_detail_on():
    return truthy(FACE_DETAIL.get("enabled")) and not NO_FACE_DETAIL and FD_OK and MODEL.get("loader") == "ckpt"


def add_face_detail(w, image, model, clip, vae, pos, neg, seed, M):
    """w に顔検出（60）と FaceDetailer（61）を足して、描き直した画像の出力を返す"""
    F = FACE_DETAIL
    w["60"] = {"class_type": "UltralyticsDetectorProvider", "inputs": {"model_name": F["model"]}}
    w["61"] = {"class_type": "FaceDetailer", "inputs": {
        "image": image, "model": model, "clip": clip, "vae": vae, "positive": pos, "negative": neg,
        "guide_size": float(F["guide_size"]), "guide_size_for": True, "max_size": float(F["max_size"]),
        "seed": seed, "steps": int(F["steps"]), "cfg": float(M["cfg"]), "sampler_name": M["sampler"], "scheduler": M["scheduler"],
        "denoise": float(F["denoise"]), "feather": int(F["feather"]), "noise_mask": True, "force_inpaint": True,
        "bbox_threshold": float(F["bbox_threshold"]), "bbox_dilation": int(F["bbox_dilation"]),
        "bbox_crop_factor": float(F["bbox_crop_factor"]), "sam_detection_hint": "center-1", "sam_dilation": 0,
        "sam_threshold": 0.93, "sam_bbox_expansion": 0, "sam_mask_hint_threshold": 0.7, "sam_mask_hint_use_negative": "False",
        "drop_size": 10, "bbox_detector": ["60", 0], "wildcard": "", "cycle": 1}}
    return ["61", 0]


# ---- 構図の下書き（ControlNet OpenPose・2026-09-29「プロンプト頼りだと歪む」対策）。model.json の "pose_control" ----
# 下書きは pose_templates.py が描く（成人の頭身）→ ComfyUI\input\pose_<id>.png。どの場面に使うかは
#   "scenes": {"画像名": "下書きid"}（最優先）／"by_pose": {"構図LoRAのid": "下書きid"}（その構図LoRAが当たった場面）
POSE_CONTROL = {"enabled": True, "model": "noob_openpose.safetensors", "union_type": "", "strength": 0.6,
                "start": 0.0, "end": 0.6, "scenes": {}, "by_pose": {}}
NO_CONTROL = False       # --no-control
NO_REGION = False        # --no-region：人物ごとの範囲（領域指定）を使わない（比べる用・2026-10-02）
NO_REF = False           # --no-ref：元絵の奥行き下書き（ref_sets）を使わず、3D の下書きだけにする（比べる用・2026-10-01）
LORA_ALT = {"on": False, "hit": None}   # 2026-09-29 --lora-to-control：構図LoRA の代わりに pose_control.lora_alt の下書きを使う（比べる用）
CONTROL_CLI = {"strength": None, "end": None}   # --control-strength／--control-end（試し撮り用）
FORCE_CONTROL = None     # --pose-image <下書きid>：この実行の全画像に使う（試し撮り用）


def load_pose_control(mj=None):
    if mj is None:
        try:
            mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
        except Exception:
            mj = {}
    if isinstance(mj.get("pose_control"), dict):
        POSE_CONTROL.update({k: v for k, v in mj["pose_control"].items() if not k.endswith("memo")})
    return POSE_CONTROL


CTRL_HIT = {"id": None, "ref": None}   # 直前の control_image_for で当たった項目の id（行為のタグを選ぶため）／ref＝元絵の奥行き下書きの構図名


def control_tags(ctrl_id):
    """下書きが当たった場面に入れる『行為のタグ』（pose_control.tags）＋元絵の奥行き下書きなら視点のタグ（pose_control.ref_tags）"""
    t = _control_tags(ctrl_id)
    ref = CTRL_HIT.get("ref")
    if ref:
        for key in ("ref_role", "ref_tags"):   # ref_role＝誰がどこにいるか（受け攻めの入れ替わり対策・2026-10-01）／ref_tags＝視点
            v = ((POSE_CONTROL.get(key) or {}).get(ref) or "").strip()
            if v:
                t = (t + ", " + v) if t else v
    return t


def _control_tags(ctrl_id):
    """下書きが当たった場面に入れる『行為のタグ』（pose_control.tags）。構図LoRA のトリガーの代わり（2026-09-29 描写が弱い対策）"""
    if ctrl_id and ctrl_id.startswith("alt:"):
        lid = ctrl_id[4:]
        t = (POSE_CONTROL.get("tags") or {}).get(lid)
        if t is None and LORA_ALT.get("hit"):
            t = LORA_ALT["hit"][0].get("trigger", "")
        return (t or "").strip()
    return ((POSE_CONTROL.get("tags") or {}).get(ctrl_id) or "").strip()


def is_pov_ref():
    """直前に選んだ元絵の下書きが POV（ref_tags に pov を含む）か"""
    ref = CTRL_HIT.get("ref")
    t = ((POSE_CONTROL.get("ref_tags") or {}).get(ref) or "") if ref else ""
    return bool(re.search(r"\bpov\b", t))


def pov_prompt(pos, neg):
    """POV の下書きのとき：『主人公の顔が見える』系の文を外し、主人公＝見ている側と書き直す。pose_control.pov_fix で調整
    （2026-10-01 Atelier e3：POV の下書きなのに主人公の顔も描かれて、主人公が2人になった対策）"""
    PF = POSE_CONTROL.get("pov_fix") or {}
    for a, b in PF.get("replace", []):
        pos = re.sub(a, b, pos, flags=re.I)
    # 主人公の顔・髪の描写（hero_remove）は、相手の描写（THE WOMAN: 〜 THE MAN の間）以外から外す
    i, j = pos.find("THE WOMAN:"), pos.find("THE MAN (")
    keep = pos[i:j] if 0 <= i < j else ""
    rest = pos.replace(keep, "\x00", 1) if keep else pos
    for a in PF.get("hero_remove", []):
        rest = re.sub(r",\s*(?:%s)(?=,|$)" % a, "", rest, flags=re.I)
    pos = rest.replace("\x00", keep, 1) if keep else rest
    add = (PF.get("pos") or "").strip()
    if add:
        pos = pos + ", " + add
    if (PF.get("neg") or "").strip():
        neg = neg.rstrip(", ") + ", " + PF["neg"].strip()
    return re.sub(r"(,\s*){2,}", ", ", pos), neg


def _partner_text(pos):
    """相手の範囲に効かせる文：場面の文から主人公の見た目のところを抜いたもの（2026-10-02）"""
    t = pos
    i, j = t.find("THE WOMAN:"), t.find("THE MAN (")
    if 0 <= i < j:   # 女性の相手：THE MAN 〜 he is slightly shorter … を抜く
        k = t.find("he is slightly shorter", j)
        k = t.find(",", k) if k >= 0 else -1
        t = t[:j] + (t[k + 1:] if k >= 0 else "")
    else:
        m = re.search(r",\s*and a naked [^:]{0,40}man:", t)   # 男の娘・NH：『, and a naked … man: 主人公の見た目』
        if m:
            k = t.find("he is slightly shorter", m.end())
            k = t.find(",", k) if k >= 0 else -1
            t = t[:m.start()] + (", " + t[k + 1:] if k >= 0 else "")
    segs = [x.strip() for x in t.split(",")]
    segs = [x for x in segs if x and not re.search(r"navy|adam's apple|his face is visible|the navy-haired man has his own", x, re.I)
            and not re.fullmatch(r"\d?(?:boys?|girls?)|1girl|1boy|2boys|duo|two people|two different characters|cmnm|yaoi", x, re.I)]
    segs = [re.sub(r"^THE WOMAN:\s*", "", x) for x in segs]
    R = POSE_CONTROL.get("region") or {}
    return ", ".join([R.get("partner_head", "the other character")] + segs + ([R["partner_tail"]] if R.get("partner_tail") else []))


def _hero_text(pos):
    R = POSE_CONTROL.get("region") or {}
    t = R.get("hero_text") or ("1boy, the navy-haired man, navy blue hair, short bangs above the eyes, short hair, "
                               "adult man, adult face, mid twenties, adam's apple, adult male body, not muscular")
    if re.search(r"\b(?:naked|nude male|completely naked)\b", pos, re.I):
        t += ", " + R.get("hero_naked", "completely naked, nude male")
    return t


def region_texts(pos, ctrl):
    """元絵の下書き（depthref_）に人物ごとの範囲（make_region_masks.py が作る pose_<下書き>_hero／_partner.png）があれば、
    {"hero": 主人公の文, "partner": 相手の文} を返す。POV（主人公が写らない）なら相手だけ"""
    R = POSE_CONTROL.get("region") or {}
    if NO_REGION or FORCE_CONTROL or not truthy(R.get("enabled", True)) or not str(ctrl).startswith("depthref_"):
        return None
    out = {}
    if not is_pov_ref() and os.path.exists(os.path.join(COMFY_INPUT, "pose_%s_hero.png" % ctrl)):
        out["hero"] = _hero_text(pos)
    if os.path.exists(os.path.join(COMFY_INPUT, "pose_%s_partner.png" % ctrl)):
        out["partner"] = _partner_text(pos)
    return out or None


def pick_control(v, text, key=None):
    """by_pose の値：下書きid、または [[正規表現, 下書きid], ...]（上から最初に当たったもの。正規表現が空なら無条件）
    2026-10-01：下書きid が "set:<名前>" なら pose_control.ref_sets の候補（元絵の奥行き下書き）から選ぶ。
    候補が無ければ次の行へ（そのあとに書いた 3D の下書きが予備になる）"""
    CTRL_HIT["ref"] = None
    R3 = POSE_CONTROL.get("ref_for_3d") or {}
    def res(cid):
        # 2026-10-02 下書きを増やす：3D の下書きの代わりに、似た構図の元絵の組（人物の範囲が効く）を先に試す
        if isinstance(cid, str) and cid in R3 and not NO_REF:
            r = resolve_ref(R3[cid], text, key)
            if r:
                return r
        return resolve_ref(cid, text, key)
    if isinstance(v, list):
        for rx, cid in v:
            if not rx or (text and re.search(rx, text, re.I)):
                cid = res(cid)
                if cid:
                    return cid
        return None
    return res(v)


COMFY_INPUT = os.path.join(os.path.dirname(OUTROOT), "input")
_REF_FILES = {}


def ref_images(comp):
    """ComfyUI\\input の pose_depthref_<構図名>.png / _2.png … （元絵から奥行き下書きを作る.bat が置く）"""
    if comp not in _REF_FILES:
        rx = re.compile(r"^pose_(depthref_%s(?:_\d+)?)\.png$" % re.escape(comp), re.I)
        try:
            ex = {str(x).lower() for x in (POSE_CONTROL.get("ref_exclude") or [])}   # 2026-10-02 使わない元絵（model.json pose_control.ref_exclude）
            _REF_FILES[comp] = sorted(m.group(1) for m in (rx.match(f) for f in os.listdir(COMFY_INPUT)) if m and m.group(1).lower() not in ex)
        except Exception:
            _REF_FILES[comp] = []
    return _REF_FILES[comp]


def _h(s):
    return int(hashlib.md5(s.encode("utf-8")).hexdigest()[:8], 16)


def resolve_ref(cid, text, key=None):
    """"set:<名前>" を元絵の奥行き下書き（depthref_<構図名>[_N]）1枚に。それ以外はそのまま返す。
    ref_sets[名前] = [{"when": 正規表現, "not": 正規表現, "comps": [構図名, ...], "default": true}, ...]
    when が当たった行の構図をすべて候補にする（when が空の行は常に候補）。どれも当たらなければ default の行。
    まず構図を選び、次にその構図の何枚目かを選ぶ（枚数の多い構図に偏らない）。同じ画像名なら毎回同じものになる"""
    if not (isinstance(cid, str) and cid.startswith("set:")):
        return cid
    if NO_REF or not truthy(POSE_CONTROL.get("ref_on", True)):
        return None
    name = cid[4:]
    rows = (POSE_CONTROL.get("ref_sets") or {}).get(name) or []
    t = text or ""
    def ok(r):
        return (not r.get("not") or not re.search(r["not"], t, re.I))
    comps = []
    for r in rows:
        if r.get("default"):
            continue
        if ok(r) and (not r.get("when") or re.search(r["when"], t, re.I)):
            comps += [c for c in r.get("comps", []) if c not in comps]
    if not [c for c in comps if ref_images(c)]:
        for r in rows:
            if r.get("default") and ok(r):
                comps += [c for c in r.get("comps", []) if c not in comps]
    comps = [c for c in comps if ref_images(c)]
    if not comps:
        return None
    k = "%s|%s" % (name, key or t)
    comp = comps[_h(k) % len(comps)]
    imgs = ref_images(comp)
    if not NO_REGION:   # 2026-10-02：人物の範囲がある元絵を優先（主人公の範囲あり＞相手だけ＞なし）。範囲なしの元絵だと髪色が入れ替わりやすい
        def has(i, role):
            return os.path.exists(os.path.join(COMFY_INPUT, "pose_%s_%s.png" % (i, role)))
        for pick in ([i for i in imgs if has(i, "hero")], [i for i in imgs if has(i, "partner")]):
            if pick:
                imgs = pick
                break
    CTRL_HIT["ref"] = comp
    return imgs[_h(k + "|img") % len(imgs)]


def control_image_for(name, pose, text=None, scene=False):
    """この画像に使う下書きid（無ければ None）。
    2026-09-29 置き換え：年齢系タグのある構図LoRA は無効にしたが、その when（判定条件）は残し、by_pose に下書きがあれば
    「構図LoRA の並び順どおりに判定して、最初に当たったのが下書きつきの項目なら、その下書き」を使う（有効な構図LoRA が先に当たればそちらに任せる）"""
    if NO_CONTROL or not truthy(POSE_CONTROL.get("enabled")) or MODEL.get("loader") != "ckpt":
        return None
    if FORCE_CONTROL:
        return FORCE_CONTROL
    sk = POSE_CONTROL.get("skip_body")
    if sk and text and re.search(sk, text, re.I):   # 下半身が人でない相手（ケンタウロス・ラミア等）は人の形の下書きを使わない（2026-10-01）
        return None
    if name and name in (POSE_CONTROL.get("scenes") or {}):
        return POSE_CONTROL["scenes"][name] or None
    bp = POSE_CONTROL.get("by_pose") or {}
    if scene and text is not None and truthy(POSE_CFG.get("enabled")) and not NO_POSE:
        for p in POSE_LIST:
            if p.get("kind", "action") != "action":
                continue
            if LORA_ALT.get("hit") and p is LORA_ALT["hit"][0]:   # 並び順どおり：この構図LoRA の代わりの下書き
                CTRL_HIT["id"] = "alt:" + p["id"]
                return LORA_ALT["hit"][1]
            if p.get("enabled") is False and p["id"] not in bp:
                continue
            if pose_match(p, text):
                CTRL_HIT["id"] = p["id"] if p["id"] in bp else None
                return pick_control(bp.get(p["id"]), text, name)   # 有効な構図LoRA（下書きなし）が先に当たれば None
        fb = POSE_CONTROL.get("fallback") or []   # 2026-10-02：どの項目にも当たらない場面も、姿勢（寝る・座る・ひざまずく…）で元絵の組を使う
        fnot = POSE_CONTROL.get("fallback_not")
        if fb and not (fnot and re.search(fnot, text, re.I)):
            cid = pick_control(fb, text, name)
            if cid:
                CTRL_HIT["id"] = "fallback"
                return cid
        return None
    for p, _f in pose or []:
        cid = pick_control(bp.get(p["id"]), text, name)
        if cid:
            return cid
    return None


def add_pose_control(w, pos, neg, cid, regions=None, clip=None):
    """w に ControlNet（70〜73）を足して、下書きつきの positive／negative を返す。
    per_image に下書きごとの設定（model・union_type・strength・end）があればそれを使う。
    regions={"hero": 主人公の文, "partner": 相手の文} を渡すと、下書きの人物ごとの範囲（pose_<id>_hero/partner.png）に
    その文だけを効かせて positive に足す（人物の入れ替わり対策・2026-09-29）"""
    C = dict(POSE_CONTROL)
    pi = (POSE_CONTROL.get("per_image") or {}).get(cid)
    if pi is None and str(cid).startswith("depthref_"):   # 元絵の奥行き下書きは共通の設定（pose_control.ref_control）
        pi = POSE_CONTROL.get("ref_control")
    C.update(pi or {})
    for k, v in CONTROL_CLI.items():   # --control-strength／--control-end は下書きごとの設定より優先
        if v is not None:
            C[k] = v
    if regions and clip:
        for i, (role, text) in enumerate(regions.items()):
            if not text:
                continue
            e, mk, sm, cb = str(80 + i * 4), str(81 + i * 4), str(82 + i * 4), str(83 + i * 4)
            w[e] = {"class_type": "CLIPTextEncode", "inputs": {"text": text, "clip": clip}}
            w[mk] = {"class_type": "LoadImageMask", "inputs": {"image": "pose_%s_%s.png" % (cid, role), "channel": "red"}}
            w[sm] = {"class_type": "ConditioningSetMask", "inputs": {"conditioning": [e, 0], "mask": [mk, 0],
                                                                     "strength": float(C.get("region_strength", 1.0)), "set_cond_area": "default"}}
            w[cb] = {"class_type": "ConditioningCombine", "inputs": {"conditioning_1": pos, "conditioning_2": [sm, 0]}}
            pos = [cb, 0]
    w["70"] = {"class_type": "ControlNetLoader", "inputs": {"control_net_name": C["model"]}}
    cn = ["70", 0]
    if C.get("union_type"):   # union 系のモデルは種類（openpose 等）を指定する
        w["73"] = {"class_type": "SetUnionControlNetType", "inputs": {"control_net": cn, "type": C["union_type"]}}
        cn = ["73", 0]
    w["71"] = {"class_type": "LoadImage", "inputs": {"image": "pose_%s.png" % cid}}
    w["72"] = {"class_type": "ControlNetApplyAdvanced", "inputs": {
        "positive": pos, "negative": neg, "control_net": cn, "image": ["71", 0],
        "strength": float(C["strength"]), "start_percent": float(C["start"]), "end_percent": float(C["end"])}}
    return ["72", 0], ["72", 1]


def get_json(path, timeout=10):
    with urllib.request.urlopen(SERVER + path, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def queue_count():
    try:
        q = get_json("/queue")
        return len(q.get("queue_running", [])) + len(q.get("queue_pending", []))
    except Exception:
        return 0


def out_dir(mod, style=None):
    """保存先フォルダ名：<MOD>_WAI（絵柄なし）／<MOD>_WAI_<絵柄>（MODごとの絵柄）"""
    return mod + MODEL["out_suffix"] + (("_" + style["name"]) if style else "")


def done_names(mod, style=None):
    d = os.path.join(OUTROOT, out_dir(mod, style))
    s = set()
    if os.path.isdir(d):
        for f in os.listdir(d):
            m = re.match(r"(.+?)_\d{5}_\.png$", f)
            if m:
                s.add(m.group(1))
    return s


def pose_assign(jobs, lora):
    """全場面の構図LoRAの割当を調べる（ComfyUI には送らない）。[(mod, n, e, [(項目, 語)...])]（場面だけ）"""
    out = []
    for mod, n, e in jobs:
        wf(e, 0, 1, "x", json.loads(json.dumps(lora)), False, name=n)
        if LAST_POSE.get("scene"):
            out.append((mod, n, e, LAST_POSE["picked"], LAST_POSE.get("control")))
    return out


def pose_report(jobs, lora):
    """--pose-report：割当を 構図LoRA_割当.csv に書き出し、LoRAごとの件数を表示する。"""
    import csv
    from collections import Counter
    res = pose_assign(jobs, lora)
    path = os.path.join(HERE, "構図LoRA_割当.csv")
    cnt, none, ccnt = Counter(), 0, Counter()
    with open(path, "w", encoding="utf-8-sig", newline="") as f:   # Excel で開けるよう BOM 付き
        wr = csv.writer(f)
        wr.writerow(["MOD", "画像名", "action", "look", "下書き", "当てはまった語"])
        for mod, n, e, picked, ctrl in res:
            act = [p["id"] for p, _ in picked if p.get("kind", "action") == "action"]
            look = [p["id"] for p, _ in picked if p.get("kind") == "look"]
            words = " / ".join("%s: %s" % (p["id"], " + ".join(h)) for p, h in picked)
            wr.writerow([mod, n, ",".join(act), ",".join(look), ctrl or "", words])
            for p, _ in picked:
                cnt[p["id"]] += 1
            if ctrl:
                ccnt[ctrl] += 1
            if not picked and not ctrl:
                none += 1
    print("\n構図LoRAの割当（場面 %d件）→ %s" % (len(res), path))
    for p in POSE_LIST:
        if p.get("enabled") is False and not cnt[p["id"]]:
            continue
        print("  %-14s %-6s %5d件" % (p["id"], p.get("kind", "action"), cnt[p["id"]]))
    if ccnt:
        print("  構図の下書き（ControlNet）:")
        for k, v in ccnt.most_common():
            print("    %-30s %5d件" % (k, v))
    print("  どれにも当たらなかった場面: %d件" % none)
    if not truthy(POSE_CFG.get("enabled")) or NO_POSE:
        print("  （構図LoRAは今オフです：model.json の pose_lora.enabled か --no-pose）")


def control_sample_jobs(jobs, lora, n_each, only=None):
    """--control-sample N：構図の下書き（ControlNet）ごとに、その下書きが当たる場面を N 件（MOD をまたいで散らして）選び、
    同じシードで「下書きあり／なし」の2枚ずつにする → output\\構図下書き確認\\<下書き>\\あり|なし\\<MOD>_<画像名>
    （2026-09-29。性的な場面の仕上がりはユーザーが確認する。Claude はこれを実行しない）"""
    res = pose_assign(jobs, lora)
    by = {}
    for mod, n, e, picked, ctrl in res:
        if not ctrl:
            continue
        ref = re.sub(r"_\d+$", "", ctrl[len("depthref_"):]) if str(ctrl).startswith("depthref_") else None
        if not only or ctrl in only or ctrl.replace("depth3d_", "") in only or (ref and (ref in only or "ref" in only)):
            by.setdefault(("ref_" + ref) if ref else ctrl, []).append((mod, n, e))   # 元絵の下書きは構図ごとにまとめる（何枚目かは問わない）
    out = []
    for ctrl, c in sorted(by.items()):
        step = max(1, len(c) // n_each)
        for mod, n, e in c[::step][:n_each]:
            for sub, off in (("あり", False), ("なし", True)):
                out.append((mod, n, e, "構図下書き確認/%s/%s/%s_%s" % (ctrl, sub, mod, n), False, off))
    return out


def pose_sample_jobs(jobs, lora, n_each):
    """--pose-sample N：構図LoRAごとに場面を N 件（MOD をまたいで散らして）選び、あり／なしの2枚ずつにする。"""
    res = pose_assign(jobs, lora)
    by = {}
    for mod, n, e, picked, _c in res:
        for p, _ in picked:
            by.setdefault(p["id"], []).append((mod, n, e))
    out = []
    for p in POSE_LIST:
        c = by.get(p["id"]) or []
        if not c:
            continue
        step = max(1, len(c) // n_each)
        for mod, n, e in c[::step][:n_each]:
            for sub, off in (("あり", False), ("なし", True)):
                out.append((mod, n, e, "構図LoRA比較/%s/%s/%s_%s" % (p["id"], sub, mod, n), off))
    return out


def style_pick(jobs, lora):
    """--style-compare で撮る4枚を選ぶ（Lamia を優先、無ければ全MODで最初に当たるもの）。[(番号, 名前, mod, n, e)]"""
    res = pose_assign(jobs, lora)
    def first(cond, pool):
        for mod, n, e, picked, *_ in pool:
            if cond(n, picked):
                return mod, n, e
        return None
    lam = [x for x in res if x[0] == "Lamia"]
    out = []
    for no, label in STYLE_PICS:
        got = None
        if no == "1":
            got = next(((m, n, e) for m, n, e in jobs if n == "Lamia_master"), None)
        elif no == "4":
            got = next(((m, n, e) for m, n, e in jobs if m == "Lamia" and "_onanie_" in n), None) or \
                  next(((m, n, e) for m, n, e in jobs if "_onanie_" in n), None)
        else:
            want = {"2": ("peg",), "3": ("kiss", "close_hug")}[no]
            cond = lambda n, picked: any(p["id"] in want and p.get("kind", "action") == "action" for p, _ in picked)
            got = first(cond, lam) or first(cond, res)
        if got:
            out.append((no, label) + got)
        else:
            print("  (絵 %s_%s に当たる画像がありません)" % (no, label))
    return out


def style_seeds(n):
    """画像ごとに固定の2つのシード（全条件で同じ）"""
    return [int(hashlib.md5(("style-compare-%s-%d" % (n, k)).encode()).hexdigest(), 16) % (2**31 - 1) for k in (1, 2)]


def style_grid():
    """撮った絵を、絵ごとに1枚の一覧画像（横6条件×縦2シード・上に条件名）にする。長辺2000px程度。"""
    from PIL import Image, ImageDraw, ImageFont
    root = os.path.join(OUTROOT, STYLE_DIR)
    font = None
    for f in (r"C:\Windows\Fonts\meiryo.ttc", r"C:\Windows\Fonts\YuGothM.ttc", r"C:\Windows\Fonts\msgothic.ttc"):
        try:
            font = ImageFont.truetype(f, 26); break
        except Exception:
            pass
    font = font or ImageFont.load_default()
    made = []
    for no, label in STYLE_PICS:
        cells = []   # [seed][cond] → パス or None
        for s in (1, 2):
            row = []
            for cond, *_ in STYLE_CANDS:
                d = os.path.join(root, cond)
                fs = sorted(f for f in (os.listdir(d) if os.path.isdir(d) else [])
                            if re.match(r"%s_%s_s%d_\d{5}_\.png$" % (no, re.escape(label), s), f))
                row.append(os.path.join(d, fs[-1]) if fs else None)   # 撮り直しがあれば一番新しいもの
            cells.append(row)
        if not any(p for r in cells for p in r):
            print("  一覧_%s_%s: まだ画像がありません" % (no, label)); continue
        first = next(p for r in cells for p in r if p)
        w0, h0 = Image.open(first).size
        ncol, nrow, head = len(STYLE_CANDS), 2, 40
        scale = 2000.0 / max(w0 * ncol, (h0 + head) * nrow)
        cw, ch = int(w0 * scale), int(h0 * scale)
        sheet = Image.new("RGB", (cw * ncol, (ch + head) * nrow), (255, 255, 255))
        dr = ImageDraw.Draw(sheet)
        for r, row in enumerate(cells):
            for c, p in enumerate(row):
                x, y = c * cw, r * (ch + head)
                dr.text((x + 8, y + 6), "%s  (seed%d)" % (STYLE_CANDS[c][0], r + 1), fill=(0, 0, 0), font=font)
                if p:
                    im = Image.open(p).convert("RGBA")
                    bg = Image.new("RGBA", im.size, (235, 235, 235, 255))   # 背景除去した立ち絵は灰色の上に
                    im = Image.alpha_composite(bg, im).convert("RGB").resize((cw, ch), Image.LANCZOS)
                    sheet.paste(im, (x, y + head))
                else:
                    dr.rectangle([x, y + head, x + cw - 1, y + head + ch - 1], fill=(200, 200, 200))
                    dr.text((x + 10, y + head + 10), "未撮影", fill=(80, 80, 80), font=font)
        out = os.path.join(root, "一覧_%s_%s.png" % (no, label))
        # 上書きの瞬間にプレビュー等がファイルを掴んでいると失敗する（Errno 22）ので、一時ファイルに書いてから置き換え、少し待って再試行
        tmp = out + ".tmp.png"
        sheet.save(tmp)
        for k in range(10):
            try:
                os.replace(tmp, out); break
            except OSError:
                time.sleep(1)
        else:
            print("  [注意] %s を上書きできません（画像を開いていたら閉じて --style-grid で作り直してください）。%s に保存しました" % (out, tmp))
            continue
        made.append(out)
        print("  一覧画像: %s（%dx%d）" % (out, sheet.size[0], sheet.size[1]))
    return made


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mod"); ap.add_argument("keys", nargs="?", default="all")
    ap.add_argument("--random", action="store_true"); ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--redo", action="store_true"); ap.add_argument("--no-lora", action="store_true")
    ap.add_argument("--no-hero", action="store_true"); ap.add_argument("--no-style", action="store_true"); ap.add_argument("--lora-strength", type=float)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--hero-strength", type=float, help="主人公LoRAの強さ（0で外す）")
    ap.add_argument("--no-face-fix", action="store_true", help="相手の顔を見せるタグを自動で足さない")
    ap.add_argument("--eyes-text", choices=["strip", "keep"], help="主人公の目隠れを文字で書くか（strip＝外してLoRAに任せる・既定／keep＝旧方式）")
    ap.add_argument("--hero-age", choices=["fresh", "mature"], help="主人公の年齢の書き方（fresh＝若い成人に言い換え・既定／mature＝旧方式）")
    ap.add_argument("--seed", type=int, help="シードを固定（比較用）")
    ap.add_argument("--face-level", type=int, choices=[1, 2, 3], help="相手の顔の対策の強さ（既定2）")
    ap.add_argument("--out", help="保存先フォルダ名（既定 <MODコード>_自作／wai は <MODコード>_WAI）")
    ap.add_argument("--model", choices=["wai", "anima"], help="使うモデル（既定は model.json）")
    ap.add_argument("--sdxl-lora-strength", type=float, help="wai で重ねる LoRA の強さを一時的に変える（0で外す・比較用）")
    ap.add_argument("--hero-scene-strength", type=float, help="2人の場面での主人公LoRAの強さを一時的に変える（比較用）")
    ap.add_argument("--add-lora", action="append", default=[], help="wai に LoRA を一時的に足す：ファイル名:強さ[:トリガー]（何度でも）")
    ap.add_argument("--no-pose", action="store_true", help="構図LoRAを一時的に外す")
    ap.add_argument("--pose-scale", type=float, help="構図LoRAの強さを一時的に X 倍にする")
    ap.add_argument("--pose-report", action="store_true", help="送らずに構図LoRAの割当を 構図LoRA_割当.csv に書き出す")
    ap.add_argument("--pose-sample", type=int, metavar="N", help="構図LoRAごとに場面を N 件、あり／なしを同じシードで撮る")
    ap.add_argument("--control-sample", type=int, metavar="N", help="構図の下書きごとに場面を N 件、下書きあり／なしを同じシードで撮る → output\\構図下書き確認\\")
    ap.add_argument("--control-id", help="--control-sample で撮る下書きを絞る（例 girl_on_top_kiss,standing_foot）")
    ap.add_argument("--style-compare", action="store_true", help="本編の絵柄LoRAを候補に差し替えて4枚×2シードを撮り、一覧画像を作る（MOD指定は無視して全MODから選ぶ）")
    ap.add_argument("--style-grid", action="store_true", help="撮り終わった絵柄比較から一覧画像だけ作り直す")
    ap.add_argument("--style", help="絵柄割当.csv を無視して、この絵柄で撮る（本編＝絵柄割当なし扱い）。保存先は <MOD>_WAI_<絵柄>")
    ap.add_argument("--style-list", action="store_true", help="使える絵柄・主人公LoRAの有無・MODごとの割当を表示する（送らない）")
    ap.add_argument("--random-style", nargs="?", const="blank", choices=["blank", "all"],
                    help="MODごとの絵柄をランダムに割り当てて 絵柄割当.csv に保存（blank＝空欄のMODだけ・既定／all＝対象MODを全部振り直す）")
    ap.add_argument("--assign-only", action="store_true", help="--random-style で割り当てて CSV に保存するだけ（撮らない）")
    ap.add_argument("--no-chara", action="store_true", help="イベントの敵キャラLoRAを一時的に外す")
    ap.add_argument("--chara-strength", type=float, help="イベントの敵キャラLoRAの強さを一時的に変える（比較用・0で外す）")
    ap.add_argument("--no-mod-style", action="store_true", help="絵柄割当.csv を使わない（今までどおり <MOD>_WAI に撮る）")
    ap.add_argument("--no-face-detail", action="store_true", help="顔の描き直し（FaceDetailer）を一時的に外す（比較用）")
    ap.add_argument("--no-control", action="store_true", help="構図の下書き（ControlNet）を一時的に外す")
    ap.add_argument("--no-region", action="store_true", help="人物ごとの範囲（領域指定）を使わない（比べる用）")
    ap.add_argument("--no-ref", action="store_true", help="元絵の奥行き下書き（pose_control.ref_sets）を使わず 3D の下書きだけにする（比べる用）")
    ap.add_argument("--lora-to-control", action="store_true", help="構図LoRA の代わりに下書き（pose_control.lora_alt）を使う（比べる用）")
    ap.add_argument("--pose-image", help="この実行の全画像に構図の下書き（pose_<id>.png）を使う（試し撮り用）")
    ap.add_argument("--control-strength", type=float, help="構図の下書きの強さを一時的に変える（既定は model.json の pose_control.strength）")
    ap.add_argument("--control-end", type=float, help="構図の下書きを効かせる範囲（0〜1。0.5＝描き始めの半分まで）を一時的に変える")
    ap.add_argument("--face-denoise", type=float, help="顔の描き直しの強さを一時的に変える（既定は model.json の face_detail.denoise）")
    a = ap.parse_args()
    global NO_FACE_DETAIL, FD_OK
    load_face_detail()
    NO_FACE_DETAIL = a.no_face_detail
    global NO_CONTROL, FORCE_CONTROL, NO_REF, NO_REGION
    load_pose_control()
    load_scene_safety()
    NO_CONTROL = a.no_control
    NO_REF = bool(getattr(a, "no_ref", False))
    NO_REGION = bool(getattr(a, "no_region", False))
    LORA_ALT["on"] = bool(getattr(a, "lora_to_control", False))
    FORCE_CONTROL = a.pose_image
    CONTROL_CLI["strength"] = a.control_strength
    CONTROL_CLI["end"] = a.control_end
    if a.face_denoise is not None:
        FACE_DETAIL["denoise"] = a.face_denoise
    if a.style_grid:
        style_grid()
        return
    global NO_POSE, POSE_SCALE, POSE_HAVE, SOLO_ONANIE, STYLE_SWAP, SKIP_ONANIE
    NO_POSE = a.no_pose
    if a.pose_scale is not None:
        POSE_SCALE = a.pose_scale
    global FACE_FIX, EYES_TEXT, FACE_LEVEL, HERO_AGE, MODEL, SDXL_LORA_STRENGTH
    MODEL = load_model(a.model)
    global ROLE_FIX
    try:
        mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
        hf = mj.get("hero_face")
        if isinstance(hf, dict):
            HERO_FACE.update(hf)
        if "role_fix" in mj:
            ROLE_FIX = bool(mj["role_fix"])
        if "solo_onanie" in mj:
            SOLO_ONANIE = bool(mj["solo_onanie"])
        if "skip_onanie" in mj:
            SKIP_ONANIE = bool(mj["skip_onanie"])
        load_pose(mj)
    except Exception:
        pass
    SDXL_LORA_STRENGTH = a.sdxl_lora_strength
    global HERO_SCENE_STRENGTH
    HERO_SCENE_STRENGTH = a.hero_scene_strength
    for x in a.add_lora:
        parts = x.split(":", 2)
        name = parts[0] if parts[0].endswith(".safetensors") else parts[0] + ".safetensors"
        st = float(parts[1]) if len(parts) > 1 and parts[1] else 0.6
        parts = x.split(":", 3)
        trg = parts[2] if len(parts) > 2 else ""
        ADD_LORAS.append({"lora_name": name, "strength": st, "clip_strength": st, "trigger": trg,
                          "role": "hero" if len(parts) > 3 and parts[3].strip().lower() == "hero" else ""})
    if a.hero_age:
        HERO_AGE = a.hero_age
    if a.face_level:
        FACE_LEVEL = a.face_level
    FACE_FIX = not a.no_face_fix
    if a.eyes_text:
        EYES_TEXT = a.eyes_text
    pdir = os.path.join(HERE, "prompts")
    allmods = sorted(f[:-5] for f in os.listdir(pdir) if f.endswith(".json"))
    if a.style_compare:
        a.mod, a.keys = "all", "all"
    if a.mod.lower() == "all":
        mods = allmods
    else:
        mods = [m.strip() for m in a.mod.replace("、", ",").split(",") if m.strip()]
        low = {m.lower(): m for m in allmods}
        bad = [m for m in mods if m.lower() not in low]
        if bad:
            print("見つからないMODコード:", ", ".join(bad)); print("使えるMODコード:", ", ".join(allmods)); sys.exit(1)
        mods = [low[m.lower()] for m in mods]
    # MODごとの絵柄（2026-09-29）
    import mod_style as MS
    global CUR_STYLE, NO_STYLE_HERO
    NO_STYLE_HERO = a.no_hero
    global CUR_CHARA, NO_CHARA, CHARA_STRENGTH
    NO_CHARA = a.no_chara or (a.chara_strength is not None and a.chara_strength <= 0)
    CHARA_STRENGTH = a.chara_strength
    PRES = MS.presets(STYLE_CANDS)
    if not os.path.isfile(MS.CSV_PATH):
        MS.write_csv(allmods)
        print("(絵柄割当.csv を作りました。絵柄の列に絵柄名を書くと、そのMODはその絵柄で撮ります)")
    ASSIGN = {} if (a.no_mod_style or MODEL.get("loader") != "ckpt" or a.style_compare) else MS.read_csv()
    bad = sorted({v for v in ASSIGN.values() if v not in PRES and v not in ("本編", "標準", "none")})
    if a.style and a.style not in PRES and a.style not in ("本編", "標準", "none"):
        bad.append(a.style)
    if bad:
        print("[中止] 知らない絵柄名: %s" % ", ".join(bad)); print("使える絵柄:", ", ".join(PRES)); sys.exit(1)
    if a.random_style and MODEL.get("loader") == "ckpt" and not a.style and not a.no_mod_style and not a.style_compare:
        # MODごとの絵柄をランダムに決めて 絵柄割当.csv に書く（次回からはその絵柄のまま＝撮り直しても絵柄がそろう）
        ASSIGN, picked = MS.random_assign(mods, ASSIGN, PRES, a.random_style)
        if picked:
            print("絵柄をランダムに割り当てました（%s）:" % ("空欄のMODだけ" if a.random_style == "blank" else "全部振り直し"))
            for m in sorted(picked):
                print("  %-10s → %s%s" % (m, picked[m], "" if PRES[picked[m]]["hero_ok"] else "（主人公LoRAはまだ無い）"))
            if not a.dry_run:
                MS.write_csv(allmods, ASSIGN, {m: "ランダム %s" % time.strftime("%m/%d %H:%M") for m in picked})
                print("→ 絵柄割当.csv に保存しました（変えたいときは CSV を直す）")
            else:
                print("（--dry-run なので 絵柄割当.csv には保存していません）")
        else:
            print("ランダム割当：空欄のMODはありません（全部振り直すなら --random-style all）")
        if a.assign_only:
            return
    MOD_STYLE = {m: MS.style_for(m, ASSIGN, PRES, a.style) for m in mods} if MODEL.get("loader") == "ckpt" else {m: None for m in mods}
    if a.style_list:
        print("使える絵柄（主人公LoRA: ○＝あり／×＝まだ無い → 主人公LoRAなしで撮る）")
        for k, p in PRES.items():
            print("  %-16s %s  強さ %s%s  主人公 %s %s" % (k, p["lora"], p["strength"], ("  トリガー " + p["trigger"]) if p["trigger"] else "",
                                                      "○" if p["hero_ok"] else "×", p["hero_lora"]))
        print("\nMODごとの割当（絵柄割当.csv。空欄＝今の model.json のまま・保存先 <MOD>_WAI）")
        for m in allmods:
            st = MS.style_for(m, MS.read_csv(), PRES)
            print("  %-10s %s" % (m, ("%s → output\\%s\\" % (st["name"], out_dir(m, st))) if st else "-"))
        return
    lora = load_lora(a)
    if not MODEL.get("lora", True):
        lora["style"]["enabled"] = False; lora["hero"]["enabled"] = False

    # 送る一覧を作る
    jobs = []
    for mod in mods:
        P = json.load(open(os.path.join(pdir, mod + ".json"), encoding="utf-8"))
        P = MS.apply_chara_map(mod, P)   # 2026-10-02 ダウンロードしたキャラLoRAに合わせて見た目の文字を置き換え（model.json chara_map）
        if a.keys == "all":
            names = list(P)
        else:
            parts = [x.strip() for x in a.keys.split(",") if x.strip()]
            names = [n for n in P if any(x in n for x in parts)]
        done = set() if (a.redo or a.out or a.pose_report or a.pose_sample or a.control_sample or a.style_compare) else done_names(mod, MOD_STYLE.get(mod))
        if SKIP_ONANIE:   # オナニー場面は当面撮らない（割当確認の件数からも外す）
            names = [n for n in names if not re.search("onani", n, re.I)]
        skip = [n for n in names if n in done]
        names = [n for n in names if n not in done]
        if not a.style_compare:
            ms = MOD_STYLE.get(mod)
            nch = sum(1 for c in MS.CHARS if MS.chara_lora(mod, c, ms)["ok"])
            print("  %-10s %3d件%s  絵柄: %s  敵キャラLoRA %d/5" % (mod, len(names), ("（撮り済み %d件は飛ばす）" % len(skip)) if skip else "",
                  ("%s（主人公LoRA %s）" % (ms["name"], "あり" if ms["hero_ok"] and not NO_STYLE_HERO else "なし")) if ms else "標準",
                  0 if NO_CHARA else nch))
        if SOLO_ONANIE:
            if HERE not in sys.path:      # ComfyUI 付属の Python は gen.py のフォルダを探さないので足す
                sys.path.insert(0, HERE)
            import solo_onanie
            for n in names:
                if "_onanie_" in n:
                    P[n] = dict(P[n], positive=solo_onanie.solo(P[n]["positive"]), negative=solo_onanie.solo_neg(P[n]["negative"]))
        jobs += [(mod, n, P[n]) for n in names]
    if a.pose_report:
        pose_report(jobs, lora)
        return
    if a.style_compare:
        if MODEL.get("loader") != "ckpt":
            print("[中止] --style-compare は wai（SDXL）用です（--model wai を付けてください）"); sys.exit(1)
        pics = style_pick(jobs, lora)
        jobs = []
        log = ["絵柄LoRAの差し替え比較（%s）" % time.strftime("%Y-%m-%d %H:%M"),
               "本編の絵柄LoRA（%s*）を外して候補1枚に差し替え。anime_screencap・主人公LoRA・構図LoRAの自動割当は標準のまま" % STYLE_BASE,
               "", "撮った絵（シードは画像ごとに固定の2つ・全条件で同じ）:"]
        for no, label, mod, n, e in pics:
            sd = style_seeds(n)
            log.append("  %s_%s: %s / %s  seed1=%d  seed2=%d" % (no, label, mod, n, sd[0], sd[1]))
            for cond, f, st, trg in STYLE_CANDS:
                d = os.path.join(OUTROOT, STYLE_DIR, cond)
                for k, s in enumerate(sd, 1):
                    if not a.redo and os.path.isdir(d) and any(re.match(r"%s_%s_s%d_\d{5}_\.png$" % (no, re.escape(label), k), x) for x in os.listdir(d)):
                        continue   # 撮り済み（--redo で撮り直し）。v2 などの新しい条件だけ撮れる
                    jobs.append((mod, n, e, "%s/%s/%s_%s_s%d" % (STYLE_DIR, cond, no, label, k), False, s,
                                 {"lora_name": f, "strength": st, "trigger": trg} if f else {}))
        log += ["", "条件:"] + ["  %s: %s%s" % (c, (f + "  強さ %s" % st) if f else "絵柄LoRAなし", ("  トリガー " + t) if t else "")
                                 for c, f, st, t in STYLE_CANDS]
        print("\n".join(log))
        print("合計 %d枚 → output\\%s\\<条件>\\" % (len(jobs), STYLE_DIR))
    else:
        print("モデル: %s  → 保存先 output\\<MODコード>%s\\%s" % (MODEL["label"], MODEL["out_suffix"] if not a.out else "（" + a.out + "）",
              "（絵柄を割り当てたMODは <MODコード>%s_<絵柄>）" % MODEL["out_suffix"] if not a.out and any(MOD_STYLE.values()) else ""))
        print("合計 %d件（1枚20秒ほど → 約%.1f時間）" % (len(jobs), len(jobs) * 20 / 3600.0))
    if MODEL.get("loader") == "ckpt":
        sl = sdxl_loras()
        print("  SDXL用LoRA: %s" % (", ".join("%s  強さ %s" % (L["lora_name"], L.get("strength")) for L in sl) or "使わない"))
    for k, label in (("style", "絵柄LoRA"), ("hero", "主人公LoRA")):
        L = lora[k]
        print("  %s: %s" % (label, ("%s  強さ %s" % (L["lora_name"], L["strength"])) if truthy(L.get("enabled"))
                            else ("使わない（Anima 用のため SDXL では外す）" if not MODEL.get("lora", True) else "使わない")))
    if a.dry_run or not jobs:
        return

    # ComfyUI の確認（LoRA ファイル・背景除去ノード）
    try:
        info = get_json("/object_info/LoraLoaderModelOnly")
        have = info["LoraLoaderModelOnly"]["input"]["required"]["lora_name"][0]
        for k in ("style", "hero"):
            if truthy(lora[k].get("enabled")) and lora[k]["lora_name"] not in have:
                print("[中止] ComfyUI の models\\loras に %s がありません。" % lora[k]["lora_name"]); sys.exit(1)
        for L in sdxl_loras():
            if L["lora_name"] not in have:
                print("[中止] ComfyUI の models\\loras に %s がありません（ComfyUI を再起動すると一覧に出ます）。" % L["lora_name"]); sys.exit(1)
        for ms in {id(x): x for x in MOD_STYLE.values() if x}.values():   # MODごとの絵柄LoRA
            for f in [ms["lora"]] + ([ms["hero_lora"]] if ms["hero_ok"] and not NO_STYLE_HERO else []):
                if f and f not in have and f.replace("\\", "/") not in have:
                    print("[中止] ComfyUI に %s がありません（絵柄 %s。ComfyUI を再起動すると一覧に出ます）。" % (f, ms["name"])); sys.exit(1)
        if not NO_CHARA:   # 敵キャラLoRA（loras\キャラ に有るのに ComfyUI の一覧に無い＝再起動が必要）
            for mod in mods:
                for c in MS.CHARS:
                    cl = MS.chara_lora(mod, c, MOD_STYLE.get(mod))
                    if cl["ok"] and cl["lora_name"] not in have and cl["lora_name"].replace("\\", "/") not in have:
                        print("[中止] ComfyUI の一覧に %s がありません（ComfyUI を再起動してください）。" % cl["lora_name"]); sys.exit(1)
        # 構図LoRA：無いものは止めずに、その画像だけ外して撮る
        if MODEL.get("loader") == "ckpt" and not NO_POSE and truthy(POSE_CFG.get("enabled")) and POSE_LIST:
            POSE_HAVE = set(get_json("/object_info/LoraLoader")["LoraLoader"]["input"]["required"]["lora_name"][0])
            miss = sorted({p["file"] for p in POSE_LIST if p.get("enabled") is not False and pose_file(p) is None})
            print("  構図LoRA: %d件%s%s" % (len([p for p in POSE_LIST if p.get("enabled") is not False]),
                                          "（強さ ×%s）" % POSE_SCALE if POSE_SCALE != 1.0 else "",
                                          ("　ComfyUI に無い %d件（その画像は外して撮る）: %s" % (len(miss), ", ".join(miss))) if miss else "　全部あり"))
        elif MODEL.get("loader") == "ckpt":
            print("  構図LoRA: 使わない")
    except SystemExit:
        raise
    except Exception as ex:
        print("[中止] ComfyUI に接続できません（起動していますか？）:", ex); sys.exit(1)
    if MODEL["loader"] == "ckpt":
        try:
            ck = get_json("/object_info/CheckpointLoaderSimple")["CheckpointLoaderSimple"]["input"]["required"]["ckpt_name"][0]
        except Exception as ex:
            print("[中止] ComfyUI からチェックポイント一覧を取れません:", ex); sys.exit(1)
        if MODEL["ckpt_name"] not in ck:
            print("[中止] ComfyUI の models\\checkpoints に %s がありません。" % MODEL["ckpt_name"])
            print("       models\\loras に置いた場合は models\\checkpoints へ移して、ComfyUI を再起動してください。"); sys.exit(1)
    if truthy(FACE_DETAIL.get("enabled")) and not NO_FACE_DETAIL and MODEL.get("loader") == "ckpt":
        try:
            FD_OK = bool(get_json("/object_info/FaceDetailer")) and FACE_DETAIL["model"] in \
                get_json("/object_info/UltralyticsDetectorProvider")["UltralyticsDetectorProvider"]["input"]["required"]["model_name"][0]
        except Exception:
            FD_OK = False
        print("  顔の描き直し: %s" % (("FaceDetailer（%s・強さ %s）" % (FACE_DETAIL["model"], FACE_DETAIL["denoise"])) if FD_OK
                                  else "使えない（Impact Pack か %s が無い）→ 描き直しなしで撮る" % FACE_DETAIL["model"]))
    global HOOK_OK
    try:
        HOOK_OK = bool(get_json("/object_info/CreateHookLora")) and bool(get_json("/object_info/SetClipHooks"))
    except Exception:
        HOOK_OK = False
    print("  キャラLoRAを相手の範囲だけにかける（LoRAフック）: %s" % ("使える" if HOOK_OK else "使えない（ComfyUI が古い）→ 画面全体にかける"))
    try:
        use_rmbg = bool(get_json("/object_info/InspyrenetRembg"))
    except Exception:
        use_rmbg = False
    if not use_rmbg:
        print("(背景除去ノード InspyrenetRembg が無いので、立ち絵も背景ありで保存します)")

    if a.style_compare:
        try:
            have = set(get_json("/object_info/LoraLoader")["LoraLoader"]["input"]["required"]["lora_name"][0])
        except Exception as ex:
            print("[中止] ComfyUI から LoRA 一覧を取れません:", ex); sys.exit(1)
        for cond, f, st, trg in STYLE_CANDS:
            if f and f not in have and f.replace("\\", "/") not in have:
                print("  [注意] %s の %s が ComfyUI に無いので、この条件は撮りません" % (cond, f))
                jobs = [j for j in jobs if not j[3].startswith("%s/%s/" % (STYLE_DIR, cond))]
        os.makedirs(os.path.join(OUTROOT, STYLE_DIR), exist_ok=True)
        with open(os.path.join(OUTROOT, STYLE_DIR, "撮影ログ.txt"), "a", encoding="utf-8") as lf:
            lf.write("\n".join(log) + "\n\n")
    if a.control_sample:
        only = [x.strip() for x in (a.control_id or "").split(",") if x.strip()]
        jobs = control_sample_jobs(jobs, lora, a.control_sample, only)
        if not jobs:
            print("構図の下書きが当たる場面がありません（model.json の pose_control.by_pose を確認）。"); return
        print("構図の下書きの確認: %d枚（下書きあり／なし・同じシード）→ output\\構図下書き確認\\<下書き>\\" % len(jobs))
    if a.pose_sample:
        jobs = pose_sample_jobs(jobs, lora, a.pose_sample)
        if not jobs:
            print("構図LoRAの当たる場面がありません。"); return
        print("構図LoRA比較: %d枚（あり／なし）→ output\\構図LoRA比較\\<id>\\" % len(jobs))

    t0 = time.time()
    for i, job in enumerate(jobs, 1):
        mod, n, e = job[:3]
        while queue_count() >= QUEUE_MAX:
            time.sleep(3)
        seed = a.seed if a.seed is not None else random.randint(0, 2**31 - 1) if a.random else int(hashlib.md5(("jisaku-" + n).encode()).hexdigest(), 16) % (2**31 - 1)
        if len(job) == 6:   # --control-sample：(mod, n, e, 保存先, 構図LoRAなし, 下書きなし)。絵柄・キャラは本番と同じ
            NO_CONTROL = bool(job[5]) or a.no_control
            CUR_STYLE = MOD_STYLE.get(mod)
            ch = MS.chara_of(n) if MODEL.get("loader") == "ckpt" else None
            CUR_CHARA = MS.chara_lora(mod, ch, CUR_STYLE) if ch else None
            w, used = wf(e, seed, a.batch, job[3], lora, use_rmbg, name=n, no_pose=job[4])
            CUR_STYLE = None; CUR_CHARA = None; NO_CONTROL = a.no_control
        elif len(job) > 5:   # --style-compare：(mod, n, e, 保存先, 構図LoRAなし, シード, 差し替える絵柄LoRA)
            seed, STYLE_SWAP = job[5], job[6]
            w, used = wf(e, seed, a.batch, job[3], lora, use_rmbg, name=n, no_pose=job[4])
            STYLE_SWAP = None
        elif len(job) > 3:   # --pose-sample：(mod, n, e, 保存先, 構図LoRAなし)
            w, used = wf(e, seed, a.batch, job[3], lora, use_rmbg, name=n, no_pose=job[4])
        else:
            CUR_STYLE = MOD_STYLE.get(mod)
            ch = MS.chara_of(n) if MODEL.get("loader") == "ckpt" else None
            CUR_CHARA = MS.chara_lora(mod, ch, CUR_STYLE) if ch else None
            w, used = wf(e, seed, a.batch, "%s/%s" % (a.out or out_dir(mod, CUR_STYLE), n), lora, use_rmbg, name=n)
            CUR_STYLE = None; CUR_CHARA = None
        body = json.dumps({"prompt": w}).encode("utf-8")
        try:
            urllib.request.urlopen(urllib.request.Request(SERVER + "/prompt", data=body, headers={"Content-Type": "application/json"}), timeout=30)
            el = time.time() - t0
            print(" [%d/%d] 送信: %s/%s  seed %d  LoRA:%s  (経過 %d分)" % (i, len(jobs), mod, n, seed, "+".join(used) or "なし", el // 60))
        except urllib.error.HTTPError as ex:
            print(" [エラー]", mod, n, ex, ex.read().decode("utf-8", "replace")[:500])
        except Exception as ex:
            print(" [エラー]", mod, n, ex)
        time.sleep(0.2)
    if a.style_compare:
        print("すべて送信しました。撮り終わるのを待って一覧画像を作ります（途中で閉じても、あとで --style-grid で作れます）")
        while queue_count() > 0:
            time.sleep(5)
        time.sleep(3)
        style_grid()
        return
    print("すべて送信しました。ComfyUI の処理が終わると ComfyUI\\output\\<MODコード>%s\\（絵柄を割り当てたMODは <MODコード>%s_<絵柄>\\）に保存されます。" % (MODEL["out_suffix"], MODEL["out_suffix"]))


if __name__ == "__main__":
    main()
