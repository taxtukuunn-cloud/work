@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  元絵候補から採用した画像を 構図下書き元 に入れる
echo  _候補\_採用.csv の「採用」欄に構図名（英小文字・数字・_）を書いた画像が対象
echo  1) ウィンドウの枠・タイトルバー・周りの黒い余白を自動で切り落とす
echo  2) 構図下書き元\構図名.png（2枚目から 構図名_2.png …）に入れる（_候補 の画像は残る）
echo  3) 奥行き下書き → 人物の範囲 を作る
echo  4) 構図下書き\_取り込み確認_日時.jpg で確認
echo  model.json に無い構図名でも入れます（登録はしません。最後に一覧を表示）
echo  することだけ見るなら: 元絵を採用する.bat --dry-run
echo ============================================
%PY% adopt_ref.py %*
echo.
pause
