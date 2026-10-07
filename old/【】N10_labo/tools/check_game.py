# -*- coding: utf-8 -*-
"""N10 開発ラボ：ゲームに正しく入っているかを点検する（読むだけ。何も書き換えない）
使い方: python check_game.py "D:\\GAME\\...\\サキュバスデュエル"
"""
import sys, os, re, json, hashlib, struct, glob

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = json.load(open(os.path.join(HERE, 'expected_hashes.json'), encoding='utf-8'))
ng, warn = [], []

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def png_info(p):
    b = open(p, 'rb').read(33)
    if len(b) < 33 or b[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    w, h = struct.unpack('>II', b[16:24])
    return w, h, b[25]  # 色の種類（6=透過あり）

def main():
    if len(sys.argv) < 2:
        print('ゲームのフォルダ（Picture や CSV がある場所）を指定してください。'); return
    root = sys.argv[1].strip('"')
    if not os.path.isdir(os.path.join(root, 'CSV')):
        print(f'×「{root}」に CSV フォルダがありません。サキュバスデュエルのフォルダ（Picture・CSV がある場所）を指定してください。'); return
    print(f'点検するゲーム: {root}\n')

    # 1) カード
    print('【1】カード（CSV\\Card）')
    card_dir = os.path.join(root, 'CSV', 'Card')
    cards = {}
    for name, h in EXP.items():
        if name == 'Lab.txt':
            continue
        p = os.path.join(card_dir, name)
        if not os.path.isfile(p):
            ng.append(f'カードがありません: CSV\\Card\\{name}'); continue
        cards[name] = p
        if sha(p) != h:
            ng.append(f'カードが最新版ではありません: CSV\\Card\\{name}（最新の zip の Card フォルダの中身で上書きしてください）')
    print(f'  {len(cards)}/10 ファイルあり')
    for other in ('Card', os.path.join('CSV', 'card')):
        d = os.path.join(root, other)
        if os.path.normcase(d) != os.path.normcase(card_dir) and os.path.isdir(d):
            dup = [os.path.basename(f) for f in glob.glob(os.path.join(d, 'Lab_*.txt'))]
            if dup:
                ng.append(f'{other}\\ にも古い Lab カードがあります（{", ".join(dup)}）。二重に読まれるので、{other}\\ 側の Lab_*.txt は消すか別の場所へ移してください')

    # 2) カードの中身の目印（実機で直った形になっているか）
    print('【2】敗北時の表示対策（マスターのカードの中身）')
    m = cards.get('Lab_master.txt')
    if m:
        t = open(m, encoding='utf-8', errors='replace').read()
        checks = [('if,is敗北,==,true', 'バトル開始直後の敗北処理'), ('話者,相手プレイヤー', '主人公の話者＝相手プレイヤー'),
                  ('画像,&敗北CG_btl_m1,1', '敗北CGの公式書式（画像,）'), ('話者生成,%シオリ', 'シオリの話者生成'), ('$$Lab_最後の責め手,=', '責め手の $$ 記録')]
        for key, label in checks:
            if key not in t:
                ng.append(f'マスターのカードに「{label}」がありません（古い版です）')
        lose = re.findall(r'^@敗北_\w+', t, re.M)
        if len(lose) != 28:
            ng.append(f'敗北シナリオが {len(lose)} 本しかありません（28本のはず）')
        for c in cards.values():
            if re.search(r'^@敗北後\s*$', open(c, encoding='utf-8', errors='replace').read(), re.M):
                ng.append(f'{os.path.basename(c)} に @敗北後 が残っています（古い版です。敗北CGが出ない原因）')
        bad = re.findall(r'^\s*話者,相手\s*$', t, re.M)
        if bad:
            ng.append(f'「話者,相手」が {len(bad)} か所残っています（古い版です）')
        print(f'  敗北シナリオ {len(lose)} 本')

    # 3) 画像
    print('【3】画像（Picture\\Lab）')
    pic = os.path.join(root, 'Picture', 'Lab')
    need = set()
    for p in cards.values():
        need |= set(re.findall(r'#Lab/([A-Za-z0-9_]+\.png)', open(p, encoding='utf-8', errors='replace').read()))
    ok = 0
    trans = {'Lab_master.png', 'Lab_e1.png', 'Lab_e2.png', 'Lab_e3.png', 'Lab_boss.png'}
    have = {f.lower(): f for f in os.listdir(pic)} if os.path.isdir(pic) else {}
    for f in sorted(need):
        real = have.get(f.lower())
        if not real:
            ng.append(f'画像がありません: Picture\\Lab\\{f}'); continue
        if real != f:
            warn.append(f'大文字・小文字が違います: {real}（正しくは {f}）')
        info = png_info(os.path.join(pic, real))
        if not info:
            ng.append(f'画像が壊れているか PNG ではありません: {f}'); continue
        w, h, color = info
        if f in trans and color != 6:
            warn.append(f'{f} は背景が透過されていません（表示はされます）')
        ok += 1
    print(f'  {ok}/{len(need)} 枚 OK')
    extra = [v for k, v in have.items() if k.endswith('.png') and k not in {n.lower() for n in need}]
    if extra:
        warn.append('使われていない画像: ' + ', '.join(extra[:10]) + (' …' if len(extra) > 10 else ''))

    # 4) 街に出す設定
    print('【4】FieldFaces')
    ff = None
    for d in ('Eventlist', 'EventList', os.path.join('CSV', 'EventList'), os.path.join('CSV', 'Eventlist')):
        p = os.path.join(root, d, 'FieldFaces', 'Lab.txt')
        if os.path.isfile(p):
            ff = p; break
    if not ff:
        ng.append('Eventlist\\FieldFaces\\Lab.txt がありません（街にシオリが出ません）')
    elif sha(ff) != EXP['Lab.txt']:
        warn.append(f'{ff} の中身が配布版と違います')
    else:
        print('  OK')

    print('\n==============================')
    if ng:
        print(f'× 直すところが {len(ng)} 件あります。このまま始めると、敗北時に画像やアイコンが出ないか、止まる可能性があります。')
        for x in ng: print('  × ' + x)
    else:
        print('○ すべてそろっています。敗北時の画像・アイコンが出る条件は満たしています。')
    for x in warn: print('  △ ' + x)

if __name__ == '__main__':
    main()
