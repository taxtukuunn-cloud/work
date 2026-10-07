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
SERVER = "http://127.0.0.1:8188"
OUTROOT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
ADULT_NEG = ("child, loli, shota, young boy, young girl, kid, teenage, underage, immature, childlike, child body, "
             "youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, flat-chested child")
ADULT_POS = "adult male, mature face, adult proportions"
ADULT_POS_FRESH = "adult male, early 20s, fresh face, adult proportions"
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
HERO_POS_FRESH = ("the navy-haired man is an adult man in his early twenties with a fresh smooth handsome face and a slim adult build, "
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
             "build": "bishounen, delicate features, slender, narrow shoulders, thin arms, slim waist",
             "build_neg": "broad shoulders on the navy-haired man, thick arms, thick neck, manly, masculine build, stocky, square jaw",
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
    (re.compile(r"adult man, mature male, 25 years old, adult male body,"),
     "adult man, 20 years old, fresh-faced adult man, handsome soft face, smooth clear skin, adult male body,"),
    (re.compile(r"(slim adult build, lean, not muscular, (?:no muscles, )?)defined jawline"), r"\1slim smooth jawline"),
    # 場面の最後に付く主人公の年齢（約630件）
    (re.compile(r"adult male, 20s, mature face, adult proportions"), "adult male, early 20s, fresh face, adult proportions"),
    # 女装娘の立ち絵（Oiran・Lingerie・Revue の _josou）
    (re.compile(r"adult man, 20s, mature face,"), "adult man, early 20s, fresh-faced, handsome soft face,"),
]
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
        if not isinstance(p, dict) or not p.get("id") or not p.get("file"):
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
]
STYLE_PICS = [("1", "立ち絵"), ("2", "ペニバン"), ("3", "キス"), ("4", "主人公")]
STYLE_DIR = "絵柄比較"


