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
set /p MOD="MODコード（例 Host ／ 複数は Host,Heels ／ 全部は all）: "
if "%MOD%"=="" goto end
set /p RS="MODの絵柄をランダムに割り当てる？（y＝絵柄が空欄のMODだけ ／ a＝入れたMODを全部振り直す ／ Enterだけ＝しない）: "
if /i "%RS%"=="y" %PY% gen.py %MOD% --random-style --assign-only
if /i "%RS%"=="a" %PY% gen.py %MOD% --random-style all --assign-only
set /p KEYS="撮る画像（Enterだけ＝全部 ／ 名前の一部をカンマ区切り 例 lose_btl,atk_m1）: "
if "%KEYS%"=="" set KEYS=all
set /p RND="撮り直し？（撮り済みも新しいシードで撮るなら y）: "
set OPT=
if /i "%RND%"=="y" set OPT=--random --redo
set /p BAT="1枚につき何枚の候補を撮る？（Enterだけ＝1。撮り直しは 4 がおすすめ）: "
if "%BAT%"=="" set BAT=1
%PY% gen.py %MOD% %KEYS% %OPT% --batch %BAT%
:end
pause
