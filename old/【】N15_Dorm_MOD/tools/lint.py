import os,re,sys
root=sys.argv[1]; bad=0
IMG=set()
for dp,_,fs in os.walk(root):
  for f in fs:
    p=os.path.join(dp,f); t=open(p,encoding='utf-8',newline='').read()
    if '\r\n' not in t: print('noCRLF',p)
    lines=t.split('\r\n'); depth=0
    if lines[0]!='default' and 'FieldFaces' not in p: print('no default',p)
    for i,l in enumerate(lines):
      s=l.strip()
      if s=='{': depth+=1
      elif s=='}': depth-=1
      elif s=='}else{': pass
      if depth<0: print('neg',p,i); bad+=1; depth=0
      if s.startswith('if,'):
        nx=lines[i+1].strip() if i+1<len(lines) else ''
        if nx!='{': print('if-no-brace',p,i,s); bad+=1
      if s.startswith(('セリフ,','説明,','技名表示,','アラート,')):
        body=s.split(',',1)[1]
        body2=re.sub(r'\{\$表示用\}','',body).replace('\\n','')
        if any(c in body2 for c in ',$%&#{}<>;'): print('badchar',p,i,s[:40]); bad+=1
      for m in re.findall(r'#Dorm/([\w]+\.png)',s): IMG.add(m)
    if depth!=0: print('unbalanced',p,depth); bad+=1
print('images',len(IMG)); print('\n'.join(sorted(IMG)))
print('errors',bad)
