# -*- coding: utf-8 -*-
"""敵キャラLoRA用の学習画像を「1枚目の見本」から撮る（2026-10-05・ユーザー決定 案1）
  1. --first : そのキャラの1枚目の候補を撮る。ダウンロードしたキャラLoRA（model.json chara_map）＋そのMODの絵柄LoRA。
               ダウンロードしたキャラLoRAが無いキャラは絵柄LoRAだけ。
               → ComfyUI\\output\\chara_ref\\<MOD>_<キャラ>_<絵柄>\\first_00001_.png …
     まとめツール ⑤ の画面で1枚選ぶと ComfyUI\\input\\chara_ref_<MOD>_<キャラ>_<絵柄>.png に写される（＝見本）。
  2. （既定）: 見本を IP-Adapter で参考にさせながら、絵柄LoRAだけで 16構図 × 2枚 撮る（キャラLoRAは使わない）。
               → ComfyUI\\output\\chara_ds\\<MOD>_<キャラ>_<絵柄>\\<構図>_00001_.png（make_chara_ds.py と同じ置き場所・名前。
               prep_chara.py・train_chara.py はそのまま使える）
make_chara_ds.py は書き換えず、プロンプトの作り方・構図・背景をそのまま借りる。
使い方: python make_chara_ds_ref.py <MODコード> [--chars master,e1] [--first] [--first-n 4] [--ref-weight 0.6] [--batch 2] [--dry-run]"""
import argparse, hashlib, json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import make_chara_ds as K
gen, MS = K.gen, K.MS

COMFY = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI")
REF_OUT = "chara_ref"
FIRST_POSE = ("full body, standing, front view, looking at viewer", "simple background, white background")
REF_END = 0.8
# 参考画像を使うと光のにじみ・きらめきが出やすい（gen.py の衣装の参考と同じ対策）
GLOW_NEG = "glowing clothes, glowing body, glow, light particles, sparkles, bloom, lens flare, neon colors, oversaturated"


def ref_file(tag):
    return "chara_ref_%s.png" % tag


