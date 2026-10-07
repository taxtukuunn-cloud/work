# -*- coding: utf-8 -*-
"""N10 開発ラボ（Lab）画像一括生成ツール

ComfyUI（起動済み）の API に Lab_prompts.json の画像を順に投げ、候補を candidates/ に保存する。
--install でゲームの Picture/Lab/ に正しい名前でコピーする。標準ライブラリのみで動く。

例:
  python run_lab_batch.py --list
  python run_lab_batch.py all
  python run_lab_batch.py lose            （キー名の一部でまとめて指定）
  python run_lab_batch.py Lab_atk_m2 --random --batch 4
  python run_lab_batch.py --install "D:\\Game\\Picture"
"""
import argparse, copy, hashlib, json, os, random, shutil, sys, time, uuid
import urllib.request, urllib.parse, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
PROMPTS = os.path.join(HERE, 'Lab_prompts.json')
WORKFLOW = os.path.join(HERE, 'Lab_workflow_api.json')
CAND = os.path.join(HERE, 'candidates')
PICKS = os.path.join(HERE, 'picks')
MOD = 'Lab'


def log(*a):
    print(*a, flush=True)


# ---------- ComfyUI API ----------
def api(server, path, data=None):
    url = server.rstrip('/') + path
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8') if data is not None else None,
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'replace')
        raise RuntimeError(f'ComfyUI がエラーを返しました（{e.code}）:\n{explain(body)}')
    except urllib.error.URLError as e:
        raise RuntimeError(f'ComfyUI に接続できません（{server}）。ComfyUI を起動してから実行してください。\n{e}')


def download(server, img, dest):
    q = urllib.parse.urlencode({'filename': img['filename'], 'subfolder': img.get('subfolder', ''), 'type': img.get('type', 'output')})
    with urllib.request.urlopen(server.rstrip('/') + '/view?' + q, timeout=120) as r, open(dest, 'wb') as f:
        f.write(r.read())


# ---------- ワークフローの書き換え ----------
def find_nodes(wf, *classes):
    return [k for k, v in wf.items() if v.get('class_type') in classes]


def upstream(wf, link):
    return link[0] if isinstance(link, list) else None


def drop_downstream(wf, node_id):
    """node_id とそれを入力に使うノード（保存など）を消す"""
    todo = [node_id]
    while todo:
        n = todo.pop()
        wf.pop(n, None)
        for k, v in list(wf.items()):
            for val in v.get('inputs', {}).values():
                if isinstance(val, list) and val and val[0] == n:
                    todo.append(k)
                    break


def patch(wf, item, seed, batch, settings, rembg):
    wf = copy.deepcopy(wf)
    ks = find_nodes(wf, 'KSampler', 'KSamplerAdvanced')
    if not ks:
        raise RuntimeError('ワークフローに KSampler がありません。')
    k = wf[ks[0]]['inputs']
    pos, neg = upstream(wf, k.get('positive')), upstream(wf, k.get('negative'))
    wf[pos]['inputs']['text'] = item['positive']
    wf[neg]['inputs']['text'] = item['negative']
    if 'seed' in k:
        k['seed'] = seed
    if 'noise_seed' in k:
        k['noise_seed'] = seed
    for key, sk in (('steps', 'steps'), ('cfg', 'cfg'), ('sampler_name', 'sampler'), ('scheduler', 'scheduler')):
        if key in k and sk in settings:
            k[key] = settings[sk]
    lat = upstream(wf, k.get('latent_image'))
    if lat in wf:
        li = wf[lat]['inputs']
        li['width'], li['height'], li['batch_size'] = settings['width'], settings['height'], batch
    rb = find_nodes(wf, 'InspyrenetRembg')
    if rb and not (rembg and item.get('transparent_background')):
        for n in rb:
            drop_downstream(wf, n)
    for n in find_nodes(wf, 'SaveImage'):
        tag = '_nobg' if any(isinstance(v, list) and v[0] in rb for v in wf[n]['inputs'].values()) else ''
        wf[n]['inputs']['filename_prefix'] = f'{MOD}/{item["key"]}{tag}'
    return wf


# ---------- モデル名の自動合わせ ----------
LOADERS = {'UNETLoader': ('unet_name', ['anima', 'wai']), 'CLIPLoader': ('clip_name', ['qwen', '06b', '0.6b']),
           'VAELoader': ('vae_name', ['qwen_image', 'qwen']), 'CheckpointLoaderSimple': ('ckpt_name', ['anima', 'wai'])}


