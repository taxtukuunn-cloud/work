@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% comfy_batch.py --pick Heels_lose_onani_e2 3
%PY% comfy_batch.py --pick Heels_lose_onedari_e2 2
echo 完了
