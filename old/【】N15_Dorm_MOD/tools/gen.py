#!/usr/bin/env python3
# N15 常識改変の社員寮（Dorm） カード生成スクリプト
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from check import parse

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "out", "Dorm_MOD")
CARD = os.path.join(OUT, "Card")
FF = os.path.join(OUT, "EventList", "FieldFaces")
os.makedirs(CARD, exist_ok=True); os.makedirs(FF, exist_ok=True)

C = "Dorm"
G = "自分プレイヤー.$常識改変度"
ROUTES = ["btl", "onani", "inochi", "onedari"]
KEYS = ["m1", "m2", "m3", "e1", "e2", "e3", "boss"]
KEYNUM = {k: i + 1 for i, k in enumerate(KEYS)}   # m1=1 .. boss=7
NAME_IMG = {"サクラ": "Dorm_master", "ハナ": "Dorm_e1", "マナ": "Dorm_e2", "サキ": "Dorm_e3", "ミズキ": "Dorm_boss"}
OWNER = {"master": "サクラ", "e1": "ハナ", "e2": "マナ", "e3": "サキ", "boss": "ミズキ"}

L = {k: json.load(open(os.path.join(BASE, "lines", f"{k}.json"), encoding="utf-8")) for k in KEYS}
TECH = {  # key -> [(name,type)]
    "m1": [(L["m1"]["name"], L["m1"]["type"])],
    "m2": [(L["m2"]["name"], L["m2"]["type"])],
    "m3": [(L["m3"]["name"], L["m3"]["type"])],
}
for k in ["e1", "e2", "e3", "boss"]:
    TECH[k] = [(t["name"], t["type"]) for t in L[k]["techs"]]

# 敗北時の弱点（ブリーフの割当表）
WEAK = {
 "btl":     {"m1":"ハグ","m2":"耳責め","m3":"乳首責め","e1":"ハグ","e2":"耳責め","e3":"乳首責め","boss":"足コキ"},
 "onani":   {k:"強制自慰" for k in KEYS},
 "inochi":  {"m1":"ハグ","m2":"耳責め","m3":"乳首責め","e1":"ハグ","e2":"耳責め","e3":"乳首責め","boss":"足コキ"},
 "onedari": {"m1":"ハグ","m2":"耳責め","m3":"乳首責め","e1":"手コキ","e2":"キス","e3":"本番","boss":"本番"},
}
BAD = set(",$%&#{}<>;\\/")

def safe(s):
    s = s.replace(",", "、")
    for c in BAD:
        if c in s:
            raise ValueError(f"禁止文字 {c}: {s}")
    return s

def wrap(s, n=28):
    out, cur = [], ""
    for ch in s:
        cur += ch
        if len(cur) >= n and ch in "、。！？」）":
            out.append(cur); cur = ""
        elif len(cur) >= n + 8 and ch not in "…—―":
            out.append(cur); cur = ""
    if cur: out.append(cur)
    return "\\n".join(out)

def ser(text):  return "セリフ," + wrap(safe(text))
def exp(text):  return "説明," + wrap(safe(text), 34)

class W:
    def __init__(self): self.l = ["default"]
    def __call__(self, *lines, ind=0):
        for x in lines: self.l.append(" " * ind + x)
    def sec(self, name): self.l.append(""); self.l.append("@" + name)
    def text(self): return "\r\n".join(self.l) + "\r\n"

def stage_if(w, texts, speaker_line, ind=0):
    """4段階のセリフ。texts=[s1..s4]"""
    conds = [("<", 6), ("<", 12), ("<", 18), (">=", 18)]
    if speaker_line:
        w(speaker_line, ind=ind)
    for i, (op, v) in enumerate(conds):
        if i == 0:
            w(f"if,{G},<,6", ind=ind)
        elif i == 3:
            w(f"if,{G},>=,18", ind=ind)
        else:
            lo = 6 if i == 1 else 12
            w(f"if,{G},>=,{lo}", ind=ind); w("{", ind=ind)
            w(f"if,{G},<,{v}", ind=ind + 1)
            w("{", ind=ind + 1); w(ser(texts[i]), ind=ind + 2); w("}", ind=ind + 1)
            w("}", ind=ind)
            continue
        w("{", ind=ind); w(ser(texts[i]), ind=ind + 1); w("}", ind=ind)

def gauge_show(w, ind=0):
    w(f"$表示用,=,{G}", ind=ind)
    w("説明,（常識改変度 {$表示用}／24）", ind=ind)
    w(f"if,{G},>=,24", ind=ind); w("{", ind=ind)
    w("とどめダメージ,相手プレイヤー,9999", ind=ind + 1); w("}", ind=ind)

