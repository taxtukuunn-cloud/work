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
echo  若く見える原因の切り分け撮影（同じ場面・同じシード）
echo  1回目：絵柄LoRAも主人公LoRAもなし   → 各フォルダの _00004_
echo  2回目：絵柄LoRAあり・主人公LoRAだけなし → 各フォルダの _00005_
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし
echo ============================================
set IDS=footjob_side_lying,side_allfours_milking,nipple_behind_standing,finger_spoon_side,straddle_pin_side,whisper_lying
%PY% gen.py all --model wai --control-sample 1 --control-id %IDS% --no-mod-style
echo 1回目を送信しました。ComfyUI の処理が終わってから何かキーを押すと2回目を送ります。
pause
%PY% gen.py all --model wai --control-sample 1 --control-id %IDS% --hero-scene-strength 0
echo.
echo 送信しました。終わったら教えてください。
pause
