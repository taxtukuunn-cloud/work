# -*- coding: utf-8 -*-
"""まとめツール：構図の元絵と下書きの画面（2026-10-05・段階A）
画面は 構図.html（ui.html の「④ 構図の元絵と下書き」タブの中に出る）。app.py から呼ばれる。
・A1 採用（見本つき）／A6 項目をつなげて構図名／A2 新しい構図／A3 範囲の確認／A4 当たり具合／A7 MODごとの割り当て／A5 判定のメモ
・画像生成フォルダの gen.py などは書き換えない。読むだけ。重い処理は今ある道具を呼ぶだけ（撮影中は押せない）
・書くファイル：_候補\\_採用.csv（採用・備考の欄）／構図下書き\\_人物の範囲.csv（直す の欄）／新しい表（語の一覧・項目対応・判定メモ など）
  model.json は「下書きを外す」「控えから戻す」のときだけ、控えを取ってから pose_control の中だけを書き換える（年齢に関わる設定には触れない）
・--test で起動したときは、書き込みを まとめツール\\_試し\\ の写しに向ける（本物の表と model.json は変えない）"""
import csv, hashlib, io, json, os, re, shutil, subprocess, sys, threading, time, zipfile

A = None          # app モジュール
TEST = False
LOCK = threading.RLock()


def init(app, test=False):
    global A, TEST
    A, TEST = app, bool(test)
    threading.Thread(target=_proc_loop, daemon=True).start()
    try:
        snap_preview()
    except Exception as ex:
        A.log("[構図の画面] 下見の控えを取れませんでした: %s" % ex)


# ---------------------------------------------------------------- 場所
def IMG():
    return A.P_img()


def PICK():
    return os.path.join(IMG(), "構図下書き元")


def CAND():
    return os.path.join(PICK(), "_候補")


def DRAFT():
    return os.path.join(IMG(), "構図下書き")


def CIN():
    return os.path.join(A.CONF["comfy_dir"], "ComfyUI", "input")


def BAK():
    return os.path.join(IMG(), "_控え")


def REC():
    return os.path.join(A.HERE, "記録")


def CACHE():
    return os.path.join(A.HERE, "_cache", "構図")


def TEST_DIR():
    return os.path.join(A.HERE, "_試し")


P_PICK_CSV = lambda: os.path.join(CAND(), "_採用.csv")
P_LIST_CSV = lambda: os.path.join(CAND(), "_候補一覧.csv")
P_NEW_CSV = lambda: os.path.join(CAND(), "_新しい構図.csv")
P_REGION_CSV = lambda: os.path.join(DRAFT(), "_人物の範囲.csv")
P_WORDS = lambda: os.path.join(DRAFT(), "構図名_語の一覧.csv")
P_ITEMS = lambda: os.path.join(DRAFT(), "構図名_項目対応.csv")
P_MEMO = lambda: os.path.join(DRAFT(), "_判定メモ.csv")
P_MANUAL = lambda: os.path.join(DRAFT(), "_手の範囲.json")
P_MODEL = lambda: os.path.join(IMG(), "model.json")
P_PREVIEW = lambda: os.path.join(IMG(), "下見_全場面.csv")
P_PREVIEW_MOD = lambda: os.path.join(IMG(), "下見_MOD別.csv")
P_POSE_REPORT = lambda: os.path.join(IMG(), "構図LoRA_割当.csv")
P_RESHOOT = lambda: os.path.join(REC(), "撮り直しの予定.csv")
P_TEXTFIX = lambda: os.path.join(REC(), "本文を直す候補.csv")
P_MODEL_LOG = lambda: os.path.join(REC(), "model変更記録.txt")
P_SNAP = lambda: os.path.join(REC(), "下見の控え")


def tpath(p):
    """--test のときの写しの場所（MOD のフォルダからの相対の場所を _試し の下に）"""
    root = os.path.normpath(A.CONF["mod_root"])
    p = os.path.normpath(p)
    rel = os.path.relpath(p, root) if p.lower().startswith(root.lower() + os.sep) else os.path.join("_外", os.path.basename(p))
    return os.path.join(TEST_DIR(), rel)


def rpath(p):
    if TEST:
        t = tpath(p)
        if os.path.exists(t):
            return t
    return p


def wpath(p):
    if TEST:
        t = tpath(p)
        os.makedirs(os.path.dirname(t), exist_ok=True)
        if not os.path.exists(t) and os.path.exists(p):
            shutil.copy2(p, t)
        return t
    return p


# ---------------------------------------------------------------- 表（csv は道具の中だけで使う）
def read_csv(p):
    p = rpath(p)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig", newline="") as f:
        return [r for r in csv.reader(f)]


def read_dicts(p):
    rows = read_csv(p)
    if not rows:
        return [], []
    head = rows[0]
    out = []
    for r in rows[1:]:
        if not any(x.strip() for x in r):
            continue
        r = r + [""] * (len(head) - len(r))
        out.append(dict(zip(head, r)))
    return head, out


_LAST_BAK = {}


def backup_data(p, why):
    """今ある表を書き換える前に 画像生成\\_控え に控えを取る（同じ表は30分に1回まで）"""
    if TEST or not os.path.exists(p):
        return
    if time.time() - _LAST_BAK.get(p, 0) < 1800:
        return
    os.makedirs(BAK(), exist_ok=True)
    b, e = os.path.splitext(os.path.basename(p))
    dst = os.path.join(BAK(), "%s_%s_%s前%s" % (b, time.strftime("%Y%m%d_%H%M"), why, e))
    shutil.copy2(p, dst)
    _LAST_BAK[p] = time.time()


def write_csv(p, rows, backup=None):
    with LOCK:
        if backup:
            backup_data(p, backup)
        w = wpath(p)
        tmp = w + ".tmp"
        with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerows(rows)
        os.replace(tmp, w)


def write_dicts(p, head, rows, backup=None):
    write_csv(p, [head] + [[r.get(h, "") for h in head] for r in rows], backup)


def append_dict(p, head, row):
    with LOCK:
        h, rows = read_dicts(p)
        if not h:
            h = head
        for k in head:
            if k not in h:
                h.append(k)
        rows.append(row)
        write_dicts(p, h, rows)


def now():
    return time.strftime("%Y-%m-%d %H:%M")


def truthy(v):
    if isinstance(v, str):
        return v.strip().lower() in ("true", "1", "yes", "y")
    return bool(v)


# ---------------------------------------------------------------- 撮影中かどうか
_PROC = {"t": 0, "names": []}
WATCH = ("gen.py", "make_region_masks.py", "depth_from_ref.py", "adopt_ref.py", "make_pose_ref.py", "import_pose_ref.py")


def _proc_loop():
    while True:
        try:
            if os.name == "nt":
                cmd = ["powershell", "-NoProfile", "-NonInteractive", "-Command",
                       "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | ForEach-Object { $_.CommandLine }"]
                r = subprocess.run(cmd, capture_output=True, timeout=30, creationflags=0x08000000)
                try:
                    txt = (r.stdout or b"").decode("utf-8")
                except UnicodeDecodeError:
                    txt = r.stdout.decode("cp932", "replace")
                found = sorted({w for line in txt.splitlines() for w in WATCH if re.search(r"(^|[\\/\s\"])%s(\s|\"|$)" % re.escape(w), line)})
                _PROC.update(t=time.time(), names=found)
        except Exception:
            pass
        time.sleep(15)


def busy():
    """撮影や下書きづくりが動いていれば、その理由のリスト（空なら動いていない）"""
    out = []
    j = A.JOBS.state()
    if j["running"]:
        out.append("このツールで作業中：" + j["title"] + ("（このあと %d 件）" % j["waiting_n"] if j["waiting_n"] else ""))
    c = A.comfy_state()
    if c["running"] + c["pending"]:
        out.append("ComfyUI が撮影中（残り %d 枚）" % (c["running"] + c["pending"]))
    if _PROC["names"]:
        out.append("処理が動いています：" + "・".join(_PROC["names"]))
    return out


def need_idle(what):
    b = busy()
    if b and not TEST:
        raise RuntimeError("撮影や下書きづくりが動いているので、%sはできません（%s）。撮影が終わってから押してください。" % (what, " ／ ".join(b)))


def add_job(title, argv, rec=None):
    if TEST:
        raise RuntimeError("試しの起動（--test）では作業を動かしません：" + title)
    A.JOBS.add(title, argv, IMG(), rec=rec)


# ---------------------------------------------------------------- model.json（読む）
_MJ = {"mt": None, "d": {}}


def model():
    p = rpath(P_MODEL())
    mt = os.path.getmtime(p)
    if _MJ["mt"] != (p, mt):
        _MJ["d"] = json.load(open(p, encoding="utf-8"))
        _MJ["mt"] = (p, mt)
    return _MJ["d"]


def pc():
    return model().get("pose_control") or {}


def registered():
    out = {}
    for s, rows in (pc().get("ref_sets") or {}).items():
        for r in rows or []:
            for c in r.get("comps") or []:
                out.setdefault(c, [])
                lab = s + ("（予備）" if r.get("default") else "")
                if lab not in out[c]:
                    out[c].append(lab)
    return out


def src_names():
    try:
        return sorted(f[:-4] for f in os.listdir(PICK()) if f.lower().endswith(".png"))
    except OSError:
        return []


_AC = {"k": None, "v": set()}


def all_comps():
    try:
        k = (os.path.getmtime(PICK()), os.path.getmtime(rpath(P_MODEL())))
    except OSError:
        k = None
    if _AC["k"] != k or k is None:
        _AC.update(k=k, v=set(registered()) | {re.sub(r"_\d+$", "", x) for x in src_names()})
    return _AC["v"]


def comp_of(draft, comps=None):
    """下書き名（depthref_xxx_2）や元絵名（xxx_2）→ 構図名"""
    n = draft[9:] if draft.startswith("depthref_") else draft
    comps = comps if comps is not None else all_comps()
    if n in comps and not re.search(r"_\d+$", n):
        return n
    m = re.match(r"^(.+?)_(\d+)$", n)
    if m and m.group(1) in comps:
        return m.group(1)
    return n if n in comps else (m.group(1) if m else n)


def comp_drafts():
    """{構図名: [元絵名…]}（構図下書き元の png から）"""
    out = {}
    for n in src_names():
        out.setdefault(re.sub(r"_\d+$", "", n), []).append(n)
    return out


# ---------------------------------------------------------------- 語の一覧・項目対応（A6）
WORD_HEAD = ["項目", "英字", "日本語", "選択肢に出す", "まとめる先", "メモ"]
ITEM_KEYS = ["人数", "技", "姿勢", "視点", "位置"]
ITEM_HEAD = ["構図名", "人数", "技", "姿勢", "視点", "位置", "同時の技", "作り方", "メモ"]
SEED = """人数,two,相手2人,○,,
人数,three,相手3人,○,,
人数,multi,相手が複数,,,古い名前の語
技,kiss,キス,○,,
技,hj,手,○,,
技,foot,足,○,,
技,nipple,乳首,○,,
技,ear,耳,○,,
技,whisper,ささやき,○,,
技,finger,指・前立腺,○,,
技,peg,ペニバン・逆アナル,○,,
技,urethra,尿道,○,,
技,chastity,貞操帯,○,,
技,armpit,脇,○,,
技,thigh,太もも,○,,
技,chest,胸に顔,○,,
技,drain,精気を吸う,○,,
技,bloodsuck,吸血,○,,
技,bound,拘束,○,,
技,straddle,またがる,○,,
技,hug,抱く,○,,
技,facesit,顔に座る,○,,
技,smother,顔をうずめる,○,,
技,paizuri,胸で挟む,○,,
技,lick,舐める,○,,
技,rimjob,お尻を舐める,○,,
技,rusty,お尻を舐めながら手,○,,
技,rah,後ろから手を回す,○,,
技,buttjob,お尻でこする,○,,
技,hairjob,髪でこする,○,,
技,step,踏む,○,,
技,collar,首輪,○,,
技,headlock,頭を抱え込む,○,,
技,oral,口,○,,
技,chin,あごを持ち上げる,○,,
技,press,押しつける,○,,
技,milking,しぼる,○,,
技,nursing,授乳の形,○,,
技,coil,巻きつく,○,,
技,handjob,手,,hj,
技,footjob,足,,foot,
技,ashikoki,足,,foot,
技,fingering,指,,finger,
技,prostate,前立腺,,finger,
技,strapon,ペニバン,,peg,
技,bondage,拘束,,bound,
技,embrace,抱き合う,,hug,
技,chesthug,胸に抱く,,chest,
技,bust,胸,,chest,
技,energy,精気,,drain,
技,anilingus,お尻を舐める,,rimjob,
技,ears,耳,,ear,
技,futadom,ふたなり責め,,,
技,job,こする,,,
技,pinch,つまむ,,,
技,toes,足の指,,,
姿勢,lie,寝る,○,,
姿勢,prone,うつ伏せ,○,,
姿勢,sit,座る,○,,
姿勢,stand,立つ,○,,
姿勢,bent,前かがみ,○,,
姿勢,fours,四つんばい,○,,
姿勢,kneel,ひざまずく,○,,
姿勢,hang,吊り,○,,
姿勢,lying,寝る,,lie,
姿勢,seated,座る,,sit,
姿勢,sitting,座る,,sit,
姿勢,standing,立つ,,stand,
姿勢,allfours,四つんばい,,fours,
姿勢,doggy,四つんばい,,fours,
姿勢,seiza,正座,,kneel,
姿勢,prostrate,ひれ伏す,,prone,
姿勢,suspension,吊り,,hang,
姿勢,inverted,逆さ,,hang,
姿勢,squat,しゃがむ,,,
姿勢,upright,体を起こす,,,
視点,pov,主人公目線,○,,
視点,side,横から,○,,
視点,front,前から,○,,
視点,behind,後ろから見る,○,,
視点,above,上から,○,,
視点,low,下から,○,,
視点,close,寄り,○,,
位置,on,上に乗る,○,,
位置,back,後ろから,○,,
位置,beside,横に並ぶ,○,,
位置,between,脚の間,○,,
位置,lap,膝の上,○,,
位置,sides,左右から,○,,
位置,sandwich,はさむ,○,,
位置,facing,向かい合う,○,,
位置,over,覆いかぶさる,○,,
位置,ontop,上に乗る,,on,
位置,top,上,,on,
位置,loom,覆いかぶさる,,over,
位置,spoon,横向きに寄り添う,,,
位置,reverse,逆向き,,,
位置,across,横切る,,,
そのほか,b,別の形b,,,同じ項目で形が違うとき
そのほか,c,別の形c,,,同じ項目で形が違うとき
そのほか,d,別の形d,,,同じ項目で形が違うとき
そのほか,alt,別の案,,,
そのほか,p,（意味を確かめる）,,,古い名前の語
そのほか,arachne,アラクネ,,,
そのほか,lamia,ラミア,,,
そのほか,succubus,サキュバス,,,
そのほか,machine,機械,,,
そのほか,tentacle,触手,,,
そのほか,tail,尻尾,,,
そのほか,bed,ベッド,,,
そのほか,bench,ベンチ,,,
そのほか,chair,椅子,,,
そのほか,desk,机,,,
そのほか,sofa,ソファ,,,
そのほか,throne,玉座,,,
そのほか,wall,壁,,,
そのほか,edge,ふち,,,
そのほか,pillow,枕,,,
そのほか,blindfold,目隠し,,,
そのほか,mask,マスク,,,
そのほか,leash,リード,,,
そのほか,rod,棒,,,
そのほか,toy,道具,,,
そのほか,clothed,服を着た,,,
そのほか,both,両方,,,
そのほか,cover,覆う,,,
そのほか,eyes,目,,,
そのほか,face,顔,,,
そのほか,head,頭,,,
そのほか,hands,両手,,,
そのほか,handhold,手をつなぐ,,,
そのほか,him,主人公を,,,
そのほか,hips,腰,,,
そのほか,hold,抱える,,,
そのほか,lean,もたれる,,,
そのほか,leg,脚,,,
そのほか,legs,脚,,,
そのほか,lift,持ち上げる,,,
そのほか,lookback,振り返る,,,
そのほか,neck,首,,,
そのほか,pin,押さえつける,,,
そのほか,ride,乗る,,,
そのほか,torso,胴,,,
そのほか,up,上げる,,,
そのほか,watch,見ている,,,
そのほか,wrap,巻きつく,,,
そのほか,xcross,X字のはりつけ,,,
そのほか,xray,断面の絵,,,
そのほか,figure,4の字,,,
そのほか,four,4の字,,,
そのほか,tongue,舌,,,
そのほか,drool,よだれ,,,
そのほか,futa,ふたなり,,,
そのほか,close,寄り,,close,"""


def words():
    head, rows = read_dicts(P_WORDS())
    if not rows:
        rows = [dict(zip(WORD_HEAD, r)) for r in csv.reader(io.StringIO(SEED)) if r]
        write_dicts(P_WORDS(), WORD_HEAD, rows)
    return rows


def word_map():
    """英字 → 語の行（最初に出てきたもの）"""
    out = {}
    for w in words():
        out.setdefault(w["英字"].strip(), w)
    return out


def canon(w):
    return (w.get("まとめる先") or "").strip() or w["英字"].strip()


def reading(name, wm=None):
    """構図名・下書き名の日本語の読み（「手・立つ・横から」）"""
    wm = wm or word_map()
    n = name[9:] if name.startswith("depthref_") else name
    if n.startswith("depth3d_"):
        return "3Dの下書き：" + reading(n[8:], wm)
    toks = n.split("_")
    num = ""
    if len(toks) > 1 and toks[-1].isdigit():
        num = toks.pop()
    out = []
    for t in toks:
        w = wm.get(t)
        out.append(w["日本語"] if w and w["日本語"] else "（%s）" % t)
    s = "・".join(out)
    return s + ("（%s枚目）" % num if num else "")


VIEW_FROM_TAGS = [("pov", r"\bpov\b"), ("side", r"from side"), ("front", r"from front"), ("behind", r"from behind"),
                  ("above", r"from above|high angle"), ("low", r"from below|low angle")]


def auto_items(comp, wm):
    P = pc()
    toks = [t for t in comp.split("_") if t]
    it = {k: "" for k in ITEM_KEYS + ["同時の技"]}
    rest = []
    techs = []
    for t in toks:
        w = wm.get(t)
        if not w:
            rest.append(t)
            continue
        cat, cv = w["項目"], canon(w)
        if cat == "技":
            if cv not in techs:
                techs.append(cv)
        elif cat == "人数":
            if not it["人数"] and cv in ("two", "three"):
                it["人数"] = cv
        elif cat in ("姿勢", "視点", "位置"):
            if not it[cat]:
                it[cat] = cv
        else:
            rest.append(t)
    if techs:
        it["技"] = techs[0]
        if len(techs) > 1:
            it["同時の技"] = techs[1]
    if not it["姿勢"]:
        it["姿勢"] = (P.get("ref_posture") or {}).get(comp, "")
    if not it["視点"]:
        tg = (P.get("ref_tags") or {}).get(comp, "")
        for k, rx in VIEW_FROM_TAGS:
            if re.search(rx, tg):
                it["視点"] = k
                break
    memo = ("名前のほかの語：" + "・".join(rest)) if rest else ""
    return it, memo


