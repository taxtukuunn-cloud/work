"""敗北シナリオを、直す前の本文（控えがあれば控え）から読みやすく出す。
使い方: python dump.py <MOD> [鍵 ...]   鍵を省くと全部。出力は 作業/dump/<MOD>.txt にも書く。
行はそのままの形（字下げだけ外す）で出すので、patches の「元の行」にそのまま写せる。
画像・SE・ウェイト・フェード・画面色・ループダメージの行は省く（射精・フラッシュ・話者は出す）。"""
import sys, os, glob, re
ROOT = 'C:/Users/taku2/Downloads/MOD/'
BAK = ROOT + '_バックアップ/直し前_2026-10-07/'
HERE = os.path.dirname(os.path.abspath(__file__))
SKIP = re.compile(r'^(画像|SE|ウェイト|フェードアウト|フェードイン|画面色|ループダメージ|エフェクト|BGM|背景|話者生成|#)')

mod = sys.argv[1]
want = sys.argv[2:]
base = BAK + mod + '/' if os.path.isdir(BAK + mod) else ROOT + mod + '/'
cards = [f for f in glob.glob(base + '**/Card/*.txt', recursive=True)
         if not re.search(r'画像生成|_控え|diagnostic|旧書式', f.replace('\\', '/'))]
if mod == 'N17_Scylla_MOD':
    cards = [c for c in cards if '/CSV/' in c.replace('\\', '/')]
out = []
for f in cards:
    raw = open(f, 'rb').read()
    t = raw.decode('utf-8-sig')
    lines = t.replace('\r\n', '\n').split('\n')
    cur = None
    for l in lines:
        s = l.strip()
        if s.startswith('@'):
            cur = s if (s.startswith('@敗北_') and (not want or s[4:] in want)) else None
            if cur:
                out.append('\n=== ' + cur + '   (' + os.path.relpath(f, base) + ')')
            continue
        if cur and s and not SKIP.match(s):
            out.append(s)
os.makedirs(os.path.join(HERE, 'dump'), exist_ok=True)
open(os.path.join(HERE, 'dump', mod + '.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
