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
echo  確認撮影13：設定の衣装で出す（キャラLoRAの立ち絵6枚）＋女装の衣装を強める（3枚）
%PY% gen.py Eiraira Eiraira_boss --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Gemini Gemini_master --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Circus Circus_master --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Cammy Cammy_boss --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Flower Flower_master --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Office Office_e3 --model wai --redo --out 確認13_衣装\立ち絵
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --out 確認13_衣装\女装
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --out 確認13_衣装\女装
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --out 確認13_衣装\女装
echo.
pause
