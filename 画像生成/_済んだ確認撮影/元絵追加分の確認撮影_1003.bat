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
echo  元絵の追加分の確認撮影（2026-10-03）
echo  今日登録した 13構図と、登録済みの構図に足した 16枚を、1つにつき1場面ずつ
echo  下書きあり／なしを同じシードで撮ります（最大 58枚）
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし
echo  ※ 当たる場面が無い下書きは撮られません（最後の一覧に出ないものがそれです）
echo ============================================
echo [1/2] 今日登録した 13構図
%PY% gen.py all --model wai --control-sample 1 --control-id kiss_above_drool,urethra_pov_rod,urethra_side_rod,peg_wall_behind_nipple,peg_kneel_behind_hj_nipple,fours_behind_nipple,peg_stand_behind_chin,nipple_behind_torso,foot_behind_nipple,ear_prone_above,foot_face_pov,bound_stand_leg_up_peg,stand_embrace_kiss_finger
echo [2/2] 登録済みの構図に足した 16枚
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_kiss_pov_4,depthref_kiss_pov_5,depthref_kiss_pov_6,depthref_nipple_pov_pinch_2,depthref_nipple_pov_pinch_3,depthref_nipple_behind_standing_2,depthref_nipple_behind_standing_3,depthref_suspension_peg_7,depthref_thigh_standing_6,depthref_finger_pov_legs_2,depthref_peg_spoon_hj_2,depthref_peg_prone_side_6,depthref_peg_desk_side_9,depthref_pov_footjob_11,depthref_peg_pov,depthref_between_legs_sit_lying
echo.
echo 送信しました。終わったら教えてください。
pause
