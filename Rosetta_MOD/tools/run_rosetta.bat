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
echo ComfyUI を起動した状態で実行してください。
echo.
"%PY%" run_rosetta_batch.py %*
echo.
pause
