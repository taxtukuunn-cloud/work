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
echo  確認撮影22：衣装の参考画像を主人公の位置だけに効かせる（参考5枚＋5場面×強さ2通り）
echo  [1/2] 主人公ひとりの衣装の絵（参考）を撮る
%PY% "衣装の参考を撮る.py" --out 確認22_参考\参考の絵 Lingerie:Lingerie_lose_inochi_e1 Revue:Revue_atk_m1 Maid:Maid_lose_btl_e1 Casino:Casino_atk_m3 Train:Train_atk_e1
if errorlevel 1 goto end
echo  [2/2] 2人の場面を撮る
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --outfit-ref 0.5 --out 確認22_参考\強さ50
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --outfit-ref 0.5 --out 確認22_参考\強さ50
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --outfit-ref 0.5 --out 確認22_参考\強さ50
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --outfit-ref 0.5 --out 確認22_参考\強さ50
%PY% gen.py Train Train_atk_e1 --model wai --redo --outfit-ref 0.5 --out 確認22_参考\強さ50
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --outfit-ref 0.8 --out 確認22_参考\強さ80
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --outfit-ref 0.8 --out 確認22_参考\強さ80
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --outfit-ref 0.8 --out 確認22_参考\強さ80
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --outfit-ref 0.8 --out 確認22_参考\強さ80
%PY% gen.py Train Train_atk_e1 --model wai --redo --outfit-ref 0.8 --out 確認22_参考\強さ80
:end
echo.
pause
