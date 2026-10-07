@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
%PY% 一覧画像を作る.py "%USERPROFILE%\Downloads\ComfyUI_windows_portable\ComfyUI\output\確認3_直し2"
echo.
echo できた一覧は output の 確認3_直し2 の中の _一覧 フォルダにあります。
pause
