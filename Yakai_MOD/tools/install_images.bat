@echo off
chcp 65001 >nul
setlocal
set "PY=C:\Users\taku2\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist "%PY%" (
  echo [エラー] Pythonが見つかりません: %PY%
  echo このbatをメモ帳で開き、4行目の PY= を ComfyUI の python_embeded\python.exe の場所に直してください。
  pause
  exit /b 1
)
set "PIC=%~1"
if "%PIC%"=="" (
  echo ゲームの Picture フォルダのパスを貼り付けてEnter ^(Saveフォルダと同じ階層のPicture^)
  set /p PIC=パス: 
)
set "PIC=%PIC:"=%"
if "%PIC:~-1%"=="\" set "PIC=%PIC:~0,-1%"
set "EXTRA=%~2"
if "%EXTRA%"=="" (
  echo 生成した画像を保存しているフォルダがあれば貼り付けてEnter ^(なければ空でEnter^)
  set /p EXTRA=パス: 
)
set "EXTRA=%EXTRA:"=%"
if "%EXTRA:~-1%"=="\" set "EXTRA=%EXTRA:~0,-1%"
if "%EXTRA%"=="" (
  "%PY%" "%~dp0install_images.py" "%PIC%"
) else (
  "%PY%" "%~dp0install_images.py" "%PIC%" "%EXTRA%"
)
pause
