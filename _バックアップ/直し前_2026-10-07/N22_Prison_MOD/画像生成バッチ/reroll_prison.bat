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
for %%K in (Prison_atk_e1 Prison_lose_inochi_e1 Prison_lose_onedari_e1 Prison_lose_onani_m3 Prison_onanie_e1) do (
  %PY% comfy_batch.py %%K --random --batch 4
)
echo done > output\Prison\_candidates\_reroll1_done.txt
