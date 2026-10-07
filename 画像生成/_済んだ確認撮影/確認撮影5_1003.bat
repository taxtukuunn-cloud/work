@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo [1/3] 髪色：画面全体の文から相手の髪色を抜く（6枚）→ output\確認5_髪
%PY% gen.py Starship Starship_atk_m2,Starship_lose_onedari_m2 --model wai --out 確認5_髪
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --out 確認5_髪
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --out 確認5_髪
%PY% gen.py Military Military_lose_btl_e3 --model wai --out 確認5_髪
%PY% gen.py Beach Beach_lose_btl_e1 --model wai --out 確認5_髪
echo [2/3] 女装の衣装：下書きを効かせる範囲を短くして、服の形が出やすいか試す（4枚）→ output\確認5_衣装
%PY% gen.py Dorm Dorm_atk_m2 --model wai --ref-end 0.35 --out 確認5_衣装
%PY% gen.py Revue Revue_atk_m1 --model wai --ref-end 0.35 --out 確認5_衣装
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --ref-end 0.35 --out 確認5_衣装
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --ref-end 0.35 --out 確認5_衣装
echo [3/3] 相手が複数の場面：崩れた下書きを外した撮り直し（5枚）→ output\確認5_複数
%PY% gen.py Heels Heels_lose_inochi_boss --model wai --out 確認5_複数
%PY% gen.py Twins Twins_lose_inochi_m1,Twins_lose_inochi_m2,Twins_lose_inochi_m3,Twins_lose_onedari_m2 --model wai --out 確認5_複数
pause
