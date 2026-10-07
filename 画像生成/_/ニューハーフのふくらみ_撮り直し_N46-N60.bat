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
echo  ニューハーフの絵（股間のふくらみを足した 230件）を撮ります
echo  立ち絵・魔法カード・場面のうち、ニューハーフが服を着たまま出る絵だけ
echo  撮り済みの絵も新しく撮り直します（古い画像は消えません）
echo ============================================
set /p OK="始めますか？（y で開始）: "
if /i not "%OK%"=="y" goto end
set /p BAT="1枚につき何枚の候補を撮る？（Enterだけ＝1）: "
if "%BAT%"=="" set BAT=1
set OPT=--redo --batch %BAT%
%PY% gen.py Alchemy Alchemy_e1,Alchemy_e3,Alchemy_boss,Alchemy_atk_e1,Alchemy_atk_e3,Alchemy_lose_btl_e1,Alchemy_lose_inochi_e1,Alchemy_lose_onedari_e1,Alchemy_lose_btl_e3,Alchemy_lose_inochi_e3,Alchemy_lose_onedari_e3,Alchemy_magic_2,Alchemy_magic_5 %OPT%
%PY% gen.py Candy Candy_e1,Candy_boss,Candy_atk_e1,Candy_atk_boss,Candy_lose_btl_e1,Candy_lose_inochi_e1,Candy_lose_onedari_e1,Candy_lose_btl_boss,Candy_lose_inochi_boss,Candy_lose_onedari_boss,Candy_magic_5 %OPT%
%PY% gen.py Circus Circus_master,Circus_e2,Circus_atk_m1,Circus_atk_m2,Circus_atk_e2,Circus_lose_btl_m1,Circus_lose_inochi_m1,Circus_lose_onedari_m1,Circus_lose_btl_m2,Circus_lose_inochi_m2,Circus_lose_onedari_m2,Circus_lose_btl_e2,Circus_lose_inochi_e2,Circus_lose_onedari_e2,Circus_magic_1,Circus_magic_3,Circus_magic_4 %OPT%
%PY% gen.py Fortune Fortune_master,Fortune_e3,Fortune_atk_m1,Fortune_atk_m2,Fortune_atk_e3,Fortune_lose_btl_m1,Fortune_lose_inochi_m1,Fortune_lose_onedari_m1,Fortune_lose_btl_m2,Fortune_lose_inochi_m2,Fortune_lose_onedari_m2,Fortune_lose_btl_e3,Fortune_lose_inochi_e3,Fortune_lose_onedari_e3,Fortune_magic_4 %OPT%
%PY% gen.py GhostShip GhostShip_master,GhostShip_e2,GhostShip_atk_m1,GhostShip_atk_m2,GhostShip_atk_e2,GhostShip_lose_btl_m1,GhostShip_lose_inochi_m1,GhostShip_lose_onedari_m1,GhostShip_lose_btl_m2,GhostShip_lose_inochi_m2,GhostShip_lose_onedari_m2,GhostShip_lose_btl_e2,GhostShip_lose_inochi_e2,GhostShip_lose_onedari_e2,GhostShip_magic_1,GhostShip_magic_3,GhostShip_magic_4 %OPT%
%PY% gen.py Lingerie Lingerie_master,Lingerie_e2,Lingerie_atk_m1,Lingerie_atk_m2,Lingerie_atk_e2,Lingerie_lose_btl_m1,Lingerie_lose_inochi_m1,Lingerie_lose_onedari_m1,Lingerie_lose_btl_m2,Lingerie_lose_inochi_m2,Lingerie_lose_onedari_m2,Lingerie_lose_btl_e2,Lingerie_lose_inochi_e2,Lingerie_lose_onedari_e2,Lingerie_magic_1,Lingerie_magic_2 %OPT%
%PY% gen.py Luna Luna_e2,Luna_boss,Luna_atk_e2,Luna_atk_boss,Luna_lose_btl_e2,Luna_lose_inochi_e2,Luna_lose_onedari_e2,Luna_lose_btl_boss,Luna_lose_inochi_boss,Luna_lose_onedari_boss,Luna_magic_3,Luna_magic_5 %OPT%
%PY% gen.py Masque Masque_e1,Masque_e3,Masque_boss,Masque_atk_e1,Masque_atk_e3,Masque_lose_btl_e1,Masque_lose_inochi_e1,Masque_lose_onedari_e1,Masque_lose_btl_e3,Masque_lose_inochi_e3,Masque_lose_onedari_e3,Masque_magic_1,Masque_magic_4,Masque_magic_5 %OPT%
%PY% gen.py Office Office_e2,Office_e3,Office_boss,Office_atk_e2,Office_atk_e3,Office_lose_btl_e2,Office_lose_inochi_e2,Office_lose_onedari_e2,Office_lose_btl_e3,Office_lose_inochi_e3,Office_lose_onedari_e3,Office_magic_2,Office_magic_3,Office_magic_4 %OPT%
%PY% gen.py Oiran Oiran_e1,Oiran_e3,Oiran_boss,Oiran_atk_e1,Oiran_atk_e3,Oiran_atk_boss,Oiran_lose_btl_e1,Oiran_lose_inochi_e1,Oiran_lose_onedari_e1,Oiran_lose_btl_e3,Oiran_lose_inochi_e3,Oiran_lose_onedari_e3,Oiran_lose_btl_boss,Oiran_lose_onedari_boss,Oiran_magic_2,Oiran_magic_4 %OPT%
%PY% gen.py Police Police_e2,Police_e3,Police_boss,Police_atk_e2,Police_atk_e3,Police_lose_btl_e2,Police_lose_inochi_e2,Police_lose_onedari_e2,Police_lose_btl_e3,Police_lose_inochi_e3,Police_lose_onedari_e3,Police_magic_2,Police_magic_3 %OPT%
%PY% gen.py Revue Revue_master,Revue_e2,Revue_atk_m1,Revue_atk_m2,Revue_atk_e2,Revue_lose_btl_m1,Revue_lose_inochi_m1,Revue_lose_onedari_m1,Revue_lose_btl_m2,Revue_lose_inochi_m2,Revue_lose_onedari_m2,Revue_lose_btl_e2,Revue_lose_inochi_e2,Revue_lose_onedari_e2,Revue_magic_1,Revue_magic_4 %OPT%
%PY% gen.py ShowPub ShowPub_master,ShowPub_e2,ShowPub_e3,ShowPub_atk_m1,ShowPub_atk_m2,ShowPub_atk_e2,ShowPub_atk_e3,ShowPub_lose_btl_m1,ShowPub_lose_inochi_m1,ShowPub_lose_onedari_m1,ShowPub_lose_btl_m2,ShowPub_lose_inochi_m2,ShowPub_lose_onedari_m2,ShowPub_lose_btl_e2,ShowPub_lose_inochi_e2,ShowPub_lose_onedari_e2,ShowPub_lose_btl_e3,ShowPub_lose_inochi_e3,ShowPub_lose_onedari_e3,ShowPub_magic_1,ShowPub_magic_3,ShowPub_magic_4 %OPT%
%PY% gen.py Starship Starship_master,Starship_e2,Starship_atk_m1,Starship_atk_m2,Starship_atk_e2,Starship_lose_btl_m1,Starship_lose_inochi_m1,Starship_lose_onedari_m1,Starship_lose_btl_m2,Starship_lose_inochi_m2,Starship_lose_onedari_m2,Starship_lose_btl_e2,Starship_lose_inochi_e2,Starship_lose_onedari_e2,Starship_magic_1,Starship_magic_2 %OPT%
%PY% gen.py Studio Studio_master,Studio_e2,Studio_atk_m1,Studio_atk_m2,Studio_atk_e2,Studio_lose_btl_m1,Studio_lose_inochi_m1,Studio_lose_onedari_m1,Studio_lose_btl_m2,Studio_lose_inochi_m2,Studio_lose_onedari_m2,Studio_lose_btl_e2,Studio_lose_inochi_e2,Studio_lose_onedari_e2,Studio_magic_1,Studio_magic_2,Studio_magic_4,Studio_magic_5 %OPT%
:end
pause
