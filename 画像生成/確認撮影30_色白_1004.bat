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
echo  確認撮影30：主人公を色白にした確認（9枚）
rem  ※撮らない場面は rem で残してあります。撮るときは行頭の rem を外してください。
rem  ふつうの場面
%PY% gen.py Police Police_atk_e1 --model wai --redo --out 確認30_色白
rem  ふつうの場面（主人公が寝ている）
%PY% gen.py Clinic Clinic_lose_btl_e1 --model wai --redo --out 確認30_色白
rem  褐色の相手
%PY% gen.py DarkElf DarkElf_atk_m1 --model wai --redo --out 確認30_色白
rem  褐色の相手
%PY% gen.py Amazon Amazon_atk_e1 --model wai --redo --out 確認30_色白
rem  男の娘の相手
%PY% gen.py Android Android_atk_m2 --model wai --redo --out 確認30_色白
rem  体の大きい相手
%PY% gen.py Oni Oni_atk_m1 --model wai --redo --out 確認30_色白
rem  女装
%PY% gen.py Train Train_atk_e1 --model wai --redo --out 確認30_色白
rem  女装
%PY% gen.py Bride Bride_atk_m3 --model wai --redo --out 確認30_色白
rem  主人公ひとりの立ち絵
%PY% gen.py Train Train_josou --model wai --redo --out 確認30_色白
rem %PY% gen.py DarkElf DarkElf_lose_btl_e1 --model wai --redo --out 確認30_色白   （褐色の相手：予備）
rem %PY% gen.py Amazon Amazon_lose_btl_e2 --model wai --redo --out 確認30_色白   （褐色の相手：予備）
rem %PY% gen.py Maid Maid_atk_m1 --model wai --redo --out 確認30_色白   （男の娘の相手：予備）
rem %PY% gen.py Harem Harem_atk_m1 --model wai --redo --out 確認30_色白   （女装：予備）
echo.
pause
