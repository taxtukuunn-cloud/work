# -*- coding: utf-8 -*-
"""loras\\絵柄 の LoRA の中身（元モデル・予測方式・トリガー候補・学習タグ・年齢に関わるタグ）を
画像生成\\絵柄LoRA_追加分の中身.txt に書く（2026-10-02）。LoRA は読むだけで変更しない。
使い方: python 絵柄LoRA_中身.py [ファイル名…]（省略時は model.json の styles で memo に「トリガー未確認」とあるもの）"""
import collections, json, os, re, struct, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LDIR = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras")
AGE = re.compile(r"\b(loli|shota|child|children|kid|toddler|aged down|teen|teenage|onee-shota|oppai loli|male child|female child|young boy|young girl|petite)\b", re.I)


def one(name, p):
    out = ["===== %s  (%s)" % (name, os.path.basename(p))]
    with open(p, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        h = json.loads(f.read(n))
    m = h.get("__metadata__") or {}
    for k in ("ss_base_model_version", "ss_sd_model_name", "modelspec.prediction_type", "ss_v_parameterization",
              "ss_network_module", "modelspec.trigger_phrase", "ss_output_name"):
        if k in m:
            out.append("  %s = %s" % (k, str(m[k])[:150]))
    dirs = json.loads(m.get("ss_dataset_dirs") or "{}")
    if dirs:
        out.append("  学習フォルダ: " + ", ".join("%s(%s枚)" % (d, v.get("img_count", "?")) for d, v in dirs.items()))
    tf = m.get("ss_tag_frequency")
    if not tf:
        out.append("  学習タグの記録なし（メタデータなし）")
    else:
        tot = collections.Counter()
        for c in json.loads(tf).values():
            tot.update(c)
        out.append("  よく出るタグ: " + ", ".join("%s %d" % x for x in tot.most_common(25)))
        ag = sorted(((t, c) for t, c in tot.items() if AGE.search(t)), key=lambda x: -x[1])
        out.append("  年齢に関わるタグ: " + (", ".join("%s %d" % x for x in ag) if ag else "なし"))
        for t in ("1boy", "1girl", "monochrome", "greyscale", "3d", "realistic"):
            if t in tot:
                out.append("    %s %d" % (t, tot[t]))
    return "\n".join(out)


def main():
    mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    st = mj["mod_style"]["styles"]
    if sys.argv[1:]:
        todo = [(a, a if os.path.isabs(a) else os.path.join(LDIR, "絵柄", a)) for a in sys.argv[1:]]
    else:
        todo = [(k, os.path.join(LDIR, v["lora"])) for k, v in st.items() if "トリガー未確認" in v.get("memo", "")]
    res = []
    for k, p in todo:
        try:
            res.append(one(k, p))
        except Exception as ex:
            res.append("===== %s  読めません: %s" % (k, ex))
        print(res[-1])
    with open(os.path.join(HERE, "絵柄LoRA_追加分の中身.txt"), "w", encoding="utf-8") as fo:
        fo.write("\n".join(res) + "\n")
    print("\n→ 絵柄LoRA_追加分の中身.txt に書きました（Claude が読みます）")


main()
