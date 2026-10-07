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
echo  アニメ調LoRA（anime_screencap-IL-NOOB_v3）の強さ比較
echo  WAI で同じシードを 2枚ずつ:
echo   0   = LoRAなし（タグだけ）
echo   06  = 強さ 0.6
echo   08  = 強さ 0.8（今の既定）
echo   10  = 強さ 1.0
echo  保存先: ComfyUI\output\^<MODコード^>_アニメ調比較\0 / 06 / 08 / 10
echo ============================================
set /p MOD="MODコード（例 Knight）: "
set /p KEY="画像の名前（例 Knight_master）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
%PY% gen.py %MOD% %KEY% --model wai --seed %SEED% --batch 2 --out %MOD%_アニメ調比較/0 --sdxl-lora-strength 0
%PY% gen.py %MOD% %KEY% --model wai --seed %SEED% --batch 2 --out %MOD%_アニメ調比較/06 --sdxl-lora-strength 0.6
%PY% gen.py %MOD% %KEY% --model wai --seed %SEED% --batch 2 --out %MOD%_アニメ調比較/08 --sdxl-lora-strength 0.8
%PY% gen.py %MOD% %KEY% --model wai --seed %SEED% --batch 2 --out %MOD%_アニメ調比較/10 --sdxl-lora-strength 1.0
echo.
echo 8枚を送りました。数分で ComfyUI\output\%MOD%_アニメ調比較\ に保存されます。
echo 気に入った強さを model.json の "strength" と "clip_strength" に書いてください。
:end
pause
