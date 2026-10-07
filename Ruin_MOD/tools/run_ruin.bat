@echo off
chcp 65001 >nul
setlocal
set COMFY=C:\Users\taku2\Downloads\ComfyUI_windows_portable
"%COMFY%\python_embeded\python.exe" "%~dp0run_ruin_batch.py" %*
echo.
pause
