@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
curl -s -o nul http://127.0.0.1:8188/ && goto ready
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
goto wait
:ready
echo ============================================
echo  直し撮影 2回目（13枚・25分ほど）
echo  保存先: output\確認3_直し2\MOD名\
echo  終わったら 一覧画像を作る_直し.bat を実行してください
echo ============================================
%PY% gen.py Amazon Amazon_lose_btl_e1 --model wai --out 確認3_直し2\Amazon
%PY% gen.py Cammy Cammy_lose_btl_e2 --model wai --out 確認3_直し2\Cammy
%PY% gen.py Clock Clock_lose_btl_e1 --model wai --out 確認3_直し2\Clock
%PY% gen.py Esthe Esthe_lose_btl_m1 --model wai --out 確認3_直し2\Esthe
%PY% gen.py Gemini Gemini_lose_btl_e3 --model wai --out 確認3_直し2\Gemini
%PY% gen.py General General_lose_btl_e1 --model wai --out 確認3_直し2\General
%PY% gen.py Masque Masque_lose_btl_m1 --model wai --out 確認3_直し2\Masque
%PY% gen.py Military Military_lose_btl_e3 --model wai --out 確認3_直し2\Military
%PY% gen.py Pawn Pawn_lose_btl_m1 --model wai --out 確認3_直し2\Pawn
%PY% gen.py Library Library_lose_btl_m1 --model wai --out 確認3_直し2\Library
%PY% gen.py Heels Heels_lose_btl_e2 --model wai --out 確認3_直し2\Heels
%PY% gen.py Tavern Tavern_lose_btl_e3 --model wai --out 確認3_直し2\Tavern
%PY% gen.py Sphinx Sphinx_lose_btl_e1 --model wai --out 確認3_直し2\Sphinx
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
pause
