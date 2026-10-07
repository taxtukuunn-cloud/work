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
echo  全MOD 一括生成（sdduel_style-000006 ＋ 主人公LoRA）
echo  撮り済みの画像は飛ばします。途中で閉じても次回は続きから。
echo ============================================
%PY% gen.py all all --dry-run
echo.
set /p OK="この内容で始めますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
%PY% gen.py all all
:end
pause
