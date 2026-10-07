@echo off
chcp 65001 >nul
rem 使い方: install_lab.bat "D:\Game\Picture"
cd /d "%~dp0"
if "%~1"=="" (
  echo ゲームの Picture フォルダを指定してください。例: install_lab.bat "D:\Game\Picture"
  pause
  exit /b 1
)
call "%~dp0find_python.bat"
if not defined PY (pause & exit /b 1)
"%PY%" run_lab_batch.py all --install "%~1"
pause
