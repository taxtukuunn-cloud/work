# -*- coding: utf-8 -*-
"""似た構図を上に出すための下ごしらえ（2026-10-05・まとめツール 段階B の B4）
元絵（構図下書き元\\*.png）と候補（構図下書き元\\_候補\\ の絵）を CLIP（openai/clip-vit-large-patch14・人物の範囲づくりと同じもの）で
数字の並び（特徴）にして、構図下書き\\_似た構図_特徴.npz に置く。まとめツールの「採用」で、選んだ候補に形の近い構図を上に出すのに使う。
・前に作った特徴は使い回す（絵が変わったものと新しいものだけ作る）。グラフィックボードを使う（無ければ CPU・遅い）
・測った結果（2026-10-05・取り込み済み 727 枚で1枚ずつ抜いて試した）：上位3つに同じ構図 67%・同じ技の構図 79%。目安として使う
使い方: python 似た構図の下ごしらえ.py"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PICK = os.path.join(HERE, "構図下書き元")
CAND = os.path.join(PICK, "_候補")
OUT = os.path.join(HERE, "構図下書き", "_似た構図_特徴.npz")
EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp")


def main():
    import numpy as np
    targets = []   # (種類, 名前, 場所)
    for f in sorted(os.listdir(PICK)):
        if f.lower().endswith(".png") and os.path.isfile(os.path.join(PICK, f)):
            targets.append(("src", f[:-4], os.path.join(PICK, f)))
    for d, where in ((CAND, "候補"), (os.path.join(CAND, "_見送り"), "見送り")):
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.lower().endswith(EXT) and os.path.isfile(os.path.join(d, f)):
                    targets.append(("cand", f, os.path.join(d, f)))
    old = {}
    if os.path.exists(OUT):
        z = np.load(OUT, allow_pickle=False)
        keys = json.loads(str(z["keys"]))
        for k, e, ef in zip(keys, z["emb"], z["emb_flip"]):
            old[(k[0], k[1])] = (k[2], e, ef)
    todo = [t for t in targets if (t[0], t[1]) not in old or old[(t[0], t[1])][0] != int(os.path.getmtime(t[2]))]
    print("絵 %d 枚（新しく特徴を作る %d 枚）" % (len(targets), len(todo)))
    new = {}
    if todo:
        import torch
        from PIL import Image
        from transformers import CLIPModel, CLIPProcessor
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        m = CLIPModel.from_pretrained("openai/clip-vit-large-patch14").to(dev).eval()
        p = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

        def emb(ims):
            with torch.no_grad():
                e = m.get_image_features(**p(images=ims, return_tensors="pt").to(dev))
            if not torch.is_tensor(e):   # transformers の版によっては包まれて返る
                e = getattr(e, "image_embeds", None) if getattr(e, "image_embeds", None) is not None else e.pooler_output
            return torch.nn.functional.normalize(e, dim=-1).cpu().numpy().astype("float32")
        for k in range(0, len(todo), 32):
            part = todo[k:k + 32]
            ims = []
            for t in part:
                try:
                    ims.append(Image.open(t[2]).convert("RGB"))
                except Exception:
                    ims.append(Image.new("RGB", (64, 64)))
            e = emb(ims)
            ef = emb([im.transpose(Image.FLIP_LEFT_RIGHT) for im in ims])
            for t, a, b in zip(part, e, ef):
                new[(t[0], t[1])] = (int(os.path.getmtime(t[2])), a, b)
            print("  %d / %d" % (min(k + 32, len(todo)), len(todo)))
    keys, E, EF = [], [], []
    for t in targets:
        v = new.get((t[0], t[1])) or old[(t[0], t[1])]
        keys.append([t[0], t[1], v[0]])
        E.append(v[1])
        EF.append(v[2])
    np.savez_compressed(OUT + ".tmp.npz", keys=json.dumps(keys, ensure_ascii=False), emb=np.stack(E), emb_flip=np.stack(EF))
    os.replace(OUT + ".tmp.npz", OUT)
    print("→ %s（元絵 %d・候補 %d）" % (OUT, sum(1 for t in targets if t[0] == "src"), sum(1 for t in targets if t[0] == "cand")))


if __name__ == "__main__":
    main()
