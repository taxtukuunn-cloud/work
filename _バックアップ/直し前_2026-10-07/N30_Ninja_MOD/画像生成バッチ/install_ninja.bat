@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_ninja.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Ninja" mkdir "%~1\Ninja"
copy /Y "%~dp0output\Ninja\*.png" "%~1\Ninja\" >nul
echo Copied to %~1\Ninja
dir /b "%~1\Ninja" | find /c ".png"
pause
