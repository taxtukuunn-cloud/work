# -*- coding: utf-8 -*-
"""models\\loras の中の LoRA が、今の絵のモデル（SDXL系）に合うかを調べる。
ファイルの先頭の一覧だけを読むので速い。結果は LoRAの種類.csv に書く。"""
import os, sys, json, struct, csv

HOME = os.environ.get("USERPROFILE") or os.path.expanduser("~")
ROOT = os.path.join(HOME, "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras")

def head(path):
    with open(path, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        if n > 200_000_000:
            raise ValueError("先頭が壊れている")
        return json.loads(f.read(n).decode("utf-8"))

def kind(h):
    meta = h.get("__metadata__") or {}
    dims = set()
    te2 = False
    for k, v in h.items():
        if k == "__metadata__" or not isinstance(v, dict):
            continue
        if "te2" in k or "text_encoder_2" in k:
            te2 = True
        sh = v.get("shape") or []
        if "attn2" in k and ("to_k" in k or "to_v" in k) and len(sh) >= 2:
            if ("lora_down" in k or "lora_A" in k or k.endswith(".weight")):
                dims.add(sh[1])
    base = str(meta.get("ss_base_model_version") or meta.get("modelspec.architecture") or "")
    if 2048 in dims:
        return "SDXL系（合う）", base
    if 768 in dims:
        return "SD1.5（合わない）", base
    if 1024 in dims:
        return "SD2（合わない）", base
    b = base.lower()
    if "xl" in b or te2:
        return "SDXL系（合う・表示から判断）", base
    if "v1" in b or "sd_1" in b or "stable-diffusion-v1" in b:
        return "SD1.5（合わない・表示から判断）", base
    return "不明", base

rows = []
for d, _, fs in os.walk(ROOT):
    for fn in sorted(fs):
        if not fn.lower().endswith(".safetensors"):
            continue
        p = os.path.join(d, fn)
        try:
            k, base = kind(head(p))
        except Exception as e:
            k, base = "読めない", str(e)[:60]
        rows.append([os.path.relpath(d, ROOT), fn, k, base])

rows.sort(key=lambda r: (r[2].startswith("SDXL"), r[0], r[1]))
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LoRAの種類.csv")
with open(out, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["フォルダ", "ファイル名", "種類", "学習元の表示"])
    w.writerows(rows)

bad = [r for r in rows if not r[2].startswith("SDXL")]
print("調べた数:", len(rows), "／合わない・不明:", len(bad))
for r in bad:
    print("  [%s] %s\\%s" % (r[2], r[0], r[1]))
print("結果:", out)
