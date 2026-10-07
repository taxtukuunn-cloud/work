p='apply_mod.py'; t=open(p,encoding='utf-8').read()
old="""    files = sorted(glob.glob(os.path.join(HERE, 'patches', mod + '.py')) + glob.glob(os.path.join(HERE, 'patches', mod + '__*.py')))"""
new="""    files = sorted(glob.glob(os.path.join(HERE, 'patches', mod + '.py')) + glob.glob(os.path.join(HERE, 'patches', mod + '__*.py')))
    if '--part' in sys.argv:   # 分担の確認用：自分の分だけを読む（--dry と一緒に使う）
        files = [os.path.join(HERE, 'patches', mod + '__' + sys.argv[sys.argv.index('--part') + 1] + '.py')]
        assert dry, '--part は --dry と一緒に使う'"""
if '--part' not in t:
    assert old in t; t=t.replace(old,new); open(p,'w',encoding='utf-8').write(t)
h='作業の手引き.md'; s=open(h,encoding='utf-8').read()
a=s.index('## 4. 手順'); b=s.index('## 5. patches の書き方')
new_h=r"""## 4. 手順（1つのMODを2人で分担する）
- 担当は依頼文に書いてある（例：パート a ＝ m1・m2・m3・e1 の16本、パート b ＝ e2・e3・boss の12本）。**自分の担当の鍵だけ**を書く。
- 自分のファイルは `patches\<MOD>__<パート>.py`（例 `patches\N41_Nekomata_MOD__a.py`）。もう一人のファイルには触らない。
1. `python dump.py <MOD> <鍵> <鍵> ...`（担当の鍵だけ出せる。`dump\<MOD>.txt` にも出る）。
2. 設計書を読み、当たる本と直し方を決める。ぱふぱふの香りは、設計書に香りの指定があればそれ、無ければキャラに合うものを決めて報告に書く。
3. `patches\<MOD>__<パート>.py` を書く（形は下）。
4. `python apply_mod.py <MOD> --dry --part <パート>` で確かめる。NOT UNIQUE・SHORTER・BADCHAR が出たら直す。
5. **本番の書き込み（--dry なし）はしない**。二人分がそろってから、取りまとめ役が行う。
6. 最後に、下の「報告」を返す。

"""
s=s[:a]+new_h+s[b:]; open(h,'w',encoding='utf-8').write(s); print('ok')
