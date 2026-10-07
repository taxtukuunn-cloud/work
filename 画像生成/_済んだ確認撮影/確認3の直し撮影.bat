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
echo  確認3でおかしかった場面の撮り直し（31枚・1時間ほど）
echo  保存先: output\確認3_直し\MOD名\
echo  終わったら 一覧画像を作る_直し.bat を実行してください
echo ============================================
%PY% gen.py Amazon Amazon_lose_btl_boss,Amazon_lose_btl_e1 --model wai --out 確認3_直し\Amazon
%PY% gen.py Cammy Cammy_lose_btl_e2 --model wai --out 確認3_直し\Cammy
%PY% gen.py Candy Candy_lose_btl_m1 --model wai --out 確認3_直し\Candy
%PY% gen.py Clinic Clinic_lose_btl_m1 --model wai --out 確認3_直し\Clinic
%PY% gen.py Clock Clock_lose_btl_e1 --model wai --out 確認3_直し\Clock
%PY% gen.py Esthe Esthe_lose_btl_m1 --model wai --out 確認3_直し\Esthe
%PY% gen.py Exam Exam_lose_btl_boss --model wai --out 確認3_直し\Exam
%PY% gen.py Gemini Gemini_lose_btl_e3 --model wai --out 確認3_直し\Gemini
%PY% gen.py General General_lose_btl_e1,General_lose_btl_boss --model wai --out 確認3_直し\General
%PY% gen.py GhostShip GhostShip_lose_btl_boss --model wai --out 確認3_直し\GhostShip
%PY% gen.py Heels Heels_lose_btl_e2 --model wai --out 確認3_直し\Heels
%PY% gen.py Lab Lab_lose_btl_m1,Lab_lose_btl_e2 --model wai --out 確認3_直し\Lab
%PY% gen.py Library Library_lose_btl_m1 --model wai --out 確認3_直し\Library
%PY% gen.py Masque Masque_lose_btl_m1 --model wai --out 確認3_直し\Masque
%PY% gen.py Military Military_lose_btl_e3 --model wai --out 確認3_直し\Military
%PY% gen.py Musashi Musashi_lose_btl_m1 --model wai --out 確認3_直し\Musashi
%PY% gen.py Octa Octa_lose_btl_boss --model wai --out 確認3_直し\Octa
%PY% gen.py Patra Patra_lose_btl_e2 --model wai --out 確認3_直し\Patra
%PY% gen.py Pawn Pawn_lose_btl_m1 --model wai --out 確認3_直し\Pawn
%PY% gen.py Revue Revue_lose_btl_boss --model wai --out 確認3_直し\Revue
%PY% gen.py Sphinx Sphinx_lose_btl_e1 --model wai --out 確認3_直し\Sphinx
%PY% gen.py Starship Starship_lose_btl_e1 --model wai --out 確認3_直し\Starship
%PY% gen.py Sylvia Sylvia_lose_btl_e2 --model wai --out 確認3_直し\Sylvia
%PY% gen.py Tavern Tavern_lose_btl_e3,Tavern_lose_btl_boss --model wai --out 確認3_直し\Tavern
%PY% gen.py Train Train_lose_btl_m1 --model wai --out 確認3_直し\Train
%PY% gen.py Valkyrie Valkyrie_lose_btl_boss,Valkyrie_lose_btl_e3 --model wai --out 確認3_直し\Valkyrie
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
pause
