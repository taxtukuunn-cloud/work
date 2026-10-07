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
echo ============================================
echo  追加した9体の確認撮影（立ち絵と敗北イベント1枚ずつ）
echo  保存先: output\キャラLoRA確認\MOD名\
echo ============================================
%PY% gen.py Sky Sky_e1,Sky_lose_btl_e1 --model wai --out キャラLoRA確認\Sky
%PY% gen.py Kiss Kiss_e2,Kiss_lose_btl_e2 --model wai --out キャラLoRA確認\Kiss
%PY% gen.py Military Military_e1,Military_lose_btl_e1 --model wai --out キャラLoRA確認\Military
%PY% gen.py Harem Harem_e2,Harem_lose_btl_e2 --model wai --out キャラLoRA確認\Harem
%PY% gen.py Clinic Clinic_e3,Clinic_lose_btl_e3 --model wai --out キャラLoRA確認\Clinic
%PY% gen.py Heels Heels_e2,Heels_lose_btl_e2 --model wai --out キャラLoRA確認\Heels
%PY% gen.py Lab Lab_e2,Lab_lose_btl_e2,Lab_e3,Lab_lose_btl_e3 --model wai --out キャラLoRA確認\Lab
%PY% gen.py Witch Witch_master,Witch_lose_btl_m1 --model wai --out キャラLoRA確認\Witch
echo.
echo 送信しました。終わったら教えてください。
pause
