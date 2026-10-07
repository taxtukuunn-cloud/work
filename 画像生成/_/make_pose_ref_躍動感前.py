# -*- coding: utf-8 -*-
"""構図の下書きの「元絵」の候補を撮る（2026-09-30）
構図LoRA（model.json の pose_loras）で、成人の2人（相手＝大人の女性／主人公＝細身の大人の男）の絵を何枚か撮る。
よいものを 画像生成\\構図下書き元\\<id>.png（2枚目以降は <id>_2.png, <id>_3.png …）に置くと、あとでその絵から下書き（奥行き）を作る（その仕組みは次の段階）。
・学習タグに子どもを示すタグがあって止めた構図LoRA（memo に「子ども」等）は使わない。
・構図LoRA 以外の構図（参考絵の構図カタログ）は 構図候補_追加.json に書く（lora を書けばその構図LoRA も使う）。
・背景は白、絵柄LoRA・主人公LoRA・敵キャラLoRA は使わない（形だけが目的）。
・切り取りは既定で全身。構図候補_追加.json の "frame"（例 "upper body"）や LORA_OVERRIDE で変えられる（乳首など小さい部分が主役の構図用）。
保存先: ComfyUI\\output\\構図候補\\<id>\\
使い方: python make_pose_ref.py [--list] [--only id,id] [--batch 4] [--dry-run]"""
import argparse, hashlib, json, os, re, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import gen

SERVER = "http://127.0.0.1:8188"
OUTDIR = "構図候補"
PICK_DIR = os.path.join(HERE, "構図下書き元")
EXTRA = os.path.join(HERE, "構図候補_追加.json")
AGE_WORDS = ("子ども", "years old", "loli", "shota")   # memo にこれがある構図LoRA は使わない

# 相手と主人公（成人の体つきをはっきり書く）
WOMAN = "adult woman, mature female, tall woman, long black hair, clothed female"
MAN = ("the man is a slim adult man with navy blue hair, adult male body, not muscular, "
       "he is shorter than the woman, submissive male")
BASE_POS = "explicit, 1girl, 1boy, femdom, dominant woman, " + WOMAN + ", " + MAN + ", white background, simple background"
BASE_NEG = ("2boys, 3boys, 2girls, 3girls, multiple girls, extra arms, extra legs, extra hands, bad anatomy, bad hands, "
            "muscular male, abs, pectorals, bara, lowres, worst quality, text, watermark, "
            # 2026-09-30 facesit・futa・rusty・whisper の学習画像に学校の制服タグが混ざっている（構図LoRA_中身一覧）
            "school uniform, serafuku, school bag, randoseru, gym uniform, buruma, "
            "speech bubble, spoken heart")   # 2026-09-30 吹き出しのハートが出た

# 画面の切り取り（既定は全身）。乳首など小さい部分が主役の構図は全身だと位置がずれるので寄せる（2026-09-30）
FRAME_DEFAULT = "full body"
NIPPLE_POS = "topless male, bare chest, flat male chest, male nipples visible"
NIPPLE_NEG = ("licking his stomach, licking his navel, licking the center of his chest, licking her own breast, "
              "licking the woman's body, clothed male, shirt on the man")
# 構図LoRA ごとの上書き（frame＝切り取り、pos／neg＝足す語、strength＝LoRA の強さ）
LORA_OVERRIDE = {
    # 2026-09-30 1回目：接写＋強さ0.8 にしたら、正面から見上げるパイズリ風の POV になり舐めていなかった
    #   → 姿勢を具体的に（横に寝そべって頭を彼の胸に・口を乳首に）、切り取りは上半身、パイズリ・正面向きをネガへ
    # 2026-09-30 2回目：横に寝そべる指定でも、脚の間から舐める POV（口がペニス）になった。この LoRA は POV で
    #   「相手が主人公の胸元から見上げる」形を覚えているので、それに合わせて顔を胸元に置き、ペニスの語は書かない（口がそちらへ行く）
    "nipple_lick_hj": {"frame": "upper body", "strength": 0.6,
                       "pos": ("pov, she lies on top of his chest, her face very close to viewer, her mouth on his nipple, "
                               "licking his nipple, looking up at viewer, her other hand gives a handjob below, " + NIPPLE_POS),
                       "neg": NIPPLE_NEG + ", paizuri, penis between breasts, titjob, fellatio, licking penis, penis in mouth, "
                                           "oral, penis near her face, kneeling between his legs, her face above his stomach"},
    "toes_nipple": {"pos": NIPPLE_POS, "neg": "clothed male, shirt on the man"},
    # 2026-09-30 1回目：POV にならず、正面から「相手が後ろに座り主人公を脚の間に抱える」絵になった → POV・下から見上げるを明記
    "lap_finger": {"frame": "upper body",
                   "pos": "pov, from below, lying on her lap, she leans over and looks down at viewer, her face above viewer, her hand on viewer's head",
                   "neg": "front view, he sits, sitting between her legs, full body, his face visible"},
}