def items_table():
    """構図名_項目対応.csv（無ければ作る。新しい構図が増えたら機械で行を足す）"""
    with LOCK:
        head, rows = read_dicts(P_ITEMS())
        have = {r["構図名"] for r in rows}
        allc = sorted(set(registered()) | set(comp_drafts()))
        wm = word_map()
        add = []
        for c in allc:
            if c not in have:
                it, memo = auto_items(c, wm)
                r = dict(構図名=c, 作り方="機械", メモ=memo, **it)
                add.append(r)
        if add or not head:
            rows += add
            rows.sort(key=lambda r: r["構図名"])
            write_dicts(P_ITEMS(), ITEM_HEAD, rows)
        return rows


def next_variant(base, taken):
    for ch in "bcdefghijklmnopqrstuvwxyz":
        n = "%s_%s" % (base, ch)
        if n not in taken:
            return n
    return base + "_z"


# ---------------------------------------------------------------- 候補（A1・A2）
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp")
PFX_RE = re.compile(r"^([a-z])(\d+)_", re.I)
_SIZE = {}


def img_size(p):
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return ""
    k = _SIZE.get(p)
    if k and k[0] == mt:
        return k[1]
    try:
        from PIL import Image
        with Image.open(p) as im:
            s = "%dx%d" % im.size
    except Exception:
        s = ""
    _SIZE[p] = (mt, s)
    return s


def pick_rows():
    rows = read_csv(P_PICK_CSV())
    if not rows:
        rows = [["番号", "ファイル名", "採用", "備考", "取り込んだ名前", "切り抜き"]]
    head = rows[0]
    for col in ("番号", "ファイル名", "採用", "備考", "取り込んだ名前", "切り抜き"):
        if col not in head:
            head.append(col)
    for r in rows[1:]:
        r += [""] * (len(head) - len(r))
    return rows


def candidates():
    rows = pick_rows()
    head = rows[0]
    H = {h: i for i, h in enumerate(head)}
    by = {}
    for r in rows[1:]:
        if len(r) > H["ファイル名"] and r[H["ファイル名"]].strip():
            by[r[H["ファイル名"]]] = r
    newm = {r["ファイル名"]: r for r in read_dicts(P_NEW_CSV())[1]}
    out = []
    for where, d in (("候補", CAND()), ("見送り", os.path.join(CAND(), "_見送り"))):
        fs = []
        for dd in ([d, tpath(d)] if TEST else [d]):   # 試しの起動では、切り抜いた写し（_試し の中）も出す
            try:
                fs += [f for f in os.listdir(dd) if os.path.isfile(os.path.join(dd, f)) and f.lower().endswith(IMG_EXT) and f not in fs]
            except OSError:
                pass
        fs.sort()
        for f in fs:
            fp = os.path.join(d, f) if os.path.exists(os.path.join(d, f)) else os.path.join(tpath(d), f)
            r = by.get(f)
            m = PFX_RE.match(f)
            num = (r[H["番号"]] if r else "") or (m.group(1).lower() + m.group(2) if m else "")
            pick = (r[H["採用"]].strip() if r else "")
            done = (r[H["取り込んだ名前"]].strip() if r else "")
            if done:
                st = "取り込み済み"
            elif pick == "見送り" or where == "見送り":
                st = "見送り"
            elif pick:
                st = "採用（取り込み待ち）"
            elif f in newm:
                st = "新しい構図"
            else:
                st = "未定"
            out.append(dict(file=f, where=where, num=num, row=bool(r), pick=pick, note=(r[H["備考"]] if r else ""),
                            done=done, crop=(r[H["切り抜き"]] if r else ""), state=st, new=f in newm,
                            new_name=(newm.get(f) or {}).get("仮の名前", ""), mt=int(os.path.getmtime(fp))))
    return out


def cand_path(f, where="候補"):
    if not f or "/" in f or "\\" in f or f.startswith(".."):
        raise RuntimeError("名前が違います")
    d = CAND() if where == "候補" else os.path.join(CAND(), "_見送り")
    p = os.path.join(d, f)
    if TEST and not os.path.isfile(p):
        p = os.path.join(tpath(d), f)
    if not os.path.isfile(p):
        raise RuntimeError("その絵はありません: " + f)
    return p


def set_pick(b):
    """_採用.csv の「採用」「備考」を書く（取り込み済みの行は変えない）"""
    f = b.get("file", "")
    cand_path(f, b.get("where", "候補"))
    val = (b.get("pick") or "").strip()
    if val not in ("", "見送り") and not re.match(r"^[a-z0-9_]+$", val):
        raise RuntimeError("構図名は 英小文字・数字・_ だけにしてください：" + val)
    with LOCK:
        rows = pick_rows()
        head = rows[0]
        H = {h: i for i, h in enumerate(head)}
        row = next((r for r in rows[1:] if r[H["ファイル名"]] == f), None)
        if row and row[H["取り込んだ名前"]].strip():
            raise RuntimeError("この絵はもう取り込み済みです（%s）。変えられません。" % row[H["取り込んだ名前"]])
        if row is None:
            m = PFX_RE.match(f)
            row = [""] * len(head)
            row[H["番号"]] = b.get("num") or (m.group(1).lower() + m.group(2) if m else "")
            row[H["ファイル名"]] = f
            rows.append(row)
        row[H["採用"]] = val
        if "note" in b:
            row[H["備考"]] = (b.get("note") or "").replace("\n", " ").strip()
        write_csv(P_PICK_CSV(), rows, backup="採用_画面から直す")
    if b.get("memo_kind"):
        add_memo(b["memo_kind"], f, val or "未定に戻す", b.get("note", ""))
    # 新しい構図の印は、構図名が決まったら外す（見送りでも外す）
    if val and not b.get("keep_new"):
        set_new({"file": f, "on": False})
    if val and val != "見送り" and b.get("items"):
        save_items_row(val, b["items"], "採用画面")
    return "書きました：%s → %s" % (f, val or "未定")


def set_new(b):
    """A2：「新しい構図」の印（_候補\\_新しい構図.csv）"""
    f = b.get("file", "")
    head = ["番号", "ファイル名", "仮の名前", "メモ", "日時"]
    with LOCK:
        h, rows = read_dicts(P_NEW_CSV())
        rows = [r for r in rows if r.get("ファイル名") != f]
        if b.get("on"):
            m = PFX_RE.match(f)
            rows.append(dict(番号=b.get("num") or (m.group(1).lower() + m.group(2) if m else ""), ファイル名=f,
                             仮の名前=(b.get("name") or "").strip(), メモ=(b.get("note") or "").strip(), 日時=now()))
        if rows or os.path.exists(rpath(P_NEW_CSV())):
            write_dicts(P_NEW_CSV(), head, rows)
    if b.get("on"):
        add_memo("新しい構図", f, b.get("name") or "", b.get("note", ""))
    return "新しい構図に%s：%s" % ("分けました" if b.get("on") else "入れていません", f)


def save_items_row(comp, items, how):
    with LOCK:
        rows = items_table()
        r = next((x for x in rows if x["構図名"] == comp), None)
        if r is None:
            r = dict(構図名=comp)
            rows.append(r)
        for k in ITEM_KEYS + ["同時の技"]:
            if k in items:
                r[k] = (items.get(k) or "").strip()
        r["作り方"] = how
        if "メモ" in items:
            r["メモ"] = items["メモ"]
        rows.sort(key=lambda x: x["構図名"])
        write_dicts(P_ITEMS(), ITEM_HEAD, rows)
    return "項目を書きました：" + comp


def crop_copy(b):
    """切り抜き・左右反転した写しを _候補 に新しい候補として保存し、_採用.csv に行を足す"""
    f = b.get("file", "")
    src = cand_path(f, b.get("where", "候補"))
    from PIL import Image
    im = Image.open(src).convert("RGB")
    W, H = im.size
    box = b.get("box")
    if box:
        l, t, r, btm = [int(round(float(x))) for x in box]
        l, t = max(0, min(W - 1, l)), max(0, min(H - 1, t))
        r, btm = max(l + 1, min(W, r)), max(t + 1, min(H, btm))
        if (r - l) < 64 or (btm - t) < 64:
            raise RuntimeError("切り抜く範囲が小さすぎます")
        im = im.crop((l, t, r, btm))
    if b.get("flip"):
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if not box and not b.get("flip"):
        raise RuntimeError("切り抜く範囲か左右反転を選んでください")
    stem = os.path.splitext(f)[0]
    what = ("切り抜き" if box else "") + ("反転" if b.get("flip") else "")
    k = 1
    while True:
        nf = "%s_%s%d.png" % (stem, what, k)
        if not os.path.exists(os.path.join(CAND(), nf)) and not os.path.exists(tpath(os.path.join(CAND(), nf))):
            break
        k += 1
    dst = wpath(os.path.join(CAND(), nf)) if TEST else os.path.join(CAND(), nf)
    im.save(dst)
    m = PFX_RE.match(f)
    num = (m.group(1).lower() + m.group(2) if m else "") + "-%s%d" % (what, k)
    with LOCK:
        rows = pick_rows()
        head = rows[0]
        Hh = {h: i for i, h in enumerate(head)}
        row = [""] * len(head)
        row[Hh["番号"]], row[Hh["ファイル名"]] = num, nf
        row[Hh["備考"]] = "%s を%s（%s）" % (f, "・".join(x for x in (("切り抜き %s" % box) if box else "", "左右反転" if b.get("flip") else "") if x), now())
        rows.append(row)
        write_csv(P_PICK_CSV(), rows, backup="採用_画面から直す")
    add_memo("切り抜き・反転", nf, what, "元：" + f)
    return {"ok": True, "msg": "写しを作りました：" + nf, "file": nf}


# ---------------------------------------------------------------- 判定のメモ（A5）
MEMO_HEAD = ["日時", "種類", "対象", "判定", "理由"]


def add_memo(kind, target, verdict, why):
    append_dict(P_MEMO(), MEMO_HEAD, dict(日時=now(), 種類=kind, 対象=target, 判定=verdict, 理由=(why or "").replace("\n", " ")))


# ---------------------------------------------------------------- 範囲（A3）
FIX_OPTS = ("入れ替え", "主人公なし", "使わない")


def manual_all():
    try:
        return json.load(open(rpath(P_MANUAL()), encoding="utf-8"))
    except Exception:
        return {}


def region_rows():
    head, rows = read_dicts(P_REGION_CSV())
    files = set(os.listdir(DRAFT())) if os.path.isdir(DRAFT()) else set()
    man = manual_all()
    reg = registered()
    ex = {x.lower() for x in pc().get("ref_exclude") or []}
    out = []
    for r in rows:
        n = r.get("元絵", "")
        res, fx = r.get("結果", ""), r.get("直す", "").strip()
        applied = res.endswith("（直す）")
        pend = (fx and not applied) or (not fx and applied) or (fx and applied and not res.startswith(fx) and not (fx == "使わない" and res.startswith("使わない")))
        hand = (man.get(n) or {}).get("shapes") or []
        if fx != "使わない":   # 手の範囲：囲んだのに作っていない／作った後に囲み直した／囲みを消したのに手の範囲のまま
            try:
                rmt = os.path.getmtime(os.path.join(DRAFT(), "region_%s_partner.png" % n))
            except OSError:
                rmt = 0
            if hand and (not res.startswith("手で指定") or float((man.get(n) or {}).get("updated", 0)) > rmt):
                pend = True
            if not hand and res.startswith("手で指定"):
                pend = True
        out.append(dict(name=n, faces=r.get("顔の数", ""), score=r.get("男らしさ", ""), result=res, fix=fx, pending=bool(pend), hand=len(hand),
                        hero=("region_%s_hero.png" % n) in files, partner=("region_%s_partner.png" % n) in files,
                        comp=comp_of(n), registered=comp_of(n) in reg, excluded=("depthref_" + n).lower() in ex))
    return out


def set_fix(b):
    names = b.get("names") or ([b["name"]] if b.get("name") else [])
    fx = (b.get("fix") or "").strip()
    if fx and fx not in FIX_OPTS:
        raise RuntimeError("直し方は %s のどれかです" % "・".join(FIX_OPTS))
    with LOCK:
        rows = read_csv(P_REGION_CSV())
        if not rows:
            raise RuntimeError("_人物の範囲.csv がありません")
        head = rows[0]
        if "直す" not in head:
            head.append("直す")
        ci = head.index("直す")
        n = 0
        for r in rows[1:]:
            if r and r[0] in names:
                r += [""] * (len(head) - len(r))
                r[ci] = fx
                n += 1
        write_csv(P_REGION_CSV(), rows, backup="人物の範囲_画面から直す")
    for nm in names:
        add_memo("範囲", nm, fx or "直しを消す", b.get("why", ""))
    return "「直す」を書きました（%d 枚）：%s" % (n, fx or "消す")


def manual_get(q):
    n = q.get("name", "")
    p = os.path.join(PICK(), n + ".png")
    if not _SAFE.match(n or "") or not os.path.isfile(p):
        raise RuntimeError("元絵がありません: " + n)
    from PIL import Image
    with Image.open(p) as im:
        w, h = im.size
    return dict(name=n, w=w, h=h, shapes=(manual_all().get(n) or {}).get("shapes") or [])


