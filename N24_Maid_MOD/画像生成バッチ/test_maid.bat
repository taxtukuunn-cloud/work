@echo off
cd /d "%~dp0"
set COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable
set PY="%COMFY%\python_embeded\python.exe"
if not exist %PY% set PY=python
%PY% -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8188/system_stats',timeout=3)" >nul 2>nul
if errorlevel 1 (
  echo ComfyUI を起動します...
  start "ComfyUI" /D "%COMFY%" "%COMFY%\run_nvidia_gpu.bat"
  %PY% wait_comfy.py
)
rem 本番の前の試し撮り：主な5枚を2候補ずつ output\Maid\_candidates\ に作る（本番の画像は上書きしない）
rem c1 は本番と同じシード（本番でこの絵になる）、c2 は別シード
rem 見るところ：主人公が小柄・筋肉なし・紺髪で目隠れか／責め手の胸が平らか／2人の取り違えがないか
for %%K in (Maid_master Maid_lose_btl_m1 Maid_atk_m3 Maid_lose_btl_e2 Maid_onanie_master) do (
  %PY% comfy_batch.py %%K --batch 2
)
echo.
echo 試し撮り完了： output\Maid\_candidates\ を確認してください
echo 体格が崩れていたら run_maid.bat Maid_lose_btl_m1 --batch 2 --lora-strength 0.5 で比べられます
pause
