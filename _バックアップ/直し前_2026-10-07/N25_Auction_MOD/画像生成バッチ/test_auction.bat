@echo off
chcp 65001 >nul
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
rem 試し撮り：全52枚の前に3枚だけ（立ち絵1・技CG1・敗北1）を候補2枚ずつ出して、LoRAの絵柄と主人公の体格・2人の取り違えを確認する
%PY% comfy_batch.py Auction_master --random --batch 2
%PY% comfy_batch.py Auction_atk_m1 --random --batch 2
%PY% comfy_batch.py Auction_lose_btl_e2 --random --batch 2
echo 出力: output\Auction\_candidates\  問題なければ gen_auction_all.bat を実行
pause