def sdxl_loras():
    """wai（SDXL）で重ねる LoRA の一覧。strength が 0 以下のものは使わない。
    "when_text_contains": "navy" があれば、その語を含む絵（主人公が出る絵）だけに使う。
    "role": "hero" は主人公LoRA（使う場面では主人公の目隠れの文字指定を外して LoRA に任せる）。"""
    if MODEL.get("loader") != "ckpt":
        return []
    out = []
    for L in MODEL.get("loras") or []:
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
            pos = rx.sub(rep, pos)
    if "navy" in pos.lower() and "mature face" not in pos and "fresh face" not in pos:
        pos = pos.rstrip(", ") + ", " + (ADULT_POS_FRESH if fresh else ADULT_POS)
    neg = e["negative"].rstrip(", ") + ", " + ADULT_NEG
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
        eyes = ", ".join(x for x in (HERO_FACE.get("eyes", "aqua eyes"), HERO_FACE.get("bangs", "short bangs above the eyes"),
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
        hp = HERO_POS_FRESH if fresh else HERO_POS
        if HERO_FACE.get("show"):
            hp += ", %s, his face and eyes are visible, slender with narrow shoulders" % HERO_FACE.get("eyes", "aqua eyes")
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
    LAST_POSE = {"scene": scene, "picked": [], "missing": []}
    if scene and "scene" in (POSE_CFG.get("apply_to") or ["scene"]) and MODEL.get("loader") == "ckpt" and not no_pose:
        for p, hits in pick_pose(name, pos):
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
    if use_rmbg and truthy(e.get("rmbg")):
        w["12"] = {"class_type": "InspyrenetRembg", "inputs": {"image": ["10", 0], "torchscript_jit": "default"}}
        w["11"]["inputs"]["images"] = ["12", 0]
    return w, used


def get_json(path, timeout=10):
    with urllib.request.urlopen(SERVER + path, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def queue_count():
    try:
        q = get_json("/queue")
        return len(q.get("queue_running", [])) + len(q.get("queue_pending", []))
    except Exception:
        return 0


def done_names(mod):
    d = os.path.join(OUTROOT, mod + MODEL["out_suffix"])
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
            out.append((mod, n, e, LAST_POSE["picked"]))
    return out


def pose_report(jobs, lora):
    """--pose-report：割当を 構図LoRA_割当.csv に書き出し、LoRAごとの件数を表示する。"""
    import csv
    from collections import Counter
    res = pose_assign(jobs, lora)
    path = os.path.join(HERE, "構図LoRA_割当.csv")
    cnt, none = Counter(), 0
    with open(path, "w", encoding="utf-8-sig", newline="") as f:   # Excel で開けるよう BOM 付き
        wr = csv.writer(f)
        wr.writerow(["MOD", "画像名", "action", "look", "当てはまった語"])
        for mod, n, e, picked in res:
            act = [p["id"] for p, _ in picked if p.get("kind", "action") == "action"]
            look = [p["id"] for p, _ in picked if p.get("kind") == "look"]
            words = " / ".join("%s: %s" % (p["id"], " + ".join(h)) for p, h in picked)
            wr.writerow([mod, n, ",".join(act), ",".join(look), words])
            for p, _ in picked:
                cnt[p["id"]] += 1
            if not picked:
                none += 1
    print("\n構図LoRAの割当（場面 %d件）→ %s" % (len(res), path))
    for p in POSE_LIST:
        if p.get("enabled") is False and not cnt[p["id"]]:
            continue
        print("  %-14s %-6s %5d件" % (p["id"], p.get("kind", "action"), cnt[p["id"]]))
    print("  どれにも当たらなかった場面: %d件" % none)
    if not truthy(POSE_CFG.get("enabled")) or NO_POSE:
        print("  （構図LoRAは今オフです：model.json の pose_lora.enabled か --no-pose）")


def pose_sample_jobs(jobs, lora, n_each):
    """--pose-sample N：構図LoRAごとに場面を N 件（MOD をまたいで散らして）選び、あり／なしの2枚ずつにする。"""
    res = pose_assign(jobs, lora)
    by = {}
    for mod, n, e, picked in res:
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
        for mod, n, e, picked in pool:
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
    ap.add_argument("--style-compare", action="store_true", help="本編の絵柄LoRAを候補に差し替えて4枚×2シードを撮り、一覧画像を作る（MOD指定は無視して全MODから選ぶ）")
    ap.add_argument("--style-grid", action="store_true", help="撮り終わった絵柄比較から一覧画像だけ作り直す")
    a = ap.parse_args()
    if a.style_grid:
        style_grid()
        return
    global NO_POSE, POSE_SCALE, POSE_HAVE, SOLO_ONANIE, STYLE_SWAP
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
    lora = load_lora(a)
    if not MODEL.get("lora", True):
        lora["style"]["enabled"] = False; lora["hero"]["enabled"] = False

    # 送る一覧を作る
    jobs = []
    for mod in mods:
        P = json.load(open(os.path.join(pdir, mod + ".json"), encoding="utf-8"))
        if a.keys == "all":
            names = list(P)
        else:
            parts = [x.strip() for x in a.keys.split(",") if x.strip()]
            names = [n for n in P if any(x in n for x in parts)]
        done = set() if (a.redo or a.out or a.pose_report or a.pose_sample or a.style_compare) else done_names(mod)
        skip = [n for n in names if n in done]
        names = [n for n in names if n not in done]
        if not a.style_compare:
            print("  %-10s %3d件%s" % (mod, len(names), ("（撮り済み %d件は飛ばす）" % len(skip)) if skip else ""))
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
        print("モデル: %s  → 保存先 output\\<MODコード>%s\\" % (MODEL["label"], MODEL["out_suffix"] if not a.out else "（" + a.out + "）"))
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
        if len(job) > 5:   # --style-compare：(mod, n, e, 保存先, 構図LoRAなし, シード, 差し替える絵柄LoRA)
            seed, STYLE_SWAP = job[5], job[6]
            w, used = wf(e, seed, a.batch, job[3], lora, use_rmbg, name=n, no_pose=job[4])
            STYLE_SWAP = None
        elif len(job) > 3:   # --pose-sample：(mod, n, e, 保存先, 構図LoRAなし)
            w, used = wf(e, seed, a.batch, job[3], lora, use_rmbg, name=n, no_pose=job[4])
        else:
            w, used = wf(e, seed, a.batch, "%s/%s" % (a.out or (mod + MODEL["out_suffix"]), n), lora, use_rmbg, name=n)
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
    print("すべて送信しました。ComfyUI の処理が終わると ComfyUI\\output\\<MODコード>%s\\ に保存されます。" % MODEL["out_suffix"])


if __name__ == "__main__":
    main()
