# -*- coding: utf-8 -*-
"""自作した画像を、ゲームで使う名前（例 Host_atk_m1.png）にそろえて 画像生成\完成\<MODコード>\ にコピーする。
使い方: python collect.py <MODコード|all|コード,コード,...> [wai|anima]
  集める元は model.json のモデル（wai＝output\<MOD>_WAI\／anima＝output\<MOD>_自作\）。2つ目に wai / anima を書けばそちら。
絵柄割当.csv で絵柄を決めたMODは output\<MOD>_WAI_<絵柄>\ から集める（2026-09-29）。
同じ名前が複数あれば一番新しいものを使う。気に入らない画像は ComfyUI の出力フォルダから先に消しておくこと。"""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
arg = sys.argv[1] if len(sys.argv) > 1 else "all"
import json
try:
    model = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8")).get("model", "wai")
except Exception:
    model = "wai"
if len(sys.argv) > 2 and sys.argv[2].lower() in ("wai", "anima"):
    model = sys.argv[2].lower()
SUFFIX = "_WAI" if model == "wai" else "_自作"
print("集める元: output\\<MODコード>%s\\（%s）" % (SUFFIX, model))
allmods = sorted(f[:-5] for f in os.listdir(os.path.join(HERE, "prompts")) if f.endswith(".json"))
mods = allmods if arg.lower() == "all" else [m.strip() for m in arg.replace("、", ",").split(",") if m.strip()]
# MODごとの絵柄（2026-09-29）：絵柄割当.csv で絵柄を決めたMODは output\<MOD>_WAI_<絵柄>\ から集める
ASSIGN = {}
if model == "wai":
    sys.path.insert(0, HERE)
    try:
        import mod_style
        ASSIGN = {k: v for k, v in mod_style.read_csv().items() if v not in ("本編", "標準", "none")}
    except Exception as ex:
        print("(絵柄割当.csv が読めないので <MOD>_WAI から集めます:", ex, ")")
for mod in mods:
    src = os.path.join(OUT, mod + SUFFIX + (("_" + ASSIGN[mod]) if mod in ASSIGN else ""))
    if mod in ASSIGN:
        print("%s: 絵柄 %s（%s）" % (mod, ASSIGN[mod], os.path.basename(src)))
    if not os.path.isdir(src):
        if arg.lower() != "all":
            print("%s: まだ画像がありません（%s）" % (mod, src))
        continue
    dst = os.path.join(HERE, "完成", mod)
    os.makedirs(dst, exist_ok=True)
    best = {}
    for f in os.listdir(src):
        m = re.match(r"(.+?)_\d{5}_\.png$", f)
        if not m: continue
        p = os.path.join(src, f)
        if m.group(1) not in best or os.path.getmtime(p) > os.path.getmtime(best[m.group(1)]):
            best[m.group(1)] = p
    for n, p in sorted(best.items()):
        shutil.copy2(p, os.path.join(dst, n + ".png"))
    print("%s: %d 枚を %s にコピーしました" % (mod, len(best), dst))
