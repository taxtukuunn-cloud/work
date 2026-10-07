# -*- coding: utf-8 -*-
"""
月影の焦らし館 MOD 用 ComfyUI 一括生成スクリプト。
ComfyUI を起動した状態（http://127.0.0.1:8188）で実行する。

使い方（run_ruin.bat 経由）:
  run_ruin.bat --list                 画像名の一覧
  run_ruin.bat Ruin_Lucia             1枚だけ生成
  run_ruin.bat all                    全部生成
  run_ruin.bat Ruin_Lucia --seed 123  シード固定
  run_ruin.bat Ruin_Lucia --random    毎回ランダム（既定は名前から決まる固定シード）
  run_ruin.bat Ruin_Lucia --batch 2    一度に2枚
  run_ruin.bat all --no-rembg          背景除去を使わない
  run_ruin.bat --list-models           ComfyUI が認識しているモデル名を表示
  run_ruin.bat Ruin_Lucia --workflow my_api.json
        ↑ 自分で動作確認済みの「API形式」ワークフローを土台にする（下記参照）

--workflow について:
  ComfyUI で動いているワークフローを「Save (API Format)」で保存し、そのファイルを指定すると、
  プロンプト・サイズ・シードだけを差し替えて実行する。モデルやノード構成は保存したものをそのまま使うので、
  ノード名のエラーが出た場合の逃げ道になる。
"""
import argparse, json, os, re, sys, time, random, zlib, urllib.request, urllib.parse, urllib.error, uuid, glob

HERE = os.path.dirname(os.path.abspath(__file__))
PROMPTS = os.path.join(HERE, "Ruin_prompts.json")
CAND = os.path.join(HERE, "candidates")


def http(url, data=None, timeout=60):
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def jget(url):
    return json.loads(http(url).decode("utf-8"))


def compose(doc, item):
    c = doc["common"]
    kind = item["kind"]
    if kind == "standing":
        pos = c["positive_standing"] + ", " + item["prompt"]
        neg = c["negative_base"]
    elif kind == "background":
        pos = "masterpiece, best quality, score_7, safe, " + item["prompt"]
        neg = "worst quality, low quality, watermark, text, signature"
    else:
        pos = c["positive_scene"] + item["prompt"]
        neg = c["negative_base"] + ", " + c["negative_male"] + ", " + c["negative_scene"]
    if item.get("negative_extra"):
        neg += ", " + item["negative_extra"]
    return pos, neg


