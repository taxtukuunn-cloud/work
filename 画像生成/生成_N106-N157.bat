@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
set MODS=Genji,Tensho,Queens,Yamatai,Poseidon,Seraph,Sphinx2,Ranch2,PandoraFarm,Hakai,Sosei,Konton,Yumir,Venus,Diamond,Arena,Queen2,Dominia1,Dominia2,LastTower,LastRoad,Kargos1,Kargos2,Shrift1,Shrift2,Moon1,Moon2,REso,Witches,LostF,Hunter,Grail,Nympho,Alfimia,Honey,Bikyaku,Daydream,VampCastle,Plansect,Spiders,Minotaur,Volcano,SuccVillage,Amos,SnowAngel,OpenSea,Madam,BlackCastle,RedMountain,ElfNinja,Research,LilyMansion
echo ============================================
echo  N106～N157（52MOD）の画像を撮ります（約2,400枚・オナニー場面は撮らない設定）
echo  撮り済みは飛ばします。途中で閉じても次回は続きから。
echo  ※出張キャラの見た目は文章の目印から作った仮のものです。原作と違えば N106-N157_場面\scene_data\コード.py の tags を直して
echo    「画像プロンプトを作り直す_N106-N157.bat」を実行してください
echo ============================================
set /p ONE="撮るMODコード（Enterだけ＝52MOD全部 ／ 例 Genji,Tensho）: "
if not "%ONE%"=="" set MODS=%ONE%
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
