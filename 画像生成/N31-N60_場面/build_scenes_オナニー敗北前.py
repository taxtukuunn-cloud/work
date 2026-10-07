# -*- coding: utf-8 -*-
"""N31〜N60 場面プロンプト生成（2026-09-27）
N1〜N30 と同じ 51枚（＋女装娘）構成にするため、N31〜N60 の prompts\\<コード>.json に
技CG7（atk_*）・敗北CG28（lose_*）・オナニーCG5（onanie_*）の 40場面を足す。
立ち絵・魔法・背景・女装娘など、すでにある項目はそのまま残す（上書きしない）。

使い方（画像生成フォルダで）:
  python N31-N60_場面\\build_scenes.py            … 30MOD すべて
  python N31-N60_場面\\build_scenes.py Onsen,Oiran … 指定MODだけ
  python N31-N60_場面\\build_scenes.py --check    … 書き込まずに件数・長さだけ確認
・場面の中身は N31-N60_場面\\scene_data\\<コード>.py（各MODの敗北シナリオ28本・技から作った英語の場面文）。
  ここを直して実行し直せば、その MOD の 40場面だけ作り直される。
・初回実行時、元の prompts\\<コード>.json を prompts_場面追加前\\ に保存する（2回目以降は保存し直さない）。
・書き方は N27 Knight の build_prompts.py／N23 Heels と同じ（主人公 v5・成人タグ・逆転防止のネガティブ）。
  gen.py 側の自動補正（主人公LoRA・相手の顔・男の娘・女装）はそのまま効く。
登場人物はすべて20歳以上の成人。個人利用のみ。
"""
import importlib.util, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # 画像生成フォルダ
PDIR = os.path.join(ROOT, "prompts")
BACK = os.path.join(ROOT, "prompts_場面追加前")
DDIR = os.path.join(HERE, "scene_data")

MODS = ["Onsen", "Arachne", "Dream", "Library", "Angel", "Harem", "Dragon", "Tutor", "DarkElf", "Casino",
        "Nekomata", "Snow", "Oni", "Mimic", "Train",
        "ShowPub", "Oiran", "Office", "Lingerie", "GhostShip", "Alchemy", "Masque", "Fortune", "Revue", "Studio",
        "Luna", "Police", "Circus", "Candy", "Starship"]

Q = "masterpiece, best quality, amazing quality, very aesthetic, absurdres"

# ---- 主人公（v5：160cm・細身の成人男性・非筋肉質）
PROT = ("faceless male, navy blue hair, short hair, hair over eyes, bangs covering eyes, adult man, mature male, 25 years old, "
        "adult male body, adult proportions, long legs, slim adult build, lean, not muscular, defined jawline, adam's apple, "
        "collarbones, flat male chest, smooth pale skin, blush, ordinary human man")
NAKED = "nude male, completely naked, penis"
DRESSED = "crossdressing adult man, crossdress, flat male chest"   # hero_outfit があるとき（gen.py の女装補正が効く）
CAGE = ("his penis is locked in a small flat silver chastity cage with a thin strap around his waist and a tiny silver padlock, "
        "flaccid penis inside the cage")

# ---- ネガティブ
NEG_BASE = ("lowres, worst quality, low quality, bad anatomy, bad hands, bad feet, extra toes, watermark, signature, text, letters, "
            "sign, logo, numbers, child, loli, shota, young, teenage, underage, childlike, child body, youthful body, baby face, "
            "round face, chubby cheeks, short limbs, big head, chibi, small body, petite male, young boy, kid, muscular, abs, "
            "pectorals, bara, hairy, twins, same face, same hair color, extra legs, three legs, four legs, extra arms, "
            "eyes visible on the navy-haired man, merged bodies, blood, bleeding, wound, gore, injury, crying in pain, "
            "rape, violence, ahegao")
NEG_HERO = ("breasts on the man, cleavage on the man, long hair on the man, wig, masculine, manly, square jaw, thick eyebrows, "
            "broad shoulders, facial hair, stubble, role reversal, reverse roles, receiver penetrating, receiver on top, "
            "receiver dominant, the navy-haired man touching the other character")
NEG_F = ("2boys, 3boys, 2girls, yuri, vaginal, penetration by male, pussy, vagina, nude female, female nudity, topless female, "
         "the woman naked, the woman undressed, navy hair on the woman, blue hair on the woman, hair over eyes on the woman, "
         "woman with hidden eyes, penis inside the woman, sex with the woman")
