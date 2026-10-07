#!/usr/bin/env python3
"""Rosetta MOD 画像チェッカー

ゲームのフォルダを指定すると、Card/Rosetta_*.txt が使っている画像が
Picture/Rosetta/ に「正しい名前で」あるかを調べます。

使い方:
  python check_images.py "C:\\...\\ゲームのフォルダ"
  （check_images.bat にゲームのフォルダをドラッグ&ドロップでもOK）
"""
import glob, os, re, sys

def main():
    if len(sys.argv) < 2:
        sys.exit("ゲームのフォルダを指定してください。（例: python check_images.py \"C:\\\\Games\\\\SuccubusDuel\"）")
    game = sys.argv[1].strip('"')
    card_dir = os.path.join(game, "Card")
    pic_dir = os.path.join(game, "Picture", "Rosetta")
    if not os.path.isdir(card_dir):
        sys.exit(f"Card フォルダが見つかりません: {card_dir}\nゲームの実行ファイル（SuccubusDuel.exe）があるフォルダを指定してください。")
    cards = sorted(glob.glob(os.path.join(card_dir, "Rosetta_*.txt")))
    print(f"Card/Rosetta_*.txt: {len(cards)} ファイル（期待値 10）")
    if len(cards) < 10:
        print("  ⚠ 足りません。zip の Card フォルダの中身を全部 Card/ に入れてください。")
    need = {}
    for c in cards:
        t = open(c, encoding="utf-8", errors="replace").read()
        for name in re.findall(r"#Rosetta/([A-Za-z0-9_]+\.png)", t):
            need.setdefault(name, set()).add(os.path.basename(c))
    if not os.path.isdir(pic_dir):
        print(f"\n✖ Picture/Rosetta フォルダがありません: {pic_dir}")
        print("  画像は Picture の中に「Rosetta」フォルダを作って入れてください。")
        return
    have = {f: f for f in os.listdir(pic_dir)}
    have_lower = {f.lower(): f for f in have}
    ok, missing, case = [], [], []
    for name in sorted(need):
        if name in have: ok.append(name)
        elif name.lower() in have_lower: case.append((name, have_lower[name.lower()]))
        else: missing.append(name)
    print(f"\n必要な画像: {len(need)} 枚  →  OK {len(ok)} / 名前違い {len(case)} / 不足 {len(missing)}")
    for n in ok: print(f"  ✔ {n}")
    for want, got in case: print(f"  ⚠ 名前が違います: 「{got}」→「{want}」に変更してください（大文字小文字・_ も一致させる）")
    for n in missing: print(f"  ✖ ありません: {n}   （使うカード: {', '.join(sorted(need[n]))}）")
    extra = [f for f in have if f not in need and f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    if extra:
        print("\nスクリプトが使っていない画像（名前違いの可能性）:")
        for f in sorted(extra): print("  ・", f)
    bad = [f for f in have if re.search(r"_c\d+\.png$", f)]
    if bad:
        print("\n⚠ 候補用の名前（_c1 など）が付いたままです。ゲームは読み込みません。_cN を外してください:")
        for f in sorted(bad): print("  ・", f)
    if not (case or missing or bad):
        print("\n✔ 画像はすべて揃っています。")

if __name__ == "__main__":
    main()
