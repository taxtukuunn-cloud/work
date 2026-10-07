@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY=C:\Users\taku2\Downloads\ComfyUI_windows_portable\python_embeded\python.exe
if not exist "%PY%" (
  echo Python が見つかりません: %PY%
  echo このファイルを右クリック→編集 で、「set PY=」の行のパスを直してください。
  pause
  exit /b 1
)
if "%~1"=="" (
  echo ゲームのフォルダ（SuccubusDuel.exe があるフォルダ）を、このファイルにドラッグ＆ドロップしてください。
  echo または:  check_images.bat "ゲームのフォルダ"
  pause
  exit /b 1
)
"%PY%" check_images.py %1
echo.
pause