def manual_save(b):
    """B1：手で囲んだ範囲（主人公・相手1・相手2、四角か楕円）を 構図下書き の _手の範囲.json に書く。範囲の画像は「作り直す」で作る"""
    n = b.get("name", "")
    info = manual_get({"name": n})
    shapes = []
    for sh in b.get("shapes") or []:
        role, kind = sh.get("role"), sh.get("kind")
        if role not in ("hero", "partner1", "partner2") or kind not in ("rect", "ellipse"):
            raise RuntimeError("囲みの種類が違います")
        x0, y0, x1, y1 = [max(0.0, float(v)) for v in sh.get("box")]
        if abs(x1 - x0) < 8 or abs(y1 - y0) < 8:
            continue
        shapes.append(dict(role=role, kind=kind, box=[round(min(x0, x1)), round(min(y0, y1)), round(min(info["w"], max(x0, x1))), round(min(info["h"], max(y0, y1)))]))
    if shapes and not any(s["role"] != "hero" for s in shapes):
        raise RuntimeError("相手の範囲（相手1）を1つは囲んでください")
    if any(s["role"] == "partner2" for s in shapes) and not any(s["role"] == "partner1" for s in shapes):
        raise RuntimeError("相手2 だけでなく、相手1 も囲んでください")
    with LOCK:
        d = manual_all()
        if shapes:
            d[n] = dict(shapes=shapes, updated=time.time(), size=[info["w"], info["h"]], when=now())
        else:
            d.pop(n, None)
        backup_data(P_MANUAL(), "手の範囲_画面から直す")
        w = wpath(P_MANUAL())
        with open(w + ".tmp", "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        os.replace(w + ".tmp", w)
    add_memo("手の範囲", n, "囲む %d 個" % len(shapes) if shapes else "囲みを消す", b.get("why", ""))
    return "手の範囲を%s：%s（撮影していないときに「直した分の範囲を作り直す」を押すと絵に反映されます）" % ("保存しました" if shapes else "消しました", n)


def remake_regions(b):
    need_idle("範囲の作り直し")
    names = [r["name"] for r in region_rows() if r["pending"]]
    if not names:
        return "作り直す範囲はありません"
    add_job("人物の範囲を作り直す（直した %d 枚）" % len(names), [A.PY, "make_region_masks.py", "--only", ",".join(names)])
    return "並べました：人物の範囲を作り直す（%d 枚）" % len(names)


# ---------------------------------------------------------------- 下見（A4・A7）
_PV = {"k": None, "rows": {}, "mods": set()}


def preview():
    p = P_PREVIEW()
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return {}, set(), 0
    if _PV["k"] != mt:
        rows = {}
        for r in read_dicts(p)[1]:
            rows[(r["MOD"], r["画像名"])] = r
        _PV.update(k=mt, rows=rows, mods={k[0] for k in rows})
    return _PV["rows"], _PV["mods"], mt


def preview_age():
    _, mods, mt = preview()
    if not mt:
        return dict(time="", stale=True, why=["下見がまだありません"], mods=0)
    why = []
    try:
        if os.path.getmtime(rpath(P_MODEL())) > mt:
            why.append("model.json が下見より新しい")
    except OSError:
        pass
    try:
        newest = max((os.path.getmtime(os.path.join(CIN(), f)) for f in os.listdir(CIN()) if f.startswith("pose_depthref_")), default=0)
        if newest > mt:
            why.append("下書きか範囲が下見より新しい")
    except OSError:
        pass
    try:
        allc = [f[:-5] for f in os.listdir(os.path.join(IMG(), "prompts")) if f.endswith(".json")]
        miss = [c for c in allc if c not in mods]
        if miss:
            why.append("下見に入っていないMODが %d 個" % len(miss))
    except OSError:
        pass
    return dict(time=time.strftime("%Y-%m-%d %H:%M", time.localtime(mt)), stale=bool(why), why=why, mods=len(mods))


def snap_preview():
    p = P_PREVIEW()
    if TEST or not os.path.exists(p):   # 試しの起動では控えを作らない
        return
    os.makedirs(P_SNAP(), exist_ok=True)
    dst = os.path.join(P_SNAP(), "下見_全場面_%s.csv" % time.strftime("%Y%m%d_%H%M%S", time.localtime(os.path.getmtime(p))))
    if not os.path.exists(dst):
        shutil.copy2(p, dst)


def prev_snapshot():
    """今の下見より前の下見（記録\\下見の控え の、今のより古い中で一番新しいもの）"""
    _, _, mt = preview()
    try:
        fs = sorted(f for f in os.listdir(P_SNAP()) if f.startswith("下見_全場面_") and f.endswith(".csv"))
    except OSError:
        return None, ""
    cur = "下見_全場面_%s.csv" % time.strftime("%Y%m%d_%H%M%S", time.localtime(mt)) if mt else ""
    older = [f for f in fs if f < cur]
    if not older:
        return None, ""
    f = older[-1]
    rows = {}
    with open(os.path.join(P_SNAP(), f), encoding="utf-8-sig", newline="") as fp:
        for r in csv.DictReader(fp):
            rows[(r["MOD"], r["画像名"])] = r
    return rows, f[len("下見_全場面_"):-4]


def queue_preview_after(what):
    """model.json を書き換えた後に下見を並べる（試しの起動では並べない）。並べたら文を返す"""
    if TEST:
        return "（試しの起動なので下見は並べません）"
    try:
        snap_preview()
        add_job("下見（%sの後）" % what, [A.PY, "gen.py", "all", "all", "--model", "wai", "--preview"])
        return "下見を並べました（数分）。終わったら「当たり具合」で割り当てが動いた場面を確かめてください。"
    except Exception as ex:
        return "下見を並べられませんでした（%s）。「当たり具合」の「下見をやり直す」を押してください。" % ex


def run_preview(b):
    need_idle("下見")
    snap_preview()
    add_job("下見（全MODの全場面を撮らずに点検）", [A.PY, "gen.py", "all", "all", "--model", "wai", "--preview"])
    return "並べました：下見（数分かかります。終わったらこの画面を開き直すと新しい結果が出ます）"


def run_pose_report(b):
    need_idle("構図LoRAの割当づくり")
    add_job("構図LoRAの割当を書き出す", [A.PY, "gen.py", "all", "all", "--model", "wai", "--pose-report"])
    return "並べました：構図LoRAの割当"


# ---------------------------------------------------------------- 場面の読み取り（A7）
POSTURE_JA = {"fours": "四つんばい", "lie": "寝る", "kneel": "ひざまずく", "sit": "座る", "stand": "立つ"}
TECH_JA = {"kiss": "キス", "close_hug": "抱きしめ", "fingering": "指", "peg": "ペニバン", "peg_nipple": "ペニバン＋乳首", "prostate": "前立腺",
           "footjob": "足", "handjob": "手", "bondage": "拘束", "bloodsuck": "吸血", "ctl_nipple": "乳首", "ctl_straddle": "またがる",
           "ctl_lap": "膝の上", "ctl_handjob": "手", "ctl_hero_pose": "主人公の姿勢から", "ctl_urethra": "尿道", "multi": "相手が複数",
           "ear_soft": "耳", "armpit": "脇", "smother": "顔をうずめる", "buttjob": "お尻", "fallback": "どの技にも当たらず、姿勢の予備"}
KIND_RX = [("翼", r"\bwings?\b"), ("尻尾", r"\btails?\b(?! bells)"), ("角", r"\bhorns?\b"), ("触手", r"tentacle"), ("獣耳", r"(?:cat|fox|dog|wolf|rabbit|bunny|animal) ears|kemonomimi")]


def scene_posture(text):
    t = text or ""
    i = t.find("THE MAN")
    if i >= 0:
        t = t[i:]
    for name, rx in pc().get("posture_rx") or []:
        try:
            if re.search(rx, t, re.I):
                return name
        except re.error:
            continue
    return ""


def partner_kind(p):
    if "newhalf" in p:
        return "NH"
    if ("femboy" in p or "otoko no ko" in p) and "1girl" not in p and "woman" not in p:
        return "男の娘"
    if re.search(r"\bfutanari\b", p, re.I):
        return "ふたなり"
    return "女性"


def partner_parts(p):
    out = [k for k, rx in KIND_RX if re.search(rx, p, re.I)]
    sk = pc().get("skip_body")
    if sk and re.search(sk, p, re.I):
        out.append("下半身が人でない")
    return out


def scene_type(code, n):
    s = n[len(code) + 1:] if n.startswith(code + "_") else n
    if s.startswith("atk_"):
        return "攻撃（技の絵）"
    m = re.match(r"lose_(btl|inochi|onedari|onani)_", s)
    if m:
        return {"btl": "敗北（バトル）", "inochi": "敗北（命乞い）", "onedari": "敗北（おねだり）", "onani": "オナニー"}[m.group(1)]
    if s == "bg":
        return "背景"
    if "onanie" in s:
        return "オナニー"
    return "立ち絵ほか"


def is_scene(n):
    return bool(re.search(r"_(?:atk|lose)_", n))


_PROMPTS = {}


def prompts_of(code):
    p = os.path.join(IMG(), "prompts", code + ".json")
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return {}
    if _PROMPTS.get(code, (None,))[0] != mt:
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            d = {}
        _PROMPTS[code] = (mt, d if isinstance(d, dict) else {})
    return _PROMPTS[code][1]


_SHOT = {"d": None, "dirty": False}
SHOT_RX = re.compile(r"^(.+)_(\d{5})_\.png$", re.I)


def _shot_cache():
    if _SHOT["d"] is None:
        p = os.path.join(CACHE(), "撮った絵の下書き.json")
        try:
            _SHOT["d"] = json.load(open(p, encoding="utf-8"))
        except Exception:
            _SHOT["d"] = {}
    return _SHOT["d"]


def _save_shot_cache():
    if _SHOT["dirty"]:
        os.makedirs(CACHE(), exist_ok=True)
        p = os.path.join(CACHE(), "撮った絵の下書き.json")
        with open(p + ".tmp", "w", encoding="utf-8") as f:
            json.dump(_SHOT["d"], f, ensure_ascii=False)
        os.replace(p + ".tmp", p)
        _SHOT["dirty"] = False


def shot_draft(path):
    """撮った絵に埋め込まれた設定から、撮ったときの下書き名（割り当てが変わった絵の撮り直し.py と同じ読み方）"""
    c = _shot_cache()
    try:
        mt = int(os.path.getmtime(path))
    except OSError:
        return None
    k = c.get(path)
    if k and k[0] == mt:
        return k[1]
    d = None
    try:
        from PIL import Image
        with Image.open(path) as im:
            pr = json.loads(im.info.get("prompt") or "")
        n = pr.get("71")
        d = re.sub(r"^pose_|\.png$", "", str(n["inputs"].get("image", "")), flags=re.I) if isinstance(n, dict) and n.get("class_type") == "LoadImage" else ""
    except Exception:
        d = None
    c[path] = [mt, d]
    _SHOT["dirty"] = True
    return d


def shots(code):
    """{画像名: (いちばん新しいファイル名, 撮ったときの下書き)}"""
    d = A.out_dir(code, A.styles())
    newest = {}
    try:
        fs = os.listdir(d)
    except OSError:
        return d, {}
    for f in fs:
        m = SHOT_RX.match(f)
        if m and (m.group(1) not in newest or int(m.group(2)) > newest[m.group(1)][0]):
            newest[m.group(1)] = (int(m.group(2)), f)
    out = {n: (f, shot_draft(os.path.join(d, f))) for n, (_, f) in newest.items()}
    return d, out


def mod_codes():
    try:
        return sorted(f[:-5] for f in os.listdir(os.path.join(IMG(), "prompts")) if f.endswith(".json"))
    except OSError:
        return []


def assign_rows(code, P=None, pv=None, regs=None, wm=None):
    """1つのMODの全部の絵（オナニーを撮らない設定なら外す）の割り当てと印"""
    P = P or pc()
    pv = pv if pv is not None else preview()[0]
    regs = regs if regs is not None else {r["name"]: r for r in region_rows()}
    wm = wm or word_map()
    rp, rt, extra = P.get("ref_posture") or {}, P.get("ref_tags") or {}, set(P.get("ref_extra") or [])
    reg = registered()
    skip = A.skip_onanie()
    pr = prompts_of(code)
    _, sh = shots(code)
    fnot = P.get("fallback_not") or ""
    rows = []
    for n, e in pr.items():
        if skip and "onani" in n.lower():
            continue
        pos = (e or {}).get("positive", "") if isinstance(e, dict) else ""
        r = pv.get((code, n))
        draft = (r or {}).get("下書き", "").strip()
        use = (r or {}).get("使うもの", "")
        sc = is_scene(n)
        comp = comp_of(draft) if draft.startswith("depthref_") else ""
        sp = scene_posture(pos) if sc else ""
        dp = rp.get(comp, "") if comp else ""
        tech = (re.search(r"行為タグ:([^ /]+)", use) or [None, ""])[1]
        why = []
        if tech.startswith("alt:"):
            why.append("構図LoRA（%s）からの置き換え" % tech[4:])
        elif tech:
            why.append("技の判定：" + TECH_JA.get(tech, tech))
        if comp:
            sets = reg.get(comp) or []
            why.append("組：" + ("・".join(sets) if sets else "（未登録）"))
            if comp in extra:
                why.append("替え専用の構図（重なったときだけ）")
        elif draft.startswith("depth3d_"):
            why.append("3Dの下書き")
        shot = sh.get(n)
        reg_r = regs.get(draft[9:]) if draft.startswith("depthref_") else None
        region = (r or {}).get("人物の範囲", "")
        marks = []
        if sc and r is not None:
            if not draft and "組み立て失敗" not in (r.get("注意") or ""):
                marks.append("下書きなし")
            if "組み立て失敗" in (r.get("注意") or ""):
                marks.append("組み立て失敗")
            if sp and dp and sp != dp and {sp, dp} != {"sit", "kneel"}:
                marks.append("姿勢の食い違い")
            if draft.startswith("depthref_"):
                if not region:
                    marks.append("範囲なし")
                elif "hero" not in region and not re.search(r"\bpov\b", rt.get(comp, "")):
                    marks.append("主人公の範囲なし")
            if shot and shot[1] is not None and shot[1].lower() != draft.lower():
                marks.append("撮った時と違う")
        if sc and r is None:
            marks.append("下見にまだ無い")
        kind = partner_kind(pos) if sc else ""
        rows.append(dict(code=code, name=n, type=scene_type(code, n), scene=sc, draft=draft, comp=comp, reading=reading(draft, wm) if draft else "",
                         region=region, region_result=(reg_r or {}).get("result", ""), region_fix=(reg_r or {}).get("fix", ""),
                         sp=sp, dp=dp, tech=tech, why=why, kind=kind, parts=partner_parts(pos) if sc else [],
                         cross=bool(re.search(r"crossdress", pos, re.I)) and "navy" in pos, shot=(shot or ("", None))[0],
                         shot_draft=(shot or ("", None))[1], done=(r or {}).get("撮り済み", "") == "済", inpv=r is not None, marks=marks,
                         note=(r or {}).get("注意", "")))
    cnt = {}
    for x in rows:
        if x["scene"] and x["draft"]:
            cnt[x["draft"]] = cnt.get(x["draft"], 0) + 1
    for x in rows:
        if x["scene"] and x["draft"].startswith("depthref_") and cnt[x["draft"]] > 1:
            x["marks"].append("同じMODで重複")
    _save_shot_cache()
    return rows


_SUM = {"k": None, "d": None}


def assign_summary():
    """MODごとのまとめ（場面の数・下書きありの数・印の種類ごとの数）"""
    pvrows, pvmods, mt = preview()
    k = (mt, os.path.getmtime(rpath(P_MODEL())), int(time.time() // 120))
    if _SUM["k"] == k:
        return _SUM["d"]
    P, regs, wm = pc(), {r["name"]: r for r in region_rows()}, word_map()
    md = A.mod_dirs()
    out = []
    for code in mod_codes():
        rows = assign_rows(code, P, pvrows, regs, wm)
        sc = [r for r in rows if r["scene"]]
        m = {}
        for r in sc:
            for x in r["marks"]:
                m[x] = m.get(x, 0) + 1
        out.append(dict(code=code, n=(md.get(code) or {}).get("n", 0), scenes=len(sc), drafts=sum(1 for r in sc if r["draft"]),
                        marked=sum(1 for r in sc if r["marks"]), marks=m, inpv=code in pvmods))
    _SUM.update(k=k, d=out)
    return out


# ---------------------------------------------------------------- MOD の文（A7 のシチュエーション）
KEYS = ("m1", "m2", "m3", "e1", "e2", "e3", "boss", "master")
_TXT = {}


def mod_texts(code):
    """{ファイル名: 中身}。読めなければ None"""
    info = A.mod_dirs().get(code) or {}
    src = info.get("dir") or info.get("zip")
    if not src:
        return None
    try:
        mt = os.path.getmtime(src)
    except OSError:
        return None
    if _TXT.get(code, (None,))[0] == (src, mt):
        return _TXT[code][1]
    texts = {}
    if info.get("dir"):
        for d, _, fs in os.walk(os.path.join(info["dir"], "CSV")):
            for f in fs:
                if f.lower().endswith(".txt"):
                    try:
                        texts[f] = open(os.path.join(d, f), encoding="utf-8-sig", errors="replace").read()
                    except OSError:
                        pass
    else:
        try:
            with zipfile.ZipFile(info["zip"]) as z:
                for x in z.namelist():
                    if "/CSV/" in x and x.lower().endswith(".txt"):
                        texts[os.path.basename(x)] = z.read(x).decode("utf-8-sig", "replace")
        except Exception:
            texts = {}
    if not texts:
        texts = None
    _TXT[code] = ((src, mt), texts)
    return texts


def role_of(code, n):
    s = n.split("_")[-1]
    return s if s in KEYS else ""


def card_file(code, role):
    return "%s_master.txt" % code if role in ("m1", "m2", "m3", "master") else "%s_mons_%s.txt" % (code, role)


def _clean(line):
    return line.strip().lstrip("﻿")


def attack_blocks(lines, key):
    """技CG の行から、技名・攻撃タイプ・段階ごとのセリフを読む"""
    out = []
    for i, ln in enumerate(lines):
        s = _clean(ln)
        if not re.match(r"^画像,%s,\d" % re.escape(key), s):
            continue
        name, atype = "", ""
        for j in range(i - 1, max(-1, i - 8), -1):
            m = re.match(r"^技名表示,(.+)$", _clean(lines[j]))
            if m:
                name = m.group(1).strip()
                break
        for j in range(i - 1, max(-1, i - 60), -1):
            m = re.match(r"^if,攻撃タイプ,==,(.+)$", _clean(lines[j]))
            if m:
                atype = m.group(1).strip()
                break
        body, target, stage, depth, tstack = [], "", "", 0, []
        for j in range(i + 1, min(len(lines), i + 160)):
            t = _clean(lines[j])
            if re.match(r"^(技名表示,|if,攻撃タイプ)", t):
                break
            if t.startswith("if,$主,==,1"):
                target = "主人公へ"
            elif t.startswith("}else{") and target == "主人公へ" and not stage:
                target = "味方モンスターへ"
            m = re.match(r"^if,\$段階,==,(\d+)", t)
            if m:
                stage = "段階" + m.group(1)
            if t == "}" and stage:
                stage = ""
            if t == "}else{" and stage:
                stage = ""
            m = re.match(r"^(セリフ|説明),(.+)$", t)
            if m:
                body.append(dict(kind=m.group(1), target=target, stage=stage, text=m.group(2)))
        out.append(dict(name=name, atype=atype, lines=body))
    return out


def context_lines(lines, i, before, after):
    out = []
    for j in range(max(0, i - before), min(len(lines), i + after + 1)):
        t = _clean(lines[j])
        m = re.match(r"^(セリフ|説明|話者|技名表示|画像|選択肢|背景)\s*,(.*)$", t)
        if m:
            out.append(dict(kind=m.group(1), text=m.group(2), here=(j == i)))
    return out


def card_profile(texts, fname, code, role):
    t = (texts or {}).get(fname) or ""
    prof = dict(card=fname, name="", explain=[], gender="", type="", fav="")
    for ln in t.splitlines():
        s = _clean(ln)
        m = re.match(r"^&カード名,(.+)$", s)
        if m and not prof["name"]:
            prof["name"] = m.group(1)
        m = re.match(r"^効果設定,\d+,explain,(.+)$", s)
        if m:
            prof["explain"].append(m.group(1))
            f = re.search(r"★得意技【([^】]+)】", m.group(1))
            if f and not prof["fav"]:
                prof["fav"] = f.group(1)
        m = re.match(r"^性別設定,(.+)$", s)
        if m:
            prof["gender"] = m.group(1)
        m = re.match(r"^タイプ設定,(.+)$", s)
        if m:
            prof["type"] = m.group(1)
    # 制作中の入力内容（身長・スリーサイズなど）があれば足す
    try:
        md = A.mod_dirs().get(code) or {}
        nm = "N%s_%s" % (md.get("n", 0), code)
        p = os.path.join(A.P_WIP, nm, "入力内容.json")
        if os.path.exists(p):
            ch = (json.load(open(p, encoding="utf-8")).get("chars") or {}).get("master" if role in ("m1", "m2", "m3") else role) or {}
            if ch:
                prof["input"] = {k: ch.get(k) for k in ("title", "name", "gender", "height", "b", "w", "h", "look", "persona") if ch.get(k)}
    except Exception:
        pass
    return prof


# ---- ゲームの中の技の名前・キャラの名前（2026-10-05 ユーザー要望「下書きがどのMODのどの技に当たっているか知りたい」）
GAME_KIND = {"atk": "攻撃（技）", "lose_btl": "負け（戦闘）", "lose_inochi": "負け（命乞い）", "lose_onedari": "負け（おねだり）", "lose_onani": "負け（自慰）"}
_GAME = {}


def game_info(code, n):
    """{chara, kind, skills, fav}。カードの文が読めなければ skills は空"""
    s = n[len(code) + 1:] if n.startswith(code + "_") else n
    role = role_of(code, n)
    kind = next((v for k, v in GAME_KIND.items() if s.startswith(k + "_")), "")
    texts = mod_texts(code)
    if texts is None or not role:
        return dict(chara="", kind=kind, skills=[], fav="")
    key = (code, role, id(texts))
    if key not in _GAME:
        fname = card_file(code, role)
        prof = card_profile(texts, fname, code, role)
        k = "&技CG_%s" % role[1] if role in ("m1", "m2", "m3") else "&技CG"
        names = []
        for a in attack_blocks((texts.get(fname) or "").splitlines(), k):
            if a.get("name") and a["name"] not in names:
                names.append(a["name"])
        _GAME[key] = dict(chara=prof.get("name", ""), skills=names, fav=prof.get("fav", ""))
    g = _GAME[key]
    return dict(chara=g["chara"], kind=kind, skills=g["skills"] if s.startswith("atk_") else [], fav=g["fav"] if s.startswith("atk_") else "")


def scene_detail(code, n):
    code = A.codes_arg([code])[0]
    pr = prompts_of(code)
    if n not in pr:
        raise RuntimeError("その画像名はありません: " + n)
    pos = (pr[n] or {}).get("positive", "")
    rows = assign_rows(code)
    row = next((r for r in rows if r["name"] == n), {})
    P = pc()
    out = dict(code=code, name=n, row=row, prompt=pos, read=None)
    # gen.py が読み取った内容（日本語）
    use = (preview()[0].get((code, n)) or {}).get("使うもの", "")
    tg = (P.get("ref_tags") or {}).get(row.get("comp", ""), "")
    view = []
    for k, rx in VIEW_FROM_TAGS:
        if re.search(rx, tg):
            view.append({"pov": "主人公目線", "side": "横から", "front": "前から", "behind": "後ろから", "above": "上から", "low": "下から"}[k])
    fnot = P.get("fallback_not") or ""
    out["gen"] = [
        ("技の判定", ("構図LoRA %s の置き換え" % row["tech"][4:]) if row.get("tech", "").startswith("alt:") else TECH_JA.get(row.get("tech", ""), row.get("tech", "")) or "なし"),
        ("主人公の姿勢（本文から）", POSTURE_JA.get(row.get("sp", ""), "読めない")),
        ("下書きの姿勢", POSTURE_JA.get(row.get("dp", ""), "決まっていない")),
        ("下書きの視点", "・".join(view) or "決まっていない"),
        ("主人公目線に書き換え", "する" if "POV書き換え" in use else "しない"),
        ("相手の種類", (row.get("kind") or "") + ("（" + "・".join(row.get("parts") or []) + "）" if row.get("parts") else "")),
        ("触れる・触れない", "触れない・離れている語がある" if fnot and re.search(fnot, pos, re.I) else "触れる"),
        ("女装", "女装の場面" if row.get("cross") else "なし"),
        ("使うもの（記録のまま）", use or "（下見にまだ無い）"),
    ]
    texts = mod_texts(code)
    if texts is None:
        out["read"] = "読めません（このMODのカードのファイルが見つからない・作りが違う）"
        return out
    role = role_of(code, n)
    fname = card_file(code, role) if role else ""
    out["profile"] = card_profile(texts, fname, code, role) if role else None
    sit = dict(attacks=[], lose=[], recall=False)
    s = n[len(code) + 1:]
    if s.startswith("atk_") and role:
        key = "&技CG_%s" % role[1] if role in ("m1", "m2", "m3") else "&技CG"
        lines = (texts.get(fname) or "").splitlines()
        sit["attacks"] = attack_blocks(lines, key)
        fav = (out["profile"] or {}).get("fav")
        for a in sit["attacks"]:
            a["fav"] = bool(fav and a["name"] == fav)
    else:
        for f, t in sorted(texts.items()):
            lines = t.splitlines()
            for i, ln in enumerate(lines):
                if re.match(r"^\s*画像,&画像_%s,\d" % re.escape(n), ln):
                    if "recall" in f.lower():
                        sit["recall"] = True
                    sit["lose"].append(dict(file=f, short=context_lines(lines, i, 14, 14), long=context_lines(lines, i, 70, 70)))
    out["situation"] = sit
    if not sit["attacks"] and not sit["lose"] and is_scene(n):
        out["read"] = "この絵が出る所を、カードの文の中に見つけられませんでした"
    return out


# ---------------------------------------------------------------- 当たり具合（A4）
def usage():
    pvrows, pvmods, mt = preview()
    P = pc()
    rp = P.get("ref_posture") or {}
    wm = word_map()
    reg = registered()
    by_draft, by_comp = {}, {}
    fail = nodraft = mism = 0
    per_mod = {}
    for (mod, n), r in pvrows.items():
        if not is_scene(n):
            continue
        d = (r.get("下書き") or "").strip()
        if "組み立て失敗" in (r.get("注意") or ""):
            fail += 1
        elif not d:
            nodraft += 1
        if d:
            by_draft.setdefault(d, []).append([mod, n])
            per_mod.setdefault((mod, d), 0)
            per_mod[(mod, d)] += 1
            if d.startswith("depthref_"):
                c = comp_of(d)
                by_comp.setdefault(c, []).append([mod, n, d])
    dup_rows = [[m, d, k] for (m, d), k in per_mod.items() if k > 1 and d.startswith("depthref_")]   # 重複よけは元絵の下書きだけ（3Dの下書きは数えない）
    # 食い違い：本文の姿勢と下書きの姿勢
    mis_rows = []
    for (mod, n), r in pvrows.items():
        d = (r.get("下書き") or "").strip()
        if not is_scene(n) or not d.startswith("depthref_"):
            continue
        dp = rp.get(comp_of(d), "")
        if not dp:
            continue
        pos = (prompts_of(mod).get(n) or {}).get("positive", "")
        sp = scene_posture(pos)
        if sp and sp != dp and {sp, dp} != {"sit", "kneel"}:
            mis_rows.append([mod, n, d, POSTURE_JA.get(sp, sp), POSTURE_JA.get(dp, dp)])
    old, when = prev_snapshot()
    moved = []
    if old is not None:
        for k, r in pvrows.items():
            if not is_scene(k[1]):
                continue
            o = old.get(k)
            if o is None:
                continue
            a, b = (o.get("下書き") or "").strip(), (r.get("下書き") or "").strip()
            if a != b:
                moved.append([k[0], k[1], a, b])
    comps = []
    for c, lst in sorted(by_comp.items(), key=lambda x: -len(x[1])):
        ds = {}
        for _, _, d in lst:
            ds[d] = ds.get(d, 0) + 1
        comps.append(dict(comp=c, reading=reading(c, wm), n=len(lst), mods=len({x[0] for x in lst}), drafts=ds, sets=reg.get(c) or [],
                          posture=rp.get(c, ""), scenes=lst))
    # 登録してあるのに一度も当たらない構図
    unused = sorted(c for c in reg if c not in by_comp)
    others = [dict(draft=d, n=len(v), scenes=v) for d, v in sorted(by_draft.items(), key=lambda x: -len(x[1])) if not d.startswith("depthref_")]
    return dict(age=preview_age(), counts=dict(scenes=sum(1 for k in pvrows if is_scene(k[1])), fail=fail, mismatch=len(mis_rows),
                                               dup=len(dup_rows), nodraft=nodraft, moved=len(moved) if old is not None else None),
                comps=comps, others=others, unused=[dict(comp=c, reading=reading(c, wm), sets=reg[c]) for c in unused],
                dup=dup_rows, mismatch=mis_rows, moved=moved, moved_from=when)


def pose_report():
    head, rows = read_dicts(P_POSE_REPORT())
    try:
        t = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(P_POSE_REPORT())))
    except OSError:
        t = ""
    return dict(time=t, head=head, rows=rows)


# ---------------------------------------------------------------- 下書きを外す（model.json・3章の決まり）
def mj_dump(d):
    return json.dumps(d, ensure_ascii=False, indent=2).replace("\n", "\r\n")


AGE_KEYS = ("hero_face", "scene_safety")


def model_backup(what):
    os.makedirs(BAK(), exist_ok=True)
    safe = re.sub(r'[\\/:*?"<>|\s]+', "_", what)[:40]
    name = "model_%s_%s前.json" % (time.strftime("%Y%m%d_%H%M%S"), safe)
    dst = os.path.join(BAK() if not TEST else os.path.dirname(wpath(os.path.join(BAK(), "x"))), name)
    src = rpath(P_MODEL())
    shutil.copy2(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("控えを取れませんでした（大きさが違う）。書き換えを止めました。")
    return name


def model_write(newd, what, from_bak=""):
    """3章の決まり：控えを取ってから書く。年齢に関わる設定が変わっていないことを確かめる。記録に1行"""
    with LOCK:
        cur = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
        for k in AGE_KEYS:
            if json.dumps(cur.get(k), sort_keys=True) != json.dumps(newd.get(k), sort_keys=True):
                raise RuntimeError("年齢に関わる設定（%s）が変わってしまうので止めました" % k)
        changed = [k for k in set(cur) | set(newd) if k != "pose_control" and json.dumps(cur.get(k), sort_keys=True) != json.dumps(newd.get(k), sort_keys=True)]
        if changed:
            raise RuntimeError("pose_control 以外（%s）が変わってしまうので止めました" % "・".join(changed))
        try:
            bname = model_backup(what)
        except Exception as ex:
            raise RuntimeError("控えを取れなかったので書き換えませんでした：%s" % ex)
        w = wpath(P_MODEL())
        with open(w + ".tmp", "wb") as f:
            f.write(mj_dump(newd).encode("utf-8"))
        json.load(open(w + ".tmp", encoding="utf-8"))   # 読めることを確かめる
        os.replace(w + ".tmp", w)
        _MJ["mt"] = None
        os.makedirs(REC(), exist_ok=True)
        with open(wpath(P_MODEL_LOG()), "a", encoding="utf-8") as f:
            f.write("%s  %s  控え: %s%s%s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), what, bname, ("  戻した元: " + from_bak) if from_bak else "",
                                               "  （試しの起動）" if TEST else ""))
        return bname


def exclude_plan(b):
    d = (b.get("draft") or "").strip()
    if not d.startswith("depthref_"):
        raise RuntimeError("外せるのは元絵の下書き（depthref_…）だけです")
    pvrows = preview()[0]
    hit = [[m, n] for (m, n), r in pvrows.items() if (r.get("下書き") or "").strip().lower() == d.lower()]
    ex = pc().get("ref_exclude") or []
    comp = comp_of(d)
    left = [x for x in comp_drafts().get(comp, []) if ("depthref_" + x).lower() not in {e.lower() for e in ex} and ("depthref_" + x).lower() != d.lower()]
    return dict(draft=d, already=d.lower() in {e.lower() for e in ex}, scenes=hit, comp=comp, left=left, n_ex=len(ex),
                change="pose_control.ref_exclude に %s を足す（%d 個 → %d 個）" % (d, len(ex), len(ex) + 1), busy=busy(), test=TEST)


def exclude(b):
    if not b.get("confirmed"):
        raise RuntimeError("確認を押してから外してください")
    need_idle("下書きを外す")
    plan = exclude_plan(b)
    if plan["already"]:
        return "もう外してあります：" + plan["draft"]
    why = (b.get("why") or "").strip() or "理由なし"
    with LOCK:
        d = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
        P = d.setdefault("pose_control", {})
        P.setdefault("ref_exclude", []).append(plan["draft"])
        P["ref_exclude_memo"] = (P.get("ref_exclude_memo") or "") + "／%s（%s 画面から外す：%s）" % (plan["draft"][9:], time.strftime("%Y-%m-%d"), why)
        bname = model_write(d, "下書き%s外し" % plan["draft"][9:])
    add_memo("下書きを外す", plan["draft"], "外す", why)
    return "外しました：%s（控え %s）。%s" % (plan["draft"], bname, queue_preview_after("下書きを外した"))


def model_backups():
    fs = []
    for d in {BAK(), os.path.dirname(wpath(os.path.join(BAK(), "x"))) if TEST else BAK()}:
        try:
            for f in os.listdir(d):
                if f.startswith("model") and f.endswith(".json"):
                    fs.append(dict(name=f, time=time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(os.path.join(d, f)))),
                                   mt=os.path.getmtime(os.path.join(d, f)), dir=d))
        except OSError:
            pass
    fs.sort(key=lambda x: -x["mt"])
    log = []
    try:
        log = open(rpath(P_MODEL_LOG()), encoding="utf-8").read().splitlines()[-50:]
    except OSError:
        pass
    return dict(files=[{k: v for k, v in x.items() if k != "dir"} for x in fs], log=log[::-1])


