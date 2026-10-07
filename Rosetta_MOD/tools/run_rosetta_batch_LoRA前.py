#!/usr/bin/env python3
"""Rosetta MOD 画像一括生成（ComfyUI API 用 / WAI-Anima など Anima 系モデル向け）

使い方:
  1. ComfyUI を起動しておく（既定 http://127.0.0.1:8188）
  2. python run_rosetta_batch.py
       → モデル本体・テキストエンコーダ・VAE を自動で選びます（決まらない時だけ番号で質問）
     python run_rosetta_batch.py --list-models          # 使えるファイルの一覧
     python run_rosetta_batch.py --unet waiANIMA_v10.safetensors   # モデル本体を直接指定
     python run_rosetta_batch.py Rosetta_pegging Elsa   # 名前の一部で絞り込み
     python run_rosetta_batch.py --random               # 毎回ちがう絵（シードをランダム）
     python run_rosetta_batch.py --seed 1               # シードをずらして別の絵に
     python run_rosetta_batch.py --batch 1              # 同時生成数（VRAM不足の時は 1）
     python run_rosetta_batch.py --no-rembg             # 背景除去を使わない
  結果は ./candidates/<ファイル名>_c1.png ... に保存されます。
  立ち絵用(transparent_background=true)は背景除去済みの透過PNGです。
  気に入ったものの `_cN` を外して Picture/Rosetta/ にコピーしてください。

必要ファイル（ComfyUI/models/ の下）:
  diffusion_models/ waiANIMA_v10.safetensors（WAI-Anima）
  text_encoders/    qwen_3_06b_base.safetensors
  vae/              qwen_image_vae.safetensors
背景除去には ComfyUI-Inspyrenet-Rembg が必要です。
"""
import argparse, copy, glob, json, os, random, sys, time, urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

