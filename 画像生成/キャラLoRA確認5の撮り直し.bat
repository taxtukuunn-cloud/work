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
echo  キャラLoRA確認5の撮り直し（5枚）：全身・1人だけで撮り直す／腕章を出さない
%PY% gen.py Exam Exam_e3 --model wai --redo --seed 101 --out キャラLoRA確認5_撮り直し
%PY% gen.py Exam Exam_e3 --model wai --redo --seed 202 --out キャラLoRA確認5_撮り直し
%PY% gen.py Mirror Mirror_e3 --model wai --redo --seed 101 --out キャラLoRA確認5_撮り直し
%PY% gen.py Office Office_e3 --model wai --redo --seed 101 --out キャラLoRA確認5_撮り直し
%PY% gen.py Prison Prison_e2 --model wai --redo --seed 101 --out キャラLoRA確認5_撮り直し
echo.
pause
