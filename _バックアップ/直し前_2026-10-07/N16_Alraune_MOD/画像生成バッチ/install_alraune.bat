@echo off

if "%~1"=="" (
  echo Usage: install_alraune.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Alraune" mkdir "%~1\Alraune"
copy /Y "%~dp0output\Alraune\*.png" "%~1\Alraune\" >nul
echo Copied to %~1\Alraune
dir /b "%~1\Alraune" | find /c ".png"
pause
