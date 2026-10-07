import sys
BODY_CMDS = ('セリフ', '説明')
def count(path):
    txt = open(path, 'rb').read().decode('utf-8-sig')
    n = 0
    for line in txt.splitlines():
        s = line.strip()
        for c in BODY_CMDS:
            if s.startswith(c + ','):
                n += len(s[len(c) + 1:].replace('\\n', ''))
    return n
if __name__ == '__main__':
    for p in sys.argv[1:]:
        c = count(p)
        print(f"{p}: {c}字 {'OK' if c >= 5000 else '★不足'}")
