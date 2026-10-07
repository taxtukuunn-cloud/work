@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
curl -s -o nul http://127.0.0.1:8188/ && goto ready
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
goto wait
:ready
echo 翔鶴・フッド・アストラ・ローマ・ヘルム・インディペンデンス・ブレマートン・オリヴィエの確認撮影（立ち絵と敗北1枚ずつ・16枚）
%PY% gen.py Tengu Tengu_master,Tengu_lose_btl_m1 --model wai --out キャラLoRA確認4\Tengu
%PY% gen.py Bride Bride_boss,Bride_lose_btl_boss --model wai --out キャラLoRA確認4\Bride
%PY% gen.py Revue Revue_master,Revue_lose_btl_m1 --model wai --out キャラLoRA確認4\Revue
%PY% gen.py Studio Studio_e3,Studio_lose_btl_e3 --model wai --out キャラLoRA確認4\Studio
%PY% gen.py Starship Starship_master,Starship_lose_btl_m1 --model wai --out キャラLoRA確認4\Starship
%PY% gen.py CrossCafe CrossCafe_e3,CrossCafe_lose_btl_e3 --model wai --out キャラLoRA確認4\CrossCafe
%PY% gen.py Eruru Eruru_e1,Eruru_lose_btl_e1 --model wai --out キャラLoRA確認4\Eruru
%PY% gen.py Angel Angel_boss,Angel_lose_btl_boss --model wai --out キャラLoRA確認4\Angel
echo.
echo 送信しました。終わったら「一覧画像を作る.bat」を実行して教えてください。
pause
