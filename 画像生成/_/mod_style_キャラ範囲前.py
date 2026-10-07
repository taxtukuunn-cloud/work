# -*- coding: utf-8 -*-
"""MODごとの絵柄（2026-09-29）
・絵柄割当.csv（MODコード,絵柄,メモ）で MOD ごとに絵柄LoRAを決める。絵柄が空のMODは今の model.json のまま。
・絵柄の中身（LoRA ファイル・強さ・トリガー）は gen.py の STYLE_CANDS（絵柄比較と同じ）＋ model.json の "mod_style"."styles" で上書き。
・主人公LoRAも絵柄ごと：sdduel_hero_xl_<絵柄>-000008.safetensors（Lora用\\hero\\S1〜S3 で作る）。
  まだ無い絵柄は主人公LoRAなしで撮る（別の絵柄の主人公LoRAは混ぜない＝絵柄がずれるため）。
・出力は ComfyUI\\output\\<MOD>_WAI_<絵柄>\\（今までの <MOD>_WAI\\ とは別フォルダ。撮り済み判定も別）。
gen.py・collect.py・make_hero_ds_xl.py から使う。"""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "絵柄割当.csv")
LORA_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "ComfyUI_windows_portable", "ComfyUI", "models", "loras")
SKIP = {"1_現行", "2_絵柄なし"}   # 比較用の条件（MOD には割り当てない）

DEFAULT_CFG = {
    "hero_lora": "sdduel_hero_xl_{style}-000008.safetensors",
    "hero_trigger": "sdduel_hero",
    "hero_strength": 0.8,
    "hero_scene_strength": 0.5,
    # 2026-09-30 ユーザー決定：2人の場面は女性キャラが主役・主人公は投影用 → 場面だけ別のエポック（浅め）の主人公LoRAを使える。
    # 空＝hero_lora と同じ。{style} は絵柄名。ファイルが無ければ hero_lora を使う
    "hero_scene_lora": "",   # 2026-09-29 ユーザー決定：イベント（2人の場面）でも主人公LoRAを入れる（既定0.5・場面の強さ比較.bat で調整）
    "styles": {},
    # ランダム割当（--random-style）で選ばない絵柄。本編v2強＝本編v2の強さ違い／matureBody＝絵柄ではなく体型LoRA／DHIBI＝白黒漫画
    "random_exclude": ["本編v2強", "matureBody", "DHIBI"],
    "random_hero_only": False,   # true＝主人公LoRA（絵柄別）がある絵柄だけから選ぶ
    # 敵キャラLoRA（2026-09-29）：イベント（2人の場面）だけに、その場面の相手（master／e1〜e3／boss）のLoRAを入れる。
    # 立ち絵は絵柄LoRAだけ（キャラLoRAは入れない）。ファイルが無いキャラは入れない。
    "chara_lora": "キャラ\\chr_{mod}_{char}_{style}-000008.safetensors",
    "chara_trigger": "chr_{mod}_{char}",
    "chara_scene_strength": 0.6,
    "chara_enabled": True,
}
CHARS = ["master", "e1", "e2", "e3", "boss"]


def cfg():
    c = json.loads(json.dumps(DEFAULT_CFG))
    try:
        mj = json.load(open(os.path.join(HERE, "model.json"), encoding="utf-8"))
        if isinstance(mj.get("mod_style"), dict):
            c.update(mj["mod_style"])
    except Exception:
        pass
    return c


def name_of(cond):
    """"3_ATRex" → "ATRex\""""
    return re.sub(r"^\d+_", "", cond)


