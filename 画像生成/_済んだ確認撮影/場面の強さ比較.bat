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
echo  イベント（2人の場面）の LoRA の強さ比較（同じシードで2枚ずつ）
echo   主人公LoRA  h0 / h03 / h05 / h07（敵キャラLoRA は既定の強さ）
echo   敵キャラLoRA c0 / c04 / c06 / c08（主人公LoRA は既定の強さ）
echo  場面の画像名を入れてください（例 Lamia_atk_m1 ／ Lamia_lose_btl_e2）
echo  保存先: ComfyUI\output\^<MOD^>_場面比較\
echo ============================================
set /p MOD="MODコード（例 Lamia）: "
set /p KEY="画像の名前（例 Lamia_atk_m1）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
set O=--model wai --seed %SEED% --batch 2
set D=%MOD%_場面比較
%PY% gen.py %MOD% %KEY% %O% --out %D%/h0 --hero-scene-strength 0
%PY% gen.py %MOD% %KEY% %O% --out %D%/h03 --hero-scene-strength 0.3
%PY% gen.py %MOD% %KEY% %O% --out %D%/h05 --hero-scene-strength 0.5
%PY% gen.py %MOD% %KEY% %O% --out %D%/h07 --hero-scene-strength 0.7
%PY% gen.py %MOD% %KEY% %O% --out %D%/c0 --chara-strength 0
%PY% gen.py %MOD% %KEY% %O% --out %D%/c04 --chara-strength 0.4
%PY% gen.py %MOD% %KEY% %O% --out %D%/c06 --chara-strength 0.6
%PY% gen.py %MOD% %KEY% %O% --out %D%/c08 --chara-strength 0.8
echo.
echo 16枚を送りました。良かった強さを model.json の mod_style に書いてください：
echo   主人公 → hero_scene_strength ／ 敵キャラ → chara_scene_strength
:end
pause
