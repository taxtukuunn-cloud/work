@echo off
REM Usage: run_mod.bat <MOD_CODE> [key|all] [--random|--seed N|--batch 1|--no-rembg|--list-models|--list-mods|--list-keys]
REM Example: run_mod.bat Inmon all
REM Example: run_mod.bat Inmon master --random
REM Example: run_mod.bat Inmon --list-keys
REM Example: run_mod.bat --list-mods

set COMFY_DIR=C:\Users\taku2\Downloads\ComfyUI_windows_portable
set PYTHON=%COMFY_DIR%\python_embeded\python.exe

if not exist "%PYTHON%" (
  echo [ERROR] %PYTHON% not found. Check COMFY_DIR.
  exit /b 1
)

"%PYTHON%" "%~dp0run_mod_batch.py" %*
