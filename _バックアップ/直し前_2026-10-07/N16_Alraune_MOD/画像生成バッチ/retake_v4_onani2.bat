@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
for %%K in (Alraune_onanie_m Alraune_onanie_e2 Alraune_lose_onani_m1) do (
  %PY% comfy_batch.py %%K --random --batch 3
)
echo Done.
pause