def resolve_models(server, wf):
    """ワークフローのモデル名が ComfyUI に無ければ、実在する名前から近いものを選んで書き換える"""
    for nid, node in wf.items():
        cls = node.get('class_type')
        if cls not in LOADERS:
            continue
        field, hints = LOADERS[cls]
        want = node['inputs'].get(field)
        try:
            have = api(server, f'/object_info/{cls}')[cls]['input']['required'][field][0]
        except Exception:
            continue
        if want in have:
            continue
        pick = None
        stem = os.path.splitext(want or '')[0].lower()
        cands = [h for h in have if stem and stem in h.lower()] or \
                [h for h in have if any(k in h.lower() for k in hints)] or \
                (have if len(have) == 1 else [])
        if len(cands) >= 1:
            pick = sorted(cands, key=len)[0]
        if pick:
            node['inputs'][field] = pick
            log(f'  モデル名を自動で合わせました: {cls} 「{want}」→「{pick}」')
        else:
            raise RuntimeError(f'{cls} の「{want}」が見つかりません。ComfyUI にあるのは: {", ".join(have) or "（なし）"}\n'
                               f'Lab_workflow_api.json の {field} を書き換えてください。')
    return wf


def explain(body):
    """ComfyUI の検証エラーを読みやすくする"""
    try:
        d = json.loads(body)
        msgs = []
        for nid, ne in d.get('node_errors', {}).items():
            for e in ne.get('errors', []):
                msgs.append(f'ノード{nid}（{ne.get("class_type")}）: {e.get("details") or e.get("message")}')
        return '\n'.join(msgs) or body[:2000]
    except Exception:
        return body[:2000]


# ---------- シード ----------
def seed_of(item):
    """キャラ単位で固定（同じキャラの画像は同じシード）"""
    h = hashlib.sha256(f'{MOD}:{item["seed_name"]}'.encode()).hexdigest()
    return int(h[:12], 16)


