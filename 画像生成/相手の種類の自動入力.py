# -*- coding: utf-8 -*-
"""相手の種類の自動入力の下ごしらえ（2026-10-05・まとめツール 段階B の B5）
元絵（構図下書き元\\*.png）に WD14 Tagger（SmilingWolf/wd-vit-tagger-v3・timm で読む）をかけ、タグを 構図下書き\\_WD14タグ.json に置く。
まとめツールの「下書きの項目」で、翼・尻尾・角などの付属物と胸の大きさの「案」として出す（決めるのは人。白黒の下書きには使わない）。
・前にかけた絵は使い回す（新しい絵と変わった絵だけかける）。グラフィックボードを使う（無ければ CPU・遅い）
・モデル（約 380MB）は初回に Hugging Face から取ってくる（2026-10-05 ユーザー了承）
・測った結果（2026-10-05・元絵 832 枚）：胸の分け方は Claude の案と 70% 一致。付属物は Claude の目の印より多く見つける（翼・尻尾・角）。
  WD14 には付属物と胸の案だけを任せる。どちらが主人公か・敵上位か・大人の体つきかは任せない
使い方: python 相手の種類の自動入力.py"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "構図下書き元")
OUT = os.path.join(HERE, "構図下書き", "_WD14タグ.json")
REPO = "SmilingWolf/wd-vit-tagger-v3"
KEEP = 0.2   # この確からしさ以上のタグを残す


def main():
    old = {}
    if os.path.exists(OUT):
        old = json.load(open(OUT, encoding="utf-8"))
    names = sorted(f[:-4] for f in os.listdir(SRC) if f.lower().endswith(".png"))
    todo = [n for n in names if (old.get(n) or {}).get("mt") != int(os.path.getmtime(os.path.join(SRC, n + ".png")))]
    print("元絵 %d 枚（新しくかける %d 枚）" % (len(names), len(todo)))
    if todo:
        import numpy as np, timm, torch
        from PIL import Image
        from huggingface_hub import hf_hub_download
        tags = [r["name"] for r in csv.DictReader(open(hf_hub_download(REPO, "selected_tags.csv"), encoding="utf-8"))]
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        m = timm.create_model("hf-hub:" + REPO, pretrained=True).eval().to(dev)

        def prep(p):
            im = Image.open(p).convert("RGBA")
            bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
            bg.alpha_composite(im)
            im = bg.convert("RGB")
            s = max(im.size)
            sq = Image.new("RGB", (s, s), (255, 255, 255))
            sq.paste(im, ((s - im.width) // 2, (s - im.height) // 2))
            a = (np.asarray(sq.resize((448, 448), Image.BICUBIC), "float32") / 255.0 - 0.5) / 0.5
            return torch.from_numpy(a[:, :, ::-1].copy()).permute(2, 0, 1)   # RGB → BGR（このモデルの決まり）
        for k in range(0, len(todo), 16):
            part = todo[k:k + 16]
            x = torch.stack([prep(os.path.join(SRC, n + ".png")) for n in part]).to(dev)
            with torch.no_grad():
                pr = torch.sigmoid(m(x)).cpu().numpy()
            for n, p in zip(part, pr):
                old[n] = dict(mt=int(os.path.getmtime(os.path.join(SRC, n + ".png"))),
                              tags={tags[i]: round(float(p[i]), 3) for i in np.where(p > KEEP)[0]})
            print("  %d / %d" % (min(k + 16, len(todo)), len(todo)))
    old = {n: v for n, v in old.items() if n in set(names)}
    with open(OUT + ".tmp", "w", encoding="utf-8") as f:
        json.dump(old, f, ensure_ascii=False)
    os.replace(OUT + ".tmp", OUT)
    print("→ %s" % OUT)


if __name__ == "__main__":
    main()
