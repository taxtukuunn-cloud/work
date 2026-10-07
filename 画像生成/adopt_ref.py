# -*- coding: utf-8 -*-
"""元絵候補（構図下書き元\\_候補\\）から採用した画像を 構図下書き元 に入れ、奥行き下書きと人物の範囲まで作る（2026-10-03）
使い方：
  1) 候補を整理する.bat で番号を付けたあと、_候補\\_採用.csv の「採用」欄に構図名（英小文字・数字・_）を書く
     （見送り＝_見送り へ移す。空欄＝まだ決めていない。どちらもここでは何もしない）
  2) 元絵を採用する.bat（このファイル）を実行
流れ：
  ・ウィンドウの撮影ならタイトルバーと外の縁を、どの画像でも周りの真っ黒な余白と一色の縁を自動で切り落とす（--no-crop で切らない）
  ・構図下書き元\\<構図名>.png（2枚目からは <構図名>_2.png …）に入れる。_候補 の画像はそのまま残る
    同じ中身がその構図にもう入っていれば入れない。入れた名前は _採用.csv の「取り込んだ名前」に書く（次からは飛ばす）
  ・構図名が model.json（pose_control.ref_sets）に無くても止めずに入れる。model.json には登録しない（最後に未登録の名前を表示）
  ・depth_from_ref.py（奥行き下書き）→ make_region_masks.py（人物の範囲）を今回入れた分について実行
  ・構図下書き\\_取り込み確認_<日時>.jpg に、今回入れた分の「奥行き下書き｜人物の範囲（青＝主人公・赤＝相手）」を1枚にまとめる
ComfyUI 付属の Python で動かす（奥行き・範囲づくりに torch などが要る）。--dry-run で、することだけ表示（何も書かない）"""
import argparse, csv, hashlib, io, json, os, re, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import import_pose_ref as ipr
from PIL import Image, ImageDraw, ImageFont

PICK_DIR = ipr.PICK_DIR
CAND = os.path.join(PICK_DIR, "_候補")
PICK_CSV = os.path.join(CAND, "_採用.csv")
OUT_DIR = os.path.join(HERE, "構図下書き")
NAME_RE = re.compile(r"^[a-z0-9_]+$")
SKIP_WORDS = ("", "見送り")


def auto_crop(img):
    """(左, 上, 右, 下) と 切ったもの の説明。ウィンドウの撮影ならタイトルバーと外の縁、どの絵でも真っ黒の余白と一色の縁を切る。
    2026-10-03 _候補 の50枚で確認：ウィンドウの撮影（タイトルバー 39〜45px）・黒帯（左右・上下）を切り、暗い絵の中身は切らない"""
    import numpy as np
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    H, W = a.shape[:2]
    gray = a.mean(2)
    t, b, l, r = 0, H, 0, W
    what = []
    # ウィンドウの撮影か：上から2〜10行目がほぼ一色（タイトルバーの色）で、20〜120px 下で絵に変わる
    if H > 200 and W > 200:
        bar = np.median(a[4:10].reshape(-1, 3), axis=0)
        fr = (np.abs(a[:min(H, 160)] - bar).max(2) < 10).mean(1)
        if fr[2:10].min() > 0.9:
            end = next((y for y in range(2, len(fr)) if fr[y] < 0.6), None)
            if end and 20 <= end <= 120:
                edge = next((y for y in range(0, 4) if fr[y] > 0.9), 2)   # 一番外の縁（角の丸みで後ろが写る）
                t, l, r, b = end, edge, W - edge, H - edge
                what.append("タイトルバー%dpx" % end)

    def black(v):   # 黒帯：ほぼ真っ黒で一様（暗い絵は切らない）
        return (v < 16).mean() > 0.98 and v.std() < 8

    def line(v):    # 窓の縁：一色の線（端から3px まで）
        return v.std() < 4

    t0, b0, l0, r0 = t, b, l, r
    for _ in range(3):
        while b - t > H * 0.4 and (black(gray[b - 1, l:r]) or (b > b0 - 3 and line(gray[b - 1, l:r]))):
            b -= 1
        while b - t > H * 0.4 and (black(gray[t, l:r]) or (t < t0 + 3 and line(gray[t, l:r]))):
            t += 1
        while r - l > W * 0.4 and (black(gray[t:b, r - 1]) or (r > r0 - 3 and line(gray[t:b, r - 1]))):
            r -= 1
        while r - l > W * 0.4 and (black(gray[t:b, l]) or (l < l0 + 3 and line(gray[t:b, l]))):
            l += 1
    if (t, b, l, r) != (t0, b0, l0, r0):
        what.append("余白・縁 上%d 下%d 左%d 右%d" % (t - t0, b0 - b, l - l0, r0 - r))
    return (l, t, r, b), what


