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
echo  主人公の年齢の比較（同じシードで4枚ずつ）
echo   A: 今の既定＝老け顔対策（20歳・fresh face に言い換え＋ネガに老け顔）
echo   B: 旧方式（mature male・25歳のまま）
echo  保存先: ComfyUI\output\^<MODコード^>_年齢比較\A / B
echo  見るところ: 主人公が老けて見えないか／逆に幼く見えないか（成人に見えること）
echo ============================================
set /p MOD="MODコード（例 Knight）: "
set /p KEY="画像の名前（例 Knight_lose_btl_m1）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_年齢比較/A
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_年齢比較/B --hero-age mature
echo.
echo 8枚を送りました。3分ほどで ComfyUI\output\%MOD%_年齢比較\ に保存されます。
:end
pause
