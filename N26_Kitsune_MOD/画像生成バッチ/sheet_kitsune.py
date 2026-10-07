# -*- coding: utf-8 -*-
"""output/Kitsune の画像を一覧（コンタクトシート）にまとめる → output/Kitsune_sheet.jpg
usage: python sheet_kitsune.py [接頭辞]   例: python sheet_kitsune.py Kitsune_lose
"""
import os, sys, glob, math
from PIL import Image, ImageDraw

here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, "output", "Kitsune")
prefix = sys.argv[1] if len(sys.argv) > 1 else "Kitsune"
files = sorted(f for f in glob.glob(os.path.join(src, "*.png")) if os.path.basename(f).startswith(prefix))
if not files:
    sys.exit("no images in " + src)
W, H, COLS = 256, 374, 6
rows = math.ceil(len(files) / COLS)
sheet = Image.new("RGB", (COLS * W, rows * (H + 22)), "white")
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB")
    im.thumbnail((W, H))
    x, y = (i % COLS) * W, (i // COLS) * (H + 22)
    sheet.paste(im, (x + (W - im.width) // 2, y))
    d.text((x + 4, y + H + 4), os.path.basename(f)[:-4].replace("Kitsune_", ""), fill="black")
out = os.path.join(here, "output", "Kitsune_sheet%s.jpg" % ("" if prefix == "Kitsune" else "_" + prefix.replace("Kitsune_", "")))
sheet.save(out, quality=85)
print(len(files), "images ->", out)
