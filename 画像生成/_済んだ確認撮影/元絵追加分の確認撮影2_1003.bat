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
echo  元絵の追加分の確認撮影 2回目（2026-10-03）
echo  1) 新しく登録した 14構図（目線の構図など）を 2場面ずつ
echo  2) 前回撮られなかった 7枚を 1枚ずつ指定して 1場面ずつ
echo  3) peg_stand_behind_chin を 3場面（前回は主人公が服を着て出たので撮り足し）
echo  下書きあり／なしを同じシードで撮ります（最大 76枚）
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし
echo ============================================
echo [1/9] 新しく登録した 14構図
%PY% gen.py all --model wai --control-sample 2 --control-id straddle_pov_upright,straddle_pov_handhold,straddle_pov_lean,reverse_straddle_pov,reverse_straddle_lookback,lap_sit_front_hj,hj_pov_close,hj_lying_beside_front,hj_stand_side,foot_sofa_lying,kneel_pov_sit_foot,smother_chest_front,pov_chest_press,lie_beside_pov
echo [2/9] kiss_pov_4
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_kiss_pov_4
echo [3/9] kiss_pov_5
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_kiss_pov_5
echo [4/9] nipple_pov_pinch_2
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_nipple_pov_pinch_2
echo [5/9] suspension_peg_7
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_suspension_peg_7
echo [6/9] peg_spoon_hj_2
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_peg_spoon_hj_2
echo [7/9] urethra_pov_rod_2
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_urethra_pov_rod_2
echo [8/9] urethra_pov_rod_3
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_urethra_pov_rod_3
echo [9/9] peg_stand_behind_chin
%PY% gen.py all --model wai --control-sample 3 --control-id peg_stand_behind_chin
echo.
echo 送信しました。終わったら教えてください。
pause
