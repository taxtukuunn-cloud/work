@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo LoRA ‚ª¡‚Ìƒ‚ƒfƒ‹‚É‡‚¤‚©‚ğ’²‚×‚Ü‚·i”•bj
%PY% "LoRA‚Ìí—Ş‚ğ’²‚×‚é.py"
echo.
pause
