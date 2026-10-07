# -*- coding: utf-8 -*-
"""選んだ元絵を 構図下書き元\\ に正しい名前で入れる（2026-09-30）
ComfyUI が付けた名前（例 peg_doggy_00003_.png）から構図名（peg_doggy）を読み取り、
構図下書き元\\peg_doggy.png、2枚目以降は peg_doggy_2.png, peg_doggy_3.png … の空いている番号で入れる。
使い方は2通り：
  1) 選んだ画像を 元絵を取り込む.bat にドラッグ＆ドロップ（何枚でも・複数の構図が混ざってもよい）→ コピー（元の画像は残る）
  2) 選んだ画像を 構図下書き元\\_入れる\\ に入れてから 元絵を取り込む.bat をダブルクリック → 移動
・同じ画像（中身が同じ）がすでに入っていれば入れない。
・名前から構図名が読めない画像は入れない（名前を変えていたら、構図名_00001_.png の形に戻すか手で置く）。"""
import hashlib, os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PICK_DIR = os.path.join(HERE, "構図下書き元")
INBOX = os.path.join(PICK_DIR, "_入れる")
CAND = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output", "構図候補")
NAME_RE = re.compile(r"^(.+?)_\d{5}_\.png$", re.I)


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def existing(cid):
    rx = re.compile(r"^%s(?:_(\d+))?\.png$" % re.escape(cid), re.I)
    out = {}
    for f in os.listdir(PICK_DIR):
        m = rx.match(f)
        if m:
            out[int(m.group(1) or 1)] = f
    return out


def next_name(cid, used):
    if 1 not in used:
        return cid + ".png"
    n = 2
    while n in used:
        n += 1
    return "%s_%d.png" % (cid, n)


def main():
    os.makedirs(INBOX, exist_ok=True)
    args = [a for a in sys.argv[1:] if a.strip()]
    move = not args
    files = args if args else [os.path.join(INBOX, f) for f in sorted(os.listdir(INBOX)) if f.lower().endswith(".png")]
    if not files:
        print("入れる画像がありません。")
        print("  選んだ画像をこの bat にドラッグ＆ドロップするか、%s に入れてから実行してください。" % INBOX)
        return
    known = set(os.listdir(CAND)) if os.path.isdir(CAND) else set()
    added, skipped = [], []
    for p in files:
        name = os.path.basename(p)
        if not os.path.isfile(p) or not name.lower().endswith(".png"):
            skipped.append((name, "png ファイルではない")); continue
        m = NAME_RE.match(name)
        if not m:
            skipped.append((name, "名前から構図名が読めない（構図名_00001_.png の形ではない）")); continue
        cid = m.group(1)
        if known and cid not in known:
            skipped.append((name, "構図候補に %s というフォルダがない（構図名の確認を）" % cid)); continue
        used = existing(cid)
        h = md5(p)
        if any(md5(os.path.join(PICK_DIR, f)) == h for f in used.values()):
            skipped.append((name, "同じ画像がもう入っている"))
            continue
        dst = next_name(cid, used)
        if move:
            shutil.move(p, os.path.join(PICK_DIR, dst))
        else:
            shutil.copy2(p, os.path.join(PICK_DIR, dst))
        added.append((name, dst))
    for s, d in added:
        print("  入れた: %s → %s" % (s, d))
    for s, why in skipped:
        print("  入れなかった: %s（%s）" % (s, why))
    print("入れた %d 枚 / 入れなかった %d 枚 → %s" % (len(added), len(skipped), PICK_DIR))


if __name__ == "__main__":
    main()
