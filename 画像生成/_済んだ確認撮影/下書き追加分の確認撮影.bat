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
echo  下書きを増やした分の確認撮影（2026-10-02）
echo  新しく使う元絵の構図ごとに1場面、下書きあり／なしを同じシードで撮ります
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし
echo  先に「人物の範囲を作る.bat」を実行しておいてください
echo ============================================
set IDS=futa,futadom_p,rusty,chastity,inverted,xcross,collar,energy_drain,energy_drain_kiss,energy_drain_ride,thigh,thigh_lying,thigh_ontop,thigh_side,thigh_standing,alt_thigh_top,toes_nipple,toes_nipple_hj,peg_chair,suspension,suspension_hj,suspension_peg,rah,rah_standing,step,side_chin_lift,hug_standing_chest,kiss_wall,close_hug_p
%PY% gen.py all --model wai --control-sample 1 --control-id %IDS%
echo.
echo 送信しました。終わったら教えてください。
pause
