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
echo  確認撮影23：衣装の参考画像その2 [1/2] 参考の絵だけ撮り直す（大人の顔つき・5枚）
%PY% "衣装の参考を撮る.py" --out 確認23_参考\参考の絵 Lingerie:Lingerie_lose_inochi_e1 Revue:Revue_atk_m1 Maid:Maid_lose_btl_e1 Casino:Casino_atk_m3 Train:Train_atk_e1
echo.
echo  参考の絵 5枚を Claude に見せてください（2人の場面はそのあと撮ります）
pause
