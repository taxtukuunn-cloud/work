@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo 撮った絵を小さく並べた一覧画像を作ります（絵は変更しません）
%PY% 一覧画像を作る.py
echo.
echo できた一覧は output の キャラLoRA確認N の中の _一覧 フォルダにあります。
pause