# ---------- 生成 ----------
def run_one(server, wf0, item, settings, args):
    seed = args.seed if args.seed is not None else (random.randint(0, 2**48) if args.random else seed_of(item))
    wf = patch(wf0, item, seed, args.batch, settings, not args.no_rembg)
    if args.dry_run:
        path = os.path.join(HERE, f'dryrun_{item["key"]}.json')
        json.dump(wf, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        log(f'  （dry-run）{path} に書き出しました')
        return
    outdir = os.path.join(CAND, item['key'])
    if not args.keep and os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.makedirs(outdir, exist_ok=True)
    cid = str(uuid.uuid4())
    pid = api(server, '/prompt', {'prompt': wf, 'client_id': cid})['prompt_id']
    t0 = time.time()
    while True:
        time.sleep(2)
        h = api(server, f'/history/{pid}')
        if pid in h:
            st = h[pid].get('status', {})
            if st.get('status_str') == 'error':
                raise RuntimeError('生成に失敗しました:\n' + json.dumps(st.get('messages', ''), ensure_ascii=False)[:2000])
            outs = h[pid].get('outputs', {})
            if outs:
                break
        if time.time() - t0 > args.timeout:
            raise RuntimeError(f'{args.timeout}秒待っても終わりませんでした。')
    n = 0
    for out in outs.values():
        for img in out.get('images', []):
            nobg = '_nobg' in img['filename']
            n += 1
            dest = os.path.join(outdir, f'{item["key"]}_s{seed}_{n:02d}{"_nobg" if nobg else ""}.png')
            download(server, img, dest)
    log(f'  → {n}枚 保存（seed {seed}, {int(time.time() - t0)}秒）: {outdir}')


def select(items, targets):
    if not targets or targets == ['all']:
        return items
    out = []
    for t in targets:
        hit = [i for i in items if i['key'] == t] or [i for i in items if t in i['key']]
        if not hit:
            raise SystemExit(f'「{t}」に当てはまる画像がありません。--list で名前を確認してください。')
        out += [i for i in hit if i not in out]
    return out


# ---------- ゲームへ入れる ----------
def install(items, picture_dir):
    dest_dir = os.path.join(picture_dir, MOD)
    os.makedirs(dest_dir, exist_ok=True)
    ok, miss = 0, []
    for it in items:
        pick = os.path.join(PICKS, it['file'])
        src = None
        if os.path.isfile(pick):
            src = pick
        else:
            d = os.path.join(CAND, it['key'])
            if os.path.isdir(d):
                files = [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.png')]
                if it.get('transparent_background') and any('_nobg' in f for f in files):
                    files = [f for f in files if '_nobg' in f]
                if files:
                    src = sorted(files, key=os.path.getmtime)[-1]
        if src:
            shutil.copyfile(src, os.path.join(dest_dir, it['file']))
            ok += 1
        else:
            miss.append(it['file'])
    log(f'{ok}枚を {dest_dir} に入れました。')
    if miss:
        log(f'まだ無い画像 {len(miss)}枚（このままだとゲームが止まる可能性があります）:')
        for m in miss:
            log('  ' + m)


def main():
    ap = argparse.ArgumentParser(description='N10 開発ラボ 画像一括生成')
    ap.add_argument('targets', nargs='*', help='all／キー名／キー名の一部（lose, atk, onani, _e2 など）')
    ap.add_argument('--server', default='http://127.0.0.1:8188')
    ap.add_argument('--workflow', default=WORKFLOW, help='API形式のワークフロー（自分のものに差し替え可）')
    ap.add_argument('--random', action='store_true', help='毎回ランダムなシード')
    ap.add_argument('--seed', type=int, help='シードを指定')
    ap.add_argument('--batch', type=int, default=1, help='1回で出す候補の枚数')
    ap.add_argument('--no-rembg', action='store_true', help='背景除去をしない')
    ap.add_argument('--keep', action='store_true', help='前回の候補を消さずに追加する')
    ap.add_argument('--timeout', type=int, default=900)
    ap.add_argument('--dry-run', action='store_true', help='生成せず、書き換えたワークフローを保存するだけ')
    ap.add_argument('--list', action='store_true', help='画像の一覧を表示')
    ap.add_argument('--list-models', action='store_true', help='ComfyUI にあるモデル名を表示')
    ap.add_argument('--install', metavar='PICTURE', help='ゲームの Picture フォルダ（その下の Lab/ に入れる）')
    a = ap.parse_args()

    data = json.load(open(PROMPTS, encoding='utf-8'))
    items, settings = data['images'], data['settings']

    if a.list:
        for i in items:
            log(f'{i["key"]:<24} シード:{i["seed_name"]:<7} {"背景除去" if i.get("transparent_background") else ""}')
        log(f'計 {len(items)}枚')
        return
    if a.list_models:
        for cls, field in (('UNETLoader', 'unet_name'), ('CLIPLoader', 'clip_name'), ('VAELoader', 'vae_name'), ('CheckpointLoaderSimple', 'ckpt_name')):
            try:
                info = api(a.server, f'/object_info/{cls}')[cls]['input']['required'][field][0]
                log(f'[{cls}]', ', '.join(info) or '（なし）')
            except Exception as e:
                log(f'[{cls}] 取得できません: {e}')
        return
    if a.install:
        install(select(items, a.targets), a.install)
        return
    if not a.targets:
        ap.print_help()
        return

    wf0 = json.load(open(a.workflow, encoding='utf-8'))
    todo = select(items, a.targets)
    if not a.dry_run:
        try:
            resolve_models(a.server, wf0)
        except RuntimeError as e:
            log(f'×{e}')
            return
    log(f'{len(todo)}枚を生成します（{a.server}）')
    fails = []
    for n, it in enumerate(todo, 1):
        log(f'[{n}/{len(todo)}] {it["key"]}')
        try:
            run_one(a.server, wf0, it, settings, a)
        except RuntimeError as e:
            log(f'  ×失敗: {e}')
            fails.append(it['key'])
            if 'に接続できません' in str(e) or '（400）' in str(e):
                log('  設定の問題なので、残りは中止しました。上のメッセージを確認してください。')
                fails += [i['key'] for i in todo[n:]]
                break
    if fails:
        log('失敗した画像: ' + ' '.join(fails))
        log('もう一度：run_lab.bat ' + ' '.join(fails))
    else:
        log('完了。候補は tools\\candidates\\ にあります。気に入ったものを tools\\picks\\ に「キー名.png」で置くと、install で優先されます。')


if __name__ == '__main__':
    main()
