"""取りまとめ役用：本番を入れて、進捗.csv に1行足す。
使い方: python finish_mod.py <MOD> [<MOD> ...]"""
import sys, subprocess, re, os, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
for mod in sys.argv[1:]:
    r = subprocess.run([sys.executable, os.path.join(HERE, 'apply_mod.py'), mod], capture_output=True, text=True, encoding='utf-8',
                       env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = r.stdout + r.stderr
    print(out.strip())
    m = re.search(r'^DONE \S+ scenes=(\d+) chars (\d+)->(\d+)', out, re.M)
    if not m:
        print('!! FAILED', mod)
        continue
    notes = []
    if 'READER rebuilt' in out or 'READER patched' in out:
        notes.append('読む用も')
    if 'not reproducible' in out or 'could not be patched' in out:
        notes.append('読む用は写せず')
    if 'SCEN MISS' in out:
        notes.append('scen一部写せず')
    line = '%s,第4段 %s本%s,済,%s,%s,%s\r\n' % (mod, m.group(1), ('(' + '・'.join(notes) + ')') if notes else '',
                                          m.group(2), m.group(3), datetime.date.today().isoformat())
    with open(os.path.join(HERE, '..', '進捗.csv'), 'ab') as f:
        f.write(line.encode('utf-8'))
    print('logged:', line.strip())
