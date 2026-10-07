@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo MOD の本文の長さの記述を書き換えます（先に控えを取ります）
%PY% "サイズの記述を直す.py"
echo.
pause
