# -*- coding: utf-8 -*-
"""サキュバスデュエルMOD まとめツール（2026-10-04）
画像生成（事前準備ふくむ）・カードとシナリオ・ゲームへ反映 を、ブラウザの1つの画面から動かす。
・起動: まとめツール.bat（ComfyUI 付属の Python で app.py を動かし、ブラウザを開く）
・画像の撮影そのものは、今までの 画像生成\\gen.py などをそのまま呼ぶ（中身は書き換えない）。
・ゲームへは「MODコードで始まる名前のファイル」だけをコピーする。本編のファイルには触れない。
・このPCの中だけで動く（127.0.0.1）。登場人物は全員20歳以上。個人利用のみ。
"""
import csv, filecmp, io, json, os, re, shutil, subprocess, sys, threading, time, urllib.parse, urllib.request, zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import newmod  # noqa: E402
import kozu  # noqa: E402  2026-10-05 構図の元絵と下書きの画面（kozu.py・構図.html）

TEST = "--test" in sys.argv   # 2026-10-05 試しの起動（別の番号で動かす。作業は動かさず、書き込みは _試し の写しへ）

CONF_PATH = os.path.join(HERE, "設定.json")
HOME = os.path.expanduser("~")
DEFAULT_CONF = {
    "mod_root": os.path.dirname(HERE),
    "comfy_dir": os.path.join(HOME, "Downloads", "ComfyUI_windows_portable"),
    "game_dir": r"D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル",
    "port": 8765,
}
NO_STYLE = ("", "本編", "標準", "none")
KEYS = ["m1", "m2", "m3", "e1", "e2", "e3", "boss"]
ROUTES = ["btl", "onani", "inochi", "onedari"]


def load_conf():
    c = dict(DEFAULT_CONF)
    try:
        c.update(json.load(open(CONF_PATH, encoding="utf-8")))
    except Exception:
        pass
    return c


CONF = load_conf()


def P_img():
    return os.path.join(CONF["mod_root"], "画像生成")


def P_out():
    return os.path.join(CONF["comfy_dir"], "ComfyUI", "output")


def P_done():
    return os.path.join(P_img(), "完成")


P_WIP = os.path.join(HERE, "制作中")
P_KIT = os.path.join(HERE, "kit")
P_COMMON = os.path.join(P_KIT, "common")
P_LOGDIR = os.path.join(HERE, "記録")
P_MANIFEST = os.path.join(HERE, "反映記録.json")

# ---------------------------------------------------------------- 記録（画面の下に出る）
LOG, LOG_LOCK = [], threading.Lock()
LOG_BASE = 0


def log(s=""):
    global LOG_BASE
    with LOG_LOCK:
        for line in str(s).splitlines() or [""]:
            LOG.append(line)
        if len(LOG) > 6000:
            cut = len(LOG) - 5000
            del LOG[:cut]
            LOG_BASE += cut


def stamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def record(name, text):
    os.makedirs(P_LOGDIR, exist_ok=True)
    with open(os.path.join(P_LOGDIR, name), "a", encoding="utf-8") as f:
        f.write("%s  %s\n" % (stamp(), text))


# ---------------------------------------------------------------- 作業（1つずつ順番に動かす）
class Jobs:
    def __init__(self):
        self.q, self.cur, self.proc, self.lock = [], None, None, threading.Lock()
        self.stop_flag = False
        threading.Thread(target=self.loop, daemon=True).start()

    def add(self, title, argv=None, cwd=None, func=None, env=None, rec=None):
        if TEST:
            raise RuntimeError("試しの起動（--test）では作業を動かしません：" + title)
        with self.lock:
            self.q.append(dict(title=title, argv=argv, cwd=cwd, func=func, env=env, rec=rec))

    def stop(self):
        with self.lock:
            n = len(self.q)
            self.q.clear()
            self.stop_flag = True
            p = self.proc
        if p and p.poll() is None:
            try:
                if os.name == "nt":
                    subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True)
                else:
                    p.terminate()
            except Exception as ex:
                log("[止められませんでした] %s" % ex)
        log("■ 止めました（待っていた作業 %d 件も取り消し）" % n)

    def state(self):
        with self.lock:
            return dict(running=bool(self.cur), title=(self.cur or {}).get("title", ""), waiting=[j["title"] for j in self.q][:30],
                        waiting_n=len(self.q))

    def loop(self):
        while True:
            with self.lock:
                job = self.q.pop(0) if self.q else None
                self.cur = job
                if job:
                    self.stop_flag = False
            if not job:
                time.sleep(0.3)
                continue
            log("")
            log("▶ %s  （%s）" % (job["title"], time.strftime("%H:%M:%S")))
            t0, code = time.time(), 0
            try:
                if job["func"]:
                    code = job["func"]() or 0
                else:
                    code = self.run(job)
            except Exception as ex:
                code = 1
                log("[失敗] %s" % ex)
            if self.stop_flag:
                code = code or -1
            log("%s %s  （%d秒）" % ("✔ 終わり" if code == 0 else "✖ 途中で終わりました（終了コード %s）" % code, job["title"], time.time() - t0))
            if job.get("rec"):
                record(job["rec"], "%s  終了コード %s" % (job["title"], code))
            if code != 0 and not self.stop_flag:
                with self.lock:
                    n = len(self.q)
                    self.q.clear()
                if n:
                    log("  うまくいかなかったので、後に続く %d 件は取り消しました。" % n)
            with self.lock:
                self.cur = None

    def run(self, job):
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"   # 出力の文字だけ UTF-8 にそろえる（スクリプトがファイルを読む時の文字コードは変えない）
        env["PYTHONUNBUFFERED"] = "1"
        env.update(job.get("env") or {})
        flags = 0x08000000 if os.name == "nt" else 0   # 黒い画面を出さない
        p = subprocess.Popen(job["argv"], cwd=job["cwd"], env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, creationflags=flags)
        self.proc = p
        for raw in p.stdout:
            try:
                s = raw.decode("utf-8")
            except UnicodeDecodeError:
                s = raw.decode("cp932", "replace")
            for part in s.rstrip("\r\n").split("\r"):
                log(part)
        p.wait()
        self.proc = None
        return p.returncode