# ---------------- 敗北シナリオ ----------------
def emit_route(w, rid, owner_name, section):
    items, errs = parse(os.path.join(BASE, "scen", rid + ".txt"))
    assert not errs, (rid, errs)
    route, key = rid.split("_")[2], rid.split("_")[3]
    w.sec(section)
    need = sorted({k for k, _ in items if k in NAME_IMG and k != owner_name})
    for n in need:
        w(f"話者生成,%{n},#{C}/{NAME_IMG[n]}.png,女", ind=4)
    cur = None
    for k, b in items:
        if k == "[CG]":
            w(f"画像,#{C}/{rid}.png,1", ind=4)
        elif k == "[絶頂]":
            w("射精", ind=4); w("フラッシュ,白", ind=4)
        elif k == "＊":
            w(exp(b), ind=4)
        else:
            sp = "自分" if k == owner_name else ("相手プレイヤー" if k == "主人公" else f"%{k}")
            if sp != cur:
                w(f"話者,{sp}", ind=4); cur = sp
            w(ser(b), ind=4)
    w(f"主人公攻撃タイプ弱点付与,{WEAK[route][key]},50", ind=4)

def emit_dispatch(w, keys):
    """@敗北後 と @前回続き と @敗北分岐"""
    w.sec("敗北後")
    w("if,$$Dorm_再生済,==,1", ind=4); w("{", ind=4); w("イベント終了", ind=8); w("}", ind=4)
    w("$経路,=,自分プレイヤー.$敗北経路", ind=4)
    w("$責め手,=,自分プレイヤー.$最後の責め手", ind=4)
    w("イベント実行,敗北分岐", ind=4)
    w("$$Dorm_敗北回数,+=,1", ind=4)
    w("$$Dorm_前回敗北経路,=,$経路", ind=4)
    w("$$Dorm_前回最後の責め手,=,$責め手", ind=4)
    w("フェードアウト,2,true", ind=4)
    w("ゲームオーバー", ind=4)
    w.sec("敗北分岐")
    w("$$Dorm_再生済,=,1", ind=4)
    w("if,$経路,<,1", ind=4); w("{", ind=4); w("$経路,=,1", ind=8); w("}", ind=4)
    lo = min(KEYNUM[k] for k in keys)
    w(f"if,$責め手,<,{lo}", ind=4); w("{", ind=4); w(f"$責め手,=,{lo}", ind=8); w("}", ind=4)
    w(f"if,$責め手,>,{max(KEYNUM[k] for k in keys)}", ind=4); w("{", ind=4); w(f"$責め手,=,{lo}", ind=8); w("}", ind=4)
    w("BGM,&&敗北BGM", ind=4)
    for ri, r in enumerate(ROUTES, 1):
        w(f"if,$経路,==,{ri}", ind=4); w("{", ind=4)
        for k in keys:
            w(f"if,$責め手,==,{KEYNUM[k]}", ind=8); w("{", ind=8)
            w(f"イベント実行,敗北_{r}_{k}", ind=12); w("}", ind=8)
        w("}", ind=4)

def street(w, secs):
    for s in secs:
        w.sec(s + "_街バトル"); w("イベント実行," + s, ind=4)

