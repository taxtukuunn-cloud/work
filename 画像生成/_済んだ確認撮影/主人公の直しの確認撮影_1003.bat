@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo 主人公の筋肉・女装の衣装・髪色の直しを確かめる撮り直し 10枚（前回と同じ番号で撮るので見比べられます）
echo 保存先：ComfyUI\output\ささやき確認3
%PY% gen.py Dorm Dorm_atk_m2,Dorm_lose_btl_m2 --model wai --out ささやき確認3
%PY% gen.py Eruru Eruru_lose_btl_e3 --model wai --out ささやき確認3
%PY% gen.py Patra Patra_lose_btl_m2 --model wai --out ささやき確認3
%PY% gen.py Revue Revue_atk_m1,Revue_lose_btl_m1 --model wai --out ささやき確認3
%PY% gen.py Idol Idol_lose_onedari_m1 --model wai --out ささやき確認3
%PY% gen.py Starship Starship_atk_m2,Starship_lose_onedari_m2 --model wai --out ささやき確認3
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --out ささやき確認3
pause
