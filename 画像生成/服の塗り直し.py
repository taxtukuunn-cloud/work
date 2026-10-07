# -*- coding: utf-8 -*-
"""女装の場面：撮った絵の「主人公の服のところ」だけを、設定の衣装で塗り直す（2026-10-03・試作）
流れ：
  1) 撮った絵から人を切り分け（yolov8x-seg）、顔を見つけて男女を判定（人物の範囲を作るのと同じ方法）
     → 主人公の体の範囲（頭と相手の体を除く）を作る
  2) その範囲だけを ComfyUI で描き直す（同じモデル・同じ絵柄LoRA。文は主人公の衣装だけ）
  3) output\\<保存先>\\ に、範囲の確認用の絵（_範囲.jpg：赤＝塗り直す所）と、塗り直した絵を保存
使い方： python 服の塗り直し.py --out 確認18_塗り直し --denoise 0.7,0.85  MOD:画像名:元の絵のパス ...
"""
import os, sys, json, re, time, argparse, shutil, urllib.request, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import numpy as np
from PIL import Image, ImageFilter

HOME = os.path.expanduser("~")
COMFY = os.path.join(HOME, "Downloads", "ComfyUI_windows_portable", "ComfyUI")
INPUT, OUTPUT = os.path.join(COMFY, "input"), os.path.join(COMFY, "output")
LORA_DIR = os.path.join(COMFY, "models", "loras")
SERVER = "http://127.0.0.1:8188"
SEG_MODEL = os.path.join(HERE, "yolov8x-seg.pt")


