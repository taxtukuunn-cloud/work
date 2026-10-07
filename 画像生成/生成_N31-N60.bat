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
echo  N31～N60（30MOD）画像生成：立ち絵・魔法・背景＋場面40枚
echo  撮り済みの画像は飛ばします。途中で閉じても次回は続きから。
echo  一部のMODだけなら 生成.bat で MODコードを入れてください。
echo ============================================
%PY% gen.py Onsen,Arachne,Dream,Library,Angel,Harem,Dragon,Tutor,DarkElf,Casino,Nekomata,Snow,Oni,Mimic,Train,ShowPub,Oiran,Office,Lingerie,GhostShip,Alchemy,Masque,Fortune,Revue,Studio,Luna,Police,Circus,Candy,Starship all --dry-run
echo.
set /p OK="この内容で始めますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
%PY% gen.py Onsen,Arachne,Dream,Library,Angel,Harem,Dragon,Tutor,DarkElf,Casino,Nekomata,Snow,Oni,Mimic,Train,ShowPub,Oiran,Office,Lingerie,GhostShip,Alchemy,Masque,Fortune,Revue,Studio,Luna,Police,Circus,Candy,Starship all
:end
pause
