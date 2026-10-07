# -*- coding: utf-8 -*-
"""月影の夜会MOD 画像バッチ生成（ComfyUI API / 標準ライブラリのみ）
使い方（ComfyUIを起動してから）:
  run_yakai.bat --list                 名前一覧
  run_yakai.bat Yakai_Mio              1枚分（候補を複数枚生成）
  run_yakai.bat Yakai_Mio Yakai_Ciel   複数指定
  run_yakai.bat all                    全部
  オプション: --random / --seed N / --batch N / --no-rembg / --list-models
              --latent sd3|empty / --steps N / --cfg X / --server URL
結果は tools\\candidates\\ に保存。
"""
import argparse, glob, json, os, random, sys, time
import urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UNET = "waiANIMA_v10Base10.safetensors"
CLIP = "qwen_3_06b_base.safetensors"
VAE = "qwen_image_vae.safetensors"


def call(server, path, data=None):
    url = server + path
    req = urllib.request.Request(url)
    if data is not None:
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def pick(server, cls, key, want, keyword):
    """ComfyUIに実在するファイル名から選ぶ（名前が違っても自動で合わせる）"""
    try:
        info = json.loads(call(server, "/object_info/" + cls))
        opts = info[cls]["input"]["required"][key][0]
    except Exception:
        return want
    if want in opts:
        return want
    for o in opts:
        if keyword.lower() in o.lower():
            print(f"  {key}: '{want}' -> '{o}' に自動変更")
            return o
    if opts:
        print(f"  {key}: '{want}' -> '{opts[0]}' に自動変更")
        return opts[0]
    return want


def build(p, seed, batch, rembg, latent, steps, cfg):
    lat = "EmptySD3LatentImage" if latent == "sd3" else "EmptyLatentImage"
    wf = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET, "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP, "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": VAE}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": p["positive"], "clip": ["2", 0]}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"text": p["negative"], "clip": ["2", 0]}},
        "6": {"class_type": lat, "inputs": {"width": p["width"], "height": p["height"], "batch_size": batch}},
        "7": {"class_type": "KSampler", "inputs": {
            "model": ["1", 0], "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["6", 0],
            "seed": seed, "steps": steps, "cfg": cfg, "sampler_name": "er_sde",
            "scheduler": "simple", "denoise": 1.0}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["3", 0]}},
    }
    last = ["8", 0]
    if rembg and p.get("transparent_background"):
        wf["10"] = {"class_type": "InspyrenetRembg", "inputs": {"image": ["8", 0], "torchscript_jit": "default"}}
        last = ["10", 0]
    wf["9"] = {"class_type": "SaveImage", "inputs": {"images": last, "filename_prefix": "yakai/" + p["name"]}}
    return wf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--random", action="store_true")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--no-rembg", action="store_true")
    ap.add_argument("--latent", choices=["sd3", "empty"], default="sd3")
    ap.add_argument("--steps", type=int, default=40)
    ap.add_argument("--cfg", type=float, default=4.5)
    ap.add_argument("--server", default="http://127.0.0.1:8188")
    a = ap.parse_args()

    with open(os.path.join(HERE, "Yakai_prompts.json"), encoding="utf-8") as f:
        prompts = {p["name"]: p for p in json.load(f)}

    if a.list:
        for n, p in prompts.items():
            print(n, "(背景除去)" if p.get("transparent_background") else "")
        return

    try:
        if a.list_models:
            for cls, key in [("UNETLoader", "unet_name"), ("CLIPLoader", "clip_name"), ("VAELoader", "vae_name")]:
                info = json.loads(call(a.server, "/object_info/" + cls))
                print(cls, info[cls]["input"]["required"][key][0])
            return

        global UNET, CLIP, VAE
        UNET = pick(a.server, "UNETLoader", "unet_name", UNET, "anima")
        CLIP = pick(a.server, "CLIPLoader", "clip_name", CLIP, "qwen")
        VAE = pick(a.server, "VAELoader", "vae_name", VAE, "qwen")
        names = list(prompts) if a.names == ["all"] else a.names
        if not names:
            print("名前を指定してください（--list で一覧）")
            return
        outdir = os.path.join(HERE, "candidates")
        os.makedirs(outdir, exist_ok=True)

        for n in names:
            if n not in prompts:
                print("見つかりません:", n)
                continue
            seed = random.randint(0, 2**31) if a.random else (a.seed if a.seed is not None else 12345)
            for old in glob.glob(os.path.join(outdir, n + "_*.png")):
                os.remove(old)
            wf = build(prompts[n], seed, a.batch, not a.no_rembg, a.latent, a.steps, a.cfg)
            print(f"[{n}] seed={seed} 生成中…")
            try:
                res = json.loads(call(a.server, "/prompt", {"prompt": wf}))
            except urllib.error.HTTPError as e:
                print("ComfyUIがエラーを返しました:\n", e.read().decode("utf-8", "replace")[:2000])
                continue
            pid = res["prompt_id"]
            while True:
                time.sleep(2)
                h = json.loads(call(a.server, "/history/" + pid))
                if pid in h:
                    break
            outs = h[pid]["outputs"].get("9", {}).get("images", [])
            if not outs:
                print("  画像が出力されませんでした:", h[pid].get("status"))
                continue
            for i, im in enumerate(outs, 1):
                q = urllib.parse.urlencode({"filename": im["filename"], "subfolder": im["subfolder"], "type": im["type"]})
                data = call(a.server, "/view?" + q)
                path = os.path.join(outdir, f"{n}_{seed}_{i}.png")
                with open(path, "wb") as f:
                    f.write(data)
                print("  保存:", path)
    except urllib.error.URLError as e:
        print("ComfyUIに接続できません。先にComfyUIを起動してください（通常のbatから）。", e)


if __name__ == "__main__":
    main()
