@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo [1/2] 女装の衣装の直し（6枚）→ output\ささやき確認4
%PY% gen.py Dorm Dorm_atk_m2,Dorm_lose_btl_m2 --model wai --out ささやき確認4
%PY% gen.py Revue Revue_atk_m1,Revue_lose_btl_m1 --model wai --out ささやき確認4
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --out ささやき確認4
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --out ささやき確認4
echo [2/2] 髪色の直し：主人公LoRAを主人公の範囲だけに強さ0.8でかける（4枚）→ output\ささやき確認4_髪
%PY% gen.py Starship Starship_atk_m2,Starship_lose_onedari_m2 --model wai --hero-hook-strength 0.8 --out ささやき確認4_髪
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --hero-hook-strength 0.8 --out ささやき確認4_髪
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --hero-hook-strength 0.8 --out ささやき確認4_髪
pause
