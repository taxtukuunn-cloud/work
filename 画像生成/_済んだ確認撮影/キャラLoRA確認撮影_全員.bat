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
echo  キャラLoRAを当てた全員の確認撮影（最新の設定で・304枚）
echo  当てたキャラごとに 立ち絵 と 敗北イベント1枚
echo  保存先: output\キャラLoRA確認2\MOD名\（前の キャラLoRA確認 とは別）
echo  終わったら 撮った絵の下書き一覧.bat を実行してください
echo ============================================
%PY% gen.py Alchemy Alchemy_master,Alchemy_lose_btl_m1 --model wai --out キャラLoRA確認2\Alchemy
%PY% gen.py Alraune Alraune_master,Alraune_lose_btl_m1 --model wai --out キャラLoRA確認2\Alraune
%PY% gen.py Amazon Amazon_e1,Amazon_lose_btl_e1,Amazon_master,Amazon_lose_btl_m1,Amazon_boss,Amazon_lose_btl_boss --model wai --out キャラLoRA確認2\Amazon
%PY% gen.py Angel Angel_master,Angel_lose_btl_m1 --model wai --out キャラLoRA確認2\Angel
%PY% gen.py Atelier Atelier_master,Atelier_lose_btl_m1 --model wai --out キャラLoRA確認2\Atelier
%PY% gen.py Beach Beach_e1,Beach_lose_btl_e1,Beach_master,Beach_lose_btl_m1,Beach_e3,Beach_lose_btl_e3 --model wai --out キャラLoRA確認2\Beach
%PY% gen.py Bride Bride_master,Bride_lose_btl_m1 --model wai --out キャラLoRA確認2\Bride
%PY% gen.py Cammy Cammy_master,Cammy_lose_btl_m1,Cammy_e1,Cammy_lose_btl_e1,Cammy_e2,Cammy_lose_btl_e2,Cammy_e3,Cammy_lose_btl_e3 --model wai --out キャラLoRA確認2\Cammy
%PY% gen.py Candy Candy_master,Candy_lose_btl_m1 --model wai --out キャラLoRA確認2\Candy
%PY% gen.py Casino Casino_master,Casino_lose_btl_m1,Casino_e2,Casino_lose_btl_e2,Casino_boss,Casino_lose_btl_boss --model wai --out キャラLoRA確認2\Casino
%PY% gen.py Centaur Centaur_boss,Centaur_lose_btl_boss --model wai --out キャラLoRA確認2\Centaur
%PY% gen.py Circus Circus_e3,Circus_lose_btl_e3 --model wai --out キャラLoRA確認2\Circus
%PY% gen.py Clinic Clinic_master,Clinic_lose_btl_m1,Clinic_e1,Clinic_lose_btl_e1,Clinic_e2,Clinic_lose_btl_e2,Clinic_e3,Clinic_lose_btl_e3 --model wai --out キャラLoRA確認2\Clinic
%PY% gen.py Clock Clock_e1,Clock_lose_btl_e1 --model wai --out キャラLoRA確認2\Clock
%PY% gen.py CrossCafe CrossCafe_boss,CrossCafe_lose_btl_boss --model wai --out キャラLoRA確認2\CrossCafe
%PY% gen.py DarkElf DarkElf_e2,DarkElf_lose_btl_e2 --model wai --out キャラLoRA確認2\DarkElf
%PY% gen.py Dorm Dorm_boss,Dorm_lose_btl_boss --model wai --out キャラLoRA確認2\Dorm
%PY% gen.py Dragon Dragon_master,Dragon_lose_btl_m1,Dragon_boss,Dragon_lose_btl_boss --model wai --out キャラLoRA確認2\Dragon
%PY% gen.py Dream Dream_e2,Dream_lose_btl_e2,Dream_boss,Dream_lose_btl_boss,Dream_master,Dream_lose_btl_m1 --model wai --out キャラLoRA確認2\Dream
%PY% gen.py Eiraira Eiraira_e3,Eiraira_lose_btl_e3 --model wai --out キャラLoRA確認2\Eiraira
%PY% gen.py Eruru Eruru_boss,Eruru_lose_btl_boss --model wai --out キャラLoRA確認2\Eruru
%PY% gen.py Esthe Esthe_master,Esthe_lose_btl_m1 --model wai --out キャラLoRA確認2\Esthe
%PY% gen.py Exam Exam_e1,Exam_lose_btl_e1,Exam_e2,Exam_lose_btl_e2,Exam_boss,Exam_lose_btl_boss --model wai --out キャラLoRA確認2\Exam
%PY% gen.py Fortune Fortune_e1,Fortune_lose_btl_e1,Fortune_e2,Fortune_lose_btl_e2,Fortune_boss,Fortune_lose_btl_boss --model wai --out キャラLoRA確認2\Fortune
%PY% gen.py Gemini Gemini_e3,Gemini_lose_btl_e3 --model wai --out キャラLoRA確認2\Gemini
%PY% gen.py General General_master,General_lose_btl_m1,General_e1,General_lose_btl_e1,General_boss,General_lose_btl_boss,General_e3,General_lose_btl_e3 --model wai --out キャラLoRA確認2\General
%PY% gen.py GhostShip GhostShip_boss,GhostShip_lose_btl_boss --model wai --out キャラLoRA確認2\GhostShip
%PY% gen.py Harem Harem_master,Harem_lose_btl_m1,Harem_e2,Harem_lose_btl_e2 --model wai --out キャラLoRA確認2\Harem
%PY% gen.py Heels Heels_master,Heels_lose_btl_m1,Heels_e1,Heels_lose_btl_e1,Heels_boss,Heels_lose_btl_boss,Heels_e3,Heels_lose_btl_e3,Heels_e2,Heels_lose_btl_e2 --model wai --out キャラLoRA確認2\Heels
%PY% gen.py Idol Idol_master,Idol_lose_btl_m1 --model wai --out キャラLoRA確認2\Idol
%PY% gen.py Inmon Inmon_boss,Inmon_lose_btl_boss,Inmon_master,Inmon_lose_btl_m1 --model wai --out キャラLoRA確認2\Inmon
%PY% gen.py Inn Inn_boss,Inn_lose_btl_boss,Inn_master,Inn_lose_btl_m1 --model wai --out キャラLoRA確認2\Inn
%PY% gen.py Kiss Kiss_master,Kiss_lose_btl_m1,Kiss_boss,Kiss_lose_btl_boss,Kiss_e2,Kiss_lose_btl_e2 --model wai --out キャラLoRA確認2\Kiss
%PY% gen.py Konoha Konoha_master,Konoha_lose_btl_m1,Konoha_e2,Konoha_lose_btl_e2,Konoha_boss,Konoha_lose_btl_boss --model wai --out キャラLoRA確認2\Konoha
%PY% gen.py Lab Lab_master,Lab_lose_btl_m1,Lab_e2,Lab_lose_btl_e2,Lab_e3,Lab_lose_btl_e3 --model wai --out キャラLoRA確認2\Lab
%PY% gen.py Library Library_master,Library_lose_btl_m1,Library_boss,Library_lose_btl_boss --model wai --out キャラLoRA確認2\Library
%PY% gen.py Lingerie Lingerie_boss,Lingerie_lose_btl_boss --model wai --out キャラLoRA確認2\Lingerie
%PY% gen.py Luna Luna_master,Luna_lose_btl_m1 --model wai --out キャラLoRA確認2\Luna
%PY% gen.py Masque Masque_master,Masque_lose_btl_m1 --model wai --out キャラLoRA確認2\Masque
%PY% gen.py Medusa Medusa_master,Medusa_lose_btl_m1 --model wai --out キャラLoRA確認2\Medusa
%PY% gen.py Military Military_master,Military_lose_btl_m1,Military_e3,Military_lose_btl_e3,Military_e1,Military_lose_btl_e1 --model wai --out キャラLoRA確認2\Military
%PY% gen.py Mimic Mimic_master,Mimic_lose_btl_m1 --model wai --out キャラLoRA確認2\Mimic
%PY% gen.py Mirror Mirror_boss,Mirror_lose_btl_boss,Mirror_master,Mirror_lose_btl_m1 --model wai --out キャラLoRA確認2\Mirror
%PY% gen.py Musashi Musashi_master,Musashi_lose_btl_m1 --model wai --out キャラLoRA確認2\Musashi
%PY% gen.py Necro Necro_master,Necro_lose_btl_m1,Necro_e2,Necro_lose_btl_e2 --model wai --out キャラLoRA確認2\Necro
%PY% gen.py Neneko Neneko_e2,Neneko_lose_btl_e2 --model wai --out キャラLoRA確認2\Neneko
%PY% gen.py Octa Octa_boss,Octa_lose_btl_boss --model wai --out キャラLoRA確認2\Octa
%PY% gen.py Office Office_master,Office_lose_btl_m1,Office_e1,Office_lose_btl_e1 --model wai --out キャラLoRA確認2\Office
%PY% gen.py Oiran Oiran_master,Oiran_lose_btl_m1 --model wai --out キャラLoRA確認2\Oiran
%PY% gen.py Oni Oni_master,Oni_lose_btl_m1 --model wai --out キャラLoRA確認2\Oni
%PY% gen.py Onsen Onsen_master,Onsen_lose_btl_m1 --model wai --out キャラLoRA確認2\Onsen
%PY% gen.py Patra Patra_master,Patra_lose_btl_m1,Patra_e1,Patra_lose_btl_e1,Patra_e2,Patra_lose_btl_e2 --model wai --out キャラLoRA確認2\Patra
%PY% gen.py Pawn Pawn_master,Pawn_lose_btl_m1 --model wai --out キャラLoRA確認2\Pawn
%PY% gen.py Perfume Perfume_master,Perfume_lose_btl_m1 --model wai --out キャラLoRA確認2\Perfume
%PY% gen.py Police Police_master,Police_lose_btl_m1 --model wai --out キャラLoRA確認2\Police
%PY% gen.py Prison Prison_e3,Prison_lose_btl_e3,Prison_boss,Prison_lose_btl_boss,Prison_master,Prison_lose_btl_m1,Prison_e1,Prison_lose_btl_e1 --model wai --out キャラLoRA確認2\Prison
%PY% gen.py Puppet Puppet_master,Puppet_lose_btl_m1 --model wai --out キャラLoRA確認2\Puppet
%PY% gen.py Queen Queen_e1,Queen_lose_btl_e1,Queen_boss,Queen_lose_btl_boss,Queen_e2,Queen_lose_btl_e2 --model wai --out キャラLoRA確認2\Queen
%PY% gen.py Ranch Ranch_boss,Ranch_lose_btl_boss --model wai --out キャラLoRA確認2\Ranch
%PY% gen.py Revue Revue_e1,Revue_lose_btl_e1,Revue_boss,Revue_lose_btl_boss --model wai --out キャラLoRA確認2\Revue
%PY% gen.py SEruru SEruru_boss,SEruru_lose_btl_boss --model wai --out キャラLoRA確認2\SEruru
%PY% gen.py Salon Salon_boss,Salon_lose_btl_boss --model wai --out キャラLoRA確認2\Salon
%PY% gen.py ShowPub ShowPub_e1,ShowPub_lose_btl_e1,ShowPub_boss,ShowPub_lose_btl_boss --model wai --out キャラLoRA確認2\ShowPub
%PY% gen.py Shrine Shrine_e3,Shrine_lose_btl_e3 --model wai --out キャラLoRA確認2\Shrine
%PY% gen.py Sister Sister_master,Sister_lose_btl_m1,Sister_boss,Sister_lose_btl_boss --model wai --out キャラLoRA確認2\Sister
%PY% gen.py Sky Sky_master,Sky_lose_btl_m1,Sky_e3,Sky_lose_btl_e3,Sky_e1,Sky_lose_btl_e1 --model wai --out キャラLoRA確認2\Sky
%PY% gen.py Slime Slime_boss,Slime_lose_btl_boss --model wai --out キャラLoRA確認2\Slime
%PY% gen.py Smith Smith_master,Smith_lose_btl_m1,Smith_e3,Smith_lose_btl_e3 --model wai --out キャラLoRA確認2\Smith
%PY% gen.py Snow Snow_master,Snow_lose_btl_m1,Snow_boss,Snow_lose_btl_boss --model wai --out キャラLoRA確認2\Snow
%PY% gen.py Sphinx Sphinx_e1,Sphinx_lose_btl_e1,Sphinx_boss,Sphinx_lose_btl_boss --model wai --out キャラLoRA確認2\Sphinx
%PY% gen.py Spirit Spirit_master,Spirit_lose_btl_m1,Spirit_e1,Spirit_lose_btl_e1,Spirit_e3,Spirit_lose_btl_e3 --model wai --out キャラLoRA確認2\Spirit
%PY% gen.py Starship Starship_boss,Starship_lose_btl_boss,Starship_e1,Starship_lose_btl_e1,Starship_e3,Starship_lose_btl_e3 --model wai --out キャラLoRA確認2\Starship
%PY% gen.py Studio Studio_e1,Studio_lose_btl_e1 --model wai --out キャラLoRA確認2\Studio
%PY% gen.py Sylvia Sylvia_e2,Sylvia_lose_btl_e2 --model wai --out キャラLoRA確認2\Sylvia
%PY% gen.py Tavern Tavern_e3,Tavern_lose_btl_e3,Tavern_boss,Tavern_lose_btl_boss --model wai --out キャラLoRA確認2\Tavern
%PY% gen.py Tea Tea_master,Tea_lose_btl_m1 --model wai --out キャラLoRA確認2\Tea
%PY% gen.py Train Train_master,Train_lose_btl_m1 --model wai --out キャラLoRA確認2\Train
%PY% gen.py Tutor Tutor_master,Tutor_lose_btl_m1 --model wai --out キャラLoRA確認2\Tutor
%PY% gen.py Twins Twins_e1,Twins_lose_btl_e1 --model wai --out キャラLoRA確認2\Twins
%PY% gen.py Underworld Underworld_master,Underworld_lose_btl_m1,Underworld_boss,Underworld_lose_btl_boss --model wai --out キャラLoRA確認2\Underworld
%PY% gen.py Valkyrie Valkyrie_e1,Valkyrie_lose_btl_e1,Valkyrie_master,Valkyrie_lose_btl_m1,Valkyrie_e2,Valkyrie_lose_btl_e2,Valkyrie_e3,Valkyrie_lose_btl_e3,Valkyrie_boss,Valkyrie_lose_btl_boss --model wai --out キャラLoRA確認2\Valkyrie
%PY% gen.py Vampire Vampire_master,Vampire_lose_btl_m1 --model wai --out キャラLoRA確認2\Vampire
%PY% gen.py Witch Witch_boss,Witch_lose_btl_boss,Witch_master,Witch_lose_btl_m1 --model wai --out キャラLoRA確認2\Witch
%PY% gen.py Yatsume Yatsume_master,Yatsume_lose_btl_m1,Yatsume_e3,Yatsume_lose_btl_e3 --model wai --out キャラLoRA確認2\Yatsume
echo.
echo 全部送信しました。ComfyUI の処理が終わるまで待ってください。
pause
