# master_base + scen/*.txt を結合。未執筆ルートは仮シナリオで埋める
import os,re
B='/home/claude/lab'
routes=['btl','onani','inochi','onedari']
hands=['m1','m2','m3','e1','e2','e3','boss']
spk={'m1':'自分','m2':'自分','m3':'自分','e1':'%ミナセ','e2':'%クロエ','e3':'%ハク','boss':'%LX01'}
weak={('m1',''):'乳首責め',('m2',''):'本番',('m3',''):'魔法責め',('e1',''):'乳首責め',('e2',''):'魔法責め',('e3',''):'本番',('boss',''):'触手',
      ('e1','onedari'):'手コキ',('e2','onedari'):'耳責め',('e3','onedari'):'魔法責め',('boss','onedari'):'触手コキ'}
written={}
for f in sorted(os.listdir(B+'/scenarios')):
    if f.endswith('.txt'):
        t=open(B+'/scenarios/'+f,encoding='utf-8').read()
        for p in re.split(r'^@',t,flags=re.M)[1:]:
            written[p.splitlines()[0].strip()]='@'+p.rstrip('\n')+'\n'
out=open(B+'/tools/master_base.txt',encoding='utf-8').read().rstrip('\n')+'\n\n'
stubs=[]
for r in routes:
    for h in hands:
        name=f'敗北_{r}_{h}'
        if name in written:
            out+=written[name]+'\n'
        else:
            stubs.append(name)
            w='強制自慰' if r=='onani' else weak.get((h,r),weak[(h,'')])
            out+=f'''@{name}
話者,{spk[h]}
画像,&敗北CG_{r}_{h},1
セリフ,（仮シナリオ）実験終了。被験体の反応はすべて記録しました。
説明,（このルートの本編は未執筆です。次回の制作で5000字以上の本編に差し替えます）
主人公攻撃タイプ弱点付与,{w},50

'''
out=out.replace('\r\n','\n')
open(B+'/Card/Lab_master.txt','w',encoding='utf-8',newline='\r\n').write(out)
print('written',len(written),'stubs',len(stubs))
# 実機確認済みの形に合わせる後処理（話者変更・画像表示・フェードイン・$$記録）
import subprocess, sys
subprocess.run([sys.executable, B + '/tools/finalize.py'], check=True)
