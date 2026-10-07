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
echo  確認撮影12：女装の場面を「主人公の範囲がある下書き」で撮る（6枚）
%PY% gen.py Casino Casino_lose_onedari_boss --model wai --redo --out 確認12_女装
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --out 確認12_女装
%PY% gen.py Dorm Dorm_atk_m1 --model wai --redo --out 確認12_女装
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --out 確認12_女装
%PY% gen.py Train Train_lose_btl_m3 --model wai --redo --out 確認12_女装
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --out 確認12_女装
echo.
pause
