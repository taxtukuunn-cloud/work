# -*- coding: utf-8 -*-
"""まだ敵キャラに割り振っていないキャラLoRA の立ち絵を1枚ずつ撮る（2026-10-03・LoRA を増やしても使える版）
見た目を確かめて、どの敵に当てるか決めるためのもの。服を着た全身の立ち絵・白い背景。
・loras\\キャラ の *.safetensors のうち、model.json の mod_style.chara_map で使っていないものを自動で探す（model.json は読むだけ）
・足す語は LoRA の中の学習タグから自動で決める（記録が無い LoRA はファイル名から作る）。下の LORAS に書いたものはその語を優先
・SKIP に書いたもの（同じキャラの別版を使用中）・chr_ で始まる自作LoRA・もう撮ってあるものは飛ばす（--redo で撮り直す）
・学習タグに年齢に関わる語（loli・child など）がある LoRA は撮らずに名前だけ表示する
保存先: ComfyUI\\output\\キャラLoRA未割当\\<名前>_00001_.png
gen.py は読まない・変えない。ComfyUI（127.0.0.1:8188）に直接送る。--dry-run で送らずに一覧だけ表示。--all で割り振り済みも含めて全部。
名前の一部を書くと、その LoRA だけ撮り直す（例: 未割当キャラLoRAの立ち絵.bat Eclipse）"""
import collections, json, os, re, struct, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
COMFY = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI")
CDIR = os.path.join(COMFY, "models", "loras", "キャラ")
ODIR = os.path.join(COMFY, "output", "キャラLoRA未割当")
AGE = re.compile(r"\b(loli|shota|child|children|kid|toddler|aged down|oppai loli|elementary|middle school)\b", re.I)
COMMON = {"1girl", "solo", "breasts", "looking at viewer", "blush", "smile", "simple background", "white background", "long hair",
          "large breasts", "open mouth", "bangs", "upper body", "cowboy shot", "standing", "full body", "closed mouth", "sitting"}
# 同じキャラの別版がもう割り振られているので撮らないもの（拡張子なし）
SKIP = {"hakuhou_XL_illustrious-noob_v1", "hindenburg_IL_v1.0", "illustrious_XL_pony_v2", "plymouth_IL_v1.0", "SovetskySoyuzILSTCAMEq2v1.1 AL"}
URL = "http://127.0.0.1:8188"
CKPT = "waiIllustriousSDXL_v170.safetensors"
STRENGTH = 0.8
SEED = 20261003
POS = ("masterpiece, best quality, amazing quality, very aesthetic, absurdres, safe, solo, 1girl, %s, adult woman, mature female, "
       "mature face, adult proportions, tall, long legs, standing, full body, looking at viewer, simple background, white background")
NEG = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, logo, "
       "child, loli, shota, young, teenage, underage, petite, childlike, child body, baby face, short limbs, big head, chibi, "
       "1boy, 2girls, multiple girls, nude, nipples, nsfw, topless, realistic, photorealistic, 3d")
