@echo off
chcp 65001 >nul
set DEST=%~1
if "%DEST%"=="" set DEST=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル\Picture
if not exist "%DEST%\Hive" mkdir "%DEST%\Hive"
copy /Y "%~dp0..\Picture\Hive\*.png" "%DEST%\Hive\" >nul
echo Copied to %DEST%\Hive
dir /b "%DEST%\Hive" | find /c ".png"
pause
