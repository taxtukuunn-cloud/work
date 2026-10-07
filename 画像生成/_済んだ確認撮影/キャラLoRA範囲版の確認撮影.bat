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
echo  キャラLoRAを相手の範囲だけにかける版の確認（Oiran と Konoha と Amazon）
echo  画面に「LoRAフック: 使える」と出るか確認してください
echo  保存先: output\キャラLoRA確認\MOD名_範囲版\
echo ============================================
%PY% gen.py Oiran Oiran_lose_btl_m1,Oiran_atk_m1,Oiran_atk_m2 --model wai --out キャラLoRA確認\Oiran_範囲版
%PY% gen.py Konoha Konoha_lose_btl_m1,Konoha_lose_btl_e2,Konoha_lose_btl_boss --model wai --out キャラLoRA確認\Konoha_範囲版
%PY% gen.py Amazon Amazon_lose_btl_e1,Amazon_atk_e1 --model wai --out キャラLoRA確認\Amazon_範囲版
echo.
echo 送信しました。終わったら教えてください。
pause