def _bak_path(name):
    if not re.match(r"^model[^\\/]*\.json$", name or ""):
        raise RuntimeError("名前が違います")
    for d in ([os.path.dirname(wpath(os.path.join(BAK(), "x")))] if TEST else []) + [BAK()]:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    raise RuntimeError("その控えはありません: " + name)


KEEP_ON_RESTORE = ("region",)


def restore_plan(b):
    p = _bak_path(b.get("name"))
    old = json.load(open(p, encoding="utf-8")).get("pose_control") or {}
    cur = pc()
    diff = []
    for k in sorted(set(old) | set(cur)):
        if k in KEEP_ON_RESTORE:
            continue
        a, c = old.get(k), cur.get(k)
        if json.dumps(a, sort_keys=True) == json.dumps(c, sort_keys=True):
            continue
        if isinstance(a, list) and isinstance(c, list):
            sa, sc = {json.dumps(x, sort_keys=True, ensure_ascii=False) for x in a}, {json.dumps(x, sort_keys=True, ensure_ascii=False) for x in c}
            diff.append("%s：戻すと %d 個 → %d 個（足される %d・消える %d）" % (k, len(c), len(a), len(sa - sc), len(sc - sa)))
        elif isinstance(a, dict) and isinstance(c, dict):
            add = [x for x in a if x not in c]
            rem = [x for x in c if x not in a]
            ch = [x for x in a if x in c and json.dumps(a[x], sort_keys=True) != json.dumps(c[x], sort_keys=True)]
            diff.append("%s：足される %d（%s）・消える %d（%s）・中身が変わる %d（%s）" % (k, len(add), "、".join(add[:6]), len(rem), "、".join(rem[:6]), len(ch), "、".join(ch[:6])))
        elif isinstance(a, str) and isinstance(c, str):
            diff.append("%s：文が変わる（今 %d 字 → 戻すと %d 字）" % (k, len(c), len(a)))
        elif a is None:
            diff.append("%s：今はあるが、戻すと無くなる" % k)
        elif c is None:
            diff.append("%s：今は無いが、戻すと入る" % k)
        else:
            diff.append("%s：%s → %s" % (k, str(c)[:60], str(a)[:60]))
    return dict(name=b.get("name"), diff=diff, busy=busy(), test=TEST,
                note="戻すのは pose_control の中だけです（人物の範囲の文 region と、年齢に関わる設定はそのまま）。戻す前の状態も控えに取ります。")


def restore(b):
    if not b.get("confirmed"):
        raise RuntimeError("確認を押してから戻してください")
    need_idle("控えから戻す")
    p = _bak_path(b.get("name"))
    old = json.load(open(p, encoding="utf-8")).get("pose_control") or {}
    with LOCK:
        d = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
        cur = d.get("pose_control") or {}
        new = {k: v for k, v in old.items() if k not in KEEP_ON_RESTORE}
        for k in KEEP_ON_RESTORE:
            if k in cur:
                new[k] = cur[k]
        d["pose_control"] = new
        bname = model_write(d, "控え%sに戻す" % os.path.splitext(b["name"])[0][:30], from_bak=b["name"])
    return "戻しました（戻す前の控え %s）。%s" % (bname, queue_preview_after("控えから戻した"))


# ---------------------------------------------------------------- 撮り直しの予定・本文を直す候補（A7）
RESHOOT_HEAD = ["日時", "MOD", "画像名", "理由", "並べた日時"]
TEXTFIX_HEAD = ["日時", "MOD", "画像名", "下書き", "メモ"]


def add_reshoot(b):
    code = A.codes_arg([b.get("code", "")])[0]
    names = [n for n in (b.get("names") or []) if re.match(r"^[A-Za-z0-9_]+$", n)]
    if not names:
        raise RuntimeError("場面が選ばれていません")
    with LOCK:
        h, rows = read_dicts(P_RESHOOT())
        have = {(r["MOD"], r["画像名"]) for r in rows if not r.get("並べた日時")}
        for n in names:
            if (code, n) not in have:
                rows.append(dict(日時=now(), MOD=code, 画像名=n, 理由=(b.get("why") or "").strip(), 並べた日時=""))
        os.makedirs(REC(), exist_ok=True)
        write_dicts(P_RESHOOT(), RESHOOT_HEAD, rows)
    return "撮り直しの予定に入れました（%d 場面）" % len(names)


def del_reshoot(b):
    keys = {(x[0], x[1]) for x in b.get("keys") or []}
    with LOCK:
        h, rows = read_dicts(P_RESHOOT())
        rows = [r for r in rows if (r["MOD"], r["画像名"]) not in keys or r.get("並べた日時")]
        write_dicts(P_RESHOOT(), RESHOOT_HEAD, rows)
    return "予定から外しました"


def run_reshoot(b):
    need_idle("撮り直し")
    with LOCK:
        h, rows = read_dicts(P_RESHOOT())
        todo = {}
        for r in rows:
            if not r.get("並べた日時"):
                todo.setdefault(r["MOD"], []).append(r["画像名"])
        if not todo:
            return "予定はありません"
        if TEST:
            raise RuntimeError("試しの起動（--test）では撮影を並べません")
        A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
        for code, names in todo.items():
            for i in range(0, len(names), 20):
                add_job("撮り直し %s（今の割り当てで %d 場面）" % (code, len(names[i:i + 20])),
                        [A.PY, "gen.py", code, ",".join(names[i:i + 20]), "--model", "wai", "--redo"], rec="撮影記録.txt")
        for r in rows:
            if not r.get("並べた日時"):
                r["並べた日時"] = now()
        write_dicts(P_RESHOOT(), RESHOOT_HEAD, rows)
    return "撮り直しを並べました（%d MOD）" % len(todo)


def add_textfix(b):
    code = A.codes_arg([b.get("code", "")])[0]
    n = b.get("name", "")
    os.makedirs(REC(), exist_ok=True)
    append_dict(P_TEXTFIX(), TEXTFIX_HEAD, dict(日時=now(), MOD=code, 画像名=n, 下書き=b.get("draft", ""), メモ=(b.get("memo") or "").replace("\n", " ")))
    return "本文を直す候補に入れました：" + n


def del_textfix(b):
    idx = set(int(i) for i in b.get("idx") or [])
    with LOCK:
        h, rows = read_dicts(P_TEXTFIX())
        rows = [r for i, r in enumerate(rows) if i not in idx]
        write_dicts(P_TEXTFIX(), TEXTFIX_HEAD, rows)
    return "外しました"


def textfix_text():
    h, rows = read_dicts(P_TEXTFIX())
    lines = ["本文を直す候補（%s 現在・%d 件）" % (now(), len(rows)), ""]
    for r in rows:
        lines.append("・%s %s（下書き %s）%s" % (r["MOD"], r["画像名"], r.get("下書き") or "なし", ("：" + r["メモ"]) if r.get("メモ") else ""))
    txt = "\n".join(lines) + "\n"
    os.makedirs(REC(), exist_ok=True)
    p = wpath(os.path.join(REC(), "本文を直す候補.txt"))
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    return dict(text=txt, path=p)


# ---------------------------------------------------------------- 構図の見本（A1）
def comp_list():
    reg = registered()
    cd = comp_drafts()
    P = pc()
    ex = {x.lower() for x in P.get("ref_exclude") or []}
    items = {r["構図名"]: r for r in items_table()}
    wm = word_map()
    out = []
    for c in sorted(set(reg) | set(cd)):
        ds = cd.get(c, [])
        use = [d for d in ds if ("depthref_" + d).lower() not in ex]
        it = items.get(c) or {}
        out.append(dict(comp=c, reading=reading(c, wm), registered=c in reg, sets=reg.get(c) or [], extra=c in set(P.get("ref_extra") or []),
                        n=len(ds), n_use=len(use), sample=(use or ds or [""])[0], drafts=ds,
                        posture=(P.get("ref_posture") or {}).get(c, ""), tags=(P.get("ref_tags") or {}).get(c, ""),
                        items={k: it.get(k, "") for k in ITEM_KEYS + ["同時の技"]}))
    return out


