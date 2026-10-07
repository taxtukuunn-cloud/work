@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
set MODS=Amazon,Atelier,Beach,Bride,Cammy,Centaur,Clock,Eiraira,Eruru,Exam,Flower,Gemini,General,Inn,Kiss,Konoha,Labyrinth,Medusa,Military,Mirror,Moth,Musashi,Necro,Neneko,Octa,Patra,Pawn,Perfume,Queen,Ranch,SEruru,Scylla,Shrine,Sister,Sky,Smith,Sphinx,Spirit,Sylvia,Tavern,Tea,Tengu,Underworld,Valkyrie,Werewolf,Yatsume
echo ============================================
echo  N61～N105（45MOD）＋ N17 Scylla の画像を撮ります（46MOD・約2,350枚・約13時間）
echo  撮り済みは飛ばします。途中で閉じても次回は続きから。
echo  ※本編キャラ（N61～N77の一部）の見た目は仮です。先に N61-N105_場面\本編キャラ外見_要確認.csv を確認してください
echo ============================================
set /p RS="MODの絵柄をランダムに割り当てる？（y＝絵柄が空欄のMODだけ ／ Enterだけ＝しない）: "
if /i "%RS%"=="y" %PY% gen.py %MODS% --random-style --assign-only
%PY% gen.py %MODS% all --dry-run
echo.
set /p OK="この内容で始めますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI を起動します...
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI の起動を待っています...
goto wait
:ready
%PY% gen.py %MODS% all
:end
pause
