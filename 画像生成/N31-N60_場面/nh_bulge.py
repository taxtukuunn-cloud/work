# -*- coding: utf-8 -*-
"""ニューハーフの立ち絵・魔法カード絵に「服の下の股間のふくらみ」を足す（2026-09-27）
対象：N31-N60_場面\\scene_data で type が "nh" の人物（N46〜N60）。
  立ち絵 <コード>_master / _e1 / _e2 / _e3 / _boss と、その人物が出る <コード>_magic_* を書き換える。
  ・positive：safe → sensitive、1girl の直後に「newhalf, crotch bulge, …（勃起していない形）」を入れる
  ・negative：futanari, penis, nsfw を外し、勃起・露出を防ぐ語を足す
何度実行しても同じ（済みの項目は飛ばす）。場面（atk/lose/onanie）は build_scenes.py 側で付く。
使い方（画像生成フォルダで）: python N31-N60_場面\\nh_bulge.py [--check]
"""
import importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PDIR = os.path.join(os.path.dirname(HERE), "prompts")
DDIR = os.path.join(HERE, "scene_data")
STAND = {"m": "master", "e1": "e1", "e2": "e2", "e3": "e3", "boss": "boss"}
POS = ("newhalf, crotch bulge, visible bulge under her clothes, "
       "the soft outline of her flaccid penis showing through the fabric at her crotch")
NEG_ADD = ("erection, erect penis, her penis exposed, penis out of her clothes, erection tenting her clothes, testicles, "
           "pussy, cameltoe")
NEG_DROP = re.compile(r",\s*(futanari|penis|nsfw)(?=\s*,|\s*$)")
QRE = re.compile(r"^masterpiece, best quality, amazing quality, very aesthetic, absurdres, (safe|sensitive), solo, 1girl, ")


def body(p):
    """品質タグ〜1girl を除いた人物部分（魔法の絵がどの人物か照合する用）"""
    return QRE.sub("", p)


def fix(e):
    p = e["positive"]
    if "crotch bulge" in p:
        return False
    m = QRE.match(p)
    if not m:
        return False
    e["positive"] = p[:m.start(1)] + "sensitive" + p[m.end(1):m.end()] + POS + ", " + p[m.end():]
    n = NEG_DROP.sub("", e["negative"])
    e["negative"] = n.rstrip(", ") + ", " + NEG_ADD
    return True


def main():
    check = "--check" in sys.argv
    total = 0
    for f in sorted(os.listdir(DDIR)):
        if not f.endswith(".py"):
            continue
        spec = importlib.util.spec_from_file_location("x", os.path.join(DDIR, f))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        D = mod.DATA
        nh = [w for w, c in D["chars"].items() if c["type"] == "nh"]
        if not nh:
            continue
        code = D["code"]
        pj = os.path.join(PDIR, code + ".json")
        P = json.load(open(pj, encoding="utf-8"))
        # 立ち絵の人物部分の先頭（ポーズの前まで）で魔法の絵を照合する
        heads = {}
        for w in STAND:
            k = "%s_%s" % (code, STAND[w])
            if k in P:
                b = body(P[k]["positive"])
                if b.startswith(POS):
                    b = b[len(POS) + 2:]
                heads[w] = b
        targets = ["%s_%s" % (code, STAND[w]) for w in nh]
        for k, e in P.items():
            if "_magic_" not in k:
                continue
            b = body(e["positive"])
            if b.startswith(POS):
                b = b[len(POS) + 2:]
            best = max(heads, key=lambda w: len(os.path.commonprefix([heads[w], b])))
            if best in nh:
                targets.append(k)
        done = [k for k in targets if k in P and fix(P[k])]
        print("  %-10s ニューハーフ %s → %d件 %s" % (code, ",".join(nh), len(done), " ".join(t.split("_", 1)[1] for t in done)))
        total += len(done)
        if done and not check:
            json.dump(P, open(pj, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("合計 %d件%s" % (total, "（確認のみ）" if check else ""))


if __name__ == "__main__":
    main()
