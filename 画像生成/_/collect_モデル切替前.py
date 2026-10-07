# -*- coding: utf-8 -*-
"""自作した画像を、ゲームで使う名前（例 Host_atk_m1.png）にそろえて 画像生成\完成\<MODコード>\ にコピーする。
使い方: python collect.py <MODコード|all|コード,コード,...>
同じ名前が複数あれば一番新しいものを使う。気に入らない画像は ComfyUI の出力フォルダから先に消しておくこと。"""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "output")
arg = sys.argv[1] if len(sys.argv) > 1 else "all"
allmods = sorted(f[:-5] for f in os.listdir(os.path.join(HERE, "prompts")) if f.endswith(".json"))
mods = allmods if arg.lower() == "all" else [m.strip() for m in arg.replace("、", ",").split(",") if m.strip()]
for mod in mods:
    src = os.path.join(OUT, mod + "_自作")
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
