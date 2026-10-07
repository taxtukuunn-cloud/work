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
echo  本編の絵柄LoRA（SDXL版 sdduel_style_xl）のエポック比較
echo  WAI・アニメ調LoRAはそのまま、同じシードで2枚ずつ:
echo   none = 絵柄LoRAなし
echo   e02 / e04 / e06 / e08 / e10 = 各エポック（強さは下で入力）
echo  保存先: ComfyUI\output\^<MODコード^>_絵柄XL比較\
echo ============================================
set /p MOD="MODコード（例 Knight）: "
set /p KEY="画像の名前（例 Knight_master）: "
if "%KEY%"=="" goto end
set /p ST="絵柄LoRAの強さ（Enterだけ＝0.6）: "
if "%ST%"=="" set ST=0.6
set SEED=%RANDOM%%RANDOM%
set O=--model wai --seed %SEED% --batch 2
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/none
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/e02 --add-lora "sdduel_style_xl-000002:%ST%:sdduel style"
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/e04 --add-lora "sdduel_style_xl-000004:%ST%:sdduel style"
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/e06 --add-lora "sdduel_style_xl-000006:%ST%:sdduel style"
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/e08 --add-lora "sdduel_style_xl-000008:%ST%:sdduel style"
%PY% gen.py %MOD% %KEY% %O% --out %MOD%_絵柄XL比較/e10 --add-lora "sdduel_style_xl:%ST%:sdduel style"
echo.
echo 12枚を送りました。数分で ComfyUI\output\%MOD%_絵柄XL比較\ に保存されます。
echo 良かったものを model.json の sdduel_style_xl の行に書き（lora_name・strength・clip_strength）、enabled を true にしてください。
:end
pause