# ---------------- マスター ----------------
def master():
    w = W()
    w.sec("初期設定")
    w("&カード名,寮母サクラ", "&カード画像,#Dorm/Dorm_master.png", "レベル設定,8", "攻撃力設定,1000",
      "最大HP設定,10000", "属性設定,地属性", "タイプ設定,魔術師", "性別設定,女", "レアリティ設定,UR",
      "攻撃エフェクト設定,&&セクシーエフェクト",
      "効果設定,1,explain,攻撃のたびに常識改変度+2（24で敗北・減らない）。ターン終了時、段階に応じて魅了／メロメロ／攻撃指示不能／魔法使用不能＋500ダメージ",
      "効果設定,0,explain,社員寮さくら寮の寮母。穏やかな微笑みのまま寮の規則を当たり前にしていく。男子寮生は女子の制服で過ごすのが当たり前ですよ",
      "&技CG_1,#Dorm/Dorm_atk_m1.png", "&技CG_2,#Dorm/Dorm_atk_m2.png", "&技CG_3,#Dorm/Dorm_atk_m3.png",
      "&背景,#Dorm/Dorm_bg.png", ind=4)

    # フィールドイベント
    w.sec("フィールドイベント")
    w("話者,自分", ind=4)
    w("if,$$Dorm_敗北回数,==,0", ind=4); w("{", ind=4)
    for t in ["街の外れ、古い木造の寮の門の前で、割烹着の女性が箒を動かす手を止めた。",
              "深緑の髪をまとめた寮母は、こちらを見るなり柔らかく微笑んだ。門をくぐった瞬間、どこか頭の奥がふわりと軽くなる。"]:
        w(exp(t), ind=8)
    w("画像,#Dorm/Dorm_master.png,1", ind=8)
    for t in ["あら、いらっしゃい。調査のかたですね。お話は伺っていますよ。",
              "ここは社員寮さくら寮。泊まるかたはみなさん寮生です。寮生は規則を守るのが当たり前ですからね。",
              "まずはカードで、寮の流儀を少しだけ教えてさしあげましょう。"]:
        w(ser(t), ind=8)
    w("}else{", ind=4)
    w("if,is前回プレイヤー勝利", ind=8); w("{", ind=8)
    w(ser("あら、新人さん。この前は負けてしまいましたね。でも結界の中にもう一度入ったということは……規則に慣れてきた証拠ですよ。"), ind=12)
    w("}else{", ind=8)
    prev = {
        1: "おかえりなさい、スズさん。この前は最後まで規則に崩れてしまいましたね。制服はお部屋に用意してありますよ。",
        2: "おかえりなさい、スズさん。個室で我慢できなかった夜のこと、点呼簿にちゃんと残っていますよ。今夜も点呼に来ますか。",
        3: "おかえりなさい、スズさん。とどめを迷ったあの一瞬、規則違反として預かったままですよ。続きの罰を受けに来たのでしょう。",
        4: "おかえりなさい、スズさん。規則に従わせてくださいって、ご自分でおっしゃいましたよね。今日も申し出に来たのでしょう。",
    }
    for i in range(1, 5):
        w(f"if,$$Dorm_前回敗北経路,==,{i}", ind=12); w("{", ind=12); w(ser(prev[i]), ind=16); w("}", ind=12)
    w("アラート,前回の続きから寮の規則に従いますか？", ind=12)
    w("選択肢生成,勝負する,誘いに乗る,引き返す", ind=12)
    w("if,選択肢,==,2", ind=12); w("{", ind=12); w("イベント実行,前回続き", ind=16); w("イベント終了", ind=16); w("}", ind=12)
    w("if,選択肢,==,3", ind=12); w("{", ind=12)
    w(ser("そうですか。門はいつでも開いていますよ。規則も、あなたのお部屋もね。"), ind=16)
    w("イベント終了", ind=16); w("}", ind=12)
    w("}", ind=8)
    w("}", ind=4)
    deck = ["Dorm_mons_e1"] * 3 + ["Dorm_mons_e2"] * 3 + ["Dorm_mons_e3"] * 3 + ["Dorm_mons_boss"] + \
           [f"Dorm_magic_{i}" for i in range(1, 6) for _ in range(2)]
    assert len(deck) == 20
    w("デッキ設定," + ",".join(deck), ind=4)
    w("デッキ報酬設定,500,500,0", ind=4)
    w("バトル開始,&背景,&&戦闘BGM", ind=4)

    w.sec("前回続き")
    w("$経路,=,$$Dorm_前回敗北経路", ind=4)
    w("$責め手,=,$$Dorm_前回最後の責め手", ind=4)
    w("$$Dorm_再生済,=,0", ind=4)
    w("イベント実行,敗北分岐", ind=4)
    w("$$Dorm_敗北回数,+=,1", ind=4)
    w("フェードアウト,2,true", ind=4)
    w("ゲームオーバー", ind=4)

    w.sec("試合開始")
    w(f"{G},=,0", "自分プレイヤー.$敗北経路,=,0", "自分プレイヤー.$最後の責め手,=,0",
      "自分プレイヤー.$最後のマスター技,=,2", "自分プレイヤー.$改定段階,=,0", "$$Dorm_再生済,=,0", "話者,自分", ind=4)
    w(ser("それでは始めましょうか。寮の規則その一。勝負の最中も、寮母の言うことはよく聞くこと。当たり前ですよ。"), ind=4)

    w.sec("召喚宣言")
    stage_if(w, ["さあ、寮の子を紹介しますね。みなさん、新人さんに規則を教えてあげて。",
                 "今日もきちんと着ましょうね。着付けの子を呼びましょうか。",
                 "点呼の時間が近いですね。みなさん、持ち場についてください。",
                 "もう誰も驚きませんよ。みんな同じですから。"], "話者,自分", ind=4)

    # 戦闘
    w.sec("戦闘")
    w("攻撃タイプランダム変更," + ",".join(TECH[k][0][1] for k in ["m1", "m2", "m3"]), ind=4)
    w("$今回付与,=,0", ind=4)
    w("if,自分プレイヤー.$敗北経路,!=,4", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,1", ind=8); w("}", ind=4)
    eff = {"ハグ": "&&セクシーエフェクト", "耳責め": "&&キスエフェクト", "乳首責め": "&&セクシーエフェクト"}
    for i, k in enumerate(["m1", "m2", "m3"], 1):
        name, typ = TECH[k][0]
        w(f"if,攻撃タイプ,==,{typ}", ind=4); w("{", ind=4)
        w("話者,自分", ind=8)
        w(f"技名表示,{safe(name)}", ind=8)
        w(f"画像,&技CG_{i},1", ind=8)
        stage_if(w, L[k]["enemy"], None, ind=8)
        stage_if(w, L[k]["hero"], "話者,相手", ind=8)
        w("話者,自分", ind=8)
        w(f"攻撃エフェクト変更,{eff[typ]}", ind=8)
        w(f"自分プレイヤー.$最後の責め手,=,{i}", f"自分プレイヤー.$最後のマスター技,=,{i}",
          f"{G},+=,2", "$今回付与,=,1", ind=8)
        gauge_show(w, ind=8)
        w("}", ind=4)
    w("if,$今回付与,==,0", ind=4); w("{", ind=4)
    w(f"{G},+=,1", ind=8); gauge_show(w, ind=8); w("}", ind=4)

    w.sec("戦闘後")
    convert(w, "サクラ", "あら、あなたも寮生になりたいのね。いいですよ。制服を用意しますから、こちらへいらっしゃい。")

    w.sec("ターン終了宣言")
    w("話者,自分", ind=4)
    w(f"if,{G},>=,24", ind=4); w("{", ind=4); w("とどめダメージ,相手プレイヤー,9999", ind=8); w("イベント終了", ind=8); w("}", ind=4)
    w(f"if,{G},>=,1", ind=4); w("{", ind=4)
    w(f"if,{G},<,6", ind=8); w("{", ind=8)
    w(ser("規則ですから。少しずつ慣れていきましょうね。"), "状態異常付与,相手プレイヤー,魅了,1", ind=12); w("}", ind=8)
    w("}", ind=4)
    w(f"if,{G},>=,6", ind=4); w("{", ind=4)
    w(f"if,{G},<,12", ind=8); w("{", ind=8)
    w(ser("明日の朝もきちんと着付けましょうね。ほら、胸がどきどきしてきたでしょう。"), "状態異常付与,相手プレイヤー,メロメロ,1", ind=12); w("}", ind=8)
    w("}", ind=4)
    w(f"if,{G},>=,12", ind=4); w("{", ind=4)
    w(f"if,{G},<,18", ind=8); w("{", ind=8)
    w(ser("点呼の時間です。点呼の間は、寮生は動かないのが当たり前ですよ。"), "状態異常付与,相手プレイヤー,攻撃指示不能,1", ind=12); w("}", ind=8)
    w("}", ind=4)
    w(f"if,{G},>=,18", ind=4); w("{", ind=4)
    w(ser("みんな同じですよ。カードも、もう持たなくていいんです。"), "状態異常付与,相手プレイヤー,魔法使用不能,1",
      "効果ダメージ,相手プレイヤー,500", ind=8); w("}", ind=4)

    w.sec("命乞い")
    w("話者,自分", ind=4)
    w("画像,#Dorm/Dorm_inochigoi.png,1", ind=4)
    w("if,命乞い回数,<=,1", ind=4); w("{", ind=4)
    w(ser("あら、手を上げるのですか。寮母に手を上げるのは寮規則違反ですよ。規則ですから。"), ind=8)
    w(ser("ここで私を倒しても、あなたが違反者になるだけ。それでもいいなら、どうぞ。"), ind=8)
    w("}else{", ind=4)
    w(ser("また迷っていますね。ほら、前にも同じところで止まったでしょう。体が規則を覚えているんですよ。"), ind=8)
    w("}", ind=4)
    w("選択肢生成,とどめを刺す,迷う", ind=4)
    w("if,選択肢,==,1", ind=4); w("{", ind=4)
    w(ser("……そう。それも一つの答えですね。規則はいつでもここで待っていますよ。"), "命乞い失敗", "イベント終了", ind=8); w("}", ind=4)
    w("自分プレイヤー.$敗北経路,=,3", ind=4)
    w("if,自分プレイヤー.$最後の責め手,<,1", ind=4); w("{", ind=4); w("自分プレイヤー.$最後の責め手,=,2", ind=8); w("}", ind=4)
    w("if,自分プレイヤー.$最後の責め手,>,3", ind=4); w("{", ind=4); w("自分プレイヤー.$最後の責め手,=,自分プレイヤー.$最後のマスター技", ind=8); w("}", ind=4)
    w(ser("迷いましたね。規則を知りながら手を止めた。それは規則を受け入れたということですよ。"), ind=4)
    w(ser("罰は規則どおりに。さあ、こちらへいらっしゃい、スズさん。"), ind=4)
    w("話者,相手プレイヤー", ind=4)
    w(ser("手が……動かない……規則だから……当たり前、だから……"), ind=4)
    w("とどめダメージ,相手プレイヤー,9999", ind=4)

    w.sec("おねだり")
    w("話者,自分", ind=4)
    w("画像,#Dorm/Dorm_onedari.png,1", ind=4)
    w(ser("あら、自分から規則に従わせてくださいって言いに来たのね。いい子ですよ。何をしてほしいのか、ちゃんと言いましょうね。"), ind=4)
    w("選択肢生成," + ",".join(safe(TECH[k][0][0]) for k in ["m1", "m2", "m3"]), ind=4)
    for i, k in enumerate(["m1", "m2", "m3"], 1):
        w(f"if,選択肢,==,{i}", ind=4); w("{", ind=4)
        w(f"攻撃タイプ固定,{TECH[k][0][1]}", f"自分プレイヤー.$最後の責め手,=,{i}", f"自分プレイヤー.$最後のマスター技,=,{i}", ind=8); w("}", ind=4)
    w("自分プレイヤー.$敗北経路,=,4", "状態異常付与,自分,弱点付与スキル,1", ind=4)
    w(ser("はい、承りました。寮生の申し出は、寮母が叶えるのが当たり前ですからね。"), ind=4)

    w.sec("おねだり後")
    w("攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル", ind=4)
    w("if,相手プレイヤーHP,>,0", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,0", ind=8); w("}", ind=4)

    w.sec("オナニー")
    w("画像,#Dorm/Dorm_onanie.png,1", "話者,相手", ind=4)
    w(ser("だめだ……制服の布が擦れて……手が、勝手に……"), ind=4)
    w("話者,自分", ind=4)
    w("if,オナニー回数,<=,1", ind=4); w("{", ind=4)
    w(ser("あら……消灯前の自慰は寮規則違反ですよ。点呼簿に書いておきますね。"), ind=8)
    w("}else{", ind=4)
    w(ser("また我慢できなかったのね。前の夜と同じ手つき。もう癖になっているのかしら。"), ind=8)
    w("}", ind=4)
    w("if,$$Dorm_前回敗北経路,==,2", ind=4); w("{", ind=4)
    w(ser("前の点呼のこと、思い出したのでしょう。いいんですよ、スズさん。そういう子は、みんなここに戻ってくるの。"), ind=8); w("}", ind=4)
    w("自分プレイヤー.$敗北経路,=,2", ind=4)
    w("if,自分プレイヤー.$最後の責め手,<,1", ind=4); w("{", ind=4); w("自分プレイヤー.$最後の責め手,=,3", ind=8); w("}", ind=4)
    w("とどめダメージ,相手プレイヤー,9999", ind=4)

    w.sec("終了時一言")
    w("if,自分プレイヤー.$敗北経路,==,0", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,1", ind=8); w("}", ind=4)
    w("話者,自分", ind=4)
    w("if,is勝利", ind=4); w("{", ind=4)
    w(ser("はい、おしまい。今日からあなたはスズさん。寮の規則は、当たり前に守りましょうね。"), ind=8)
    w("}else{", ind=4)
    w(ser("あら、負けてしまいました。でも、門をくぐったあなたの体は、もう少しだけ規則を覚えていますよ。"), ind=8)
    w("}", ind=4)

    emit_dispatch(w, KEYS)
    for r in ROUTES:
        for k in KEYS:
            emit_route(w, f"Dorm_lose_{r}_{k}", "サクラ", f"敗北_{r}_{k}")
    street(w, ["戦闘", "戦闘後", "命乞い", "おねだり", "おねだり後", "オナニー", "終了時一言", "敗北後"])
    return w.text()

