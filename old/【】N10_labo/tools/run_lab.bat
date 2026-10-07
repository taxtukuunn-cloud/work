@echo off
chcp 65001 >nul
cd /d "%~dp0"
call "%~dp0find_python.bat"
if not defined PY (pause & exit /b 1)
"%PY%" run_lab_batch.py %*
pause
