@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
echo Rerolling 22 images x 2 candidates...
%PY% comfy_batch.py Lamia_e3 --random --batch 2
%PY% comfy_batch.py Lamia_atk_m1 --random --batch 2
%PY% comfy_batch.py Lamia_atk_m2 --random --batch 2
%PY% comfy_batch.py Lamia_atk_m3 --random --batch 2
%PY% comfy_batch.py Lamia_atk_e2 --random --batch 2
%PY% comfy_batch.py Lamia_onanie_m --random --batch 2
%PY% comfy_batch.py Lamia_onanie_e1 --random --batch 2
%PY% comfy_batch.py Lamia_onanie_e2 --random --batch 2
%PY% comfy_batch.py Lamia_onanie_e3 --random --batch 2
%PY% comfy_batch.py Lamia_onanie_boss --random --batch 2
%PY% comfy_batch.py Lamia_lose_btl_m2 --random --batch 2
%PY% comfy_batch.py Lamia_lose_inochi_m2 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onedari_m2 --random --batch 2
%PY% comfy_batch.py Lamia_lose_btl_m3 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onani_m3 --random --batch 2
%PY% comfy_batch.py Lamia_lose_inochi_m3 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onedari_m3 --random --batch 2
%PY% comfy_batch.py Lamia_lose_btl_e1 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onedari_e1 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onani_e2 --random --batch 2
%PY% comfy_batch.py Lamia_lose_inochi_e2 --random --batch 2
%PY% comfy_batch.py Lamia_lose_onedari_boss --random --batch 2
echo DONE
pause
