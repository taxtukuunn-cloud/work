# -*- coding: utf-8 -*-
"""白黒の下書き（奥行き）の自動点検（2026-10-05・まとめツール 段階B の B7）
目的：全部を目で見なくて済むように、怪しい下書きにだけ印を付ける。グラフィックボードは使わない。
・計算で見つける（毎回同じ結果）
    頭が上の端で切れている／頭が横の端で切れている：人物の範囲（region_<名前>_hero／_partner.png）の頭の所が、手前の形のまま画面の端にかかっている
    黒い余白が残っている：元絵（構図下書き元）の上下左右に、真っ黒な一色の帯が 2% 以上ある
    長い直線が残っている：白黒の下書きに、画面の 6 割以上にわたるまっすぐな段差がある（窓枠・柱など）
・目で見た印（Claude が一覧を見て付けたもの）は 構図下書き\\_奥行き点検_目.json から読む
    形が読めない／小物や線が残っている／1人だけ／翼・尻尾・触手など
・結果
    構図下書き\\_奥行き点検.csv（下書きの名前・元絵の名前・構図名・印の種類・検出の方法・メモ・判定・相手の種類）
      判定・相手の種類は、まとめツールの画面で付けたもの。作り直しても残す
    構図下書き\\_奥行き点検_一覧_NN.png（全部・名前つき）／_奥行き点検_印あり_NN.png（印のある絵だけ・印つき）
・印が無い絵が必ず大丈夫とは限らない（縮小して見るため、小さな崩れは拾えない）。最後は確認撮影で確かめる
・白黒からは決めないこと：どちらが主人公か、筋肉質か、服の有無、技の種類（元の絵を人が見て決める）
使い方: python 奥行き点検.py [--no-sheet]"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFT = os.path.join(HERE, "構図下書き")
SRC = os.path.join(HERE, "構図下書き元")
CSV_PATH = os.path.join(DRAFT, "_奥行き点検.csv")
EYE_PATH = os.path.join(DRAFT, "_奥行き点検_目.json")
SHORT = {"頭が上の端で切れている": "頭が上で切れ", "頭が横の端で切れている": "頭が横で切れ", "黒い余白が残っている": "黒い余白", "長い直線が残っている": "長い直線",
         "翼・尻尾・触手など": "翼・尻尾など", "小物や線が残っている": "小物・線"}
HEAD = ["下書きの名前", "元絵の名前", "構図名", "印の種類", "検出の方法", "メモ", "判定", "相手の種類"]
TOP_CUT, SIDE_CUT, MARGIN, LINE = 0.3, 0.3, 0.02, 0.6


def measure(n):
    import numpy as np
    from PIL import Image
    a = np.asarray(Image.open(os.path.join(DRAFT, "depthref_%s.png" % n)).convert("L"), "float32")
    fg = a > max(60, a.max() * 0.45)   # 手前の形（白いほど手前）
    hm = np.zeros(a.shape, bool)       # 頭〜胸の範囲
    for role in ("hero", "partner"):
        p = os.path.join(DRAFT, "region_%s_%s.png" % (n, role))
        if os.path.exists(p):
            hm |= np.asarray(Image.open(p).convert("L").resize((a.shape[1], a.shape[0]))) > 200
    top = float((fg[:3] & hm[:3]).mean())
    side = float(max((fg[:, :3] & hm[:, :3]).mean(), (fg[:, -3:] & hm[:, -3:]).mean()))
    marg = 0.0
    sp = os.path.join(SRC, n + ".png")
    if os.path.exists(sp):
        s = np.asarray(Image.open(sp).convert("L"), "float32")
        H, W = s.shape

        def run(rows):
            k = 0
            for r in rows:
                if r.mean() < 20 and r.std() < 6:
                    k += 1
                else:
                    break
            return k
        marg = max(run(s) / H, run(s[::-1]) / H, run(s.T) / W, run(s.T[::-1]) / W)
    gy, gx = np.abs(a[2:, :] - a[:-2, :]), np.abs(a[:, 2:] - a[:, :-2])
    line = float(max((gy > 30).mean(1)[5:-5].max(), (gx > 30).mean(0)[5:-5].max()))
    return top, side, marg, line


def comp_of(n):
    return re.sub(r"_\d+$", "", n)


def read_model():
    try:
        mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    except Exception:
        return set(), {}
    pc = mj.get("pose_control") or {}
    return {x.lower() for x in pc.get("ref_exclude") or []}, pc.get("ref_tags") or {}


def main():
    names = sorted(f[9:-4] for f in os.listdir(DRAFT) if f.startswith("depthref_") and f.endswith(".png"))
    ex, tags = read_model()
    eye = {}
    if os.path.exists(EYE_PATH):
        eye = json.load(open(EYE_PATH, encoding="utf-8"))
    keep = {}   # 画面で付けた 判定・相手の種類 は残す
    if os.path.exists(CSV_PATH):
        for r in csv.DictReader(open(CSV_PATH, encoding="utf-8-sig")):
            if r.get("判定") or r.get("相手の種類"):
                keep[r["下書きの名前"]] = (r.get("判定", ""), r.get("相手の種類", ""))
    rows, flagged = [], {}
    for i, n in enumerate(names):
        top, side, marg, line = measure(n)
        d = "depthref_" + n
        tg = tags.get(comp_of(n), "")
        near = "（寄り・目線の構図では起きやすい）" if re.search(r"\bpov\b|close-up", tg) else ""
        fl = []
        if top >= TOP_CUT:
            fl.append(("頭が上の端で切れている", "計算", "上の端にかかる割合 %.2f%s" % (top, near)))
        if side >= SIDE_CUT:
            fl.append(("頭が横の端で切れている", "計算", "横の端にかかる割合 %.2f%s" % (side, near)))
        if marg >= MARGIN:
            fl.append(("黒い余白が残っている", "計算", "元絵の黒い帯 %.0f%%" % (marg * 100)))
        if line >= LINE:
            fl.append(("長い直線が残っている", "計算", "まっすぐな段差が画面の %.0f%%（窓枠・柱など）" % (line * 100)))
        for e in eye.get(n, []):
            fl.append((e["kind"], "目", e.get("memo", "")))
        if fl:
            flagged[n] = fl
        jd, kind = keep.get(d, ("", ""))
        for k, how, memo in fl:
            rows.append([d, n, comp_of(n), k, how, memo + ("（外した下書き）" if d.lower() in ex else ""), jd, kind])
        if not fl and (jd or kind):   # 印が消えても、画面で付けた相手の種類は残す
            rows.append([d, n, comp_of(n), "", "", "", jd, kind])
        if i % 100 == 99:
            print("  %d / %d" % (i + 1, len(names)))
    with open(CSV_PATH + ".tmp", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEAD)
        w.writerows(rows)
    os.replace(CSV_PATH + ".tmp", CSV_PATH)
    cnt = {}
    for r in rows:
        if r[3]:
            cnt[r[3]] = cnt.get(r[3], 0) + 1
    print("\n点検した下書き: %d 枚／印のある下書き: %d 枚" % (len(names), len(flagged)))
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        print("  %-16s %d" % (k, v))
    print("→ %s" % CSV_PATH)
    if "--no-sheet" not in sys.argv:
        sheets(names, flagged)


def sheets(names, flagged):
    from PIL import Image, ImageDraw, ImageFont
    try:
        font = ImageFont.truetype(r"C:\Windows\Fonts\meiryo.ttc", 12)
    except Exception:
        font = ImageFont.load_default()
    for f in os.listdir(DRAFT):
        if re.match(r"^_奥行き点検_(一覧|印あり)_\d+\.png$", f):
            os.remove(os.path.join(DRAFT, f))
    C, R, cw = 8, 5, 180

    def make(lst, label, prefix):
        ch = 300 if label else 290
        n = 0
        for k in range(0, len(lst), C * R):
            part = lst[k:k + C * R]
            im = Image.new("RGB", (cw * C, ch * ((len(part) + C - 1) // C)), "white")
            dr = ImageDraw.Draw(im)
            for i, nm in enumerate(part):
                t = Image.open(os.path.join(DRAFT, "depthref_%s.png" % nm)).convert("RGB")
                t.thumbnail((cw - 6, 240))
                x, y = (i % C) * cw, (i // C) * ch
                im.paste(t, (x + 3 + (cw - 6 - t.width) // 2, y + 3))
                dr.text((x + 3, y + 246), nm[:26], fill="black", font=font)
                if label:   # 一覧では短い名前で（隣の絵にはみ出さないように）
                    t = "・".join(sorted({SHORT.get(a, a) for a, _, _ in flagged[nm]}))
                    dr.text((x + 3, y + 262), t[:14], fill="red", font=font)
                    dr.text((x + 3, y + 278), t[14:28], fill="red", font=font)
            n += 1
            im.save(os.path.join(DRAFT, "_奥行き点検_%s_%02d.png" % (prefix, n)))
        return n
    a = make(names, False, "一覧")
    b = make([n for n in names if n in flagged], True, "印あり")
    print("一覧画像: 全部 %d 枚・印あり %d 枚 → %s\\_奥行き点検_*.png" % (a, b, DRAFT))


if __name__ == "__main__":
    main()
