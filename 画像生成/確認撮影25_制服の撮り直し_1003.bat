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
echo  確認撮影25：制服（Train）の参考の絵を細身で撮り直す → Claude が確認 → 2人の場面×強さ2通り
%PY% "衣装の参考を撮る.py" --out 確認25_参考\参考の絵 --seed-add 1 Train:Train_atk_e1
if errorlevel 1 goto end
echo.
echo  ここで止めて、Claude に「参考できた」と伝えてください。OK が出たら何かキーを押して続きへ。
pause
%PY% gen.py Train Train_atk_e1 --model wai --redo --outfit-ref 0.5 --out 確認25_参考\強さ50
%PY% gen.py Train Train_atk_e1 --model wai --redo --outfit-ref 0.8 --out 確認25_参考\強さ80
:end
echo.
pause
