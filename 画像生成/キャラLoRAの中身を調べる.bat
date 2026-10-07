@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  キャラLoRAの中身（トリガー・学習タグ・年齢タグ）を調べます（2026-10-02）
echo  LoRA は読むだけで変更しません。撮影もしません
echo ============================================
%PY% キャラLoRA_中身.py
echo.
pause
