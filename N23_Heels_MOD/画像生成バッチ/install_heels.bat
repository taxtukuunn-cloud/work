@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_heels.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Heels" mkdir "%~1\Heels"
copy /Y "%~dp0output\Heels\*.png" "%~1\Heels\" >nul
echo Copied to %~1\Heels
dir /b "%~1\Heels" | find /c ".png"
pause
