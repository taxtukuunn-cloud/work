@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  全MODの絵柄をランダムに割り振り直す（撮影はしません）
echo  ・今の 絵柄割当.csv の割当はすべて上書きされます
echo  ・同じ絵柄が偏らないように振ります
echo  ・本編v2・本編v2強・matureBody・DHIBI は選びません
echo ============================================
if exist 絵柄割当.csv copy /y 絵柄割当.csv 絵柄割当_振り直し前.csv >nul && echo 今の割当を 絵柄割当_振り直し前.csv に残しました
%PY% gen.py all --model wai --random-style all --assign-only
echo.
echo 結果は 絵柄割当.csv を開いて確認してください。
pause