def post(path, data):
    req = urllib.request.Request(SERVER + path, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def get(path):
    with urllib.request.urlopen(SERVER + path, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


CS = {}


def clipseg_heat(img, prompts):
    """文で場所を探す（CLIPSeg）。各文について 0〜1 の地図（H×W）を返す"""
    import torch
    if not CS:
        from transformers import CLIPSegProcessor, CLIPSegForImageSegmentation
        CS["dev"] = "cuda" if torch.cuda.is_available() else "cpu"
        CS["proc"] = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
        CS["model"] = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined").to(CS["dev"]).eval()
    W, H = img.size
    inp = CS["proc"](text=prompts, images=[img] * len(prompts), padding=True, return_tensors="pt").to(CS["dev"])
    with torch.no_grad():
        lg = CS["model"](**inp).logits
    if lg.dim() == 2:
        lg = lg[None]
    hm = torch.sigmoid(torch.nn.functional.interpolate(lg[:, None].float(), size=(H, W), mode="bilinear", align_corners=False))[:, 0]
    return hm.cpu().numpy()


def hero_mask(img, seg, det, clf, RM):
    """(塗り直す範囲 bool配列 か None, 説明)
    1) 人の切り分け（yolov8x-seg）で2人に分かれ、顔で主人公を決められれば、それを使う（正確）
    2) だめなら CLIPSeg で「男／女」の場所を探し、男のほうが強い所を主人公の体とする（おおまか）"""
    W, H = img.size
    yy, xx = np.mgrid[0:H, 0:W]
    fb = RM.faces(det, img)
    sc = [RM.maleness(clf, img, b) for b in fb]
    def ell(b, k=1.0, up=0.15):
        x0, y0, x1, y1 = b
        cx, cy, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2 - (y1 - y0) * up, (x1 - x0) * 0.95 * k, (y1 - y0) * 1.05 * k
        return ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
    def inside(m, b):
        cx, cy = int((b[0] + b[2]) / 2), int((b[1] + b[3]) / 2)
        return bool(m[min(H - 1, max(0, cy)), min(W - 1, max(0, cx))])
    r = seg(img, classes=[0], conf=0.25, retina_masks=True, verbose=False)[0]
    ms = [] if r.masks is None else [m > 0.5 for m in r.masks.data.cpu().numpy()]
    ms = [m for m in ms if m.sum() > W * H * 0.02]
    info = "人%d・顔%d・男らしさ %s" % (len(ms), len(fb), " / ".join("%.2f" % s for s in sc) or "-")
    # --- 1) 切り分けで決める
    hero_face = None
    if len(fb) >= 2:
        k = max(range(len(fb)), key=lambda i: sc[i])
        rest = sorted(sc[:k] + sc[k + 1:])
        if sc[k] >= 0.5 or sc[k] - rest[-1] >= 0.05:   # 2人のうち、より男らしいほうを主人公に
            hero_face = fb[k]
    elif len(fb) == 1 and sc[0] >= 0.5:
        hero_face = fb[0]
    partner_faces = [b for b in fb if b is not hero_face]
    if len(ms) >= 2:
        hero = None
        if hero_face is not None:
            c = [m for m in ms if inside(m, hero_face)]
            if c:
                hero = min(c, key=lambda m: m.sum())
        if hero is None and partner_faces:
            c = [m for m in ms if not any(inside(m, b) for b in partner_faces)]
            if c:
                hero = max(c, key=lambda m: m.sum())
        if hero is not None:
            out = hero.copy()
            for m in ms:
                if m is not hero:
                    out &= ~m
            if hero_face is not None:
                out &= ~ell(hero_face)
            if out.sum() >= W * H * 0.01:
                return out, info + "（切り分けで決定）"
    # --- 2) CLIPSeg
    hm = clipseg_heat(img, ["a man", "a man's body and clothes", "a woman", "a woman's body and dress"])
    man, wom = np.maximum(hm[0], hm[1]), np.maximum(hm[2], hm[3])
    man, wom = man / max(man.max(), 1e-6), wom / max(wom.max(), 1e-6)
    out = (man > 0.25) & (man > wom)
    try:   # 服の下のほう（ズボンなど）まで届くよう少し広げ、相手がはっきり強い所は戻す
        from scipy import ndimage
        out = ndimage.binary_dilation(out, iterations=max(6, int(min(W, H) * 0.03))) & ~((wom > man) & (wom > 0.45))
    except Exception:
        pass
    if hero_face is None and fb:   # 顔の所の「男」の強さで主人公の顔を決める
        def fs(b):
            x0, y0, x1, y1 = [int(v) for v in b]
            return float((man[y0:y1, x0:x1] - wom[y0:y1, x0:x1]).mean())
        k = max(range(len(fb)), key=lambda i: fs(fb[i]))
        if fs(fb[k]) > 0:
            hero_face = fb[k]
            partner_faces = [b for b in fb if b is not hero_face]
    if hero_face is not None:
        out &= ~ell(hero_face)
    for b in partner_faces:   # 相手の顔と髪は守る
        out &= ~ell(b, 1.5, 0.25)
    if out.sum() < W * H * 0.01:
        return None, info + "・CLIPSeg でも主人公の体が見つからない"
    return out, info + "（CLIPSeg で決定）"


def outfit_of(gen, pos):
    o = gen._hero_outfit(pos)
    for rx, b in gen.SAFETY.get("_subs", []):
        o = rx.sub(b, o)
    o = re.sub(r"^only\s+", "", re.sub(r"^[^,:]{0,40}:\s*", "", o))
    o = re.sub(r"\b(?:on|over) his flat chest\b", "", o)
    return re.sub(r"\s{2,}", " ", o).strip(" ,")


def workflow(M, style, src, mask, pos, neg, seed, denoise, prefix, depth=None, dstr=0.0, dend=0.8):
    w = {"3": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": M["ckpt_name"]}}}
    mo, co = ["3", 0], ["3", 1]
    if style and style.get("lora") and os.path.isfile(os.path.join(LORA_DIR, style["lora"])):
        w["30"] = {"class_type": "LoraLoader", "inputs": {"model": mo, "clip": co, "lora_name": style["lora"],
                   "strength_model": float(style.get("strength", 0.6)), "strength_clip": float(style.get("strength", 0.6))}}
        mo, co = ["30", 0], ["30", 1]
    w["4"] = {"class_type": "CLIPSetLastLayer", "inputs": {"clip": co, "stop_at_clip_layer": int(M.get("clip_skip", -2))}}
    w["6"] = {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 0], "text": pos}}
    w["7"] = {"class_type": "CLIPTextEncode", "inputs": {"clip": ["4", 0], "text": neg}}
    w["40"] = {"class_type": "LoadImage", "inputs": {"image": src}}
    w["41"] = {"class_type": "LoadImage", "inputs": {"image": mask}}
    w["42"] = {"class_type": "ImageToMask", "inputs": {"image": ["41", 0], "channel": "red"}}
    w["43"] = {"class_type": "VAEEncode", "inputs": {"pixels": ["40", 0], "vae": ["3", 2]}}
    w["44"] = {"class_type": "SetLatentNoiseMask", "inputs": {"samples": ["43", 0], "mask": ["42", 0]}}
    cp, cn_ = ["6", 0], ["7", 0]
    if depth and dstr > 0:   # 2026-10-03 体の形を保つ：元の絵の奥行きを下書きにして塗り直す（強く塗ると体が消えた対策）
        w["70"] = {"class_type": "ControlNetLoader", "inputs": {"control_net_name": "xinsir_union_sdxl_promax.safetensors"}}
        w["73"] = {"class_type": "SetUnionControlNetType", "inputs": {"control_net": ["70", 0], "type": "depth"}}
        w["71"] = {"class_type": "LoadImage", "inputs": {"image": depth}}
        w["72"] = {"class_type": "ControlNetApplyAdvanced", "inputs": {"positive": cp, "negative": cn_, "control_net": ["73", 0],
                   "image": ["71", 0], "strength": float(dstr), "start_percent": 0.0, "end_percent": float(dend)}}
        cp, cn_ = ["72", 0], ["72", 1]
    w["9"] = {"class_type": "KSampler", "inputs": {"model": mo, "positive": cp, "negative": cn_, "latent_image": ["44", 0],
              "seed": seed, "steps": int(M.get("steps", 28)), "cfg": float(M.get("cfg", 6.0)),
              "sampler_name": M.get("sampler", "euler_ancestral"), "scheduler": M.get("scheduler", "normal"), "denoise": float(denoise)}}
    w["10"] = {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 2]}}
    w["45"] = {"class_type": "ImageCompositeMasked", "inputs": {"destination": ["40", 0], "source": ["10", 0], "x": 0, "y": 0,
               "resize_source": False, "mask": ["42", 0]}}
    w["11"] = {"class_type": "SaveImage", "inputs": {"images": ["45", 0], "filename_prefix": prefix}}
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="確認18_塗り直し")
    ap.add_argument("--denoise", default="0.7,0.85")
    ap.add_argument("--depth", default="0", help="体の形を保つ強さ（0＝使わない。0.6,0.9 のように複数可）")
    ap.add_argument("--depth-end", type=float, default=0.8)
    ap.add_argument("items", nargs="+")
    a = ap.parse_args()
    try:
        get("/system_stats")
    except Exception as e:
        print("[中止] ComfyUI に接続できません（起動していますか？）:", e); return
    import torch
    from ultralytics import YOLO
    from transformers import pipeline
    import make_region_masks as RM
    import gen
    import mod_style as MS
    dev = 0 if torch.cuda.is_available() else -1
    seg, det = YOLO(SEG_MODEL), YOLO(RM.FACE_MODEL)
    clf = pipeline("zero-shot-image-classification", model=RM.CLIPS["large"], device=dev)
    M = gen.MODELS["wai"]
    dstrs = [float(x) for x in a.depth.split(",") if x.strip()]
    dpipe = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Small-hf", device=dev) if any(x > 0 for x in dstrs) else None
    cfg_all = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    styles = (cfg_all.get("mod_style") or {}).get("styles") or {}
    assign = MS.read_csv()
    odir = os.path.join(OUTPUT, a.out)
    os.makedirs(odir, exist_ok=True)
    ids = []
    for it in a.items:
      try:
          mod, name, path = it.split(":", 2)
          if not os.path.isabs(path):
              path = os.path.join(OUTPUT, path)
          if not os.path.exists(path):
              print("  [なし] %s" % path); continue
          P = json.load(open(os.path.join(HERE, "prompts", mod + ".json"), encoding="utf-8"))
          pos0 = P[name]["positive"]
          outfit = outfit_of(gen, pos0)
          img = Image.open(path).convert("RGB")
          m, why = hero_mask(img, seg, det, clf, RM)
          print("■ %s  %s  衣装: %s" % (name, why, outfit or "（拾えない）"))
          if m is None or not outfit:
              print("   → 飛ばす"); continue
          mk = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.MaxFilter(17)).filter(ImageFilter.GaussianBlur(6))
          ov = np.array(img).astype("float32"); wv = np.array(mk).astype("float32")[..., None] / 255 * 0.5
          Image.fromarray((ov * (1 - wv) + np.array([255, 30, 30], "float32") * wv).clip(0, 255).astype("uint8")).save(
              os.path.join(odir, "%s_範囲.jpg" % name), quality=88)
          src_n, mask_n = "cloth_src_%s.png" % name, "cloth_mask_%s.png" % name
          img.save(os.path.join(INPUT, src_n)); mk.convert("RGB").save(os.path.join(INPUT, mask_n))
          dep_n = None
          if dpipe is not None:
              dd = dpipe(img)["predicted_depth"].squeeze().float().cpu().numpy()
              lo, hi = np.percentile(dd, 1), np.percentile(dd, 99)
              dd = ((dd - lo) / max(hi - lo, 1e-6)).clip(0, 1)
              dep_n = "cloth_depth_%s.png" % name
              dimg = Image.fromarray((dd * 255).astype("uint8")).resize(img.size, Image.BICUBIC).filter(ImageFilter.GaussianBlur(2)).convert("RGB")
              dimg.save(os.path.join(INPUT, dep_n)); dimg.save(os.path.join(odir, "%s_奥行き.jpg" % name), quality=85)
          st = styles.get(assign.get(mod, ""), {})
          trig = (st.get("trigger") or "").strip()
          pos = ", ".join(x for x in [trig, M.get("quality_pos", "masterpiece, best quality"),
                 # 2026-10-03 「男」と書くと男物の服に戻る（v2）。塗り直す範囲は服だけなので、服を着た細い体として書く
                 "1girl, solo, slender, flat chest, (%s:1.3)" % outfit, "fully clothed, detailed clothes, cute outfit"] if x)
          neg = ", ".join([M.get("quality_neg", "worst quality"), "breasts, large breasts, medium breasts, cleavage, t-shirt, shirt, necktie, business suit, jacket, "
                 "trousers, pants, jeans, male clothes, casual clothes, naked, nude, topless, nipples, child, text, watermark, extra arms, extra hands, face, head"])
          seed = int(hashlib.md5(("cloth-" + name).encode()).hexdigest(), 16) % (2 ** 31 - 1)
          for d in [float(x) for x in a.denoise.split(",") if x.strip()]:
            for ds in dstrs:
              w = workflow(M, st, src_n, mask_n, pos, neg, seed, d, "%s/%s_d%02d_k%02d" % (a.out, name, round(d * 100), round(ds * 100)),
                           dep_n, ds, a.depth_end)
              try:
                  ids.append(post("/prompt", {"prompt": w})["prompt_id"])
              except urllib.error.HTTPError as e:
                  print("   [送れない] %s" % e.read().decode("utf-8", "replace")[:600]); break
      except Exception:
          import traceback; traceback.print_exc(); print("   → この絵は飛ばす")
    print("送った数: %d。ComfyUI が描き終わるのを待ちます…" % len(ids))
    t0 = time.time()
    while ids and time.time() - t0 < 1800:
        ids = [i for i in ids if i not in get("/history/" + i)]
        time.sleep(3)
    print("終わりました。保存先: %s" % odir)


if __name__ == "__main__":
    main()
