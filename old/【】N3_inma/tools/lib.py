# カード生成用の共通部品（N3 Inma）
import os, re

CODE = "Inma"
FRAG_DIR = "/home/claude/Inma/frag"
MON_REACT = "ぐ……っ！ 体に……紋が……浮かんで……！"

def img(name):
    return f"#{CODE}/{CODE}_{name}.png"

def ind(lines, n=1):
    sp = " " * n
    return [sp + l if l else l for l in lines]

def block(cond, body, n=0):
    """if,cond { body } を返す（必ず波括弧）"""
    return [f"if,{cond}", "{"] + ind(body) + ["}"]

def ifelse(cond, a, b):
    return [f"if,{cond}", "{"] + ind(a) + ["}else{"] + ind(b) + ["}"]

def staged(var, four):
    """ゲージ4段階の分岐（<6 / 6-11 / 12-17 / 18+）。four は各段階の行リスト"""
    out = []
    out += block(f"{var},<,6", four[0])
    out += block(f"{var},>=,6", block(f"{var},<,12", four[1]))
    out += block(f"{var},>=,12", block(f"{var},<,18", four[2]))
    out += block(f"{var},>=,18", four[3])
    return out

G = "自分プレイヤー.$淫紋度"

def gauge_add(n):
    return [
        f"{G},+=,{n}",
        f"$表示用,=,{G}",
        "説明,（淫紋度 {$表示用}／24）",
    ] + block(f"{G},>=,24", ["とどめダメージ,相手プレイヤー,9999"])

def attack(atype, waza, cg, self4, opp4, gain, tech_no, extra=None, effect=None):
    """攻撃タイプ1つ分のブロック"""
    body = ["話者変更,自分", f"技名表示,{waza}", f"画像表示,{cg},1"]
    body += staged(G, [[f"セリフ,{s}"] for s in self4])
    body += ["話者変更,相手"]
    body += ifelse("相手,==,相手プレイヤー",
                   staged(G, [[f"セリフ,{s}"] for s in opp4]),
                   [f"セリフ,{MON_REACT}"])
    body += ["話者変更,自分"]
    if effect:
        body += [f"攻撃エフェクト変更,{effect}"]
    body += [f"$最後の技,=,{tech_no}", "$今回付与,=,1"]
    if extra:
        body += extra
    body += gauge_add(gain)
    return block(f"攻撃タイプ,==,{atype}", body)

def frag(name):
    path = os.path.join(FRAG_DIR, name + ".txt")
    with open(path, encoding="utf-8") as f:
        return [l.rstrip("\r\n").strip() for l in f if l.strip()]

def townbattle(sections):
    out = []
    for s in sections:
        out += ["", f"@{s}_街バトル", f"    イベント実行,{s}"]
    return out

def write_card(path, lines):
    text = "\r\n".join(lines) + "\r\n"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
