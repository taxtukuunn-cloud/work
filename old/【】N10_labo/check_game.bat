@echo off
chcp 65001 >nul
rem ゲームに正しく入っているかを点検します（何も書き換えません）
set GAME=%~1
if "%GAME%"=="" set GAME=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル
call "%~dp0tools\find_python.bat"
if not defined PY (
  where python >nul 2>nul && set PY=python
)
if not defined PY (pause & exit /b 1)
"%PY%" "%~dp0tools\check_game.py" "%GAME%"
pause
