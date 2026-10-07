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
echo  横長の元絵・追加分の確認撮影（2026-10-02）
echo  パラダイス・サキュバスから入れた元絵5枚（4構図）を、1枚につき1場面ずつ
echo  下書きあり／なしを同じシードで撮ります
echo  横長の下書き（peg_fours_front・peg_fours_front_2・nipple_pov_straddle）は「あり」だけ 1216x832 で撮ります
echo  保存先: output\構図下書き確認\ref_構図名\あり と なし
echo  ※ stand_embrace_back は人物の範囲が作れなかったため、今は場面が当たりません（撮られなくて正常）
echo ============================================
echo [1/3] peg_fours_front（1枚目）
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_peg_fours_front
echo [2/3] peg_fours_front_2（2枚目）
%PY% gen.py all --model wai --control-sample 1 --control-id depthref_peg_fours_front_2
echo [3/3] nipple_pov_straddle・inverted_seated_toy・stand_embrace_back
%PY% gen.py all --model wai --control-sample 1 --control-id nipple_pov_straddle,inverted_seated_toy,stand_embrace_back
echo.
echo 送信しました。終わったら教えてください。
pause
