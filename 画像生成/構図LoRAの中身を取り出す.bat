@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  構図LoRA の中身（学習タグなど）を取り出す（2026-09-30）
echo  LoRA は変更しません。数秒で終わります。ComfyUI の起動は不要です。
echo  出力: 画像生成\構図LoRA_中身\
echo ============================================
%PY% 構図LoRA_中身.py %*
echo.
echo 終わったら Claude に「中身を取り出した」と伝えてください。
pause
