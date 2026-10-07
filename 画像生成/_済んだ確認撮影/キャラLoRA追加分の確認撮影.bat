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
echo  追加した8体（保留分）の確認撮影（2026-10-02）
echo  保存先: output\キャラLoRA確認\MOD名\
echo ============================================
%PY% gen.py Valkyrie Valkyrie_master,Valkyrie_lose_btl_m1 --model wai --out キャラLoRA確認\Valkyrie
%PY% gen.py Sylvia Sylvia_e2,Sylvia_lose_btl_e2 --model wai --out キャラLoRA確認\Sylvia
%PY% gen.py Prison Prison_master,Prison_lose_btl_m1 --model wai --out キャラLoRA確認\Prison
%PY% gen.py Beach Beach_e1,Beach_lose_btl_e1 --model wai --out キャラLoRA確認\Beach
%PY% gen.py Studio Studio_e1,Studio_lose_btl_e1 --model wai --out キャラLoRA確認\Studio
%PY% gen.py Circus Circus_e3,Circus_lose_btl_e3 --model wai --out キャラLoRA確認\Circus
%PY% gen.py Smith Smith_e3,Smith_lose_btl_e3 --model wai --out キャラLoRA確認\Smith
%PY% gen.py Sphinx Sphinx_e1,Sphinx_lose_btl_e1 --model wai --out キャラLoRA確認\Sphinx
echo.
echo 送信しました。終わったら教えてください。
pause
