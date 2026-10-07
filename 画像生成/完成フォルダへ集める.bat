@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
set /p MOD="MODコード（例 Host ／ 複数は Host,Heels ／ Enterだけ＝全部）: "
if "%MOD%"=="" set MOD=all
%PY% collect.py %MOD%
pause
