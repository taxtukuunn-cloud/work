@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  構図LoRAの割当確認（ComfyUI には送りません）
echo  結果: 画像生成\構図LoRA_割当.csv（MOD, 画像名, action, look, 当てはまった語）
echo ============================================
%PY% gen.py all --model wai --pose-report
echo.
pause
