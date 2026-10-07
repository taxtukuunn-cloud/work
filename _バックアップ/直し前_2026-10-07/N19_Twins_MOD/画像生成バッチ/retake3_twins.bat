@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
%PY% comfy_batch.py Twins_onanie_master --random --batch 3
echo 撮り直し完了
pause
