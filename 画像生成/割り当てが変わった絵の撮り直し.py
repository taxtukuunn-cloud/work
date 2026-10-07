# -*- coding: utf-8 -*-
"""撮り済みの絵のうち、いまの割り当てと違う下書きで撮られている場面だけを撮り直す（2026-10-04）
使い方: python 割り当てが変わった絵の撮り直し.py [MOD,MOD…] [--dry-run]
  MOD を省略すると全MOD。--dry-run は一覧を出すだけ（撮らない）。
流れ:
  1) 下見_全場面.csv（gen.py all all --model wai --preview が作る「いまの割り当て」）を読む
  2) 各MODの保存先（output\\<MOD>_WAI_<絵柄>。絵柄割当.csv のとおり）で、場面ごとにいちばん新しい絵の
     埋め込み設定から「撮ったときの下書き」を読む
  3) いまの割り当てと違う場面だけ gen.py <MOD> <名前,…> --model wai --redo で撮り直す
・まだ撮っていない場面、立ち絵など下書きを使わない絵は何もしない。
・元の絵は消さない（番号が増えた新しい絵ができ、完成フォルダへ集めるときは新しい方が採用される）。
・一覧は 割り当てが変わった絵_一覧.csv に残す（MOD・画像名・撮ったときの下書き・いまの下書き）。"""
import csv, json, os, re, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
DRY = "--dry-run" in sys.argv
ONLY = {x.strip() for x in args[0].split(",") if x.strip()} if args else None
PREVIEW = os.path.join(HERE, "下見_全場面.csv")
if not os.path.exists(PREVIEW):
    print("下見_全場面.csv がありません。先に 下見_全MOD.bat を実行してください。"); sys.exit(1)

now = {}   # (MOD, 画像名) → いまの下書き（無ければ ""）
for r in csv.DictReader(open(PREVIEW, encoding="utf-8-sig")):
    if re.search(r"_(?:atk|lose)_", r["画像名"]) and "組み立て失敗" not in (r.get("注意") or ""):
        now[(r["MOD"], r["画像名"])] = (r.get("下書き") or "").strip()

def shot_draft(path):
    """絵に埋め込まれた設定から、撮ったときの下書き名（pose_ と .png を外したもの）。下書きなしは ""。読めなければ None"""
    try:
        pr = json.loads(Image.open(path).info.get("prompt") or "")
    except Exception:
        return None
    n = pr.get("71")
    if isinstance(n, dict) and n.get("class_type") == "LoadImage":
        return re.sub(r"^pose_|\.png$", "", str(n["inputs"].get("image", "")), flags=re.I)
    return ""

rx = re.compile(r"^(.+)_(\d{5})_\.png$", re.I)
todo, rows, total, unread = [], [], 0, 0
for r in list(csv.reader(open(os.path.join(HERE, "絵柄割当.csv"), encoding="utf-8-sig")))[1:]:
    if not r or not r[0].strip():
        continue
    mod, style = r[0].strip(), (r[1].strip() if len(r) > 1 else "")
    if ONLY and mod not in ONLY:
        continue
    d = os.path.join(OUT, mod + "_WAI" + ("_" + style if style and style != "本編" else ""))
    if not os.path.isdir(d):
        continue
    newest = {}
    for f in os.listdir(d):
        m = rx.match(f)
        if m and (m.group(1) not in newest or int(m.group(2)) > newest[m.group(1)][0]):
            newest[m.group(1)] = (int(m.group(2)), f)
    names = []
    for name, (_, f) in sorted(newest.items()):
        if (mod, name) not in now:
            continue
        old = shot_draft(os.path.join(d, f))
        if old is None:
            unread += 1
            continue
        if old.lower() != now[(mod, name)].lower():
            names.append(name)
            rows.append([mod, name, old or "（下書きなし）", now[(mod, name)] or "（下書きなし）"])
    if names:
        todo.append((mod, names))
        total += len(names)
        print("  %-10s %d枚: %s" % (mod, len(names), ", ".join(names)))
with open(os.path.join(HERE, "割り当てが変わった絵_一覧.csv"), "w", encoding="utf-8-sig", newline="") as fp:
    csv.writer(fp).writerows([["MOD", "画像名", "撮ったときの下書き", "いまの下書き"]] + rows)
print("撮り直す絵: %d枚（%d MOD）%s → 割り当てが変わった絵_一覧.csv" % (total, len(todo), ("／設定を読めなかった絵 %d枚" % unread) if unread else ""))
if DRY or not todo:
    sys.exit(0)
for mod, names in todo:
    for i in range(0, len(names), 20):   # 画像名が多いと1行が長くなりすぎるので 20枚ずつ
        subprocess.call([sys.executable, os.path.join(HERE, "gen.py"), mod, ",".join(names[i:i + 20]), "--model", "wai", "--redo"], cwd=HERE)
