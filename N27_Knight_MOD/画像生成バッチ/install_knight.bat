@echo off
chcp 65001 >nul
set DEST=%~1
if "%DEST%"=="" set DEST=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture
if not exist "%DEST%\Knight" mkdir "%DEST%\Knight"
copy /Y "%~dp0output\Knight\*.png" "%DEST%\Knight\" >nul
echo Copied to %DEST%\Knight
dir /b "%DEST%\Knight" | find /c ".png"
pause
