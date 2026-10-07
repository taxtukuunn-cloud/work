@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo 髪色の原因の切り分け：顔の描き直しを外して撮る（3枚）→ output\確認6_顔描き直しなし
%PY% gen.py Starship Starship_atk_m2,Starship_lose_onedari_m2 --model wai --no-face-detail --out 確認6_顔描き直しなし
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --no-face-detail --out 確認6_顔描き直しなし
pause
