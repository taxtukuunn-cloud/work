@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
set /p N=一覧にする キャラLoRA確認 の番号を入れてください（例: 3）: 
%PY% 一覧画像を作る.py "%USERPROFILE%\Downloads\ComfyUI_windows_portable\ComfyUI\output\キャラLoRA確認%N%"
echo.
echo できた一覧は output の キャラLoRA確認%N% の中の _一覧 フォルダにあります。
pause