def build(pos, neg, seed, batch, prefix, extra=None, ref=None, ref_weight=0.6):
    """make_chara_ds.workflow と同じ組み立てに、extra（キャラLoRA）と ref（見本の IP-Adapter）を足したもの"""
    gen.CUR_TEXT = "chara dataset"
    gen.CUR_SCENE = False
    gen.CUR_CHARA = None
    loras = [L for L in gen.sdxl_loras() if L.get("role") not in ("hero", "chara", "chara_own")] + list(extra or [])
    trig = ", ".join(L["trigger"] for L in (extra or []) if L.get("trigger"))
    if trig:
        pos = trig + ", " + pos
    if ref:
        neg = neg.rstrip(", ") + ", " + GLOW_NEG
    pos, neg = gen.adapt_prompt(pos, neg)
    M = gen.MODEL
    w = {"3": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": M["ckpt_name"]}}}
    m, c = ["3", 0], ["3", 1]
    for i, L in enumerate(loras):
        nid = str(30 + i)
        w[nid] = {"class_type": "LoraLoader", "inputs": {"model": m, "clip": c, "lora_name": L["lora_name"],
                  "strength_model": float(L["strength"]), "strength_clip": float(L.get("clip_strength", L["strength"]))}}
        m, c = [nid, 0], [nid, 1]
    names = ["%s@%s" % (L["lora_name"], L["strength"]) for L in loras]
    if ref:
        w["95"] = {"class_type": "IPAdapterModelLoader", "inputs": {"ipadapter_file": gen.IPA_MODEL}}
        w["96"] = {"class_type": "CLIPVisionLoader", "inputs": {"clip_name": gen.IPA_CLIPV}}
        w["97"] = {"class_type": "LoadImage", "inputs": {"image": ref}}
        w["99"] = {"class_type": "IPAdapterAdvanced", "inputs": {
            "model": m, "ipadapter": ["95", 0], "image": ["97", 0], "weight": float(ref_weight),
            "weight_type": "linear", "combine_embeds": "concat", "start_at": 0.0, "end_at": REF_END,
            "embeds_scaling": "V only", "clip_vision": ["96", 0]}}
        m = ["99", 0]
        names.append("見本 %s@%s" % (ref, ref_weight))
    w.update({
     "4": {"class_type": "CLIPSetLastLayer", "inputs": {"clip": c, "stop_at_clip_layer": int(M.get("clip_skip", -2))}},
     "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["4", 0]}},
     "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 0]}},
     "8": {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": batch}},
     "9": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": int(M["steps"]), "cfg": float(M["cfg"]),
           "sampler_name": M["sampler"], "scheduler": M["scheduler"], "denoise": 1.0,
           "model": m, "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0]}},
     "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 2]}},
     "11": {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": prefix}},
    })
    if hasattr(gen, "face_detail_on") and gen.face_detail_on():
        w["11"]["inputs"]["images"] = gen.add_face_detail(w, ["10", 0], m, ["4", 0], ["3", 2], ["6", 0], ["7", 0], seed, M)
        names.append("顔描き直し@%s" % gen.FACE_DETAIL["denoise"])
    return w, names, pos


def done_count(d, pk):
    """その構図の撮り済みの枚数（外した絵 _外した も数える）"""
    rx = re.compile(r"^%s_\d{5}_\.png$" % re.escape(pk))
    n = 0
    for x in (d, os.path.join(d, "_外した")):
        try:
            n += sum(1 for f in os.listdir(x) if rx.match(f))
        except OSError:
            pass
    return n


def downloaded_lora(mod, c, st):
    """1枚目に使うダウンロードしたキャラLoRA（chara_map）。無い・ファイルが無いなら None"""
    # chara_lora は自作ができると自作を返す（自作に切り替え）ので、ここでは chara_map のダウンロードしたものを直接使う
    e = MS.chara_map_entry(mod, c)
    if not e:
        return None
    f = e["lora"]
    if not os.path.isfile(os.path.join(MS.LORA_DIR, *re.split(r"[\\/]", f))):
        return None
    st = float(e.get("strength", MS.cfg().get("chara_map_strength", 0.8)))
    return {"lora_name": f, "strength": st, "clip_strength": st, "trigger": e.get("trigger", "")}


def send(w):
    req = urllib.request.Request(K.SERVER + "/prompt", data=json.dumps({"prompt": w}).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=30)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mod")
    ap.add_argument("--chars", default=",".join(MS.CHARS))
    ap.add_argument("--first", action="store_true", help="1枚目の候補を撮る（キャラLoRA＋絵柄LoRA）")
    ap.add_argument("--first-n", type=int, default=4)
    ap.add_argument("--ref-weight", type=float, default=0.6, help="見本の効き（0.4〜0.8。上げると似るが構図も見本に寄る）")
    ap.add_argument("--batch", type=int, default=2)
    ap.add_argument("--style")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-face-detail", action="store_true")
    ap.add_argument("--out", help="試し撮り：保存先を ComfyUI\\output\\<これ>\\<タグ>\\ にする（学習用の置き場所に混ぜない）")
    ap.add_argument("--ref-file", help="試し撮り：見本を ComfyUI\\input の この絵にする（選んだ見本を変えない）")
    ap.add_argument("--poses", help="撮る構図を絞る（例 front_full,side,sitting）")
    ap.add_argument("--skip-done", action="store_true", help="撮り済みは飛ばす（まとめて撮るとき。途中で止めても続きから撮れる。外した絵も撮り済みに数える）")
    a = ap.parse_args()
    poses = [p for p in K.POSES if not a.poses or p[0] in a.poses.split(",")]
    gen.MODEL = gen.load_model("wai")
    if hasattr(gen, "load_face_detail"):
        gen.load_face_detail()
        gen.NO_FACE_DETAIL = a.no_face_detail
        if gen.face_detail_on() and not a.dry_run:
            try:
                gen.FD_OK = bool(gen.get_json("/object_info/FaceDetailer"))
            except Exception:
                gen.FD_OK = False
    P = json.load(open(os.path.join(K.GEN_DIR, "prompts", a.mod + ".json"), encoding="utf-8"))
    P = MS.apply_chara_map(a.mod, P)   # ダウンロードしたキャラLoRAに合わせた見た目の文字（gen.py と同じ）
    st = K.resolve_style(a.mod, a.style)
    sname = st["name"] if st else "std"
    chars = [c.strip() for c in a.chars.split(",") if c.strip()]
    todo = []   # (キャラ, key, 保存先, pos, neg, seed, batch, extra, ref)
    for c in chars:
        key = "%s_%s" % (a.mod, c)
        tag = "%s_%s_%s" % (a.mod, c, sname)
        if key not in P:
            print("  %s: 立ち絵のプロンプト %s が無いので飛ばします" % (c, key)); continue
        neg = P[key]["negative"] + ", " + K.NEG_ADD
        if a.first:
            if a.skip_done and done_count(os.path.join(COMFY, "output", a.out or REF_OUT, tag), "first") >= a.first_n:
                print("  %s: 1枚目の候補は撮り済みなので飛ばします" % c); continue
            dl = downloaded_lora(a.mod, c, st)
            print("  %s: 1枚目の候補 %d 枚（%s）" % (c, a.first_n, "キャラLoRA " + dl["lora_name"] + " ＋絵柄LoRA" if dl else "ダウンロードしたキャラLoRAが無いので絵柄LoRAだけ"))
            for i in range(a.first_n):
                seed = int(hashlib.md5(("chara-first-%s-%d" % (key, i)).encode()).hexdigest(), 16) % (2**31 - 1)
                todo.append((c, key, "%s/%s/first" % (a.out or REF_OUT, tag), K.prompt(P[key], *FIRST_POSE), neg, seed, 1, [dl] if dl else [], None))
            continue
        rf = a.ref_file or ref_file(tag)
        if not os.path.isfile(os.path.join(COMFY, "input", rf)):
            print("  %s: 見本（ComfyUI\\input\\%s）がまだ無いので飛ばします。先に1枚目を選んでください" % (c, rf)); continue
        old = os.path.join(COMFY, "output", a.out or K.OUT, tag)
        if not a.out and not a.skip_done and os.path.isdir(old) and any(f.endswith(".png") for f in os.listdir(old)):
            print("  %s: 前に撮った学習用の絵が %s に残っています（混ざります。要らなければ画面で外してください）" % (c, old))
        for pk, pt in poses:
            i = [p[0] for p in K.POSES].index(pk)
            if a.skip_done and done_count(old, pk) >= a.batch:
                continue
            seed = int(hashlib.md5(("chara-ref-%s-%s" % (key, pk)).encode()).hexdigest(), 16) % (2**31 - 1)
            todo.append((c, key, "%s/%s/%s" % (a.out or K.OUT, tag, pk), K.prompt(P[key], pt, K.BGS[i % len(K.BGS)]), neg, seed, a.batch, [], rf))
    n_img = sum(t[6] for t in todo)
    print("%s: %s  絵柄 %s  %d 枚" % ("1枚目の候補" if a.first else "見本から学習用の絵", a.mod, sname, n_img))
    if not todo:
        return
    t = todo[0]
    w, names, pos = build(t[3], t[4], 1, t[6], "x", t[7], t[8], a.ref_weight)
    print("使うもの:", ", ".join(names))
    print("例（%s）: %s ..." % (t[0], pos[:260]))
    if a.dry_run:
        return
    for i, (c, key, prefix, pos, neg, seed, batch, extra, ref) in enumerate(todo, 1):
        while gen.queue_count() >= 4:
            time.sleep(3)
        w, _, _ = build(pos, neg, seed, batch, prefix, extra, ref, a.ref_weight)
        try:
            send(w)
            print(" [%d/%d] %s %s" % (i, len(todo), c, prefix.split("/")[-1]))
        except urllib.error.HTTPError as ex:
            print(" [エラー]", c, prefix, ex, ex.read().decode("utf-8", "replace")[:400]); sys.exit(1)
        time.sleep(0.2)
    print("すべて送信しました。")


if __name__ == "__main__":
    main()
