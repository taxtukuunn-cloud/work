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
echo  確認撮影29：Dorm の衣装を「寮の世話係の制服」に置き換えて撮る＋Maid の参考の撮り直し（参考の絵2枚 → Claude が確認 → 2人の場面2枚）
%PY% "衣装の参考を撮る.py" --out 確認29_Dorm\参考の絵 --seed-add 1 Dorm:Dorm_atk_m1
if errorlevel 1 goto end
%PY% "衣装の参考を撮る.py" --out 確認29_Dorm\参考の絵 --seed-add 1 Maid:Maid_lose_btl_e1
if errorlevel 1 goto end
echo.
echo  ここで止めて、Claude に「参考できた」と伝えてください。OK が出たら何かキーを押して続きへ。
pause
%PY% gen.py Dorm Dorm_atk_m1 --model wai --redo --out 確認29_Dorm\参考なし
%PY% gen.py Dorm Dorm_atk_m1 --model wai --redo --outfit-ref 0.4 --out 確認29_Dorm\強さ40
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --outfit-ref 0.4 --out 確認29_Dorm\強さ40
%PY% gen.py Tavern Tavern_atk_e3 --model wai --redo --outfit-ref 0.4 --out 確認29_Dorm\強さ40
rem %PY% gen.py Dorm Dorm_atk_m3 --model wai --redo --out 確認29_Dorm\参考なし   （寝間着の場面：今回は対象外）
:end
echo.
pause
