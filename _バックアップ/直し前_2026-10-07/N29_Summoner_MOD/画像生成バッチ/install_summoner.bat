@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_summoner.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Summoner" mkdir "%~1\Summoner"
copy /Y "%~dp0output\Summoner\*.png" "%~1\Summoner\" >nul
echo Copied to %~1\Summoner
dir /b "%~1\Summoner" | find /c ".png"
pause
