@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
set "GEN=%USERPROFILE%\Downloads\MOD\画像生成"
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
echo  絵柄別の主人公LoRA のエポック比較
echo  その絵柄で、同じシードで2枚ずつ:
echo   none = 主人公LoRAなし ／ e02 e04 e06 e08 e10 = 各エポック
echo  主人公がひとりで出る絵（オナニー・立ち絵）がおすすめ（例 Lamia_onanie_m1）
echo  保存先: ComfyUI\output\^<MODコード^>_主人公比較_^<絵柄^>\
echo ============================================
set /p S="絵柄名（例 ATRex）: "
if "%S%"=="" goto end
set /p MOD="MODコード（例 Lamia）: "
set /p KEY="画像の名前（例 Lamia_onanie_m1）: "
if "%KEY%"=="" goto end
set /p ST="主人公LoRAの強さ（Enterだけ＝0.8）: "
if "%ST%"=="" set ST=0.8
set SEED=%RANDOM%%RANDOM%
set H=sdduel_hero_xl_%S%
set O=--model wai --style %S% --no-hero --seed %SEED% --batch 2
set D=%MOD%_主人公比較_%S%
%PY% gen.py %MOD% %KEY% %O% --out %D%/none
%PY% gen.py %MOD% %KEY% %O% --out %D%/e02 --add-lora "%H%-000002:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/e04 --add-lora "%H%-000004:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/e06 --add-lora "%H%-000006:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/e08 --add-lora "%H%-000008:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/e10 --add-lora "%H%:%ST%:sdduel_hero:hero"
echo.
echo 12枚を送りました。数分で ComfyUI\output\%D%\ に保存されます。
echo 8エポック目以外が良ければ、model.json の mod_style の styles に
echo   "%S%": {"hero_lora": "%H%-000006.safetensors", "hero_strength": 0.8}
echo のように書いてください（書き方は README_MODごとの絵柄.txt）。
:end
pause