NEG_M = ("1girl, female, woman, breasts, large breasts, medium breasts, cleavage, 3boys, vaginal, pussy, vagina, "
         "navy hair on the other man, blue hair on the other man, the other man naked, the other man undressed, "
         "clothes on the navy-haired man, hair over eyes on the other man, masculine face")
NEG_NOSTRAP = ", strap-on, dildo on the woman"
NEG_F_NOPEN = ", futanari, penis on the woman, her penis"
# ニューハーフ：服の下の股間のふくらみ（勃起していないペニスの形）が分かるように（2026-09-27）
NH_BULGE = ("newhalf, crotch bulge, visible bulge under her clothes, the soft outline of her flaccid penis showing through the fabric "
            "at her crotch")
NEG_NH_NOPEN = (", her penis exposed, penis out of her clothes, her erection, erect penis on the woman, erection tenting her clothes, "
                "testicles")
NEG_M_NOPEN = ", penis on the other man, the other man's penis, erection on the other man"
NEG_INSERT = ", merged, fused, overlapping penises, penis touching penis"
NEG_ONANI = (", the other character touching him, hands on him, the other character masturbating, hand on penis, holding penis, "
             "handjob, stroking penis, penis grab, hand on crotch, hand near penis, touching penis")
NEG_CAGE = ", erection, erect penis, large penis"
NEG_NAKEDCLOTH = ", clothes on the naked man, the naked man wearing the other character's clothes"

KEYS_ATK = ["m1", "m2", "m3", "e1", "e2", "e3", "boss"]
KEYS_LOSE = [r + "_" + w for w in ["m1", "m2", "m3", "e1", "e2", "e3", "boss"] for r in ("btl", "onani", "inochi", "onedari")]
KEYS_ONA = ["master", "e1", "e2", "e3", "boss"]
ONA_WHO = {"master": "m", "e1": "e1", "e2": "e2", "e3": "e3", "boss": "boss"}
FEMALE_TYPES = ("woman", "nh")     # 見た目が女性（1girl）＝女性・ニューハーフ（人外の女性も woman）


