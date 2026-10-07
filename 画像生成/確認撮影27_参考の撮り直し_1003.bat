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
echo  確認撮影27：参考の絵 4枚の撮り直し（ひざ丈メイド・アイドル・巫女・ブラウス）
%PY% "衣装の参考を撮る.py" --out 確認26_参考\参考の絵_撮り直し --seed-add 1 Heels:Heels_atk_e2 Idol:Idol_atk_m2 Shrine:Shrine_atk_e2 Perfume:Perfume_atk_e3
echo.
echo  Claude に「撮り直しできた」と伝えてください
pause
