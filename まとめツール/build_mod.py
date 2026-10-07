# -*- coding: utf-8 -*-
"""制作中のMOD（cfg.py・scen 28本・lines 5本）から、MODフォルダ（CSV・README・読む用シナリオ集・画像一覧・tools.zip）を組み立てる。
kit の package.py と同じ中身を、このPCの場所で動くようにしたもの。
使い方: python build_mod.py <制作中のフォルダ> <kit\\common> <MODの置き場> <控えの置き場> [--trial]
  --trial … 設定（cfg.py）だけを確かめる通し確認。見本のシナリオとセリフを仮に入れてカードが10枚できるかを見る。何も置かない。"""
import glob, importlib.util, json, os, re, shutil, subprocess, sys, time, zipfile

MOD, COMMON, ROOT, BAK = [os.path.abspath(a) for a in sys.argv[1:5]]
TRIAL = "--trial" in sys.argv
sys.path.insert(0, COMMON)
KEYS = ["m1", "m2", "m3", "e1", "e2", "e3", "boss"]
ROUTES = {"btl": "戦闘負け", "onani": "オナニー負け", "inochi": "命乞い負け", "onedari": "おねだり負け"}


def load_cfg(d):
    spec = importlib.util.spec_from_file_location("cfg", os.path.join(d, "cfg.py"))
    cm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cm)
    return cm.CFG


def run(args, cwd=None):
    env = dict(os.environ, PYTHONPATH=COMMON, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable] + args, cwd=cwd, env=env)
    if r.returncode:
        print("[中止] %s が途中で止まりました" % os.path.basename(args[0]))
        sys.exit(r.returncode)


CFG = load_cfg(MOD)
C, OUTN, S = CFG["code"], CFG["outdir"], CFG["stack"]
print("設定を読みました: %s（%s）／主人公の累積「%s」・男モンスターの累積「%s」" % (OUTN, CFG["quest_name"], S, CFG.get("mstack", S)))

# 決まりの点検（組み立ての前に）
errs = []
chars = [("master", CFG["master"])] + [(k, CFG["mons"][k]) for k in ["e1", "e2", "e3", "boss"]]
for k, d in chars:
    types = [t["type"] for t in d["techs"]]
    if len(set(types)) < 2:
        errs.append("%s：攻撃タイプが2種ありません" % d["name"])
    if len(types) != len(set(types)):
        errs.append("%s：同じ攻撃タイプが重なっています" % d["name"])
    if len([t for t in d["techs"] if t.get("fav")]) != 1:
        errs.append("%s：得意技（★）が1つではありません" % d["name"])
if CFG.get("mstack", S) == S:
    errs.append("累積スタックが主人公用と男モンスター用で同じ名前です（N106〜は別々の名前にする決まり）")
for e in errs:
    print("  [注意] " + e)

