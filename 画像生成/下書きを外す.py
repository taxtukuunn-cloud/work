# -*- coding: utf-8 -*-
"""撮った絵の下書き一覧.csv で「外す」に何か書いた行の下書きを、model.json の pose_control.ref_exclude に足す（2026-10-02）。
下書きのファイルは消さない（使わなくなるだけ）。model.json は 変更前 を model_下書き除外_前.json に残す"""
import csv, json, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "撮った絵の下書き一覧.csv")
MJ = os.path.join(HERE, "model.json")
rows = list(csv.reader(open(CSV, encoding="utf-8-sig")))[1:]
pick = {}
for r in rows:
    if len(r) > 2 and r[2].strip():
        for ref in [x.strip() for x in r[1].split(",")]:
            if ref.startswith("depthref_"):
                pick.setdefault(ref, r[0])
            elif ref and ref != "（下書きなし）":
                print("外せない下書き（元絵の下書きではない）:", ref, " ←", r[0])
if not pick:
    print("○の付いた行がありません。"); raise SystemExit
raw = open(MJ, "rb").read()
m = json.loads(raw.decode("utf-8"))
ex = m["pose_control"].setdefault("ref_exclude", [])
new = [k for k in pick if k not in ex]
if not new:
    print("もう全部外してあります。"); raise SystemExit
shutil.copyfile(MJ, os.path.join(HERE, "model_下書き除外_前.json"))
ex += new
m["pose_control"]["ref_exclude_memo"] = m["pose_control"].get("ref_exclude_memo", "") + "／" + "、".join("%s（%s）" % (k[9:], pick[k]) for k in new)
open(MJ, "wb").write((json.dumps(m, ensure_ascii=False, indent=2).replace("\n", "\r\n") + "\r\n").encode("utf-8"))
print("外した下書き %d枚:" % len(new)); [print("  ", k, "←", pick[k]) for k in new]
