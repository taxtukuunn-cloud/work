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
echo  絵柄LoRAの差し替え比較（本編の sdduel_style を外して候補1枚に差し替え）
echo   1_現行 2_絵柄なし 3_ATRex 4_Mosouko 5_GEN 6_IFL × 4枚（立ち絵・ペニバン・キス・主人公）× 2シード ＝ 48枚
echo  保存先: ComfyUI\output\絵柄比較\^<条件^>\
echo  撮り終わると 一覧_1_立ち絵.png など4枚の一覧画像を作ります（このウィンドウは閉じずに待ってください）
echo  model.json の標準設定は変えません
echo ============================================
%PY% gen.py all --model wai --style-compare
echo.
echo 一覧画像: ComfyUI\output\絵柄比較\一覧_1_立ち絵.png ／ 一覧_2_ペニバン.png ／ 一覧_3_キス.png ／ 一覧_4_主人公.png
echo 途中で閉じた場合は、撮り終わってから  %%PY%% gen.py all --style-grid  で一覧画像だけ作れます
pause