# ---------------------------------------------------------------- 小さい絵（作り置き）
_SAFE = re.compile(r"^[^\\/:*?\"<>|]+$")


def _thumb_from(src, key, w, extra_mt=0, build=None):
    os.makedirs(CACHE(), exist_ok=True)
    mt = max(os.path.getmtime(src), extra_mt)
    cp = os.path.join(CACHE(), "%s.%d.jpg" % (hashlib.md5(key.encode("utf-8")).hexdigest(), w))
    if os.path.exists(cp) and int(os.path.getmtime(cp)) == int(mt):
        return open(cp, "rb").read()
    from PIL import Image
    im = build() if build else Image.open(src).convert("RGB")
    if w:
        im.thumbnail((w, w * 2))
    im.save(cp, "JPEG", quality=82)
    os.utime(cp, (mt, mt))
    return open(cp, "rb").read()


def _fit(img, resample=None):
    from PIL import Image
    w, h = img.size
    tw, th = (1216, 832) if w > h else (832, 1216)
    s = max(tw / w, th / h)
    img = img.resize((max(tw, round(w * s)), max(th, round(h * s))), resample or Image.LANCZOS)
    w, h = img.size
    l, t = (w - tw) // 2, (h - th) // 2
    return img.crop((l, t, l + tw, t + th))


def kimg(q):
    k, n, w = q.get("k", ""), q.get("n", ""), max(0, min(1600, int(q.get("w", 0) or 0)))
    if not n or not _SAFE.match(n) or ".." in n:
        raise RuntimeError("名前が違います")
    if k == "cand":
        where = q.get("where", "候補")
        p = os.path.join(CAND(), n) if where == "候補" else os.path.join(CAND(), "_見送り", n)
        if TEST and not os.path.exists(p):
            p = tpath(p)
    elif k == "src":
        p = os.path.join(PICK(), n + ".png")
    elif k == "depth":
        p = os.path.join(DRAFT(), n + ".png")
        if not os.path.exists(p):
            p = os.path.join(CIN(), "pose_%s.png" % n)
    elif k == "region":
        src = os.path.join(PICK(), n + ".png")
        if not os.path.exists(src):
            raise RuntimeError("元絵がありません: " + n)
        hp, pp = os.path.join(DRAFT(), "region_%s_hero.png" % n), os.path.join(DRAFT(), "region_%s_partner.png" % n)
        p1, p2 = os.path.join(DRAFT(), "region_%s_partner1.png" % n), os.path.join(DRAFT(), "region_%s_partner2.png" % n)
        emt = max([os.path.getmtime(x) for x in (hp, pp, p1, p2) if os.path.exists(x)] + [0])
        has = tuple(os.path.exists(x) for x in (hp, pp, p1, p2))
        layers = ((p1, (255, 40, 40)), (p2, (255, 150, 0)), (hp, (40, 90, 255))) if has[2] and has[3] else ((pp, (255, 40, 40)), (hp, (40, 90, 255)))

        def build():
            import numpy as np
            from PIL import Image
            a = np.array(_fit(Image.open(src).convert("RGB"))).astype("float32")
            for mp, col in layers:
                if os.path.exists(mp):
                    m = Image.open(mp).convert("L").resize((a.shape[1], a.shape[0]))
                    wt = np.array(m).astype("float32")[..., None] / 255 * 0.5
                    a = a * (1 - wt) + np.array(col, "float32") * wt
            return Image.fromarray(a.clip(0, 255).astype("uint8"))
        return _thumb_from(src, "region|%s|%s" % (n, has), w, emt, build), "image/jpeg"
    elif k == "chara":
        return cl_img(q, w)
    elif k == "cltry":
        return cl_try_img(q, w)
    elif k == "mood":
        return mood_img(q, w)
    elif k == "clref":
        return cl_ref_img(q, w)
    elif k == "check":
        return check_img(q, w)
    elif k == "shot":
        code = A.codes_arg([q.get("code", "")])[0]
        body, ct = A.thumb(code, n, w)
        return body, ct
    else:
        raise RuntimeError("種類が違います")
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません: " + n)
    if not w:
        ext = os.path.splitext(p)[1].lower()
        return open(p, "rb").read(), {".png": "image/png", ".webp": "image/webp", ".bmp": "image/bmp"}.get(ext, "image/jpeg")
    return _thumb_from(p, "%s|%s" % (k, p), w), "image/jpeg"


def prewarm(b):
    """小さい絵の作り置き（元絵・白黒・範囲）。画面が重くならないように"""
    if TEST:
        raise RuntimeError("試しの起動（--test）では作業を動かしません")

    def run():
        names = src_names()
        n = 0
        for i, nm in enumerate(names):
            if A.JOBS.stop_flag:
                return -1
            for k in ("src", "depth", "region"):
                try:
                    kimg({"k": k, "n": nm if k != "depth" else "depthref_" + nm, "w": "240"})
                    n += 1
                except Exception:
                    pass
            if i % 100 == 99:
                A.log("  小さい絵 %d / %d" % (i + 1, len(names)))
        A.log("小さい絵を作り置きしました（%d 枚）" % n)
        return 0
    A.JOBS.add("小さい絵を作り置きする（元絵・白黒・範囲）", func=run)
    return "並べました：小さい絵の作り置き（グラフィックボードは使いません）"


# ---------------------------------------------------------------- B2 構図の登録（model.json の pose_control・3章の決まり）
TECH2SET = {"hj": ["handjob"], "kiss": ["kiss"], "nipple": ["nipple"], "finger": ["fingering", "prostate"], "peg": ["peg"], "foot": ["footjob"],
            "ear": ["ear", "ear_soft"], "whisper": ["ear_soft", "ear"], "urethra": ["urethra"], "chastity": ["chastity"], "armpit": ["armpit"],
            "thigh": ["thigh"], "chest": ["seat_chest", "stand_chest"], "drain": ["energy_drain"], "bloodsuck": ["bloodsuck"], "bound": ["bondage"],
            "straddle": ["straddle"], "hug": ["close_hug", "stand_embrace"], "smother": ["smother"], "paizuri": ["paizuri"], "rusty": ["rusty"],
            "rimjob": ["rusty"], "rah": ["rah", "rah_behind"], "buttjob": ["buttjob"], "step": ["step"], "collar": ["collar"]}
POSTURE_SAMPLES = [("lie", "he lies on the bed"), ("fours", "he is on all fours"), ("sit", "he sits on a chair"), ("stand", "he stands"),
                   ("kneel", "he kneels"), ("hang", "he is suspended, hanging by his wrists")]
VIEW_TAG = {"pov": "pov", "side": "from side", "front": "from front", "behind": "from behind", "above": "from above", "low": "from below, low angle", "close": "close-up"}
HERO_ROLE = {"lie": "the navy-haired man lies on his back", "prone": "the navy-haired man lies face down", "sit": "the navy-haired man sits",
             "stand": "the navy-haired man stands", "bent": "the navy-haired man bends forward", "fours": "the navy-haired man is on all fours",
             "kneel": "the navy-haired man kneels", "hang": "the navy-haired man is suspended by his wrists"}
PART_ROLE = {"on": "the other character sits on top of him", "back": "the other character is behind him", "beside": "the other character is beside him",
             "between": "the other character is between his legs", "lap": "the other character sits on his lap", "sides": "two other characters are on both sides of him",
             "sandwich": "two other characters sandwich him from the front and the back", "facing": "the other character faces him",
             "over": "the other character leans over him"}
POSTURE_OF_ITEM = {"lie": "lie", "prone": "fours", "bent": "fours", "fours": "fours", "sit": "sit", "stand": "stand", "kneel": "kneel", "hang": ""}
ROW_JA = {"lie": "寝ている場面", "fours": "四つんばい・前かがみの場面", "sit": "座っている場面", "stand": "立っている場面", "kneel": "ひざまずく場面", "hang": "吊られている場面"}


def row_kind(r):
    """ref_sets の1行が、どんな場面に当たる行か（例文を当てて決める）"""
    if r.get("default"):
        return "default", "予備（姿勢の行のどれにも当たらないとき）"
    w = r.get("when") or ""
    if not w:
        return "always", "いつも（姿勢を問わない）"
    hit = []
    for k, t in POSTURE_SAMPLES:
        try:
            if re.search(w, t, re.I) and not (r.get("not") and re.search(r["not"], t, re.I)):
                hit.append(k)
        except re.error:
            pass
    if len(hit) == 1:
        return hit[0], ROW_JA[hit[0]]
    return "other", "そのほかの条件の行" + (("（" + "・".join(ROW_JA[h] for h in hit) + "）") if hit else "")


def reg_info(q):
    comp = q.get("comp", "")
    if not re.match(r"^[a-z0-9_]+$", comp or ""):
        raise RuntimeError("構図名が違います")
    P = pc()
    wm = word_map()
    reg = registered()
    it = next((r for r in items_table() if r["構図名"] == comp), None) or {}
    items = {k: it.get(k, "") for k in ITEM_KEYS + ["同時の技"]}
    try:
        drafts = sorted(f[5:-4] for f in os.listdir(CIN()) if re.match(r"^pose_depthref_%s(?:_\d+)?\.png$" % re.escape(comp), f))
    except OSError:
        drafts = []
    ex = {x.lower() for x in P.get("ref_exclude") or []}
    rp = P.get("ref_posture") or {}
    want = POSTURE_OF_ITEM.get(items.get("姿勢", ""), "")
    sug_sets = []
    if items.get("人数") in ("two", "three"):
        sug_sets.append("multi")
    if items.get("技") == "peg" and items.get("同時の技") == "nipple":
        sug_sets.append("peg_nipple")
    for t in (items.get("技"), items.get("同時の技")):
        for x in TECH2SET.get(t or "", []):
            if x not in sug_sets:
                sug_sets.append(x)
    sets = []
    for name, rows in (P.get("ref_sets") or {}).items():
        out = []
        for i, r in enumerate(rows or []):
            k, lab = row_kind(r)
            comps = r.get("comps") or []
            out.append(dict(i=i, kind=k, label=lab, comps=[dict(c=c, r=reading(c, wm), p=rp.get(c, "")) for c in comps],
                            has=comp in comps, suggest=bool(name in sug_sets and ((want and k == want) or (not want and k == "always")))))
        sets.append(dict(name=name, rows=out, suggest=name in sug_sets))
    sets.sort(key=lambda x: (not x["suggest"], x["name"]))
    role = ", ".join(x for x in (HERO_ROLE.get(items.get("姿勢", ""), ""), PART_ROLE.get(items.get("位置", ""), "")) if x)
    if items.get("視点") == "pov":
        role = "seen through the navy-haired man's eyes, the other character faces the viewer" + (
            (", " + PART_ROLE[items["位置"]].replace("him", "the viewer")) if items.get("位置") in PART_ROLE else "")
    return dict(comp=comp, reading=reading(comp, wm), registered=comp in reg, reg_sets=reg.get(comp) or [], items=items,
                drafts=[dict(d=d, ex=d.lower() in ex) for d in drafts], sets=sets,
                tags=(P.get("ref_tags") or {}).get(comp) or VIEW_TAG.get(items.get("視点", ""), ""),
                role=(P.get("ref_role") or {}).get(comp) or role, posture=rp.get(comp, want),
                extra=(comp in set(P.get("ref_extra") or [])) if comp in reg else True, busy=busy(), test=TEST)


def _reg_apply(d, b):
    """model.json（d）に登録を足す。変わる所の説明のリストを返す"""
    comp = b.get("comp", "")
    if not re.match(r"^[a-z0-9_]+$", comp or ""):
        raise RuntimeError("構図名が違います")
    P = d.setdefault("pose_control", {})
    rows = [(str(x[0]), int(x[1])) for x in b.get("rows") or []]
    if not rows:
        raise RuntimeError("合う組（行）を1つ以上選んでください。合う組が無い構図は画面からは登録しません（「新しい構図」に残して Claude に頼む）")
    try:
        have = [f for f in os.listdir(CIN()) if re.match(r"^pose_depthref_%s(?:_\d+)?\.png$" % re.escape(comp), f)]
    except OSError:
        have = []
    if not have:
        raise RuntimeError("この構図の白黒の下書き（ComfyUI の input の pose_depthref_%s.png）がまだありません。先に元絵を取り込んでください" % comp)
    tags, role = (b.get("tags") or "").strip(), (b.get("role") or "").strip()
    posture = (b.get("posture") or "").strip()
    if posture not in ("", "lie", "fours", "sit", "stand", "kneel"):
        raise RuntimeError("姿勢が違います")
    if not role:
        raise RuntimeError("役の文（誰がどこにいるか）を入れてください")
    if re.search(r"\b(?:child|children|loli|shota|kid|teen|teenage|young boy|young girl|underage)\b", tags + " " + role, re.I):
        raise RuntimeError("視点・役の文に、幼さにつながる語は入れられません")
    diff = []
    sets = P.get("ref_sets") or {}
    for sname, i in rows:
        if sname not in sets or not (0 <= i < len(sets[sname])):
            raise RuntimeError("その組はありません: %s %d" % (sname, i))
        r = sets[sname][i]
        r.setdefault("comps", [])
        if comp not in r["comps"]:
            r["comps"].append(comp)
            diff.append("ref_sets「%s」の %d 行目（%s）に %s を足す（%d 個 → %d 個）" % (sname, i + 1, row_kind(r)[1], comp, len(r["comps"]) - 1, len(r["comps"])))
    for key, val, lab in (("ref_tags", tags, "視点"), ("ref_role", role, "役の文")):
        m = P.setdefault(key, {})
        if val and m.get(comp) != val:
            diff.append("%s（%s）：%s → %s" % (key, lab, m.get(comp) or "なし", val))
            m[comp] = val
    rp = P.setdefault("ref_posture", {})
    if posture and rp.get(comp) != posture:
        diff.append("ref_posture（姿勢）：%s → %s" % (rp.get(comp) or "なし", posture))
        rp[comp] = posture
    ext = P.setdefault("ref_extra", [])
    if b.get("extra") and comp not in ext:
        ext.append(comp)
        diff.append("ref_extra（替え専用）に %s を足す（重なったときの替えにだけ使う）" % comp)
    if not b.get("extra") and comp in ext:
        ext.remove(comp)
        diff.append("ref_extra（替え専用）から %s を外す（最初の候補にもなる）" % comp)
    return diff


def reg_plan(b):
    d = json.loads(json.dumps(model()))
    diff = _reg_apply(d, b)
    return dict(diff=diff, busy=busy(), test=TEST,
                note="書き換える前に model.json の控えを取ります。年齢に関わる設定は変えません。書いたあとは下見をやり直してください。")


def reg_do(b):
    if not b.get("confirmed"):
        raise RuntimeError("変わる所を確かめてから「確認した。登録する」を押してください")
    need_idle("構図の登録")
    with LOCK:
        d = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
        diff = _reg_apply(d, b)
        if not diff:
            return "変わる所がありません（もう登録してあります）"
        bname = model_write(d, "構図%s登録" % b["comp"])
    if b.get("items"):
        save_items_row(b["comp"], b["items"], "登録画面")
    add_memo("構図の登録", b["comp"], "登録", "／".join(diff)[:300])
    _AC["k"] = None
    return "登録しました：%s（控え %s）。%s" % (b["comp"], bname, queue_preview_after("構図の登録"))


# ---------------------------------------------------------------- B3 確認撮影（gen.py --control-sample を呼ぶだけ）
CHECK_DIR = lambda: os.path.join(A.P_out(), "構図下書き確認")
CHECK_POINTS = ["役が逆になっていないか（相手が攻め・主人公が受け）", "主人公が筋肉質・大柄になっていないか", "主人公が女性の体になっていないか",
                "頭が切れていないか", "相手の服や翼が主人公に移っていないか", "人物が幼く見えないか"]


def _id_hits(i, pvrows):
    """確認撮影の対象（構図名か下書き名）に、今の下見で当たっている場面"""
    out = []
    for (m, n), r in pvrows.items():
        d = (r.get("下書き") or "").strip()
        if not is_scene(n) or not d.startswith("depthref_"):
            continue
        if d.lower() == i.lower() or ("depthref_" + i).lower() == d.lower() or comp_of(d) == i:
            out.append([m, n, d])
    return out


def _siblings(comp, pvrows):
    """当たる場面が無い構図（替え専用など）：同じ組の同じ行の、ほかの構図が当たっている場面（＝この構図も選ばれうる場面）"""
    P = pc()
    rows = [r for rs in (P.get("ref_sets") or {}).values() for r in rs or [] if comp in (r.get("comps") or [])]
    mates = {c for r in rows for c in (r.get("comps") or []) if c != comp}
    out = []
    for (m, n), r in pvrows.items():
        d = (r.get("下書き") or "").strip()
        if is_scene(n) and d.startswith("depthref_") and comp_of(d) in mates:
            out.append([m, n, d])
    return out


def check_plan(q):
    ids = [x for x in re.split(r"[,\s、]+", q.get("ids", "")) if x]
    pvrows = preview()[0]
    out = []
    for i in ids:
        i = i[9:] if i.startswith("depthref_") and comp_of(i) == i[9:] else i
        hits = _id_hits(i, pvrows)
        comp = comp_of(i)
        sib = _siblings(comp, pvrows) if not hits else []
        out.append(dict(id=i, comp=comp, reading=reading(i, word_map()), hits=len(hits), mods=len({h[0] for h in hits}),
                        sample=hits[:6], sib=len(sib)))
    return dict(rows=out, points=CHECK_POINTS, busy=busy(), test=TEST, age=preview_age())


