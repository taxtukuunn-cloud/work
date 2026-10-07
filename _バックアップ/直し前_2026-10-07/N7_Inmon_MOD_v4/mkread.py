import os
NAMES={"m1":"ヴェルミナ（聖印の口づけ）","m2":"ヴェルミナ（紋なぞり）","m3":"ヴェルミナ（神具の儀式）","e1":"ベニ（紅墨の描紋）","e2":"シオン（囁きの香）","e3":"リツ（後ろの躾）","boss":"セレス（完成の抱擁）"}
R={"btl":"戦闘負け","onani":"オナニー負け","inochi":"命乞い負け","onedari":"おねだり負け"}
out=["N7 淫紋の神官（月紋神殿）敗北シナリオ集（読む用・ゲームには入れない）",""]
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
open("out/N7_Inmon_敗北シナリオ集_読む用.txt","w",encoding="utf-8",newline="\r\n").write("\n".join(out))
