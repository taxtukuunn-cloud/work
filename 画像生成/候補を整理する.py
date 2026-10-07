# -*- coding: utf-8 -*-
"""構図下書き元\\_候補\\ の元絵候補を整理する（2026-10-03）。見るのは _候補\\ だけ。
  1) まだ番号の無い画像に c0001 から通し番号を付ける（名前の先頭に「c0001_」を足す。元の名前は残る）
     → _候補\\_候補一覧.csv に「番号・今の名前・元の名前・大きさ・付けた日時」を追記
  2) 中身が同じ・ほぼ同じ画像（差分）は、先に番号を付けた1枚を残す
     → 後の方は _採用.csv の「採用」に 見送り、「備考」に どれと同じか を書く（消さない）
  3) _候補\\_採用.csv の「採用」が 見送り の画像を _候補\\_見送り\\ へ移す（消さない。戻すときは手で戻す）
  4) _候補\\_一覧\\一覧_01.jpg …（20枚ずつ・長辺2000px・各コマに番号）を作り直す（_見送り の画像は入れない）
_採用.csv の「採用」は空欄のままでよい（見送り と書いたものだけ動かす）。
使い方: python 候補を整理する.py [--dry-run]"""
import argparse, csv, hashlib, os, re, shutil, sys, time
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.join(HERE, "構図下書き元", "_候補")
LIST_CSV = os.path.join(CAND, "_候補一覧.csv")
PICK_CSV = os.path.join(CAND, "_採用.csv")
SKIP_DIR = os.path.join(CAND, "_見送り")
SHEET_DIR = os.path.join(CAND, "_一覧")
EXTS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")
NUM_RE = re.compile(r"^c(\d{4,})_", re.I)
SIMILAR = 18.0   # 縮小した白黒画像の平均の差（0〜255）。これ以下を「ほぼ同じ」とみなす（2026-10-03 の56枚：差分は4〜17・別の場面は32以上）
PER, COLS, CW, CH = 20, 5, 400, 300   # 1枚に20コマ（5x4）・2000x1200


def images(d):
    return sorted(f for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f.lower().endswith(EXTS)) if os.path.isdir(d) else []


def read_csv(p):
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as fp:
        return list(csv.reader(fp))


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def feat(p):
    with Image.open(p) as im:
        g = im.convert("L").resize((48, 48), Image.BILINEAR)
        return list(getattr(g, "get_flattened_data", g.getdata)())