# 足す語を手で決めたもの（ここに無い LoRA は自動）。ファイル名（拡張子なし）: 足す語
LORAS = [
    ("_echidna_gbf-elesico-ilxl", "gbfechid, long hair, white hair, harem outfit, veil"),
    ("_europa_fgo-elesico-ilxl", "blonde hair, very long hair, purple eyes, crown, white dress"),
    ("argus_XL_illustrious-noob_v1", "argus (azur lane), military uniform"),
    ("BD2_Eclipse_nyraen_v2", "eclipsedef, blue eyes, long hair, black hair, colored inner hair, multicolored hair, blue hair, horns, broken horn, horn ornament, purple leotard, bare shoulders, frills, black gloves"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供）。衣装違い：eclipseNMB（バニー）・eclipseBV（水着）・eclipseBID（花嫁）
    ("BD2_Luvencia_nyraen_v2.5", "Luvencia-DS, blue eyes, short hair, black hair, multicolored hair, colored inner hair, blue hair, mole under eye, black choker, office_lady, black_jacket, white_shirt, black_gloves, black_skirt, black_thighhighs, black_high_heels"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供）。Luvencia＝素の姿／Luvencia-DS（事務員）／Luvencia-WD（紫の上着・左右で色の違う目）／Luvencia-OCV（防弾ベスト・headset）
    ("BD2_Nebris_nyraen_v2.5", "nebrisemployee, dark_skin, blue_eyes, long hair, bangs, ivory hair, multicolored_hair, green_streaked_hair, black_hairpin, white turtleneck, long sleeves, black_belt, black_skirt, black_thigh_boots, heels"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供）。nebris＝素の姿／nebrisdef（白いドレスと黒金の鎧・角・とがった耳・槍）／nebrisemployee（白いタートルネックの店員）／nebris-LLG・nebris-LBK（水着。LBK は nippleless clothes を含むので立ち絵には使わない）
    ("BD2_Wilhelmina_nyraen_v2.2", "wilhelmina-SL, blue eyes, hair over one eye, long hair, blonde hair, white sleeveless crop_top, gold buttons, white elbow gloves, blue bodysuit bottoms, black thigh high boots, heels, white spotted coat, coat on shoulders"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供）。wilhelmina＝素の姿／wilhelmina-SL（白い上着と肩にかけた白いコート）／wilhelmina-WQ（黒い帽子・青いエプロンドレス）／wilhelmina-FRZQ（白い衣装・青い毛皮の縁・銀の冠）
    ("BD2_Zenith_nyraen_v2.2", "Zenith-RH, purple eyes, orange hair, long hair, hair between eyes, green scarf hood, red feathers, white short sleeve, black highleg leotard, black fingerless elbow gloves, black waist belt, black thighhighs, yellow straps, green ankle heel boots"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供）。Zenith＝素の姿（ポニーテール）／Zenith-RH（緑のフードと赤い羽根の狩人）／Zenith-WG（白い水着と白い上着）／Zenith-SB（白いバニー。topless・groin cutout を含むので立ち絵には使わない）
    ("burnice_white_zzz_illustrious_goofy", "burnice white"),
    ("Darian_ilxl_v2", "Darian-YD, blue eyes, long wavy hair, white hair, hair flower, purple_military_uniform, asymmetry top, white layered top, epaulette, brooch, black gloves, black belt, pelvic curtain, white pantyhose, white high heels"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供・ブラウンダスト2）。Darian＝素の姿／Darian-YD（紫の軍服）／Darian-BSB（白いバニー。breast_cutout を含むので立ち絵には使わない）
    ("indomitable_(azur_lane)_2_il_3-000012", r"indomitable\(azur_lane\), horn, white_dress, cloak"),
    ("Lion_XL_illustrious-noob_v1", r"lion \(azur lane\), military uniform"),
    ("PittsburghILSTCAMEq2v1.2 AL", "star hair ornament, red eyes, purple hair, medium hair, side ponytail, white dress"),
    ("regensburg_illust_scarxzys", "regensburg (azur lane)"),
    ("roon_XL_illustrious_v1", r"roon \(azur lane\), military uniform"),
    ("Saja-19", "saja, black hair, yellow eyes, pointy ears, hair tubes"),
    ("Sylvia_ilxl_v2", "Sylviamarine, long hair, drill hair, pink hair, hair over one eye, blue eyes, peaked_cap, white headwear, blue bolero_top, white ceremonial_dress_uniform, blue corset_top, black necktie, white gloves, white hot_pants, black high_heels, coat on shoulders, epaulettes"),   # 2026-10-03 配布ページの呼び出し語（ユーザー提供・ブラウンダスト2）。Sylvia＝素の姿／Sylviadef（白い踊り子の衣装・青い腰布）／Sylviamarine（白い礼装の軍服・制帽）／Sylviaswqueen（白いチョゴリ・髪をまとめる）／Sylvia-BIA（白い水着・貝の飾り）
    ("Lime", "Lime, slime girl"),   # 2026-10-03 ユーザーから：合言葉は Lime
    ("TamamoRaceQueen", "t4m4r4ce, animal ears, pink hair, twintails, hair bow, yellow eyes, cropped jacket"),
]


def post(path, data):
    req = urllib.request.Request(URL + path, data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def wf(name, trig):
    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CKPT}},
        "2": {"class_type": "LoraLoader", "inputs": {"lora_name": "キャラ\\%s.safetensors" % name, "strength_model": STRENGTH,
                                                    "strength_clip": STRENGTH, "model": ["1", 0], "clip": ["1", 1]}},
        "3": {"class_type": "CLIPSetLastLayer", "inputs": {"stop_at_clip_layer": -2, "clip": ["2", 1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": POS % trig, "clip": ["3", 0]}},
        "5": {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": ["3", 0]}},
        "6": {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": 1}},
        "7": {"class_type": "KSampler", "inputs": {"seed": SEED, "steps": 28, "cfg": 6.0, "sampler_name": "euler_ancestral",
                                                   "scheduler": "normal", "denoise": 1.0, "model": ["2", 0],
                                                   "positive": ["4", 0], "negative": ["5", 0], "latent_image": ["6", 0]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["1", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0], "filename_prefix": "キャラLoRA未割当/%s" % name.replace(" ", "_")}},
    }


def used_loras():
    """model.json の mod_style.chara_map で使っている LoRA のファイル名（拡張子なし）"""
    try:
        cm = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))["mod_style"]["chara_map"]
    except Exception as ex:
        print("model.json が読めません（割り振り済みの判定なしで進めます）: %s" % ex)
        return set()
    out = set()
    for d in cm.values():
        for v in d.values():
            if isinstance(v, dict) and v.get("lora"):
                out.add(os.path.splitext(os.path.basename(v["lora"].replace("\\", "/")))[0])
    return out


def auto_trigger(name):
    """(足す語, 年齢に関わるタグ)。LoRA の先頭にある学習タグの記録から決める。記録が無ければファイル名から"""
    guess = re.sub(r"[_\-]+", " ", re.split(r"[-_ ](?:XL|IL|ilxl|ixl|illu|illus|illustrious|nikke|richy|nyraen|elesico|v\d)", name, maxsplit=1, flags=re.I)[0]).strip().lower()
    try:
        with open(os.path.join(CDIR, name + ".safetensors"), "rb") as f:
            n = struct.unpack("<Q", f.read(8))[0]
            m = json.loads(f.read(n)).get("__metadata__") or {}
    except Exception:
        return guess, []
    tp = m.get("modelspec.trigger_phrase")
    tf = m.get("ss_tag_frequency")
    if not tf:
        return (tp if tp and tp != "None" else guess), []
    tot = collections.Counter()
    for c in json.loads(tf).values():
        tot.update(c)
    mx = max(tot.values()) if tot else 1
    trig = [t for t, c in tot.most_common(10) if c >= 0.6 * mx and t not in COMMON][:7]
    age = [t for t in tot if AGE.search(t)]
    return (", ".join(trig) or (tp if tp and tp != "None" else guess)), age


def main():
    dry, redo, every = "--dry-run" in sys.argv, "--redo" in sys.argv, "--all" in sys.argv
    only = [a.lower() for a in sys.argv[1:] if not a.startswith("--")]   # 名前の一部を書くと、その LoRA だけ撮り直す（例: Eclipse）
    hand = dict(LORAS)
    used = set() if every else used_loras()
    files = sorted(os.path.splitext(f)[0] for f in os.listdir(CDIR) if f.endswith(".safetensors") and not f.startswith("chr_"))
    done = set()
    if os.path.isdir(ODIR) and not redo:
        done = {re.sub(r"_\d{5}_\.png$", "", f) for f in os.listdir(ODIR) if f.endswith(".png")}
    todo, skipped = [], collections.Counter()
    for name in files:
        if only:
            if any(o in name.lower() for o in only):
                todo.append((name, hand[name] if name in hand else auto_trigger(name)[0]))
            continue
        if name in used:
            skipped["割り振り済み"] += 1
        elif name in SKIP:
            skipped["同じキャラの別版を使用中"] += 1
        elif name.replace(" ", "_") in done:
            skipped["もう撮ってある"] += 1
        else:
            trig, age = (hand[name], []) if name in hand else auto_trigger(name)
            if age:
                print(" 撮りません（学習タグに年齢に関わる語: %s）: %s" % (", ".join(age[:5]), name))
                skipped["年齢に関わるタグあり"] += 1
            else:
                todo.append((name, trig))
    if "--list" in sys.argv:   # 2026-10-03 撮らずに、割り振っていない LoRA と足す語を 未割当キャラLoRA_合言葉.csv に書き出す（割り当て用）
        import csv
        outp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "未割当キャラLoRA_合言葉.csv")
        with open(outp, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ファイル名", "足す語", "年齢に関わるタグ", "扱い"])
            for name in files:
                if name in used:
                    continue
                trig, age = (hand[name], []) if name in hand else auto_trigger(name)
                w.writerow([name, trig, ", ".join(age[:8]), "別版を使用中" if name in SKIP else ("撮らない（年齢タグ）" if age else "")])
        print("書き出しました: %s" % outp)
        return
    print("loras\\キャラ %d個 → 撮る %d個（%s）" % (len(files), len(todo), "・".join("%s %d" % x for x in skipped.items()) or "飛ばすものなし"))
    ok = 0
    for i, (name, trig) in enumerate(todo, 1):
        if dry:
            print(" [%d/%d] %s  ← %s" % (i, len(todo), name, trig))
            continue
        try:
            post("/prompt", {"prompt": wf(name, trig)})
            ok += 1
            print(" [%d/%d] 送信: %s  ← %s" % (i, len(todo), name, trig))
        except Exception as ex:
            body = ""
            if hasattr(ex, "read"):
                try:
                    body = ex.read().decode("utf-8", "replace")[:400]
                except Exception:
                    pass
            print(" [%d/%d] 送れませんでした: %s（%s %s）" % (i, len(todo), name, ex, body))
    if not dry:
        print("\n%d枚を送信しました。保存先: ComfyUI\\output\\キャラLoRA未割当\\" % ok)


main()
