@echo off
cd /d "%~dp0"
set "PY=C:\Users\taku2\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist "%PY%" goto nopy
"%PY%" make_frames.py make
if errorlevel 1 goto end
if exist "out\確認用_範囲.png" start "" "out\確認用_範囲.png"
if exist "out\確認用_往復.gif" start "" "out\確認用_往復.gif"
:end
pause
exit /b 0
:nopy
echo ComfyUI の Python が見つかりません。
echo %PY%
pause
exit /b 1
