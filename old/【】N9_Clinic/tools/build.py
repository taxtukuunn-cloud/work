# -*- coding: utf-8 -*-
"""N9 前立腺クリニック（Clinic）MOD ビルダー
使い方: python build.py  → ../out/ にカード一式を出力し、チェック結果を表示
- 敗北シナリオの原稿は ../src/lose/<経路>_<責め手>.txt（書式は README 参照）
- 原稿がまだ無いルートは、同じ責め手の btl 原稿に経路ごとの導入を付けた「仮版」を出力する
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from data_cards import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "lose")
OUT = os.path.join(ROOT, "out")
CARD = os.path.join(OUT, "Card")
FF = os.path.join(OUT, "EventList", "FieldFaces")
G = "自分プレイヤー.$" + GAUGE          # 共有ゲージ（敵マスターのカード変数）
PC_SPEAKER = "話者,相手プレイヤー"      # 敗北シナリオ内の主人公の話者（実機で違えばここだけ直す）

ROUTES = {1: "btl", 2: "onani", 3: "inochi", 4: "onedari"}
WHO = {1: "m1", 2: "m2", 3: "m3", 4: "e1", 5: "e2", 6: "e3", 7: "boss"}
WHO_NAME = {1: "ミヤビ", 2: "ミヤビ", 3: "ミヤビ", 4: "アヤ", 5: "レン", 6: "ミサ", 7: "カズハ"}
SPEAKER_IMG = {"ミヤビ": "Clinic_master", "アヤ": "Clinic_e1", "レン": "Clinic_e2",
               "ミサ": "Clinic_e3", "カズハ": "Clinic_boss"}
# 弱点（経路×責め手）。オナニー負けは強制自慰
WEAK = {
    "m1": "手コキ", "m2": "本番", "m3": "魔法責め",
    "e1": {"btl": "乳首責め", "inochi": "乳首責め", "onedari": "本番"},
    "e2": {"btl": "本番", "inochi": "本番", "onedari": "手コキ"},
    "e3": {"btl": "本番", "inochi": "本番", "onedari": "魔法責め"},
    "boss": {"btl": "魔法責め", "inochi": "魔法責め", "onedari": "本番"},
}
def weak(route, who):
    if route == "onani":
        return "強制自慰"
    w = WEAK[who]
    return w if isinstance(w, str) else w[route]

STAGE_NAME = ["問診", "検査", "治療", "通院確定"]
BAD_CHARS = set("$%&#{}<>")

def clean(t):
    t = t.replace(",", "、")
    bad = [c for c in t if c in BAD_CHARS]
    if bad:
        raise ValueError("本文に使えない文字 %s : %s" % (bad, t))
    return t

class W:
    def __init__(self):
        self.lines = []
    def __call__(self, s, d=0):
        self.lines.append(" " * d + s)
    def ifb(self, cond, body, d=0, els=None):
        self(f"if,{cond}", d); self("{", d)
        body(d + 1)
        if els:
            self("}else{", d); els(d + 1)
        self("}", d)
    def text(self):
        return "\r\n".join(self.lines) + "\r\n"

def stage_calc(w, d=0):
    w("$段階,=,1", d)
    for i, th in enumerate([6, 12, 18]):
        w.ifb(f"{G},>=,{th}", lambda dd, v=i + 2: w(f"$段階,=,{v}", dd), d)

def show_gauge(w, d):
    w(f"$表示用,=,{G}", d)
    w("説明,（" + GAUGE + " {$表示用}／24）", d)

def finish_check(w, d):
    def fin(dd):
        w("$$Clinic_確定経路,=,$$Clinic_敗北経路", dd)
        w("とどめダメージ,相手プレイヤー,9999", dd)
    w.ifb(f"{G},>=,24", fin, d)

def attack_block(w, tech, idx, sid, d, img_var, is_master):
    def body(dd):
        w("話者,自分", dd)
        w("技名表示," + tech["name"], dd)
        w(f"画像,{img_var},1", dd)
        def vs_pc(d3):
            for s in range(4):
                w.ifb(f"$段階,==,{s+1}", lambda d4, t=tech["atk"][s]: w("セリフ," + clean(t), d4), d3)
            w("話者,相手", d3)
            for s in range(4):
                w.ifb(f"$段階,==,{s+1}", lambda d4, t=tech["pc"][s]: w("セリフ," + clean(t), d4), d3)
        def vs_mon(d3):
            w("セリフ," + clean(tech["mon_atk"]), d3)
            w("話者,相手", d3)
            w("セリフ," + clean(tech["mon_pc"]), d3)
        w.ifb("相手,==,相手プレイヤー", vs_pc, dd, els=vs_mon)
        w("話者,自分", dd)
        w("攻撃エフェクト変更,&&セクシーエフェクト", dd)
        if is_master:
            w(f"$最後の技,=,{sid}", dd)
        w(f"$$Clinic_最後の責め手,=,{sid}", dd)
        w(f"{G},+=,2", dd)
        def jelly(d3):
            w(f"{G},+=,1", d3)
            w("自分プレイヤー.$ゼリー,=,0", d3)
            w("説明,注入されていたゼリーが熱を帯び、責めの感覚を増幅させた", d3)
        w.ifb("自分プレイヤー.$ゼリー,==,1", jelly, dd)
        if tech.get("jelly"):
            w("自分プレイヤー.$ゼリー,=,1", dd)
        if tech["status"]:
            st, n = tech["status"]
            w(f"状態異常付与,相手,{st},{n}", dd)
        w("$今回付与,=,1", dd)
        show_gauge(w, dd)
        finish_check(w, dd)
        w("画像削除,1", dd)
    w.ifb(f"攻撃タイプ,==,{tech['type']}", body, d)

def fallback_add(w, d=0):
    def b(dd):
        w(f"{G},+=,1", dd)
        show_gauge(w, dd)
        finish_check(w, dd)
    w.ifb("$今回付与,==,0", b, d)

def convert_block(w):
    w("@戦闘後")
    def c(d):
        def c2(dd):
            def c3(d3):
                w("話者,自分", d3)
                w("セリフ," + clean(CONVERT_LINE), d3)
                w("コントロール変更,相手,自分所属", d3)
                w("説明,男モンスターは通院患者として院長側の待合室へ移った", d3)
            w.ifb(f"{G},>=,8", c3, dd)
        w.ifb("相手.HP,<=,1", c2, d)
    w.ifb("相手,!=,相手プレイヤー", c)
    w("")

def street_hooks(w, sections):
    for s in sections:
        w(f"@{s}_街バトル")
        w(f"    イベント実行,{s}")
        w("")

def lose_dispatch(w):
    """@敗北再生：N12・ロゼッタで実機確認済みの形。画像は @初期設定 の & 変数、CGの直後にフェードイン"""
    w("@敗北再生")
    w("BGM,&BGM_敗北")
    w("背景,&背景")
    w("画像,&カード画像,1")
    w("フェードイン,1")
    w("$経路,=,$$Clinic_確定経路")
    w.ifb("$経路,==,0", lambda d: w("$経路,=,$$Clinic_敗北経路", d))
    w.ifb("死亡理由,==,オナニー", lambda d: w("$経路,=,2", d))
    w.ifb("$経路,==,0", lambda d: w("$経路,=,1", d))
    w("$責め手,=,$$Clinic_最後の責め手")
    w.ifb("$責め手,==,0", lambda d: w("$責め手,=,1", d))
    for r, rn in ROUTES.items():
        def rb(d, r=r, rn=rn):
            for s_, sn in WHO.items():
                def sb(dd, rn=rn, sn=sn):
                    w(f"イベント実行,敗北_{rn}_{sn}", dd)
                    w(f"主人公攻撃タイプ弱点付与,{weak(rn, sn)},50", dd)
                w.ifb(f"$責め手,==,{s_}", sb, d)
        w.ifb(f"$経路,==,{r}", rb)
    w("画像全削除")
    w("フェードアウト")
    w("$$Clinic_敗北回数,+=,1")
    w("$$Clinic_前回敗北経路,=,$経路")
    w("$$Clinic_前回最後の責め手,=,$責め手")
    w.ifb("$経路,==,2", lambda d: w("$$Clinic_オナニー回数,+=,1", d))
    w.ifb("$経路,==,3", lambda d: w("$$Clinic_命乞い回数,+=,1", d))
    w("説明,GAME OVER")
    w("")

# ---------------- マスター ----------------
def build_master():
    m = MASTER; w = W()
    w("default"); w("@初期設定")
    for s in [f"&カード名,{m['name']}", f"&カード画像,#Clinic/{m['img']}.png", f"レベル設定,{m['lv']}",
              f"攻撃力設定,{m['atk']}", f"最大HP設定,{m['hp']}", f"属性設定,{m['attr']}", f"タイプ設定,{m['type']}",
              "性別設定,女", f"レアリティ設定,{m['rare']}", "攻撃エフェクト設定,&&セクシーエフェクト",
              f"効果設定,1,explain,{clean(m['explain'])}", f"効果設定,0,explain,{clean(m['flavor'])}"]:
        w("    " + s)
    for t in m["techs"]:
        w(f"    &技CG_{t['id']},#Clinic/{t['img']}.png")
    for k in ["inochigoi", "onanie", "onedari"]:
        w(f"    &CG_{k},#Clinic/Clinic_{k}.png")
    w("    &背景,#Clinic/Clinic_bg.png")
    for k, f in [("master", "Clinic_master"), ("e1", "Clinic_e1"), ("e2", "Clinic_e2"), ("e3", "Clinic_e3"), ("boss", "Clinic_boss")]:
        w(f"    &立ち絵_{k},#Clinic/{f}.png")
    for rn in ROUTES.values():
        for sn in WHO.values():
            w(f"    &敗北CG_{rn}_{sn},#Clinic/Clinic_lose_{rn}_{sn}.png")
    w("    &BGM_戦闘,&&戦闘BGM")
    w("    &BGM_敗北,&&敗北BGM")
    w("")
    # フィールドイベント
    F = FIELD
    w("@フィールドイベント")
    w("話者,自分")
    def first(d):
        for k, t in F["first"]:
            w(f"{k},{clean(t)}", d)
    def again(d):
        def won(dd):
            for k, t in F["win"]:
                w(f"{k},{clean(t)}", dd)
        def lost(dd):
            for r in range(1, 5):
                def rl(d3, r=r):
                    for k, t in F["lose"][r]:
                        w(f"{k},{clean(t)}", d3)
                w.ifb(f"$$Clinic_前回敗北経路,==,{r}", rl, dd)
            w("アラート," + clean(F["continue_alert"]), dd)
            w("選択肢生成,診察を受けて立つ,治療の続きを受ける,引き返す", dd)
            def c2(d3):
                w("イベント実行,前回続き", d3); w("イベント終了", d3)
            w.ifb("選択肢,==,2", c2, dd)
            def c3(d3):
                w("セリフ," + clean(F["leave"]), d3); w("イベント終了", d3)
            w.ifb("選択肢,==,3", c3, dd)
        w.ifb("is前回プレイヤー勝利", won, d, els=lost)
    w.ifb("$$Clinic_敗北回数,==,0", first, els=again)
    w("セリフ," + clean(F["challenge"]))
    deck = ["Clinic_mons_e1"] * 3 + ["Clinic_mons_e2"] * 3 + ["Clinic_mons_e3"] * 3 + ["Clinic_mons_boss"]
    for mg in MAGIC:
        deck += [mg["file"]] * 2
    w("デッキ設定," + ",".join(deck))
    for v, val in [("敗北経路", 1), ("確定経路", 0), ("最後の責め手", 1), ("再生済", 0)]:
        w(f"$$Clinic_{v},=,{val}")
    w("バトル開始,&背景,&BGM_戦闘")
    def lost_now(d):
        def p(dd):
            w("$$Clinic_再生済,=,1", dd)
            w("イベント実行,敗北再生", dd)
        w.ifb("$$Clinic_再生済,==,0", p, d)
    w.ifb("is敗北,==,true", lost_now)
    w("")
    # 試合開始
    w("@試合開始")
    for s in [f"自分.${GAUGE},=,0", "自分.$ゼリー,=,0", "自分.$観察6,=,0", "自分.$観察12,=,0", "自分.$観察18,=,0",
              "$$Clinic_敗北経路,=,1", "$$Clinic_確定経路,=,0", "$$Clinic_最後の責め手,=,1", "$$Clinic_再生済,=,0",
              "$最後の技,=,1", "話者,自分"]:
        w(s)
    w("セリフ,では、診察を始めます。……楽にしてください。最初は問診からですよ")
    show_gauge(w, 0)
    w("")
    # 召喚宣言
    w("@召喚宣言")
    w("話者,自分")
    stage_calc(w)
    for s in range(4):
        w.ifb(f"$段階,==,{s+1}", lambda d, t=m["summon"][s]: w("セリフ," + clean(t), d))
    w("")
    # 戦闘
    w("@戦闘")
    w("攻撃タイプランダム変更," + ",".join(t["type"] for t in m["techs"]))
    w("$今回付与,=,0")
    stage_calc(w)
    for t in m["techs"]:
        attack_block(w, t, t["id"], t["id"], 0, f"&技CG_{t['id']}", True)
    fallback_add(w)
    w("")
    convert_block(w)
    # ターン終了宣言
    w("@ターン終了宣言")
    w("話者,自分")
    finish_check(w, 0)
    stage_calc(w)
    effects = [("寸止め", 1), ("発情", 2), ("攻撃指示不能", 1), ("魔法使用不能", 1)]
    for s in range(4):
        def te(d, s=s):
            w("セリフ," + clean(m["turnend"][s]), d)
            w(f"状態異常付与,相手プレイヤー,{effects[s][0]},{effects[s][1]}", d)
            if s == 3:
                w("イベントダメージ,相手プレイヤー,500", d)
        w.ifb(f"$段階,==,{s+1}", te)
    show_gauge(w, 0)
    w("")
    # おねだり
    w("@おねだり")
    w("話者,自分")
    w("画像,&CG_onedari,1")
    w("セリフ,治療をご希望ですか。……では、どの治療を受けたいのか、ご自分の口でどうぞ")
    w("選択肢生成," + ",".join(t["name"] for t in m["techs"]))
    for i, t in enumerate(m["techs"]):
        def ob(d, t=t):
            w("話者,相手", d)
            w("セリフ," + clean({1: "しょ、触診を……お願いします……っ、ちゃんと……全部、触って確かめてください……",
                                 2: "ぜ、前立腺マッサージを……っ、奥の……張ってるところ……押してください……",
                                 3: "に、尿道の……ブジーの治療を……っ、ゼリー、入れて……ください……"}[t["id"]]), d)
            w("話者,自分", d)
            w("セリフ," + clean(f"はい。{t['name']}ですね。……今の言葉、カルテに一言一句書いておきます"), d)
            w(f"攻撃タイプ固定,{t['type']}", d)
        w.ifb(f"選択肢,==,{i+1}", ob)
    w("$$Clinic_敗北経路,=,4")
    w("状態異常付与,自分,弱点付与スキル")
    w("画像削除,1")
    w("")
    w("@おねだり後")
    w("攻撃タイプ固定解除")
    w("状態異常解除,自分,弱点付与スキル")
    w.ifb("相手プレイヤー.HP,>,0", lambda d: w("$$Clinic_敗北経路,=,1", d))
    w("話者,自分")
    w("セリフ,希望どおりの治療でしたね。……次回も、同じ言葉で予約してください")
    w("")
    # 命乞い
    w("@命乞い")
    w("話者,自分")
    w("画像,&CG_inochigoi,1")
    def inochi1(d):
        w("セリフ,……待ってください。ここで治療をやめたら、あなたの症状は悪化します。本当に、治療を拒否しますか", d)
        w("セリフ,私を倒しても、体の火照りは消えませんよ。……ほら、今もこんなに震えている", d)
    def inochi2(d):
        w("セリフ,また迷っていますね。前回もそうでした。……治療拒否の同意書、今度こそ署名できますか", d)
        w("セリフ,手が止まっていますよ。……それが、あなたの本当の答えです", d)
    w.ifb("$$Clinic_命乞い回数,==,0", inochi1, els=inochi2)
    w("選択肢生成,とどめを刺す,迷う")
    def kill(d):
        w("セリフ,……そうですか。治療拒否、承りました。……また、症状が出たら来てくださいね", d)
        w("画像削除,1", d)
        w("命乞い失敗", d)
        w("イベント終了", d)
    w.ifb("選択肢,==,1", kill)
    w("話者,相手")
    w("セリフ,……っ、手が……動かない……")
    w("話者,自分")
    w("セリフ,治療拒否は撤回、ですね。……では、同意書の代わりに、体で署名していただきます")
    w("$$Clinic_確定経路,=,3")
    w("$$Clinic_最後の責め手,=,$最後の技")
    w("とどめダメージ,相手プレイヤー,9999")
    w("")
    # オナニー
    w("@オナニー")
    w("話者,自分")
    w("画像,&CG_onanie,1")
    w("フェードイン,1")
    def on1(d):
        w("セリフ,……待合室で、ご自分で触ってしまったんですね。症状の悪化です。即入院の手続きをしますね", d)
    def on2(d):
        w("セリフ,また待合室で。……前回と同じ手つきですね。カルテの記録と、ほとんど同じです", d)
    w.ifb("$$Clinic_オナニー回数,==,0", on1, els=on2)
    w("話者,相手")
    w("セリフ,ちが……っ、手が……止まらなくて……っ")
    w("話者,自分")
    w("セリフ,止めなくていいですよ。……診察室で、続きを私が引き継ぎます")
    w("$$Clinic_確定経路,=,2")
    w("とどめダメージ,相手プレイヤー,9999")
    w("")
    w("@終了時一言")
    w.ifb("$$Clinic_敗北経路,==,0", lambda d: w("$$Clinic_敗北経路,=,1", d))
    w("話者,自分")
    w("セリフ,お大事に。……と言いたいところですが、あなたにはまだ早いですね")
    w("")
    lose_dispatch(w)
    w("@前回続き")
    w("$$Clinic_確定経路,=,$$Clinic_前回敗北経路")
    w("$$Clinic_最後の責め手,=,$$Clinic_前回最後の責め手")
    w("$$Clinic_再生済,=,1")
    w("イベント実行,敗北再生")
    w("")
    street_hooks(w, ["試合開始", "召喚宣言", "戦闘", "戦闘後", "ターン終了宣言", "おねだり", "おねだり後",
                     "命乞い", "オナニー", "終了時一言"])
    return w.text()

# ---------------- モンスター ----------------
OB_LINES = {
    "乳首の検査": "む、胸の検査を……っ、乳首、たくさん触って……調べてください……",
    "アナル体温計": "お、お尻で……お熱、はかってください……っ、体温計……入れて……",
    "指での前立腺検査": "ぜ、前立腺の検査……お願いします……っ、指で……奥まで……",
    "感度測定": "か、感度……測ってください……っ、止められても……いいから……",
    "アナルゼリー注入": "お、お尻に……ゼリー……入れてください……っ",
    "尿道ゼリー注入": "に、尿道に……お薬……ゼリー、入れてください……っ",
    "尿道ブジー治療": "ブ、ブジーを……っ、奥まで……入れて、治療してください……",
    "内側からの前立腺刺激": "な、内側から……前立腺……揺らしてください……っ",
}

def build_monster(mo, is_boss=False):
    if mo["key"] == "e3":
        for t in mo["techs"]:
            t["jelly"] = True
    w = W()
    w("default"); w("@初期設定")
    for s in [f"&カード名,{mo['name']}", f"&カード画像,#Clinic/{mo['img']}.png", f"レベル設定,{mo['lv']}",
              f"攻撃力設定,{mo['atk']}", f"最大HP設定,{mo['hp']}", f"属性設定,{mo['attr']}",
              f"タイプ設定,{mo['type']}", "性別設定,女", f"レアリティ設定,{mo['rare']}",
              "攻撃エフェクト設定,&&セクシーエフェクト",
              f"効果設定,0,explain,{clean(mo['flavor'])}",
              f"効果設定,1,forceTrigger,{clean(mo['explain'])}",
              "誘発効果設定,1,場に出た時", "効果条件設定,1,トリガー受動カード,==,自分"]:
        w("    " + s)
    has_te = is_boss or mo.get("turnend")
    if has_te:
        w("    効果設定,2,forceTrigger,自分のターン終了時の効果")
        w("    誘発効果設定,2,エンドフェイズ開始時")
        w("    効果条件設定,2,Now自分ターン,==,true")
    w(f"    &技CG,#Clinic/{mo['techs'][0]['img']}.png")
    w("")
    # 効果
    w("@効果")
    w("switch,効果ID")
    w("case,1"); w("{")
    w("    話者,自分")
    w("    セリフ," + clean(mo["summon_line"]))
    if mo["summon_gain"]:
        w(f"    {G},+=,{mo['summon_gain']}")
        show_gauge(w, 4)
        finish_check(w, 4)
    w("}")
    if has_te:
        w("case,2"); w("{")
        w("    話者,自分")
        if is_boss:
            w("    セリフ," + clean(mo["turnend_line"]))
            w("    状態異常付与,相手プレイヤー,寸止め,2")
            observe(w, mo, 4)
        else:
            st, n, line = mo["turnend"]
            w("    セリフ," + clean(line))
            w(f"    状態異常付与,相手プレイヤー,{st},{n}")
        w("}")
    w("")
    # 戦闘
    w("@戦闘")
    w("攻撃タイプランダム変更," + ",".join(t["type"] for t in mo["techs"]))
    w("$今回付与,=,0")
    stage_calc(w)
    for t in mo["techs"]:
        attack_block(w, t, 0, mo["sid"], 0, "&技CG", False)
    fallback_add(w)
    if is_boss:
        observe(w, mo, 0)
    w("")
    convert_block(w)
    # おねだり
    w("@おねだり")
    w("話者,自分")
    w("セリフ,治療のご希望ですね。……どちらにしますか")
    w("選択肢生成," + ",".join(t["name"] for t in mo["techs"]))
    for i, t in enumerate(mo["techs"]):
        def ob(d, t=t):
            w("話者,相手", d)
            w("セリフ," + clean(OB_LINES[t["name"]]), d)
            w("話者,自分", d)
            w("セリフ," + clean(f"{t['name']}ですね。承りました。……今のお願い、カルテに残しておきます"), d)
            w(f"攻撃タイプ固定,{t['type']}", d)
        w.ifb(f"選択肢,==,{i+1}", ob)
    w("$$Clinic_敗北経路,=,4")
    w("状態異常付与,自分,弱点付与スキル")
    w("")
    w("@おねだり後")
    w("攻撃タイプ固定解除")
    w("状態異常解除,自分,弱点付与スキル")
    w.ifb("相手プレイヤー.HP,>,0", lambda d: w("$$Clinic_敗北経路,=,1", d))
    w("")
    # 命乞い
    w("@命乞い")
    w("話者,自分")
    w("セリフ," + clean({
        "e1": "ま、待ってください……っ、私がいなくなったら、誰があなたのお熱をはかるんですか……？ 治療、途中ですよ……",
        "e2": "手順外の行動です。……停止してください。検査を中断すれば、あなたの数値は記録されないまま悪化します",
        "e3": "……待って。お薬、まだ残ってるんです。……あなたのために、温めておいたのに",
        "boss": "……治療拒否ですか。許可しません。私を倒しても、あなたの体は私の診断どおりに悪化し続けます",
    }[mo["key"]]))
    w("選択肢生成,とどめを刺す,迷う")
    def kill(d):
        w("命乞い失敗", d); w("イベント終了", d)
    w.ifb("選択肢,==,1", kill)
    w("話者,相手")
    w("セリフ,……っ、でも……")
    w("話者,自分")
    w("セリフ,迷いましたね。……それは治療に同意したということです")
    w("$$Clinic_確定経路,=,3")
    w(f"$$Clinic_最後の責め手,=,{mo['sid']}")
    w("とどめダメージ,相手プレイヤー,9999")
    w("")
    # オナニー
    w("@オナニー")
    def on(d):
        w("話者,自分", d)
        w("セリフ,……待合室で、ご自分で？ 症状の悪化ですね。診察室へどうぞ", d)
        w("$$Clinic_確定経路,=,2", d)
        w(f"$$Clinic_最後の責め手,=,{mo['sid']}", d)
        w("とどめダメージ,相手プレイヤー,9999", d)
    w.ifb("$$Clinic_確定経路,==,0", on)
    w("")
    w("@終了時一言")
    w.ifb("$$Clinic_敗北経路,==,0", lambda d: w("$$Clinic_敗北経路,=,1", d))
    w("")
    street_hooks(w, ["効果", "戦闘", "戦闘後", "おねだり", "おねだり後", "命乞い", "オナニー", "終了時一言"])
    return w.text()

def observe(w, mo, d):
    """副院長の固有効果『経過観察』：6・12・18を越えるたびに発情＋治療度+1（各1回）"""
    for i, th in enumerate([6, 12, 18]):
        def ob(dd, i=i, th=th):
            def ob2(d3, i=i, th=th):
                w(f"自分プレイヤー.$観察{th},=,1", d3)
                w("話者,自分", d3)
                w("セリフ," + clean(mo["observe"][i]), d3)
                w("状態異常付与,相手プレイヤー,発情,2", d3)
                w(f"{G},+=,1", d3)
                show_gauge(w, d3)
                finish_check(w, d3)
            w.ifb(f"自分プレイヤー.$観察{th},==,0", ob2, dd)
        w.ifb(f"{G},>=,{th}", ob, d)

# ---------------- 魔法・罠 ----------------
def build_magic(mg, i):
    w = W()
    w("default"); w("@初期設定")
    w(f"    &カード名,{mg['name']}")
    w(f"    &カード画像,#Clinic/Clinic_magic_{i}.png")
    w(f"    &CG,#Clinic/Clinic_magic_{i}.png")
    w("    属性設定,光属性")
    w(f"    タイプ設定,{mg['kind']}")
    w(f"    レアリティ設定,{mg['rare']}")
    w(f"    効果設定,0,explain,{clean(mg['flavor'])}")
    if mg["kind"] == "通常罠":
        w(f"    効果設定,1,forceTrigger,{clean(mg['explain'])}")
        w("    誘発効果設定,1,onAttack")
        w("    効果条件設定,1,トリガー能動カード.所属,!=,自分所属")
    else:
        w(f"    効果設定,1,play,{clean(mg['explain'])}")
    if mg["name"] == "紹介状":
        w("    効果ターゲット設定,1,ランダム,自分デッキ.?isモンスター:true,1")
    if mg["name"] == "処方薬":
        w("    効果ターゲット設定,1,選択,相手モンスター.?性別:男,1")
    if mg["kind"] == "永続魔法":
        w("    効果設定,2,forceTrigger,自分のエンドフェイズごとに治療度+1")
        w("    誘発効果設定,2,エンドフェイズ開始時")
        w("    効果条件設定,2,Now自分ターン,==,true")
    w("")
    w("@効果")
    w("switch,効果ID")
    w("case,1"); w("{")
    w("    話者,自分プレイヤー")
    w("    画像,&CG,1")
    w("    セリフ," + clean(mg["line"]))
    if mg["name"] == "検査キット":
        w("    状態異常付与,トリガー能動カード,寸止め,2")
    if mg["name"] == "紹介状":
        w("    効果サーチ,効果対象,自分所属")
    if mg["name"] == "処方薬":
        w("    状態異常付与,効果対象,発情,2")
    if mg["kind"] == "永続魔法":
        w("    $経過,=,0")
    if mg["gain"] and mg["kind"] != "永続魔法":
        w(f"    {G},+=,{mg['gain']}")
        show_gauge(w, 4)
    w("    画像削除,1")
    w("}")
    if mg["kind"] == "永続魔法":
        w("case,2"); w("{")
        w("    話者,自分プレイヤー")
        w("    セリフ," + clean(mg["tick"]))
        w(f"    {G},+=,1")
        w("    $経過,+=,1")
        show_gauge(w, 4)
        def br(d):
            w("説明,治療室の予約期間が終わった", d)
            w("効果破壊,自分", d)
        w.ifb("$経過,>=,3", br, 4)
        w("}")
    w("")
    w("@効果_街バトル")
    w("    イベント実行,効果")
    return w.text()

# ---------------- 敗北シナリオ ----------------
SPK = {"ミヤビ", "アヤ", "レン", "ミサ", "カズハ", "僕"}
ROUTE_INTRO = {  # 原稿がないルートの仮版で、btl原稿の前に付ける導入
    "onani": ["（待合室で。治療度に追い詰められた手が、我慢しきれずに自分の股間へ伸びた）",
              "{N}：……待合室で、ご自分で触ってしまったんですね。症状の悪化です。診察室へどうぞ"],
    "inochi": ["（とどめを刺すはずの手が止まった。治療を拒むことが、どうしてもできなかった）",
               "{N}：迷いましたね。……治療拒否は撤回。では、治療を最後まで受けていただきます"],
    "onedari": ["（自分の口から、治療してください、と言ってしまった。その声はもう取り消せない）",
                "{N}：ご自分からのお願いですね。……承りました。お望みの治療を、最後まで"],
}

def parse_src(text):
    """原稿 → (コマンド行リスト, 本文字数, 使った話者)"""
    out, n, used, cur = [], 0, set(), None
    for raw in text.splitlines():
        s = raw.strip()
        if not s or s.startswith("//"):
            continue
        if s.startswith("!"):
            c = s[1:].split()
            if c[0] == "CG": out.append("画像,&CG,1")
            elif c[0] == "フラッシュ": out.append("フラッシュ,ピンク")
            elif c[0] == "SE": out.append("SE,&&行為はげしめSE" if len(c) > 1 and c[1] == "激" else "SE,&&行為SE")
            elif c[0] == "暗転": out += ["フェードアウト", "フェードイン"]
            else: raise ValueError("不明な命令 " + s)
            continue
        m = re.match(r"^(ミヤビ|アヤ|レン|ミサ|カズハ|僕)：(.+)$", s)
        if m:
            who, body = m.group(1), clean(m.group(2))
            if who != cur:
                out.append(PC_SPEAKER if who == "僕" else f"話者,%{who}")
                cur = who
            if who != "僕":
                used.add(who)
            out.append("セリフ," + body); n += len(body)
        else:
            body = clean(s)
            out.append("説明," + body); n += len(body)
    return out, n, used

STAND_VAR = {"アヤ": "e1", "レン": "e2", "ミサ": "e3", "カズハ": "boss"}

def build_lose(route, who_id):
    """原稿 → マスター内の @敗北_<経路>_<責め手>。
    画像・アイコンは @初期設定 の & 変数だけを使う（N12・N11で実機確認済み）。"""
    who = WHO[who_id]
    p = os.path.join(SRC, f"{route}_{who}.txt")
    provisional = False
    if os.path.exists(p):
        text = open(p, encoding="utf-8").read()
    else:
        provisional = True
        base = open(os.path.join(SRC, f"btl_{who}.txt"), encoding="utf-8").read()
        text = "\n".join(x.replace("{N}", WHO_NAME[who_id]) for x in ROUTE_INTRO[route]) + "\n" + base
    cmds, n, used = parse_src(text)
    w = W()
    w(f"@敗北_{route}_{who}")
    for u in sorted(used):
        if u in STAND_VAR:
            w(f"話者生成,%{u},&立ち絵_{STAND_VAR[u]},女")
    for c in cmds:
        if c == "画像,&CG,1":
            w(f"画像,&敗北CG_{route}_{who},1")
            w("フェードイン,1")
        elif c == "話者,%ミヤビ":
            w("話者,自分")
        else:
            w(c)
    w("")
    return w.text(), n, provisional

def check_braces(txt, name):
    depth = 0
    for i, l in enumerate(txt.split("\r\n")):
        s = l.strip()
        if s in ("{",): depth += 1
        elif s == "}": depth -= 1
        elif s == "}else{": pass
        if depth < 0: raise ValueError(f"{name}:{i+1} 括弧の対応が崩れています")
        if s.startswith("if,"):
            nxt = txt.split("\r\n")[i + 1].strip()
            if nxt != "{": raise ValueError(f"{name}:{i+1} if の直後に {{ がありません")
    if depth != 0: raise ValueError(f"{name} 括弧が閉じていません")

def write(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(txt)

def main():
    import shutil
    shutil.rmtree(OUT, ignore_errors=True)
    report, lose_text = [], ""
    for r in ROUTES.values():
        for sid in WHO:
            txt, n, prov = build_lose(r, sid)
            lose_text += txt
            report.append((f"@敗北_{r}_{WHO[sid]}", n, prov))
    files = {"Clinic_master.txt": build_master() + lose_text}
    for mo in MONSTERS:
        files[mo["file"] + ".txt"] = build_monster(mo)
    files[BOSS["file"] + ".txt"] = build_monster(BOSS, True)
    for i, mg in enumerate(MAGIC, 1):
        files[mg["file"] + ".txt"] = build_magic(mg, i)
    for name, txt in files.items():
        check_braces(txt, name)
        check_images(txt, name)
        write(os.path.join(CARD, name), txt)
    write(os.path.join(FF, "Clinic.txt"),
          "#Clinic/Clinic_master.png,Card/Clinic_master,フィールドイベント,場所,==,&&場所モルゲン")
    print("カード", len(files), "ファイル出力 OK（括弧・if・禁止文字・画像の書き方をチェック済み）")
    ok = True
    for name, n, prov in report:
        flag = "仮版" if prov else ("OK" if n >= 5000 else "字数不足")
        if not prov and n < 5000: ok = False
        print(f"  {name:28s} {n:6d}字  {flag}")
    print("本番原稿の合計", sum(n for _, n, p in report if not p), "字")
    return 0 if ok else 1


def check_images(txt, name):
    """実機で出なかった書き方が残っていないか：直接パスの画像・話者、イベント内での & 代入、外部イベント実行"""
    sec = ""
    for i, l in enumerate(txt.split("\r\n"), 1):
        s_ = l.strip()
        if s_.startswith("@"):
            sec = s_
            continue
        if sec != "@初期設定" and re.match(r"^&[^,]+,#", s_):
            raise ValueError(f"{name}:{i} 画像変数を @初期設定 の外で定義しています: {s_}")
        if re.match(r"^(画像|画像表示|話者生成|背景|背景変更),.*#", s_):
            raise ValueError(f"{name}:{i} 画像を直接パスで指定しています: {s_}")
        if s_.startswith("外部イベント実行"):
            raise ValueError(f"{name}:{i} 外部イベント実行 は使わない（実機でアイコンが出なかった）: {s_}")


if __name__ == "__main__":
    sys.exit(main())
