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
echo トネリコ（Alchemy master）・ルージュ（Cammy e3）・おみい（Patra e2）の確認撮影
%PY% gen.py Alchemy Alchemy_master,Alchemy_lose_btl_m1 --model wai --out キャラLoRA確認\Alchemy
%PY% gen.py Cammy Cammy_e3,Cammy_lose_btl_e3 --model wai --out キャラLoRA確認\Cammy
%PY% gen.py Patra Patra_e2,Patra_lose_btl_e2 --model wai --out キャラLoRA確認\Patra
echo.
echo 送信しました。終わったら教えてください。
pause
