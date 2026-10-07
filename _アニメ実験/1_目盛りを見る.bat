@echo off
cd /d "%~dp0"
set "PY=C:\Users\taku2\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist "%PY%" goto nopy
if "%~1"=="" goto noarg
"%PY%" make_frames.py grid "%~1"
goto done
:noarg
"%PY%" make_frames.py grid
:done
if exist "–Ú·‚è.png" start "" "–Ú·‚è.png"
pause
exit /b 0
:nopy
echo ComfyUI ‚Ì Python ‚ªŒ©‚Â‚©‚è‚Ü‚¹‚ñB
echo %PY%
pause
exit /b 1
