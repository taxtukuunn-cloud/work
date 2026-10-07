@echo off
chcp 65001 >nul
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
rem 強さを変えるときは次の行を  set LS=--lora-strength 0.5  のように書き換える（空ならlora_settings.jsonの値＝0.6）
set LS=
call backup_before_lora_vampire.bat
if not exist "output\Vampire_beforeLoRA\Vampire_master.png" (
  echo 控えが取れていないので中止します。
  pause
  exit /b
)
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  %PY% wait_comfy.py
)
rem 全51枚をLoRAありで撮り直す（output\Vampire の同名画像を上書き。元は Vampire_beforeLoRA にある）
%PY% comfy_batch.py all %LS%
echo.
echo 51枚の撮り直しが終わりました。崩れた画像は run_vampire.bat ^<キー^> --random --batch 3 で候補を出して --pick で選び直し。
pause
