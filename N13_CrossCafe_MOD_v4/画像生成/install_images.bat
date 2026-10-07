@echo off
REM Usage: install_images.bat <MOD_CODE> "<game>\Picture" [--overwrite]
REM Example: install_images.bat Circle "D:\Games\SuccubusDuel\Picture"
set COMFY_DIR=C:\Users\taku2\Downloads\ComfyUI_windows_portable
set PYTHON=%COMFY_DIR%\python_embeded\python.exe
if not exist "%PYTHON%" set PYTHON=python
"%PYTHON%" "%~dp0install_images.py" %*
pause
