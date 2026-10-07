@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
%PY% 一覧画像を作る.py "%USERPROFILE%\Downloads\ComfyUI_windows_portable\ComfyUI\output\主人公範囲比較_05"
%PY% 一覧画像を作る.py "%USERPROFILE%\Downloads\ComfyUI_windows_portable\ComfyUI\output\主人公範囲比較_08"
echo.
echo できた一覧は output の 主人公範囲比較_05 と _08 の中の _一覧 フォルダにあります。
pause
