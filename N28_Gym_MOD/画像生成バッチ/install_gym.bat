@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_gym.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Gym" mkdir "%~1\Gym"
copy /Y "%~dp0output\Gym\*.png" "%~1\Gym\" >nul
echo Copied to %~1\Gym
dir /b "%~1\Gym" | find /c ".png"
pause
