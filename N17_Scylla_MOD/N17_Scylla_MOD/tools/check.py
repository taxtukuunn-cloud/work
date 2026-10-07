"""Scylla MOD の書式チェック。使い方: python3 check.py <ファイル...>"""
import sys, re, json
OFFICIAL = set('通常攻撃 おっぱい パイズリ ぱふぱふ フェラ 手コキ 足コキ 脇コキ ハグ ふとももコキ 膝コキ 尻コキ 尻尾コキ 髪コキ キス スマタ 素股 魔法責め 触手 触手コキ 耳責め 乳首責め 強制自慰 パンチラ 息 本番'.split())
TEXT_CMDS = ('セリフ', '説明', 'アラート', '技名表示')
BAD = set(',$%&#{}<>;!?♪')
NG_WORDS = ['幼い', 'ロリ', '少女', '小さな子', '子供っぽ', '子どもっぽ', '幼女', '幼児']
def check_text(body):
    e = []
    if re.fullmatch(r"（[^,]*\{\$表示用\}／(24|12|6)）", body):
        return e
    bad = [ch for ch in body if ch in BAD]
    if bad: e.append('禁止文字 ' + ''.join(sorted(set(bad))))
    for w in NG_WORDS:
        if w in body: e.append('禁止語 ' + w)
    return e
def check(path):
    if path.endswith('.json'):
        errs = []
        def walk(o, k=''):
            if isinstance(o, str):
                for x in check_text(o): errs.append(f'{k}: {x} : {o[:30]}')
            elif isinstance(o, list):
                for i, v in enumerate(o): walk(v, f'{k}[{i}]')
            elif isinstance(o, dict):
                for kk, v in o.items(): walk(v, f'{k}.{kk}')
        try:
            walk(json.load(open(path, encoding='utf-8')))
        except Exception as ex:
            errs.append(f'JSONエラー {ex}')
        return errs
    errs = []
    txt = open(path, 'rb').read().decode('utf-8-sig')
    lines = txt.replace('\r\n', '\n').split('\n')
    if lines[0].strip() != 'default':
        errs.append('1行目がdefaultでない')
    depth = 0; prev_if = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if prev_if and s != '{':
            errs.append(f'{i}: ifの次が {{ でない')
        prev_if = s.startswith('if,')
        if s == 'else' or s.startswith('else,'):
            errs.append(f'{i}: 単独else')
        is_text = any(s.startswith(c + ',') for c in TEXT_CMDS)
        if not is_text:
            depth += s.count('{') - s.count('}')
            if depth < 0:
                errs.append(f'{i}: 閉じ括弧過多'); depth = 0
        for c in TEXT_CMDS:
            if s.startswith(c + ','):
                for x in check_text(s[len(c) + 1:]):
                    errs.append(f'{i}: {x} : {s[:40]}')
        for c in ('話者変更', '画像表示'):
            if s.startswith(c + ','):
                errs.append(f'{i}: 旧書式 {c}')
        m = re.match(r'(攻撃タイプランダム変更|主人公攻撃タイプ弱点付与|攻撃タイプ固定),(.*)', s)
        if m:
            parts = m.group(2).split(',')
            names = parts if m.group(1) == '攻撃タイプランダム変更' else parts[:1]
            for n in names:
                if n not in OFFICIAL:
                    errs.append(f'{i}: 非公式の攻撃タイプ {n}')
        m = re.match(r'if,攻撃タイプ,==,(.*)', s)
        if m and m.group(1) not in OFFICIAL:
            errs.append(f'{i}: 非公式の攻撃タイプ {m.group(1)}')
        if not is_text:
            for img in re.findall(r'#([^,\s]+)', s):
                if not re.fullmatch(r'Scylla/Scylla_[A-Za-z0-9_]+\.png', img):
                    errs.append(f'{i}: 画像参照の形式 {img}')
    if depth != 0:
        errs.append(f'括弧の対応が取れていない（残り {depth}）')
    return errs
if __name__ == '__main__':
    bad_total = 0
    for p in sys.argv[1:]:
        e = check(p)
        if e:
            bad_total += 1
            print(f'NG {p}')
            for x in e[:30]: print('   ', x)
        else:
            print(f'OK {p}')
    sys.exit(1 if bad_total else 0)
