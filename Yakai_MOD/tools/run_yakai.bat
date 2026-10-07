@echo off
chcp 65001 >nul
set "PY=C:\Users\taku2\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist "%PY%" (
  echo [エラー] Pythonが見つかりません: %PY%
  echo このbatをメモ帳で開き、3行目の PY= を ComfyUI の python_embeded\python.exe の場所に直してください。
  pause
  exit /b 1
)
"%PY%" "%~dp0run_yakai_batch.py" %*
pause
