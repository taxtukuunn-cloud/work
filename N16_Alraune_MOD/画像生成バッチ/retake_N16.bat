@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
if not exist "output\Alraune\_old" mkdir "output\Alraune\_old"
for %%K in (Alraune_onanie_e2 Alraune_onanie_e3 Alraune_lose_onani_m1 Alraune_lose_onedari_m1 Alraune_lose_btl_m2 Alraune_lose_btl_m3 Alraune_lose_inochi_e2) do (
  copy /Y "output\Alraune\%%K.png" "output\Alraune\_old\%%K.png" >nul
  %PY% comfy_batch.py %%K --random
)
echo Retake done.
pause
