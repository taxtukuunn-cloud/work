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
echo  全MOD 一括生成（MODごとの絵柄＝絵柄割当.csv ＋ 絵柄別の主人公LoRA）
echo  撮り済みの画像は飛ばします。途中で閉じても次回は続きから。
echo ============================================
set /p RS="MODの絵柄をランダムに割り当てる？（y＝絵柄が空欄のMODだけ ／ a＝全MODを振り直す ／ Enterだけ＝しない）: "
if /i "%RS%"=="y" %PY% gen.py all --random-style --assign-only
if /i "%RS%"=="a" %PY% gen.py all --random-style all --assign-only
echo.
%PY% gen.py all all --dry-run
echo.
set /p OK="この内容で始めますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
%PY% gen.py all all
:end
pause
