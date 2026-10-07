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
echo  元絵の奥行き下書き（depthref）の確認撮影
echo  構図ごとに、その構図が当たる場面を選び、同じシードで「下書きあり／なし」を撮ります
echo  保存先: ComfyUI\output\構図下書き確認\ref_^<構図名^>\あり\ と なし\
echo  見るところ: 構図が下書きどおりか／受け攻めが入れ替わっていないか
echo  使えない構図は 構図下書き元 の元絵を消して 元絵から奥行き下書きを作る.bat を実行
echo ============================================
set /p N="構図ごとに何場面撮りますか（例 1）: "
if "%N%"=="" set N=1
set /p IDS="構図名を絞るならカンマ区切りで（空欄で全部）: "
if "%IDS%"=="" set IDS=ref
set /p ST="下書きの強さ（空欄＝設定どおり 0.6）: "
set /p EN="下書きを効かせる範囲（空欄＝設定どおり 0.5）: "
set OPT=
if not "%ST%"=="" set OPT=%OPT% --control-strength %ST%
if not "%EN%"=="" set OPT=%OPT% --control-end %EN%
%PY% gen.py all --model wai --control-sample %N% --control-id %IDS% %OPT%
echo.
echo 送信しました。ComfyUI の処理が終わると output\構図下書き確認\ に保存されます。
pause
