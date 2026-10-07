@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo MOD の本文から長さの記述を探します（書き換えはしません）
%PY% "サイズの記述を探す.py"
echo.
pause