JOBS = Jobs()
PY = sys.executable


# ---------------------------------------------------------------- ComfyUI
def comfy_get(path, timeout=2):
    with urllib.request.urlopen("http://127.0.0.1:8188" + path, timeout=timeout) as r:
        return r.read()


def comfy_state():
    try:
        q = json.loads(comfy_get("/queue"))
        return dict(up=True, running=len(q.get("queue_running", [])), pending=len(q.get("queue_pending", [])))
    except Exception:
        return dict(up=False, running=0, pending=0)


def comfy_start_and_wait():
    if comfy_state()["up"]:
        log("ComfyUI は起動しています。")
        return 0
    bat = os.path.join(CONF["comfy_dir"], "run_nvidia_gpu.bat")
    if not os.path.exists(bat):
        log("[中止] %s がありません。「設定」で ComfyUI の場所を確かめてください。" % bat)
        return 1
    log("ComfyUI を起動します（別の黒い画面が開きます。閉じないでください）...")
    subprocess.Popen('start "ComfyUI" /D "%s" cmd /k run_nvidia_gpu.bat' % CONF["comfy_dir"], shell=True)
    for i in range(120):
        time.sleep(5)
        if JOBS.stop_flag:
            return -1
        if comfy_state()["up"]:
            log("ComfyUI が起動しました。")
            return 0
        if i % 4 == 3:
            log("  起動を待っています...（%d秒）" % ((i + 1) * 5))
    log("[中止] 10分待っても ComfyUI が起動しませんでした。")
    return 1


# ---------------------------------------------------------------- MOD の一覧
_PROMPT_CACHE = {}


def prompt_names(code):
    p = os.path.join(P_img(), "prompts", code + ".json")
    try:
        mt = os.path.getmtime(p)
    except OSError:
        return []
    if _PROMPT_CACHE.get(code, (0,))[0] != mt:
        try:
            d = json.load(open(p, encoding="utf-8"))
            names = list(d.keys()) if isinstance(d, dict) else [x.get("name") for x in d if isinstance(x, dict)]
        except Exception:
            names = []
        _PROMPT_CACHE[code] = (mt, [n for n in names if n])
    return _PROMPT_CACHE[code][1]


def skip_onanie():
    try:
        return bool(json.load(open(os.path.join(P_img(), "model.json"), encoding="utf-8")).get("skip_onanie"))
    except Exception:
        return True


def styles():
    out = {}
    try:
        with open(os.path.join(P_img(), "絵柄割当.csv"), encoding="utf-8-sig", newline="") as f:
            for i, row in enumerate(csv.reader(f)):
                if i and row and row[0].strip():
                    out[row[0].strip()] = (row[1].strip() if len(row) > 1 else "")
    except Exception:
        pass
    return out


def out_dir(code, st):
    s = st.get(code, "")
    return os.path.join(P_out(), code + "_WAI" + ("" if s in NO_STYLE else "_" + s))


RX_SHOT = re.compile(r"(.+?)_(\d{5})_\.png$")


def shots(code, st):
    """撮った絵：{画像名: [ファイル名…（新しい順）]}"""
    d, out = out_dir(code, st), {}
    try:
        files = os.listdir(d)
    except OSError:
        return d, out
    for f in files:
        m = RX_SHOT.match(f)
        if m:
            out.setdefault(m.group(1), []).append(f)
    for v in out.values():
        v.sort(reverse=True)
    return d, out


RX_MODDIR = re.compile(r"^(?:N(\d+)_)?([A-Za-z0-9]+)_MOD(?:_v\d+)?$")
RX_MODZIP = re.compile(r"^N(\d+)_([A-Za-z0-9]+)_MOD\.zip$")


def mod_dirs():
    """{コード: {n, dir, zip}}"""
    out, root = {}, CONF["mod_root"]
    try:
        names = os.listdir(root)
    except OSError:
        return out
    for nm in names:
        p = os.path.join(root, nm)
        m = RX_MODDIR.match(nm)
        if m and os.path.isdir(os.path.join(p, "CSV", "Card")):
            out.setdefault(m.group(2), {}).update(n=int(m.group(1) or 0), dir=p, name=nm)
        z = RX_MODZIP.match(nm)
        if z and os.path.isfile(p):
            out.setdefault(z.group(2), {"n": int(z.group(1))}).update(zip=p)
    return out


