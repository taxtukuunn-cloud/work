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
echo  構図LoRAの比較（LoRAごとに場面を1件、同じシードで「あり／なし」を1枚ずつ）
echo  保存先: ComfyUI\output\構図LoRA比較\^<id^>\あり\ と なし\
echo  見るところ: 構図（体位・位置関係）が場面の文に近づいたか／絵柄・顔が崩れていないか
echo  強すぎる・弱すぎる LoRA は model.json の pose_loras の strength を直してください
echo ============================================
%PY% gen.py all --model wai --pose-sample 1
echo.
echo 送信しました。ComfyUI の処理が終わると output\構図LoRA比較\ に保存されます。
pause