def registered():
    """model.json の pose_control.ref_sets に出てくる構図名"""
    try:
        pc = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8")).get("pose_control") or {}
    except Exception:
        return set()
    out = set()
    for rows in (pc.get("ref_sets") or {}).values():
        for r in rows or []:
            out.update(r.get("comps") or [])
    return out


def read_rows():
    with open(PICK_CSV, encoding="utf-8-sig", newline="") as fp:
        rows = list(csv.reader(fp))
    head = rows[0]
    for col in ("取り込んだ名前", "切り抜き"):
        if col not in head:
            head.append(col)
    for r in rows[1:]:
        r += [""] * (len(head) - len(r))
    return rows


def check_sheet(names, unreg):
    """今回入れた分の「奥行き下書き｜人物の範囲」を1枚に（2段の高さ 380px・2列）"""
    import numpy as np
    status = {}
    p = os.path.join(OUT_DIR, "_人物の範囲.csv")
    if os.path.exists(p):
        status = {r[0]: r[3] for r in list(csv.reader(open(p, encoding="utf-8-sig")))[1:] if len(r) > 3}
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", 22)
    except Exception:
        font = ImageFont.load_default()
    RH, rows = 380, []
    for n in names:
        dp = os.path.join(OUT_DIR, "depthref_%s.png" % n)
        if not os.path.exists(dp):
            continue
        dep = Image.open(dp).convert("RGB")
        W, H = dep.size
        src = Image.open(os.path.join(PICK_DIR, n + ".png")).convert("RGB")
        s = max(W / src.width, H / src.height)   # depth_from_ref.py と同じ切り抜き
        src = src.resize((max(W, round(src.width * s)), max(H, round(src.height * s))), Image.LANCZOS)
        l, t = (src.width - W) // 2, (src.height - H) // 2
        a = np.array(src.crop((l, t, l + W, t + H))).astype("float32")
        for role, col in (("partner", (255, 40, 40)), ("hero", (40, 90, 255))):
            mp = os.path.join(OUT_DIR, "region_%s_%s.png" % (n, role))
            if os.path.exists(mp):
                m = Image.open(mp).convert("L").resize((W, H))
                w = np.array(m).astype("float32")[..., None] / 255 * 0.45
                a = a * (1 - w) + np.array(col, "float32") * w
        ov = Image.fromarray(a.clip(0, 255).astype("uint8"))
        k = RH / H
        tiles = [im.resize((round(W * k), RH)) for im in (dep, ov)]
        row = Image.new("RGB", (sum(t.width for t in tiles) + 10, RH + 34), "white")
        x = 0
        for tl in tiles:
            row.paste(tl, (x, 34)); x += tl.width + 10
        comp = re.sub(r"_\d+$", "", n)
        label = "%s %dx%d %s%s" % (n, W, H, (status.get(n) or "範囲なし")[:12], "  ※未登録" if comp in unreg else "")
        ImageDraw.Draw(row).text((4, 4), label, fill="red" if comp in unreg else "black", font=font)
        rows.append(row)
    if not rows:
        return None
    cols = 2 if len(rows) > 1 else 1
    cw = max(r.width for r in rows) + 20
    nrow = (len(rows) + cols - 1) // cols
    sheet = Image.new("RGB", (cw * cols, (RH + 54) * nrow + 40), "white")
    for i, r in enumerate(rows):
        sheet.paste(r, ((i % cols) * cw + 10, (i // cols) * (RH + 54) + 10))
    ImageDraw.Draw(sheet).text((10, (RH + 54) * nrow + 6), "左＝奥行き下書き／右＝人物の範囲（青＝主人公・赤＝相手）／赤字＝model.json に未登録の構図",
                               fill="black", font=font)
    p = os.path.join(OUT_DIR, "_取り込み確認_%s.jpg" % time.strftime("%Y%m%d_%H%M"))
    sheet.save(p, quality=88)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="することだけ表示（何も書かない）")
    ap.add_argument("--no-crop", action="store_true", help="枠・余白を切り落とさない")
    a = ap.parse_args()
    if not os.path.exists(PICK_CSV):
        print("_採用.csv がありません。先に 候補を整理する.bat を実行してください: %s" % PICK_CSV); sys.exit(1)
    rows = read_rows()
    head = rows[0]
    ci, ni, fi, ki = head.index("採用"), head.index("取り込んだ名前"), head.index("ファイル名"), head.index("切り抜き")
    reg = registered()
    added, unreg, skipped = [], set(), []
    pending, hashes = {}, {}   # 今回入れる名前（構図名 → {番号: 名前}）と、その中身の md5
    for r in rows[1:]:
        comp = r[ci].strip()
        if comp in SKIP_WORDS or r[ni].strip():
            continue
        if not NAME_RE.match(comp):
            skipped.append((r[fi], "構図名「%s」は英小文字・数字・_ だけにしてください" % comp)); continue
        src = os.path.join(CAND, r[fi])
        if not os.path.isfile(src):
            skipped.append((r[fi], "_候補 に画像がない")); continue
        img = Image.open(src).convert("RGB")
        box, what = ((0, 0) + img.size, []) if a.no_crop else auto_crop(img)
        img = img.crop(box)
        used = ipr.existing(comp)
        used.update(pending.get(comp, {}))   # --dry-run で同じ構図が続くとき
        buf = io.BytesIO()
        img.save(buf, "PNG")
        h = hashlib.md5(buf.getvalue()).hexdigest()
        if any(f in hashes and hashes[f] == h or (f not in hashes and ipr.md5(os.path.join(PICK_DIR, f)) == h) for f in used.values()):
            skipped.append((r[fi], "同じ画像が %s にもう入っている" % comp)); continue
        dst = ipr.next_name(comp, used)
        n = int(dst[len(comp) + 1:-4]) if dst != comp + ".png" else 1
        pending.setdefault(comp, {})[n] = dst
        hashes[dst] = h
        if not a.dry_run:
            with open(os.path.join(PICK_DIR, dst), "wb") as fp:
                fp.write(buf.getvalue())
            r[ni], r[ki] = dst, (" / ".join(what) or "なし")
        added.append(dst[:-4])
        if comp not in reg:
            unreg.add(comp)
        print("  入れる: %s → %s  %dx%d  切り落とし: %s%s" % (r[fi], dst, img.size[0], img.size[1], " / ".join(what) or "なし",
                                                       "  ※model.json に未登録" if comp not in reg else ""))
    for f, why in skipped:
        print("  入れなかった: %s（%s）" % (f, why))
    print("%s %d 枚 / 入れなかった %d 枚" % ("入れる（--dry-run なので入れていない）" if a.dry_run else "入れた", len(added), len(skipped)))
    if a.dry_run or not added:
        if unreg:
            print("model.json に未登録の構図名:", ", ".join(sorted(unreg)))
        return
    with open(PICK_CSV, "w", encoding="utf-8-sig", newline="") as fp:
        csv.writer(fp).writerows(rows)
    print("\n---- 奥行き下書きを作る ----")
    subprocess.call([sys.executable, os.path.join(HERE, "depth_from_ref.py"), "--no-collect"], cwd=HERE)
    print("\n---- 人物の範囲を作る ----")
    subprocess.call([sys.executable, os.path.join(HERE, "make_region_masks.py"), "--only", ",".join(added)], cwd=HERE)
    p = check_sheet(added, unreg)
    print("\n今回入れた %d 枚: %s" % (len(added), ", ".join(added)))
    if p:
        print("確認用: %s" % p)
    if unreg:
        print("model.json に未登録の構図名（登録していません。撮影で使うには pose_control の ref_sets・ref_tags・ref_role に足す）:")
        for c in sorted(unreg):
            print("  %s" % c)


if __name__ == "__main__":
    main()
