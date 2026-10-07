@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY=python
where python >nul 2>nul || set PY=py
if exist "%COMFY%\python_embeded\python.exe" set PY="%COMFY%\python_embeded\python.exe"
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if not errorlevel 1 goto ready
echo Starting ComfyUI...
start "ComfyUI" /D "%COMFY%" cmd /c run_nvidia_gpu.bat
:wait
timeout /t 10 /nobreak >nul
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 goto wait
:ready
echo ComfyUI OK. Generating 52 images...
%PY% comfy_batch.py all --skip-existing
pause
