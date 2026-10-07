# -*- coding: utf-8 -*-
"""N106〜N157の画像プロンプトを作る（2026-09-29）
N1〜N60 と同じ構成（立ち絵5・背景1・技CG7・敗北CG28・オナニーCG5・魔法5＋女装娘）で prompts\\<コード>.json を作る。
場面（技・敗北・オナニー）の組み立ては N31-N60_場面\\build_scenes.py と同じ関数を使う（主人公・成人タグ・逆転防止ネガが共通）。

使い方（画像生成フォルダで）:
  python N61-N105_場面\\build_new.py              … scene_data にある全MOD
  python N61-N105_場面\\build_new.py Gemini,Kiss  … 指定MODだけ
  python N61-N105_場面\\build_new.py --check      … 書き込まずに件数・長さ・年齢表現だけ確認
・中身は N61-N105_場面\\scene_data\\<コード>.py（書き方は SPEC_N61-N105.md）。直して実行し直せば、その MOD の JSON だけ作り直す。
・既に prompts\\<コード>.json がある場合は prompts_N106-N157作成前\\ に一度だけ保存してから上書きする。
・本編キャラ（chars の canon: True）は、本編の立ち絵を見ずに文章から作った見た目。本編キャラ外見_要確認.csv に一覧を書き出すので、
  立ち絵と違えば scene_data の tags を直して実行し直す。本編キャラはゲームの立ち絵を使うので、立ち絵の画像は撮らなくてよい（キャラLoRAの学習用には使える）。
登場人物はすべて20歳以上の成人。個人利用のみ。
"""
import csv, importlib.util, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PDIR = os.path.join(ROOT, "prompts")
BACK = os.path.join(ROOT, "prompts_N106-N157作成前")
DDIR = os.path.join(HERE, "scene_data")

_spec = importlib.util.spec_from_file_location("build_scenes", os.path.join(ROOT, "N31-N60_場面", "build_scenes.py"))
BS = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(BS)
Q, j = BS.Q, BS.j

NEG_STAND = ("lowres, worst quality, low quality, bad anatomy, bad hands, watermark, signature, text, letters, sign, logo, numbers, "
             "child, loli, shota, young, teenage, underage, petite female, muscular, abs, pectorals, bara, hairy, twins, same face, "
             "extra legs, extra arms, merged bodies, blood, injury, childlike, child body, youthful body, baby face, round face, "
             "chubby cheeks, short limbs, big head, chibi, small body, young boy, kid")
NEG_F = "1boy, 2girls, multiple girls, futanari, penis, nude, nipples, nsfw, topless"
NEG_NH = ("1boy, 2girls, multiple girls, nude, nipples, topless, masculine, manly, male face, square jaw, broad shoulders, facial hair, "
          "beard, stubble, flat chest, erection, erect penis, her penis exposed, penis out of her clothes, erection tenting her clothes, "
          "testicles, pussy, cameltoe")
NEG_M = "1girl, female, woman, breasts, large breasts, medium breasts, cleavage, nude, nipples, nsfw, masculine face, manly, broad shoulders"
NEG_BG = "1girl, 1boy, person, people, nude, nsfw"
AGE_BAD = re.compile(r"\b(child|children|kid|kids|loli|shota|teen|teenage|teenager|young girl|young boy|little girl|little boy|"
                     r"schoolgirl|school uniform|petite|1[0-9] years old|underage|elementary|middle school|high school|aged down|flat-chested child)\b", re.I)
AGE_OK = re.compile(r"\b(adult|mature|years old|20s|30s|early 20s)\b", re.I)


