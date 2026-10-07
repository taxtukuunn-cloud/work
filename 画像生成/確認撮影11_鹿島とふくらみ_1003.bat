@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI を起動します...
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI の起動を待っています...
goto wait
:ready
echo  確認撮影11：鹿島の撮り直し＋ふくらみの言い回し直し（7枚）
%PY% gen.py Salon Salon_e2 --model wai --redo --out 確認11
%PY% gen.py Alchemy Alchemy_e1 --model wai --redo --out 確認11
%PY% gen.py Vampire Vampire_boss --model wai --redo --out 確認11
%PY% gen.py Angel Angel_master --model wai --redo --out 確認11
%PY% gen.py Hive Hive_atk_m1 --model wai --redo --out 確認11
%PY% gen.py Angel Angel_atk_m1 --model wai --redo --out 確認11
%PY% gen.py Office Office_atk_e3 --model wai --redo --out 確認11
echo.
pause
