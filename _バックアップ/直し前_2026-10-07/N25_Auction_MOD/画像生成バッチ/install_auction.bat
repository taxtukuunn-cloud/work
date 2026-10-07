@echo off
chcp 65001 >nul
if "%~1"=="" (
  echo Usage: install_auction.bat "C:\...\SuccubusDuel\Picture"
  pause
  exit /b 1
)
if not exist "%~1\Auction" mkdir "%~1\Auction"
copy /Y "%~dp0output\Auction\*.png" "%~1\Auction\" >nul
echo Copied to %~1\Auction
dir /b "%~1\Auction" | find /c ".png"
pause
