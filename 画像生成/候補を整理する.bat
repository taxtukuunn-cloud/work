@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  構図下書き元\_候補 の元絵候補を整理する
echo  1) 番号の無い画像に c0001 から番号を付ける（元の名前は残る・_候補一覧.csv に追記）
echo  2) 同じ・ほぼ同じ画像（差分）は1枚を残し、残りを _採用.csv で 見送り にする
echo  3) _採用.csv の「採用」が 見送り の画像を _候補\_見送り へ移す（消さない）
echo  4) _候補\_一覧\一覧_01.jpg … を作り直す（20枚ずつ）
echo ============================================
%PY% 候補を整理する.py %*
echo.
pause
