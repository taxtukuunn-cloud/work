"""全MOD共通：patches/<MOD>.py の直しを、控え（直す前）から入れ直す。何度動かしても同じ結果になる。

使い方:  python apply_mod.py <MODフォルダ名> [--dry]
  --dry  書き込まずに、直しが当たるかと、確認の結果だけを出す。

やること
  1. 控え（_バックアップ/直し前_2026-10-07/<MOD>）が無ければ、MODを丸ごとコピーして作る（上書きはしない）。
  2. カード（Card フォルダの *.txt）の @敗北_<鍵> の節に直しを入れる。
  3. 道具の元（tools/scen フォルダ、tools.zip の中の scen）にも同じ直しを入れる。
  4. 読む用シナリオ集を、直す前の本文から作り直してみて、今のファイルと一字も違わなければ、新しい本文で作り直す。
  5. 確かめる：字数が減っていない／使えない記号がない／{ } の数／改行と BOM が元のまま／直していない節が元のまま。

patches/<MOD>.py の書き方
  P = { '<鍵>': [ 操作, ... ], ... }     鍵は @敗北_ の後ろ（例 'btl_m1'、'ロゼッタ'）
  操作:
    ('after',   '元の行', ['新しい行', ...])   元の行のすぐ後ろに足す
    ('before',  '元の行', [...])                 すぐ前に足す
    ('replace', '元の行', [...])                 入れ替える
    ('last_cmd', '射精', ['フラッシュ,ピンク'])  その節の最後の「射精」の行を入れ替える
  元の行は字下げを除いた形で、節の中で一つだけ当たること。
"""
import sys, os, re, glob, shutil, zipfile, importlib.util, io

ROOT = 'C:/Users/taku2/Downloads/MOD/'
BAK = ROOT + '_バックアップ/直し前_2026-10-07/'
HERE = os.path.dirname(os.path.abspath(__file__))
BAD = re.compile(r'[,$%&#{}<>]')
ROUTES = {"btl": "戦闘負け", "onani": "オナニー負け", "inochi": "命乞い負け", "onedari": "おねだり負け"}
KEYS = ["m1", "m2", "m3", "e1", "e2", "e3", "boss"]


class Text:
    """keeps newline style, BOM and final newline of a file"""
    def __init__(self, raw):
        self.bom = raw.startswith(b'\xef\xbb\xbf')
        t = raw[3:].decode('utf-8') if self.bom else raw.decode('utf-8')
        self.nl = '\r\n' if '\r\n' in t else '\n'
        self.lines = t.split(self.nl)

    def dump(self):
        b = self.nl.join(self.lines).encode('utf-8')
        return (b'\xef\xbb\xbf' + b) if self.bom else b


def sec_range(lines, name):
    hits = [i for i, l in enumerate(lines) if l.strip() == name]
    if len(hits) != 1:
        return None
    s = hits[0]; e = s + 1
    while e < len(lines) and not lines[e].strip().startswith('@'):
        e += 1
    return s, e


def apply_ops(lines, s, e, ops, indent, where, strict=True):
    misses = []
    for op in ops:
        kind = op[0]
        if kind == 'last_cmd':
            cmd, new = op[1], op[2]
            hits = [i for i in range(s, e) if lines[i].strip() == cmd]
            if not hits:
                if strict: sys.exit('NO CMD %s in %s' % (cmd, where))
                misses.append(cmd); continue
            i = hits[-1]
            ind = lines[i][:len(lines[i]) - len(lines[i].lstrip())]
            lines[i:i + 1] = [ind + x for x in new]
            e += len(new) - 1
            continue
        if kind == 'cmd_after':
            # ('cmd_after', '目印の行', '射精', ['フラッシュ,ピンク'])：目印の行より後で最初の「射精」の行を入れ替える
            anchor, cmd, new = op[1], op[2], op[3]
            hits = [i for i in range(s, e) if lines[i].strip() == anchor.strip()]
            if len(hits) != 1:
                if strict: sys.exit('NOT UNIQUE (%d) in %s: %s' % (len(hits), where, anchor[:60]))
                misses.append(anchor[:40]); continue
            j = next((k for k in range(hits[0] + 1, e) if lines[k].strip() == cmd), None)
            if j is None:
                if strict: sys.exit('NO %s after anchor in %s: %s' % (cmd, where, anchor[:60]))
                misses.append(cmd); continue
            ind = lines[j][:len(lines[j]) - len(lines[j].lstrip())]
            lines[j:j + 1] = [ind + x for x in new]
            e += len(new) - 1
            continue
        old, new = op[1], op[2]
        hits = [i for i in range(s, e) if lines[i].strip() == old.strip()]
        if len(hits) != 1:
            if strict: sys.exit('NOT UNIQUE (%d) in %s: %s' % (len(hits), where, old[:60]))
            misses.append(old[:40]); continue
        i = hits[0]
        ind = lines[i][:len(lines[i]) - len(lines[i].lstrip())] if indent is None else indent
        nl = [ind + x for x in new]
        if kind == 'replace':
            lines[i:i + 1] = nl; e += len(nl) - 1
        elif kind == 'after':
            lines[i + 1:i + 1] = nl; e += len(nl)
        elif kind == 'before':
            lines[i:i] = nl; e += len(nl)
        else:
            sys.exit('BAD OP ' + kind)
    return misses


