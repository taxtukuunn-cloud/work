# 使い方: python ins.py 対象.txt 追記.txt
# 追記.txt は「>>> セクション名|アンカー行の先頭文字列」で始まるブロックを並べる（アンカーの直前に挿入）
import sys
p,q=sys.argv[1],sys.argv[2]
t=open(p,encoding='utf-8').read()
blocks=open(q,encoding='utf-8').read().split('>>> ')[1:]
for b in blocks:
    head,body=b.split('\n',1)
    sec,anchor=head.split('|',1)
    s=t.index('@'+sec+'\n'); e=t.find('\n@',s+1); e=len(t) if e<0 else e
    seg=t[s:e]
    i=seg.index('\n'+anchor)+1
    seg=seg[:i]+body.strip('\n')+'\n'+seg[i:]
    t=t[:s]+seg+t[e:]
open(p,'w',encoding='utf-8').write(t)
