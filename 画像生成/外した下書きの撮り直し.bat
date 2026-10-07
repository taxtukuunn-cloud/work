@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  外した下書き finger_front_legs で撮ってしまった絵だけを撮り直します
echo  （まだ撮っていない場面は何もしません。元の絵は消しません）
echo ============================================
%PY% 外した下書きの撮り直し.py finger_front_legs --dry-run
echo.
set /p GO="この絵を撮り直しますか？（y で開始 ／ Enterだけ＝やめる）: "
if /i not "%GO%"=="y" goto end
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI を起動します...
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
goto wait
:ready
%PY% 外した下書きの撮り直し.py finger_front_legs
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
:end
pause
