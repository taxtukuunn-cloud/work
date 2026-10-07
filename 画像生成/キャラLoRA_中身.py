# -*- coding: utf-8 -*-
"""loras\\キャラ の LoRA の中身（元モデル・予測方式・トリガー候補・学習タグ・年齢に関わるタグ）を
画像生成\\キャラLoRA_中身.txt にまとめて書く（2026-10-02）。LoRA は読むだけで変更しない。
使い方: python キャラLoRA_中身.py [ファイル名…]（省略時は loras\\キャラ の全部。chr_ で始まる自作LoRAは除く）。txt に既にあるLoRAは飛ばして末尾に追記"""
import collections, json, os, re, struct, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras", "キャラ")
AGE = re.compile(r"\b(loli|shota|child|children|kid|toddler|aged down|teen|teenage|onee-shota|oppai loli|young|petite|flat chest|school uniform|serafuku|elementary|middle school|high school)\b", re.I)
COMMON = {"1girl", "solo", "breasts", "looking at viewer", "blush", "smile", "simple background", "white background",
          "long hair", "large breasts", "open mouth", "bangs", "upper body", "cowboy shot", "standing", "full body"}


def one(fn):
    p = os.path.join(CDIR, fn)
    out = ["===== " + fn]
    with open(p, "rb") as f:
        n = struct.unpack("<Q", f.read(8))[0]
        h = json.loads(f.read(n))
    m = h.get("__metadata__") or {}
    keys = [k for k in h if k != "__metadata__"]
    xl = any("lora_unet_input_blocks_4_1_transformer_blocks_1" in k or "lora_te2_" in k for k in keys)
    out.append("  形式: %s / %s / %s" % ("SDXL" if xl else "SD1.5かも", m.get("modelspec.prediction_type", "?"),
                                       ("v予測" if str(m.get("ss_v_parameterization", "")).lower() == "true" else "-")))
    for k in ("ss_sd_model_name", "modelspec.trigger_phrase", "ss_output_name", "modelspec.title"):
        if m.get(k) and m.get(k) != "None":
            out.append("  %s = %s" % (k, str(m[k])[:150]))
    dirs = json.loads(m.get("ss_dataset_dirs") or "{}")
    if dirs:
        out.append("  学習フォルダ: " + ", ".join("%s(%s枚)" % (d, v.get("img_count", "?")) for d, v in dirs.items()))
    tf = m.get("ss_tag_frequency")
    if not tf:
        out.append("  学習タグの記録なし（メタデータなし）")
        return "\n".join(out)
    tot = collections.Counter()
    for c in json.loads(tf).values():
        tot.update(c)
    mx = max(tot.values()) if tot else 1
    trig = [t for t, c in tot.most_common(8) if c >= 0.6 * mx and t not in COMMON]
    out.append("  トリガー候補: " + ", ".join(trig))
    out.append("  よく出るタグ: " + ", ".join("%s %d" % x for x in tot.most_common(35)))
    ag = sorted(((t, c) for t, c in tot.items() if AGE.search(t)), key=lambda x: -x[1])
    out.append("  年齢に関わるタグ: " + (", ".join("%s %d" % x for x in ag[:15]) if ag else "なし"))
    return "\n".join(out)


def main():
    """2026-10-02 ユーザー要望：すでに書いてある分（===== ファイル名 の段）は書き換えない。まだ無いLoRAだけ調べて末尾に足す"""
    out = os.path.join(HERE, "キャラLoRA_中身.txt")
    done = set()
    if os.path.isfile(out):
        for line in open(out, encoding="utf-8"):
            if line.startswith("===== "):
                done.add(line[6:].split("  読めません")[0].strip())
    fs = sys.argv[1:] or sorted(f for f in os.listdir(CDIR) if f.endswith(".safetensors") and not f.startswith("chr_"))
    fs = [f for f in fs if f not in done]
    if not fs:
        print("新しいLoRAはありません（キャラLoRA_中身.txt はそのまま）")
        return
    res = []
    for f in fs:
        try:
            res.append(one(f))
        except Exception as ex:
            res.append("===== %s  読めません: %s" % (f, ex))
        print(res[-1].splitlines()[0])
    with open(out, "a", encoding="utf-8") as fo:   # 追記だけ（既存の行は触らない）
        fo.write("\n".join(res) + "\n")
    print("\n新しい %d個を キャラLoRA_中身.txt の末尾に足しました（前からある分はそのまま。Claude が読みます）" % len(res))


main()
