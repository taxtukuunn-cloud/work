# -*- coding: utf-8 -*-
"""構図LoRA（models\\loras\\構図\\*.safetensors）の中身（メタデータ＝学習の元モデル・学習タグ等）だけを取り出す（2026-09-30）
LoRA 本体は読まない（先頭のヘッダだけ）のですぐ終わる。LoRA ファイルは変更しない。
出力: このフォルダの 構図LoRA_中身\\<ファイル名>.json（Claude が一覧表を作るのに使う）
使い方: python 構図LoRA_中身.py [--all]   （既定は json がまだ無いものだけ）"""
import glob, json, os, struct, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras", "構図")
OUT = os.path.join(HERE, "構図LoRA_中身")
os.makedirs(OUT, exist_ok=True)
files = sorted(glob.glob(os.path.join(SRC, "*.safetensors")))
print("構図LoRA: %d 個（%s）" % (len(files), SRC))
n = 0
for p in files:
    name = os.path.basename(p)
    dst = os.path.join(OUT, name + ".json")
    if os.path.exists(dst) and "--all" not in sys.argv:
        continue
    try:
        with open(p, "rb") as f:
            k = struct.unpack("<Q", f.read(8))[0]
            h = json.loads(f.read(k))
        m = h.get("__metadata__") or {}
        keys = [x for x in h if x != "__metadata__"]
        m["_nkeys"] = len(keys)
        m["_sample_keys"] = keys[:5]
        m["_size"] = os.path.getsize(p)
        with open(dst, "w", encoding="utf-8") as fo:
            json.dump(m, fo, ensure_ascii=False)
        n += 1
        print("  書いた:", name)
    except Exception as ex:
        print("  読めません:", name, ex)
print("新しく書いた: %d 個 → %s" % (n, OUT))
