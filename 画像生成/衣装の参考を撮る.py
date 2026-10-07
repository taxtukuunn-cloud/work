# -*- coding: utf-8 -*-
"""女装の場面：主人公ひとりが設定の衣装を着た絵（参考画像）を撮って、ComfyUI\\input\\outfit_ref_<画像名>.png に置く（2026-10-03）
2人の場面では文で衣装を書くと相手に移るので、ひとりの絵で衣装を確定させ、gen.py --outfit-ref で主人公の位置だけに効かせる。
使い方： python 衣装の参考を撮る.py --out 確認22_参考\\参考の絵  MOD:画像名 ...
"""
import os, sys, json, re, time, argparse, shutil, urllib.request, urllib.error, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

HOME = os.path.expanduser("~")
COMFY = os.path.join(HOME, "Downloads", "ComfyUI_windows_portable", "ComfyUI")
INPUT, OUTPUT = os.path.join(COMFY, "input"), os.path.join(COMFY, "output")
LORA_DIR = os.path.join(COMFY, "models", "loras")
SERVER = "http://127.0.0.1:8188"


def post(path, data):
    req = urllib.request.Request(SERVER + path, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def get(path):
    with urllib.request.urlopen(SERVER + path, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def outfit_of(gen, pos):
    o = gen._hero_outfit(pos)
    for rx, b in gen.SAFETY.get("_subs", []):
        o = rx.sub(b, o)
    o = re.sub(r"^only\s+", "", re.sub(r"^[^,:]{0,40}:\s*", "", o))
    o = re.sub(r"\b(?:on|over) his flat chest\b", "", o)
    o = re.sub(r"\s*\bopen at the crotch\b|\s*\bcrotchless\b", "", o)   # 参考の絵は着衣の立ち姿だけ
    return re.sub(r"\s{2,}", " ", o).strip(" ,")


RMBG = False
BG = (118, 112, 108)   # 参考画像の背景：白ではなく落ち着いた中間の色


def workflow(M, style, pos, neg, seed, prefix, hero=None, hero_w=0.0):
    w = {"3": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": M["ckpt_name"]}}}
    mo, co = ["3", 0], ["3", 1]
    if style and style.get("lora") and os.path.isfile(os.path.join(LORA_DIR, style["lora"])):
        w["30"] = {"class_type": "LoraLoader", "inputs": {"model": mo, "clip": co, "lora_name": style["lora"],
                   "strength_model": float(style.get("strength", 0.6)), "strength_clip": float(style.get("strength", 0.6))}}
        mo, co = ["30", 0], ["30", 1]
    if hero and hero_w > 0 and os.path.isfile(os.path.join(LORA_DIR, hero)):   # 主人公LoRA：顔つき・髪を本編の主人公（大人の男性）に寄せる
        w["31"] = {"class_type": "LoraLoader", "inputs": {"model": mo, "clip": co, "lora_name": hero,
                   "strength_model": float(hero_w), "strength_clip": float(hero_w)}}
        mo, co = ["31", 0], ["31", 1]
    w["4"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": co, "stop_at_clip_layer": int(M.get("clip_skip", -2))}}
    w["6"] = {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 0], "text": pos}}
    w["7"] = {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 0], "text": neg}}
    w["8"] = {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}}
    w["9"] = {"class_type": "KSampler", "inputs": {"model": mo, "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0],
              "seed": seed, "steps": int(M.get("steps", 28)), "cfg": float(M.get("cfg", 6.0)),
              "sampler_name": M.get("sampler", "euler_ancestral"), "scheduler": M.get("scheduler", "normal"), "denoise": 1.0}}
    w["10"] = {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 2]}}
    w["11"] = {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": prefix}}
    if RMBG:   # 背景を抜いた版も保存（参考画像の白い背景が、2人の場面で白い光のにじみ・色の飛びになった対策）
        w["12"] = {"class_type": "InspyrenetRembg", "inputs": {"image": ["10", 0], "torchscript_jit": "default"}}
        w["13"] = {"class_type": "SaveImage", "inputs": {"images": ["12", 0], "filename_prefix": prefix + "_cut"}}
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="確認22_参考\\参考の絵")
    ap.add_argument("--hero", type=float, default=0.7, help="主人公LoRAの強さ（0＝使わない）")
    ap.add_argument("--seed-add", type=int, default=0, help="同じ場面を別の絵で撮り直すときに足す数")
    ap.add_argument("items", nargs="+")
    a = ap.parse_args()
    try:
        get("/system_stats")
    except Exception as e:
        print("[中止] ComfyUI に接続できません（起動していますか？）:", e); return 1
    try:
        get("/object_info/IPAdapterAdvanced")["IPAdapterAdvanced"]
    except Exception:
        print("[中止] ComfyUI に参考画像の部品（IPAdapterAdvanced）が見つかりません。ComfyUI を起動し直してください。"); return 1
    global RMBG
    try:
        RMBG = bool(get("/object_info/InspyrenetRembg").get("InspyrenetRembg"))
    except Exception:
        RMBG = False
    import gen
    import mod_style as MS
    gen.load_scene_safety()
    M = gen.MODELS["wai"]
    cfg_all = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    styles = (cfg_all.get("mod_style") or {}).get("styles") or {}
    assign = MS.read_csv()
    jobs = []
    for it in a.items:
        mod, name = it.split(":", 1)
        P = json.load(open(os.path.join(HERE, "prompts", mod + ".json"), encoding="utf-8"))
        key = name if name in P else name[len(mod) + 1:]
        outfit = outfit_of(gen, P[key]["positive"])
        print("■ %s  衣装: %s" % (name, outfit or "（拾えない）"))
        if not outfit:
            print("   → 飛ばす"); continue
        st = styles.get(assign.get(mod, ""), {})
        trig = (st.get("trigger") or "").strip()
        # 2026-10-03 その2：1回目は顔が丸く目を閉じた幼い少女のように出た（使わない）→ 大人の男性の顔つき・頭身を強く書き、主人公LoRAも使う。
        # 参考画像は中央の正方形しか見ないので、頭から太ももまでが入る構図に固定する
        MSY = cfg_all.get("mod_style") or {}
        hero, htrig = MSY.get("hero_lora") or "", (MSY.get("hero_trigger") or "sdduel_hero")
        pos = ", ".join(x for x in [trig, htrig if a.hero > 0 else "", M.get("quality_pos", "masterpiece, best quality"),
               "1boy, solo, (adult man:1.2), 27 years old, (mature adult male face:1.2), narrow eyes, sharp adult jawline, adam's apple, "
               "long legs, adult proportions, navy blue hair, (very short hair:1.2), hair above the ears, short bangs above the eyes, fair pale skin, "
               "slim adult male build, slender, slim shoulders, slim neck, not muscular, flat male chest, crossdressing, (%s:1.3), fully clothed, "
               "women's clothes in a slim fitted cut, fitted at the shoulders and waist, narrow waist" % outfit,
               "full body, (whole head in frame:1.2), face visible, space above the head, feet in frame, standing straight, facing viewer, looking at viewer, open eyes, troubled expression, blush, "
               "simple background, white background"] if x)
        neg = ", ".join(x for x in [M.get("quality_neg", "worst quality, low quality"), gen.SAFETY.get("hero_neg", "child, shota"),
               "1girl, girl, woman, female, breasts, cleavage, cute, big eyes, large eyes, round face, big head, short stature, petite, loli, chibi, "
               "closed eyes, blindfold, mask, eyes covered, (head out of frame:1.3), cropped head, faceless, lower body only, legs only, close-up, upper body only, cowboy shot, "
               "oversized clothes, boxy jacket, baggy clothes, loose jacket, shoulder pads, men's suit, "
               "2boys, multiple people, long hair, medium hair, shoulder-length hair, bob cut, wig, "
               "naked, nude, topless, nipples, muscular, broad shoulders, wide shoulders, bulky, stocky, thick neck, large hands, beard, text, watermark, extra arms, bad hands"] if x)
        seed = (int(hashlib.md5(("outfitref-" + name).encode()).hexdigest(), 16) + a.seed_add) % (2 ** 31 - 1)
        try:
            pid = post("/prompt", {"prompt": workflow(M, st, pos, neg, seed, "%s/%s" % (a.out.replace("\\", "/"), name), hero, a.hero)})["prompt_id"]
        except urllib.error.HTTPError as e:
            print("   [送れない] %s" % e.read().decode("utf-8", "replace")[:600]); continue
        jobs.append((name, pid))
    t0 = time.time(); ok = 0
    for name, pid in jobs:
        h = {}
        while time.time() - t0 < 1800:
            h = get("/history/" + pid)
            if pid in h:
                break
            time.sleep(3)
        try:
            im = h[pid]["outputs"]["11"]["images"][0]
            src = os.path.join(OUTPUT, im.get("subfolder", ""), im["filename"])
            # 参考画像は中央の正方形しか見ない → 人物だけを切り出し、中間色の正方形の中央に置く
            from PIL import Image
            im0 = Image.open(src).convert("RGB"); bg = (255, 255, 255)
            cut = (h[pid]["outputs"].get("13") or {}).get("images")
            if cut:   # 背景を抜いた版があれば、その透明部分で人物の範囲を決め、背景を中間色にする
                c0 = Image.open(os.path.join(OUTPUT, cut[0].get("subfolder", ""), cut[0]["filename"])).convert("RGBA")
                al = c0.split()[3]; bb = al.point(lambda v: 255 if v > 40 else 0).getbbox()
                base = Image.new("RGB", c0.size, BG); base.paste(c0, (0, 0), al); im0, bg = base, BG
            else:
                from PIL import ImageChops
                bb = ImageChops.difference(im0, Image.new("RGB", im0.size, im0.getpixel((2, 2)))).convert("L").point(lambda v: 255 if v > 24 else 0).getbbox()
            if bb and (bb[2] - bb[0]) > im0.width * 0.15:
                m_ = 12
                bb = (max(0, bb[0] - m_), max(0, bb[1] - m_), min(im0.width, bb[2] + m_), min(im0.height, bb[1] + int((bb[3] - bb[1]) * 0.72)))   # 頭〜ひざ上
                im0 = im0.crop(bb)
            sd = max(im0.size)
            sq = Image.new("RGB", (sd, sd), bg); sq.paste(im0, ((sd - im0.width) // 2, (sd - im0.height) // 2))
            sq.save(os.path.join(INPUT, "outfit_ref_%s.png" % name)); ok += 1
            print("  参考の絵を置いた: outfit_ref_%s.png" % name)
        except Exception as e:
            print("  [失敗] %s: %s" % (name, e))
    print("終わりました（%d／%d 枚）。保存先: %s" % (ok, len(a.items), os.path.join(OUTPUT, a.out)))
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
