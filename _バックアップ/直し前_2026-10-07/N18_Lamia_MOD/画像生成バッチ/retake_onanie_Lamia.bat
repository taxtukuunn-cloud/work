@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
echo Retaking 4 onanie images x 3 candidates...
%PY% comfy_batch.py Lamia_onanie_m --random --batch 3
%PY% comfy_batch.py Lamia_onanie_e1 --random --batch 3
%PY% comfy_batch.py Lamia_onanie_e2 --random --batch 3
%PY% comfy_batch.py Lamia_onanie_e3 --random --batch 3
echo DONE
pause
