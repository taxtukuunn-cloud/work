@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo  下見：全MODの全場面を、撮らずに組み立てて一覧にします（ComfyUI は起動していなくてかまいません・数分）
%PY% gen.py all all --model wai --preview
echo.
echo  できたもの： 下見_全場面.csv ／ 下見_MOD別.csv（このフォルダ）
echo  Claude に「下見できた」と伝えてください
pause
