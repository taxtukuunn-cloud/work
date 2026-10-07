@echo off

if "%~1"=="" (
  echo Usage: install_lamia.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Lamia" mkdir "%~1\Lamia"
copy /Y "%~dp0output\Lamia\*.png" "%~1\Lamia\" >nul
echo Copied to %~1\Lamia
dir /b "%~1\Lamia" | find /c ".png"
pause
