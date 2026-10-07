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
ADD_LORAS = []              # --add-lora ファイル名:強さ[:トリガー] で一時的に足す（比較用）


def sdxl_loras():
    """wai（SDXL）で重ねる LoRA の一覧。strength が 0 以下のものは使わない。"""
    if MODEL.get("loader") != "ckpt":
        return []
    out = []
    for L in MODEL.get("loras") or []:
        if not isinstance(L, dict) or not L.get("lora_name") or L.get("enabled") is False:
            continue
        L = dict(L)
        if SDXL_LORA_STRENGTH is not None:
            L["strength"] = SDXL_LORA_STRENGTH; L["clip_strength"] = SDXL_LORA_STRENGTH
        if float(L.get("strength", 0.8)) <= 0:
            continue
        out.append(L)
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


def wf(e, seed, batch, prefix, lora, use_rmbg):
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
    if scene and hero_on and EYES_TEXT == "strip":
        pos = HIDE_RE.sub("", pos)
        pos = SHUT_RE.sub("", pos)
        neg = NEG_EYES_RE.sub("", neg)
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
        head, tail = [HERO_POS_FRESH if fresh else HERO_POS], [HERO_NEG]
        if ("femboy" in P0 or "otoko no ko" in P0) and "1girl" not in P0 and "woman" not in P0:
            head.append(FEMBOY_POS); tail.append(FEMBOY_NEG)
        if "naked navy" in P0 and "crossdress" not in P0:
            head.append(NAKED_POS); tail.append(NAKED_NEG)
        pos = ", ".join(head) + ", " + pos
        neg = neg + ", " + ", ".join(tail)
    if FACE_FIX and scene and "crossdress" in e["positive"]:
        pos = DRESS_POS + ", " + pos
        neg = neg + ", " + DRESS_NEG
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
    ap.add_argument("--add-lora", action="append", default=[], help="wai に LoRA を一時的に足す：ファイル名:強さ[:トリガー]（何度でも）")
    a = ap.parse_args()
    global FACE_FIX, EYES_TEXT, FACE_LEVEL, HERO_AGE, MODEL, SDXL_LORA_STRENGTH
    MODEL = load_model(a.model)
    SDXL_LORA_STRENGTH = a.sdxl_lora_strength
    for x in a.add_lora:
        parts = x.split(":", 2)
        name = parts[0] if parts[0].endswith(".safetensors") else parts[0] + ".safetensors"
        st = float(parts[1]) if len(parts) > 1 and parts[1] else 0.6
        ADD_LORAS.append({"lora_name": name, "strength": st, "clip_strength": st, "trigger": parts[2] if len(parts) > 2 else ""})
    if a.hero_age:
        HERO_AGE = a.hero_age
    if a.face_level:
        FACE_LEVEL = a.face_level
    FACE_FIX = not a.no_face_fix
    if a.eyes_text:
        EYES_TEXT = a.eyes_text
    pdir = os.path.join(HERE, "prompts")
    allmods = sorted(f[:-5] for f in os.listdir(pdir) if f.endswith(".json"))
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
        done = set() if (a.redo or a.out) else done_names(mod)
        skip = [n for n in names if n in done]
        names = [n for n in names if n not in done]
        print("  %-10s %3d件%s" % (mod, len(names), ("（撮り済み %d件は飛ばす）" % len(skip)) if skip else ""))
        jobs += [(mod, n, P[n]) for n in names]
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

    t0 = time.time()
    for i, (mod, n, e) in enumerate(jobs, 1):
        while queue_count() >= QUEUE_MAX:
            time.sleep(3)
        seed = a.seed if a.seed is not None else random.randint(0, 2**31 - 1) if a.random else int(hashlib.md5(("jisaku-" + n).encode()).hexdigest(), 16) % (2**31 - 1)
        w, used = wf(e, seed, a.batch, "%s/%s" % (a.out or (mod + MODEL["out_suffix"]), n), lora, use_rmbg)
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
    print("すべて送信しました。ComfyUI の処理が終わると ComfyUI\\output\\<MODコード>%s\\ に保存されます。" % MODEL["out_suffix"])


if __name__ == "__main__":
    main()
