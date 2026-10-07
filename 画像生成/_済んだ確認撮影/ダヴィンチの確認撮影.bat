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
echo レオナルド・ダ・ヴィンチ（Revue e1）の確認撮影
%PY% gen.py Revue Revue_e1,Revue_lose_btl_e1 --model wai --out キャラLoRA確認\Revue
echo.
echo 送信しました。終わったら教えてください。
pause
