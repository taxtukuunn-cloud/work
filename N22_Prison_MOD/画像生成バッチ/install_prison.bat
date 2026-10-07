@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_prison.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Prison" mkdir "%~1\Prison"
copy /Y "%~dp0output\Prison\*.png" "%~1\Prison\" >nul
echo Copied to %~1\Prison
dir /b "%~1\Prison" | find /c ".png"
pause