# 構図LoRA ごとの補足（トリガー語に足す姿勢の説明）
HINT = {
    "lamia": "lamia woman, snake lower body coiled around him, he lies on his back",
    "arachne": "arachne woman with spider lower body on top of him",
    "succubus_tail": "succubus woman, her tail wrapped around him, he lies on his back",
    "energy_drain": "succubus draining his energy, glowing aura, he lies on his back, she leans over him",
    "lamia_coil": "lamia woman wrapping her snake tail around his body, standing",
    "toes_nipple": "she sits, pinching his nipples with her toes, he lies on his back",
    "nipple_lick_hj": "",   # 姿勢は LORA_OVERRIDE の pos に書く（POV で胸元から見上げる）
    "peg_pov": "pov, she wears a strap-on, he lies on his back with legs up",
    "peg_chair": "he is tied to a chair with legs up, she wears a strap-on and stands in front of him",
    "suspension": "he hangs with wrists bound above his head, she stands in front of him",
    "inverted": "he hangs upside down, she stands in front of him",
    "peg_spoon": "both lie on their sides, she spoons him from behind wearing a strap-on",
    "peg_doggy": "he is on all fours, she kneels behind him wearing a strap-on",
    "peg_strapon": "he lies on his back with legs up, she kneels between his legs wearing a strap-on",
    "futa": "futanari woman, he is on all fours, she kneels behind him",
    "whisper": "she whispers into his ear from behind, he sits",
    "lap_finger": "he lies with his head on her lap, lap pillow, she looks down at him",
    "rusty": "he stands and bends over, she kneels behind him",
    "chastity": "pov, he wears a chastity cage, she looks down at him",
    "xcross": "he is restrained on an x-cross, spread-eagle, she stands beside him",
    "collar": "he kneels on all fours wearing a collar, she holds the leash and stands",
    "facesit": "she sits on his face, he lies on his back",
    "step": "pov from below, she stands and steps on him, looking down",
    "thigh": "she straddles him, thighjob, he lies on his back",
    "rah": "she stands behind him and reaches around, reach-around handjob, he stands",
    "rah_behind": "she hugs him from behind and reaches around to his chest, he sits",
    "headlock": "she holds his head in a headlock from beside him and gives a handjob",
    "paizuri": "pov, he lies on his back, she kneels between his legs, paizuri",
    "xray": "cross-section, he lies on his back with legs up, she kneels between his legs wearing a strap-on",
    "figure_four": "she locks his head between her thighs, figure-four leg lock, both lie on the floor",
    "alt_ashikoki": "she sits and gives a footjob, he lies on his back",
    "alt_thigh_top": "pov, she straddles him, thighjob",
    "alt_strapon": "he is on all fours, she kneels behind him wearing a strap-on",
    "alt_anilingus": "he is on all fours, she kneels behind him, handjob from behind",
}


def picks(k):
    """構図下書き元に置いた元絵（<id>.png・<id>_2.png …）"""
    if not os.path.isdir(PICK_DIR):
        return []
    rx = re.compile(r"^%s(?:_(\d+))?\.png$" % re.escape(k), re.I)
    return sorted(f for f in os.listdir(PICK_DIR) if rx.match(f))


def items():
    """[(id, {lora, strength, trigger, prompt, neg, from})]"""
    mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
    out, skipped = [], []
    seen_file = {}
    for p in mj.get("pose_loras") or []:
        if not isinstance(p, dict) or not p.get("file"):
            continue
        memo = p.get("memo", "") or ""
        if any(w in memo for w in AGE_WORDS):
            skipped.append(p["id"]); continue
        ov = LORA_OVERRIDE.get(p["id"], {})
        out.append((p["id"], {"lora": p["file"], "strength": float(ov.get("strength", p.get("strength", 0.6))),
                              "trigger": p.get("trigger", ""),
                              "prompt": ", ".join(x for x in (HINT.get(p["id"], ""), ov.get("pos", "")) if x),
                              "neg": ", ".join(x for x in (p.get("neg", ""), ov.get("neg", "")) if x),
                              "frame": ov.get("frame", FRAME_DEFAULT), "from": "構図LoRA"}))
    if os.path.isfile(EXTRA):
        loras = {p["id"]: p for p in mj.get("pose_loras") or [] if isinstance(p, dict)}
        for e in json.load(open(EXTRA, encoding="utf-8")):
            if not isinstance(e, dict) or not e.get("id") or e["id"].startswith("_"):
                continue
            L = loras.get(e.get("lora") or "")
            if L and any(w in (L.get("memo") or "") for w in AGE_WORDS):
                print("(%s: 構図LoRA %s は年齢の理由で止めているので使わず、プロンプトだけで撮ります)" % (e["id"], L["id"]))
                L = None
            out.append((e["id"], {"lora": L["file"] if L else "", "strength": float(e.get("strength", L.get("strength", 0.6) if L else 0)),
                                  "trigger": L.get("trigger", "") if L else "", "prompt": e.get("prompt", ""),
                                  "neg": e.get("neg", ""), "frame": e.get("frame", FRAME_DEFAULT), "from": "カタログ"}))
    return out, skipped


