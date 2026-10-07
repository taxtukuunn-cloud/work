@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo 撮った絵（output\キャラLoRA確認）がどの下書きで撮られたかを一覧にします（絵は変更しません）
%PY% 撮った絵の下書き一覧.py
echo.
echo 撮った絵の下書き一覧.csv を開くか、Claude に送ってください。
pause
