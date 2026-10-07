# -*- coding: utf-8 -*-
"""元絵の下書きから「人物ごとの範囲」を作る（2026-10-02・人物ごとの領域指定）
目的：主人公と相手の説明を画面の別々の範囲に効かせ、髪色の入れ替わり・主人公の幼さ／女性化を防ぐ。
流れ：
  1) 構図下書き元\\<名前>.png の顔を face_yolov8m（FaceDetailer と同じ顔の検出）で見つける
     ※ 2026-10-02 第2版：人の切り分け（yolov8x-seg）は重なった2人を1人にまとめてしまう（470枚中312枚）ため、
       「顔から頭・胸まで」の範囲にした。髪色・顔つき・年齢感が一番効く所。体は全体の文に任せる
  2) 顔ごとに CLIP で「男／女」を判定し、男らしさが一番高い顔を主人公、一番低い顔を相手とする
     （元絵は「女の相手＋男」で撮った構図候補なので、男＝主人公）。2人の範囲が重なる所は近い顔の方に分ける
  3) 構図下書き\\region_<名前>_hero.png ／ _partner.png（832x1216・白＝その人の範囲、ふちをぼかす）を作り、
     ComfyUI\\input\\pose_depthref_<名前>_hero.png ／ _partner.png に置く（gen.py が本番で使う）
  4) 構図下書き\\_人物の範囲.csv と 構図下書き\\_人物の範囲一覧_N.png（青＝主人公・赤＝相手）を作る
     判定違いは CSV の「直す」列に 入れ替え ／ 主人公なし ／ 使わない を書いて再実行すると反映
     （主人公なし＝POV など主人公が写らない構図。使わない＝範囲を作らず、下書きだけで撮る）
初回だけ CLIP（約1.7GB）を自動ダウンロードします（顔の検出は FaceDetailer の face_yolov8m を使う）。
オプション：--force（全部作り直す）／--only 名前,名前（その元絵だけ）／--clip base（CLIP を小さい版に）
"""
import argparse, csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
from PIL import Image, ImageDraw, ImageFilter, ImageFont

PICK_DIR = os.path.join(HERE, "構図下書き元")
OUT_DIR = os.path.join(HERE, "構図下書き")
COMFY_INPUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "input")
SIZE = (832, 1216)
CSV_PATH = os.path.join(OUT_DIR, "_人物の範囲.csv")
CLIPS = {"large": "openai/clip-vit-large-patch14", "base": "openai/clip-vit-base-patch32"}
MALE = ["an anime illustration of a man", "an anime illustration of a naked man with a flat male chest"]
FEMALE = ["an anime illustration of a woman", "an anime illustration of a woman with breasts"]
FIX_OPTS = ("入れ替え", "主人公なし", "使わない")


def fit(img, resample=Image.LANCZOS):
    """depth_from_ref.py と同じ切り抜き（832x1216・比率が違えば中央）"""
    w, h = img.size
    tw, th = SIZE
    s = max(tw / w, th / h)
    img = img.resize((max(tw, round(w * s)), max(th, round(h * s))), resample)
    w, h = img.size
    l, t = (w - tw) // 2, (h - th) // 2
    return img.crop((l, t, l + tw, t + th))


def read_fixes():
    fixes = {}
    if os.path.exists(CSV_PATH):
        rows = list(csv.reader(open(CSV_PATH, encoding="utf-8-sig")))
        if rows and "直す" in rows[0]:
            ci = rows[0].index("直す")
            for r in rows[1:]:
                if len(r) > ci and r[ci].strip():
                    fixes[r[0].strip()] = r[ci].strip()
    return fixes


FACE_MODEL = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI",
                          "models", "ultralytics", "bbox", "face_yolov8m.pt")


def faces(det, img):
    """顔の枠 (x0,y0,x1,y1) を大きい順に。小さすぎる顔（幅が画面の3%未満）は捨てる"""
    r = det(img, conf=0.3, verbose=False)[0]
    out = []
    for b in r.boxes.xyxy.cpu().numpy().tolist():
        x0, y0, x1, y1 = b
        if (x1 - x0) >= img.size[0] * 0.03:
            out.append((x0, y0, x1, y1))
    out.sort(key=lambda b: -(b[2] - b[0]) * (b[3] - b[1]))
    return out[:3]