def wip_list():
    out = []
    if not os.path.isdir(P_WIP):
        return out
    for nm in sorted(os.listdir(P_WIP), key=lambda s: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", s)]):
        d = os.path.join(P_WIP, nm)
        m = re.match(r"^N(\d+)_([A-Za-z0-9]+)$", nm)
        if not (m and os.path.isdir(d)):
            continue
        scen = [f for f in os.listdir(os.path.join(d, "scen")) if f.endswith(".txt")] if os.path.isdir(os.path.join(d, "scen")) else []
        lines = [f for f in os.listdir(os.path.join(d, "lines")) if f.endswith(".json")] if os.path.isdir(os.path.join(d, "lines")) else []
        want = ["%s_%s.txt" % (r, k) for k in KEYS for r in ROUTES]
        out.append(dict(name=nm, n=int(m.group(1)), code=m.group(2), cfg=os.path.exists(os.path.join(d, "cfg.py")),
                        brief=os.path.exists(os.path.join(d, "brief.md")), scen=len([f for f in scen if f in want]),
                        scen_missing=[f[:-4] for f in want if f not in scen], lines=len(lines),
                        built=os.path.isdir(os.path.join(CONF["mod_root"], "%s_MOD" % nm, "CSV", "Card"))))
    return out


def mods_overview():
    st, md, skip = styles(), mod_dirs(), skip_onanie()
    try:
        pcodes = sorted(f[:-5] for f in os.listdir(os.path.join(P_img(), "prompts")) if f.endswith(".json"))
    except OSError:
        pcodes = []
    rows = []
    for code in sorted(set(md) | set(pcodes), key=lambda c: (md.get(c, {}).get("n", 9999) or 9998, c)):
        info = md.get(code, {})
        names = [n for n in prompt_names(code) if not (skip and "onani" in n)]
        fix_old_names(out_dir(code, st))
        d, sh = shots(code, st)
        try:
            done = len([f for f in os.listdir(os.path.join(P_done(), code)) if f.lower().endswith(".png")])
        except OSError:
            done = 0
        cards = 0
        if info.get("dir"):
            try:
                cards = len([f for f in os.listdir(os.path.join(info["dir"], "CSV", "Card")) if f.endswith(".txt")])
            except OSError:
                pass
        rows.append(dict(code=code, n=info.get("n", 0), folder=info.get("name", ""), zip=bool(info.get("zip")) and not info.get("dir"),
                         style=st.get(code, ""), total=len(names), shot=len([n for n in names if n in sh]), done=done, cards=cards,
                         prompts=bool(names)))
    return rows


# ---------------------------------------------------------------- 画像タブの作業
def img_script(name):
    return os.path.join(P_img(), name)


def need_img(name):
    if not os.path.exists(img_script(name)):
        raise RuntimeError("画像生成フォルダに %s がありません" % name)


def codes_arg(codes):
    codes = [c for c in codes if re.match(r"^[A-Za-z0-9]+$", c)]
    if not codes:
        raise RuntimeError("MODが選ばれていません")
    return codes


def act_shoot(b):
    need_img("gen.py")
    codes = codes_arg(b.get("codes", []))
    keys = re.sub(r"[^A-Za-z0-9_,]", "", (b.get("keys") or "all").replace("、", ",")) or "all"
    opt = ["--model", "wai"]
    if b.get("redo"):
        opt += ["--random", "--redo"]
    n = max(1, min(8, int(b.get("batch") or 1)))
    if n > 1:
        opt += ["--batch", str(n)]
    JOBS.add("ComfyUI の起動を確かめる", func=comfy_start_and_wait)
    for c in codes:
        JOBS.add("撮影 %s（%s）" % (c, "全部" if keys == "all" else keys), [PY, "gen.py", c, keys] + opt, P_img(), rec="撮影記録.txt")
    return "撮影を %d 件 並べました" % len(codes)


def act_collect(b):
    need_img("collect.py")
    codes = b.get("codes") or []
    arg = ",".join(codes_arg(codes)) if codes else "all"
    JOBS.add("完成フォルダへ集める（%s）" % ("全部" if arg == "all" else "%d個" % len(codes)), [PY, "collect.py", arg], P_img())
    return "並べました"


SIMPLE = {
    # id: (題, スクリプト, 引数, ComfyUI が要るか)
    "sort": ("元絵の候補を整理する", "候補を整理する.py", [], False),
    "adopt_dry": ("元絵を採用する（することだけ見る）", "adopt_ref.py", ["--dry-run"], False),
    "adopt": ("元絵を採用する", "adopt_ref.py", [], False),
    "depth": ("奥行き下書きを作る", "depth_from_ref.py", [], False),
    "region": ("人物の範囲を作る", "make_region_masks.py", [], False),
    "pose_list": ("構図の一覧を見る", "make_pose_ref.py", ["--list"], False),
    "style_list": ("絵柄の一覧と割当を見る", "gen.py", ["all", "--style-list"], False),
    "style_blank": ("絵柄が空欄のMODにランダムで割り当てる", "gen.py", ["all", "--random-style", "--assign-only"], False),
    "preview": ("下見（全MODの全場面を撮らずに点検）", "gen.py", ["all", "all", "--model", "wai", "--preview"], False),
    "thumbs": ("確認撮影の一覧画像を作る", "一覧画像を作る.py", [], False),
}


def act_simple(b):
    title, script, args, comfy = SIMPLE[b["id"]]
    need_img(script)
    if comfy:
        JOBS.add("ComfyUI の起動を確かめる", func=comfy_start_and_wait)
    JOBS.add(title, [PY, script] + args, P_img())
    return "並べました：" + title


def act_pose(b):
    need_img("make_pose_ref.py")
    ids = re.sub(r"[^A-Za-z0-9_,]", "", (b.get("ids") or "").replace("、", ","))
    n = max(1, min(16, int(b.get("n") or 4)))
    args = (["--only", ids] if ids else []) + ["--batch", str(n)]
    if b.get("dry"):
        JOBS.add("構図の元絵候補（件数だけ見る）", [PY, "make_pose_ref.py"] + args + ["--dry-run"], P_img())
    else:
        JOBS.add("ComfyUI の起動を確かめる", func=comfy_start_and_wait)
        JOBS.add("構図の元絵候補を撮る（%s・%d枚ずつ）" % (ids or "全部", n), [PY, "make_pose_ref.py"] + args, P_img())
    return "並べました"


def build_scripts():
    out = []
    try:
        for nm in sorted(os.listdir(P_img())):
            if nm.endswith("_場面") and os.path.exists(os.path.join(P_img(), nm, "build_new.py")):
                out.append(nm)
    except OSError:
        pass
    return out


def act_prompts(b):
    d = b.get("dir", "")
    if d not in build_scripts():
        raise RuntimeError("そのフォルダはありません")
    codes = b.get("codes") or []
    arg = [",".join(codes_arg(codes))] if codes else []
    sc = os.path.join(d, "build_new.py")
    if b.get("write"):
        JOBS.add("画像プロンプトを作り直す（%s）" % d, [PY, sc] + arg, P_img())
    else:
        JOBS.add("画像プロンプトの点検（%s・書き込まない）" % d, [PY, sc] + arg + ["--check"], P_img())
    return "並べました"


def act_comfy(b):
    JOBS.add("ComfyUI を起動する", func=comfy_start_and_wait)
    return "並べました"


def bats():
    try:
        return sorted(f for f in os.listdir(P_img()) if f.lower().endswith(".bat"))
    except OSError:
        return []


def act_bat(b):
    nm = b.get("name", "")
    if nm not in bats():
        raise RuntimeError("その bat はありません")
    subprocess.Popen('start "%s" /D "%s" cmd /c "%s"' % (nm, P_img(), nm), shell=True)
    return "別の画面で開きました：" + nm


def act_reject(b):
    code = codes_arg([b.get("code", "")])[0]
    d, _ = shots(code, styles())
    dst = os.path.join(d, "_外した")
    n = 0
    for f in b.get("files", []):
        if RX_SHOT.match(f) and os.path.dirname(f) == "" and os.path.exists(os.path.join(d, f)):
            os.makedirs(dst, exist_ok=True)
            t = os.path.join(dst, f)
            if os.path.exists(t):   # 同じ名前がもう外してある時は、名前を変えずに日時のフォルダへ（戻した時にそのまま使えるように）
                sub = os.path.join(dst, time.strftime("%Y%m%d_%H%M%S"))
                os.makedirs(sub, exist_ok=True)
                t = os.path.join(sub, f)
            shutil.move(os.path.join(d, f), t)
            n += 1
    log("%s: %d 枚を _外した フォルダへ移しました（消していません）" % (code, n))
    return "%d 枚を外しました" % n


RX_OLD = re.compile(r"^\d{9,11}_(.+?_\d{5}_\.png)$")   # 前の版が付けた「数字_」つきの名前


def free_name(d, f):
    """d に同じ名前があれば、空いている番号の名前を返す（Host_atk_m1_00001_.png → …_00006_.png）"""
    if not os.path.exists(os.path.join(d, f)):
        return f
    m = RX_SHOT.match(f)
    n = int(m.group(2))
    while True:
        n += 1
        c = "%s_%05d_.png" % (m.group(1), n)
        if not os.path.exists(os.path.join(d, c)):
            return c


def fix_old_names(d):
    """撮った絵のフォルダに「数字_」つきの名前（前の版で外した絵を手で戻したもの）があれば、元の名前に直す"""
    try:
        files = os.listdir(d)
    except OSError:
        return
    for f in files:
        m = RX_OLD.match(f)
        if m and os.path.isfile(os.path.join(d, f)):
            t = free_name(d, m.group(1))
            os.rename(os.path.join(d, f), os.path.join(d, t))
            log("名前を直しました: %s → %s" % (f, t))


def rejected(d):
    """_外した の中の絵：[{path（_外した からの場所）, file（元の名前）, name（画像名）}]"""
    out, base = [], os.path.join(d, "_外した")
    for root, _, files in os.walk(base):
        for f in sorted(files):
            m = RX_OLD.match(f)
            orig = m.group(1) if m else f
            sm = RX_SHOT.match(orig)
            if sm:
                rel = os.path.relpath(os.path.join(root, f), base).replace(os.sep, "/")
                out.append(dict(path=rel, file=orig, name=sm.group(1), mtime=os.path.getmtime(os.path.join(root, f))))
    out.sort(key=lambda x: (x["name"], -x["mtime"]))
    return out


def rej_path(d, rel):
    base = os.path.join(d, "_外した")
    p = os.path.normpath(os.path.join(base, *rel.split("/")))
    if not p.startswith(os.path.normpath(base) + os.sep) or not os.path.isfile(p):
        raise RuntimeError("その絵はありません: " + rel)
    return p


def act_restore(b):
    code = codes_arg([b.get("code", "")])[0]
    d, _ = shots(code, styles())
    known = {r["path"]: r for r in rejected(d)}
    n = 0
    for rel in b.get("files", []):
        if rel not in known:
            continue
        t = free_name(d, known[rel]["file"])
        shutil.move(rej_path(d, rel), os.path.join(d, t))
        log("%s: 戻しました %s" % (code, t))
        n += 1
    return "%d 枚を戻しました" % n


def act_reshoot(b):
    need_img("gen.py")
    code = codes_arg([b.get("code", "")])[0]
    names = [n for n in b.get("names", []) if re.match(r"^[A-Za-z0-9_]+$", n)]
    if not names:
        raise RuntimeError("撮り直す絵が選ばれていません")
    n = max(1, min(8, int(b.get("batch") or 4)))
    JOBS.add("ComfyUI の起動を確かめる", func=comfy_start_and_wait)
    JOBS.add("撮り直し %s（%d種類・%d枚ずつ）" % (code, len(names), n),
             [PY, "gen.py", code, ",".join(names), "--model", "wai", "--random", "--redo", "--batch", str(n)], P_img(), rec="撮影記録.txt")
    return "並べました"


def images(code):
    code = codes_arg([code])[0]
    st, skip = styles(), skip_onanie()
    fix_old_names(out_dir(code, st))
    d, sh = shots(code, st)
    names = [n for n in prompt_names(code) if not (skip and "onani" in n)]
    rows = [dict(name=n, files=sh.get(n, [])) for n in names]
    extra = [dict(name=n, files=v, extra=True) for n, v in sorted(sh.items()) if n not in names]
    return dict(code=code, dir=d, rows=rows + extra, rejected=rejected(d))


def thumb(code, f, w, rej=False):
    code = codes_arg([code])[0]
    d, _ = shots(code, styles())
    if rej:
        src = rej_path(d, f)
        key = "_外した_" + f.replace("/", "_")
    else:
        if not RX_SHOT.match(f) or os.path.dirname(f):
            raise RuntimeError("名前が違います")
        src, key = os.path.join(d, f), f
    if not w:
        return open(src, "rb").read(), "image/png"
    cdir = os.path.join(HERE, "_cache", os.path.basename(d))
    cp = os.path.join(cdir, "%s.%d.jpg" % (key, w))
    if not (os.path.exists(cp) and int(os.path.getmtime(cp)) == int(os.path.getmtime(src))):   # 元の絵が入れ替わったら作り直す
        try:
            from PIL import Image
        except Exception:
            return open(src, "rb").read(), "image/png"
        os.makedirs(cdir, exist_ok=True)
        im = Image.open(src).convert("RGB")
        im.thumbnail((w, w * 2))
        im.save(cp, "JPEG", quality=82)
        mt = os.path.getmtime(src)
        os.utime(cp, (mt, mt))
    return open(cp, "rb").read(), "image/jpeg"


# ---------------------------------------------------------------- カード・シナリオ
def kit_ready():
    return os.path.exists(os.path.join(P_COMMON, "gen_v4.py"))


def ensure_kit():
    if kit_ready():
        return
    z = os.path.join(HERE, "kit_base.zip")
    if not os.path.exists(z):
        raise RuntimeError("kit_base.zip がありません（まとめツールのフォルダに置いてください）")
    with zipfile.ZipFile(z) as zf:
        zf.extractall(P_KIT)
    log("制作キット（共通スクリプト）を kit フォルダに展開しました。")


def wip_dir(name):
    if not re.match(r"^N\d+_[A-Za-z0-9]+$", name or ""):
        raise RuntimeError("名前が違います")
    d = os.path.join(P_WIP, name)
    if not os.path.isdir(d):
        raise RuntimeError("制作中フォルダに %s がありません" % name)
    return d


def kit_env():
    return {"PYTHONPATH": P_COMMON}


def fwd(p):
    return p.replace("\\", "/")


def act_check(b):
    ensure_kit()
    d = wip_dir(b.get("name"))
    scen = sorted(fwd(os.path.join(d, "scen", f)) for f in os.listdir(os.path.join(d, "scen")) if f.endswith(".txt")) if os.path.isdir(os.path.join(d, "scen")) else []
    lines = sorted(fwd(os.path.join(d, "lines", f)) for f in os.listdir(os.path.join(d, "lines")) if f.endswith(".json")) if os.path.isdir(os.path.join(d, "lines")) else []
    nm = b["name"]

    def run():
        code = 0
        log("―― 敗北シナリオ %d/28 本 ――" % len(scen))
        if scen:
            code |= JOBS.run(dict(argv=[PY, os.path.join(P_COMMON, "check4000.py")] + scen, cwd=d, env=kit_env()))
        log("―― カードのセリフ %d/5 本 ――" % len(lines))
        if lines:
            code |= JOBS.run(dict(argv=[PY, os.path.join(P_COMMON, "check_lines.py")] + lines, cwd=d, env=kit_env()))
        miss = [w["scen_missing"] for w in wip_list() if w["name"] == nm]
        if miss and miss[0]:
            log("まだ無いシナリオ: " + " ".join(miss[0]))
        log("（NG は直す所の目安です。点検はファイルを書き換えません）")
        return 0
    JOBS.add("点検 %s" % nm, func=run)
    return "並べました"


def act_build(b):
    ensure_kit()
    d = wip_dir(b.get("name"))
    trial = bool(b.get("trial"))
    argv = [PY, os.path.join(HERE, "build_mod.py"), d, P_COMMON, CONF["mod_root"], os.path.join(HERE, "控え")]
    if trial:
        argv.append("--trial")
    JOBS.add(("通し確認 %s（設定だけ確かめる）" if trial else "組み立て %s") % b["name"], argv, d, env=kit_env())
    return "並べました"


def act_newmod(b):
    ensure_kit()
    used = set(mod_dirs()) | {w["code"] for w in wip_list()}
    try:
        used |= {f[:-5] for f in os.listdir(os.path.join(P_img(), "prompts")) if f.endswith(".json")}
    except OSError:
        pass
    errs = newmod.validate(b, used)
    if errs:
        return {"ok": False, "errors": errs}
    name = "N%d_%s" % (int(b["n"]), b["code"])
    d = os.path.join(P_WIP, name)
    os.makedirs(os.path.join(d, "scen"))
    os.makedirs(os.path.join(d, "lines"))
    with open(os.path.join(d, "cfg.py"), "w", encoding="utf-8", newline="\n") as f:
        f.write(newmod.make_cfg(b))
    with open(os.path.join(d, "brief.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(newmod.make_brief(b))
    with open(os.path.join(d, "入力内容.json"), "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=1)
    log("制作中\\%s を作りました（cfg.py・brief.md・入力内容.json）。続けて通し確認をします。" % name)
    act_build({"name": name, "trial": True})
    return {"ok": True, "name": name}


def act_import_kit(b):
    """_共通ツール の kit106 zip から、作りかけのMOD（cfg・brief・scen・lines）を 制作中 に取り込む"""
    ensure_kit()
    z = os.path.join(CONF["mod_root"], "_共通ツール", "kit106_N106-N157_途中.zip")
    if not os.path.exists(z):
        raise RuntimeError("_共通ツール\\kit106_N106-N157_途中.zip がありません")

    def run():
        n = 0
        with zipfile.ZipFile(z) as zf:
            names = zf.namelist()
            codes = sorted({x.split("/")[1] for x in names if x.startswith("mods/") and x.count("/") >= 2})
            for c in codes:
                try:
                    src = zf.read("mods/%s/cfg.py" % c).decode("utf-8")
                except KeyError:
                    continue
                m = re.search(r'outdir\s*=\s*"N(\d+)_', src)
                if not m:
                    continue
                name = "N%s_%s" % (m.group(1), c)
                d = os.path.join(P_WIP, name)
                if os.path.exists(d):
                    continue
                for x in names:
                    if x.startswith("mods/%s/" % c) and not x.endswith("/"):
                        rel = x.split("/", 2)[2]
                        if rel.split("/")[0] in ("out", "__pycache__"):
                            continue
                        t = os.path.join(d, *rel.split("/"))
                        os.makedirs(os.path.dirname(t), exist_ok=True)
                        with open(t, "wb") as f:
                            f.write(zf.read(x))
                n += 1
                log("  取り込み: " + name)
        log("%d 個を 制作中 に取り込みました（すでにあるものは飛ばしました）" % n)
        return 0
    JOBS.add("作りかけのMODを取り込む（kit106）", func=run)
    return "並べました"


def act_unzip(b):
    code = codes_arg([b.get("code", "")])[0]
    info = mod_dirs().get(code, {})
    if not info.get("zip") or info.get("dir"):
        raise RuntimeError("展開する zip がありません")

    def run():
        with zipfile.ZipFile(info["zip"]) as zf:
            tops = {x.split("/")[0] for x in zf.namelist()}
            want = os.path.basename(info["zip"])[:-4]
            dst = CONF["mod_root"] if tops == {want} else os.path.join(CONF["mod_root"], want)
            for x in zf.namelist():
                t = os.path.normpath(os.path.join(dst, x))
                if not t.startswith(os.path.normpath(CONF["mod_root"]) + os.sep):
                    raise RuntimeError("zip の中の場所がおかしい: " + x)
            zf.extractall(dst)
        log("%s を展開しました → %s" % (os.path.basename(info["zip"]), os.path.join(CONF["mod_root"], want)))
        return 0
    JOBS.add("zip を展開 %s" % code, func=run)
    return "並べました"


# ---------------------------------------------------------------- ゲームへ反映
def load_manifest():
    try:
        return json.load(open(P_MANIFEST, encoding="utf-8"))
    except Exception:
        return {}


def game_ok():
    g = CONF["game_dir"]
    if not os.path.isdir(g):
        return "ゲームのフォルダが見つかりません: %s" % g
    if not (os.path.isdir(os.path.join(g, "CSV", "Card")) and os.path.isdir(os.path.join(g, "Picture"))):
        return "ゲームのフォルダに CSV\\Card か Picture がありません（場所が違うかもしれません）: %s" % g
    gr, mr = os.path.normcase(os.path.abspath(g)), os.path.normcase(os.path.abspath(CONF["mod_root"]))
    if gr.startswith(mr) or mr.startswith(gr):
        return "ゲームのフォルダとMODのフォルダが重なっています"
    return ""


def own_name(code, f):
    return f == code + ".txt" or f.startswith(code + "_")


def deploy_items(code, info):
    """[(元, ゲームの中の場所, 種類)], 対象外の名前"""
    items, skipped = [], []
    cdir = os.path.join(info["dir"], "CSV")
    for root, _, files in os.walk(cdir):
        for f in sorted(files):
            if not f.lower().endswith(".txt"):
                continue
            if not own_name(code, f):
                skipped.append(f)
                continue
            parts = os.path.relpath(os.path.join(root, f), cdir).split(os.sep)
            parts = ["EventList" if x.lower() == "eventlist" else x for x in parts]
            items.append((os.path.join(root, f), os.path.join("CSV", *parts), "csv"))
    pics = {}
    for d in (os.path.join(info["dir"], "Picture", code), os.path.join(P_done(), code)):   # 完成フォルダの絵を優先
        try:
            for f in sorted(os.listdir(d)):
                if f.lower().endswith(".png") and f.startswith(code + "_") and not RX_SHOT.match(f):
                    pics[f] = os.path.join(d, f)
        except OSError:
            pass
    for f, src in sorted(pics.items()):
        items.append((src, os.path.join("Picture", code, f), "img"))
    return items, skipped


def same_file(a, b):
    try:
        sa, sb = os.stat(a), os.stat(b)
    except OSError:
        return False
    if sa.st_size != sb.st_size:
        return False
    if int(sa.st_mtime) == int(sb.st_mtime):
        return True
    return filecmp.cmp(a, b, shallow=False)


def deploy_plan(codes):
    err = game_ok()
    if err:
        return dict(ok=False, error=err)
    md, man, g = mod_dirs(), load_manifest(), CONF["game_dir"]
    rows, tot = [], dict(new=0, upd=0, same=0, held=0)
    for code in codes_arg(codes):
        info = md.get(code)
        if not info or not info.get("dir"):
            continue
        items, skipped = deploy_items(code, info)
        r = dict(code=code, n=info.get("n", 0), new=0, upd=0, same=0, held=0, held_names=[], skipped=skipped, csv=0, img=0)
        for src, rel, kind in items:
            r[kind] += 1
            dst = os.path.join(g, rel)
            if not os.path.exists(dst):
                k = "new"
            elif same_file(src, dst):
                k = "same"
            elif rel in man:
                k = "upd"
            else:
                k = "held"
                r["held_names"].append(rel)
            r[k] += 1
            tot[k] += 1
        rows.append(r)
    recall = os.path.join(CONF["mod_root"], "_共通ツール", "Picture", "RecallUI", "recall_panel.png")
    need_recall = os.path.exists(recall) and not os.path.exists(os.path.join(g, "Picture", "RecallUI", "recall_panel.png"))
    return dict(ok=True, rows=rows, total=tot, recall=need_recall, game=g)


def act_deploy(b):
    err = game_ok()
    if err:
        raise RuntimeError(err)
    codes = codes_arg(b.get("codes", []))
    over = bool(b.get("overwrite_held"))

    def run():
        md, man, g = mod_dirs(), load_manifest(), CONF["game_dir"]
        ts = time.strftime("%Y%m%d_%H%M%S")
        bak = os.path.join(HERE, "反映前の控え", ts)
        groot = os.path.normcase(os.path.abspath(g)) + os.sep
        tot = dict(new=0, upd=0, same=0, held=0)
        for code in codes:
            if JOBS.stop_flag:
                break
            info = md.get(code)
            if not info or not info.get("dir"):
                log("%s: MODフォルダが無いので飛ばします" % code)
                continue
            items, skipped = deploy_items(code, info)
            c = dict(new=0, upd=0, same=0, held=0)
            for src, rel, kind in items:
                dst = os.path.join(g, rel)
                base = os.path.basename(dst)
                named = base.startswith(code + "_") if kind == "img" else own_name(code, base)
                if not os.path.normcase(os.path.abspath(dst)).startswith(groot) or not named:
                    log("  [飛ばす] 場所か名前が決まりに合いません: " + rel)
                    continue
                if os.path.exists(dst):
                    if same_file(src, dst):
                        c["same"] += 1
                        man.setdefault(rel, dict(code=code, at=ts))
                        continue
                    ours = rel in man
                    if not ours and not over:
                        c["held"] += 1
                        continue
                    if kind == "csv" or not ours:   # 上書きする前に控えを取る（絵は、このツールで入れた覚えのないものだけ）
                        bp = os.path.join(bak, rel)
                        os.makedirs(os.path.dirname(bp), exist_ok=True)
                        shutil.copy2(dst, bp)
                    c["upd"] += 1
                else:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    c["new"] += 1
                shutil.copy2(src, dst)
                man[rel] = dict(code=code, at=ts)
            for k in tot:
                tot[k] += c[k]
            log("%-12s 新しく %3d／入れ替え %3d／同じ %3d／保留 %3d%s" % (code, c["new"], c["upd"], c["same"], c["held"],
                                                              ("／対象外 %d" % len(skipped)) if skipped else ""))
        recall = os.path.join(CONF["mod_root"], "_共通ツール", "Picture", "RecallUI", "recall_panel.png")
        rdst = os.path.join(g, "Picture", "RecallUI", "recall_panel.png")
        if os.path.exists(recall) and not os.path.exists(rdst):
            os.makedirs(os.path.dirname(rdst), exist_ok=True)
            shutil.copy2(recall, rdst)
            man[os.path.join("Picture", "RecallUI", "recall_panel.png")] = dict(code="_共通", at=ts)
            log("回想の栞の共通画像（recall_panel.png）を入れました")
        tmp = P_MANIFEST + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(man, f, ensure_ascii=False, indent=0)
        os.replace(tmp, P_MANIFEST)
        log("合計： 新しく %d／入れ替え %d／同じなので何もしない %d／保留 %d" % (tot["new"], tot["upd"], tot["same"], tot["held"]))
        if os.path.isdir(bak):
            log("入れ替える前のファイルの控え: " + bak)
        if tot["held"]:
            log("保留＝ゲームに同じ名前で中身の違うファイルがあり、このツールで入れた記録が無いもの。前に手で入れた自分のMODなら「保留も入れ替える」に印を付けてもう一度。")
        record("反映記録.txt", "%d個のMOD  新規%d 入れ替え%d 同じ%d 保留%d" % (len(codes), tot["new"], tot["upd"], tot["same"], tot["held"]))
        return 0
    JOBS.add("ゲームへ反映（%d個のMOD）" % len(codes), func=run)
    return "並べました"


# ---------------------------------------------------------------- そのほか
def act_open(b):
    what = b.get("what")
    table = {
        "img": P_img(), "out": P_out(), "done": P_done(), "wip": P_WIP, "mod": CONF["mod_root"], "game": CONF["game_dir"],
        "style_csv": os.path.join(P_img(), "絵柄割当.csv"), "tool": HERE, "log": P_LOGDIR,
        "pose_src": os.path.join(P_img(), "構図下書き元"), "pose": os.path.join(P_img(), "構図下書き"),
        "pose_cand": os.path.join(P_out(), "構図候補"), "preview_csv": os.path.join(P_img(), "下見_MOD別.csv"),
    }
    p = table.get(what)
    if what == "outdir":
        p, _ = shots(codes_arg([b.get("code", "")])[0], styles())
    if what == "wipdir":
        p = wip_dir(b.get("name"))
    if not p or not os.path.exists(p):
        raise RuntimeError("まだありません: %s" % (p or what))
    os.startfile(p)
    return "開きました"


def act_config(b):
    for k in ("mod_root", "comfy_dir", "game_dir"):
        if isinstance(b.get(k), str) and b[k].strip():
            CONF[k] = b[k].strip().strip('"')
    with open(CONF_PATH, "w", encoding="utf-8") as f:
        json.dump(CONF, f, ensure_ascii=False, indent=1)
    return "設定を保存しました"


ACTIONS = dict(shoot=act_shoot, collect=act_collect, simple=act_simple, pose=act_pose, prompts=act_prompts, comfy=act_comfy, bat=act_bat,
               reject=act_reject, restore=act_restore, reshoot=act_reshoot, check=act_check, build=act_build, newmod=act_newmod, import_kit=act_import_kit,
               unzip=act_unzip, deploy=act_deploy, open=act_open, config=act_config)


def status():
    return dict(comfy=comfy_state(), job=JOBS.state(), conf=CONF, game_error=game_ok(),
                paths=dict(img=os.path.exists(img_script("gen.py")), comfy=os.path.isdir(CONF["comfy_dir"]), kit=kit_ready() or os.path.exists(os.path.join(HERE, "kit_base.zip"))))


class H(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *a):
        pass

    def send(self, body, ctype="application/json; charset=utf-8", code=200):
        if not isinstance(body, bytes):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def local(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        org = self.headers.get("Origin")
        return host in ("127.0.0.1", "localhost") and (not org or re.match(r"^http://(127\.0\.0\.1|localhost)(:\d+)?$", org))

    def do_GET(self):
        if not self.local():
            return self.send({"error": "このPCの中からだけ使えます"}, code=403)
        u = urllib.parse.urlparse(self.path)
        q = {k: v[0] for k, v in urllib.parse.parse_qs(u.query).items()}
        try:
            if u.path == "/":
                return self.send(open(os.path.join(HERE, "ui.html"), "rb").read(), "text/html; charset=utf-8")
            if u.path == "/api/status":
                return self.send(status())
            if u.path == "/api/log":
                since = int(q.get("since", 0))
                with LOG_LOCK:
                    i = max(0, since - LOG_BASE)
                    return self.send(dict(lines=LOG[i:], next=LOG_BASE + len(LOG)))
            if u.path == "/api/mods":
                return self.send(dict(mods=mods_overview(), wip=wip_list(), bats=bats(), builds=build_scripts(), skip_onanie=skip_onanie()))
            if u.path == "/api/images":
                return self.send(images(q.get("code", "")))
            if u.path == "/img":
                body, ct = thumb(q.get("code", ""), q.get("file", ""), int(q.get("w", 0)), q.get("rej") == "1")
                return self.send(body, ct)
            if u.path == "/kozu":   # 2026-10-05 構図の元絵と下書きの画面
                return self.send(open(os.path.join(HERE, "構図.html"), "rb").read(), "text/html; charset=utf-8")
            if u.path == "/manual":
                return self.send(open(os.path.join(HERE, "説明書.html"), "rb").read(), "text/html; charset=utf-8")
            if u.path == "/manual_img":
                f = q.get("f", "")
                if not re.match(r"^[A-Za-z0-9_\-]+\.(png|jpg)$", f):
                    return self.send({"error": "名前が違います"}, code=404)
                return self.send(open(os.path.join(HERE, "説明書の絵", f), "rb").read(), "image/png" if f.endswith(".png") else "image/jpeg")
            if u.path == "/kimg":
                body, ct = kozu.kimg(q)
                return self.send(body, ct)
            if u.path.startswith("/api/kozu/"):
                return self.send(kozu.get(u.path[len("/api/kozu/"):], q))
            if u.path == "/api/newmod_defaults":
                nums = [m.get("n", 0) for m in mod_dirs().values()] + [w["n"] for w in wip_list()]
                return self.send(dict(next_n=max(nums + [157]) + 1, types=newmod.TYPES, statuses=newmod.STATUSES))
            return self.send({"error": "ありません"}, code=404)
        except Exception as ex:
            return self.send({"error": str(ex)}, code=500)

    def do_POST(self):
        if not self.local() or self.headers.get("X-Tool") != "1":
            return self.send({"error": "このPCの画面からだけ使えます"}, code=403)
        try:
            n = int(self.headers.get("Content-Length") or 0)
            b = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            u = urllib.parse.urlparse(self.path).path
            if u == "/api/stop":
                JOBS.stop()
                return self.send({"ok": True, "msg": "止めました"})
            if u == "/api/deploy_plan":
                return self.send(deploy_plan(b.get("codes", [])))
            if u.startswith("/api/kozu/"):
                return self.send(kozu.post(u[len("/api/kozu/"):], b))
            if u == "/api/do":
                if TEST and b.get("action") != "open":
                    return self.send({"ok": False, "error": "試しの起動（--test）では、この操作はしません"})
                r = ACTIONS[b.get("action")](b)
                return self.send(r if isinstance(r, dict) else {"ok": True, "msg": r})
            return self.send({"error": "ありません"}, code=404)
        except Exception as ex:
            return self.send({"ok": False, "error": str(ex)}, code=200)


def main():
    port = int(CONF.get("port", 8765))
    if "--port" in sys.argv:   # 2026-10-05 別の番号でもう1つ起動する（例 --port 8766 --test --no-browser）
        port = int(sys.argv[sys.argv.index("--port") + 1])
    url = "http://127.0.0.1:%d/" % port
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", port), H)
    except OSError:
        print("すでに起動しているようです。ブラウザで開きます: " + url)
        import webbrowser
        webbrowser.open(url)
        return
    srv.daemon_threads = True
    print("まとめツールを起動しました。ブラウザで開きます: " + url)
    print("この黒い画面を閉じるとツールが止まります（動かしている作業も止まります）。")
    log("まとめツールを起動しました（%s）%s" % (stamp(), "　※試しの起動：作業は動かさず、書き込みは _試し の写しへ" if TEST else ""))
    kozu.init(sys.modules[__name__], TEST)
    if "--no-browser" not in sys.argv:
        import webbrowser
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
