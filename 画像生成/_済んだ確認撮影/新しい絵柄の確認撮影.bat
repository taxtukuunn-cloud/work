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
echo  新しい絵柄14種の確認撮影（2026-10-02）
echo  絵柄ごとに1MOD：立ち絵（master）と 敗北イベント1枚（lose_btl_m1）
echo  保存先: output\MOD名_WAI_絵柄名\（本番と同じ場所。良ければそのまま使えます）
echo ============================================
set MODS=Alraune,Cammy,Inma,Hive,Pawn,Harem,Sphinx,Prison,Idol,Clock,Police,Casino,Luna,Tea
%PY% gen.py %MODS% _master,_lose_btl_m1 --model wai
echo.
echo 送信しました。終わったら教えてください。
pause
