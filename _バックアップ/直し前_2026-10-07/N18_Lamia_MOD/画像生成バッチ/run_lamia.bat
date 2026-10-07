@echo off

cd /d "%~dp0"
set PY=python
where python >nul 2>nul || set PY=py
if exist "%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe" set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
%PY% comfy_batch.py %*
pause