if TRIAL:
    ref = os.path.join(os.path.dirname(COMMON), "ref", "sample_Medusa")
    tmp = os.path.join(os.path.dirname(os.path.dirname(COMMON)), "_tmp", os.path.basename(MOD))
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    shutil.copy(os.path.join(MOD, "cfg.py"), tmp)
    shutil.copytree(os.path.join(ref, "scen"), os.path.join(tmp, "scen"))
    shutil.copytree(os.path.join(ref, "lines"), os.path.join(tmp, "lines"))
    prep = json.load(open(os.path.join(ref, "lines", "boss.json"), encoding="utf-8"))["prep"]
    for k, d in chars:
        p = os.path.join(tmp, "lines", ("m" if k == "master" else k) + ".json")
        j = json.load(open(p, encoding="utf-8"))
        if any(t.get("insert") for t in d["techs"]) and not j.get("prep"):
            j["prep"] = prep
        while len(j["techs"]) < len(d["techs"]):
            j["techs"].append(j["techs"][-1])
        json.dump(j, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    run([os.path.join(COMMON, "gen_v4.py"), tmp])
    n = len(glob.glob(os.path.join(tmp, "out", OUTN, "Card", "*.txt")))
    shutil.rmtree(tmp, ignore_errors=True)
    if n < 10:
        print("[NG] カードが %d 枚しかできませんでした（10枚できるはず）。cfg.py を見直してください。" % n)
        sys.exit(1)
    print("[OK] 通し確認：カード %d 枚ができました（見本のシナリオとセリフで確かめただけ。MODフォルダには何も置いていません）" % n)
    print("次は brief.md の（未記入）を埋め、scen に敗北シナリオ28本、lines にセリフ5本を置いてから「組み立て」です。")
    sys.exit(0)

miss = [f"{r}_{k}" for k in KEYS for r in ROUTES if not os.path.exists(os.path.join(MOD, "scen", f"{r}_{k}.txt"))]
missl = [k for k in ["m", "e1", "e2", "e3", "boss"] if not os.path.exists(os.path.join(MOD, "lines", k + ".json"))]
if miss or missl:
    if miss:
        print("[中止] 敗北シナリオが足りません（%d/28）: %s" % (28 - len(miss), " ".join(miss)))
    if missl:
        print("[中止] セリフが足りません: " + " ".join(k + ".json" for k in missl))
    sys.exit(1)

run([os.path.join(COMMON, "gen_v4.py"), MOD])
card = os.path.join(MOD, "out", OUTN, "Card")
run([os.path.join(COMMON, "patch_recall_ui.py"), card, C])

DST = os.path.join(ROOT, OUTN)
ts = time.strftime("%Y%m%d_%H%M%S")
if os.path.isdir(os.path.join(DST, "CSV")):
    b = os.path.join(BAK, "%s_%s" % (OUTN, ts))
    shutil.copytree(os.path.join(DST, "CSV"), os.path.join(b, "CSV"))
    print("前の CSV の控え: " + b)
os.makedirs(os.path.join(DST, "CSV", "Card"), exist_ok=True)
os.makedirs(os.path.join(DST, "CSV", "Eventlist", "Quest"), exist_ok=True)
for f in glob.glob(os.path.join(DST, "CSV", "Card", C + "_*.txt")):
    os.remove(f)
for f in glob.glob(os.path.join(card, "*.txt")):
    shutil.copy(f, os.path.join(DST, "CSV", "Card"))
shutil.copy(os.path.join(MOD, "out", OUTN, "Eventlist", "Quest", f"{C}.txt"), os.path.join(DST, "CSV", "Eventlist", "Quest"))

imgs = set()
for f in glob.glob(os.path.join(DST, "CSV", "Card", "*.txt")):
    imgs |= set(re.findall(r"#%s/([\w\-]+\.png)" % C, open(f, encoding="utf-8").read()))
imgs = sorted(imgs)
with open(os.path.join(DST, "画像一覧.txt"), "w", encoding="utf-8", newline="\r\n") as fo:
    fo.write(f"{OUTN} で使う画像（ゲームの Picture\\{C}\\ に置く）  計{len(imgs)}枚\n\n" + "\n".join(imgs) + "\n")

spk = {s[0]: s[0][1:] for s in CFG["speakers"]}
out, total, shortest = [], 0, None
for k in KEYS:
    for r in ROUTES:
        p = os.path.join(MOD, "scen", f"{r}_{k}.txt")
        out.append(f"\n==================== {r}_{k}（{ROUTES[r]}） ====================\n")
        who, n = None, 0
        for l in open(p, encoding="utf-8-sig").read().splitlines():
            cmd, _, rest = l.partition(",")
            if cmd == "話者":
                who = "僕" if rest == "相手プレイヤー" else spk.get(rest, rest.lstrip("%"))
            elif cmd == "セリフ":
                out.append(f"{who}「{rest.replace(chr(92)+'n', '')}」"); n += len(rest.replace("\\n", ""))
            elif cmd == "説明":
                out.append(rest.replace("\\n", "\n")); n += len(rest.replace("\\n", ""))
            elif cmd == "射精":
                out.append("（射精）")
        total += n
        if shortest is None or n < shortest[0]:
            shortest = (n, f"{r}_{k}")
with open(os.path.join(DST, f"{OUTN.replace('_MOD','')}_読む用シナリオ集.txt"), "w", encoding="utf-8", newline="\r\n") as fo:
    fo.write(f"{OUTN} 敗北シナリオ28本（読む用。ゲームには入れない）\n" + "\n".join(out) + "\n")

with zipfile.ZipFile(os.path.join(DST, "tools.zip"), "w", zipfile.ZIP_DEFLATED) as z:
    for f in ["cfg.py", "brief.md", "入力内容.json"]:
        if os.path.exists(os.path.join(MOD, f)):
            z.write(os.path.join(MOD, f), f"tools/{f}")
    for sub in ["scen", "lines"]:
        for f in sorted(glob.glob(os.path.join(MOD, sub, "*"))):
            z.write(f, f"tools/{sub}/{os.path.basename(f)}")
    for f in ["gen_v4.py", "cfgkit.py", "patch_recall_ui.py", "check4000.py", "check_lines.py", "STYLE.md", "lines_spec.md"]:
        if os.path.exists(os.path.join(COMMON, f)):
            z.write(os.path.join(COMMON, f), f"tools/common/{f}")

M = CFG["master"]
allc = [M] + [CFG["mons"][k] for k in ["e1", "e2", "e3", "boss"]]
fav = "／".join(f"{d['name']}「{t['name']}」+{t['fav']}" for d in allc for t in d["techs"] if t.get("fav"))
ins = "・".join(f"{d['name']}「{t['name']}」" for d in allc for t in d["techs"] if t.get("insert"))
fate = "破壊" if CFG.get("mon_fate") == "destroy" else "敵側へ寝返り（コントロール変更）"
readme = f"""{OUTN}  {time.strftime('%Y-%m-%d')}
======================================================
サキュバスデュエル用・個人利用のみ。登場人物は全員20歳以上。
{CFG['quest_name']}

■ 内容
- CSV\\Card\\  カード（{C}_master／mons_e1〜e3・mons_boss／magic_1〜5／{C}_recall＝回想の栞{"／" + C + "_josou＝女装娘（デッキ外）" if CFG.get("josou") else ""}）
- CSV\\Eventlist\\Quest\\{C}.txt  クエスト登録（通常＋【回想バトル】の2行）
- {OUTN.replace('_MOD','')}_読む用シナリオ集.txt  敗北シナリオ28本（合計 約{total//1000}千字。ゲームには入れない）
- 画像一覧.txt  必要な画像 {len(imgs)}枚
- tools.zip  生成キット（cfg.py・brief.md・scen 28本・lines 5本・共通スクリプト）

■ ゲームへの入れ方
まとめツールの「ゲームへ反映」で入れる（カード・クエスト登録・画像・回想の栞の共通画像をまとめてコピー。本MODのファイル以外は書き換えない）。

■ 仕組み
- 累積スタック「{S}」：主人公 相手プレイヤー.${S}（12で敗北）、男モンスター 相手.${CFG.get("mstack", S)}（6で{fate}）。
  ★得意技だけ加算：{fav}。
  攻撃時のセリフは受けた側の段階（主人公 1-3/4-6/7-9/10-11、モンスター 0-1/2-3/4/5）で4段階×主人公向け／モンスター向け。
- 指ほぐし：{ins or "なし"} は受けた側の $ほぐし が2未満なら「〇〇の指ほぐし」に置き換わる。
- 回想バトル：「回想の栞」方式。敗北シナリオはマスターの @敗北_<経路>_<責め手>。

■ 直し方
まとめツールの 制作中\\{os.path.basename(MOD)}\\ の cfg.py・scen・lines を直し、「点検」→「組み立て」。
"""
open(os.path.join(DST, "README.txt"), "w", encoding="utf-8", newline="\r\n").write(readme)
shutil.rmtree(os.path.join(MOD, "out"), ignore_errors=True)
print("[OK] 組み立てました: %s" % DST)
print("  カード %d 枚／必要な画像 %d 枚／シナリオ 合計 %d 字（いちばん短い本 %s：%d 字）" % (
    len(glob.glob(os.path.join(DST, "CSV", "Card", "*.txt"))), len(imgs), total, shortest[1], shortest[0]))
if shortest[0] < 5000:
    print("  [注意] 5,000字に届いていない本があります（プロジェクトの決まりは1本5,000字以上。「点検」の基準は約4,000字）。")
