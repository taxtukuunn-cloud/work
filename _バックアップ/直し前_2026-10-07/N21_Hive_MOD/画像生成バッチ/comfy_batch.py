# -*- coding: utf-8 -*-
"""
N21 Hive MOD image batch generator for ComfyUI (API).
Usage:
  python comfy_batch.py --check                 # test connection / list models
  python comfy_batch.py all                     # generate all 51 images
  python comfy_batch.py all --skip-existing     # only missing images
  python comfy_batch.py Hive_lose_btl          # every key starting with this text
  python comfy_batch.py Hive_atk_m1 --random --batch 4   # 4 candidates with random seeds
  python comfy_batch.py --pick Hive_atk_m1 3   # adopt candidate 3 as the final image
  python comfy_batch.py --list                  # list keys
"""
import json, os, sys, time, random, shutil, uuid, urllib.request, urllib.parse, urllib.error, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
CONF = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
DATA = json.load(open(os.path.join(HERE, CONF.get("prompts", "hive_prompts.json")), encoding="utf-8"))
CODE = DATA["code"]
OUT = os.path.join(HERE, CONF.get("out_dir", "output"), CODE)
CAND = os.path.join(OUT, "_candidates")
SERVER = "http://" + CONF.get("server", "127.0.0.1:8188")
CLIENT = str(uuid.uuid4())


def api(path, data=None):
    req = urllib.request.Request(SERVER + path)
    if data is not None:
        req.data = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
    return body


def object_info(node=None):
    try:
        return json.loads(api("/object_info" + ("/" + node if node else "")))
    except Exception:
        return {}


def char_seed(name):
    base = int(CONF.get("seed_base", 20260923))
    fixed = CONF.get("fixed_seeds", {})
    if name in fixed:
        return int(fixed[name])
    return (base + zlib.crc32(name.encode("utf-8"))) % (2 ** 32)


# ---------- workflow ----------
def builtin_workflow(pos, neg, seed, prefix, rembg):
    if CONF.get("unet_name"):
        return anima_workflow(pos, neg, seed, prefix, rembg)
    wf = {
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CONF["ckpt_name"]}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 1]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": CONF["width"], "height": CONF["height"], "batch_size": 1}},
        "3": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": CONF["steps"], "cfg": CONF["cfg"],
                                                    "sampler_name": CONF["sampler"], "scheduler": CONF["scheduler"],
                                                    "denoise": 1.0, "model": ["4", 0], "positive": ["6", 0],
                                                    "negative": ["7", 0], "latent_image": ["5", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefix, "images": ["8", 0]}},
    }
    if CONF.get("clip_skip"):
        wf["10"] = {"class_type": "CLIPSetLastLayer", "inputs": {"stop_at_clip_layer": -int(CONF["clip_skip"]), "clip": ["4", 1]}}
        wf["6"]["inputs"]["clip"] = ["10", 0]
        wf["7"]["inputs"]["clip"] = ["10", 0]
    if rembg:
        add_rembg(wf, "8", "9")
    return wf


