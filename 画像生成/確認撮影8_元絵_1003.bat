@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo 新しい元絵の下書き 23種類を1場面ずつ確認撮影します → output\確認8_元絵
%PY% gen.py Alraune Alraune_lose_onedari_e3,Alraune_lose_inochi_e3 --model wai --out 確認8_元絵
%PY% gen.py Neneko Neneko_lose_btl_e3 --model wai --out 確認8_元絵
%PY% gen.py DarkElf DarkElf_lose_btl_m1 --model wai --out 確認8_元絵
%PY% gen.py Musashi Musashi_atk_m2,Musashi_atk_m3 --model wai --out 確認8_元絵
%PY% gen.py Perfume Perfume_lose_btl_m3 --model wai --out 確認8_元絵
%PY% gen.py Patra Patra_atk_m1 --model wai --out 確認8_元絵
%PY% gen.py Clock Clock_lose_onedari_m3 --model wai --out 確認8_元絵
%PY% gen.py Auction Auction_lose_btl_e3,Auction_lose_onedari_m2 --model wai --out 確認8_元絵
%PY% gen.py Bride Bride_lose_inochi_m3 --model wai --out 確認8_元絵
%PY% gen.py Candy Candy_atk_m2,Candy_lose_inochi_boss --model wai --out 確認8_元絵
%PY% gen.py Eiraira Eiraira_atk_boss --model wai --out 確認8_元絵
%PY% gen.py Heels Heels_lose_inochi_boss --model wai --out 確認8_元絵
%PY% gen.py Atelier Atelier_atk_e2 --model wai --out 確認8_元絵
%PY% gen.py Alchemy Alchemy_atk_boss --model wai --out 確認8_元絵
%PY% gen.py Casino Casino_lose_onedari_boss --model wai --out 確認8_元絵
%PY% gen.py Esthe Esthe_lose_inochi_boss --model wai --out 確認8_元絵
%PY% gen.py Angel Angel_lose_inochi_m2 --model wai --out 確認8_元絵
%PY% gen.py Centaur Centaur_lose_inochi_boss --model wai --out 確認8_元絵
%PY% gen.py Labyrinth Labyrinth_atk_m2 --model wai --out 確認8_元絵
pause
