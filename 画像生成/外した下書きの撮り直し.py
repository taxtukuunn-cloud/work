# -*- coding: utf-8 -*-
"""外した下書き（model.json pose_control.ref_exclude）で撮ってしまった絵だけを探して撮り直す（2026-10-03）
使い方: python 外した下書きの撮り直し.py [下書き名,下書き名…] [--dry-run]
  下書き名を省略すると finger_front_legs。 例) python 外した下書きの撮り直し.py finger_front_legs,rah_behind_4
・各MODの今の保存先（output\\<MOD>_WAI_<絵柄>。絵柄割当.csv のとおり）にある png の埋め込み設定を読み、
  場面ごとにいちばん新しい絵がその下書きで撮られていたら gen.py <MOD> <名前,…> --model wai --redo で撮り直す。
・まだ撮っていない場面は何もしない。元の絵は消さない（番号が増えた新しい絵ができ、完成フォルダへ集めるときは新しい方が採用される）。"""
import csv, json, os, re, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
DRY = "--dry-run" in sys.argv
bad = {"pose_depthref_%s.png" % re.sub(r"^(pose_)?(depthref_)?", "", x.strip()).replace(".png", "").lower()
       for x in (args[0] if args else "finger_front_legs").split(",") if x.strip()}
print("探す下書き:", ", ".join(sorted(bad)))
try:
    ex = {str(x).lower() for x in json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8-sig"))["pose_control"].get("ref_exclude") or []}
    for b in sorted(bad):
        if b[5:-4] not in ex:
            print("※ %s は model.json の ref_exclude に入っていません（撮り直しても同じ下書きになるかもしれません）" % b[5:-4])
except Exception as e:
    print("model.json を読めませんでした:", e)
rx = re.compile(r"^(.+)_(\d{5})_\.png$", re.I)
todo, total = [], 0
for r in list(csv.reader(open(os.path.join(HERE, "絵柄割当.csv"), encoding="utf-8-sig")))[1:]:
    if not r or not r[0].strip():
        continue
    mod, style = r[0].strip(), (r[1].strip() if len(r) > 1 else "")
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
        try:
            pr = json.loads(Image.open(os.path.join(d, f)).info.get("prompt") or "{}")
        except Exception:
            continue
        if any(n.get("class_type") == "LoadImage" and str(n["inputs"].get("image", "")).lower() in bad for n in pr.values()):
            names.append(name)
    if names:
        todo.append((mod, names))
        total += len(names)
        print("  %-10s %d枚: %s" % (mod, len(names), ", ".join(names)))
print("撮り直す絵: %d枚（%d MOD）" % (total, len(todo)))
if DRY or not todo:
    sys.exit(0)
for mod, names in todo:
    subprocess.call([sys.executable, os.path.join(HERE, "gen.py"), mod, ",".join(names), "--model", "wai", "--redo"], cwd=HERE)
