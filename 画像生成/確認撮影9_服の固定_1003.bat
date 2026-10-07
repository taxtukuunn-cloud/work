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
echo  確認撮影9：服の固定（2026-10-03）
echo  主人公の顔が隠れる下書きで、服の取り違えを直す試し
echo  確認撮影8 と同じ場面を7枚（3分ほど）
echo  保存先: output\確認9_服の固定
echo ============================================
%PY% gen.py Perfume Perfume_lose_btl_m3 --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Heels Heels_lose_inochi_boss --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Casino Casino_lose_onedari_boss --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Musashi Musashi_atk_m2 --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Eiraira Eiraira_atk_boss --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Centaur Centaur_lose_inochi_boss --model wai --redo --outfit-anchor --out 確認9_服の固定
%PY% gen.py Labyrinth Labyrinth_atk_m2 --model wai --redo --outfit-anchor --out 確認9_服の固定
echo.
echo 終わりました。
pause
