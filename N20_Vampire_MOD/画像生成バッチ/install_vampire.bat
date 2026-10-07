@echo off
chcp 65001 >nul
set DEST=%~1
if "%DEST%"=="" set DEST=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture
if not exist "%DEST%\Vampire" mkdir "%DEST%\Vampire"
copy /Y "%~dp0output\Vampire\*.png" "%DEST%\Vampire\" >nul
echo Copied to %DEST%\Vampire
dir /b "%DEST%\Vampire" | find /c ".png"
pause
