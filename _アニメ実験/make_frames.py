# -*- coding: utf-8 -*-
"""アニメ実験キット：1枚の絵から、少しずつ変形させたコマ（連番PNG）を作る。

使い方（bat から呼ぶ）
  python make_frames.py grid [画像]   … 目盛りつきの絵を作る（画像を渡すと start.png として取り込む）
  python make_frames.py make          … anime_config.json のとおりにコマ・確認用GIF・試し用カードを作る

必要なもの：Pillow と numpy（ComfyUI 付属の Python に入っている）
"""
import json
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "anime_config.json")
OUT = os.path.join(HERE, "out")
CODE = "AnimeTest"          # ゲームに入れる時のフォルダ名・ファイル名（半角英数）


def font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        try:
            return ImageFont.load_default(size=size)
        except Exception:
            return ImageFont.load_default()


def load_config():
    with open(CONFIG, encoding="utf-8-sig") as f:
        return json.load(f)


def open_rgb(path):
    im = Image.open(path)
    if im.mode != "RGB":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[3])
        im = bg
    return im


# ---------------------------------------------------------------- 目盛り
def cmd_grid(src=None):
    dst = os.path.join(HERE, "start.png")
    if src:
        open_rgb(src).save(dst)
        print("取り込みました:", dst)
    if not os.path.exists(dst):
        print("start.png がありません。絵を「1_目盛りを見る.bat」にドラッグしてください。")
        return 1
    im = open_rgb(dst)
    w, h = im.size
    d = ImageDraw.Draw(im, "RGBA")
    f = font(max(14, w // 50))
    for x in range(0, w, 50):
        big = x % 100 == 0
        d.line([(x, 0), (x, h)], fill=(255, 255, 0, 150 if big else 60), width=2 if big else 1)
        if big:
            d.rectangle([x + 2, 2, x + 2 + f.size * 2.4, 4 + f.size], fill=(0, 0, 0, 170))
            d.text((x + 4, 2), str(x), fill=(255, 255, 0, 255), font=f)
    for y in range(0, h, 50):
        big = y % 100 == 0
        d.line([(0, y), (w, y)], fill=(0, 255, 255, 150 if big else 60), width=2 if big else 1)
        if big and y:
            d.rectangle([2, y + 2, 2 + f.size * 2.4, y + 4 + f.size], fill=(0, 0, 0, 170))
            d.text((4, y + 2), str(y), fill=(0, 255, 255, 255), font=f)
    out = os.path.join(HERE, "目盛り.png")
    im.save(out)
    print("目盛りつきの絵:", out)
    print("絵の大きさ: 横 %d × 縦 %d" % (w, h))
    print("黄色の数字＝横の位置(cx)、水色の数字＝縦の位置(cy) です。")
    return 0


# ---------------------------------------------------------------- 変形
def field(shape, regions):
    """各画素を最大でどれだけ動かすか（横・縦）の地図を作る。
    範囲（だ円）の中心で 1、ふちで 0 になるなめらかな重みを掛ける。"""
    h, w = shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    fx = np.zeros((h, w), np.float32)
    fy = np.zeros((h, w), np.float32)
    for r in regions:
        rr = np.sqrt(((xx - r["cx"]) / max(1, r["rx"])) ** 2 + ((yy - r["cy"]) / max(1, r["ry"])) ** 2)
        wgt = np.where(rr < 1.0, 0.5 * (1.0 + np.cos(np.pi * np.clip(rr, 0, 1))), 0.0).astype(np.float32)
        fx += wgt * float(r.get("dx", 0))
        fy += wgt * float(r.get("dy", 0))
    return fx, fy


def warp(arr, fx, fy, t):
    """t（0〜1）の分だけ動かした絵を作る。
    できあがりの各画素について「元の絵のどこから色を持ってくるか」を逆算して、
    まわり4画素をなめらかに混ぜる（バイリニア）。"""
    h, w = arr.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    sx = np.clip(xx - fx * t, 0, w - 1)
    sy = np.clip(yy - fy * t, 0, h - 1)
    x0 = np.floor(sx).astype(np.int32)
    y0 = np.floor(sy).astype(np.int32)
    x1 = np.minimum(x0 + 1, w - 1)
    y1 = np.minimum(y0 + 1, h - 1)
    ax = (sx - x0)[..., None]
    ay = (sy - y0)[..., None]
    a = arr.astype(np.float32)
    top = a[y0, x0] * (1 - ax) + a[y0, x1] * ax
    bot = a[y1, x0] * (1 - ax) + a[y1, x1] * ax
    return np.clip(top * (1 - ay) + bot * ay + 0.5, 0, 255).astype(np.uint8)


def mosaic(im, rects):
    """全部のコマに、同じ位置・同じ粗さでモザイクをかける（コマごとにちらつかない）。"""
    for m in rects:
        x, y, w, h = int(m["x"]), int(m["y"]), int(m["w"]), int(m["h"])
        b = max(2, int(m.get("block", 16)))
        box = (x, y, min(im.width, x + w), min(im.height, y + h))
        if box[2] <= box[0] or box[3] <= box[1]:
            continue
        part = im.crop(box)
        small = part.resize((max(1, part.width // b), max(1, part.height // b)), Image.BOX)
        im.paste(small.resize(part.size, Image.NEAREST), box)
    return im


def preview_regions(im, regions, mos):
    im = im.copy()
    d = ImageDraw.Draw(im, "RGBA")
    f = font(max(18, im.width // 35))
    for i, r in enumerate(regions, 1):
        cx, cy, rx, ry = r["cx"], r["cy"], r["rx"], r["ry"]
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=(255, 0, 0, 255), width=3)
        ex, ey = cx + r.get("dx", 0) * 4, cy + r.get("dy", 0) * 4     # 矢印は4倍に伸ばして描く
        d.line([(cx, cy), (ex, ey)], fill=(255, 255, 0, 255), width=5)
        d.ellipse([ex - 8, ey - 8, ex + 8, ey + 8], fill=(255, 255, 0, 255))
        d.rectangle([cx - rx + 4, cy - ry + 4, cx - rx + 4 + f.size * 1.4, cy - ry + 8 + f.size], fill=(0, 0, 0, 180))
        d.text((cx - rx + 8, cy - ry + 4), str(i), fill=(255, 80, 80, 255), font=f)
    for m in mos:
        d.rectangle([m["x"], m["y"], m["x"] + m["w"], m["y"] + m["h"]], outline=(0, 255, 255, 255), width=3)
    return im


# ---------------------------------------------------------------- 試し用カード
def write_card(n, sec):
    name = lambda i: "#%s/anime/%s (%d).png" % (CODE, CODE, i)
    one = list(range(1, n + 1))                        # 1→2→…→n
    pong = one + list(range(n - 1, 1, -1))             # 1→…→n→…→2（往復）
    koma = lambda seq: ",".join("&コマ%d" % i for i in seq)

    def se(seq):                                       # 一番深いコマ（n）の所でだけ音を鳴らす
        cells = ["&&行為SE" if i == n else "" for i in seq] + [""]
        return ",".join(cells)

    L = ["default", "@初期設定",
         "    &カード名,アニメ実験",
         "    &カード画像,%s" % name(1),
         "    レベル設定,1", "    攻撃力設定,0", "    最大HP設定,100",
         "    属性設定,闇属性", "    タイプ設定,悪魔", "    性別設定,女", "    レアリティ設定,UR",
         "    攻撃エフェクト設定,&&セクシーエフェクト",
         "    &背景,&&豪華な寝室背景"]
    L += ["    &コマ%d,%s" % (i, name(i)) for i in one]
    L += ["    &試し一方向,(%s,(%s),(%s))" % (sec, koma(one), se(one)),
          "    &試し往復,(%s,(%s),(%s))" % (sec, koma(pong), se(pong)),
          "    &試し往復4倍,(%s,(%s),(%s))" % (round(sec * 4, 3), koma(pong), se(pong)),
          "    効果設定,0,explain,アニメ再生の実験用カード",
          "",
          "@クエストイベント",
          "話者,自分",
          "背景,&背景",
          "説明,【アニメ実験】これから3種類の動きを順番に再生します。",
          "アニメ,&試し一方向,",
          "説明,①一方向（%d コマ・時間 %s）を再生中。\\n1周の速さと、音の鳴る間隔を見てください。" % (n, sec),
          "説明,①のまま、文章を送っても動き続けていますか？",
          "アニメ削除,",
          "アニメ,&試し往復,",
          "説明,②往復（%d コマ・時間 %s）を再生中。\\n①よりなめらかに見えますか？" % (len(pong), sec),
          "アニメ加速,0.5",
          "説明,②に アニメ加速 0.5 を1回かけました。",
          "アニメ加速,0.5",
          "説明,②に アニメ加速 0.5 をもう1回かけました。\\nさっきよりさらに速くなりましたか？（足し算かどうかの確認）",
          "アニメ加速,-0.5",
          "説明,②に アニメ加速 -0.5 をかけました。少し遅くなりましたか？",
          "アニメ停止,",
          "説明,アニメ停止 をしました。絵は残っていますか？ 止まっていますか？",
          "アニメ削除,",
          "説明,アニメ削除 をしました。絵は消えましたか？",
          "アニメ,&試し往復4倍,",
          "説明,③往復（時間 %s＝②の4倍）を再生中。\\n②の4倍ゆっくりなら、時間の数字が大きいほど遅い、で確定です。" % round(sec * 4, 3),
          "アニメ削除,",
          "説明,実験はここまでです。おつかれさまでした。",
          ""]
    p = os.path.join(OUT, "CSV", "Card")
    os.makedirs(p, exist_ok=True)
    with open(os.path.join(p, "%s_master.txt" % CODE), "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(L))
    q = os.path.join(OUT, "CSV", "EventList", "Quest")
    os.makedirs(q, exist_ok=True)
    with open(os.path.join(q, "%s.txt" % CODE), "w", encoding="utf-8", newline="") as f:
        f.write("【実験】アニメ再生テスト,Card/%s_master,クエストイベント" % CODE)


# ---------------------------------------------------------------- コマを作る
def cmd_make():
    cfg = load_config()
    src = os.path.join(HERE, cfg.get("input", "start.png"))
    if not os.path.exists(src):
        print("元の絵がありません:", src)
        return 1
    n = int(cfg.get("frames", 4))
    if not 2 <= n <= 12:
        print("frames は 2〜12 にしてください。")
        return 1
    regions = cfg.get("regions", [])
    mos = cfg.get("mosaic", [])
    im = open_rgb(src)
    arr = np.asarray(im)
    w, h = im.size
    for i, r in enumerate(regions, 1):
        for k in ("cx", "cy", "rx", "ry"):
            if k not in r:
                print("regions の %d 番目に %s がありません。" % (i, k))
                return 1
        if not (0 <= r["cx"] <= w and 0 <= r["cy"] <= h):
            print("注意：regions の %d 番目の中心が絵の外です（絵は 横%d×縦%d）。" % (i, w, h))
        if math.hypot(r.get("dx", 0), r.get("dy", 0)) > min(r["rx"], r["ry"]) * 0.35:
            print("注意：regions の %d 番目は動かす量が範囲に対して大きく、絵が伸びて見えるかもしれません。" % i)

    fx, fy = field(arr.shape[:2], regions)
    pic = os.path.join(OUT, "Picture", CODE, "anime")
    os.makedirs(pic, exist_ok=True)
    for old in os.listdir(pic):
        if old.startswith(CODE + " (") and old.endswith(".png"):
            os.remove(os.path.join(pic, old))

    frames = []
    for k in range(n):
        t = k / (n - 1)
        if cfg.get("ease", True):                       # 動き始めと終わりをゆっくりにする
            t = 0.5 - 0.5 * math.cos(math.pi * t)
        fr = mosaic(Image.fromarray(warp(arr, fx, fy, t)), mos)
        fr.save(os.path.join(pic, "%s (%d).png" % (CODE, k + 1)))
        frames.append(fr)
        print("コマ %d／%d（動かす割合 %.0f%%）" % (k + 1, n, t * 100))

    preview_regions(im, regions, mos).save(os.path.join(OUT, "確認用_範囲.png"))
    seq = frames + frames[-2:0:-1]
    scale = min(1.0, 480 / w)
    small = [f.resize((int(w * scale), int(h * scale)), Image.LANCZOS) for f in seq]
    small[0].save(os.path.join(OUT, "確認用_往復.gif"), save_all=True, append_images=small[1:],
                  duration=int(cfg.get("gif_ms", 90)), loop=0)
    write_card(n, float(cfg.get("seconds", 0.3)))
    print()
    print("できました:", OUT)
    print("  確認用_範囲.png … 赤いだ円＝動かす範囲、黄色の線＝動かす向き（4倍に伸ばして表示）")
    print("  確認用_往復.gif … ブラウザで開くと動きが見られます")
    print("  Picture・CSV    … 「3_ゲームに入れる.bat」でゲームへコピーされます")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "make"
    sys.exit(cmd_grid(sys.argv[2] if len(sys.argv) > 2 else None) if mode == "grid" else cmd_make())
