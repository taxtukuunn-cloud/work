src=open('patches/N119_Venus_MOD.py',encoding='utf-8').read()
def block(key):
    i=src.index("P['%s'] = ["%key); j=src.index("\n]\n",i)+3
    return src[i:j]
ci=src.index('DRILL = ['); cj=src.index("P['btl_boss']")
ex = "# N119 見本の抜粋（全体は patches/N119_Venus_MOD.py）\n# レイディアス m2（指で前立腺・踵）と、アテナ boss（分身のペニバン）の btl\n\n"
ex += "P = {}\n" + block('btl_m2') + "\n" + src[ci:cj] + block('btl_boss') + "\n"
ex += "# 最後の絶頂の「射精」行（全本に付ける）\nfor _k in P:\n    P[_k].append(('last_cmd', '射精', ['フラッシュ,ピンク']))\n"
open('見本_抜粋.py','w',encoding='utf-8').write(ex)
print(len(ex))
h='作業の手引き.md'; s=open(h,encoding='utf-8').read()
a=s.index('## 0. 先に読むもの'); b=s.index('## 1. 絶対に守ること')
s=s[:a]+r"""## 0. 先に読むもの（これだけでよい。大きな資料を全部読み直さない）
1. この手引き（決まりは2章にまとめてある）。
2. 見本：`見本_抜粋.py`（N119 の直し方・量・言い回しの手本。全体を見たい時だけ `patches\N119_Venus_MOD.py`）。
3. そのMODの設計書：tools.zip の中の `brief.md`、MODフォルダの `tools\brief.md`・`brief.md`・設計メモ・執筆ガイド・README のどれか。**口調、一人称、呼び方、部位の呼び方の表、場所、小道具はこれに従う。** 長ければ、登場人物と呼び方の表、技の表だけでよい。
   zip の中は `python -c "import zipfile;print(zipfile.ZipFile(r'<zip>').read('tools/brief.md').decode('utf-8'))"` で読める（書き換えない）。
4. 技の細かい書き方で迷った時だけ、`..\資料\claude_技の解説と構図とシチュ_2026-10-07.md` のその技の項を読む。
5. dump は自分専用の場所に出す：`python dump.py <MOD> <鍵...>` の出力をそのまま読むか、`%TEMP%` などへ保存する（`dump\` フォルダはもう一人と上書きし合う）。

"""+s[b:]
open(h,'w',encoding='utf-8').write(s); print('ok')
