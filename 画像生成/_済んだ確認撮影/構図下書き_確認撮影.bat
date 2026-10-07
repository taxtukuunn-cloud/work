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
echo  構図の下書き（3D の奥行き）の確認撮影
echo  下書きごとに、その下書きが当たる場面を選び、同じシードで「下書きあり／なし」を撮ります
echo  絵柄・キャラの LoRA は本番（絵柄割当.csv）と同じです
echo  保存先: ComfyUI\output\構図下書き確認\^<下書き^>\あり\ と なし\
echo  見るところ: 構図が場面の文に近づいたか／人物が成人に見えるか（見えない構図は使わない）
echo ============================================
echo  下書き: standing_embrace girl_on_top_kiss all_fours_behind all_fours_behind_reach legs_up_front lying_leanover
echo          standing_foot side_handjob arms_up_bound neck_bite girl_on_top_straddle lap_pillow
echo          standing_front_chest seated_front_chest kneel_front_chest
set /p N="下書きごとに何場面撮りますか（例 1）: "
if "%N%"=="" set N=1
set /p IDS="下書きを絞るなら名前をカンマ区切りで（空欄で全部）: "
set /p ST="下書きの強さ（空欄＝設定どおり 0.7。行為が弱いときは 0.5 など）: "
set /p EN="下書きを効かせる範囲（空欄＝設定どおり 0.5。0.4 なら描き始めの4割だけ）: "
set OPT=
if not "%ST%"=="" set OPT=%OPT% --control-strength %ST%
if not "%EN%"=="" set OPT=%OPT% --control-end %EN%
if "%IDS%"=="" (
  %PY% gen.py all --model wai --control-sample %N% %OPT%
) else (
  %PY% gen.py all --model wai --control-sample %N% --control-id %IDS% %OPT%
)
echo.
echo 送信しました。ComfyUI の処理が終わると output\構図下書き確認\ に保存されます。
pause
