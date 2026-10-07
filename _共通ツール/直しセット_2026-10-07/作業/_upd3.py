p='apply_mod.py'; t=open(p,encoding='utf-8').read()
helper = '''

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
            out.extend(rest.split("\\n"))
        elif s == "射精":
            out.append("（射精）")
    return out


def patch_reader(rlines, old_lines, new_lines):
    """読む用の行に、old→new の本文の違いだけを写す。写せなければ None"""
    import difflib
    old_r, new_r = render(old_lines), render(new_lines)
    if old_r == new_r:
        return rlines
    pos, k = [], 0
    for x in old_r:
        while k < len(rlines) and rlines[k] != x:
            k += 1
        if k >= len(rlines):
            return None
        pos.append(k); k += 1
    out = list(rlines)
    for tag, i1, i2, j1, j2 in reversed(difflib.SequenceMatcher(None, old_r, new_r, autojunk=False).get_opcodes()):
        if tag == 'equal':
            continue
        if tag in ('replace', 'delete'):
            out[pos[i1]:pos[i2 - 1] + 1] = new_r[j1:j2]
        else:  # insert
            at = pos[i1 - 1] + 1 if i1 > 0 else pos[0]
            out[at:at] = new_r[j1:j2]
    return out
'''
anchor = "\ndef main():"
assert 'def patch_reader' not in t
t = t.replace(anchor, helper + anchor, 1)
# reader stage: after the reproduce attempt, fall back to patching
old = """            else:
                report.append('READER not reproducible (left as is) ' + os.path.basename(rf))
    elif readers:
        report.append('READER no scen (left as is)')"""
new = """            else:
                ok = patch_reader_file(rf, src, dry, card_pairs, report)
                if not ok:
                    report.append('READER not reproducible (left as is) ' + os.path.basename(rf))
    elif readers:
        for rf in readers:
            if not patch_reader_file(rf, src, dry, card_pairs, report):
                report.append('READER could not be patched (left as is) ' + os.path.basename(rf))"""
assert old in t; t = t.replace(old, new)
# collect card old/new pairs per key during the card stage
old2 = """        after = sections(tx.lines)"""
new2 = """        after = sections(tx.lines)
        for k2 in after:
            if k2.startswith('@敗北_') and k2[4:] in P:
                card_pairs[k2[4:]] = (before[k2], after[k2])"""
assert old2 in t; t = t.replace(old2, new2)
old3 = """    done = set()
    total0 = total1 = 0"""
new3 = """    done = set()
    card_pairs = {}
    total0 = total1 = 0"""
assert old3 in t; t = t.replace(old3, new3)
func = '''

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
'''
t = t.replace(anchor, func + anchor, 1)
open(p, 'w', encoding='utf-8').write(t); print('ok')