class Comfy:
    def __init__(self, host):
        self.host = host.rstrip("/")
    def get(self, path):
        return urllib.request.urlopen(self.host + path).read()
    def post(self, path, data):
        req = urllib.request.Request(self.host + path, json.dumps(data).encode(),
                                     {"Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req))
    def options(self, node, field):
        info = json.loads(self.get("/object_info/" + node))
        return info[node]["input"]["required"][field][0]

def pick(label, opts, requested, prefer, where):
    if requested:
        if requested in opts:
            return requested
        print(f"指定の{label}が見つかりません。使えるもの:")
        print("\n".join("  " + o for o in opts))
        sys.exit(1)
    if not opts:
        sys.exit(f"{label}が見つかりません。ComfyUI/models/{where}/ にファイルを置いて、ComfyUI を再起動してください。")
    cands = [o for o in opts if any(k in o.lower() for k in prefer)]
    if len(cands) == 1:
        return cands[0]
    if cands:
        opts = cands
    if len(opts) == 1:
        return opts[0]
    print(f"{label}を番号で選んでください:")
    for i, o in enumerate(opts, 1):
        print(f"  {i}. {o}")
    while True:
        s = input("番号> ").strip()
        if s.isdigit() and 1 <= int(s) <= len(opts):
            return opts[int(s) - 1]

def main():
    ap = argparse.ArgumentParser(description="Rosetta MOD 画像一括生成（Anima系）")
    ap.add_argument("filters", nargs="*", help="ファイル名の一部（省略で全件）")
    ap.add_argument("--host", default=os.environ.get("COMFY_HOST", "http://127.0.0.1:8188"))
    ap.add_argument("--unet", "--model", dest="unet", help="モデル本体（例: waiANIMA_v10.safetensors）")
    ap.add_argument("--clip", help="テキストエンコーダ（例: qwen_3_06b_base.safetensors）")
    ap.add_argument("--vae", help="VAE（例: qwen_image_vae.safetensors）")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--no-rembg", action="store_true", help="背景除去を使わない")
    ap.add_argument("--random", action="store_true", help="シードを毎回ランダムにする")
    ap.add_argument("--seed", type=int, default=0, help="各画像の基準シードにこの値を足す")
    ap.add_argument("--batch", type=int, help="同時に作る枚数（既定は Rosetta_prompts.json の値）")
    a = ap.parse_args()

    api = Comfy(a.host)
    try:
        unets = api.options("UNETLoader", "unet_name")
        clips = api.options("CLIPLoader", "clip_name")
        vaes = api.options("VAELoader", "vae_name")
        if a.list_models:
            for label, o in (("モデル本体 (diffusion_models)", unets), ("テキストエンコーダ (text_encoders)", clips), ("VAE (vae)", vaes)):
                print(f"[{label}]"); print("\n".join("  " + x for x in o) or "  (なし)")
            return
        wf = json.load(open(os.path.join(HERE, "Rosetta_workflow_api.json"), encoding="utf-8"))
        doc = json.load(open(os.path.join(HERE, "Rosetta_prompts.json"), encoding="utf-8"))
        unet = pick("モデル本体", unets, a.unet, ("anima",), "diffusion_models")
        clip = pick("テキストエンコーダ", clips, a.clip, ("qwen_3_06b", "qwen3_06b"), "text_encoders")
        vae = pick("VAE", vaes, a.vae, ("qwen_image_vae",), "vae")
    except urllib.error.URLError:
        sys.exit(f"ComfyUI に接続できません（{a.host}）。起動しているか確認してください。")
    print(f"モデル本体: {unet}\nテキストエンコーダ: {clip}\nVAE: {vae}")

    d = doc["defaults"]
    batch = a.batch or d["batch_size"]
    out_dir = os.path.join(HERE, "candidates")
    os.makedirs(out_dir, exist_ok=True)
    items = [i for i in doc["items"] if not a.filters or any(k in i["file"] for k in a.filters)]
    print(f"{len(items)} 件を生成します（1件あたり {batch} 枚）")

    failed = []
    for n, it in enumerate(items, 1):
        use_rembg = it["transparent_background"] and not a.no_rembg
        g = copy.deepcopy(wf)
        g["12"]["inputs"]["unet_name"] = unet
        g["13"]["inputs"]["clip_name"] = clip
        g["14"]["inputs"]["vae_name"] = vae
        g["6"]["inputs"]["text"] = it["positive"]
        g["7"]["inputs"]["text"] = it["negative"]
        g["5"]["inputs"].update(width=it["width"], height=it["height"], batch_size=batch)
        seed = random.randint(0, 2**32 - 1) if a.random else it["seed"] + a.seed
        g["3"]["inputs"].update(seed=seed, steps=d["steps"], cfg=d["cfg"],
                                sampler_name=d["sampler_name"], scheduler=d["scheduler"])
        stem = os.path.splitext(it["file"])[0]
        g["9"]["inputs"]["filename_prefix"] = "Rosetta/" + stem
        g["11"]["inputs"]["filename_prefix"] = "Rosetta/" + stem + "_rembg"
        if use_rembg:
            save_node = "11"; del g["9"]
        else:
            save_node = "9"; del g["10"]; del g["11"]
        print(f"[{n}/{len(items)}] {it['file']}  ({it['timing']})" + ("  +背景除去" if use_rembg else "") + f"  seed={seed}")
        try:
            pid = api.post("/prompt", {"prompt": g})["prompt_id"]
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            print("   エラー:", body[:500])
            if "InspyrenetRembg" in body:
                print("   → ComfyUI-Manager で「ComfyUI-Inspyrenet-Rembg」を導入するか、--no-rembg を付けてください。")
            if "qwen_image" in body or "er_sde" in body or "UNETLoader" in body:
                print("   → ComfyUI が古く Anima に未対応の可能性があります。update フォルダの update_comfyui.bat で更新して再起動してください。")
            failed.append(it["file"])
            continue
        while True:
            hist = json.loads(api.get("/history/" + pid))
            if pid in hist:
                break
            time.sleep(2)
        st = hist[pid].get("status", {})
        imgs = hist[pid].get("outputs", {}).get(save_node, {}).get("images", [])
        if not imgs:
            err = None
            for m in st.get("messages", []):
                if m[0] == "execution_error":
                    err = m[1]
            if err:
                msg = str(err.get("exception_message", "")).strip()
                print(f"   ⚠ ComfyUI でエラー: [{err.get('node_type')}] {msg[:300]}")
                low = msg.lower()
                if "clip input is invalid" in low:
                    print("     → テキストエンコーダが読めていません。qwen_3_06b_base.safetensors が text_encoders にあるか確認してください。")
                elif "transparent_background" in low or "no module named" in low:
                    print("     → 必要な部品が未導入です。custom_nodes\\\\ComfyUI-Inspyrenet-Rembg で requirements.txt を pip install してください。")
                elif "out of memory" in low:
                    print("     → GPUメモリ不足です。--batch 1 を付けて再実行してください。")
                elif "urlopen" in low or "connection" in low or "download" in low:
                    print("     → 背景除去モデルのダウンロードに失敗しています。ネットワークを確認して再実行してください。")
                elif "errno 22" in low:
                    print("     → ComfyUI を「黒い画面のbatファイル」から普通に起動してください（バックグラウンド起動だと出ることがあります）。")
                if use_rembg and "clip" not in low:
                    print("     → 切り分け：--no-rembg を付けて成功するか確認してください。")
            elif st.get("status_str") == "success":
                print("   ⚠ 画像が返ってきませんでした（エラーなし）。--random（または --seed 1）を付けて再実行してください。")
            else:
                print("   ⚠ 画像が返ってきませんでした。ComfyUI の黒い画面に出ているエラーを確認してください。")
            print("     既存の候補ファイルはそのまま残しています。")
            failed.append(it["file"] + "（生成できず）")
            continue
        for old in glob.glob(os.path.join(out_dir, stem + "_c*.png")):
            os.remove(old)
        for k, im in enumerate(imgs, 1):
            q = urllib.parse.urlencode({"filename": im["filename"], "subfolder": im["subfolder"], "type": im["type"]})
            with open(os.path.join(out_dir, f"{stem}_c{k}.png"), "wb") as f:
                f.write(api.get("/view?" + q))
    ok = len(items) - len(failed)
    print(f"\n結果: {ok} 件成功 / {len(failed)} 件失敗")
    if failed:
        print("失敗:", ", ".join(failed))
        print("→ 原因を直したら、名前を指定して再実行できます（例: python run_rosetta_batch.py " + failed[0].split("（")[0].replace(".png", "") + " --random）")
    if ok:
        print("candidates/ から選んで Picture/Rosetta/ に置いてください。")

if __name__ == "__main__":
    main()
