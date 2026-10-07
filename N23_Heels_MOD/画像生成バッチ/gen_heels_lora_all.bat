@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
call backup_heels.bat
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  echo 起動を待っています（最大5分）...
  %PY% wait_comfy.py
)
rem 52枚をLoRAありで撮り直し、output\Heels の同名ファイルを上書きする（元の画像は output\Heels_LoRA前）
%PY% comfy_batch.py all %*
pause
