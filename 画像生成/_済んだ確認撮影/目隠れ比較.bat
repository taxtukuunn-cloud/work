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
echo  比較 その5（1回ごとの当たり外れが大きいので、4枚ずつで比べる）
echo   A: 今の既定（4枚）
echo   B: 旧方式＝主人公の目隠れを文字でも書く（4枚）
echo  保存先: ComfyUI\output\^<MODコード^>_比較5\A / B
echo  見るところ: 相手の目が見えるか／役と服が入れ替わっていないか
echo ============================================
set /p MOD="MODコード（例 Android）: "
set /p KEY="画像の名前（例 Android_atk_e1）: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_比較5/A
%PY% gen.py %MOD% %KEY% --seed %SEED% --batch 4 --out %MOD%_比較5/B --eyes-text keep
echo.
echo 8枚を送りました。3分ほどで ComfyUI\output\%MOD%_比較5\ に保存されます。
:end
pause