def load(code):
    p = os.path.join(DDIR, code + ".py")
    spec = importlib.util.spec_from_file_location("sd_" + code, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.DATA


def j(*xs):
    return ", ".join(x.strip().strip(",").strip() for x in xs if x and x.strip().strip(","))


def scene(D, who, place, action, desc, opt, onani=False):
    c = D["chars"][who]
    t = c["type"]
    fem = t in FEMALE_TYPES
    pen = opt.get("pen")                       # None / "strapon" / "penis" / "toy"
    cage = bool(opt.get("cage"))
    outfit = opt.get("hero_outfit") or ""
    cage_t = CAGE
    if cage and isinstance(opt.get("cage"), str):
        cage_t = opt["cage"]
    elif cage and re.search(r"\bgold(en)?\b", action):
        cage_t = CAGE.replace("silver", "gold")
    body = cage_t if cage else ("erection" if not opt.get("flaccid") else "flaccid penis")
    if outfit:
        hero = j(PROT, DRESSED, "he wears " + outfit, body if (cage or "penis" in action or "crotch" in action) else "")
    else:
        hero = j(PROT, NAKED, body)
    taller = c.get("height_note") or ("she is taller than him" if fem else "the other man is taller than him")
    if fem:
        keep = "she keeps her clothes on, fully clothed female, " + (
            "only the man is crossdressed" if outfit else "only the navy-haired man is naked")
    else:
        keep = "the other man keeps his clothes on, " + (
            "only the navy-haired man is crossdressed" if outfit else "only the shorter navy-haired man is naked")
    place_t = D["places"][place]
    world = D["world"]
    if onani:
        head = "1girl, 1boy" if fem else "2boys"
        pos = j(Q, "explicit", head + ", solo focus on the navy-haired man", hero, "he is in the foreground", action,
                "hands far away from his crotch, penis untouched" if "penis untouched" not in action and "cage" not in action and not cage else "",
                c["name"] + " stands far in the background fully clothed, watching, small in frame, not touching him",
                world, place_t, desc, "adult male, 20s, mature face, adult proportions")
    else:
        if fem:
            pt = NH_BULGE if (t == "nh" and pen != "penis") else ""
            if pen == "strapon":
                pt = j(pt, "black leather strap-on harness worn over her clothes, strap-on")
            elif pen == "penis":
                pt = ("newhalf, futanari" if t == "nh" else "futanari") + \
                     ", her clothes opened only at the crotch, her large penis exposed, two separate penises"
            pos = j(Q, "explicit", "1girl, 1boy, duo, two people", "THE WOMAN: " + c["tags"], pt,
                    "THE MAN (clearly visible in the picture): 1boy, male, " + hero, "he is slightly shorter than her",
                    action, keep, taller, world, place_t, desc)
        else:
            pt = ""
            if pen == "penis":
                pt = "the other man's clothes opened only at the crotch, his large penis exposed, two separate penises"
            elif pen == "strapon":
                pt = "strap-on harness worn over his clothes, strap-on"
            pos = j(Q, "explicit", "2boys", c["tags"], pt, "and a naked shorter adult man: " + hero if not outfit else
                    "and a crossdressed shorter adult man: " + hero, "he is slightly shorter than the other man",
                    action, keep, taller, world, place_t, desc)
    neg = NEG_BASE + ", " + NEG_HERO + ", " + (NEG_F if fem else NEG_M)
    if outfit:
        neg = neg.replace(", clothes on the navy-haired man", "")
    if fem:
        if pen not in ("strapon", "toy"):
            neg += NEG_NOSTRAP
        if pen != "penis":
            neg += NEG_NH_NOPEN if t == "nh" else NEG_F_NOPEN
    else:
        if pen != "penis":
            neg += NEG_M_NOPEN
    if pen in ("penis",):
        neg += NEG_INSERT
    if onani:
        neg += NEG_ONANI
    if cage:
        neg += NEG_CAGE
    if not outfit:
        neg += NEG_NAKEDCLOTH
    if c.get("neg"):
        neg += ", " + c["neg"]
    if opt.get("neg"):
        neg += ", " + opt["neg"]
    return {"positive": pos, "negative": neg, "width": 832, "height": 1216, "rmbg": False}


def unpack(v):
    if len(v) == 2:
        return v[0], v[1], {}
    return v[0], v[1], v[2] or {}


def build(code):
    D = load(code)
    out = {}
    for k in KEYS_ATK:
        place, action, opt = unpack(D["atk"][k])
        who = "m" if k.startswith("m") else k
        out[code + "_atk_" + k] = scene(D, who, place, action, D["atk_desc"].get(k, ""), opt)
    for k in KEYS_LOSE:
        place, action, opt = unpack(D["lose"][k])
        w = k.split("_", 1)[1]
        who = "m" if w.startswith("m") else w
        onani = k.startswith("onani_")
        desc = c_name(D, who) + " " + D["lose_desc"]
        out[code + "_lose_" + k] = scene(D, who, place, action, desc, opt, onani=onani)
    for k in KEYS_ONA:
        place, action, opt = unpack(D["onanie"][k])
        who = ONA_WHO[k]
        out[code + "_onanie_" + k] = scene(D, who, place, action + ", flushed, sweat, trembling",
                                           "he pleasures himself during the card battle while the other character watches from afar.",
                                           opt, onani=True)
    return out


def c_name(D, who):
    return D["chars"][who]["name"]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    mods = MODS if not args else [m.strip() for m in args[0].split(",") if m.strip()]
    total = 0
    for code in mods:
        try:
            new = build(code)
        except FileNotFoundError:
            print("  %-10s scene_data がありません（飛ばす）" % code); continue
        pj = os.path.join(PDIR, code + ".json")
        P = json.load(open(pj, encoding="utf-8"))
        # 既存（立ち絵・背景・魔法・女装娘）は残し、場面は作り直す。並びは Knight と同じ（立ち絵→背景→場面→魔法）
        keep = {k: v for k, v in P.items() if k not in new and not any(
            k.startswith(code + x) for x in ("_atk_", "_lose_", "_onanie_"))}
        head = {k: v for k, v in keep.items() if "_magic_" not in k}
        magic = {k: v for k, v in keep.items() if "_magic_" in k}
        R = dict(head); R.update(new); R.update(magic)
        L = max(len(v["positive"]) for v in new.values())
        print("  %-10s 既存 %2d件 ＋ 場面 %2d件 ＝ %2d件（場面の最長 %d字）" % (code, len(keep), len(new), len(R), L))
        total += len(new)
        if check:
            continue
        os.makedirs(BACK, exist_ok=True)
        b = os.path.join(BACK, code + ".json")
        if not os.path.exists(b):
            shutil.copy2(pj, b)
        json.dump(R, open(pj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("場面 合計 %d件%s" % (total, "（確認のみ・書き込みなし）" if check else ""))


if __name__ == "__main__":
    main()