def anima_workflow(pos, neg, seed, prefix, rembg):
    # Anima系（UNET + CLIP(qwen_image) + VAE の3ローダー）
    wf = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": CONF["unet_name"], "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": CONF.get("clip_name", "qwen_3_06b_base.safetensors"),
                                                      "type": CONF.get("clip_type", "qwen_image")}},
        "11": {"class_type": "VAELoader", "inputs": {"vae_name": CONF.get("vae_name", "qwen_image_vae.safetensors")}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["2", 0]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["2", 0]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": CONF["width"], "height": CONF["height"], "batch_size": 1}},
        "3": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": CONF["steps"], "cfg": CONF["cfg"],
                                                    "sampler_name": CONF["sampler"], "scheduler": CONF["scheduler"],
                                                    "denoise": 1.0, "model": ["1", 0], "positive": ["6", 0],
                                                    "negative": ["7", 0], "latent_image": ["5", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["11", 0]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": prefix, "images": ["8", 0]}},
    }
    if rembg:
        add_rembg(wf, "8", "9")
    return wf


def add_rembg(wf, decode_id, save_id):
    node = CONF.get("rembg_node", "InspyrenetRembg")
    if not node or not object_info(node):
        print("   (rembg node not found - saved with background)")
        return
    wf["90"] = {"class_type": node, "inputs": {"image": [decode_id, 0], "torchscript_jit": "default"}}
    wf[save_id]["inputs"]["images"] = ["90", 0]


def template_workflow(pos, neg, seed, prefix, rembg):
    wf = json.load(open(os.path.join(HERE, CONF["template"]), encoding="utf-8"))
    ks = [k for k, v in wf.items() if "KSampler" in v.get("class_type", "") or "SamplerCustom" in v.get("class_type", "")]
    if not ks:
        sys.exit("template: no KSampler node found")
    k = ks[0]
    inp = wf[k]["inputs"]
    for s in ("seed", "noise_seed"):
        if s in inp:
            inp[s] = seed
    for name, text in (("positive", pos), ("negative", neg)):
        link = inp.get(name)
        if isinstance(link, list) and "text" in wf[link[0]]["inputs"]:
            wf[link[0]]["inputs"]["text"] = text
    for v in wf.values():
        ct = v.get("class_type", "")
        if ct.startswith("Empty") and "Latent" in ct:
            v["inputs"]["width"] = CONF["width"]
            v["inputs"]["height"] = CONF["height"]
            v["inputs"]["batch_size"] = 1
    saves = [k2 for k2, v in wf.items() if v.get("class_type") == "SaveImage"]
    if not saves:
        sys.exit("template: no SaveImage node found")
    wf[saves[0]]["inputs"]["filename_prefix"] = prefix
    if rembg:
        src = wf[saves[0]]["inputs"]["images"][0]
        add_rembg(wf, src, saves[0])
    return wf



# ---------- LoRA（2026-09-25 追加）----------
# 設定は Downloads\Lora用\lora_settings.json（全MOD共通）。config.json に "lora": {...} があればそちらを優先。
# 一時的に外す: --no-lora ／ 強さを変える: --lora-strength 0.6
LORA_SETTINGS = os.path.join(os.path.expanduser("~"), "Downloads", "Lora用", "lora_settings.json")


def lora_conf():
    if "--no-lora" in sys.argv:
        return None
    c = dict(CONF.get("lora") or {})
    if not c and os.path.exists(LORA_SETTINGS):
        try:
            c = json.load(open(LORA_SETTINGS, encoding="utf-8"))
        except Exception as e:
            print("   (lora_settings.json を読めません: %s)" % e)
            c = {}
    if not (c.get("enabled") and c.get("lora_name")):
        return None
    if "--lora-strength" in sys.argv:
        c["strength"] = float(sys.argv[sys.argv.index("--lora-strength") + 1])
    return c


def apply_lora(wf, lc):
    ks = [k for k, v in wf.items() if "KSampler" in v.get("class_type", "") or "SamplerCustom" in v.get("class_type", "")]
    if not ks:
        return wf
    src = wf[ks[0]]["inputs"]["model"]
    wf["80"] = {"class_type": "LoraLoaderModelOnly", "inputs": {"lora_name": lc["lora_name"],
                "strength_model": float(lc.get("strength", 0.8)), "model": src}}
    wf[ks[0]]["inputs"]["model"] = ["80", 0]
    return wf


def make_workflow(item, seed, prefix):
    f = template_workflow if CONF.get("template") else builtin_workflow
    pos = item["positive"]
    lc = lora_conf()
    trig = (lc or {}).get("trigger", "")
    if trig and trig not in pos:
        pos = trig + ", " + pos
    wf = f(pos, item["negative"], seed, prefix, item.get("rembg") and CONF.get("use_rembg", True))
    if lc:
        apply_lora(wf, lc)
    return wf


# ---------- run ----------
def generate(item, seed, dest):
    prefix = CODE + "/" + os.path.splitext(os.path.basename(dest))[0]
    wf = make_workflow(item, seed, prefix)
    try:
        res = json.loads(api("/prompt", {"prompt": wf, "client_id": CLIENT}))
    except urllib.error.HTTPError as e:
        print("   ERROR from ComfyUI:", e.read().decode("utf-8", "ignore")[:800])
        return False
    pid = res["prompt_id"]
    t0 = time.time()
    while True:
        time.sleep(1.5)
        h = json.loads(api("/history/" + pid))
        if pid in h:
            break
        if time.time() - t0 > CONF.get("timeout_sec", 900):
            print("   timeout")
            return False
    outs = h[pid].get("outputs", {})
    for node in outs.values():
        for im in node.get("images", []):
            q = urllib.parse.urlencode({"filename": im["filename"], "subfolder": im.get("subfolder", ""), "type": im.get("type", "output")})
            data = api("/view?" + q)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            open(dest, "wb").write(data)
            return True
    print("   no image returned (check the ComfyUI console)")
    return False


def select(pattern):
    if pattern == "all":
        return DATA["images"]
    sel = [i for i in DATA["images"] if i["key"] == pattern or i["key"].startswith(pattern)]
    if not sel:
        sys.exit("no key matches: " + pattern + "  (see --list)")
    return sel


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return
    if a[0] == "--list":
        for i in DATA["images"]:
            print(i["key"])
        return
    if a[0] == "--check":
        try:
            api("/system_stats")
        except Exception as e:
            sys.exit("cannot reach ComfyUI at " + SERVER + " : " + str(e))
        print("ComfyUI OK:", SERVER)
        ck = object_info("CheckpointLoaderSimple")
        names = ck.get("CheckpointLoaderSimple", {}).get("input", {}).get("required", {}).get("ckpt_name", [[]])[0]
        print("checkpoints:", *names, sep="\n  ")
        print("config ckpt_name:", CONF.get("ckpt_name"), "->", "FOUND" if CONF.get("ckpt_name") in names else "NOT FOUND (edit config.json)")
        un = object_info("UNETLoader").get("UNETLoader", {}).get("input", {}).get("required", {}).get("unet_name", [[]])[0]
        print("diffusion_models:", *un, sep="\n  ")
        if CONF.get("unet_name"):
            print("config unet_name:", CONF["unet_name"], "->", "FOUND" if CONF["unet_name"] in un else "NOT FOUND (edit config.json)")
        print("rembg node:", "FOUND" if object_info(CONF.get("rembg_node", "InspyrenetRembg")) else "not installed (standing images keep white background)")
        return
    if a[0] == "--pick":
        key, n = a[1], a[2]
        src = os.path.join(CAND, "%s_c%s.png" % (key, n))
        shutil.copyfile(src, os.path.join(OUT, key + ".png"))
        print("adopted", src)
        return
    items = select(a[0])
    _lc = lora_conf()
    print("LoRA:", ("%s  強さ %s" % (_lc["lora_name"], _lc.get("strength", 0.8))) if _lc else "使わない")
    rnd = "--random" in a
    batch = int(a[a.index("--batch") + 1]) if "--batch" in a else 1
    skip = "--skip-existing" in a
    ok = ng = 0
    for n, it in enumerate(items, 1):
        final = os.path.join(OUT, it["key"] + ".png")
        if skip and batch == 1 and os.path.exists(final):
            continue
        for b in range(1, batch + 1):
            seed = random.randint(0, 2 ** 32 - 1) if rnd or b > 1 else char_seed(it["seed_char"])
            dest = os.path.join(CAND, "%s_c%d.png" % (it["key"], b)) if batch > 1 else final
            print("[%d/%d] %s  seed=%d%s" % (n, len(items), it["key"], seed, "  cand %d" % b if batch > 1 else ""))
            if generate(it, seed, dest):
                ok += 1
            else:
                ng += 1
    print("done: %d ok / %d failed  ->  %s" % (ok, ng, OUT))
    if batch > 1:
        print("pick one with:  run_hive.bat --pick <key> <number>")


if __name__ == "__main__":
    main()
