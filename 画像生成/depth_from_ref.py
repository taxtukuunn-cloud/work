# -*- coding: utf-8 -*-
"""選んだ構図の元絵から奥行き（depth）下書きを作る（2026-10-01）
流れ：
  1) output\\構図候補\\<構図名>\\ に残っている画像を「選んだ画像」とみなし、
     構図下書き元\\ に <構図名>.png / <構図名>_2.png … の名前でコピー（同じ中身は入れない）
     ※ --no-collect を付けるとこの手順を飛ばす（構図下書き元 に手で入れた分だけ使う）
  2) 構図下書き元\\ の各画像から Depth Anything V2 で奥行きを推定し、
     構図下書き\\depthref_<元の名前>.png に保存（832x1216、手前ほど白）
     2026-10-02 横長：元絵が横長（幅＞高さ）なら 1216x832 で作る（gen.py はその絵だけ横長で撮る）
     小さい形は最終プロンプトで決めるため、ぼかして大きな形だけ残す（--blur で強さ変更、0 でなし）
     すでに作ってあり、元絵の方が古ければ作り直さない（--force で全部作り直し）
  3) 構図下書き\\_元絵奥行き一覧.png に「元絵｜奥行き」を並べた確認用の一覧を作る
  4) ComfyUI\\input\\pose_depthref_<名前>.png に置く（gen.py が本番で使う）。
     元絵を消した構図下書きは、depthref_ と pose_depthref_ も片づける（使えない下書きを外すときは元絵を消して再実行）
初回だけ Hugging Face から推定モデル（Small 約100MB）を自動ダウンロードします。
"""
import argparse, os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import import_pose_ref as ipr
from PIL import Image, ImageDraw, ImageFilter, ImageFont

PICK_DIR = ipr.PICK_DIR
CAND = ipr.CAND
OUT_DIR = os.path.join(HERE, "構図下書き")
COMFY_INPUT = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(CAND)), "input"))
SIZE = (832, 1216)
SIZE_LAND = (1216, 832)   # 2026-10-02 横長の元絵
MODELS = {"small": "depth-anything/Depth-Anything-V2-Small-hf",
          "base": "depth-anything/Depth-Anything-V2-Base-hf"}


SEEN = os.path.join(PICK_DIR, "_取り込み済み.txt")   # 一度取り込んだ画像（中身の md5）。消した元絵を次の実行で入れ直さないため


def collect():
    if not os.path.isdir(CAND):
        print("構図候補フォルダがありません: %s" % CAND); return 0
    seen = set(open(SEEN, encoding="utf-8").read().split()) if os.path.exists(SEEN) else set()
    for f in os.listdir(PICK_DIR):   # 今ある元絵も取り込み済みとして記録
        if f.lower().endswith(".png"):
            seen.add(ipr.md5(os.path.join(PICK_DIR, f)))
    n = 0
    for cid in sorted(os.listdir(CAND)):
        d = os.path.join(CAND, cid)
        if not os.path.isdir(d):
            continue
        used = ipr.existing(cid)
        hashes = {ipr.md5(os.path.join(PICK_DIR, f)) for f in used.values()}
        for f in sorted(os.listdir(d)):
            if not f.lower().endswith(".png"):
                continue
            p = os.path.join(d, f)
            h = ipr.md5(p)
            if h in hashes or h in seen:
                continue
            dst = ipr.next_name(cid, used)
            ipr.shutil.copy2(p, os.path.join(PICK_DIR, dst))
            used[int(dst[len(cid) + 1:-4]) if dst != cid + ".png" else 1] = dst
            hashes.add(h)
            seen.add(h)
            n += 1
    with open(SEEN, "w", encoding="utf-8") as fp:
        fp.write("\n".join(sorted(seen)) + "\n")
    return n