def maleness(clf, img, b):
    """顔の周り（顔の2.2倍）を切り抜いた『男らしさ』（0〜1）"""
    x0, y0, x1, y1 = b
    w, h = x1 - x0, y1 - y0
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 + h * 0.3
    s = max(w, h) * 2.2 / 2
    crop = img.crop((int(max(0, cx - s)), int(max(0, cy - s)), int(min(img.size[0], cx + s)), int(min(img.size[1], cy + s))))
    res = clf(crop, candidate_labels=MALE + FEMALE)
    sc = {d["label"]: d["score"] for d in res}
    mm = sum(sc[x] for x in MALE)
    return mm / max(mm + sum(sc[x] for x in FEMALE), 1e-6)


def head_masks(size, boxes, chest=True):
    """顔ごとに『頭〜胸』の楕円（chest=False なら頭だけ）。重なる所は近い顔の方へ（numpy bool の配列のリスト）"""
    import numpy as np
    W, H = size
    yy, xx = np.mgrid[0:H, 0:W]
    ells, dists = [], []
    for (x0, y0, x1, y1) in boxes:
        w, h = x1 - x0, y1 - y0
        cx = (x0 + x1) / 2
        if chest:
            top, bot = y0 - h * 0.6, y1 + h * 2.2      # 髪の上〜胸まで
            rx = w * 1.6
        else:   # 主人公の顔が見つからない絵：主人公の頭が近くにあることが多いので、相手の頭だけにする（2026-10-02）
            top, bot = y0 - h * 0.5, y1 + h * 0.4
            rx = w * 0.95
        cy, ry = (top + bot) / 2, (bot - top) / 2
        ells.append(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1)
        dists.append((xx - cx) ** 2 + (yy - (y0 + y1) / 2) ** 2)
    if len(ells) >= 2:
        near = np.argmin(np.stack(dists), axis=0)
        ells = [e & (near == k) for k, e in enumerate(ells)]
    return ells


def to_mask(m, grow=0, blur=14):
    """範囲の画像：ふちをぼかす"""
    import cv2, numpy as np
    im = fit(Image.fromarray(m.astype("uint8") * 255), Image.NEAREST)
    if grow:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (grow * 2 + 1, grow * 2 + 1))
        im = Image.fromarray(cv2.dilate(np.array(im), k))
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    return im.convert("RGB")


