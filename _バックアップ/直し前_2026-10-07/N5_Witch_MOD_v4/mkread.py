import os
NAMES={"m1":"ミルティ（変化薬の口移し）","m2":"ミルティ（呪いの衣装）","m3":"ミルティ（乳首開発の薬）","e1":"ポーラ（感度上げの塗り薬）","e2":"ドール（脱げないお召し物）","e3":"スモーカ（発情の紫煙）","boss":"オルガ（変化薬のゼリー）"}
R={"btl":"戦闘負け","onani":"オナニー負け","inochi":"命乞い負け","onedari":"おねだり負け"}
out=["N5 魔女の薬屋（翠の瓶）敗北シナリオ集（読む用・ゲームには入れない）",""]
for k,n in NAMES.items():
  for r,rn in R.items():
    out.append(f"■ {n}／{rn}（{r}_{k}）")
    sp=None
    for l in open(f"scen/{r}_{k}.txt",encoding="utf-8").read().splitlines():
      l=l.strip()
      if l in("##PLAY","##END"): out.append("――――"); continue
      c,_,t=l.partition(",")
      if c=="話者": sp="主人公" if "相手プレイヤー" in t else t.lstrip("%")
      elif c=="セリフ": out.append(f"【{sp}】"); out.append(t.replace("\\n","\n"))
      elif c=="説明": out.append(t.replace("\\n","\n"))
    out.append("");out.append("")
open("out/N5_Witch_敗北シナリオ集_読む用.txt","w",encoding="utf-8",newline="\r\n").write("\n".join(out))
