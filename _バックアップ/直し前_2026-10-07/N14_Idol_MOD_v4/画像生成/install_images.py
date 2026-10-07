# -*- coding: utf-8 -*-
"""
ComfyUI の output にできた画像を、カードが参照する名前でゲームの Picture/<MOD>/ にコピーする。

  python install_images.py <MODコード> "<ゲームのPictureフォルダ>" [--output "<ComfyUIのoutput>"] [--overwrite]

- ComfyUI は保存名の末尾に _00001_ を付けるので、それを外して <MOD>_<キー>.png にする。
- 同じキーの画像が複数あれば、一番新しいもの（更新日時）を使う。
- 背景除去版（_rmbg）があれば立ち絵はそちらを優先する。
- 既にある画像は --overwrite を付けない限り上書きしない。
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT = r"C:\Users\taku2\Downloads\ComfyUI_windows_portable\ComfyUI\output"


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    mod, picture = args[0], args[1]
    out_dir = DEFAULT_OUTPUT
    if "--output" in args:
        out_dir = args[args.index("--output") + 1]
    overwrite = "--overwrite" in args
    prompts = json.load(open(os.path.join(HERE, "prompts", f"{mod}_prompts.json"), encoding="utf-8"))
    dest = os.path.join(picture, mod)
    os.makedirs(dest, exist_ok=True)

    found = {}
    for fn in os.listdir(out_dir):
        m = re.match(r"(.+?)(_rmbg)?_\d{5}_?\.png$", fn)
        if not m:
            continue
        base, rmbg = m.group(1), bool(m.group(2))
        full = os.path.join(out_dir, fn)
        score = (rmbg, os.path.getmtime(full))
        if base not in found or score > found[base][0]:
            found[base] = (score, full)

    done, skipped, missing = 0, 0, []
    for key, v in prompts.items():
        target = v["file"]
        base = target.rsplit(".", 1)[0]
        if base not in found:
            missing.append(target)
            continue
        to = os.path.join(dest, target)
        if os.path.exists(to) and not overwrite:
            skipped += 1
            continue
        shutil.copy2(found[base][1], to)
        done += 1
        print(f"  {os.path.basename(found[base][1])} -> {mod}\\{target}")
    print(f"\nコピー {done} 枚 / 既にあるので飛ばした {skipped} 枚（--overwrite で上書き）")
    if missing:
        print(f"まだ生成されていない画像 {len(missing)} 枚:")
        for t in missing:
            print("  ", t)


if __name__ == "__main__":
    main()
