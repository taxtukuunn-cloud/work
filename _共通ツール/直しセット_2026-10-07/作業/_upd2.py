p='apply_mod.py'; t=open(p,encoding='utf-8').read()
old="""        old, new = op[1], op[2]
        hits = [i for i in range(s, e) if lines[i].strip() == old.strip()]"""
new="""        if kind == 'cmd_after':
            # ('cmd_after', '目印の行', '射精', ['フラッシュ,ピンク'])：目印の行より後で最初の「射精」の行を入れ替える
            anchor, cmd, new = op[1], op[2], op[3]
            hits = [i for i in range(s, e) if lines[i].strip() == anchor.strip()]
            if len(hits) != 1:
                if strict: sys.exit('NOT UNIQUE (%d) in %s: %s' % (len(hits), where, anchor[:60]))
                misses.append(anchor[:40]); continue
            j = next((k for k in range(hits[0] + 1, e) if lines[k].strip() == cmd), None)
            if j is None:
                if strict: sys.exit('NO %s after anchor in %s: %s' % (cmd, where, anchor[:60]))
                misses.append(cmd); continue
            ind = lines[j][:len(lines[j]) - len(lines[j].lstrip())]
            lines[j:j + 1] = [ind + x for x in new]
            e += len(new) - 1
            continue
        old, new = op[1], op[2]
        hits = [i for i in range(s, e) if lines[i].strip() == old.strip()]"""
assert old in t and 'cmd_after' not in t; t=t.replace(old,new); open(p,'w',encoding='utf-8').write(t)
h='作業の手引き.md'; s=open(h,encoding='utf-8').read()
old_h="- その時は、**その節の最後の `射精` の行を `フラッシュ,ピンク` に替える**"
new_h="""- **本文を、ところてん・何も出ないメスイキに言い換えた絶頂は、どれも、その絶頂の `射精` の行を `フラッシュ,ピンク` に替える**（画面の演出と本文を合わせる）。途中の絶頂は `('cmd_after', '目印の行', '射精', ['フラッシュ,ピンク'])`（目印の行＝その絶頂の直前の、主人公の声などの行。その後で最初の `射精` が替わる）。前の責めで本当に射精する絶頂の `射精` は残す。
- 最後の絶頂は、**その節の最後の `射精` の行を `フラッシュ,ピンク` に替える**"""
assert old_h in s; s=s.replace(old_h,new_h)
s=s.replace("""  ('last_cmd', '射精', ['フラッシュ,ピンク']),
]""","""  ('cmd_after', r'セリフ,目印の行', '射精', ['フラッシュ,ピンク']),
  ('last_cmd', '射精', ['フラッシュ,ピンク']),
]""")
open(h,'w',encoding='utf-8').write(s); print('ok')
