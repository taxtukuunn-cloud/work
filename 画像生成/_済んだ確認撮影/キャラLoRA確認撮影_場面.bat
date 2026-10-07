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
echo  キャラLoRAの場面の確認撮影（髪色を合わせた版・161枚）
echo  当てた全員の敗北イベント1枚 と、見た目を直した9人の立ち絵
echo  保存先: output\キャラLoRA確認3\MOD名\
echo  終わったら 一覧画像を作る.bat を実行してください
echo ============================================
%PY% gen.py Alchemy Alchemy_lose_btl_m1 --model wai --out キャラLoRA確認3\Alchemy
%PY% gen.py Alraune Alraune_lose_btl_m1 --model wai --out キャラLoRA確認3\Alraune
%PY% gen.py Amazon Amazon_lose_btl_e1,Amazon_lose_btl_m1,Amazon_lose_btl_boss --model wai --out キャラLoRA確認3\Amazon
%PY% gen.py Angel Angel_lose_btl_m1 --model wai --out キャラLoRA確認3\Angel
%PY% gen.py Atelier Atelier_lose_btl_m1 --model wai --out キャラLoRA確認3\Atelier
%PY% gen.py Beach Beach_lose_btl_e1,Beach_lose_btl_m1,Beach_lose_btl_e3 --model wai --out キャラLoRA確認3\Beach
%PY% gen.py Bride Bride_lose_btl_m1 --model wai --out キャラLoRA確認3\Bride
%PY% gen.py Cammy Cammy_lose_btl_m1,Cammy_lose_btl_e1,Cammy_lose_btl_e2,Cammy_lose_btl_e3 --model wai --out キャラLoRA確認3\Cammy
%PY% gen.py Candy Candy_lose_btl_m1 --model wai --out キャラLoRA確認3\Candy
%PY% gen.py Casino Casino_lose_btl_m1,Casino_lose_btl_e2,Casino_lose_btl_boss --model wai --out キャラLoRA確認3\Casino
%PY% gen.py Centaur Centaur_lose_btl_boss --model wai --out キャラLoRA確認3\Centaur
%PY% gen.py Circus Circus_lose_btl_e3 --model wai --out キャラLoRA確認3\Circus
%PY% gen.py Clinic Clinic_lose_btl_m1,Clinic_lose_btl_e1,Clinic_lose_btl_e2,Clinic_lose_btl_e3 --model wai --out キャラLoRA確認3\Clinic
%PY% gen.py Clock Clock_lose_btl_e1 --model wai --out キャラLoRA確認3\Clock
%PY% gen.py CrossCafe CrossCafe_lose_btl_boss --model wai --out キャラLoRA確認3\CrossCafe
%PY% gen.py DarkElf DarkElf_e2,DarkElf_lose_btl_e2 --model wai --out キャラLoRA確認3\DarkElf
%PY% gen.py Dorm Dorm_lose_btl_boss --model wai --out キャラLoRA確認3\Dorm
%PY% gen.py Dragon Dragon_lose_btl_m1,Dragon_boss,Dragon_lose_btl_boss --model wai --out キャラLoRA確認3\Dragon
%PY% gen.py Dream Dream_lose_btl_e2,Dream_lose_btl_boss,Dream_lose_btl_m1 --model wai --out キャラLoRA確認3\Dream
%PY% gen.py Eiraira Eiraira_lose_btl_e3 --model wai --out キャラLoRA確認3\Eiraira
%PY% gen.py Eruru Eruru_lose_btl_boss --model wai --out キャラLoRA確認3\Eruru
%PY% gen.py Esthe Esthe_lose_btl_m1 --model wai --out キャラLoRA確認3\Esthe
%PY% gen.py Exam Exam_lose_btl_e1,Exam_lose_btl_e2,Exam_lose_btl_boss --model wai --out キャラLoRA確認3\Exam
%PY% gen.py Fortune Fortune_lose_btl_e1,Fortune_lose_btl_e2,Fortune_lose_btl_boss --model wai --out キャラLoRA確認3\Fortune
%PY% gen.py Gemini Gemini_lose_btl_e3 --model wai --out キャラLoRA確認3\Gemini
%PY% gen.py General General_lose_btl_m1,General_lose_btl_e1,General_lose_btl_boss,General_lose_btl_e3 --model wai --out キャラLoRA確認3\General
%PY% gen.py GhostShip GhostShip_lose_btl_boss --model wai --out キャラLoRA確認3\GhostShip
%PY% gen.py Harem Harem_lose_btl_m1,Harem_lose_btl_e2 --model wai --out キャラLoRA確認3\Harem
%PY% gen.py Heels Heels_lose_btl_m1,Heels_lose_btl_e1,Heels_lose_btl_boss,Heels_lose_btl_e3,Heels_lose_btl_e2 --model wai --out キャラLoRA確認3\Heels
%PY% gen.py Idol Idol_master,Idol_lose_btl_m1 --model wai --out キャラLoRA確認3\Idol
%PY% gen.py Inmon Inmon_lose_btl_boss,Inmon_lose_btl_m1 --model wai --out キャラLoRA確認3\Inmon
%PY% gen.py Inn Inn_boss,Inn_lose_btl_boss,Inn_lose_btl_m1 --model wai --out キャラLoRA確認3\Inn
%PY% gen.py Kiss Kiss_lose_btl_m1,Kiss_lose_btl_boss,Kiss_lose_btl_e2 --model wai --out キャラLoRA確認3\Kiss
%PY% gen.py Konoha Konoha_lose_btl_m1,Konoha_lose_btl_e2,Konoha_lose_btl_boss --model wai --out キャラLoRA確認3\Konoha
%PY% gen.py Lab Lab_lose_btl_m1,Lab_lose_btl_e2,Lab_lose_btl_e3 --model wai --out キャラLoRA確認3\Lab
%PY% gen.py Library Library_lose_btl_m1,Library_lose_btl_boss --model wai --out キャラLoRA確認3\Library
%PY% gen.py Lingerie Lingerie_lose_btl_boss --model wai --out キャラLoRA確認3\Lingerie
%PY% gen.py Luna Luna_lose_btl_m1 --model wai --out キャラLoRA確認3\Luna
%PY% gen.py Masque Masque_lose_btl_m1 --model wai --out キャラLoRA確認3\Masque
%PY% gen.py Medusa Medusa_lose_btl_m1 --model wai --out キャラLoRA確認3\Medusa
%PY% gen.py Military Military_lose_btl_m1,Military_lose_btl_e3,Military_lose_btl_e1 --model wai --out キャラLoRA確認3\Military
%PY% gen.py Mimic Mimic_lose_btl_m1 --model wai --out キャラLoRA確認3\Mimic
%PY% gen.py Mirror Mirror_lose_btl_boss,Mirror_lose_btl_m1 --model wai --out キャラLoRA確認3\Mirror
%PY% gen.py Musashi Musashi_lose_btl_m1 --model wai --out キャラLoRA確認3\Musashi
%PY% gen.py Necro Necro_lose_btl_m1,Necro_lose_btl_e2 --model wai --out キャラLoRA確認3\Necro
%PY% gen.py Neneko Neneko_lose_btl_e2 --model wai --out キャラLoRA確認3\Neneko
%PY% gen.py Octa Octa_lose_btl_boss --model wai --out キャラLoRA確認3\Octa
%PY% gen.py Office Office_lose_btl_m1,Office_lose_btl_e1 --model wai --out キャラLoRA確認3\Office
%PY% gen.py Oiran Oiran_master,Oiran_lose_btl_m1 --model wai --out キャラLoRA確認3\Oiran
%PY% gen.py Oni Oni_lose_btl_m1 --model wai --out キャラLoRA確認3\Oni
%PY% gen.py Onsen Onsen_lose_btl_m1 --model wai --out キャラLoRA確認3\Onsen
%PY% gen.py Patra Patra_master,Patra_lose_btl_m1,Patra_lose_btl_e1,Patra_lose_btl_e2 --model wai --out キャラLoRA確認3\Patra
%PY% gen.py Pawn Pawn_lose_btl_m1 --model wai --out キャラLoRA確認3\Pawn
%PY% gen.py Perfume Perfume_lose_btl_m1 --model wai --out キャラLoRA確認3\Perfume
%PY% gen.py Police Police_lose_btl_m1 --model wai --out キャラLoRA確認3\Police
%PY% gen.py Prison Prison_lose_btl_e3,Prison_lose_btl_boss,Prison_lose_btl_m1,Prison_lose_btl_e1 --model wai --out キャラLoRA確認3\Prison
%PY% gen.py Puppet Puppet_lose_btl_m1 --model wai --out キャラLoRA確認3\Puppet
%PY% gen.py Queen Queen_lose_btl_e1,Queen_lose_btl_boss,Queen_lose_btl_e2 --model wai --out キャラLoRA確認3\Queen
%PY% gen.py Ranch Ranch_lose_btl_boss --model wai --out キャラLoRA確認3\Ranch
%PY% gen.py Revue Revue_lose_btl_e1,Revue_lose_btl_boss --model wai --out キャラLoRA確認3\Revue
%PY% gen.py SEruru SEruru_lose_btl_boss --model wai --out キャラLoRA確認3\SEruru
%PY% gen.py Salon Salon_lose_btl_boss --model wai --out キャラLoRA確認3\Salon
%PY% gen.py ShowPub ShowPub_lose_btl_e1,ShowPub_lose_btl_boss --model wai --out キャラLoRA確認3\ShowPub
%PY% gen.py Shrine Shrine_lose_btl_e3 --model wai --out キャラLoRA確認3\Shrine
%PY% gen.py Sister Sister_lose_btl_m1,Sister_lose_btl_boss --model wai --out キャラLoRA確認3\Sister
%PY% gen.py Sky Sky_lose_btl_m1,Sky_lose_btl_e3,Sky_lose_btl_e1 --model wai --out キャラLoRA確認3\Sky
%PY% gen.py Slime Slime_lose_btl_boss --model wai --out キャラLoRA確認3\Slime
%PY% gen.py Smith Smith_lose_btl_m1,Smith_lose_btl_e3 --model wai --out キャラLoRA確認3\Smith
%PY% gen.py Snow Snow_lose_btl_m1,Snow_lose_btl_boss --model wai --out キャラLoRA確認3\Snow
%PY% gen.py Sphinx Sphinx_e1,Sphinx_lose_btl_e1,Sphinx_lose_btl_boss --model wai --out キャラLoRA確認3\Sphinx
%PY% gen.py Spirit Spirit_lose_btl_m1,Spirit_lose_btl_e1,Spirit_lose_btl_e3 --model wai --out キャラLoRA確認3\Spirit
%PY% gen.py Starship Starship_lose_btl_boss,Starship_lose_btl_e1,Starship_lose_btl_e3 --model wai --out キャラLoRA確認3\Starship
%PY% gen.py Studio Studio_lose_btl_e1 --model wai --out キャラLoRA確認3\Studio
%PY% gen.py Sylvia Sylvia_lose_btl_e2 --model wai --out キャラLoRA確認3\Sylvia
%PY% gen.py Tavern Tavern_lose_btl_e3,Tavern_lose_btl_boss --model wai --out キャラLoRA確認3\Tavern
%PY% gen.py Tea Tea_lose_btl_m1 --model wai --out キャラLoRA確認3\Tea
%PY% gen.py Train Train_lose_btl_m1 --model wai --out キャラLoRA確認3\Train
%PY% gen.py Tutor Tutor_master,Tutor_lose_btl_m1 --model wai --out キャラLoRA確認3\Tutor
%PY% gen.py Twins Twins_lose_btl_e1 --model wai --out キャラLoRA確認3\Twins
%PY% gen.py Underworld Underworld_lose_btl_m1,Underworld_lose_btl_boss --model wai --out キャラLoRA確認3\Underworld
%PY% gen.py Valkyrie Valkyrie_lose_btl_e1,Valkyrie_lose_btl_m1,Valkyrie_lose_btl_e2,Valkyrie_lose_btl_e3,Valkyrie_lose_btl_boss --model wai --out キャラLoRA確認3\Valkyrie
%PY% gen.py Vampire Vampire_lose_btl_m1 --model wai --out キャラLoRA確認3\Vampire
%PY% gen.py Witch Witch_boss,Witch_lose_btl_boss,Witch_lose_btl_m1 --model wai --out キャラLoRA確認3\Witch
%PY% gen.py Yatsume Yatsume_lose_btl_m1,Yatsume_lose_btl_e3 --model wai --out キャラLoRA確認3\Yatsume
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
pause
