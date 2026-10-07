@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  選んだ元絵を 構図下書き元 に正しい名前で入れる
echo  ・画像をこの bat にドラッグ＆ドロップ → コピー（元の画像は残る）
echo  ・または 構図下書き元\_入れる に入れてからダブルクリック → 移動
echo  名前は自動（peg_doggy_00003_.png → peg_doggy.png、2枚目から peg_doggy_2.png …）
echo ============================================
%PY% import_pose_ref.py %*
echo.
pause
