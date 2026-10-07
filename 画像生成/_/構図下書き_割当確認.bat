@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  構図の下書き（3D の奥行き・ControlNet）の割当確認（画像は作りません）
echo  結果: 構図LoRA_割当.csv の「下書き」列、画面に下書きごとの件数
echo ============================================
%PY% gen.py all --pose-report
echo.
pause