def convert(w, who, line):
    w(f"if,{G},>=,8", ind=4); w("{", ind=4)
    w("if,相手,==,相手モンスター.?性別:男", ind=8); w("{", ind=8)
    w("if,相手.HP,<=,1", ind=12); w("{", ind=12)
    w("話者,自分", ser(line) if True else "", ind=16)
    w("コントロール変更,相手,自分所属", ind=16)
    w("説明,常識改変度が高まり、男モンスターが寮生として敵側に移った。", ind=16)
    w("}", ind=12); w("}", ind=8); w("}", ind=4)

# ---------------- モンスター ----------------
MON = {
 "e1": dict(name="着付け担当ハナ", lv=4, atk=1200, hp=3000, attr="風属性", typ="魔術師", rare="R",
            eff="召喚時：常識改変度+1。攻撃のたびに常識改変度+1。スカート規則で魅了を付与",
            flavor="桜色の髪の着付け係。帯も紐もリボンも、一度結んだらほどけない。はい、腕を上げてくださいませ",
            status={1: None, 2: ("魅了", 2)}),
 "e2": dict(name="挨拶担当マナ", lv=3, atk=1000, hp=2800, attr="水属性", typ="魔術師", rare="R",
            eff="自分のターン終了時：常識改変度+1（1ターン1回）。攻撃のたびに常識改変度+1。挨拶の復唱で魅了を付与",
            flavor="規則書を抱えた生真面目な規則番。言い間違えたら、最初からやり直しです",
            status={1: ("魅了", 1), 2: None}),
 "e3": dict(name="日課担当サキ", lv=4, atk=1400, hp=3200, attr="闇属性", typ="戦士", rare="R",
            eff="召喚時：相手プレイヤーに攻撃指示不能1ターン。攻撃のたびに常識改変度+1。日課の拡張で寸止めを付与",
            flavor="点呼用のバインダーを手放さない監督役。点呼。——返事。遅れた分だけ日課が増えます",
            status={1: None, 2: ("寸止め", 1)}),
 "boss": dict(name="社長秘書ミズキ", lv=7, atk=2500, hp=6000, attr="闇属性", typ="魔術師", rare="SR",
            eff="召喚時：常識改変度+3。攻撃のたびに常識改変度+2。固有効果・規則の改定：場にいる間、常識改変度が6・12・18を越えるたびに相手の男モンスター全体へ300ダメージ（各1回・最大3回）。総仕上げでメロメロを付与",
            flavor="商会の社長秘書。寮の規則そのものを書き換える権限を持つ。規則違反です。処分を言い渡します",
            status={1: ("魅了", 1), 2: ("メロメロ", 1)}),
}
EFFECT_ANIM = {"ハグ": "&&セクシーエフェクト", "手コキ": "&&セクシーエフェクト", "耳責め": "&&キスエフェクト",
               "キス": "&&キスエフェクト", "乳首責め": "&&セクシーエフェクト", "本番": "&&セクシーエフェクト",
               "足コキ": "&&セクシーエフェクト"}

