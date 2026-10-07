#!/usr/bin/env python3
"""主人公のセリフの直後に続く \\n 入りのセリフ（話者行の抜け）に、直前の責め手の話者行を補う。
使い方: python3 fix_speaker.py <file> ...   （直した行数を表示）"""
import sys

def fix(p):
    L = open(p, encoding="utf-8-sig").read().split("\n")
    out, spk, last_npc, prev_protag, n = [], None, None, False, 0
    for l in L:
        cmd, _, rest = l.partition(",")
        if cmd == "話者":
            spk = rest
            if rest != "相手プレイヤー":
                last_npc = rest
            prev_protag = False
            out.append(l); continue
        if cmd == "セリフ" and spk == "相手プレイヤー" and prev_protag and "\\n" in rest and last_npc:
            out.append(f"話者,{last_npc}"); spk = last_npc; n += 1
            prev_protag = False
            out.append(l); continue
        prev_protag = (cmd == "セリフ" and spk == "相手プレイヤー")
        out.append(l)
    if n:
        open(p, "w", encoding="utf-8").write("\n".join(out))
    return n

if __name__ == "__main__":
    for p in sys.argv[1:]:
        n = fix(p)
        if n:
            print(f"fixed {n} {p}")
