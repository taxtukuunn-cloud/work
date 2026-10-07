import os
NAMES={"m1":"リリム（淫紋なぞり）","m2":"リリム（精気吸いキス）","m3":"リリム（尻尾責め）","e1":"ナギ（吸精キス）","e2":"ルカ（尻尾の乳首なぞり）","e3":"ピオ（羽のくすぐり焦らし）","boss":"ヴァル（王の精気吸い）"}
R={"btl":"戦闘負け","onani":"オナニー負け","inochi":"命乞い負け","onedari":"おねだり負け"}
out=["N3 男の娘淫魔（淫魔の館）敗北シナリオ集（読む用・ゲームには入れない）",""]
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
open("out/N3_Inma_敗北シナリオ集_読む用.txt","w",encoding="utf-8",newline="\r\n").write("\n".join(out))
