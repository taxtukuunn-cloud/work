# 字数・禁止文字・if括弧チェック
import sys,re,glob
def body_len(sec):
    n=0
    for l in sec.splitlines():
        l=l.strip()
        for k in ('セリフ,','説明,'):
            if l.startswith(k): n+=len(l[len(k):])
    return n
def sections(text):
    parts=re.split(r'^@',text,flags=re.M)
    return [(p.splitlines()[0],p) for p in parts[1:]]
bad=re.compile(r'[,$%&#{}<>]')
ok=True
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read()
    lines=t.splitlines()
    depth=0
    for i,l in enumerate(lines,1):
        s=l.strip()
        if s=='{': depth+=1
        if s=='}': depth-=1
        if s=='}else{': pass
        if s.startswith('if,'):
            nxt=lines[i].strip() if i<len(lines) else ''
            if nxt!='{': print(f'{f}:{i} if without brace'); ok=False
        if s=='else': print(f'{f}:{i} lone else'); ok=False
        for k in ('セリフ,','説明,','アラート,'):
            if s.startswith(k):
                body=s[len(k):].replace('{$表示用}','')
                if bad.search(body): print(f'{f}:{i} bad char: {s[:40]}'); ok=False
    if depth!=0: print(f'{f}: brace depth {depth}'); ok=False
    for name,sec in sections(t):
        if name.startswith('敗北_'):
            n=body_len(sec); flag='' if n>=5000 else '  <-- SHORT'
            print(f'{name}: {n}{flag}')
            if n<5000: ok=False
print('OK' if ok else 'NG')
