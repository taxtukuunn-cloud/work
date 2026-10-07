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
echo ============================================
echo  確認撮影10：ふたなり・ニューハーフの股間のふくらみ／相手のペニスを大きめに（2026-10-03）
echo  8枚（3分ほど）
echo  保存先: output\確認10_ふくらみ
echo ============================================
%PY% gen.py Angel Angel_master --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Angel Angel_atk_m1 --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Angel Angel_atk_m3 --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Alchemy Alchemy_e1 --model wai --redo --out 確認10_ふくらみ
%PY% gen.py ShowPub ShowPub_atk_m1 --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Vampire Vampire_boss --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Hive Hive_atk_m1 --model wai --redo --out 確認10_ふくらみ
%PY% gen.py Knight Knight_atk_m3 --model wai --redo --out 確認10_ふくらみ
echo.
echo 終わりました。
pause
