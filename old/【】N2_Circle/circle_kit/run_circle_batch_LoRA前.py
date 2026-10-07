# -*- coding: utf-8 -*-
"""N2 Circle 画像一括生成（ComfyUI API）
使い方:
  python run_circle_batch.py --list
  python run_circle_batch.py                 全52枚
  python run_circle_batch.py Circle_e3       1枚だけ（前方一致で複数指定可）
  python run_circle_batch.py lose_btl --batch 3 --random
オプション:
  --workflow PATH  ひな形のAPIワークフロー（既定: Rosetta_workflow_api.json）
  --server URL     既定 http://127.0.0.1:8188
  --batch N        1枚あたりの候補数（既定1）
  --seed N / --random   シード指定／ランダム（既定はキャラ単位で固定）
  --no-rembg       背景除去を使わない
  --game DIR       ゲームフォルダ。指定すると 候補1枚目を DIR/Picture/Circle/名前.png に置く
  --overwrite      既に画像がある場合も上書き
"""
import json, sys, os, time, hashlib, random, argparse, urllib.request, urllib.parse, copy, shutil

HERE=os.path.dirname(os.path.abspath(__file__))

def load_items():
    return json.load(open(os.path.join(HERE,"Circle_prompts.json"),encoding="utf-8"))

def group_seed(mod, group):
    return int(hashlib.sha256(f"{mod}:{group}".encode()).hexdigest()[:8],16)

def api(server, path, data=None):
    req=urllib.request.Request(server+path, data=json.dumps(data).encode() if data is not None else None,
                               headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def fetch(server, fn, sub, typ):
    q=urllib.parse.urlencode({"filename":fn,"subfolder":sub,"type":typ})
    with urllib.request.urlopen(f"{server}/view?{q}", timeout=120) as r:
        return r.read()

def prepare(wf, item, seed, use_rembg):
    wf=copy.deepcopy(wf)
    ks=[k for k,v in wf.items() if "KSampler" in v.get("class_type","")]
    if not ks: raise SystemExit("ワークフローに KSampler が見つかりません")
    k=ks[0]; kin=wf[k]["inputs"]
    def set_text(link, text):
        nid=link[0]
        node=wf[nid]
        if "text" in node["inputs"]: node["inputs"]["text"]=text
        else:
            for key,val in node["inputs"].items():
                if isinstance(val,str): node["inputs"][key]=text; break
    set_text(kin["positive"], item["positive"])
    set_text(kin["negative"], item["negative"])
    for key in ("seed","noise_seed"):
        if key in kin: kin[key]=seed
    lat=kin.get("latent_image")
    if lat and lat[0] in wf:
        li=wf[lat[0]]["inputs"]
        if "width" in li: li["width"]=item["width"]; li["height"]=item["height"]
        if "batch_size" in li: li["batch_size"]=1
    rembg=[n for n,v in wf.items() if "rembg" in v.get("class_type","").lower() or "inspyrenet" in v.get("class_type","").lower()]
    want_rembg = use_rembg and item.get("transparent_background")
    if not want_rembg and rembg:
        # 背景除去ノードと、それにつながる保存ノードを外す
        drop=set(rembg); changed=True
        while changed:
            changed=False
            for n,v in list(wf.items()):
                if n in drop: continue
                for val in v["inputs"].values():
                    if isinstance(val,list) and len(val)==2 and val[0] in drop:
                        drop.add(n); changed=True; break
        for n in drop: wf.pop(n,None)
    saves=[n for n,v in wf.items() if v.get("class_type") in ("SaveImage","Image Save")]
    for n in saves: wf[n]["inputs"]["filename_prefix"]=f"Circle/{item['name']}"
    # 背景除去を使う場合は、背景除去側の保存だけ残す
    if want_rembg and rembg and len(saves)>1:
        keep=[n for n in saves if any(isinstance(v,list) and v[0] in rembg for v in wf[n]["inputs"].values())]
        for n in saves:
            if keep and n not in keep: wf.pop(n)
    return wf

def run_one(server, wf_tmpl, item, seed, use_rembg, outdir):
    wf=prepare(wf_tmpl, item, seed, use_rembg)
    pid=api(server,"/prompt",{"prompt":wf})["prompt_id"]
    while True:
        time.sleep(2)
        h=api(server,f"/history/{pid}")
        if pid in h:
            h=h[pid]; break
    if h.get("status",{}).get("status_str")=="error":
        print("  エラー:", json.dumps(h.get("status"),ensure_ascii=False)[:500]); return []
    saved=[]
    for node in h.get("outputs",{}).values():
        for im in node.get("images",[]):
            data=fetch(server, im["filename"], im.get("subfolder",""), im.get("type","output"))
            os.makedirs(outdir,exist_ok=True)
            p=os.path.join(outdir,f"{item['name']}_s{seed}.png")
            open(p,"wb").write(data); saved.append(p)
    return saved

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("names",nargs="*"); ap.add_argument("--list",action="store_true")
    ap.add_argument("--workflow",default=os.path.join(HERE,"Rosetta_workflow_api.json"))
    ap.add_argument("--server",default="http://127.0.0.1:8188")
    ap.add_argument("--batch",type=int,default=1); ap.add_argument("--seed",type=int)
    ap.add_argument("--random",action="store_true"); ap.add_argument("--no-rembg",action="store_true")
    ap.add_argument("--game"); ap.add_argument("--overwrite",action="store_true")
    a=ap.parse_args()
    data=load_items(); items=data["items"]
    if a.list:
        for it in items: print(f"{it['name']:28s} {it['rating']:9s} {it['description']}")
        return
    if a.names:
        items=[it for it in items if any(it["name"]==n or it["name"].startswith(n) or it["name"].startswith("Circle_"+n) for n in a.names)]
    if not items: raise SystemExit("該当する画像がありません（--list で一覧）")
    if not os.path.exists(a.workflow): raise SystemExit(f"ワークフローがありません: {a.workflow}")
    wf=json.load(open(a.workflow,encoding="utf-8"))
    if "nodes" in wf: raise SystemExit("画面用のワークフローです。ComfyUIで『Save (API Format)』したJSONを指定してください")
    for it in items:
        cand=os.path.join(HERE,"candidates",it["name"])
        for b in range(a.batch):
            if a.random: seed=random.randint(1,2**31-1)
            elif a.seed is not None: seed=a.seed+b
            else: seed=group_seed(data["mod"],it["seed_group"])+b
            print(f"[{it['name']}] seed={seed} …")
            saved=run_one(a.server,wf,it,seed,not a.no_rembg,cand)
            for p in saved: print("  ->",p)
            if a.game and saved and b==0:
                dst=os.path.join(a.game,"Picture","Circle",it["name"]+".png")
                if a.overwrite or not os.path.exists(dst):
                    os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copy(saved[-1],dst)
                    print("  => ゲームに配置:",dst)
if __name__=="__main__": main()
