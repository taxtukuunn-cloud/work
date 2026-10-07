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
echo  相手が複数の場面の確認撮影（2026-10-03）
echo  相手が2～3人で主人公も映る 16場面（Twins 12・Heels のボス 4）を、
echo  新しく作った「相手が複数」の下書きで撮ります（16枚・6分ほど）
echo  保存先: output\複数の組確認\Twins と Heels
echo ============================================
echo [1/2] Twins（12枚）
%PY% gen.py Twins Twins_atk_m1,Twins_atk_m2,Twins_atk_m3,Twins_lose_btl_m1,Twins_lose_inochi_m1,Twins_lose_onedari_m1,Twins_lose_btl_m2,Twins_lose_inochi_m2,Twins_lose_onedari_m2,Twins_lose_btl_m3,Twins_lose_inochi_m3,Twins_lose_onedari_m3 --model wai --out 複数の組確認\Twins
echo [2/2] Heels のボス（4枚）
%PY% gen.py Heels Heels_atk_boss,Heels_lose_btl_boss,Heels_lose_inochi_boss,Heels_lose_onedari_boss --model wai --out 複数の組確認\Heels
echo.
echo 送信しました。終わったら教えてください。
pause
