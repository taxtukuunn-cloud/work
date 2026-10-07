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
echo  人物ごとの範囲（領域指定）の確認撮影
echo  若く見えた6構図を通常設定で撮ります（範囲が効くのは「あり」だけ）
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし（次の番号）
echo ============================================
set IDS=footjob_side_lying,side_allfours_milking,nipple_behind_standing,finger_spoon_side,straddle_pin_side,whisper_lying
%PY% gen.py all --model wai --control-sample 1 --control-id %IDS%
echo.
echo 送信しました。終わったら教えてください。
pause
