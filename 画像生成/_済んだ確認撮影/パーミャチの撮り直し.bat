@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
curl -s -o nul http://127.0.0.1:8188/ && goto ready
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
goto wait
:ready
echo パーミャチ（Candy master）：立ち絵はキャラLoRAあり・場面はLoRAなしで撮り直し
%PY% gen.py Candy Candy_master,Candy_lose_btl_m1,Candy_atk_m1 --model wai --out キャラLoRA確認\Candy_撮り直し
echo.
echo 送信しました。終わったら教えてください。
pause
