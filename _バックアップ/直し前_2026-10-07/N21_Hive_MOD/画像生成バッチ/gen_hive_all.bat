@echo off
chcp 65001 >nul
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
rem ComfyUI が起動していなければ起動する
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  echo 起動を待っています（最大5分）...
  %PY% wait_comfy.py
)
%PY% comfy_batch.py all --skip-existing
echo.
echo 51枚の生成が終わりました。output\Hive を確認してください。
pause