def presets(style_cands):
    """{絵柄名: {"name","lora","strength","trigger","hero_lora","hero_strength","hero_scene_strength","hero_ok"}}"""
    c = cfg()
    out = {}
    for cond, f, st, trg in style_cands:
        if cond in SKIP or not f:
            continue
        out[name_of(cond)] = {"name": name_of(cond), "lora": f, "strength": st, "trigger": trg}
    for k, v in (c.get("styles") or {}).items():   # model.json で上書き・追加
        if isinstance(v, dict):
            out.setdefault(k, {"name": k, "lora": "", "strength": 0.6, "trigger": ""})
            if "lora" in v: out[k]["lora"] = v["lora"]
            for x in ("strength", "trigger", "hero_lora", "hero_strength", "hero_scene_strength", "hero_scene_lora"):
                if x in v: out[k][x] = v[x]
    for k, p in out.items():
        p.setdefault("hero_lora", c["hero_lora"].replace("{style}", k))
        p.setdefault("hero_strength", c["hero_strength"])
        p.setdefault("hero_scene_strength", c["hero_scene_strength"])
        p["hero_trigger"] = c.get("hero_trigger", "sdduel_hero")
        p["hero_ok"] = bool(p["hero_lora"]) and os.path.isfile(os.path.join(LORA_DIR, p["hero_lora"]))
        p.setdefault("hero_scene_lora", (c.get("hero_scene_lora") or "").replace("{style}", k))
        p["hero_scene_ok"] = bool(p["hero_scene_lora"]) and os.path.isfile(os.path.join(LORA_DIR, p["hero_scene_lora"]))
    return out


def read_csv():
    """{MODコード: 絵柄名}（絵柄が空の行は入れない）"""
    res = {}
    if not os.path.isfile(CSV_PATH):
        return res
    for enc in ("utf-8-sig", "cp932"):
        try:
            rows = list(csv.reader(open(CSV_PATH, encoding=enc, newline="")))
            break
        except UnicodeDecodeError:
            continue
    else:
        return res
    for r in rows[1:]:
        if len(r) >= 2 and r[0].strip() and not r[0].strip().startswith("#") and r[1].strip():
            res[r[0].strip()] = r[1].strip()
    return res


def random_assign(mods, assign, pres, mode="blank", rng=None):
    """MODに絵柄をランダムに割り当てる（2026-09-29）。mode: blank＝空欄のMODだけ／all＝全部振り直す。
    なるべく同じ絵柄が偏らないよう、今使われている数が少ない絵柄から選ぶ。戻り値 (新しい割当, {MOD: 絵柄} 今回決めた分)"""
    import random as _r
    rng = rng or _r.Random()
    c = cfg()
    ex = set(c.get("random_exclude") or [])
    pool = [k for k, p in pres.items() if k not in ex and (p["hero_ok"] or not c.get("random_hero_only"))]
    if not pool:
        raise ValueError("ランダムで選べる絵柄がありません（model.json の mod_style.random_exclude / random_hero_only を確認）")
    new = dict(assign)
    targets = [m for m in mods if mode == "all" or not new.get(m)]
    for m in targets:
        new.pop(m, None)
    count = {k: 0 for k in pool}
    for v in new.values():
        if v in count:
            count[v] += 1
    rng.shuffle(targets)
    picked = {}
    for m in targets:
        low = min(count.values())
        st = rng.choice([k for k in pool if count[k] == low])
        count[st] += 1
        new[m] = picked[m] = st
    return new, picked


def write_csv(mods, keep=None, memo_add=None):
    """絵柄割当.csv を作る（既にある割当は残す）。Excel で開けるよう UTF-8（BOM付き）"""
    keep = keep if keep is not None else read_csv()
    memo = {}
    if os.path.isfile(CSV_PATH):
        try:
            for r in list(csv.reader(open(CSV_PATH, encoding="utf-8-sig", newline="")))[1:]:
                if len(r) >= 3:
                    memo[r[0].strip()] = r[2]
        except Exception:
            pass
    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["MODコード", "絵柄", "メモ"])
        for m in mods:
            w.writerow([m, keep.get(m, ""), (memo_add or {}).get(m, memo.get(m, ""))])


def suffix(style_name):
    return ("_" + style_name) if style_name else ""


