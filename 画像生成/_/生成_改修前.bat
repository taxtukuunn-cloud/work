@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI を起動します...
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI の起動を待っています...
goto wait
:ready
echo 使えるMODコード:
dir /b prompts
echo.
set /p MOD="MODコード（例 Host）: "
set /p KEYS="撮る画像（Enterだけ＝全部 ／ 名前の一部をカンマ区切り 例 lose_btl,atk_m1）: "
if "%KEYS%"=="" set KEYS=all
set /p RND="シードをランダムにする？（撮り直しは y）: "
set OPT=
if /i "%RND%"=="y" set OPT=--random
%PY% gen.py %MOD% %KEYS% %OPT%
pause
