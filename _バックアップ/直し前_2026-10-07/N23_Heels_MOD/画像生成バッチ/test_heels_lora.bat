@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
call backup_heels.bat
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  echo 起動を待っています（最大5分）...
  %PY% wait_comfy.py
)
rem 試し撮り：4枚×候補2枚。完成画像は上書きせず output\Heels\_candidates に保存する
%PY% comfy_batch.py Heels_onanie_master --random --batch 2
%PY% comfy_batch.py Heels_atk_m1 --random --batch 2
%PY% comfy_batch.py Heels_lose_btl_m3 --random --batch 2
%PY% comfy_batch.py Heels_master --random --batch 2
echo.
echo 試し撮りが終わりました。output\Heels\_candidates の _c1 _c2 を見てください。
echo 主人公が幼く見える・体格が崩れる場合は、強さを下げて： test_heels_lora.bat の代わりに
echo   run_heels.bat Heels_onanie_master --random --batch 2 --lora-strength 0.5
pause