def check_run(b):
    need_idle("確認撮影")
    ids = [x for x in (b.get("ids") or []) if re.match(r"^[a-z0-9_]+$", x)]
    if not ids:
        raise RuntimeError("撮る下書き（構図名か下書き名）を選んでください")
    n = max(1, min(4, int(b.get("n") or 2)))
    pvrows = preview()[0]
    auto, simple = [], []
    for i in ids:
        (auto if _id_hits(i, pvrows) else simple).append(i)
    jobs, msg = [], []   # 先に全部を確かめてから並べる（途中で止まって半分だけ並ぶことがないように）
    if auto:
        jobs.append(("確認撮影（%s・%d場面ずつ、下書きあり／なし）" % ("、".join(auto), n),
                     [A.PY, "gen.py", "all", "all", "--model", "wai", "--control-sample", str(n), "--control-id",
                      ",".join(i if comp_of(i) == i else "depthref_" + i for i in auto)]))   # 下書き1枚は depthref_ つきで渡す（gen.py の絞り方）
        msg.append("今の割り当てで当たる場面から撮る：%s" % "、".join(auto))
    for i in simple:   # 当たる場面が無い構図：同じ組の行の場面を選び、その下書きを当てて撮る（簡易。人物の範囲は使わない）
        if not b.get("allow_simple"):
            raise RuntimeError("%s は、今の下見で当たる場面がありません（替え専用など）。「簡易で撮る」に印を付けると、同じ組の場面に当てて撮ります" % i)
        comp = comp_of(i)
        draft = i if i.startswith("depthref_") else ("depthref_" + i if os.path.exists(os.path.join(CIN(), "pose_depthref_%s.png" % i)) else "")
        if not draft:
            cand = sorted(f[5:-4] for f in os.listdir(CIN()) if re.match(r"^pose_depthref_%s(?:_\d+)?\.png$" % re.escape(comp), f))
            draft = cand[0] if cand else ""
        if not draft:
            raise RuntimeError("%s の白黒の下書きがありません" % i)
        sib = _siblings(comp, pvrows)
        if not sib:
            raise RuntimeError("%s は、同じ組の場面も見つかりません（登録してから撮ってください）" % i)
        step = max(1, len(sib) // n)
        pick = sib[::step][:n]
        for mod in sorted({p[0] for p in pick}):
            names = [p[1] for p in pick if p[0] == mod]
            jobs.append(("確認撮影・簡易（%s を %s に当てる）" % (draft, mod),
                         [A.PY, "gen.py", mod, ",".join(names), "--model", "wai", "--pose-image", draft, "--out", "構図下書き確認/簡易_%s/あり" % draft]))
        msg.append("簡易（範囲なし）で撮る：%s" % draft)
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません：" + "／".join(t for t, _ in jobs))
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    for t, argv in jobs:
        add_job(t, argv)
    return "並べました。" + "／".join(msg) + "。撮り終わったら、下の「撮った確認の絵」で見てください。"


SHOT_N = re.compile(r"^(.+?)_(\d{5})_\.png$")


def check_list(q):
    base = CHECK_DIR()
    out = []
    try:
        ds = sorted(os.listdir(base))
    except OSError:
        ds = []
    for d in ds:
        p = os.path.join(base, d)
        if not os.path.isdir(p):
            continue
        n = 0
        mt = 0
        for sub in ("あり", "なし"):
            try:
                fs = [f for f in os.listdir(os.path.join(p, sub)) if f.endswith(".png")]
            except OSError:
                fs = []
            n += len(fs)
            mt = max([mt] + [os.path.getmtime(os.path.join(p, sub, f)) for f in fs])
        name = d[4:] if d.startswith("ref_") else d
        out.append(dict(dir=d, name=name, reading=("相手ごとの文の試し：" + d[5:]) if d.startswith("相手ごと_") else reading(name, word_map()) if not d.startswith("簡易_") else "簡易：" + reading(d[3:], word_map()),
                        n=n, time=time.strftime("%Y-%m-%d %H:%M", time.localtime(mt)) if mt else "", mt=mt))
    out.sort(key=lambda x: -x["mt"])
    return dict(dirs=out, points=CHECK_POINTS)


def check_imgs(q):
    d = q.get("dir", "")
    if not _SAFE.match(d or "") or ".." in d:
        raise RuntimeError("名前が違います")
    p = os.path.join(CHECK_DIR(), d)
    pairs = {}
    for sub in ("あり", "なし"):
        try:
            fs = sorted(f for f in os.listdir(os.path.join(p, sub)) if f.endswith(".png"))
        except OSError:
            fs = []
        for f in fs:
            m = SHOT_N.match(f)
            key = m.group(1) if m else f
            pairs.setdefault(key, {})[sub] = f   # 同じ名前は新しい番号が後に来るので、いちばん新しいものが残る
    return dict(dir=d, pairs=[dict(key=k, yes=v.get("あり", ""), no=v.get("なし", "")) for k, v in sorted(pairs.items())], points=CHECK_POINTS)


def check_img(q, w):
    d, sub, f = q.get("dir", ""), q.get("sub", ""), q.get("f", "")
    if sub not in ("あり", "なし") or not all(_SAFE.match(x or "") and ".." not in x for x in (d, f)):
        raise RuntimeError("名前が違います")
    p = os.path.join(CHECK_DIR(), d, sub, f)
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません")
    if not w:
        return open(p, "rb").read(), "image/png"
    return _thumb_from(p, "check|" + p, w), "image/jpeg"


# ---------------------------------------------------------------- B7 白黒の下書きの自動点検（画像生成\\奥行き点検.py の結果を見て決める）
P_DCHECK = lambda: os.path.join(DRAFT(), "_奥行き点検.csv")
DC_HEAD = ["下書きの名前", "元絵の名前", "構図名", "印の種類", "検出の方法", "メモ", "判定", "相手の種類"]
PART_KINDS = ["翼", "尻尾", "角", "蛇の胴", "触手", "多い腕", "機械", "獣耳", "蜘蛛の脚"]


def depth_check(q):
    head, rows = read_dicts(P_DCHECK())
    ex = {x.lower() for x in pc().get("ref_exclude") or []}
    wm = word_map()
    by = {}
    for r in rows:
        d = r["下書きの名前"]
        x = by.setdefault(d, dict(draft=d, src=r["元絵の名前"], comp=r["構図名"], flags=[], verdict=r.get("判定", ""), kinds=r.get("相手の種類", ""),
                                  excluded=d.lower() in ex, reading=reading(r["構図名"], wm)))
        if r.get("印の種類"):
            x["flags"].append(dict(kind=r["印の種類"], how=r["検出の方法"], memo=r["メモ"]))
        x["verdict"] = x["verdict"] or r.get("判定", "")
        x["kinds"] = x["kinds"] or r.get("相手の種類", "")
    try:
        t = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(rpath(P_DCHECK()))))
    except OSError:
        t = ""
    try:
        total = len([f for f in os.listdir(DRAFT()) if f.startswith("depthref_") and f.endswith(".png")])
    except OSError:
        total = 0
    return dict(rows=list(by.values()), time=t, total=total, part_kinds=PART_KINDS)


def depth_decide(b):
    d = b.get("draft", "")
    if not d.startswith("depthref_"):
        raise RuntimeError("下書きの名前が違います")
    verdict = (b.get("verdict") or "").strip()
    if verdict not in ("", "問題なし", "外す"):
        raise RuntimeError("判定が違います")
    kinds = [k for k in (b.get("kinds") or []) if k in PART_KINDS]
    with LOCK:
        head, rows = read_dicts(P_DCHECK())
        if not head:
            head = DC_HEAD
        hit = [r for r in rows if r["下書きの名前"] == d]
        if not hit:
            n = d[9:]
            r = dict(下書きの名前=d, 元絵の名前=n, 構図名=re.sub(r"_\d+$", "", n), 印の種類="", 検出の方法="", メモ="")
            rows.append(r)
            hit = [r]
        for r in hit:
            if "verdict" in b:
                r["判定"] = verdict
            if "kinds" in b:
                r["相手の種類"] = "・".join(kinds)
        write_dicts(P_DCHECK(), head, rows, backup="奥行き点検_画面から直す")
    if "kinds" in b:   # B8：付属物は下書きの項目の表にも入れる
        trait_save({"name": d[9:], "parts": kinds})
    add_memo("奥行きの点検", d, verdict or ("相手の種類：" + "・".join(kinds) if "kinds" in b else "未定に戻す"), b.get("why", ""))
    return "書きました：%s（%s）" % (d, verdict or "・".join(kinds) or "未定")


def depth_run(b):
    add_job("白黒の下書きの自動点検（グラフィックボードは使いません）", [A.PY, "奥行き点検.py"])
    return "並べました：白黒の下書きの自動点検（数分）。終わったら一覧を読み直してください"


# ---------------------------------------------------------------- B8 下書きの項目（胸・体つき・付属物・胸を使う構図か）と、相手の種類での当て分けの入り切り
P_TRAITS = lambda: os.path.join(DRAFT(), "_下書きの項目.json")
BREASTS = ["平ら", "小さめ", "あり", "写らない"]
BODIES = ["", "細身", "くびれと尻が強い"]


def traits_all():
    try:
        return json.load(open(rpath(P_TRAITS()), encoding="utf-8"))
    except Exception:
        return {}


def traits_get(q):
    T = traits_all()
    ex = {x.lower() for x in pc().get("ref_exclude") or []}
    wm = word_map()
    rows = []
    for n in src_names():
        t = T.get(n) or {}
        rows.append(dict(name=n, comp=re.sub(r"_\d+$", "", n), reading=reading(n, wm), chest=t.get("胸", ""), body=t.get("体つき", ""),
                         parts=t.get("付属物") or [], use=bool(t.get("胸を使う")), checked=bool(t.get("確認")), how=t.get("作り方", ""),
                         excluded=("depthref_" + n).lower() in ex, has=bool(t), wd=wd_guess(n)))
    return dict(rows=rows, breasts=BREASTS, bodies=BODIES, parts=PART_KINDS, on=truthy(pc().get("trait_filter", False)), busy=busy(), test=TEST)


def trait_save(b):
    n = b.get("name", "")
    if n not in set(src_names()):
        raise RuntimeError("その下書きはありません: " + n)
    with LOCK:
        T = traits_all()
        t = T.setdefault(n, {})
        if "chest" in b:
            if b["chest"] not in BREASTS:
                raise RuntimeError("胸の選び方が違います")
            t["胸"] = b["chest"]
        if "body" in b:
            if b["body"] not in BODIES:
                raise RuntimeError("体つきの選び方が違います")
            t["体つき"] = b["body"]
        if "parts" in b:
            t["付属物"] = [p for p in b["parts"] if p in PART_KINDS]
        if "use" in b:
            t["胸を使う"] = bool(b["use"])
        t["確認"] = bool(b.get("checked", True))
        t["作り方"] = "画面（%s）" % now()
        backup_data(P_TRAITS(), "下書きの項目_画面から直す")
        w = wpath(P_TRAITS())
        with open(w + ".tmp", "w", encoding="utf-8") as f:
            json.dump(T, f, ensure_ascii=False, indent=1)
        os.replace(w + ".tmp", w)
    return "保存しました：%s" % n


def trait_switch_plan(b):
    on = bool(b.get("on"))
    cur = truthy(pc().get("trait_filter", False))
    return dict(on=on, cur=cur, busy=busy(), test=TEST,
                diff=[] if on == cur else ["pose_control.trait_filter：%s → %s" % ("入" if cur else "切", "入" if on else "切")],
                note="入れると、男の娘には胸のある下書き・胸を使う構図を当てず、人の相手には翼・尻尾などのある下書きを当てず、翼などのある相手には同じ物のある下書きを優先します。"
                     "今の選び方で合っている場面はそのままで、合わない場面だけ替わります。撮り済みの絵は自動では撮り直しません。")


def trait_switch(b):
    if not b.get("confirmed"):
        raise RuntimeError("確認を押してから切り替えてください")
    need_idle("当て分けの切り替え")
    on = bool(b.get("on"))
    with LOCK:
        d = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
        P = d.setdefault("pose_control", {})
        if truthy(P.get("trait_filter", False)) == on:
            return "もう%sになっています" % ("入" if on else "切")
        P["trait_filter"] = on
        P["trait_filter_memo"] = "2026-10-05 相手の種類で下書きを当て分ける（構図下書き\\_下書きの項目.json）。まとめツールの「下書きの項目」タブで入り切り"
        bname = model_write(d, "相手の種類の当て分けを%s" % ("入れる" if on else "切る"))
    return "当て分けを%sにしました（控え %s）。%s" % ("入" if on else "切", bname, queue_preview_after("当て分けの切り替え"))


# ---------------------------------------------------------------- B6 相手ごとの文（相手が2人の場面・prompts_相手ごと\\<MOD>.json。今の prompts は書き換えない）
def P_SPLIT(code):
    return os.path.join(IMG(), "prompts_相手ごと", code + ".json")


def split_all(code):
    try:
        return json.load(open(rpath(P_SPLIT(code)), encoding="utf-8"))
    except Exception:
        return {}


def split_get(q):
    code = A.codes_arg([q.get("code", "")])[0]
    n = q.get("name", "")
    e = split_all(code).get(n) or {}
    r = preview()[0].get((code, n)) or {}
    d = (r.get("下書き") or "").strip()
    masks = d.startswith("depthref_") and all(os.path.exists(os.path.join(CIN(), "pose_%s_partner%d.png" % (d, k))) for k in (1, 2))
    return dict(code=code, name=n, a=e.get("相手1", ""), b=e.get("相手2", ""), memo=e.get("メモ", ""), draft=d, masks=bool(masks), busy=busy(), test=TEST)