def monster(k):
    m, d = MON[k], L[k]
    who = OWNER[k]; num = KEYNUM[k]
    add = 2 if k == "boss" else 1
    w = W()
    w.sec("初期設定")
    w(f"&カード名,{m['name']}", f"&カード画像,#Dorm/Dorm_{k}.png", f"レベル設定,{m['lv']}", f"攻撃力設定,{m['atk']}",
      f"最大HP設定,{m['hp']}", f"属性設定,{m['attr']}", f"タイプ設定,{m['typ']}", "性別設定,女", f"レアリティ設定,{m['rare']}",
      "攻撃エフェクト設定,&&セクシーエフェクト", f"&技CG,#Dorm/Dorm_atk_{k}.png", ind=4)
    if True:
        w("効果設定,1,forceTrigger," + (safe(m["eff"]) if k != "e2" else "召喚時の口上"), "誘発効果設定,1,場に出た時", "効果条件設定,1,トリガー受動カード,==,自分", ind=4)
    if k in ("e2", "boss"):
        w("効果設定,2,forceTrigger," + ("自分のターン終了時の効果" if k == "e2" else "規則の改定の判定"),
          "誘発効果設定,2,エンドフェイズ開始時", "効果条件設定,2,Now自分ターン,==,true", ind=4)
        if k == "e2":
            w("効果設定,3,explain," + safe(m["eff"]), ind=4)
    w("効果設定,0,explain," + safe(m["flavor"]), ind=4)

    w.sec("効果")
    w("switch,効果ID", ind=4)
    w("case,1", ind=4); w("{", ind=4)
    w("話者,自分", ser(d["summon"]), ind=8)
    if k == "e1":
        w(f"{G},+=,1", ind=8); gauge_show(w, ind=8)
    if k == "e3":
        w("状態異常付与,相手プレイヤー,攻撃指示不能,1", ind=8)
    if k == "boss":
        w(f"{G},+=,3", ind=8); gauge_show(w, ind=8); w("イベント実行,改定判定", ind=8)
    w("}", ind=4)
    w("case,2", ind=4); w("{", ind=4)
    if k == "e2":
        w("話者,自分", ser("寮規則第三条。消灯前の挨拶を復唱してください。——はい、記録しました。"), f"{G},+=,1", ind=8)
        gauge_show(w, ind=8)
    if k == "boss":
        w("イベント実行,改定判定", ind=8)
    w("}", ind=4)
    w("endswitch", ind=4)

    if k == "boss":
        w.sec("改定判定")
        for i, th in enumerate([6, 12, 18], 1):
            w(f"if,{G},>=,{th}", ind=4); w("{", ind=4)
            w(f"if,自分プレイヤー.$改定段階,<,{i}", ind=8); w("{", ind=8)
            w(f"自分プレイヤー.$改定段階,=,{i}", "話者,自分", "技名表示,規則の改定", ser(d["kaitei"][i - 1]),
              "効果ダメージ,相手モンスター.?性別:男,300", ind=12)
            w("}", ind=8); w("}", ind=4)

    w.sec("戦闘")
    w("攻撃タイプランダム変更," + ",".join(t for _, t in TECH[k]), ind=4)
    w("$今回付与,=,0", ind=4)
    w("if,自分プレイヤー.$敗北経路,!=,4", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,1", ind=8); w("}", ind=4)
    for i, (name, typ) in enumerate(TECH[k], 1):
        t = d["techs"][i - 1]
        w(f"if,攻撃タイプ,==,{typ}", ind=4); w("{", ind=4)
        w("話者,自分", f"技名表示,{safe(name)}", "画像,&技CG,1", ind=8)
        stage_if(w, t["enemy"], None, ind=8)
        stage_if(w, t["hero"], "話者,相手", ind=8)
        w("話者,自分", f"攻撃エフェクト変更,{EFFECT_ANIM[typ]}", f"自分プレイヤー.$最後の責め手,=,{num}",
          f"{G},+=,{add}", "$今回付与,=,1", ind=8)
        st = m["status"][i]
        if st:
            w(f"状態異常付与,相手,{st[0]},{st[1]}", ind=8)
        gauge_show(w, ind=8)
        w("}", ind=4)
    w("if,$今回付与,==,0", ind=4); w("{", ind=4)
    w(f"自分プレイヤー.$最後の責め手,=,{num}", f"{G},+=,1", ind=8); gauge_show(w, ind=8); w("}", ind=4)
    if k == "boss":
        w("イベント実行,改定判定", ind=4)

    w.sec("戦闘後")
    convert(w, who, d["convert"])

    w.sec("命乞い")
    w("話者,自分", ind=4)
    w("if,命乞い回数,<=,1", ind=4); w("{", ind=4); w(ser(d["inochi"][0]), ind=8)
    w("}else{", ind=4); w(ser(d["inochi"][1]), ind=8); w("}", ind=4)
    w("選択肢生成,とどめを刺す,迷う", ind=4)
    w("if,選択肢,==,1", ind=4); w("{", ind=4)
    w(ser(d["defeated"]), "命乞い失敗", "イベント終了", ind=8); w("}", ind=4)
    w(f"自分プレイヤー.$敗北経路,=,3", f"自分プレイヤー.$最後の責め手,=,{num}", ind=4)
    w("画像,#Dorm/Dorm_inochigoi.png,1", ser(d["inochi_punish"]), ind=4)
    w("とどめダメージ,相手プレイヤー,9999", ind=4)

    w.sec("おねだり")
    w("話者,自分", ser(d["onedari"]), ind=4)
    w("選択肢生成," + ",".join(safe(n) for n, _ in TECH[k]), ind=4)
    for i, (_, typ) in enumerate(TECH[k], 1):
        w(f"if,選択肢,==,{i}", ind=4); w("{", ind=4); w(f"攻撃タイプ固定,{typ}", ind=8); w("}", ind=4)
    w(f"自分プレイヤー.$敗北経路,=,4", f"自分プレイヤー.$最後の責め手,=,{num}", "状態異常付与,自分,弱点付与スキル,1", ind=4)

    w.sec("おねだり後")
    w("攻撃タイプ固定解除", "状態異常解除,自分,弱点付与スキル", ind=4)
    w("if,相手プレイヤーHP,>,0", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,0", ind=8); w("}", ind=4)

    w.sec("オナニー")
    w("画像,#Dorm/Dorm_onanie.png,1", "話者,自分", ser(d["onani"]), ind=4)
    w(f"自分プレイヤー.$敗北経路,=,2", f"自分プレイヤー.$最後の責め手,=,{num}", "とどめダメージ,相手プレイヤー,9999", ind=4)

    w.sec("終了時一言")
    w("if,自分プレイヤー.$敗北経路,==,0", ind=4); w("{", ind=4); w("自分プレイヤー.$敗北経路,=,1", ind=8); w("}", ind=4)
    w("話者,自分", ind=4)
    w("if,is勝利", ind=4); w("{", ind=4); w(ser(d["end"]), ind=8)
    w("}else{", ind=4); w(ser(d["defeated"]), ind=8); w("}", ind=4)

    emit_dispatch(w, [k])
    for r in ROUTES:
        emit_route(w, f"Dorm_lose_{r}_{k}", who, f"敗北_{r}_{k}")
    street(w, ["効果", "戦闘", "戦闘後", "命乞い", "おねだり", "おねだり後", "オナニー", "終了時一言", "敗北後"])
    return w.text()

