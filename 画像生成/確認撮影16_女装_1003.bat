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
echo  確認撮影16：女装の場面で相手の服も強める／Maid の衣装を拾う（6枚）
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --out 確認16_女装
%PY% gen.py Perfume Perfume_lose_btl_m3 --model wai --redo --out 確認16_女装
%PY% gen.py Heels Heels_lose_inochi_boss --model wai --redo --out 確認16_女装
%PY% gen.py Maid Maid_atk_m1 --model wai --redo --out 確認16_女装
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --out 確認16_女装
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --out 確認16_女装
echo.
pause
