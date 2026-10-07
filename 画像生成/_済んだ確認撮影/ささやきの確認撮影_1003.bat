@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ささやきの場面 41枚（座った主人公の後ろ・横からささやく下書きに移した場面）を確認撮影します。
echo 保存先：ComfyUI\output\ささやき確認
%PY% gen.py Cammy Cammy_lose_inochi_m3 --model wai --out ささやき確認
%PY% gen.py Circle Circle_atk_e3,Circle_lose_btl_e3,Circle_lose_inochi_e3 --model wai --out ささやき確認
%PY% gen.py CrossCafe CrossCafe_lose_btl_e3 --model wai --out ささやき確認
%PY% gen.py Dorm Dorm_atk_m2,Dorm_lose_btl_m2 --model wai --out ささやき確認
%PY% gen.py Dream Dream_lose_btl_m1 --model wai --out ささやき確認
%PY% gen.py Eruru Eruru_lose_btl_e3,Eruru_lose_inochi_e3,Eruru_lose_onedari_e3 --model wai --out ささやき確認
%PY% gen.py Esthe Esthe_atk_e3 --model wai --out ささやき確認
%PY% gen.py Fortune Fortune_atk_m1 --model wai --out ささやき確認
%PY% gen.py Idol Idol_lose_onedari_m1,Idol_lose_onedari_m3 --model wai --out ささやき確認
%PY% gen.py Inn Inn_atk_e3 --model wai --out ささやき確認
%PY% gen.py Konoha Konoha_lose_inochi_m1,Konoha_lose_btl_e1 --model wai --out ささやき確認
%PY% gen.py Lab Lab_atk_e2 --model wai --out ささやき確認
%PY% gen.py Library Library_lose_inochi_m1 --model wai --out ささやき確認
%PY% gen.py Luna Luna_atk_e2,Luna_lose_inochi_e2 --model wai --out ささやき確認
%PY% gen.py Necro Necro_lose_inochi_m3 --model wai --out ささやき確認
%PY% gen.py Neneko Neneko_lose_btl_m2 --model wai --out ささやき確認
%PY% gen.py Office Office_atk_m1 --model wai --out ささやき確認
%PY% gen.py Patra Patra_lose_btl_m2 --model wai --out ささやき確認
%PY% gen.py Pawn Pawn_atk_e1,Pawn_lose_inochi_e1 --model wai --out ささやき確認
%PY% gen.py Revue Revue_atk_m1,Revue_lose_btl_m1 --model wai --out ささやき確認
%PY% gen.py SEruru SEruru_atk_e1,SEruru_lose_inochi_e3,SEruru_lose_onedari_e3 --model wai --out ささやき確認
%PY% gen.py Starship Starship_atk_m2,Starship_lose_btl_m2,Starship_lose_inochi_m2,Starship_lose_onedari_m2 --model wai --out ささやき確認
%PY% gen.py Tea Tea_lose_inochi_e2 --model wai --out ささやき確認
%PY% gen.py Tengu Tengu_atk_e3,Tengu_lose_inochi_e2,Tengu_lose_btl_e3 --model wai --out ささやき確認
pause