def apply_judged():
    """_元の名前.csv の「実際の構図」列を反映する（2026-10-01）。
    構図名 → その構図の名前に付け替え（例 headlock_3.png → hj_behind_seated_7.png）／「消す」→ 構図下書き元\\_消した\\ へ移す（元に戻せる）。
    空欄はそのまま。反映後、対応表は作り直されるので列は消える"""
    import csv, shutil
    path = os.path.join(PICK_DIR, "_元の名前.csv")
    if not os.path.exists(path):
        return
    rows = list(csv.reader(open(path, encoding="utf-8-sig")))
    if not rows or "実際の構図" not in rows[0]:
        return
    ci = rows[0].index("実際の構図")
    known = set(os.listdir(CAND)) if os.path.isdir(CAND) else set()
    trash = os.path.join(PICK_DIR, "_消した")
    moved = gone = 0
    for r in rows[1:]:
        if len(r) <= ci or not r[ci].strip():
            continue
        f, to = r[0].strip(), r[ci].strip()
        src = os.path.join(PICK_DIR, f)
        if not os.path.exists(src):
            continue
        if to == "消す":
            os.makedirs(trash, exist_ok=True)
            shutil.move(src, os.path.join(trash, f)); gone += 1
            print("  消した: %s（_消した に移動）" % f)
            continue
        if known and to not in known:
            print("  [注意] %s の「%s」という構図はありません（名前の確認を）。そのままにします" % (f, to)); continue
        dst = ipr.next_name(to, ipr.existing(to))
        os.rename(src, os.path.join(PICK_DIR, dst)); moved += 1
        print("  付け替え: %s → %s" % (f, dst))
    print("実際の構図を反映: 付け替え %d 枚 / 消した %d 枚" % (moved, gone))


def write_map():
    """構図下書き元\\_元の名前.csv：取り込んだ名前 ⇔ 構図候補での元の名前（ComfyUI の連番）。番号がずれて紛らわしいため（2026-10-01）"""
    cand = {}
    if os.path.isdir(CAND):
        for cid in os.listdir(CAND):
            d = os.path.join(CAND, cid)
            if os.path.isdir(d):
                for f in os.listdir(d):
                    if f.lower().endswith(".png"):
                        cand.setdefault(ipr.md5(os.path.join(d, f)), "%s\\%s" % (cid, f))
    rows = ["取り込んだ名前,構図候補での元の名前"]
    for f in sorted(os.listdir(PICK_DIR)):
        if f.lower().endswith(".png"):
            rows.append("%s,%s" % (f, cand.get(ipr.md5(os.path.join(PICK_DIR, f)), "（構図候補に無い）")))
    with open(os.path.join(PICK_DIR, "_元の名前.csv"), "w", encoding="utf-8-sig") as fp:
        fp.write("\n".join(rows) + "\n")
    print("名前の対応表: %s" % os.path.join(PICK_DIR, "_元の名前.csv"))


def size_for(w, h):
    """元絵の向きで下書きの大きさを決める（横長＝1216x832／それ以外＝832x1216）"""
    return SIZE_LAND if w > h else SIZE


def fit(img):
    """832x1216（横長の元絵は 1216x832）に合わせる（比率が違えば中央で切り抜き）"""
    w, h = img.size
    tw, th = size_for(w, h)
    s = max(tw / w, th / h)
    img = img.resize((max(tw, round(w * s)), max(th, round(h * s))), Image.LANCZOS)
    w, h = img.size
    l, t = (w - tw) // 2, (h - th) // 2
    return img.crop((l, t, l + tw, t + th))


def load_pipe(kind):
    import torch
    from transformers import pipeline
    dev = 0 if torch.cuda.is_available() else -1
    print("推定モデル: %s（%s）" % (MODELS[kind], "GPU" if dev == 0 else "CPU"))
    return pipeline("depth-estimation", model=MODELS[kind], device=dev)


def to_depth(pipe, img, blur):
    import numpy as np
    r = pipe(img)
    d = r["predicted_depth"]
    d = d.squeeze().float().cpu().numpy()
    lo, hi = np.percentile(d, 1), np.percentile(d, 99)
    d = ((d - lo) / max(hi - lo, 1e-6)).clip(0, 1)
    out = Image.fromarray((d * 255).astype("uint8")).resize(img.size, Image.BICUBIC)
    if blur > 0:
        out = out.filter(ImageFilter.GaussianBlur(blur))
    return out.convert("RGB")


