@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
set /p MOD="MODコード（例 Host）: "
%PY% collect.py %MOD%
pause
