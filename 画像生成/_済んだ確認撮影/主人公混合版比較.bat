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
echo  絵柄混合の主人公LoRA（sdduel_hero_xl_mix）のエポック比較（2026-09-30）
echo  選んだ絵柄ごとに、同じシードで2枚ずつ:
echo   none = 主人公LoRAなし ／ e04 e06 e08 e10 = 各エポック
echo  1つのLoRAで全部の絵柄に使うので、絵柄を2～3個選んで見比べてください
echo  保存先: ComfyUI\output\^<MOD^>_主人公混合比較\^<絵柄^>\^<エポック^>\
echo ============================================
%PY% gen.py --style-list
echo.
set /p STYLES="絵柄名をカンマ区切りで（例 ATRex,GEN,Bose）: "
if "%STYLES%"=="" goto end
set /p MOD="MODコード（例 Lamia）: "
if "%MOD%"=="" goto end
set /p KEY="画像の名前（2人の場面がおすすめ 例 Lamia_atk_m1）: "
if "%KEY%"=="" goto end
set /p ST="主人公LoRAの強さ（Enterだけ＝0.3・2人の場面の既定）: "
if "%ST%"=="" set ST=0.3
set SEED=%RANDOM%%RANDOM%
set H=sdduel_hero_xl_mix
set D=%MOD%_主人公混合比較
for %%S in (%STYLES%) do call :one %%S
echo.
echo 送りました。数分～十数分で ComfyUI\output\%D%\ に保存されます。
echo  見るところ: 紺の短髪・水色の目・細身の大人の顔になっているか／相手の顔に主人公が混ざっていないか／絵柄が崩れていないか
echo 2人の場面は今 6エポック・0.3。ほかが良ければ、そのエポック名を Claude に伝えてください。
goto end
:one
set O=--model wai --style %1 --no-hero --seed %SEED% --batch 2
%PY% gen.py %MOD% %KEY% %O% --out %D%/%1/none
%PY% gen.py %MOD% %KEY% %O% --out %D%/%1/e04 --add-lora "%H%-000004:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/%1/e06 --add-lora "%H%-000006:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/%1/e08 --add-lora "%H%-000008:%ST%:sdduel_hero:hero"
%PY% gen.py %MOD% %KEY% %O% --out %D%/%1/e10 --add-lora "%H%:%ST%:sdduel_hero:hero"
exit /b 0
:end
pause