def build_graph(doc, pos, neg, seed, batch, prefix, rembg):
    s = doc["settings"]
    g = {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": s["unet"], "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": s["clip"], "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": s["vae"]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["2", 0]}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["2", 0]}},
        "6": {"class_type": "EmptySD3LatentImage", "inputs": {"width": s["width"], "height": s["height"], "batch_size": batch}},
        "7": {"class_type": "KSampler", "inputs": {
            "model": ["1", 0], "seed": seed, "steps": s["steps"], "cfg": s["cfg"],
            "sampler_name": s["sampler"], "scheduler": s["scheduler"],
            "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["6", 0], "denoise": 1.0}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["3", 0]}},
    }
    last = ["8", 0]
    if rembg:
        g["9"] = {"class_type": "InspyrenetRembg", "inputs": {"image": last, "torchscript_jit": "default"}}
        last = ["9", 0]
    g["10"] = {"class_type": "SaveImage", "inputs": {"images": last, "filename_prefix": prefix}}
    return g


def patch_workflow(path, doc, pos, neg, seed, batch, prefix, rembg):
    with open(path, "r", encoding="utf-8") as f:
        g = json.load(f)
    ks = [k for k, v in g.items() if v.get("class_type", "").startswith("KSampler")]
    if not ks:
        sys.exit("指定ワークフローに KSampler が見つかりません（API形式で保存しましたか？）")
    k = ks[0]
    g[k]["inputs"]["seed"] = seed
    pk, nk = g[k]["inputs"]["positive"][0], g[k]["inputs"]["negative"][0]
    g[pk]["inputs"]["text"] = pos
    g[nk]["inputs"]["text"] = neg
    lat = g[k]["inputs"]["latent_image"][0]
    if "width" in g[lat]["inputs"]:
        g[lat]["inputs"]["width"] = doc["settings"]["width"]
        g[lat]["inputs"]["height"] = doc["settings"]["height"]
        g[lat]["inputs"]["batch_size"] = batch
    saves = [i for i, v in g.items() if v.get("class_type") == "SaveImage"]
    if not saves:
        sys.exit("指定ワークフローに SaveImage が見つかりません")
    sv = saves[0]
    g[sv]["inputs"]["filename_prefix"] = prefix
    has_rembg = [i for i, v in g.items() if v.get("class_type") == "InspyrenetRembg"]
    dec = [i for i, v in g.items() if v.get("class_type") == "VAEDecode"]
    if has_rembg and not rembg:
        # 背景除去ノードを飛ばして VAEDecode の出力を保存する
        g[sv]["inputs"]["images"] = [dec[0], 0]
    elif rembg and not has_rembg and dec:
        nid = str(max(int(i) for i in g if i.isdigit()) + 1)
        g[nid] = {"class_type": "InspyrenetRembg", "inputs": {"image": [dec[0], 0], "torchscript_jit": "default"}}
        g[sv]["inputs"]["images"] = [nid, 0]
    elif rembg and has_rembg:
        g[sv]["inputs"]["images"] = [has_rembg[0], 0]
    return g


def run_one(url, doc, item, args):
    pos, neg = compose(doc, item)
    if args.seed is not None:
        seed = args.seed
    elif args.random:
        seed = random.randint(0, 2**31 - 1)
    else:
        seed = zlib.crc32(item["name"].encode("utf-8")) % (2**31)
    rembg = item.get("transparent_background", False) and not args.no_rembg
    prefix = "Ruin/" + item["name"] + "_" + str(seed)
    if args.workflow:
        graph = patch_workflow(args.workflow, doc, pos, neg, seed, args.batch, prefix, rembg)
    else:
        graph = build_graph(doc, pos, neg, seed, args.batch, prefix, rembg)
    payload = json.dumps({"prompt": graph, "client_id": str(uuid.uuid4())}).encode("utf-8")
    try:
        res = json.loads(http(url + "/prompt", payload).decode("utf-8"))
    except urllib.error.URLError as e:
        if not isinstance(e, urllib.error.HTTPError):
            print("  [ERROR] ComfyUI に接続できません:", e)
            return []
        body = e.read().decode("utf-8", "replace")
        if rembg and "InspyrenetRembg" in body:
            print("  [WARN] 背景除去ノード(InspyrenetRembg)が未導入のため、背景除去なしでやり直します。")
            print("         （白背景のまま保存されます。後で背景除去してください）")
            args.no_rembg = True
            return run_one(url, doc, item, args)
        print("  [ERROR] ComfyUI がワークフローを受け付けませんでした:")
        print("  " + body[:2500])
        print("  → 上の内容（特に 'missing_node_type' や 'value not in list'）を確認してください。")
        print("  → 解決しない時は  run_ruin.bat --check  の結果を教えてください。")
        return []
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print("  [ERROR] ComfyUI がワークフローを受け付けませんでした:")
        print("  " + body[:1500])
        print("  → 'missing_node_type' ならノード未導入（--no-rembg を試す）。")
        print("  → それ以外は --workflow で動作確認済みのAPI形式JSONを指定してください。")
        return []
    pid = res["prompt_id"]
    print("  queued:", item["name"], "seed", seed, "rembg" if rembg else "")
    t0 = time.time()
    while True:
        time.sleep(2)
        hist = jget(url + "/history/" + pid)
        if pid in hist:
            h = hist[pid]
            if h.get("status", {}).get("status_str") == "error":
                print("  [ERROR] 生成に失敗しました:", json.dumps(h["status"], ensure_ascii=False)[:800])
                return []
            break
        if time.time() - t0 > 1800:
            print("  [ERROR] タイムアウト")
            return []
    saved = []
    idx = 0
    for node in h["outputs"].values():
        for im in node.get("images", []):
            q = urllib.parse.urlencode({"filename": im["filename"], "subfolder": im.get("subfolder", ""), "type": im["type"]})
            data = http(url + "/view?" + q, timeout=120)
            os.makedirs(CAND, exist_ok=True)
            idx += 1
            dest = os.path.join(CAND, "%s_%d_%02d.png" % (item["name"], seed, idx))
            with open(dest, "wb") as f:
                f.write(data)
            saved.append(dest)
    for d in saved:
        print("  saved:", d)
    return saved


NEEDED = ["UNETLoader", "CLIPLoader", "VAELoader", "CLIPTextEncode", "EmptySD3LatentImage",
          "KSampler", "VAEDecode", "SaveImage", "InspyrenetRembg"]


def resolve_models(url, doc):
    """設定のモデル名がComfyUIに無ければ、近い名前を自動で選ぶ。"""
    st = doc["settings"]
    for cls, key, skey, hint in (("UNETLoader", "unet_name", "unet", "waianima"),
                                 ("CLIPLoader", "clip_name", "clip", "qwen_3"),
                                 ("VAELoader", "vae_name", "vae", "qwen_image_vae")):
        try:
            opts = jget(url + "/object_info/" + cls)[cls]["input"]["required"][key][0]
        except Exception:
            continue
        if st[skey] in opts:
            continue
        pick = [o for o in opts if hint in o.lower()] or (opts if len(opts) == 1 else [])
        if pick:
            print("[info] %s: '%s' が無いので '%s' を使います" % (key, st[skey], pick[0]))
            st[skey] = pick[0]
        else:
            print("[WARN] %s: '%s' が見つかりません。候補: %s" % (key, st[skey], opts))


def find_workflow():
    """同じフォルダ（またはその親）にある API 形式ワークフローを探す。"""
    names = ["Ruin_workflow_api.json", "Rosetta_workflow_api.json"]
    for d in (HERE, os.path.dirname(HERE)):
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


def check(url):
    print("== ComfyUI 接続確認:", url)
    try:
        st = jget(url + "/system_stats")
        print("OK 接続できました。ComfyUI version:", st.get("system", {}).get("comfyui_version", "?"))
    except Exception as e:
        print("NG 接続できません:", e)
        print("  → ComfyUI を通常のbat（run_nvidia_gpu.bat）で起動し、黒い画面に")
        print("    'To see the GUI go to: http://127.0.0.1:8188' と出てから実行してください。")
        print("  → 違うポートで起動している場合は --url http://127.0.0.1:ポート番号")
        return
    print("== 必要なノード")
    for cls in NEEDED:
        try:
            jget(url + "/object_info/" + cls)
            print("  OK  ", cls)
        except Exception:
            print("  無し", cls, "  ← ", "背景除去は --no-rembg で回避可" if cls == "InspyrenetRembg" else "ComfyUI の更新が必要かも（update_comfyui.bat）")
    print("== モデル")
    for cls, key in (("UNETLoader", "unet_name"), ("CLIPLoader", "clip_name"), ("VAELoader", "vae_name")):
        try:
            print(" ", cls, "=", jget(url + "/object_info/" + cls)[cls]["input"]["required"][key][0])
        except Exception as e:
            print(" ", cls, "取得失敗", e)
    print("  ↑ 上のモデル名と Ruin_prompts.json の settings（unet/clip/vae）が一致しているか確認。")
    wf = find_workflow()
    print("== 自動で使えるAPI形式ワークフロー:", wf or "見つからない")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--random", action="store_true")
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--no-rembg", action="store_true")
    ap.add_argument("--workflow")
    ap.add_argument("--url", default="http://127.0.0.1:8188")
    args = ap.parse_args()

    with open(PROMPTS, "r", encoding="utf-8") as f:
        doc = json.load(f)
    items = {i["name"]: i for i in doc["images"]}

    if args.list:
        for n, i in items.items():
            print(("[transparent] " if i["transparent_background"] else "              ") + n)
        return
    if args.check:
        check(args.url)
        return
    if not args.workflow:
        args.workflow = find_workflow()
        if args.workflow:
            print("[info] 既存のワークフローを使います:", args.workflow)
    if args.list_models:
        try:
            for cls, key in (("UNETLoader", "unet_name"), ("CLIPLoader", "clip_name"), ("VAELoader", "vae_name")):
                info = jget(args.url + "/object_info/" + cls)
                print(cls, key, "=", info[cls]["input"]["required"][key][0])
        except Exception as e:
            print("ComfyUI に接続できません。先に ComfyUI を起動してください:", e)
        return
    if not args.names:
        ap.print_help()
        return

    try:
        jget(args.url + "/system_stats")
    except Exception as e:
        sys.exit("ComfyUI に接続できません（" + args.url + "）。先に ComfyUI を通常のbatから起動してください。\n" + str(e))

    if not args.workflow:
        resolve_models(args.url, doc)
    targets = list(items) if args.names == ["all"] else args.names
    for n in targets:
        if n not in items:
            print("[SKIP] 未定義の名前:", n)
            continue
        # 同じ名前の古い候補を掃除（画像が更新されない問題の対策）
        pat = re.compile(re.escape(n) + r"_\d+_\d+\.png")
        for old in glob.glob(os.path.join(CAND, n + "_*.png")):
            if pat.fullmatch(os.path.basename(old)):
                try:
                    os.remove(old)
                except OSError:
                    pass
        print("==", n)
        run_one(args.url, doc, items[n], args)
    print("完了。tools\\candidates の画像を選んで、Picture\\Ruin\\<名前>.png としてコピーしてください。")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        import traceback
        traceback.print_exc()
        print("\n予期しないエラーです。上の表示を教えてください。")
