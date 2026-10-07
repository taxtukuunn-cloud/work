@echo off
chcp 65001 >nul
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
if not exist "%USERPROFILE%\Downloads\Lora用\lora_settings.json" (
  echo [注意] Downloads\Lora用\lora_settings.json が見つかりません。LoRAなしで生成されます。
  pause
  exit /b
)
call backup_before_lora_vampire.bat
rem ComfyUI が起動していなければ起動する
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  %PY% wait_comfy.py
)
rem 試し撮り：3場面×2枚。c1＝今の画像と同じシード（LoRAの有無だけの比べ）、c2＝ランダム
rem 採用画像は上書きしない（output\Vampire\_candidates に出る）
%PY% comfy_batch.py Vampire_master --batch 2
%PY% comfy_batch.py Vampire_atk_m1 --batch 2
%PY% comfy_batch.py Vampire_lose_btl_e1 --batch 2
echo.
echo 試し撮り完了。output\Vampire\_candidates の *_c1.png と、output\Vampire の同名画像を比べてください。
echo 主人公が小柄・華奢のままか（150cm・非筋肉質）、紺の短髪・顔なしが保たれているかを確認。
pause