# ---------------- 魔法・罠 ----------------
MAGIC = [
 dict(n=1, name="寮規則", typ="通常魔法", rare="R", eff="常識改変度+2",
      flavor="寮生が守るべき規則をまとめた冊子。読むほどに、書かれていることが当たり前に思えてくる",
      lines=["新人さん、まずはこれを読みましょうね。寮規則。ここに書いてあることは、ぜんぶ当たり前のことですよ。"],
      body=[f"{G},+=,2"]),
 dict(n=2, name="制服", typ="通常魔法", rare="R", eff="相手の男モンスター全体に魅了2ターン。常識改変度+1",
      flavor="白いブラウスに赤いリボン、紺のプリーツスカート。男子寮生の制服です",
      lines=["寮生はみんな制服を着るのが当たり前。あなたたちの分も用意しましたよ。サイズはぴったりのはずです。"],
      body=["状態異常付与,相手モンスター.?性別:男,魅了,2", f"{G},+=,1"]),
 dict(n=4, name="新人歓迎", typ="通常魔法", rare="R", eff="自分のデッキから寮スタッフ（モンスター）1枚を手札に加える",
      flavor="新人さんのために、先輩たちが集まってくれました",
      lines=["新人さんの歓迎会ですよ。先輩を一人紹介しましょうね。"],
      body=["効果サーチ,効果対象,自分所属"]),
]