def split_save(b):
    code = A.codes_arg([b.get("code", "")])[0]
    n = b.get("name", "")
    if n not in prompts_of(code):
        raise RuntimeError("その画像名はありません: " + n)
    a, c = (b.get("a") or "").strip(), (b.get("b") or "").strip()
    for t in (a, c):
        if re.search(r"\b(?:child|children|loli|shota|kid|teen|teenage|young boy|young girl|underage|petite|small body)\b", t, re.I):
            raise RuntimeError("相手の見た目に、幼さにつながる語は入れられません")
    with LOCK:
        d = split_all(code)
        if a or c:
            d[n] = {"相手1": a, "相手2": c, "メモ": (b.get("memo") or "").strip(), "日時": now()}
        else:
            d.pop(n, None)
        p = P_SPLIT(code)
        backup_data(p, "相手ごとの文_画面から直す")
        w = wpath(p)
        os.makedirs(os.path.dirname(w), exist_ok=True)
        with open(w + ".tmp", "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
        os.replace(w + ".tmp", w)
    add_memo("相手ごとの文", n, "保存" if (a or c) else "消す", "")
    return "相手ごとの文を%s：%s（相手1と相手2の両方が入っていて、下書きに相手ごとの範囲があるときだけ使われます）" % ("保存しました" if (a or c) else "消しました", n)


def split_try(b):
    """その場面を、相手ごとの文あり／なし（同じシード）で1枚ずつ試しに撮る → output\\構図下書き確認\\相手ごと_<画像名>\\"""
    need_idle("試し撮り")
    code = A.codes_arg([b.get("code", "")])[0]
    n = b.get("name", "")
    if not re.match(r"^[A-Za-z0-9_]+$", n) or n not in prompts_of(code):
        raise RuntimeError("その画像名はありません: " + n)
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    out = "構図下書き確認/相手ごと_%s" % n
    add_job("試し撮り %s（相手ごとの文あり）" % n, [A.PY, "gen.py", code, n, "--model", "wai", "--redo", "--out", out + "/あり"])
    add_job("試し撮り %s（相手ごとの文なし）" % n, [A.PY, "gen.py", code, n, "--model", "wai", "--redo", "--no-partner-split", "--out", out + "/なし"])
    return "並べました。撮り終わったら「確認撮影」タブの「撮った確認の絵」の「相手ごと_%s」で見比べてください。" % n


# ---------------------------------------------------------------- B4 似た構図を上に出す（画像生成\\似た構図の下ごしらえ.py が作った特徴で比べる）
_SIM = {"mt": None}


def sim_data():
    p = os.path.join(DRAFT(), "_似た構図_特徴.npz")
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return None
    if _SIM.get("mt") != mt:
        try:
            import numpy as np
        except Exception:
            return None
        z = np.load(p, allow_pickle=False)
        _SIM.update(mt=mt, keys=json.loads(str(z["keys"])), E=z["emb"], EF=z["emb_flip"])
    return _SIM


def similar(q):
    """選んだ候補に形の近い構図（元絵の中で一番近い1枚の近さ。左右反転も比べる）。目安"""
    f = q.get("file", "")
    d = sim_data()
    if d is None:
        return dict(ready=False, why="似た構図の下ごしらえがまだです（「下ごしらえをする」を押してください）")
    idx = [i for i, k in enumerate(d["keys"]) if k[0] == "cand" and k[1] == f]
    if not idx:
        return dict(ready=False, why="この候補の特徴がまだありません（新しく置いた候補は「下ごしらえをする」を押すと比べられます）")
    import numpy as np
    e = d["E"][idx[0]]
    src = [i for i, k in enumerate(d["keys"]) if k[0] == "src"]
    sc = np.maximum(d["E"][src] @ e, d["EF"][src] @ e)
    best = {}
    for i, v in zip(src, sc):
        n = d["keys"][i][1]
        c = re.sub(r"_\d+$", "", n)
        if float(v) > best.get(c, (-9, ""))[0]:
            best[c] = (float(v), n)
    top = sorted(best.items(), key=lambda x: -x[1][0])
    return dict(ready=True, comps={c: dict(score=round(v, 3), sample=n) for c, (v, n) in top}, order=[c for c, _ in top])


def similar_run(b):
    need_idle("似た構図の下ごしらえ")
    add_job("似た構図の下ごしらえ（グラフィックボードを使います）", [A.PY, "似た構図の下ごしらえ.py"])
    return "並べました：似た構図の下ごしらえ（新しい絵だけ作ります）"


# ---------------------------------------------------------------- B5 相手の種類の自動入力（WD14 の案。画像生成\\相手の種類の自動入力.py が作る）
WD_TH = 0.35
WD_PART = [("翼", r"(^|_)wings?$"), ("尻尾", r"(^|_)tails?$"), ("角", r"(^|_)horns?$"), ("蛇の胴", r"^lamia$|snake_tail|^naga$"),
           ("触手", r"tentacles?$"), ("蜘蛛の脚", r"arachne|spider_girl|extra_legs"), ("多い腕", r"extra_arms"), ("機械", r"^robot$|mechanical_arms|^cyborg$")]
WD_CHEST = [("平ら", "flat_chest"), ("小さめ", "small_breasts"), ("あり", "medium_breasts"), ("あり", "large_breasts"), ("あり", "huge_breasts"), ("あり", "gigantic_breasts")]
_WD = {"mt": None, "d": {}}


def wd_all():
    p = os.path.join(DRAFT(), "_WD14タグ.json")
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return {}
    if _WD["mt"] != mt:
        _WD.update(mt=mt, d=json.load(open(p, encoding="utf-8")))
    return _WD["d"]


def wd_guess(n):
    t = (wd_all().get(n) or {}).get("tags")
    if t is None:
        return None
    parts = [p for p, rx in WD_PART if any(v >= WD_TH and re.search(rx, k) for k, v in t.items())]
    if "蛇の胴" in parts and "尻尾" in parts:   # ラミアの蛇の胴を「尻尾」と読むことがある
        parts.remove("尻尾")
    sc, lab = max(((t.get(k, 0), lab) for lab, k in WD_CHEST), default=(0, ""))
    top = [k for k, v in sorted(t.items(), key=lambda x: -x[1]) if re.search(r"wing|tail|horn|breast|chest|tentacle|lamia|arachne|robot|extra_", k) and v >= WD_TH][:6]
    return dict(parts=parts, chest=lab if sc >= WD_TH else "写らない", tags=top)


def wd_apply(b):
    n = b.get("name", "")
    g = wd_guess(n)
    if g is None:
        raise RuntimeError("この下書きの WD14 の案がまだありません（「WD14 をかける」を押してください）")
    cur = (traits_all().get(n) or {}).get("付属物") or []
    return trait_save({"name": n, "parts": cur + [p for p in g["parts"] if p not in cur], "checked": False}) + "（WD14 の付属物を足しました。絵を見て確かめたら保存してください）"


def wd_apply_all(b):
    """まだ確かめていない下書きの付属物に、WD14 の案を足す（今の印は消さない。WD14 が見落とすもの〈蜘蛛の脚など〉があるため。胸と確かめた下書きは変えない）"""
    T = traits_all()
    n = 0
    with LOCK:
        for name in src_names():
            t = T.setdefault(name, {})
            if t.get("確認"):
                continue
            g = wd_guess(name)
            if g is None:
                continue
            cur = t.get("付属物") or []
            add = [p for p in g["parts"] if p not in cur]
            if add:
                t["付属物"] = cur + add
                t["作り方"] = "WD14 の付属物（%s）" % now()
                n += 1
        backup_data(P_TRAITS(), "下書きの項目_WD14を入れる")
        w = wpath(P_TRAITS())
        with open(w + ".tmp", "w", encoding="utf-8") as f:
            json.dump(T, f, ensure_ascii=False, indent=1)
        os.replace(w + ".tmp", w)
    add_memo("下書きの項目", "（まだ確かめていない全部）", "WD14 の付属物を足す", "%d 枚" % n)
    return "WD14 の付属物を足しました（%d 枚。今の印は消していません。確かめた下書きは変えていません）" % n


def wd_run(b):
    need_idle("WD14 をかける")
    add_job("相手の種類の自動入力（WD14 をかける・グラフィックボードを使います）", [A.PY, "相手の種類の自動入力.py"])
    return "並べました：WD14 をかける（新しい絵だけ）"


# ---------------------------------------------------------------- 相手キャラの LoRA（Lora用\\chara の道具を呼ぶ・2026-10-05）
CL_CHARS = ["master", "e1", "e2", "e3", "boss"]
CL_JA = {"master": "マスター", "e1": "下級1（e1）", "e2": "下級2（e2）", "e3": "下級3（e3）", "boss": "上級（boss）"}
LORA_ROOT = lambda: os.path.join(os.path.expanduser("~"), "Downloads", "Lora用")
CL_DIR = lambda: os.path.join(LORA_ROOT(), "chara")
CL_VENV = lambda: os.path.join(LORA_ROOT(), "sd-scripts", "venv", "Scripts", "python.exe")
CL_DS = lambda: os.path.join(A.P_out(), "chara_ds")
CL_DATA = lambda: os.path.join(LORA_ROOT(), "学習データ_chara")
CL_LORAS = lambda: os.path.join(A.CONF["comfy_dir"], "ComfyUI", "models", "loras", "キャラ")
CL_TRY = "キャラLoRA確認"
CL_MIN = 12
CL_POINTS = ["そのキャラに見えるか（髪・目・服・付属物）", "崩れていないか（手足の数・顔・体のつながり）", "別人や2人目が出ていないか",
             "**幼く見えないか**（顔ではなく体で見る。小柄・子どもっぽい体の絵は外す）", "絵柄がそのMODの絵柄になっているか"]


def cl_style(code):
    s = A.styles().get(code, "")
    return "std" if s in ("", "本編", "標準", "none") else s


def cl_map(code):
    try:
        mj = json.load(open(rpath(P_MODEL()), encoding="utf-8"))
    except Exception:
        return {}
    return ((mj.get("mod_style") or {}).get("chara_map") or {}).get(code) or {}


def cl_tag(code, ch):
    return "%s_%s_%s" % (code, ch, cl_style(code))


def cl_pngs(d):
    try:
        return sorted(f for f in os.listdir(d) if f.lower().endswith(".png") and os.path.isfile(os.path.join(d, f)))
    except OSError:
        return []


def cl_status(code):
    P = prompts_of(code)
    cm = cl_map(code)
    try:
        lfs = os.listdir(CL_LORAS())
    except OSError:
        lfs = []
    out = []
    for ch in CL_CHARS:
        tag = cl_tag(code, ch)
        ds = os.path.join(CL_DS(), tag)
        own = sorted(f for f in lfs if f.startswith("chr_%s" % tag) and f.endswith(".safetensors"))
        e = cm.get(ch) or {}
        stand = (P.get("%s_%s" % (code, ch)) or {}).get("positive", "")
        out.append(dict(char=ch, ja=CL_JA[ch], tag=tag, has_prompt=bool(stand), shot=len(cl_pngs(ds)), rejected=len(cl_pngs(os.path.join(ds, "_外した"))),
                        data=len(cl_pngs(os.path.join(CL_DATA(), tag, "img"))), toml=os.path.exists(os.path.join(CL_DIR(), "toml", tag + ".toml")),
                        own=own, done=any(f.endswith("-000008.safetensors") for f in own),
                        mapped=(e.get("lora") or "") if e.get("enabled", True) is not False else "",
                        scenes=len(cl_scenes(code, ch)), ref=os.path.isfile(cl_ref_path(tag)), firsts=len(cl_pngs(os.path.join(CL_REF(), tag))),
                        checked=os.path.isfile(os.path.join(ds, "_確かめた.txt"))))
    return out


def chara_mods(q):
    md = A.mod_dirs()
    rows = []
    for code in mod_codes():
        st = cl_status(code)
        rows.append(dict(code=code, n=(md.get(code) or {}).get("n", 0), style=cl_style(code), chars=st,
                         shot=sum(1 for c in st if c["shot"]), done=sum(1 for c in st if c["done"]), mapped=sum(1 for c in st if c["mapped"])))
    return dict(mods=rows, points=CL_POINTS, venv=os.path.exists(CL_VENV()), tools=os.path.exists(os.path.join(CL_DIR(), "make_chara_ds_ref.py")),
                busy=busy(), comfy=A.comfy_state(), test=TEST)


def chara_imgs(q):
    code = A.codes_arg([q.get("code", "")])[0]
    ch = q.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    tag = cl_tag(code, ch)
    d = os.path.join(CL_DS(), tag)
    P = prompts_of(code)
    return dict(code=code, char=ch, tag=tag, files=cl_pngs(d), rejected=cl_pngs(os.path.join(d, "_外した")),
                stand=(P.get("%s_%s" % (code, ch)) or {}).get("positive", ""), min=CL_MIN, points=CL_POINTS)


def cl_img(q, w):
    tag, f = q.get("tag", ""), q.get("n", "")
    if not all(_SAFE.match(x or "") and ".." not in x for x in (tag, f)):
        raise RuntimeError("名前が違います")
    p = os.path.join(CL_DS(), tag, "_外した" if q.get("rej") == "1" else "", f)
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません")
    if not w:
        return open(p, "rb").read(), "image/png"
    return _thumb_from(p, "chara|" + p, w), "image/jpeg"


def chara_move(b):
    """学習用の絵を 外す（_外した へ移すだけ・消さない）／戻す"""
    code = A.codes_arg([b.get("code", "")])[0]
    ch = b.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    d = os.path.join(CL_DS(), cl_tag(code, ch))
    rej = os.path.join(d, "_外した")
    back = bool(b.get("back"))
    if TEST:
        raise RuntimeError("試しの起動（--test）では絵を動かしません")
    n = 0
    for f in b.get("files") or []:
        if not _SAFE.match(f) or ".." in f:
            continue
        src, dst = (os.path.join(rej, f), os.path.join(d, f)) if back else (os.path.join(d, f), os.path.join(rej, f))
        if os.path.isfile(src) and not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            n += 1
    add_memo("キャラLoRAの絵", cl_tag(code, ch), "戻す" if back else "外す", "%d 枚" % n)
    return "%d 枚を%s" % (n, "戻しました" if back else "外しました（_外した へ移しただけで、消していません）")


def chara_shoot(b):
    need_idle("学習用の絵の撮影")
    code = A.codes_arg([b.get("code", "")])[0]
    chars = [c for c in (b.get("chars") or CL_CHARS) if c in CL_CHARS]
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    have = [c for c in chars if os.path.isfile(cl_ref_path(cl_tag(code, c)))]
    if not have:
        raise RuntimeError("見本がまだありません。先に「1. 1枚目の候補を撮る」「2. 見本を選ぶ」をしてください。")
    wt = float(b.get("weight") or 0.6)
    if not 0.2 <= wt <= 1.0:
        raise RuntimeError("見本の効きは 0.2〜1.0 にしてください")
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    A.JOBS.add("キャラLoRAの学習用の絵を見本から撮る %s（%s・見本の効き %s）" % (code, ",".join(have), wt),
               [A.PY, "make_chara_ds_ref.py", code, "--chars", ",".join(have), "--ref-weight", str(wt)], CL_DIR())
    skip = [CL_JA[c] for c in chars if c not in have]
    return "並べました：見本から学習用の絵を撮る（1キャラ 32 枚）" + ("。見本が無いので飛ばしたキャラ：" + "、".join(skip) if skip else "")


# ---- 1枚目の見本から量産する（2026-10-05 ユーザー決定 案1：1枚目＝キャラLoRA＋絵柄LoRA、量産＝見本を IP-Adapter で参考にして絵柄LoRAだけ）
CL_REF = lambda: os.path.join(A.P_out(), "chara_ref")


def cl_ref_path(tag):
    return os.path.join(CIN(), "chara_ref_%s.png" % tag)


def cl_stands(code, ch):
    """今の立ち絵（ComfyUI\output\<MOD>_…\<MOD>_<キャラ>_00001_.png）"""
    rx = re.compile(r"^%s_%s_\d{5}_\.png$" % (re.escape(code), re.escape(ch)))
    out = []
    try:
        ds = [d for d in os.listdir(A.P_out()) if d.startswith(code + "_") and os.path.isdir(os.path.join(A.P_out(), d))]
    except OSError:
        ds = []
    for d in sorted(ds):
        out += [dict(src="stand", d=d, n=f) for f in cl_pngs(os.path.join(A.P_out(), d)) if rx.match(f)]
    return out


def cl_ref_from(tag):
    try:
        return open(os.path.join(CL_REF(), tag, "_選んだ見本.txt"), encoding="utf-8").read().strip()
    except OSError:
        return ""


def chara_refs(q):
    code = A.codes_arg([q.get("code", "")])[0]
    ch = q.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    tag = cl_tag(code, ch)
    e = cl_map(code).get(ch) or {}
    return dict(code=code, char=ch, tag=tag, firsts=[dict(src="first", n=f) for f in cl_pngs(os.path.join(CL_REF(), tag))],
                stands=cl_stands(code, ch), chosen=os.path.isfile(cl_ref_path(tag)), chosen_from=cl_ref_from(tag),
                mapped=(e.get("lora") or "") if e.get("enabled", True) is not False else "")


def cl_ref_src(q):
    tag, src, f = q.get("tag", ""), q.get("src", ""), q.get("n", "")
    if src == "chosen":
        if not _SAFE.match(tag or "") or ".." in tag:
            raise RuntimeError("名前が違います")
        return cl_ref_path(tag)
    if not all(_SAFE.match(x or "") and ".." not in x for x in (tag, f)):
        raise RuntimeError("名前が違います")
    if src == "first":
        return os.path.join(CL_REF(), tag, f)
    if src == "stand":
        d = q.get("d", "")
        if not _SAFE.match(d or "") or ".." in d:
            raise RuntimeError("名前が違います")
        return os.path.join(A.P_out(), d, f)
    raise RuntimeError("名前が違います")


def cl_ref_img(q, w):
    p = cl_ref_src(q)
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません")
    if not w:
        return open(p, "rb").read(), "image/png"
    return _thumb_from(p, "clref|%s|%s" % (p, os.path.getmtime(p)), w), "image/jpeg"


def chara_first(b):
    """1枚目の候補を撮る（ダウンロードしたキャラLoRA＋絵柄LoRA・1キャラ4枚）"""
    need_idle("1枚目の候補を撮る")
    code = A.codes_arg([b.get("code", "")])[0]
    chars = [c for c in (b.get("chars") or CL_CHARS) if c in CL_CHARS]
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    A.JOBS.add("キャラLoRAの1枚目の候補を撮る %s（%s）" % (code, ",".join(chars)), [A.PY, "make_chara_ds_ref.py", code, "--chars", ",".join(chars), "--first"], CL_DIR())
    return "並べました：1枚目の候補を撮る（1キャラ 4 枚）。撮り終わったら「2. 見本を選ぶ」で1枚選んでください。"


def chara_pick_ref(b):
    """選んだ絵を見本にする（ComfyUI\input\chara_ref_<タグ>.png に写す。前の見本は chara_ref\<タグ>\_前の見本_<日時>.png に残す）"""
    code = A.codes_arg([b.get("code", "")])[0]
    ch = b.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    tag = cl_tag(code, ch)
    src = cl_ref_src(dict(tag=tag, src=b.get("src", ""), n=b.get("n", ""), d=b.get("d", "")))
    if b.get("src") == "chosen" or not os.path.isfile(src):
        raise RuntimeError("絵がありません")
    if TEST:
        raise RuntimeError("試しの起動（--test）では見本を変えません")
    dst = cl_ref_path(tag)
    keep = os.path.join(CL_REF(), tag)
    os.makedirs(keep, exist_ok=True)
    if os.path.isfile(dst):
        shutil.copy2(dst, os.path.join(keep, "_前の見本_%s.png" % time.strftime("%Y%m%d_%H%M%S")))
    shutil.copy2(src, dst)
    what = ("今の立ち絵 %s\%s" % (b.get("d"), b.get("n"))) if b.get("src") == "stand" else ("1枚目の候補 %s" % b.get("n"))
    open(os.path.join(keep, "_選んだ見本.txt"), "w", encoding="utf-8").write("%s（%s）" % (what, now()))
    add_memo("キャラLoRAの見本", tag, "見本を選ぶ", what)
    return "見本にしました：%s" % what


# ---- MOD をまたいでまとめて進める（2026-10-05 ユーザー要望「全MODでまとめて選べるように」・A2 候補を撮って選ぶ・B1 場面のあるキャラだけ・合間に少しずつ）
CL_BATCH_STEPS = {"first": "1枚目の候補を撮る", "shoot": "見本から量産する", "train": "学習データを作って学習する"}


def cl_need(step, c):
    """そのキャラが、まとめて進める step の対象か（場面のあるキャラだけ）"""
    if not c["scenes"] or not c["has_prompt"] or c["done"]:
        return False
    if step == "first":
        return not c["ref"] and c["firsts"] < 4
    if step == "shoot":
        return c["ref"] and c["shot"] + c["rejected"] < 32 and not c["checked"]
    return False


def cl_batch_plan(step, codes, limit):
    """[(MOD, [キャラ…])]。limit はキャラの人数（0＝全部）"""
    out, n = [], 0
    for code in codes:
        st = cl_status(code)
        if step == "train":
            shot = [c for c in st if c["scenes"] and (c["shot"] or c["rejected"])]
            # その MOD の撮ったキャラを全部「確かめた」にしてから学習する（学習データは MOD ごとに作るので）
            if not shot or not all(c["checked"] for c in shot):
                continue
            todo = [c["char"] for c in shot if not c["done"] and c["shot"] >= CL_MIN]
        else:
            todo = [c["char"] for c in st if cl_need(step, c)]
        if limit:
            todo = todo[:max(0, limit - n)]
        if todo:
            out.append((code, todo))
            n += len(todo)
        if limit and n >= limit:
            break
    return out


def cl_codes(b):
    cs = b.get("codes") or []
    return mod_codes() if cs == "all" or not cs else A.codes_arg(cs)


def chara_batch_plan(q):
    """まとめて進める前の数（各段階の残り）"""
    codes = cl_codes({"codes": [x for x in (q.get("codes") or "").split(",") if x]})
    left = {k: 0 for k in CL_BATCH_STEPS}
    pick = refs = 0
    for code in codes:
        st = cl_status(code)
        for c in st:
            for k in ("first", "shoot"):
                left[k] += cl_need(k, c)
            if c["scenes"] and c["has_prompt"] and not c["ref"] and c["firsts"] >= 4:   # 撮っている途中のキャラは数えない
                refs += 1
            if c["scenes"] and c["shot"] and c["shot"] + c["rejected"] >= 32 and not c["checked"] and not c["done"]:
                pick += 1
    left["train"] = sum(len(x[1]) for x in cl_batch_plan("train", codes, 0))
    return dict(mods=len(codes), left=left, refs=refs, pick=pick, comfy=A.comfy_state(), busy=busy())


def chara_batch(b):
    step = b.get("step", "")
    if step not in CL_BATCH_STEPS:
        raise RuntimeError("段階が違います")
    limit = int(b.get("limit") or 0)
    codes = cl_codes(b)
    need_idle(CL_BATCH_STEPS[step])
    plan = cl_batch_plan(step, codes, limit)
    if not plan:
        raise RuntimeError("いま「%s」をするキャラはありません" % CL_BATCH_STEPS[step]
                           + ("（学習は、そのMODで撮ったキャラを全部「確かめた」にしてから並べます）" if step == "train" else ""))
    if TEST:
        raise RuntimeError("試しの起動（--test）では作業を並べません")
    n = sum(len(x[1]) for x in plan)
    if step == "train":
        if A.comfy_state()["up"]:
            raise RuntimeError("ComfyUI が起動しています。学習はグラフィックボードを取り合うので、ComfyUI の黒い画面を閉じてから押してください。")
        if not os.path.exists(CL_VENV()):
            raise RuntimeError("学習の道具（Lora用\sd-scripts）がありません。")
        for code, chars in plan:
            A.JOBS.add("キャラLoRAの学習データを作る %s" % code, [A.PY, "prep_chara.py", code], CL_DIR())
            A.JOBS.add("キャラLoRAを学習する %s（%s）" % (code, ",".join(chars)), [CL_VENV(), "train_chara.py", code], CL_DIR())
        add_memo("キャラLoRA（まとめて）", "%d MOD" % len(plan), CL_BATCH_STEPS[step], "%d キャラ" % n)
        return "並べました：%d MOD・%d キャラの学習（1キャラ 8〜17分）。終わるまで ComfyUI は起動しないでください。" % (len(plan), n)
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    for code, chars in plan:
        argv = [A.PY, "make_chara_ds_ref.py", code, "--chars", ",".join(chars), "--skip-done"] + (["--first"] if step == "first" else ["--ref-weight", str(float(b.get("weight") or 0.6))])
        A.JOBS.add("キャラLoRA %s %s（%s）" % (CL_BATCH_STEPS[step], code, ",".join(chars)), argv, CL_DIR())
    add_memo("キャラLoRA（まとめて）", "%d MOD" % len(plan), CL_BATCH_STEPS[step], "%d キャラ" % n)
    per = 4 if step == "first" else 32
    return "並べました：%d MOD・%d キャラ・最大 %d 枚（撮り済みは飛ばします。途中で止めても、次は続きから撮ります）" % (len(plan), n, n * per)


def chara_check(b):
    """量産した絵を「確かめた」にする／戻す（chara_ds\<タグ>\_確かめた.txt）"""
    code = A.codes_arg([b.get("code", "")])[0]
    ch = b.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    if TEST:
        raise RuntimeError("試しの起動（--test）では変えません")
    d = os.path.join(CL_DS(), cl_tag(code, ch))
    f = os.path.join(d, "_確かめた.txt")
    if b.get("on", True):
        n = len(cl_pngs(d))
        if n + len(cl_pngs(os.path.join(d, "_外した"))) < 32 and b.get("force") is not True:
            raise RuntimeError("まだ撮っている途中です（%d / 32 枚）。撮り終わってから確かめてください。" % (n + len(cl_pngs(os.path.join(d, "_外した")))))
        if n < CL_MIN:
            raise RuntimeError("残っている絵が %d 枚です。%d 枚以上残してください（足りなければ、このキャラだけ量産し直してください）" % (n, CL_MIN))
        os.makedirs(d, exist_ok=True)
        open(f, "w", encoding="utf-8").write("%s　%d 枚" % (now(), n))
        add_memo("キャラLoRAの絵", cl_tag(code, ch), "確かめた", "%d 枚" % n)
        return "確かめた にしました（%d 枚）" % n
    if os.path.isfile(f):
        os.remove(f)
    return "確かめた を外しました"


# ---- 雰囲気の語（しっとり）を試す（2026-10-05 ユーザー要望。画像生成\雰囲気設定.json・gen.py --mood／--no-mood）
MOOD_TRY = "雰囲気確認"
MOOD_DEF = {"on": False, "scope": "scene", "pos": "", "neg": "", "memo": ""}


def P_MOOD():
    return os.path.join(IMG(), "雰囲気設定.json")


def mood_get(q):
    try:
        m = json.load(open(rpath(P_MOOD()), encoding="utf-8"))
    except Exception:
        m = dict(MOOD_DEF)
    try:
        ready = "MOOD_FILE" in open(os.path.join(IMG(), "gen.py"), encoding="utf-8").read()
    except OSError:
        ready = False
    base = os.path.join(A.P_out(), MOOD_TRY)
    try:
        tags = sorted((d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))), reverse=True)
    except OSError:
        tags = []
    return dict(mood=m, ready=ready, tags=tags, busy=busy(), test=TEST)


