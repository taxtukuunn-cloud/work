import re,os,glob,shutil
SRC='/home/claude/Witch/Card'; DST='/home/claude/Witch2/Card'
os.makedirs(DST,exist_ok=True)
rd=lambda p: open(p,encoding='utf-8').read().replace('\r\n','\n').split('\n')
def wr(p,lines): open(p,'w',encoding='utf-8',newline='').write('\r\n'.join(lines).rstrip('\r\n')+'\r\n')
FADE_KEYS=('Witch_lose_','Witch_onanie')
def img_line(l, defs):
    """画像,#Witch/X.png,1 / 画像,&v,1 -> 画像表示,&img_X,1 (+fade)"""
    ind=l[:len(l)-len(l.lstrip())]; t=l.strip()
    if not t.startswith('画像,'): return [l]
    args=t[3:].split(',')
    ref=args[0]; out=[]
    fade=False
    m=re.match(r'#Witch/([A-Za-z0-9_]+)\.png$',ref)
    if m:
        name=m.group(1); defs.add(name); ref='&img_'+name
        fade=name.startswith(FADE_KEYS)
    out.append(ind+'画像表示,'+','.join([ref]+args[1:]))
    if fade: out.append(ind+'フェードイン,1')
    return out
def sections(lines):
    secs=[];cur=None
    for l in lines[1:]:
        if l.startswith('@'): cur=[l,[]]; secs.append(cur)
        elif cur is not None: cur[1].append(l)
    return secs
def join(secs): 
    out=['default']
    for h,b in secs:
        while b and b[-1].strip()=='' : b=b[:-1]
        out+= [h]+b+['']
    return out
def mirror(l,prefix):
    t=l.strip(); ind=l[:len(l)-len(l.lstrip())]
    m=re.match(re.escape(prefix)+r'\.\$(敗北経路|最後の責め手),=,(\d+)$',t)
    if m: return [l, ind+f'$$Witch_{m.group(1)},=,{m.group(2)}']
    return [l]
def guard_onedari_after(body,prefix):
    out=[]
    for l in body:
        t=l.strip()
        if re.match(re.escape(prefix)+r'\.\$敗北経路,=,',t):
            out+=['if,相手プレイヤー.HP,>,0','{',' '+t,' $$Witch_敗北経路,=,1','}']
        else: out.append(l)
    return out
def add_defs(init,defs):
    have=set(re.findall(r'&img_([A-Za-z0-9_]+),',''.join(init)))
    extra=['    &img_%s,#Witch/%s.png'%(d,d) for d in sorted(defs-have)]
    return init+extra

# ---------- lose scenarios -> master sections ----------
NAMES={'e1':('ポーラ','Witch_e1'),'e2':('ドール','Witch_e2'),'e3':('スモーカ','Witch_e3'),'boss':('オルガ','Witch_boss')}
lose_secs=[];defs=set(['Witch_master','Witch_e1','Witch_e2','Witch_e3','Witch_boss','Witch_bg'])
for r in ['btl','onani','inochi','onedari']:
    for w in ['m1','m2','m3','e1','e2','e3','boss']:
        L=rd(f'{SRC}/Witch_lose_{r}_{w}.txt')
        body=[];started=False
        for l in L:
            if l.strip()=='@イベント': started=True; continue
            if not started or l.strip()=='': continue
            body.append(l)
        new=[]
        if w in NAMES:
            nm,img=NAMES[w]; new.append(f'話者生成,%{nm},&img_{img},女')
        for l in body:
            t=l.strip()
            if t=='話者変更,相手': new.append('話者変更,相手プレイヤー'); continue
            if t=='話者変更,自分プレイヤー': new.append('話者変更,自分'); continue
            if t=='話者変更,自分' and w in NAMES: new.append(f'話者,%{NAMES[w][0]}'); continue
            new+=img_line(l,defs)
        lose_secs.append([f'@敗北_{r}_{w}',new])