def magic_file(mg):
    w = W()
    w.sec("初期設定")
    w(f"&カード名,{mg['name']}", f"&カード画像,#Dorm/Dorm_magic_{mg['n']}.png", "属性設定,地属性",
      f"タイプ設定,{mg['typ']}", f"レアリティ設定,{mg['rare']}", ind=4)
    if mg["n"] == 3:
        w("効果設定,1,play,場に残る。自分のターン終了時ごとに常識改変度+1。3回で自壊",
          "効果設定,2,forceTrigger,朝礼の進行", "誘発効果設定,2,エンドフェイズ開始時", "効果条件設定,2,Now自分ターン,==,true", ind=4)
    elif mg["n"] == 5:
        w("効果設定,1,forceTrigger,相手の攻撃時に発動。攻撃したカードに攻撃指示不能1ターン。常識改変度+1",
          "誘発効果設定,1,onAttack", "効果条件設定,1,トリガー能動カード.所属,!=,自分所属", ind=4)
    else:
        w(f"効果設定,1,play,{safe(mg['eff'])}", ind=4)
        if mg["n"] == 4:
            w("効果ターゲット設定,1,ランダム,自分デッキ.?isモンスター:true,1", ind=4)
    w("効果設定,0,explain," + safe(mg["flavor"]), ind=4)
    w.sec("効果")
    w("switch,効果ID", ind=4)
    w("case,1", ind=4); w("{", ind=4)
    w("話者,自分プレイヤー", f"画像,#Dorm/Dorm_magic_{mg['n']}.png,1", ind=8)
    for t in mg["lines"]:
        w(ser(t), ind=8)
    w(*mg["body"], ind=8)
    if any(G in b for b in mg["body"]):
        gauge_show(w, ind=8)
    w("}", ind=4)
    if mg["n"] == 3:
        w("case,2", ind=4); w("{", ind=4)
        w("話者,自分プレイヤー", f"画像,#Dorm/Dorm_magic_3.png,1", ser("朝礼の時間ですよ。寮規則、本日の一条。みなさん、ご一緒に。"),
          f"{G},+=,1", "$経過,+=,1", ind=8)
        gauge_show(w, ind=8)
        w("if,$経過,>=,3", ind=8); w("{", ind=8); w("効果破壊,自分", ind=12); w("}", ind=8)
        w("}", ind=4)
    w("endswitch", ind=4)
    street(w, ["効果"])
    return w.text()

