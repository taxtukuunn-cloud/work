# N32〜N45 用 cfg の共通部品（gen_v4.py の CFG を短く書くため）
def T(name, type_, fav=0, insert=False, finger=False, st=None, eff=None, josou=False):
    d = dict(name=name, type=type_)
    if josou: d["josou"] = True
    if fav: d["fav"] = fav
    if insert: d["insert"] = True
    if finger: d["finger"] = True
    if st: d["statuses"] = [st] if isinstance(st, tuple) else st
    if eff: d["effect"] = eff
    return d


def explain_tech(t, S):
    s = f"【{t['name']}】"
    if t.get("fav"):
        s = "★得意技" + s + f"で受けた相手の{S}+{t['fav']}"
    if t.get("insert"):
        s += "（逆アナル。指で2回ほぐした後だけ。足りなければ指ほぐし）"
    if t.get("finger"):
        s += "（ほぐし+1）"
    for st in t.get("statuses", []):
        s += f"、{st[0]}{st[1]}ターン"
    return s


def MAG(no, name, type_, rare, explain, ops, target=None, persist=False):
    d = dict(no=no, name=name, type=type_, rare=rare, explain=explain, ops=ops)
    if target: d["target"] = target
    if persist:
        d["persist_ops"] = ops
        d["persist_explain"] = "自分のターン終了時：男モンスター1体（いなければ主人公）の累積+1。3回目で自壊。"
    return d


SEL_M = "効果ターゲット設定,1,選択,相手モンスター.?性別:男,1"
SEARCH = "効果ターゲット設定,1,ランダム,自分デッキ.?isモンスター:true,1"


def std_magic(S, spec):
    """spec: [(name, kind, arg)] kind: add n / trap 状態 / target 状態 T / search / persist"""
    out = []
    for i, (name, kind, arg) in enumerate(spec, 1):
        if kind == "add":
            out.append(MAG(i, name, "通常魔法", "R", f"男モンスター1体（いなければ主人公）の{S}+{arg}。", [("add", arg)]))
        elif kind == "trap":
            out.append(MAG(i, name, "通常罠", "R", f"相手が攻撃した時に発動。攻撃したカードに{arg}1ターン。", [("status_attacker", arg, 1)]))
        elif kind == "target":
            st, n = arg
            out.append(MAG(i, name, "通常魔法", "R", f"男モンスター1体に{st}{n}ターン。", [("status_target", st, n)], target=SEL_M))
        elif kind == "josou":
            out.append(MAG(i, name, "通常魔法", "SR", f"相手の男モンスター1体に{arg}を着せる。そのモンスターは即、女装娘になる（主人公側に残る）。", [("josou_target",)], target=SEL_M))
        elif kind == "search":
            out.append(MAG(i, name, "通常魔法", "N", "自分のデッキからモンスター1枚をランダムに手札に加える。", [("search",)], target=SEARCH))
        elif kind == "persist":
            d = MAG(i, name, "永続魔法", "SR", f"発動時と、自分のターン終了時に、男モンスター1体（いなければ主人公）の{S}+1。3回目のターン終了時に自壊する。", [("add", 1)], persist=True)
            d["persist_explain"] = f"自分のターン終了時：男モンスター1体（いなければ主人公）の{S}+1。3回目で自壊。"
            out.append(d)
    return out