def diff(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="何もせず、することだけ表示")
    a = ap.parse_args()
    if not os.path.isdir(CAND):
        print("候補フォルダがありません: %s" % CAND); sys.exit(1)
    dry = a.dry_run

    # ---- 1) 番号を付ける ----
    rows = read_csv(LIST_CSV)
    used = set()
    for r in rows[1:]:
        m = re.match(r"^c(\d+)$", r[0]) if r else None
        if m:
            used.add(int(m.group(1)))
    for d in (CAND, SKIP_DIR):
        for f in images(d):
            m = NUM_RE.match(f)
            if m:
                used.add(int(m.group(1)))
    nxt = max(used) + 1 if used else 1
    new = [f for f in images(CAND) if not NUM_RE.match(f)]
    new.sort(key=lambda f: (os.path.getmtime(os.path.join(CAND, f)), f))   # 置いた順
    added = []
    for f in new:
        num = "c%04d" % nxt
        nxt += 1
        dst = "%s_%s" % (num, f)
        with Image.open(os.path.join(CAND, f)) as im:
            size = "%dx%d" % im.size
        if not dry:
            os.rename(os.path.join(CAND, f), os.path.join(CAND, dst))
        added.append([num, dst, f, size, time.strftime("%Y-%m-%d %H:%M")])
        print("  番号: %s → %s" % (f, dst))
    if added and not dry:
        head = [] if rows else [["番号", "今の名前", "元の名前", "大きさ", "付けた日時"]]
        with open(LIST_CSV, "a", encoding="utf-8-sig" if not rows else "utf-8", newline="") as fp:
            csv.writer(fp).writerows(head + added)
    print("番号を付けた: %d 枚" % len(added))

    # ---- 2) 同じ・ほぼ同じ画像 → _採用.csv に 見送り の案 ----
    prow = read_csv(PICK_CSV)
    if not prow:
        prow = [["番号", "ファイル名", "採用", "備考"]]
    known = {r[0] for r in prow[1:] if r}
    here = [f for f in images(CAND) if NUM_RE.match(f)]
    if dry:   # 番号を付けた後の名前で考える
        here = sorted(here + [r[1] for r in added])
    here.sort(key=lambda f: int(NUM_RE.match(f).group(1)))
    src_of = {r[1]: r[2] for r in added}
    F, H = {}, {}
    for f in here:
        p = os.path.join(CAND, src_of.get(f, f) if dry else f)
        F[f], H[f] = feat(p), md5(p)
    seen, rep, dup = [], {}, 0   # rep：差分 → 残す1枚（差分が連なっても代表にまとめる）
    for f in here:
        num = NUM_RE.match(f).group(0)[:-1]
        same = next((k for k in seen if H[k] == H[f]), None)
        near = None
        if same is None:
            best = min(((diff(F[f], F[k]), k) for k in seen), default=None)
            if best and best[0] <= SIMILAR:
                near = best
        if same or near:
            rep[f] = rep.get(same or near[1], same or near[1])
        if num not in known:
            if same or near:
                k = NUM_RE.match(rep[f]).group(0)[:-1]
                note = "%s と同じ中身" % k if same else "%s とほぼ同じ（差 %.1f）" % (k, near[0])
                prow.append([num, f, "見送り", note]); dup += 1
                print("  見送りの案: %s（%s）" % (f, note))
            else:
                prow.append([num, f, "", ""])
            known.add(num)
        seen.append(f)
    print("同じ・ほぼ同じで見送りにした: %d 枚（_採用.csv。採用したいものは 見送り を消して、_見送り から戻す）" % dup)

    # ---- 3) 見送り → _見送り へ移す ----
    moved = 0
    for r in prow[1:]:
        if len(r) > 2 and r[2].strip() == "見送り":
            p = os.path.join(CAND, r[1])
            if os.path.isfile(p):
                if not dry:
                    os.makedirs(SKIP_DIR, exist_ok=True)
                    shutil.move(p, os.path.join(SKIP_DIR, r[1]))
                moved += 1
    if not dry:
        with open(PICK_CSV, "w", encoding="utf-8-sig", newline="") as fp:
            csv.writer(fp).writerows(prow)
    print("_見送り へ移した: %d 枚" % moved)

    # ---- 4) 一覧画像 ----
    if dry:
        return
    os.makedirs(SHEET_DIR, exist_ok=True)
    show = sorted((f for f in images(CAND) if NUM_RE.match(f)), key=lambda f: int(NUM_RE.match(f).group(1)))
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 30)
    except Exception:
        font = ImageFont.load_default()
    n = 0
    for s in range(0, len(show), PER):
        part = show[s:s + PER]
        rws = (len(part) + COLS - 1) // COLS
        sheet = Image.new("RGB", (COLS * CW, rws * CH), "black")
        dr = ImageDraw.Draw(sheet)
        for k, f in enumerate(part):
            with Image.open(os.path.join(CAND, f)) as im:
                t = im.convert("RGB")
                t.thumbnail((CW - 4, CH - 4))
            x, y = (k % COLS) * CW, (k // COLS) * CH
            sheet.paste(t, (x + (CW - t.width) // 2, y + (CH - t.height) // 2))
            dr.rectangle([x, y, x + 100, y + 38], fill="black")
            dr.text((x + 5, y + 2), NUM_RE.match(f).group(0)[:-1], fill="yellow", font=font)
        n += 1
        sheet.save(os.path.join(SHEET_DIR, "一覧_%02d.jpg" % n), quality=88)
    for f in os.listdir(SHEET_DIR):   # 枚数が減ったときの古い一覧（この道具が作ったものだけ）
        m = re.match(r"^一覧_(\d+)\.jpg$", f)
        if m and int(m.group(1)) > n:
            os.remove(os.path.join(SHEET_DIR, f))
    print("一覧: %d 枚（候補 %d 枚）→ %s" % (n, len(show), SHEET_DIR))


if __name__ == "__main__":
    main()