def workflow(it, seed, batch, prefix):
    pos = ", ".join(x for x in (it["trigger"], it["prompt"], BASE_POS, it.get("frame", FRAME_DEFAULT)) if x)
    neg = ", ".join(x for x in (BASE_NEG, gen.ADULT_NEG, gen.ADULT_BODY_NEG, it["neg"]) if x)
    gen.CUR_TEXT = pos
    gen.CUR_SCENE = False
    pos, neg = gen.adapt_prompt(pos, neg)
    M = gen.MODEL
    w = {"3": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": M["ckpt_name"]}}}
    m, c = ["3", 0], ["3", 1]
    if it["lora"]:
        w["50"] = {"class_type": "LoraLoader", "inputs": {"model": m, "clip": c, "lora_name": it["lora"],
                   "strength_model": it["strength"], "strength_clip": it["strength"]}}
        m, c = ["50", 0], ["50", 1]
    w.update({
     "4": {"class_type": "CLIPSetLastLayer", "inputs": {"clip": c, "stop_at_clip_layer": int(M.get("clip_skip", -2))}},
     "6": {"class_type": "CLIPTextEncode", "inputs": {"text": pos, "clip": ["4", 0]}},
     "7": {"class_type": "CLIPTextEncode", "inputs": {"text": neg, "clip": ["4", 0]}},
     "8": {"class_type": "EmptyLatentImage", "inputs": {"width": 832, "height": 1216, "batch_size": batch}},   # 場面と同じ大きさ
     "9": {"class_type": "KSampler", "inputs": {"seed": seed, "steps": int(M["steps"]), "cfg": float(M["cfg"]),
           "sampler_name": M["sampler"], "scheduler": M["scheduler"], "denoise": 1.0,
           "model": m, "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["8", 0]}},
     "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 2]}},
     "11": {"class_type": "SaveImage", "inputs": {"images": ["10", 0], "filename_prefix": prefix}},
    })
    return w, pos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--only", help="id をカンマ区切り（空＝全部）")
    ap.add_argument("--batch", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    gen.MODEL = gen.load_model("wai")
    its, skipped = items()
    os.makedirs(PICK_DIR, exist_ok=True)
    if a.list or a.dry_run:
        print("撮れる構図（%d）:" % len(its))
        for k, it in its:
            n = len(picks(k))
            done = ("  ※元絵 %d枚" % n) if n else ""
            print("  %-22s %s %s%s" % (k, it["from"], (it["lora"] or "（プロンプトだけ）").split("\\")[-1], done))
        if skipped:
            print("年齢の理由で使わない構図LoRA:", ", ".join(skipped))
        if a.list:
            return
    if a.only:
        want = [x.strip() for x in a.only.replace("、", ",").split(",") if x.strip()]
        bad = [x for x in want if x not in dict(its)]
        if bad:
            print("知らない id:", ", ".join(bad), "（--list で一覧）"); sys.exit(1)
        its = [(k, v) for k, v in its if k in want]
    print("構図 %d 種 × %d 枚 = %d 枚 → ComfyUI\\output\\%s\\<id>\\" % (len(its), a.batch, len(its) * a.batch, OUTDIR))
    if a.dry_run:
        k, it = its[0]
        print("例（%s）:" % k, workflow(it, 1, 1, "x")[1][:400], "...")
        return
    try:
        urllib.request.urlopen(SERVER + "/", timeout=5)
    except Exception:
        print("ComfyUI が動いていません。"); sys.exit(1)
    for i, (k, it) in enumerate(its, 1):
        while gen.queue_count() >= 4:
            time.sleep(3)
        seed = int(hashlib.md5(("poseref-" + k).encode()).hexdigest(), 16) % (2**31 - 1)
        w, _ = workflow(it, seed, a.batch, "%s/%s/%s" % (OUTDIR, k, k))
        req = urllib.request.Request(SERVER + "/prompt", data=json.dumps({"prompt": w}).encode("utf-8"),
                                     headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=30)
            print(" [%d/%d] %s" % (i, len(its), k))
        except urllib.error.HTTPError as ex:
            print(" [エラー]", k, ex, ex.read().decode("utf-8", "replace")[:400]); sys.exit(1)
        time.sleep(0.2)
    print("送信しました。撮れたら ComfyUI\\output\\%s\\<id>\\ からよい画像を選び（成人の体つきに見えるものだけ）、" % OUTDIR)
    print("  元絵を取り込む.bat にドラッグ＆ドロップしてください（構図下書き元\\<id>.png, <id>_2.png … で入ります）。")


if __name__ == "__main__":
    main()