def load(code):
    spec = importlib.util.spec_from_file_location("sd_" + code, os.path.join(DDIR, code + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.DATA


def body_head(c):
    t = c["type"]
    if t == "otoko":
        return "safe", "1boy", NEG_STAND + ", " + NEG_M
    if t == "nh":
        return "sensitive", "1girl, " + BS.NH_BULGE, NEG_STAND + ", " + NEG_NH
    return "safe", "1girl", NEG_STAND + ", " + NEG_F


def stand(D, who):
    c = D["chars"][who]
    rating, head, neg = body_head(c)
    pos = j(Q, rating, "solo", head, c["tags"], c.get("pose", "standing, confident smile, looking at viewer"),
            "full body, simple background, white background")
    if c.get("neg"):
        neg += ", " + c["neg"]
    v = {"positive": pos, "negative": neg, "width": 832, "height": 1216, "rmbg": True}
    return fix_scene(D, who, v)


def magic(D, v):
    who, place, action = v
    if who:
        c = D["chars"][who]
        rating, head, neg = body_head(c)
        pos = j(Q, rating, "solo", head, c["tags"], action, "looking at viewer", D["world"], D["places"][place])
        if c.get("neg"):
            neg += ", " + c["neg"]
    else:
        pos = j(Q, "safe", "no humans, still life", action, D["world"], D["places"][place], "detailed background")
        neg = NEG_STAND + ", " + NEG_BG
    return {"positive": pos, "negative": neg, "width": 832, "height": 1216, "rmbg": False}


def bg(D):
    return {"positive": j(Q, "safe", "no humans, scenery", D["bg"], "detailed background"),
            "negative": NEG_STAND + ", " + NEG_BG, "width": 832, "height": 1216, "rmbg": False}


def josou(D):
    # 女装娘（男モンスターが女装させられた姿）。主人公LoRA・主人公補正が入らないよう navy ではなく dark blue hair（N46〜N60 と同じ）
    pos = j(Q, "safe", "solo", "1boy, adult man, 20s, mature face, adult proportions, slender, soft body",
            "dark blue hair, short hair, hair over eyes", "crossdressing", D["josou"],
            "holding down the hem, looking down in embarrassment", "full body, simple background, white background")
    neg = NEG_STAND + ", 2girls, multiple girls, futanari, penis, nude, nipples, nsfw, topless, 1girl, breasts, petite male, muscular"
    return {"positive": pos, "negative": neg, "width": 832, "height": 1216, "rmbg": True}


def build(code):
    D = load(code)
    out = {}
    for k, name in (("m", "master"), ("e1", "e1"), ("e2", "e2"), ("e3", "e3"), ("boss", "boss")):
        out["%s_%s" % (code, name)] = stand(D, k)
    if D.get("josou"):
        out[code + "_josou"] = josou(D)
    out[code + "_bg"] = bg(D)
    out.update(BS_build(D, code))
    for i in range(1, 6):
        out["%s_magic_%d" % (code, i)] = magic(D, D["magic"][str(i)] if str(i) in D["magic"] else D["magic"][i])
    return D, out


MULTI_LEG = re.compile(r"\b(centaur|arachne|spider lower body|horse lower body|octopus|scylla|tentacles? (?:from|below) the waist|lamia|snake lower body|mermaid|fish tail)\b", re.I)
LEG_NEG = ("extra legs", "three legs", "four legs")
STRAP_DEFAULT = "black leather strap-on harness worn over her clothes"


def fix_scene(D, who, v):
    """build_scenes の共通ネガ・ペニバンを人物に合わせて直す（2026-09-29）
    ・人外の下半身（ケンタウロス・アラクネ・タコ等）は extra legs 系のネガを外す（脚の多い体と打ち消し合うため）
    ・chars の "strap"（例 "golden strap-on on a white leather harness"）があればペニバンの色・形を差し替える"""
    c = D["chars"][who]
    if MULTI_LEG.search(c["tags"]):
        for t in LEG_NEG:
            v["negative"] = re.sub(r"(^|,\s*)" + re.escape(t) + r"(?=\s*,|\s*$)", "", v["negative"])
    if c.get("strap") and STRAP_DEFAULT in v["positive"]:
        v["positive"] = v["positive"].replace(STRAP_DEFAULT, c["strap"] + " worn over her clothes")
    for t in c.get("neg_remove") or []:
        v["negative"] = re.sub(r"(^|,\s*)" + re.escape(t) + r"(?=\s*,|\s*$)", "", v["negative"])
    v["negative"] = re.sub(r"^,\s*", "", v["negative"])
    return v


def BS_build(D, code):
    """build_scenes.build と同じ（scene_data を直接渡す）"""
    out = {}
    for k in BS.KEYS_ATK:
        place, action, opt = BS.unpack(D["atk"][k])
        who = "m" if k.startswith("m") else k
        out[code + "_atk_" + k] = fix_scene(D, who, BS.scene(D, who, place, action, D["atk_desc"].get(k, ""), opt))
    for k in BS.KEYS_LOSE:
        place, action, opt = BS.unpack(D["lose"][k])
        w = k.split("_", 1)[1]
        who = "m" if w.startswith("m") else w
        desc = D["chars"][who]["name"] + " " + D["lose_desc"]
        out[code + "_lose_" + k] = fix_scene(D, who, BS.scene(D, who, place, action, desc, opt, onani=k.startswith("onani_")))
    for k in BS.KEYS_ONA:
        place, action, opt = BS.unpack(D["onanie"][k])
        out[code + "_onanie_" + k] = fix_scene(D, BS.ONA_WHO[k], BS.scene(D, BS.ONA_WHO[k], place, action + ", flushed, sweat, trembling",
                                              "he pleasures himself during the card battle while the other character watches from afar.",
                                              opt, onani=True))
    return out


def check(code, D, out):
    errs = []
    for k in ("m", "e1", "e2", "e3", "boss"):
        c = D["chars"][k]
        if c["type"] not in ("woman", "nh", "otoko"):
            errs.append("%s type=%s" % (k, c["type"]))
        if AGE_BAD.search(c["tags"]):
            errs.append("%s tags に年齢の語: %s" % (k, AGE_BAD.search(c["tags"]).group(0)))
        if not AGE_OK.search(c["tags"]):
            errs.append("%s tags に成人の語（adult woman / mature female 等）が無い" % k)
        if re.search(r"\b(navy|blue hair|blue eyes|aqua)\b", c["tags"], re.I):
            errs.append("%s tags に紺・青系（主人公と紛れる）" % k)
    for n, v in out.items():
        p = v["positive"]
        m = AGE_BAD.search(re.sub(r"\byoung\b", "", p))
        if m:
            errs.append("%s: 年齢の語 %s" % (n, m.group(0)))
    places = set(D["places"])
    for sec in ("atk", "lose", "onanie"):
        for k, v in D[sec].items():
            if v[0] not in places:
                errs.append("%s.%s 場所キー %s が places に無い" % (sec, k, v[0]))
    for k, v in (D["magic"].items()):
        if v[1] not in places or (v[0] and v[0] not in D["chars"]):
            errs.append("magic.%s の場所か人物が無い" % k)
    n_expect = 5 + 1 + 40 + 5 + (1 if D.get("josou") else 0)
    if len(out) != n_expect:
        errs.append("件数 %d（期待 %d）" % (len(out), n_expect))
    return errs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    chk = "--check" in sys.argv
    allc = sorted(f[:-3] for f in os.listdir(DDIR) if f.endswith(".py"))
    mods = allc if not args else [m.strip() for m in args[0].split(",") if m.strip()]
    total, bad, canon = 0, 0, []
    for code in mods:
        try:
            D, out = build(code)
        except Exception as ex:
            print("  %-10s [エラー] %s" % (code, ex)); bad += 1; continue
        errs = check(code, D, out)
        L = max(len(v["positive"]) for v in out.values())
        print("  %-10s %2d件（最長 %d字）%s" % (code, len(out), L, ("  ★" + " / ".join(errs[:4])) if errs else ""))
        if errs:
            bad += 1
        for k in ("m", "e1", "e2", "e3", "boss"):
            c = D["chars"][k]
            if c.get("canon"):
                canon.append([code, {"m": "master"}.get(k, k), c.get("jp", ""), c.get("canon_img", ""), c["tags"]])
        total += len(out)
        if chk:
            continue
        pj = os.path.join(PDIR, code + ".json")
        if os.path.exists(pj):
            os.makedirs(BACK, exist_ok=True)
            b = os.path.join(BACK, code + ".json")
            if not os.path.exists(b):
                shutil.copy2(pj, b)
        json.dump(out, open(pj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if canon and not chk:
        with open(os.path.join(HERE, "本編キャラ外見_要確認.csv"), "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["MODコード", "キャラ", "名前", "本編の画像", "今のタグ（本編の立ち絵と違えば scene_data を直す）"])
            w.writerows(canon)
    print("合計 %d件／%dMOD%s%s" % (total, len(mods), "（確認のみ）" if chk else "", ("　★要確認 %dMOD" % bad) if bad else ""))


if __name__ == "__main__":
    main()
