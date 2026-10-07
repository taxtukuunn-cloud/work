@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
%PY% comfy_batch.py Alraune_lose_inochi_e2 --random --batch 3
echo Done.
pause
