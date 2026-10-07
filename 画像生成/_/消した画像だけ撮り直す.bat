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
echo  消した画像だけ撮り直す
echo  ComfyUI\output\^<MODコード^>_自作\ に1枚も残っていない名前だけを、新しいシードで撮ります。
echo  （まだ一度も撮っていない画像も対象になります。残っている画像は撮りません）
echo ============================================
echo 使えるMODコード:
dir /b prompts
echo.
set /p MOD="MODコード（例 Knight ／ 複数は Knight,Oiran ／ Enterだけ＝全部）: "
if "%MOD%"=="" set MOD=all
set /p BAT="1枚につき何枚の候補を撮る？（Enterだけ＝1。撮り直しは 4 がおすすめ）: "
if "%BAT%"=="" set BAT=1
echo.
%PY% gen.py %MOD% all --dry-run
echo.
set /p OK="この件数で撮りますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
%PY% gen.py %MOD% all --random --batch %BAT%
:end
pause
