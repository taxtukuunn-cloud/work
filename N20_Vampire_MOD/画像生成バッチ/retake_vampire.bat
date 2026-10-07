@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% comfy_batch.py Vampire_atk_boss --random --batch 3
%PY% comfy_batch.py Vampire_atk_e2 --random --batch 3
%PY% comfy_batch.py Vampire_atk_m2 --random --batch 3
%PY% comfy_batch.py Vampire_lose_btl_boss --random --batch 3
%PY% comfy_batch.py Vampire_lose_btl_e2 --random --batch 3
%PY% comfy_batch.py Vampire_lose_btl_m2 --random --batch 3
%PY% comfy_batch.py Vampire_lose_inochi_boss --random --batch 3
%PY% comfy_batch.py Vampire_lose_onani_m1 --random --batch 3
%PY% comfy_batch.py Vampire_lose_onani_m3 --random --batch 3
%PY% comfy_batch.py Vampire_lose_onedari_e2 --random --batch 3
%PY% comfy_batch.py Vampire_lose_onedari_m3 --random --batch 3
echo 撮り直し完了（output\Vampire\_candidates を確認）
pause