def mood_save(b):
    m = {k: b.get(k, MOOD_DEF[k]) for k in MOOD_DEF}
    m["on"] = bool(m["on"])
    if m["scope"] not in ("scene", "lose", "atk"):
        raise RuntimeError("使う場面が違います")
    for k in ("pos", "neg"):
        m[k] = re.sub(r"\s+", " ", str(m[k] or "")).strip().strip(",").strip()
    with LOCK:
        backup_data(P_MOOD(), "雰囲気設定")
        w = wpath(P_MOOD())
        with open(w + ".tmp", "w", encoding="utf-8") as f:
            json.dump(m, f, ensure_ascii=False, indent=2)
        os.replace(w + ".tmp", w)
    add_memo("雰囲気の語", "雰囲気設定.json", "使う" if m["on"] else "使わない", "%s／%s" % (m["scope"], m["pos"][:60]))
    return "保存しました（本番の撮影で%s）" % ("使います" if m["on"] else "使いません")


def mood_try(b):
    """選んだ場面を、雰囲気の語あり／なし（同じシード）で撮る → output\\雰囲気確認\\<日時>\\あり|なし"""
    need_idle("雰囲気の試し撮り")
    code = A.codes_arg([b.get("code", "")])[0]
    pr = prompts_of(code)
    names = [n for n in (b.get("names") or []) if n in pr and is_scene(n)]
    if not names:
        sc = [n for n in pr if is_scene(n) and "onani" not in n.lower()]
        names = [n for n in sc if "_lose_btl_" in n][:1] + [n for n in sc if "_atk_" in n][:1]
    if not names:
        raise RuntimeError("このMODに場面がありません")
    if not mood_get({})["ready"]:
        raise RuntimeError("gen.py にまだ雰囲気の語が組み込まれていません")
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    tag = "%s_%s" % (time.strftime("%m%d_%H%M%S"), code)
    out = "%s/%s" % (MOOD_TRY, tag)
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    add_job("雰囲気の試し撮り %s（あり）" % code, [A.PY, "gen.py", code, ",".join(names), "--model", "wai", "--redo", "--mood", "--out", out + "/あり"])
    add_job("雰囲気の試し撮り %s（なし）" % code, [A.PY, "gen.py", code, ",".join(names), "--model", "wai", "--redo", "--no-mood", "--out", out + "/なし"])
    add_memo("雰囲気の語", tag, "試し撮り", "、".join(names))
    return "並べました：雰囲気の試し撮り（%s）。撮り終わったら「試し撮りを見る」で見比べてください。" % "、".join(names)


def mood_imgs(q):
    tag = q.get("tag", "")
    if not _SAFE.match(tag or "") or ".." in tag:
        raise RuntimeError("名前が違います")
    base = os.path.join(A.P_out(), MOOD_TRY, tag)
    pairs = {}
    for sub in ("あり", "なし"):
        for f in cl_pngs(os.path.join(base, sub)):
            m = SHOT_N.match(f)
            pairs.setdefault(m.group(1) if m else f, {})[sub] = f
    return dict(tag=tag, pairs=[dict(key=k, yes=v.get("あり", ""), no=v.get("なし", "")) for k, v in sorted(pairs.items())])


def mood_img(q, w):
    tag, sub, f = q.get("tag", ""), q.get("sub", ""), q.get("n", "")
    if sub not in ("あり", "なし") or not all(_SAFE.match(x or "") and ".." not in x for x in (tag, f)):
        raise RuntimeError("名前が違います")
    p = os.path.join(A.P_out(), MOOD_TRY, tag, sub, f)
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません")
    return (open(p, "rb").read(), "image/png") if not w else (_thumb_from(p, "mood|" + p, w), "image/jpeg")


def chara_prep(b):
    code = A.codes_arg([b.get("code", "")])[0]
    if TEST:
        raise RuntimeError("試しの起動（--test）では作業を動かしません")
    A.JOBS.add("キャラLoRAの学習データを作る %s" % code, [A.PY, "prep_chara.py", code], CL_DIR())
    return "並べました：学習データを作る（%d 枚以上残っているキャラだけ）" % CL_MIN


def chara_train(b):
    need_idle("学習")
    code = A.codes_arg([b.get("code", "")])[0]
    if A.comfy_state()["up"]:
        raise RuntimeError("ComfyUI が起動しています。学習はグラフィックボードを取り合うので、ComfyUI の黒い画面を閉じてから押してください。")
    if not os.path.exists(CL_VENV()):
        raise RuntimeError("学習の道具（Lora用\\sd-scripts）がありません。先に Lora用\\1_セットアップ.bat を実行してください。")
    if TEST:
        raise RuntimeError("試しの起動（--test）では作業を動かしません")
    argv = [CL_VENV(), "train_chara.py", code] + (["--redo"] if b.get("redo") else [])
    A.JOBS.add("キャラLoRAを学習する %s（1キャラ 8〜17分）" % code, argv, CL_DIR())
    return "並べました：学習（学習済みのキャラは飛ばします）。終わるまで ComfyUI は起動しないでください。"


def cl_scenes(code, ch):
    P = prompts_of(code)
    keys = ("m1", "m2", "m3") if ch == "master" else (ch,)
    return [n for n in P if is_scene(n) and n.split("_")[-1] in keys and "onani" not in n.lower()]


def chara_try(b):
    """試し撮り：そのキャラの場面を2つ、キャラLoRAあり／なし（同じシード）で → output\\キャラLoRA確認\\<タグ>\\あり|なし"""
    need_idle("試し撮り")
    code = A.codes_arg([b.get("code", "")])[0]
    ch = b.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    sc = cl_scenes(code, ch)
    pick = [n for n in sc if "_lose_btl_" in n][:1] + [n for n in sc if "_atk_" in n][:1]
    pick = pick or sc[:2]
    # 2026-10-05 ふたなりの場面があれば1つ足す（学習用の絵は全年齢で特徴が入らないので、場面で出るかを確かめる・ユーザー決定 案A）
    P = prompts_of(code)
    fu = [n for n in sc if n not in pick and "futanari" in (P.get(n) or {}).get("positive", "").lower()][:1]
    if fu and not any("futanari" in (P.get(n) or {}).get("positive", "").lower() for n in pick):
        pick += fu
    if not pick:
        raise RuntimeError("このキャラの場面がありません")
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    out = "%s/%s" % (CL_TRY, cl_tag(code, ch))
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    add_job("キャラLoRAの試し撮り %s（あり）" % cl_tag(code, ch), [A.PY, "gen.py", code, ",".join(pick), "--model", "wai", "--redo", "--out", out + "/あり"])
    add_job("キャラLoRAの試し撮り %s（なし）" % cl_tag(code, ch), [A.PY, "gen.py", code, ",".join(pick), "--model", "wai", "--redo", "--no-chara", "--out", out + "/なし"])
    return "並べました：試し撮り（%s）。撮り終わったら、このキャラの「試し撮りを見る」で見比べてください。" % "、".join(pick)


def chara_try_imgs(q):
    tag = q.get("tag", "")
    if not _SAFE.match(tag or "") or ".." in tag:
        raise RuntimeError("名前が違います")
    base = os.path.join(A.P_out(), CL_TRY, tag)
    pairs = {}
    for sub in ("あり", "なし"):
        for f in cl_pngs(os.path.join(base, sub)):
            m = SHOT_N.match(f)
            pairs.setdefault(m.group(1) if m else f, {})[sub] = f
    return dict(tag=tag, pairs=[dict(key=k, yes=v.get("あり", ""), no=v.get("なし", "")) for k, v in sorted(pairs.items())])


def cl_try_img(q, w):
    tag, sub, f = q.get("tag", ""), q.get("sub", ""), q.get("n", "")
    if sub not in ("あり", "なし") or not all(_SAFE.match(x or "") and ".." not in x for x in (tag, f)):
        raise RuntimeError("名前が違います")
    p = os.path.join(A.P_out(), CL_TRY, tag, sub, f)
    if not os.path.isfile(p):
        raise RuntimeError("絵がありません")
    return (open(p, "rb").read(), "image/png") if not w else (_thumb_from(p, "cltry|" + p, w), "image/jpeg")


def chara_reshoot(b):
    """そのキャラの場面を、今の割り当てと同じシードで撮り直す（できた LoRA を使った絵になる・前の絵は消えない）"""
    need_idle("撮り直し")
    code = A.codes_arg([b.get("code", "")])[0]
    ch = b.get("char", "")
    if ch not in CL_CHARS:
        raise RuntimeError("キャラが違います")
    sc = cl_scenes(code, ch)
    if not sc:
        raise RuntimeError("このキャラの場面がありません")
    if TEST:
        raise RuntimeError("試しの起動（--test）では撮影を並べません")
    A.JOBS.add("ComfyUI の起動を確かめる", func=A.comfy_start_and_wait)
    add_job("キャラLoRAで撮り直し %s（%d 場面）" % (cl_tag(code, ch), len(sc)), [A.PY, "gen.py", code, ",".join(sc), "--model", "wai", "--redo"], rec="撮影記録.txt")
    return "並べました：%s の %d 場面を撮り直す" % (CL_JA[ch], len(sc))


# ---------------------------------------------------------------- 入口
def state():
    return dict(busy=busy(), test=TEST, age=preview_age())


def get(path, q):
    if path == "ping":
        return dict(ok=True, test=TEST)
    if path == "state":
        return state()
    if path == "words":
        return dict(words=words(), head=WORD_HEAD)
    if path == "items":
        wm = word_map()
        return dict(rows=[dict(r, 読み=reading(r["構図名"], wm)) for r in items_table()], head=ITEM_HEAD, registered=sorted(registered()))
    if path == "comps":
        return dict(comps=comp_list())
    if path == "cands":
        return dict(cands=candidates(), age=None)
    if path == "chara_mods":
        return chara_mods(q)
    if path == "chara_imgs":
        return chara_imgs(q)
    if path == "chara_try_imgs":
        return chara_try_imgs(q)
    if path == "mood":
        return mood_get(q)
    if path == "mood_imgs":
        return mood_imgs(q)
    if path == "chara_refs":
        return chara_refs(q)
    if path == "chara_batch_plan":
        return chara_batch_plan(q)
    if path == "similar":
        return similar(q)
    if path == "split":
        return split_get(q)
    if path == "traits":
        return traits_get(q)
    if path == "depth_check":
        return depth_check(q)
    if path == "check_plan":
        return check_plan(q)
    if path == "check_list":
        return check_list(q)
    if path == "check_imgs":
        return check_imgs(q)
    if path == "reg_info":
        return reg_info(q)
    if path == "manual":
        return manual_get(q)
    if path == "regions":
        return dict(rows=region_rows())
    if path == "usage":
        return usage()
    if path == "pose_report":
        return pose_report()
    if path == "assign_sum":
        return dict(mods=assign_summary(), age=preview_age())
    if path == "assign":
        code = A.codes_arg([q.get("code", "")])[0]
        rows = assign_rows(code)
        for r in rows:
            r["game"] = game_info(code, r["name"])
        return dict(code=code, rows=rows, age=preview_age(), readable=mod_texts(code) is not None)
    if path == "assign_by":   # 構図（または下書き1枚）から見る：MOD をまたいで当たっている場面
        comp, draft = q.get("comp", ""), q.get("draft", "")
        pv = preview()[0]

        def hit(d):
            d = (d or "").strip()
            return bool(d) and ((draft and d.lower() == draft.lower()) or (comp and d.startswith("depthref_") and comp_of(d) == comp))
        mods = sorted({m for (m, n), r in pv.items() if hit(r.get("下書き"))})
        P, regs, wm = pc(), {r["name"]: r for r in region_rows()}, word_map()
        rows = [r for m in mods for r in assign_rows(m, P, pv, regs, wm) if hit(r["draft"])]
        for r in rows:
            r["game"] = game_info(r["code"], r["name"])
        return dict(rows=rows, age=preview_age())
    if path == "scene":
        return scene_detail(q.get("code", ""), q.get("name", ""))
    if path == "memos":
        return dict(memo=read_dicts(P_MEMO())[1], reshoot=read_dicts(P_RESHOOT())[1], textfix=read_dicts(P_TEXTFIX())[1])
    if path == "backups":
        return model_backups()
    if path == "unreadable":
        return dict(codes=[c for c in mod_codes() if mod_texts(c) is None])
    raise RuntimeError("ありません: " + path)


def post(path, b):
    fn = {
        "pick": set_pick, "new": set_new, "crop": crop_copy, "items": lambda b: save_items_row(b["comp"], b.get("items") or {}, b.get("how") or "手"),
        "fix": set_fix, "manual_save": manual_save, "reg_plan": reg_plan, "reg_do": reg_do, "check_run": check_run, "depth_decide": depth_decide, "depth_run": depth_run, "trait_save": trait_save, "trait_switch_plan": trait_switch_plan, "trait_switch": trait_switch, "split_save": split_save, "split_try": split_try, "similar_run": similar_run, "chara_move": chara_move, "chara_shoot": chara_shoot, "chara_first": chara_first, "mood_save": mood_save, "mood_try": mood_try, "chara_batch": chara_batch, "chara_check": chara_check, "chara_pick_ref": chara_pick_ref, "chara_prep": chara_prep, "chara_train": chara_train, "chara_try": chara_try, "chara_reshoot": chara_reshoot, "wd_apply": wd_apply, "wd_apply_all": wd_apply_all, "wd_run": wd_run, "remake_regions": remake_regions, "preview": run_preview, "pose_report": run_pose_report,
        "exclude_plan": exclude_plan, "exclude": exclude, "restore_plan": restore_plan, "restore": restore,
        "reshoot_add": add_reshoot, "reshoot_del": del_reshoot, "reshoot_run": run_reshoot,
        "textfix_add": add_textfix, "textfix_del": del_textfix, "textfix_text": lambda b: textfix_text(),
        "memo": lambda b: (add_memo(b.get("kind") or "そのほか", b.get("target", ""), b.get("verdict", ""), b.get("why", "")), "メモしました")[1],
        "word_add": word_add, "word_save": word_save, "prewarm": prewarm,
    }.get(path)
    if not fn:
        raise RuntimeError("ありません: " + path)
    r = fn(b)
    return r if isinstance(r, dict) else {"ok": True, "msg": r}


def word_add(b):
    cat, en, ja = (b.get("cat") or "").strip(), (b.get("en") or "").strip().lower(), (b.get("ja") or "").strip()
    if cat not in ("人数", "技", "姿勢", "視点", "位置", "そのほか"):
        raise RuntimeError("項目が違います")
    if not re.match(r"^[a-z0-9]+$", en):
        raise RuntimeError("英字は 英小文字と数字だけ（_ は使えません）")
    if not ja:
        raise RuntimeError("日本語訳を入れてください")
    with LOCK:
        ws = words()
        if any(w["英字"] == en and w["項目"] == cat for w in ws):
            raise RuntimeError("もうあります：%s（%s）" % (en, cat))
        ws.append(dict(項目=cat, 英字=en, 日本語=ja, 選択肢に出す="○" if b.get("show", True) else "", まとめる先=(b.get("canon") or "").strip(), メモ=(b.get("memo") or "").strip()))
        write_dicts(P_WORDS(), WORD_HEAD, ws)
    return "語を足しました：%s（%s）" % (ja, en)


def word_save(b):
    """語の一覧の1行を直す（英字は変えない）"""
    en, cat = (b.get("en") or "").strip(), (b.get("cat") or "").strip()
    with LOCK:
        ws = words()
        w = next((x for x in ws if x["英字"] == en and x["項目"] == cat), None)
        if not w:
            raise RuntimeError("その語はありません")
        for k in ("日本語", "選択肢に出す", "まとめる先", "メモ"):
            if k in b:
                w[k] = (b.get(k) or "").strip()
        write_dicts(P_WORDS(), WORD_HEAD, ws)
    return "直しました：%s" % en
