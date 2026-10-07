@echo off
chcp 65001 >nul
cd /d "%~dp0"
rem 2026-09-26 成人の体つき修正のあとで51枚を撮り直す。
rem 今の output\Prison は output\Prison_旧_2026-09-24 に名前を変えて残す（消さない）。
if exist "output\Prison_旧_2026-09-24" (
  echo output\Prison_旧_2026-09-24 はすでにあります。続きから生成します。
) else (
  if exist "output\Prison" ren "output\Prison" "Prison_旧_2026-09-24"
)
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  echo 起動を待っています（最大5分）...
  %PY% wait_comfy.py
)
%PY% comfy_batch.py all --skip-existing
pause
