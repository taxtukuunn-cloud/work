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
echo  主人公LoRAを主人公の範囲だけにかける比べ撮り（10場面 x 強さ2通り＝20枚・40分ほど）
echo  保存先: output\主人公範囲比較_05\ と output\主人公範囲比較_08\
echo  終わったら 一覧画像を作る_主人公範囲.bat を実行してください
echo ============================================
%PY% gen.py Military Military_lose_btl_e3 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Military
%PY% gen.py Library Library_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Library
%PY% gen.py Pawn Pawn_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Pawn
%PY% gen.py Beach Beach_lose_btl_e1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Beach
%PY% gen.py Clinic Clinic_lose_btl_e2 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Clinic
%PY% gen.py Idol Idol_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Idol
%PY% gen.py Smith Smith_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Smith
%PY% gen.py Twins Twins_lose_btl_e1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Twins
%PY% gen.py Bride Bride_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Bride
%PY% gen.py Angel Angel_lose_btl_m1 --model wai --hero-hook-strength 0.5 --out 主人公範囲比較_05\Angel
%PY% gen.py Military Military_lose_btl_e3 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Military
%PY% gen.py Library Library_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Library
%PY% gen.py Pawn Pawn_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Pawn
%PY% gen.py Beach Beach_lose_btl_e1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Beach
%PY% gen.py Clinic Clinic_lose_btl_e2 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Clinic
%PY% gen.py Idol Idol_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Idol
%PY% gen.py Smith Smith_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Smith
%PY% gen.py Twins Twins_lose_btl_e1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Twins
%PY% gen.py Bride Bride_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Bride
%PY% gen.py Angel Angel_lose_btl_m1 --model wai --hero-hook-strength 0.8 --out 主人公範囲比較_08\Angel
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
pause
