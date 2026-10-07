@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI wo kidou shimasu...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  %PY% wait_comfy.py
)
rem LoRA の効き方を見る試し撮り 4枚（立ち絵・技CG・敗北CG・オナニーCG）。出力は output\Kitsune\
%PY% comfy_batch.py Kitsune_master
%PY% comfy_batch.py Kitsune_atk_m2
%PY% comfy_batch.py Kitsune_lose_btl_e2
%PY% comfy_batch.py Kitsune_onanie_master
%PY% sheet_kitsune.py
echo owari. output\Kitsune_sheet.jpg wo kakunin.
pause