def body(lines):
    out = []
    for l in lines:
        m = re.match(r'\s*(セリフ|説明),(.*)$', l)
        if m:
            out.append(m.group(2))
    return out


def nchars(lines):
    return sum(len(x.replace('\\n', '')) for x in body(lines))


def sections(lines):
    secs, cur = {}, None
    for l in lines:
        s = l.strip()
        if s.startswith('@'):
            cur = s; secs.setdefault(cur, [])
        elif cur:
            secs[cur].append(l)
    return secs


def reader_from_scen(get_scen, outn):
    out = []
    for k in KEYS:
        for r in ROUTES:
            lines = get_scen(f'{r}_{k}')
            if lines is None:
                return None
            out.append(f"\n==================== {r}_{k}（{ROUTES[r]}） ====================\n")
            who = None
            for l in lines:
                cmd, _, rest = l.partition(",")
                if cmd == "話者":
                    who = "僕" if rest == "相手プレイヤー" else rest.lstrip("%")
                elif cmd == "セリフ":
                    out.append(f"{who}「{rest.replace(chr(92)+'n', '')}」")
                elif cmd == "説明":
                    out.append(rest.replace("\\n", "\n"))
                elif cmd == "射精":
                    out.append("（射精）")
    return (f"{outn} 敗北シナリオ28本（読む用。ゲームには入れない）\n" + "\n".join(out) + "\n").replace('\n', '\r\n').encode('utf-8')



def render(lines):
    """scen／カードの行を、読む用の行（何行かに分かれる）に直す"""
    out, who = [], None
    for l in lines:
        s = l.strip()
        cmd, _, rest = s.partition(",")
        if cmd == "話者":
            who = "僕" if rest == "相手プレイヤー" else rest.lstrip("%")
        elif cmd == "セリフ":
            out.append(f"{who}「{rest.replace(chr(92)+'n', '')}」")
        elif cmd == "説明":
            out.extend(rest.split(chr(92) + "n"))
        elif s == "射精":
            out.append("（射精）")
    return out


def patch_reader(rlines, old_lines, new_lines):
    """読む用の行に、old→new の本文の違いだけを写す。写せなければ None"""
    import difflib
    old_r, new_r = render(old_lines), render(new_lines)
    if old_r == new_r:
        return rlines
    # 読む用がカードより少し古いことがあるので、見つからない行は飛ばして先へ進む
    pos, k = [], 0
    for x in old_r:
        j = k
        while j < len(rlines) and rlines[j] != x:
            j += 1
        if j < len(rlines):
            pos.append(j); k = j + 1
        else:
            pos.append(None)
    if sum(p is not None for p in pos) < len(pos) * 0.7:
        return None
    out = list(rlines)
    for tag, i1, i2, j1, j2 in reversed(difflib.SequenceMatcher(None, old_r, new_r, autojunk=False).get_opcodes()):
        if tag == 'equal':
            continue
        if tag in ('replace', 'delete'):
            if pos[i1] is None or pos[i2 - 1] is None:
                return None
            out[pos[i1]:pos[i2 - 1] + 1] = new_r[j1:j2]
        else:  # insert
            if i1 > 0 and pos[i1 - 1] is not None:
                at = pos[i1 - 1] + 1
            elif i1 < len(pos) and pos[i1] is not None:
                at = pos[i1]
            else:
                return None
            out[at:at] = new_r[j1:j2]
    return out


