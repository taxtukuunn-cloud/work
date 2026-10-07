@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
rem 候補から採用する画像を決めて output\Heels\ に上書き
%PY% comfy_batch.py --pick Heels_atk_m1 3
%PY% comfy_batch.py --pick Heels_atk_m2 1
%PY% comfy_batch.py --pick Heels_atk_m3 1
%PY% comfy_batch.py --pick Heels_lose_btl_m1 3
%PY% comfy_batch.py --pick Heels_lose_onani_m1 2
%PY% comfy_batch.py --pick Heels_lose_inochi_m1 1
%PY% comfy_batch.py --pick Heels_lose_btl_m2 2
%PY% comfy_batch.py --pick Heels_lose_onani_m2 2
%PY% comfy_batch.py --pick Heels_lose_onedari_m2 1
%PY% comfy_batch.py --pick Heels_lose_btl_m3 3
%PY% comfy_batch.py --pick Heels_lose_onani_m3 3
%PY% comfy_batch.py --pick Heels_lose_inochi_m3 1
%PY% comfy_batch.py --pick Heels_lose_onedari_m3 1
%PY% comfy_batch.py --pick Heels_lose_btl_e1 2
%PY% comfy_batch.py --pick Heels_lose_onani_e1 1
%PY% comfy_batch.py --pick Heels_lose_inochi_e1 1
%PY% comfy_batch.py --pick Heels_lose_btl_e2 2
%PY% comfy_batch.py --pick Heels_lose_inochi_e2 2
rem 構図を直した2枚をもう一度3候補ずつ
%PY% comfy_batch.py Heels_lose_onani_e2 --random --batch 3
%PY% comfy_batch.py Heels_lose_onedari_e2 --random --batch 3
echo 完了
