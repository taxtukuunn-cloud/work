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
echo ============================================
echo  まだ敵キャラに割り振っていないキャラLoRA 18個の立ち絵（2026-10-03）
echo  1個につき1枚、服を着た全身の立ち絵を撮ります（18枚・6分ほど）
echo  保存先: output\キャラLoRA未割当\
echo ============================================
%PY% 未割当キャラLoRAの立ち絵.py %*
echo.
echo 終わったら教えてください。
pause