def overlay(src, hero, partner, label):
    import numpy as np
    a = np.array(fit(src.convert("RGB"))).astype("float32")
    for mk, col in ((partner, (255, 40, 40)), (hero, (40, 90, 255))):
        if mk is None:
            continue
        w = np.array(mk.convert("L")).astype("float32")[..., None] / 255 * 0.45
        a = a * (1 - w) + np.array(col, "float32") * w
    im = Image.fromarray(a.clip(0, 255).astype("uint8")).resize((277, 405))
    d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("C:\\Windows\\Fonts\\meiryo.ttc", 15)
    except Exception:
        f = ImageFont.load_default()
    d.rectangle((0, 0, 277, 22), fill=(0, 0, 0))
    d.text((4, 2), label, fill=(255, 255, 255), font=f)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    ap.add_argument("--clip", default="large", choices=list(CLIPS))
    a = ap.parse_args()
    os.makedirs(OUT_DIR, exist_ok=True)
    fixes = read_fixes()
    names = sorted(f[:-4] for f in os.listdir(PICK_DIR) if f.lower().endswith(".png"))
    if a.only:
        want = {x.strip() for x in a.only.split(",") if x.strip()}
        names = [n for n in names if n in want]
    # 元絵が消えた範囲は片づける
    alive = set(os.listdir(PICK_DIR))
    for d, pre in ((OUT_DIR, "region_"), (COMFY_INPUT, "pose_depthref_")):
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            for role in ("_hero.png", "_partner.png"):
                if f.startswith(pre) and f.endswith(role):
                    stem = f[len(pre):-len(role)]
                    if stem + ".png" not in alive:
                        os.remove(os.path.join(d, f))
    import torch
    from ultralytics import YOLO
    from transformers import pipeline
    dev = 0 if torch.cuda.is_available() else -1
    print("顔の検出: face_yolov8m ／ 男女の判定: %s（%s）" % (CLIPS[a.clip], "GPU" if dev == 0 else "CPU"))
    det = YOLO(FACE_MODEL)
    clf = pipeline("zero-shot-image-classification", model=CLIPS[a.clip], device=dev)
    old = {}
    if os.path.exists(CSV_PATH):
        for r in list(csv.reader(open(CSV_PATH, encoding="utf-8-sig")))[1:]:
            if r:
                old[r[0]] = r
    rows, tiles = [], []
    for i, n in enumerate(names):
        src_p = os.path.join(PICK_DIR, n + ".png")
        hp, pp = os.path.join(OUT_DIR, "region_%s_hero.png" % n), os.path.join(OUT_DIR, "region_%s_partner.png" % n)
        fx = fixes.get(n, "")
        if fx and fx not in FIX_OPTS:
            print("  [注意] %s の「直す」=%s は分かりません（%s のどれか）" % (n, fx, "／".join(FIX_OPTS))); fx = ""
        src = Image.open(src_p).convert("RGB")
        fb = faces(det, src)
        scores = [maleness(clf, src, b) for b in fb]
        ms = head_masks(src.size, fb)
        hero = partner = None
        status = ""
        if fx == "使わない":
            status = "使わない（直す）"
        elif not fb:
            status = "顔が見つからない"
        else:
            order = sorted(range(len(fb)), key=lambda k: -scores[k])
            if len(fb) == 1:
                if scores[0] < 0.5 or fx == "主人公なし":
                    partner, status = head_masks(src.size, fb, chest=False)[0], "相手だけ（主人公の顔が写らない）"
                else:
                    status = "顔が1つだけ（男）→ 使わない"
            else:
                h, p = order[0], order[-1]
                if fx == "入れ替え":
                    h, p = p, h
                if fx == "主人公なし":
                    partner, status = ms[p], "主人公なし（直す）"
                else:
                    hero, partner = ms[h], ms[p]
                    gap = abs(scores[h] - scores[p])
                    status = ("入れ替え（直す）" if fx == "入れ替え" else
                              ("判定あいまい・要確認" if gap < 0.25 else "OK"))
        hm = to_mask(hero) if hero is not None else None
        pm = to_mask(partner) if partner is not None else None
        for path, mk, role in ((hp, hm, "hero"), (pp, pm, "partner")):
            dst = os.path.join(COMFY_INPUT, "pose_depthref_%s_%s.png" % (n, role))
            if mk is None:
                for x in (path, dst):
                    if os.path.exists(x):
                        os.remove(x)
                continue
            mk.save(path)
            if os.path.isdir(COMFY_INPUT):
                mk.save(dst)
        sc = " / ".join("%.2f" % s for s in scores)
        rows.append([n, str(len(fb)), sc, status, fx])
        tiles.append(overlay(src, hm, pm, "%s  %s" % (n, status[:10])))
        print("  [%d/%d] %s  顔%d  男らしさ %s  → %s" % (i + 1, len(names), n, len(fb), sc or "-", status))
    if a.only:   # 一部だけ作り直したときは、残りの行を前回のまま残す
        done = {r[0] for r in rows}
        rows += [r for k, r in sorted(old.items()) if k not in done]
        rows.sort()
    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as fp:
        w = csv.writer(fp)
        w.writerow(["元絵", "顔の数", "男らしさ", "結果", "直す"])
        w.writerows(rows)
    # 一覧（24枚ずつ）
    for f in os.listdir(OUT_DIR):
        if f.startswith("_人物の範囲一覧_") and f.endswith(".png") and not a.only:
            os.remove(os.path.join(OUT_DIR, f))
    for k in range(0, len(tiles), 24):
        sub = tiles[k:k + 24]
        cols = 6
        sheet = Image.new("RGB", (277 * cols, 405 * ((len(sub) + cols - 1) // cols)), "white")
        for j, t in enumerate(sub):
            sheet.paste(t, ((j % cols) * 277, (j // cols) * 405))
        sheet.save(os.path.join(OUT_DIR, "_人物の範囲一覧_%d.png" % (k // 24 + 1)))
    bad = sum(1 for r in rows if not r[3].startswith(("OK", "相手だけ", "入れ替え（", "主人公なし（")))
    print("\n範囲を作った元絵: %d 枚（要確認・使わない %d 枚）" % (len(rows), bad))
    print("確認: %s\\_人物の範囲一覧_*.png（青＝主人公・赤＝相手）／ %s" % (OUT_DIR, CSV_PATH))


if __name__ == "__main__":
    main()
