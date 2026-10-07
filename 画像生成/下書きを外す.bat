@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo 撮った絵の下書き一覧.csv で ○ を付けた絵の下書きを、これから使わないようにします（ファイルは消しません）
%PY% 下書きを外す.py
echo.
pause
