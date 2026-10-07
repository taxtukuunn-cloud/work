import os
NAMES={"m1":"ルミナ（オイルの乳首ほぐし）","m2":"ルミナ（アロマ催眠）","m3":"ルミナ（脳イキ施術）","e1":"ノア（骨盤の奥押し）","e2":"ミント（アロマ催眠）","e3":"リコ（会員登録の暗示）","boss":"ヴィオラ（特別全身施術）"}
R={"btl":"戦闘負け","onani":"オナニー負け","inochi":"命乞い負け","onedari":"おねだり負け"}
out=["N8 洗脳エステ（ルミエール）敗北シナリオ集（読む用・ゲームには入れない）",""]
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
open("out/N8_Esthe_敗北シナリオ集_読む用.txt","w",encoding="utf-8",newline="\r\n").write("\n".join(out))
