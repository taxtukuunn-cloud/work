# -*- coding: utf-8 -*-
"""MOD画像の自作用 一括生成ツール（2026-09-26）
使い方: python gen.py <MODコード> [all|名前の一部,名前の一部...] [--random] [--batch N]
・prompts\<MODコード>.json を ComfyUI（Anima）に送る。出力は ComfyUI\output\<MODコード>_自作\
・絵柄LoRA（sdduel_style）と主人公LoRA（sdduel_hero、主人公が出る絵だけ）は Lora用\lora_hook.py で自動的に入る
・登場人物はすべて成人。幼く見える絵を避けるタグを毎回ネガティブに必ず足す（このツールでは外せない）
"""
import argparse, copy, hashlib, json, os, random, sys, time, urllib.request
try:
    sys.path.insert(0, os.path.join(os.path.expanduser("~"), "Downloads", "Lora用")); import lora_hook  # noqa
except Exception as e:
    print("(LoRA設定を読み込めませんでした:", e, ")")

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = "http://127.0.0.1:8188"
ADULT_NEG = ("child, loli, shota, young boy, young girl, kid, teenage, underage, immature, childlike, child body, "
             "youthful body, baby face, round face, chubby cheeks, short limbs, big head, chibi, petite male, flat-chested child")
ADULT_POS = "adult male, mature face, adult proportions"

def wf(e, seed, batch, prefix):
    pos = e["positive"]
    if "navy" in pos and "mature face" not in pos:
        pos = pos.rstrip(", ") + ", " + ADULT_POS
    neg = e["negative"].rstrip(", ") + ", " + ADULT_NEG
    w = {
     "3": {"class_type": "UNETLoader", "inputs": {"unet_name": "waiANIMA_v10Base10.safetensors", "weight_dtype": "default"}},
     "4": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_06b_base.safetensors", "type": "qwen_image"}},
     "5": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_vae.safetensors"}},
     "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["4", 0]}},
     "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 0]}},
     "8": {"class_type": "EmptyLatentImage", "inputs": {"width": e.get("width", 832), "height": e.get("height", 1216), "batch_size": batch}},
     "9": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": 36, "cfg": 4.5, "sampler_name": "er_sde", "scheduler": "simple",
           "denoise": 1.0, "model": ["3", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0]}},
     "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["5", 0]}},
     "11": {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": prefix}},
    }
    if e.get("rmbg"):
        w["12"] = {"class_type": "InspyrenetRembg", "inputs": {"image": ["10", 0], "torchscript_jit": "default"}}
        w["11"]["inputs"]["images"] = ["12", 0]
    return w

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mod"); ap.add_argument("keys", nargs="?", default="all")
    ap.add_argument("--random", action="store_true"); ap.add_argument("--batch", type=int, default=1)
    a = ap.parse_args()
    p = os.path.join(HERE, "prompts", a.mod + ".json")
    if not os.path.exists(p):
        print("見つかりません:", p); print("使えるMODコード:", ", ".join(sorted(f[:-5] for f in os.listdir(os.path.join(HERE, "prompts"))))); sys.exit(1)
    P = json.load(open(p, encoding="utf-8"))
    if a.keys == "all":
        names = list(P)
    else:
        parts = [x.strip() for x in a.keys.split(",") if x.strip()]
        names = [n for n in P if any(x in n for x in parts)]
    if not names:
        print("該当する画像がありません。名前の一覧は prompts\\%s.json を見てください。" % a.mod); sys.exit(1)
    print("=== %s：%d件 → ComfyUI\\output\\%s_自作\\ ===" % (a.mod, len(names), a.mod))
    for n in names:
        seed = random.randint(0, 2**31 - 1) if a.random else int(hashlib.md5(("jisaku-" + n).encode()).hexdigest(), 16) % (2**31 - 1)
        body = json.dumps({"prompt": wf(P[n], seed, a.batch, "%s_自作/%s" % (a.mod, n))}).encode("utf-8")
        try:
            urllib.request.urlopen(urllib.request.Request(SERVER + "/prompt", data=body, headers={"Content-Type": "application/json"}), timeout=15)
            print(" 送信:", n, "seed", seed)
        except Exception as ex:
            print(" [エラー]", n, ex)
        time.sleep(0.2)
    print("送信完了。ComfyUI の処理が終わると出力フォルダに保存されます。")

if __name__ == "__main__":
    main()
