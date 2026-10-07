# -*- coding: utf-8 -*-
"""
全MOD共通のComfyUI一括生成スクリプト。
tools/prompts/<pre>_prompts.json を読み、ComfyUI APIに順番に投げる。

使い方（ComfyUIポータブル同梱Pythonで実行。run_mod.bat 経由を推奨）：
  python run_mod_batch.py <MODコード> [キャラキー|all] [オプション]

  <MODコード> は tools/prompts/ のファイル名の接頭辞（例: Rosetta, Arachne, Host, Inmon など）
  第2引数省略時は all（そのMODの全画像を生成）

オプション：
  --random          シード固定を無視して毎回ランダムシード
  --seed N           シードを指定
  --batch N          1回のAPI呼び出しで生成する枚数（既定1）
  --no-rembg         背景除去をスキップ（InspyrenetRembgノード未導入の場合）
  --list-models      利用可能なモデル一覧をComfyUIから取得して表示するだけ
  --list-mods        tools/prompts/ にあるMODコード一覧を表示するだけ
  --list-keys        指定MODの画像キー一覧を表示するだけ（生成はしない）
  --server URL        ComfyUIのURL（既定 http://127.0.0.1:8188）

出力：tools/candidates/<MODコード>/ 以下に保存（ComfyUI本体のoutputにも通常どおり保存される）。
"""
# --- 絵柄LoRA（2026-09-26追加：Downloads\Lora用\lora_hook.py を読み込む。外すときはこの5行を消す） ---
try:
    import os as _lo, sys as _ls; _ls.path.insert(0, _lo.path.join(_lo.path.expanduser("~"), "Downloads", "Lora用")); import lora_hook  # noqa
except Exception as _le:
    print("(LoRA設定を読み込めませんでした:", _le, ")")
import argparse
import copy
import hashlib
import json
import os
import random
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_PATH = os.path.join(HERE, "workflow_api.json")
PROMPTS_DIR = os.path.join(HERE, "prompts")
CANDIDATES_DIR = os.path.join(HERE, "candidates")


def load_workflow():
    with open(WORKFLOW_PATH, encoding="utf-8") as f:
        return json.load(f)


def list_mods():
    return sorted(
        fn[: -len("_prompts.json")]
        for fn in os.listdir(PROMPTS_DIR)
        if fn.endswith("_prompts.json")
    )


def load_prompts(mod_code):
    path = os.path.join(PROMPTS_DIR, f"{mod_code}_prompts.json")
    if not os.path.exists(path):
        print(f"[エラー] {path} が見つかりません。")
        print("利用可能なMODコード:", ", ".join(list_mods()))
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def submit(server, workflow_template, entry_data, seed, batch, use_rembg):
    wf = copy.deepcopy(workflow_template)
    wf.pop("_comment", None)
    wf["6"]["inputs"]["text"] = entry_data["positive"]
    wf["7"]["inputs"]["text"] = entry_data["negative"]
    wf["8"]["inputs"]["width"] = entry_data.get("width", 832)
    wf["8"]["inputs"]["height"] = entry_data.get("height", 1216)
    wf["8"]["inputs"]["batch_size"] = batch
    wf["9"]["inputs"]["seed"] = seed
    wf["11"]["inputs"]["filename_prefix"] = entry_data["file"].rsplit(".", 1)[0]

    transparent = entry_data.get("transparent_background", False)
    if transparent and use_rembg:
        wf["12"]["inputs"]["image"] = ["10", 0]
        wf["11"]["inputs"]["images"] = ["12", 0]
        wf["11"]["inputs"]["filename_prefix"] += "_rmbg"
    else:
        wf.pop("12", None)

    payload = json.dumps({"prompt": wf}).encode("utf-8")
    req = urllib.request.Request(
        f"{server}/prompt", data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  [送信エラー] {entry_data['file']}: HTTP {e.code} {e.reason}")
        print(f"  [ComfyUIからの詳細] {body[:2000]}")
        return None
    except Exception as e:
        print(f"  [送信エラー] {entry_data['file']}: {e}")
        return None


def check_models(server):
    targets = [
        ("UNETLoader", "unet_name", "UNET (workflow_api.jsonのnode 3)"),
        ("CLIPLoader", "clip_name", "CLIP (workflow_api.jsonのnode 4)"),
        ("VAELoader", "vae_name", "VAE (workflow_api.jsonのnode 5)"),
    ]
    ok = True
    for class_type, field, label in targets:
        try:
            with urllib.request.urlopen(f"{server}/object_info/{class_type}", timeout=10) as resp:
                info = json.loads(resp.read())
            models = info[class_type]["input"]["required"][field][0]
            print(f"{label} の候補:")
            for m in models:
                print("  -", m)
        except Exception as e:
            ok = False
            print(f"[エラー] {class_type} の情報取得に失敗しました。ComfyUIが起動しているか確認してください。")
            print(" ", e)
    if ok:
        print()
        print("上のリストと workflow_api.json の unet_name / clip_name / vae_name が一致しているか確認してください。")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mod", nargs="?", help="MODコード（例: Rosetta, Inmon, Host ...）")
    ap.add_argument("key", nargs="?", default="all", help="画像キー、または all")
    ap.add_argument("--random", action="store_true")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--no-rembg", action="store_true")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--list-mods", action="store_true")
    ap.add_argument("--list-keys", action="store_true")
    ap.add_argument("--server", default="http://127.0.0.1:8188")
    args = ap.parse_args()

    if args.list_models:
        check_models(args.server)
        return

    if args.list_mods or not args.mod:
        print("利用可能なMODコード:")
        for m in list_mods():
            print(" -", m)
        if not args.mod:
            return

    prompts = load_prompts(args.mod)

    if args.list_keys:
        print(f"{args.mod} の画像キー（{len(prompts)}件）:")
        for k in prompts:
            print(" -", k)
        return

    workflow = load_workflow()
    out_dir = os.path.join(CANDIDATES_DIR, args.mod)
    os.makedirs(out_dir, exist_ok=True)

    if args.key != "all" and args.key not in prompts:
        print(f"[エラー] キー '{args.key}' が見つかりません。--list-keys で確認してください。")
        sys.exit(1)

    targets = list(prompts.items()) if args.key == "all" else [(args.key, prompts[args.key])]
    print(f"=== {args.mod}：{len(targets)}件を生成します ===")

    for key, data in targets:
        if args.seed is not None:
            seed = args.seed
        elif args.random:
            seed = random.randint(0, 2**31 - 1)
        else:
            # キャラ単位で固定シード：同じキャラ（マスター／下級/上級/受け側）の
            # 立ち絵・技CG・敗北CGなどが同じシードになり、見た目が揃いやすくなる。
            char_key = data.get("char_key") or data["file"]
            seed = int(hashlib.md5(f"{args.mod}-{char_key}".encode("utf-8")).hexdigest(), 16) % (2**31 - 1)

        print(f"[{key}] {data['file']}  seed={seed}  safety={data['safety']}")
        res = submit(args.server, workflow, data, seed, args.batch, not args.no_rembg)
        if res:
            with open(os.path.join(out_dir, f"{key}_last_submit.json"), "w", encoding="utf-8") as f:
                json.dump({"seed": seed, "response": res}, f, ensure_ascii=False, indent=2)
        time.sleep(0.3)

    print("=== 送信完了。ComfyUIのキュー状況・出力フォルダを確認してください ===")


if __name__ == "__main__":
    main()
