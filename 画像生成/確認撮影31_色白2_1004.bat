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
echo  確認撮影31：全裸の主人公に服が付く・肌が青白くなる、の対策を確かめる（4枚）
rem  ※撮らない場面は rem で残してあります。
rem  全裸のはずが白いスーツになった場面
%PY% gen.py Police Police_atk_e1 --model wai --redo --out 確認31_色白2
rem  服を着て肌が青白くなった場面
%PY% gen.py DarkElf DarkElf_atk_m1 --model wai --redo --out 確認31_色白2
rem  褐色の相手：別の場面
%PY% gen.py DarkElf DarkElf_atk_e1 --model wai --redo --out 確認31_色白2
rem  肌の色の比較用
%PY% gen.py Clinic Clinic_lose_btl_e1 --model wai --redo --out 確認31_色白2
rem %PY% gen.py Amazon Amazon_atk_e1 --model wai --redo --out 確認31_色白2   （確認30で問題なし）
rem %PY% gen.py Oni Oni_atk_m1 --model wai --redo --out 確認31_色白2   （確認30で問題なし）
rem %PY% gen.py Train Train_atk_e1 --model wai --redo --out 確認31_色白2   （確認30で問題なし）
rem %PY% gen.py Bride Bride_atk_m3 --model wai --redo --out 確認31_色白2   （確認30で問題なし）
rem %PY% gen.py Android Android_atk_m2 --model wai --redo --out 確認31_色白2   （主人公が服を着る場面なので今回の対策の対象外）
echo.
pause