# ---------- master ----------
M=sections(rd(f'{SRC}/Witch_master.txt'))
out=[]
for h,b in M:
    if h=='@敗北後':
        b=['イベント実行,敗北処理']
    elif h=='@おねだり後':
        b=guard_onedari_after(b,'自分')
    elif h=='@フィールドイベント':
        nb=[]
        for l in b:
            if l.startswith('デッキ設定,'):
                nb+=['$$Witch_敗北経路,=,1','$$Witch_最後の責め手,=,1','$$Witch_再生済,=,0',l]
            elif l.startswith('バトル開始,'):
                nb+=[l,'if,is敗北,==,true','{',' イベント実行,敗北処理','}']
            else: nb.append(l)
        b=nb
    elif h=='@前回続き':
        b=[('話者変更,相手プレイヤー' if l.strip()=='話者変更,相手' else l) for l in b]
    nb=[]
    for l in b:
        for x in img_line(l,defs): nb+=mirror(x,'自分')
    out.append([h,nb])
# 敗北処理
disp=[]
RN={'btl':1,'onani':2,'inochi':3,'onedari':4}; WN={'m1':1,'m2':2,'m3':3,'e1':4,'e2':5,'e3':6,'boss':7}
for r,rn in RN.items():
    disp+=[f'if,$経路,==,{rn}','{']
    for w,wn in WN.items():
        disp+=[f' if,$責め手,==,{wn}',' {',f'  イベント実行,敗北_{r}_{w}',' }']
    disp+=['}']
proc=['if,$$Witch_再生済,==,1','{',' イベント終了','}','$$Witch_再生済,=,1',
 'BGM,&BGM_敗北','話者変更,相手プレイヤー','画像表示,&カード画像,1','フェードイン,3','背景変更,&背景',
 '$経路,=,$$Witch_敗北経路','$責め手,=,$$Witch_最後の責め手',
 'if,死亡理由,==,オナニー','{',' $経路,=,2','}',
 'if,$経路,<,1','{',' $経路,=,1','}','if,$経路,>,4','{',' $経路,=,1','}',
 'if,$責め手,<,1','{',' $責め手,=,1','}','if,$責め手,>,7','{',' $責め手,=,1','}']+disp+[
 '$$Witch_敗北回数,+=,1','$$Witch_前回敗北経路,=,$経路','$$Witch_前回最後の責め手,=,$責め手',
 'フェードアウト,2,true','ゲームオーバー']
# insert 敗北処理 + lose sections before the 街バトル receivers
idx=next(i for i,(h,b) in enumerate(out) if h.endswith('_街バトル'))
out=out[:idx]+[['@敗北処理',proc]]+lose_secs+out[idx:]
# defs into master @初期設定
init=out[0]; assert init[0]=='@初期設定'
init[1]=add_defs(init[1],defs)
init[1]=[l for l in init[1] if l.strip()!='']
wr(f'{DST}/Witch_master.txt',join(out))

# ---------- monsters ----------
for f in ['Witch_mons_e1','Witch_mons_e2','Witch_mons_e3','Witch_mons_boss']:
    S=sections(rd(f'{SRC}/{f}.txt')); d=set(); o=[]
    for h,b in S:
        if h=='@敗北後': b=['外部カードイベント実行,敗北後,自分プレイヤー']
        elif h=='@おねだり後': b=guard_onedari_after(b,'自分プレイヤー')
        nb=[]
        for l in b:
            for x in img_line(l,d): nb+=mirror(x,'自分プレイヤー')
        o.append([h,nb])
    o[0][1]=[l for l in add_defs(o[0][1],d) if l.strip()!='']
    wr(f'{DST}/{f}.txt',join(o))
# ---------- magic ----------
for i in range(1,6):
    f=f'Witch_magic_{i}'; S=sections(rd(f'{SRC}/{f}.txt')); o=[]
    for h,b in S:
        nb=[]
        for l in b:
            t=l.strip(); ind=l[:len(l)-len(l.lstrip())]
            if t.startswith(f'画像,#Witch/{f}.png'): nb.append(ind+'画像表示,&カード画像,1')
            elif t.startswith('画像,'): raise Exception(t)
            else: nb+=mirror(l,'自分プレイヤー')
        o.append([h,nb])
    wr(f'{DST}/{f}.txt',join(o))
print('ok')
