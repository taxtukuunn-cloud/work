import os
NAMES={"m1":"ジュレア（全身ぬるぬる責め）","m2":"ジュレア（アナルゼリー注入）","m3":"ジュレア（ゼリーの繭）","e1":"アオ（乳首吸い）","e2":"アカ（発情粘液の口移し）","e3":"モモ（桃ゼリーの耳ふさぎ）","boss":"ヴィスカ（内側から前立腺を揺らす）"}
R={"btl":"戦闘負け","onani":"オナニー負け","inochi":"命乞い負け","onedari":"おねだり負け"}
out=["N11 スライム調教（翠の洞）敗北シナリオ集（読む用・ゲームには入れない）",""]
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
open("out/N11_Slime_敗北シナリオ集_読む用.txt","w",encoding="utf-8",newline="\r\n").write("\n".join(out))
