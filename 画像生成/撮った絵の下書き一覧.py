# -*- coding: utf-8 -*-
"""ComfyUI\\output の撮った絵（png）に埋め込まれた設定から、どの下書き（depthref_…）・どのLoRAで撮ったかを一覧にする（2026-10-02）
使い方: python 撮った絵の下書き一覧.py [フォルダ]（省略時は output\\キャラLoRA確認）→ 画像生成\\撮った絵の下書き一覧.csv（Excel で開ける）"""
import csv, json, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
def _latest():   # キャラLoRA確認3 → 2 → 無印 の順で、ある中でいちばん新しいフォルダ
    c = [d for d in os.listdir(OUT) if d.startswith("キャラLoRA確認") and os.path.isdir(os.path.join(OUT, d))]
    c.sort(key=lambda d: int(d.replace("キャラLoRA確認", "") or 1))
    return os.path.join(OUT, c[-1] if c else "キャラLoRA確認")
root = sys.argv[1] if len(sys.argv) > 1 else _latest()
print("調べるフォルダ:", root)
rows = []
for d, _, fs in os.walk(root):
    for f in sorted(fs):
        if not f.lower().endswith(".png"):
            continue
        p = os.path.join(d, f)
        try:
            pr = json.loads(Image.open(p).info.get("prompt") or "{}")
        except Exception:
            pr = {}
        refs = [str(n["inputs"].get("image", "")) for n in pr.values() if n.get("class_type") == "LoadImage"
                and not str(n["inputs"].get("image", "")).endswith(("_hero.png", "_partner.png"))]
        loras = [str(n["inputs"].get("lora_name", "")) for n in pr.values() if n.get("class_type") in ("LoraLoader", "CreateHookLora")]
        hook = any(n.get("class_type") == "CreateHookLora" for n in pr.values())
        ref = ", ".join(r.replace("pose_", "").replace(".png", "") for r in refs) or "（下書きなし）"
        rows.append([os.path.relpath(p, root), ref, "", "あり" if hook else "", " / ".join(loras)])
CSV = os.path.join(HERE, "撮った絵の下書き一覧.csv")
old = {}
if os.path.isfile(CSV):   # 前に付けた○は残す
    try:
        for r in list(csv.reader(open(CSV, encoding="utf-8-sig")))[1:]:
            if len(r) > 2 and r[2].strip():
                old[r[0]] = r[2]
    except Exception:
        pass
for r in rows:
    r[2] = old.get(r[0], "")
with open(CSV, "w", encoding="utf-8-sig", newline="") as fo:
    w = csv.writer(fo)
    w.writerow(["画像", "下書き", "外す（ダメな絵に○）", "キャラLoRAを相手の範囲だけ", "LoRA"])
    w.writerows(rows)
print("%d枚 → 撮った絵の下書き一覧.csv" % len(rows))
