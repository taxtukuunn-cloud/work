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
echo  モデルの比較（同じシードで4枚ずつ）
echo   A: WAI-Anima（今まで・LoRAあり）
echo   B: waiIllustriousSDXL_v170（LoRAなし）
echo  保存先: ComfyUI\output\^<MODコード^>_モデル比較\A / B
echo ============================================
set /p MOD="MODコード（例 Knight）: "
set /p KEY="画像の名前（例 Knight_lose_btl_m1）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_モデル比較/A --model anima
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_モデル比較/B --model wai
echo.
echo 8枚を送りました。数分で ComfyUI\output\%MOD%_モデル比較\ に保存されます。
:end
pause
