import glob,re,sys
OFFICIAL=set("通常攻撃 おっぱい パイズリ ぱふぱふ フェラ 手コキ 足コキ 脇コキ ハグ ふとももコキ 膝コキ 尻コキ 尻尾コキ 髪コキ キス スマタ 素股 魔法責め 触手 触手コキ 耳責め 乳首責め 強制自慰 パンチラ 息 本番".split())
imgs=set();bad=0
for p in sorted(glob.glob("out/Card/*.txt")):
    raw=open(p,"rb").read()
    assert raw.count(b"\r\n")==raw.count(b"\n"), p+" not CRLF"
    lines=raw.decode("utf-8").split("\r\n")
    assert lines[0]=="default"
    depth=0;errs=[]
    for i,l in enumerate(lines,1):
        s=l.strip()
        if s=="{": depth+=1
        elif s=="}": depth-=1
        elif s=="}else{": pass
        if depth<0: errs.append(f"L{i} depth<0")
        if s.startswith("if,"):
            if lines[i].strip()!="{": errs.append(f"L{i} if without brace")
        if s=="else" or s.startswith("else,"): errs.append(f"L{i} bare else")
        for key in ("セリフ,","説明,","アラート,"):
            if s.startswith(key):
                t=s.split(",",1)[1]
                t2=re.sub(r"\{\$表示用\}","",t)
                b=[c for c in t2 if c in ",$%&#{}<>"]
                if b: errs.append(f"L{i} bad chars {b}: {t[:30]}")
        if s.startswith("効果設定,"):
            t=s.split(",",3)[3]
            if any(c in t for c in ",$%&#{}<>"): errs.append(f"L{i} bad in explain")
        m=re.findall(r"#Inma/[^,]+\.png",s); imgs.update(m)
        for key in ("攻撃タイプランダム変更,","攻撃タイプ固定,","主人公攻撃タイプ弱点付与,"):
            if s.startswith(key):
                parts=s.split(",")[1:]
                if key.startswith("主人公"): parts=parts[:1]
                for a in parts:
                    if a not in OFFICIAL: errs.append(f"L{i} unofficial type {a}")
        m=re.match(r"if,攻撃タイプ,==,(.+)",s)
        if m and m.group(1) not in OFFICIAL: errs.append(f"L{i} type {m.group(1)}")
    if depth!=0: errs.append(f"final depth {depth}")
    print(("OK " if not errs else "NG ")+p, len(lines)); 
    for e in errs[:10]: print("  ",e)
    bad+=len(errs)
print("\n画像", len(imgs)); print("\n".join(sorted(imgs)))
sys.exit(1 if bad else 0)
