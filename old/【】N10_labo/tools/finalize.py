# 実機確認済みの形（N4・N11）に合わせる後処理。Card/*.txt をまとめて直す
import re,glob,os
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FADE_AFTER=('&敗北CG_','&オナニーCG','&命乞いCG','&おねだりCG','&カード画像')
def fix(text):
    out=[];sec=''
    for line in text.replace('\r\n','\n').split('\n'):
        s=line.strip(); ind=line[:len(line)-len(line.lstrip())]
        if s.startswith('@'): sec=s[1:]
        in_lose=sec.startswith('敗北_') or sec in('敗北処理','敗北再生','前回続き')
        m=re.match(r'話者,(.+)$',s)
        if m:
            who=m.group(1)
            if who.startswith('%'): out.append(line); continue
            if in_lose and who=='相手': who='相手プレイヤー'
            if in_lose and who=='自分': who='%シオリ'
            out.append(f'{ind}{"話者" if in_lose else "話者変更"},{who}'); continue
        m=re.match(r'画像,(.+)$',s)
        if m:
            out.append(f'{ind}{"画像" if in_lose else "画像表示"},{m.group(1)}')
            if m.group(1).startswith(FADE_AFTER) and not (sec=='敗北処理'):
                out.append(f'{ind}フェードイン,1')
            continue
        out.append(line)
        m=re.match(r'(自分プレイヤー|自分)\.\$(最後の責め手|敗北経路),=,(\d+)$',s)
        if m:
            out.append(f'{ind}$$Lab_{m.group(2)},=,{m.group(3)}')
    return '\n'.join(out)
for f in glob.glob(B+'/Card/*.txt'):
    t=open(f,encoding='utf-8').read()
    open(f,'w',encoding='utf-8',newline='\r\n').write(fix(t).rstrip('\n')+'\n')
print('finalized')
