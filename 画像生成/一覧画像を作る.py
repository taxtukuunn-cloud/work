# -*- coding: utf-8 -*-
"""撮った絵を小さく並べた一覧画像（1枚に15枚）を作る（2026-10-02）。絵そのものは変更しない。
使い方: python 一覧画像を作る.py [フォルダ]（省略時は output のいちばん新しい キャラLoRA確認N）
→ <フォルダ>\\_一覧\\立ち絵_01.jpg … と 場面_01.jpg …（絵の上に 画像名 と 使った下書き を表示）"""
import json, os, sys
from PIL import Image, ImageDraw
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")


def _latest():
    c = [d for d in os.listdir(OUT) if d.startswith("キャラLoRA確認") and os.path.isdir(os.path.join(OUT, d))]
    c.sort(key=lambda d: int(d.replace("キャラLoRA確認", "") or 1))
    return os.path.join(OUT, c[-1] if c else "キャラLoRA確認")


root = sys.argv[1] if len(sys.argv) > 1 else _latest()
dst = os.path.join(root, "_一覧")
os.makedirs(dst, exist_ok=True)
files = []
for d, _, fs in os.walk(root):
    if os.path.basename(d) == "_一覧":
        continue
    for f in sorted(fs):
        if f.lower().endswith(".png"):
            files.append(os.path.join(d, f))
files.sort()
groups = {"立ち絵": [f for f in files if "_lose_" not in os.path.basename(f) and "_atk_" not in os.path.basename(f)],
          "場面": [f for f in files if "_lose_" in os.path.basename(f) or "_atk_" in os.path.basename(f)]}
COLS, PER, TW, TH = 5, 15, 250, 365
n = 0
for g, fs in groups.items():
    for s in range(0, len(fs), PER):
        part = fs[s:s + PER]
        W = Image.new("RGB", (COLS * TW, ((len(part) + COLS - 1) // COLS) * (TH + 26)), "white")
        dr = ImageDraw.Draw(W)
        for k, f in enumerate(part):
            try:
                im = Image.open(f)
                pr = json.loads(im.info.get("prompt") or "{}")
            except Exception:
                continue
            ref = [str(x["inputs"].get("image", "")) for x in pr.values() if x.get("class_type") == "LoadImage"
                   and not str(x["inputs"].get("image", "")).endswith(("_hero.png", "_partner.png"))]
            hook = any(x.get("class_type") == "CreateHookLora" for x in pr.values())
            r = ref[0].replace("pose_depthref_", "").replace("pose_", "").replace(".png", "") if ref else "-"
            im = im.convert("RGBA")
            bg = Image.new("RGBA", im.size, (200, 200, 200, 255)); bg.alpha_composite(im)
            im = bg.convert("RGB"); im.thumbnail((TW - 4, TH))
            x, y = (k % COLS) * TW, (k // COLS) * (TH + 26)
            W.paste(im, (x + 2, y + 24))
            dr.text((x + 3, y + 1), os.path.basename(f).replace("_00001_.png", ""), fill="red")
            dr.text((x + 3, y + 12), r + (" HOOK" if hook else ""), fill="blue")
        W.save(os.path.join(dst, "%s_%02d.jpg" % (g, s // PER + 1)), quality=82)
        n += 1
print("%d枚の絵 → 一覧画像 %d枚: %s" % (len(files), n, dst))
