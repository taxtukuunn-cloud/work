# 簡易記法 src/<経路>_<責め手>.txt → scenarios/<経路>_<責め手>.txt（カード書式）
# 記法 N:説明 M:シオリ P:主人公 A:ミナセ K:クロエ H:ハク X:LX-01 !生コマンド W:弱点の攻撃タイプ
import os,re,glob
B='/home/claude/lab'
SPK={'M':'自分','P':'相手','A':'%ミナセ','K':'%クロエ','H':'%ハク','X':'%LX01'}
BAD=set(',$%&#{}<>')
def split_long(t,lim=90):
    if len(t)<=lim: return [t]
    out=[];cur=''
    for seg in re.split(r'(?<=[。！？])',t):
        if not seg: continue
        if cur and len(cur)+len(seg)>lim: out.append(cur);cur=seg
        else: cur+=seg
    if cur: out.append(cur)
    return out
for p in sorted(glob.glob(B+'/src/*.txt')):
    key=os.path.basename(p)[:-4]
    lines=['@敗北_'+key];cur=None;n=0;err=[]
    for raw in open(p,encoding='utf-8'):
        l=raw.strip()
        if not l: continue
        if l.startswith('!'): lines.append(l[1:]);cur=None if l.startswith('!話者') else cur;continue
        if l.startswith('W:'): lines.append('主人公攻撃タイプ弱点付与,'+l[2:].strip()+',50');continue
        if len(l)<2 or l[1]!=':' or l[0] not in 'NMPAKHX': err.append('記法:'+l[:15]);continue
        tag,body=l[0],l[2:].strip()
        if BAD & set(body): err.append('禁止文字:'+body[:20])
        for part in split_long(body):
            n+=len(part)
            if tag=='N': lines.append('説明,'+part)
            else:
                if cur!=SPK[tag]: lines.append('話者,'+SPK[tag]);cur=SPK[tag]
                lines.append('セリフ,'+part)
    open(f'{B}/scenarios/{key}.txt','w',encoding='utf-8').write('\n'.join(lines)+'\n')
    print(key,n,'' if n>=5000 else '←不足',err if err else '')
