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
echo  追加した7体の確認撮影（2026-10-02）
echo  保存先: output\キャラLoRA確認\MOD名\
echo ============================================
%PY% gen.py Patra Patra_e1,Patra_lose_btl_e1 --model wai --out キャラLoRA確認\Patra
%PY% gen.py Angel Angel_master,Angel_lose_btl_m1 --model wai --out キャラLoRA確認\Angel
%PY% gen.py Sister Sister_boss,Sister_lose_btl_boss --model wai --out キャラLoRA確認\Sister
%PY% gen.py Pawn Pawn_master,Pawn_lose_btl_m1 --model wai --out キャラLoRA確認\Pawn
%PY% gen.py Underworld Underworld_boss,Underworld_lose_btl_boss --model wai --out キャラLoRA確認\Underworld
%PY% gen.py Starship Starship_e1,Starship_lose_btl_e1 --model wai --out キャラLoRA確認\Starship
%PY% gen.py Candy Candy_master,Candy_lose_btl_m1 --model wai --out キャラLoRA確認\Candy
echo.
echo 送信しました。終わったら教えてください。
pause