def sheet(pairs):
    if not pairs:
        return
    tw, th = 208, 304
    cols = 4  # 1組＝元絵＋奥行きの2枚
    rows = math.ceil(len(pairs) / cols)
    W, H = cols * tw * 2, rows * (th + 22)
    img = Image.new("RGB", (W, H), "white")
    dr = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", 14)
    except Exception:
        font = ImageFont.load_default()
    def tile(p):   # 横長の絵も縦横比を保って枠に収める（2026-10-02）
        t = Image.open(p).convert("RGB")
        t.thumbnail((tw, th))
        return t
    for i, (name, src, dep) in enumerate(pairs):
        x, y = (i % cols) * tw * 2, (i // cols) * (th + 22)
        for k, p in enumerate((src, dep)):
            t = tile(p)
            img.paste(t, (x + k * tw + (tw - t.width) // 2, y + (th - t.height) // 2))
        dr.text((x + 4, y + th + 3), name, fill="black", font=font)
    p = os.path.join(OUT_DIR, "_元絵奥行き一覧.png")
    img.save(p)
    print("確認用の一覧: %s" % p)


def deploy():
    """構図下書き\\depthref_*.png → ComfyUI\\input\\pose_depthref_*.png。元絵の無いものは片づける"""
    import shutil
    srcs = {f for f in os.listdir(PICK_DIR) if f.lower().endswith(".png")}
    gone = 0
    for f in os.listdir(OUT_DIR):
        if f.startswith("depthref_") and f.lower().endswith(".png") and f[len("depthref_"):] not in srcs:
            os.remove(os.path.join(OUT_DIR, f)); gone += 1
    if not os.path.isdir(COMFY_INPUT):
        print("ComfyUI の input フォルダがありません: %s" % COMFY_INPUT); return
    have = {f for f in os.listdir(OUT_DIR) if f.startswith("depthref_") and f.lower().endswith(".png")}
    put = 0
    for f in sorted(have):
        s, d = os.path.join(OUT_DIR, f), os.path.join(COMFY_INPUT, "pose_" + f)
        if not os.path.exists(d) or os.path.getmtime(d) < os.path.getmtime(s):
            shutil.copy2(s, d); put += 1
    for f in os.listdir(COMFY_INPUT):
        if f.startswith("pose_depthref_") and f[len("pose_"):] not in have:
            # 2026-10-02 人物の範囲（pose_depthref_<名前>_hero／_partner.png）は消さない（片づけは make_region_masks.py がする）
            m = ipr.re.match(r"^pose_(depthref_.+)_(?:hero|partner)\.png$", f)
            if m and m.group(1) + ".png" in have:
                continue
            os.remove(os.path.join(COMFY_INPUT, f)); gone += 1
    print("ComfyUI\\input に置いた: %d 枚 / 片づけた: %d 枚（本番で使える奥行き下書き %d 枚）" % (put, gone, len(have)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-collect", action="store_true", help="構図候補からの取り込みをしない")
    ap.add_argument("--force", action="store_true", help="全部作り直す")
    ap.add_argument("--blur", type=float, default=3.0, help="ぼかしの強さ（0でなし）")
    ap.add_argument("--model", choices=list(MODELS), default="small")
    ap.add_argument("--only", default="", help="この構図名だけ（カンマ区切り）")
    a = ap.parse_args()
    os.makedirs(PICK_DIR, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    apply_judged()
    if not a.no_collect:
        print("構図候補から取り込み: %d 枚" % collect())
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    srcs = sorted(f for f in os.listdir(PICK_DIR) if f.lower().endswith(".png"))
    if only:
        srcs = [f for f in srcs if ipr.re.sub(r"(_\d+)?\.png$", "", f, flags=ipr.re.I) in only]
    todo, pairs = [], []
    for f in srcs:
        src = os.path.join(PICK_DIR, f)
        dep = os.path.join(OUT_DIR, "depthref_" + f)
        pairs.append((f[:-4], src, dep))
        if a.force or not os.path.exists(dep) or os.path.getmtime(dep) < os.path.getmtime(src):
            todo.append((f, src, dep))
    print("元絵 %d 枚 / 奥行きを作る %d 枚" % (len(srcs), len(todo)))
    if todo:
        pipe = load_pipe(a.model)
        for i, (f, src, dep) in enumerate(todo, 1):
            try:
                img = fit(Image.open(src).convert("RGB"))
                to_depth(pipe, img, a.blur).save(dep)
                print("  [%d/%d] %s → %s" % (i, len(todo), f, os.path.basename(dep)))
            except Exception as e:
                print("  [%d/%d] %s 失敗: %s" % (i, len(todo), f, e))
    sheet([p for p in pairs if os.path.exists(p[2])])
    deploy()
    write_map()
    print("完了 → %s" % OUT_DIR)


if __name__ == "__main__":
    main()
