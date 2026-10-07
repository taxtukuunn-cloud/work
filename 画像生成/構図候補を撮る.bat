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
echo  構図の下書きの「元絵」候補を撮る（2026-09-30）
echo  構図LoRA（年齢の理由で止めたものは除く）と 構図候補_追加.json の構図で、
echo  大人の2人の絵を白背景で撮ります（絵柄・主人公・敵キャラの LoRA は使わない）
echo  保存先: ComfyUI\output\構図候補\^<id^>\
echo ============================================
%PY% make_pose_ref.py --list
echo.
set /p IDS="撮る構図の id をカンマ区切りで（空欄で全部）: "
set /p N="1構図あたり何枚（空欄＝4）: "
if "%N%"=="" set N=4
if "%IDS%"=="" (
  %PY% make_pose_ref.py --batch %N% --dry-run
) else (
  %PY% make_pose_ref.py --only %IDS% --batch %N% --dry-run
)
if errorlevel 1 goto end
echo.
set /p OK="この内容で撮りますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
if "%IDS%"=="" (
  %PY% make_pose_ref.py --batch %N%
) else (
  %PY% make_pose_ref.py --only %IDS% --batch %N%
)
echo.
echo 撮れたら、構図ごとによい画像を選んで 元絵を取り込む.bat にドラッグ＆ドロップしてください。
echo  （構図下書き元\^<id^>.png、2枚目から ^<id^>_2.png … の名前で自動で入ります）
echo  選ぶ目安: 腕や脚の数が正しい／2人の位置関係がはっきり／どちらも大人の体つきに見える
echo  （幼く見える絵は使わない）
:end
pause
