# -*- coding: utf-8 -*-
"""画像の配置チェック＆自動配置
使い方: install_images.bat  （Pictureフォルダと、生成画像を置いたフォルダを聞かれる）
- 必要な画像が Picture\\Yakai\\ に正しい名前であるか確認する
- 見つからないものは、Pictureフォルダ以下・tools\\candidates・指定した追加フォルダを再帰的に探し、
  名前が NAME.png または NAME_シード_番号.png のものを Picture\\Yakai\\NAME.png としてコピーする
"""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = (".png", ".jpg", ".jpeg", ".webp")

def scan(dirs):
    idx = {}
    for d in dirs:
        if not d or not os.path.isdir(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                stem, ext = os.path.splitext(f)
                if ext.lower() in EXT:
                    idx.setdefault(stem.lower(), []).append(os.path.join(root, f))
    return idx

def main():
    args = [a.strip('"') for a in sys.argv[1:]]
    if not args:
        print(__doc__)
        return
    pic = args[0]
    if not os.path.isdir(pic):
        print("Pictureフォルダが見つかりません:", pic)
        print("（ゲームの Save フォルダと同じ階層にある Picture フォルダを指定）")
        return
    extra = args[1:]
    dest = os.path.join(pic, "Yakai")
    os.makedirs(dest, exist_ok=True)
    names = [p["name"] for p in json.load(open(os.path.join(HERE, "Yakai_prompts.json"), encoding="utf-8"))]
    idx = scan([pic, os.path.join(HERE, "candidates"), HERE] + extra)
    ok = fixed = missing = 0
    for n in names:
        target = os.path.join(dest, n + ".png")
        if os.path.exists(target):
            ok += 1
            continue
        pat = re.compile(r"^" + re.escape(n.lower()) + r"(_\d+_\d+)?$")
        found = sorted(p for stem, ps in idx.items() if pat.match(stem) for p in ps)
        if found:
            src = found[0]
            if src.lower().endswith(".png"):
                shutil.copy(src, target)
            else:
                print("注意: png以外です。pngに変換してください:", src)
                continue
            print("配置:", n + ".png", "<-", src)
            fixed += 1
        else:
            print("見つからない:", n + ".png")
            missing += 1
    print(f"\n正常 {ok} / 探して配置 {fixed} / 見つからない {missing}")
    print("配置先:", dest)

if __name__ == "__main__":
    main()
