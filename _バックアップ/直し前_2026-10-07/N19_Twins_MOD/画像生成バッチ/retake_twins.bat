@echo off
chcp 65001 >nul
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  %PY% wait_comfy.py
)
rem v4（技の変更・得意技に合わせたオナニー）と崩れていた画像の撮り直し 23枚
%PY% comfy_batch.py Twins_atk_m3 --random
%PY% comfy_batch.py Twins_atk_e3 --random
%PY% comfy_batch.py Twins_lose_btl_m2 --random
%PY% comfy_batch.py Twins_lose_inochi_m1 --random
%PY% comfy_batch.py Twins_lose_onedari_m1 --random
%PY% comfy_batch.py Twins_lose_inochi_m2 --random
%PY% comfy_batch.py Twins_lose_onedari_m2 --random
%PY% comfy_batch.py Twins_lose_btl_m3 --random
%PY% comfy_batch.py Twins_lose_inochi_m3 --random
%PY% comfy_batch.py Twins_lose_onedari_m3 --random
%PY% comfy_batch.py Twins_lose_onani_m1 --random
%PY% comfy_batch.py Twins_lose_onani_m2 --random
%PY% comfy_batch.py Twins_lose_onani_m3 --random
%PY% comfy_batch.py Twins_lose_onani_e1 --random
%PY% comfy_batch.py Twins_lose_onani_e2 --random
%PY% comfy_batch.py Twins_lose_onani_e3 --random
%PY% comfy_batch.py Twins_lose_onani_boss --random
%PY% comfy_batch.py Twins_lose_inochi_e2 --random
%PY% comfy_batch.py Twins_onanie_master --random
%PY% comfy_batch.py Twins_onanie_e1 --random
%PY% comfy_batch.py Twins_onanie_e2 --random
%PY% comfy_batch.py Twins_onanie_e3 --random
%PY% comfy_batch.py Twins_onanie_boss --random
echo 撮り直し完了
pause
