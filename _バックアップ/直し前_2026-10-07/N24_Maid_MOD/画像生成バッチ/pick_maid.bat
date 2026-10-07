@echo off
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
rem 候補から採用する画像を決めて output\Maid\ に上書き
rem 使い方: pick_maid.bat Maid_atk_m3 2   （output\Maid\_candidates\Maid_atk_m3_c2.png を採用）
if "%~2"=="" (
  echo 使い方: pick_maid.bat キー 番号
  echo   例: pick_maid.bat Maid_atk_m3 2
  pause
  exit /b 1
)
%PY% comfy_batch.py --pick %~1 %~2
pause