MAGIC += [
 dict(n=3, name="朝礼", typ="永続魔法", rare="SR", eff="", flavor="毎朝の朝礼で規則を一条ずつ唱和する。三日目には、誰も疑問を口にしない",
      lines=["明日から毎朝、朝礼に出てもらいますね。寮生は朝礼に出るのが当たり前ですから。"], body=["$経過,=,0"]),
 dict(n=5, name="就寝点呼", typ="通常罠", rare="R", eff="", flavor="消灯前の点呼。名前を呼ばれたら、その場で動かずに返事をすること",
      lines=["そこまで。就寝点呼の時間です。点呼の間は動かないのが規則ですよ。"],
      body=["状態異常付与,トリガー能動カード,攻撃指示不能,1", f"{G},+=,1"]),
]

def main():
    files = {"Dorm_master.txt": master()}
    for k in ["e1", "e2", "e3", "boss"]:
        files[f"Dorm_mons_{k}.txt"] = monster(k)
    for mg in MAGIC:
        files[f"Dorm_magic_{mg['n']}.txt"] = magic_file(mg)
    for fn, t in files.items():
        open(os.path.join(CARD, fn), "w", encoding="utf-8", newline="").write(t)
    open(os.path.join(FF, "Dorm.txt"), "w", encoding="utf-8", newline="").write(
        "#Dorm/Dorm_master.png,Card/Dorm_master,フィールドイベント,場所,==,&&場所モルゲン\r\n")
    print("written", len(files) + 1)

if __name__ == "__main__":
    main()