def patch_reader_file(rf, src, dry, card_pairs, report):
    """読む用の各本に、カードで直した所だけを写す（書式を問わない）"""
    tx = Text(open(rf, 'rb').read())
    lines = tx.lines
    for key, (old, new) in card_pairs.items():
        res = patch_reader(lines, old, new)
        if res is None:
            report.append('READER miss %s' % key)
            return False
        lines = res
    tx.lines = lines
    if not dry:
        open(src + os.path.basename(rf), 'wb').write(tx.dump())
    report.append('READER patched ' + os.path.basename(rf))
    return True

def main():
    mod = sys.argv[1]
    dry = '--dry' in sys.argv
    src, bak = ROOT + mod + '/', BAK + mod + '/'
    if not os.path.isdir(bak):
        if dry:
            bak = src
        else:
            shutil.copytree(src, bak)
            print('backup made:', bak)
    # patches/<MOD>.py と、分担した patches/<MOD>__*.py をまとめて読む
    P, SCEN_EXTRA, READER_FORCE = {}, {}, False
    files = sorted(glob.glob(os.path.join(HERE, 'patches', mod + '.py')) + glob.glob(os.path.join(HERE, 'patches', mod + '__*.py')))
    if '--part' in sys.argv:   # 分担の確認用：自分の分だけを読む（--dry と一緒に使う）
        files = [os.path.join(HERE, 'patches', mod + '__' + sys.argv[sys.argv.index('--part') + 1] + '.py')]
        assert dry, '--part は --dry と一緒に使う'
    if not files:
        sys.exit('no patches for ' + mod)
    for pf in files:
        spec = importlib.util.spec_from_file_location('p', pf)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.P.items():
            if k in P:
                sys.exit('key in two patch files: ' + k)
            P[k] = v
        SCEN_EXTRA.update(getattr(m, 'SCEN_EXTRA', {}))   # 道具の元だけに入れる直し
        READER_FORCE = READER_FORCE or getattr(m, 'READER_FORCE', False)
    # 調査で「B（カードの方が新しい）」「C（カードに直に）」だったMODは、古い scen や丸ごと zip に触らない
    kind = 'A'
    try:
        import csv
        for r in csv.reader(open(os.path.join(HERE, '..', '全MOD_調査.csv'), encoding='utf-8-sig')):
            if r and r[0] == mod:
                kind = r[4][:1]
    except Exception:
        pass
    report = []

    # ---- cards
    cards = [f for f in glob.glob(bak + '**/Card/*.txt', recursive=True)
             if not re.search(r'画像生成|_控え|diagnostic|旧書式', f.replace('\\', '/'))]
    rel_cards = [os.path.relpath(f, bak).replace('\\', '/') for f in cards]
    if mod == 'N17_Scylla_MOD':
        rel_cards = [c for c in rel_cards if c.startswith('CSV/')]
    done = set()
    card_pairs = {}
    total0 = total1 = 0
    for rel in rel_cards:
        tx = Text(open(bak + rel, 'rb').read())
        before = sections(tx.lines)
        touched = False
        for key, ops in P.items():
            name = '@敗北_' + key
            r = sec_range(tx.lines, name)
            if r is None:
                continue
            apply_ops(tx.lines, r[0], r[1], ops, None, rel + ' ' + name)
            done.add(key); touched = True
        if not touched:
            continue
        after = sections(tx.lines)
        for k2 in after:
            if k2.startswith('@敗北_') and k2[4:] in P:
                card_pairs[k2[4:]] = (before[k2], after[k2])
        for k, v in before.items():
            if not (k.startswith('@敗北_') and k[4:] in P):
                assert after.get(k) == v, 'untouched section changed: ' + k
                continue
            c0, c1 = nchars(v), nchars(after[k])
            total0 += c0; total1 += c1
            if c1 < c0:
                report.append('SHORTER %s %d->%d' % (k, c0, c1))
            for b in body(after[k]):
                if BAD.search(b):
                    report.append('BADCHAR %s %s' % (k, b[:40]))
        t = '\n'.join(tx.lines)
        if t.count('{') != t.count('}'):
            report.append('BRACES ' + rel)
        if not dry:
            open(src + rel, 'wb').write(tx.dump())
    missing = set(P) - done
    if missing:
        sys.exit('sections not found: %s' % sorted(missing))

    # ---- scen (folders and zips)
    new_scen = {}
    scen_dirs = glob.glob(bak + '**/scen', recursive=True) if kind == 'A' else []
    if kind != 'A':
        report.append('SCEN skipped (type %s: card is the source)' % kind)
    for d in scen_dirs:
        if re.search(r'画像生成|_控え', d.replace('\\', '/')):
            continue
        for key, ops in P.items():
            f = os.path.join(d, key + '.txt')
            if not os.path.exists(f):
                continue
            tx = Text(open(f, 'rb').read())
            miss = apply_ops(tx.lines, 0, len(tx.lines), ops + SCEN_EXTRA.get(key, []), '', f, strict=False)
            if miss:
                report.append('SCEN MISS %s %s' % (key, miss))
            rel = os.path.relpath(f, bak).replace('\\', '/')
            new_scen[rel] = tx.lines
            if not dry:
                open(src + rel, 'wb').write(tx.dump())
    for zp in (glob.glob(bak + '*.zip') + glob.glob(bak + 'tools/*.zip')) if kind == 'A' else []:
        relz = os.path.relpath(zp, bak).replace('\\', '/')
        if re.match(r'N\d+_.*_MOD(_v4)?\.zip$', os.path.basename(zp)):
            continue  # whole-MOD snapshot zips are old copies: leave them
        try:
            zi = zipfile.ZipFile(zp)
        except Exception:
            continue
        names = zi.namelist()
        hits = {n: re.search(r'(?:^|/)scen/(\w+)\.txt$', n).group(1) for n in names if re.search(r'(?:^|/)scen/(\w+)\.txt$', n)}
        hits = {n: k for n, k in hits.items() if k in P}
        if not hits:
            continue
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zo:
            for info in zi.infolist():
                data = zi.read(info.filename)
                if info.filename in hits:
                    tx = Text(data)
                    k = hits[info.filename]
                    miss = apply_ops(tx.lines, 0, len(tx.lines), P[k] + SCEN_EXTRA.get(k, []), '', relz + ':' + info.filename, strict=False)
                    if miss:
                        report.append('ZIP SCEN MISS %s %s' % (hits[info.filename], miss))
                    new_scen[relz + ':' + info.filename] = tx.lines
                    data = tx.dump()
                ni = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                ni.compress_type = zipfile.ZIP_DEFLATED; ni.external_attr = info.external_attr
                zo.writestr(ni, data)
        if not dry:
            open(src + relz, 'wb').write(buf.getvalue())

    # ---- reading copy (only when the old one can be reproduced exactly)
    readers = sorted(set(f for f in glob.glob(bak + '*読む用*.txt') + glob.glob(bak + '*読む用*.md') + glob.glob(bak + '*シナリオ集*.md')))
    if readers and new_scen:
        def getter(table, use_new):
            def g(key):
                for path, lines in table.items():
                    if path.endswith('scen/' + key + '.txt'):
                        return lines
                return None
            return g
        old_table = {}
        for path in new_scen:
            if ':' in path:
                zrel, n = path.split(':', 1)
                old_table[path] = Text(zipfile.ZipFile(bak + zrel).read(n)).lines
            else:
                old_table[path] = Text(open(bak + path, 'rb').read()).lines
        for rf in readers:
            cur = open(rf, 'rb').read()
            old = reader_from_scen(getter(old_table, False), mod)
            if old is not None and (old == cur or READER_FORCE):
                new = reader_from_scen(getter(new_scen, True), mod)
                if not dry:
                    open(src + os.path.basename(rf), 'wb').write(new)
                report.append('READER rebuilt ' + os.path.basename(rf))
            else:
                ok = patch_reader_file(rf, src, dry, card_pairs, report)
                if not ok:
                    report.append('READER not reproducible (left as is) ' + os.path.basename(rf))
    elif readers:
        for rf in readers:
            if not patch_reader_file(rf, src, dry, card_pairs, report):
                report.append('READER could not be patched (left as is) ' + os.path.basename(rf))

    print('%s %s scenes=%d chars %d->%d' % ('DRY' if dry else 'DONE', mod, len(done), total0, total1))
    for r in report:
        print('  ' + r)


if __name__ == '__main__':
    main()