def style_for(mod, assign, pres, force=None):
    """MOD の絵柄（preset dict）。force＝--style で全MOD一時的に。"本編"／空＝None（今の model.json のまま）"""
    s = force if force is not None else assign.get(mod, "")
    if not s or s in ("本編", "標準", "none"):
        return None
    if s not in pres:
        raise KeyError(s)
    return pres[s]


def chara_of(name):
    """画像名から、その絵の相手キャラ（master／e1〜e3／boss）を返す。立ち絵・魔法・背景などは None。
    例 Lamia_atk_m1→master、Lamia_lose_btl_e2→e2、Lamia_atk_boss→boss、Lamia_master→None（立ち絵）"""
    parts = name.split("_")
    if len(parts) == 2 and parts[1] in CHARS:   # 2026-10-02 立ち絵（Lamia_master・Lamia_e1 等）。使うのは chara_map の LoRA だけ
        return parts[1]
    if len(parts) < 3 or parts[1] not in ("atk", "lose", "onanie"):
        return None
    last = parts[-1]
    if re.fullmatch(r"m\d*|master", last):
        return "master"
    if re.fullmatch(r"e\d", last) or last == "boss":
        return last
    return None


def chara_trigger(mod, char):
    return cfg()["chara_trigger"].replace("{mod}", mod).replace("{char}", char).lower()


def chara_lora(mod, char, style):
    """{"lora_name","strength","trigger","ok"}。style は preset（None なら絵柄なし＝'std'）
    2026-10-02：model.json mod_style.chara_map に当てたキャラLoRA（ダウンロードしたもの）があればそれを優先（立ち絵にも使う）"""
    c = cfg()
    e = chara_map_entry(mod, char)
    if e:
        f = e["lora"]
        st = float(e.get("strength", c.get("chara_map_strength", 0.8)))
        return {"lora_name": f, "strength": st, "scene_strength": float(e.get("scene_strength", c.get("chara_map_scene_strength", st))),
                "trigger": e.get("trigger", ""), "stand": True, "mapped": True,
                "ok": bool(c.get("chara_enabled", True)) and os.path.isfile(os.path.join(LORA_DIR, *re.split(r"[\\\\/]", f)))}
    sname = style["name"] if style else "std"
    f = c["chara_lora"].replace("{mod}", mod).replace("{char}", char).replace("{style}", sname)
    ov = ((style or {}).get("chara") or {}) if isinstance(style, dict) else {}
    return {"lora_name": f, "strength": float(c.get("chara_scene_strength", 0.6)), "trigger": chara_trigger(mod, char),
            "ok": bool(c.get("chara_enabled", True)) and os.path.isfile(os.path.join(LORA_DIR, *re.split(r"[\\\\/]", f)))}


# ---- ダウンロードしたキャラLoRAを MOD の敵キャラに当てる（2026-10-02） ----
# model.json mod_style.chara_map = {"<MOD>": {"<master|e1|e2|e3|boss>": {"lora": "キャラ\\xxx.safetensors", "trigger": "...",
#   "strength": 立ち絵の強さ, "scene_strength": 場面の強さ, "replace": [["元の文字列", "置き換え"], ...], "memo": "..."}}}
# replace は prompts を読み込んだ直後にそのMODの全画像の positive に当てる（見た目の文字をキャラLoRAのキャラに合わせる）。prompts\*.json は書き換えない。
def chara_map_entry(mod, char):
    m = (cfg().get("chara_map") or {}).get(mod) or {}
    e = m.get(char) if char else None
    if isinstance(e, dict) and e.get("lora") and e.get("enabled", True) is not False:
        return e
    return None


def apply_chara_map(mod, P):
    m = (cfg().get("chara_map") or {}).get(mod) or {}
    pairs = []
    for ch in CHARS:
        e = chara_map_entry(mod, ch)
        if e:
            pairs += [(a, b) for a, b in (e.get("replace") or []) if a]
    if not pairs:
        return P
    out = {}
    for n, e in P.items():
        e = dict(e)
        s = e.get("positive", "")
        for a, b in pairs:
            s = s.replace(a, b)
        e["positive"] = s
        out[n] = e
    return out
