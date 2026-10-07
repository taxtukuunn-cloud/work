@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_kitsune.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Kitsune" mkdir "%~1\Kitsune"
copy /Y "%~dp0output\Kitsune\*.png" "%~1\Kitsune\" >nul
echo Copied to %~1\Kitsune
dir /b "%~1\Kitsune" | find /c ".png"
pause
