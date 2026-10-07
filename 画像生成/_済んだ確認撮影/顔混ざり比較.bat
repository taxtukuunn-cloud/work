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
echo  2人の場面での顔の混ざり比較（主人公LoRAの強さ別・同じシードで2枚ずつ）
echo   s08 = 0.8（立ち絵と同じ）  s06 = 0.6（今の既定）
echo   s04 = 0.4                  s00 = 主人公LoRAなし（文字の指定だけ）
echo  保存先: ComfyUI\output\^<MODコード^>_顔混ざり比較\
echo  見るところ: 相手の顔が主人公に似ていないか／主人公が主人公に見えるか
echo ============================================
set /p MOD="MODコード（例 Knight）: "
set /p KEY="場面の名前（例 Knight_atk_m1）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
set O=--model wai --seed %SEED% --batch 2
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_顔混ざり比較/s08 --hero-scene-strength 0.8
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_顔混ざり比較/s06 --hero-scene-strength 0.6
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_顔混ざり比較/s04 --hero-scene-strength 0.4
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_顔混ざり比較/s00 --hero-scene-strength 0
echo.
echo 8枚を送りました。良かった強さを model.json の sdduel_hero_xl の "scene_strength" に書いてください。
:end
pause
