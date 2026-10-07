@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_twins.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Twins" mkdir "%~1\Twins"
copy /Y "%~dp0output\Twins\*.png" "%~1\Twins\" >nul
echo Copied to %~1\Twins
dir /b "%~1\Twins" | find /c ".png"
pause
