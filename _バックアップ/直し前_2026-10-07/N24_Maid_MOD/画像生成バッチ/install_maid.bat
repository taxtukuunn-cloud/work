@echo off
if "%~1"=="" (
  echo 使い方: install_maid.bat "D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Maid" mkdir "%~1\Maid"
copy /Y "%~dp0output\Maid\*.png" "%~1\Maid\" >nul
echo %~1\Maid にコピーしました
dir /b "%~1\Maid" | find /c ".png"
pause
