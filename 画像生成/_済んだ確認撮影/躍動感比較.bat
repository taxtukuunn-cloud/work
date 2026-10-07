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
echo  躍動感の比べ撮り（2026-10-02・同じシードで2枚ずつ）
echo   a_今         下書き 0.6 / 0.5   動きの語なし   元絵は今のまま
echo   b_弱め       下書き 0.5 / 0.4   動きの語あり   元絵は今のまま
echo   c_もっと弱め 下書き 0.45 / 0.35 動きの語あり   元絵は今のまま
echo   d_カメラ違い 下書き 0.5 / 0.4   動きの語あり   カメラ違いの元絵（_low/_dutch/_fore/_high）だけ
echo  ※ d は、カメラ違いの元絵を撮って下書きを作ったあとでないと、3D の下書きか下書きなしになります
echo  ※ model.json の ref_control は書き換えません（数値はこの撮影だけ）
echo  保存先: ComfyUI\output\^<MOD^>_躍動感比較\^<名前^>\
echo ============================================
set /p MOD="MODコード（例 Lamia）: "
if "%MOD%"=="" goto end
echo 画像の名前をカンマ区切りで（lose_btl と atk を数枚。例 Lamia_lose_btl_e1,Lamia_atk_m1,Lamia_atk_e2）
set /p KEY="画像の名前: "
if "%KEY%"=="" goto end
set SEED=%RANDOM%%RANDOM%
set O=--model wai --seed %SEED% --batch 2
set D=%MOD%_躍動感比較
%PY% gen.py %MOD% %KEY% %O% --out %D%/a_今 --ref-strength 0.6 --ref-end 0.5 --no-motion
%PY% gen.py %MOD% %KEY% %O% --out %D%/b_弱め --ref-strength 0.5 --ref-end 0.4
%PY% gen.py %MOD% %KEY% %O% --out %D%/c_もっと弱め --ref-strength 0.45 --ref-end 0.35
%PY% gen.py %MOD% %KEY% %O% --out %D%/d_カメラ違い --ref-strength 0.5 --ref-end 0.4 --ref-cam
echo.
echo 4条件を送りました（シード %SEED%）。
echo ComfyUI の処理が全部終わってから、何かキーを押すと条件ごとの一覧画像を作ります。
pause
set "OUTD=%COMFY_DIR%\ComfyUI\output\%D%"
for %%N in (a_今 b_弱め c_もっと弱め d_カメラ違い) do (
  if exist "%OUTD%\%%N" %PY% 一覧画像を作る.py "%OUTD%\%%N"
)
echo.
echo 一覧は %OUTD%\^<名前^>\_一覧\ にあります。その jpg を Claude に渡してください。
echo 見るところ: (1)動きが出たか (2)役が逆になっていないか (3)3人目が出ていないか
echo            (4)主人公が幼く・ごつく見えないか (5)絵柄LoRAの色が光の語でくずれていないか
:end
pause
