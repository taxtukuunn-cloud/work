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
echo  問題が出た15枚の撮り直し（キャラLoRAは相手の範囲だけ・顔を包むPOV下書きを外した版）
echo  保存先: output\キャラLoRA確認\MOD名_撮り直し\
echo ============================================
%PY% gen.py Prison Prison_lose_btl_e3 --model wai --out キャラLoRA確認\Prison_撮り直し
%PY% gen.py Eruru Eruru_lose_btl_boss --model wai --out キャラLoRA確認\Eruru_撮り直し
%PY% gen.py Eiraira Eiraira_lose_btl_e3 --model wai --out キャラLoRA確認\Eiraira_撮り直し
%PY% gen.py Masque Masque_lose_btl_m1 --model wai --out キャラLoRA確認\Masque_撮り直し
%PY% gen.py Library Library_lose_btl_m1 --model wai --out キャラLoRA確認\Library_撮り直し
%PY% gen.py Clinic Clinic_lose_btl_m1 --model wai --out キャラLoRA確認\Clinic_撮り直し
%PY% gen.py Inn Inn_lose_btl_boss --model wai --out キャラLoRA確認\Inn_撮り直し
%PY% gen.py Harem Harem_lose_btl_m1 --model wai --out キャラLoRA確認\Harem_撮り直し
%PY% gen.py Exam Exam_lose_btl_e2 --model wai --out キャラLoRA確認\Exam_撮り直し
%PY% gen.py Ranch Ranch_boss --model wai --out キャラLoRA確認\Ranch_撮り直し
%PY% gen.py Amazon Amazon_lose_btl_e1 --model wai --out キャラLoRA確認\Amazon_撮り直し2
%PY% gen.py Beach Beach_lose_btl_e1 --model wai --out キャラLoRA確認\Beach_撮り直し
%PY% gen.py Sister Sister_lose_btl_boss --model wai --out キャラLoRA確認\Sister_撮り直し
%PY% gen.py Shrine Shrine_lose_btl_e3 --model wai --out キャラLoRA確認\Shrine_撮り直し
%PY% gen.py Studio Studio_lose_btl_e1 --model wai --out キャラLoRA確認\Studio_撮り直し
echo.
echo 送信しました。終わったら教えてください。
pause
