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
    return "外しました：%s（控え %s）。下見をやり直すと割り当てに反映されます。" % (plan["draft"], bname)


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
    return "戻しました（戻す前の控え %s）。下見をやり直すと割り当てに反映されます。" % bname


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
        return dict(code=code, rows=assign_rows(code), age=preview_age(), readable=mod_texts(code) is not None)
    if path == "assign_by":   # 構図（または下書き1枚）から見る：MOD をまたいで当たっている場面
        comp, draft = q.get("comp", ""), q.get("draft", "")
        pv = preview()[0]

        def hit(d):
            d = (d or "").strip()
            return bool(d) and ((draft and d.lower() == draft.lower()) or (comp and d.startswith("depthref_") and comp_of(d) == comp))
        mods = sorted({m for (m, n), r in pv.items() if hit(r.get("下書き"))})
        P, regs, wm = pc(), {r["name"]: r for r in region_rows()}, word_map()
        rows = [r for m in mods for r in assign_rows(m, P, pv, regs, wm) if hit(r["draft"])]
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
        "fix": set_fix, "manual_save": manual_save, "remake_regions": remake_regions, "preview": run_preview, "pose_report": run_pose_report,
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
