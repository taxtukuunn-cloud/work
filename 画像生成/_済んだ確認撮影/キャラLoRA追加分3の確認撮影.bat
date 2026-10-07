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
echo ============================================
echo  追加した53体の確認撮影（立ち絵と敗北イベント1枚ずつ）
echo  保存先: output\キャラLoRA確認\MOD名\
echo ============================================
%PY% gen.py Vampire Vampire_master,Vampire_lose_btl_m1 --model wai --out キャラLoRA確認\Vampire
%PY% gen.py Necro Necro_master,Necro_lose_btl_m1,Necro_e2,Necro_lose_btl_e2 --model wai --out キャラLoRA確認\Necro
%PY% gen.py Medusa Medusa_master,Medusa_lose_btl_m1 --model wai --out キャラLoRA確認\Medusa
%PY% gen.py Mirror Mirror_master,Mirror_lose_btl_m1 --model wai --out キャラLoRA確認\Mirror
%PY% gen.py Lab Lab_master,Lab_lose_btl_m1 --model wai --out キャラLoRA確認\Lab
%PY% gen.py Train Train_master,Train_lose_btl_m1 --model wai --out キャラLoRA確認\Train
%PY% gen.py Idol Idol_master,Idol_lose_btl_m1 --model wai --out キャラLoRA確認\Idol
%PY% gen.py Salon Salon_boss,Salon_lose_btl_boss --model wai --out キャラLoRA確認\Salon
%PY% gen.py Slime Slime_boss,Slime_lose_btl_boss --model wai --out キャラLoRA確認\Slime
%PY% gen.py SEruru SEruru_boss,SEruru_lose_btl_boss --model wai --out キャラLoRA確認\SEruru
%PY% gen.py Inn Inn_master,Inn_lose_btl_m1 --model wai --out キャラLoRA確認\Inn
%PY% gen.py Queen Queen_e2,Queen_lose_btl_e2 --model wai --out キャラLoRA確認\Queen
%PY% gen.py Sky Sky_master,Sky_lose_btl_m1,Sky_e3,Sky_lose_btl_e3 --model wai --out キャラLoRA確認\Sky
%PY% gen.py Alraune Alraune_master,Alraune_lose_btl_m1 --model wai --out キャラLoRA確認\Alraune
%PY% gen.py Tea Tea_master,Tea_lose_btl_m1 --model wai --out キャラLoRA確認\Tea
%PY% gen.py Oni Oni_master,Oni_lose_btl_m1 --model wai --out キャラLoRA確認\Oni
%PY% gen.py Onsen Onsen_master,Onsen_lose_btl_m1 --model wai --out キャラLoRA確認\Onsen
%PY% gen.py Dorm Dorm_boss,Dorm_lose_btl_boss --model wai --out キャラLoRA確認\Dorm
%PY% gen.py Esthe Esthe_master,Esthe_lose_btl_m1 --model wai --out キャラLoRA確認\Esthe
%PY% gen.py Yatsume Yatsume_master,Yatsume_lose_btl_m1,Yatsume_e3,Yatsume_lose_btl_e3 --model wai --out キャラLoRA確認\Yatsume
%PY% gen.py Prison Prison_e1,Prison_lose_btl_e1 --model wai --out キャラLoRA確認\Prison
%PY% gen.py Valkyrie Valkyrie_e3,Valkyrie_lose_btl_e3,Valkyrie_boss,Valkyrie_lose_btl_boss --model wai --out キャラLoRA確認\Valkyrie
%PY% gen.py Snow Snow_boss,Snow_lose_btl_boss --model wai --out キャラLoRA確認\Snow
%PY% gen.py Beach Beach_master,Beach_lose_btl_m1,Beach_e3,Beach_lose_btl_e3 --model wai --out キャラLoRA確認\Beach
%PY% gen.py Clinic Clinic_e2,Clinic_lose_btl_e2 --model wai --out キャラLoRA確認\Clinic
%PY% gen.py Dream Dream_master,Dream_lose_btl_m1 --model wai --out キャラLoRA確認\Dream
%PY% gen.py Starship Starship_e3,Starship_lose_btl_e3 --model wai --out キャラLoRA確認\Starship
%PY% gen.py Mimic Mimic_master,Mimic_lose_btl_m1 --model wai --out キャラLoRA確認\Mimic
%PY% gen.py GhostShip GhostShip_boss,GhostShip_lose_btl_boss --model wai --out キャラLoRA確認\GhostShip
%PY% gen.py Octa Octa_boss,Octa_lose_btl_boss --model wai --out キャラLoRA確認\Octa
%PY% gen.py Sphinx Sphinx_boss,Sphinx_lose_btl_boss --model wai --out キャラLoRA確認\Sphinx
%PY% gen.py Fortune Fortune_e1,Fortune_lose_btl_e1,Fortune_e2,Fortune_lose_btl_e2,Fortune_boss,Fortune_lose_btl_boss --model wai --out キャラLoRA確認\Fortune
%PY% gen.py General General_e3,General_lose_btl_e3 --model wai --out キャラLoRA確認\General
%PY% gen.py Library Library_boss,Library_lose_btl_boss --model wai --out キャラLoRA確認\Library
%PY% gen.py Heels Heels_e3,Heels_lose_btl_e3 --model wai --out キャラLoRA確認\Heels
%PY% gen.py Kiss Kiss_boss,Kiss_lose_btl_boss --model wai --out キャラLoRA確認\Kiss
%PY% gen.py Office Office_e1,Office_lose_btl_e1 --model wai --out キャラLoRA確認\Office
%PY% gen.py Military Military_e3,Military_lose_btl_e3 --model wai --out キャラLoRA確認\Military
%PY% gen.py Revue Revue_boss,Revue_lose_btl_boss --model wai --out キャラLoRA確認\Revue
%PY% gen.py Gemini Gemini_e3,Gemini_lose_btl_e3 --model wai --out キャラLoRA確認\Gemini
%PY% gen.py CrossCafe CrossCafe_boss,CrossCafe_lose_btl_boss --model wai --out キャラLoRA確認\CrossCafe
%PY% gen.py Atelier Atelier_master,Atelier_lose_btl_m1 --model wai --out キャラLoRA確認\Atelier
%PY% gen.py Perfume Perfume_master,Perfume_lose_btl_m1 --model wai --out キャラLoRA確認\Perfume
%PY% gen.py Inmon Inmon_master,Inmon_lose_btl_m1 --model wai --out キャラLoRA確認\Inmon
%PY% gen.py Amazon Amazon_master,Amazon_lose_btl_m1,Amazon_boss,Amazon_lose_btl_boss --model wai --out キャラLoRA確認\Amazon
echo.
echo 送信しました。終わったら教えてください。
pause
