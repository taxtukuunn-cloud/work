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
echo  キャラLoRAを当てたキャラの確認撮影（2026-10-02）
echo  当てたキャラごとに 立ち絵 と 敗北イベント1枚（lose_btl）
echo  保存先: output\キャラLoRA確認\MOD名\（本番のフォルダとは別）
echo ============================================
%PY% gen.py Amazon Amazon_e1,Amazon_lose_btl_e1 --model wai --out キャラLoRA確認\Amazon
%PY% gen.py Bride Bride_master,Bride_lose_btl_m1 --model wai --out キャラLoRA確認\Bride
%PY% gen.py Cammy Cammy_master,Cammy_lose_btl_m1,Cammy_e1,Cammy_lose_btl_e1,Cammy_e2,Cammy_lose_btl_e2 --model wai --out キャラLoRA確認\Cammy
%PY% gen.py Casino Casino_master,Casino_lose_btl_m1,Casino_e2,Casino_lose_btl_e2,Casino_boss,Casino_lose_btl_boss --model wai --out キャラLoRA確認\Casino
%PY% gen.py Clinic Clinic_master,Clinic_lose_btl_m1,Clinic_e1,Clinic_lose_btl_e1 --model wai --out キャラLoRA確認\Clinic
%PY% gen.py Clock Clock_e1,Clock_lose_btl_e1 --model wai --out キャラLoRA確認\Clock
%PY% gen.py DarkElf DarkElf_e2,DarkElf_lose_btl_e2 --model wai --out キャラLoRA確認\DarkElf
%PY% gen.py Dragon Dragon_master,Dragon_lose_btl_m1,Dragon_boss,Dragon_lose_btl_boss --model wai --out キャラLoRA確認\Dragon
%PY% gen.py Dream Dream_e2,Dream_lose_btl_e2,Dream_boss,Dream_lose_btl_boss --model wai --out キャラLoRA確認\Dream
%PY% gen.py Eiraira Eiraira_e3,Eiraira_lose_btl_e3 --model wai --out キャラLoRA確認\Eiraira
%PY% gen.py Eruru Eruru_boss,Eruru_lose_btl_boss --model wai --out キャラLoRA確認\Eruru
%PY% gen.py Exam Exam_e1,Exam_lose_btl_e1,Exam_e2,Exam_lose_btl_e2,Exam_boss,Exam_lose_btl_boss --model wai --out キャラLoRA確認\Exam
%PY% gen.py General General_master,General_lose_btl_m1,General_e1,General_lose_btl_e1,General_boss,General_lose_btl_boss --model wai --out キャラLoRA確認\General
%PY% gen.py Harem Harem_master,Harem_lose_btl_m1 --model wai --out キャラLoRA確認\Harem
%PY% gen.py Heels Heels_master,Heels_lose_btl_m1,Heels_e1,Heels_lose_btl_e1,Heels_boss,Heels_lose_btl_boss --model wai --out キャラLoRA確認\Heels
%PY% gen.py Inmon Inmon_boss,Inmon_lose_btl_boss --model wai --out キャラLoRA確認\Inmon
%PY% gen.py Inn Inn_boss,Inn_lose_btl_boss --model wai --out キャラLoRA確認\Inn
%PY% gen.py Kiss Kiss_master,Kiss_lose_btl_m1 --model wai --out キャラLoRA確認\Kiss
%PY% gen.py Konoha Konoha_master,Konoha_lose_btl_m1,Konoha_e2,Konoha_lose_btl_e2,Konoha_boss,Konoha_lose_btl_boss --model wai --out キャラLoRA確認\Konoha
%PY% gen.py Library Library_master,Library_lose_btl_m1 --model wai --out キャラLoRA確認\Library
%PY% gen.py Lingerie Lingerie_boss,Lingerie_lose_btl_boss --model wai --out キャラLoRA確認\Lingerie
%PY% gen.py Luna Luna_master,Luna_lose_btl_m1 --model wai --out キャラLoRA確認\Luna
%PY% gen.py Masque Masque_master,Masque_lose_btl_m1 --model wai --out キャラLoRA確認\Masque
%PY% gen.py Military Military_master,Military_lose_btl_m1 --model wai --out キャラLoRA確認\Military
%PY% gen.py Mirror Mirror_boss,Mirror_lose_btl_boss --model wai --out キャラLoRA確認\Mirror
%PY% gen.py Musashi Musashi_master,Musashi_lose_btl_m1 --model wai --out キャラLoRA確認\Musashi
%PY% gen.py Neneko Neneko_e2,Neneko_lose_btl_e2 --model wai --out キャラLoRA確認\Neneko
%PY% gen.py Office Office_master,Office_lose_btl_m1 --model wai --out キャラLoRA確認\Office
%PY% gen.py Oiran Oiran_master,Oiran_lose_btl_m1 --model wai --out キャラLoRA確認\Oiran
%PY% gen.py Patra Patra_master,Patra_lose_btl_m1 --model wai --out キャラLoRA確認\Patra
%PY% gen.py Tutor Tutor_master,Tutor_lose_btl_m1 --model wai --out キャラLoRA確認\Tutor
%PY% gen.py Prison Prison_e3,Prison_lose_btl_e3,Prison_boss,Prison_lose_btl_boss --model wai --out キャラLoRA確認\Prison
%PY% gen.py Puppet Puppet_master,Puppet_lose_btl_m1 --model wai --out キャラLoRA確認\Puppet
%PY% gen.py Queen Queen_e1,Queen_lose_btl_e1,Queen_boss,Queen_lose_btl_boss --model wai --out キャラLoRA確認\Queen
%PY% gen.py Ranch Ranch_boss,Ranch_lose_btl_boss --model wai --out キャラLoRA確認\Ranch
%PY% gen.py ShowPub ShowPub_e1,ShowPub_lose_btl_e1,ShowPub_boss,ShowPub_lose_btl_boss --model wai --out キャラLoRA確認\ShowPub
%PY% gen.py Shrine Shrine_e3,Shrine_lose_btl_e3 --model wai --out キャラLoRA確認\Shrine
%PY% gen.py Sister Sister_master,Sister_lose_btl_m1 --model wai --out キャラLoRA確認\Sister
%PY% gen.py Smith Smith_master,Smith_lose_btl_m1 --model wai --out キャラLoRA確認\Smith
%PY% gen.py Snow Snow_master,Snow_lose_btl_m1 --model wai --out キャラLoRA確認\Snow
%PY% gen.py Spirit Spirit_master,Spirit_lose_btl_m1,Spirit_e1,Spirit_lose_btl_e1,Spirit_e3,Spirit_lose_btl_e3 --model wai --out キャラLoRA確認\Spirit
%PY% gen.py Starship Starship_boss,Starship_lose_btl_boss --model wai --out キャラLoRA確認\Starship
%PY% gen.py Tavern Tavern_e3,Tavern_lose_btl_e3,Tavern_boss,Tavern_lose_btl_boss --model wai --out キャラLoRA確認\Tavern
%PY% gen.py Police Police_master,Police_lose_btl_m1 --model wai --out キャラLoRA確認\Police
%PY% gen.py Twins Twins_e1,Twins_lose_btl_e1 --model wai --out キャラLoRA確認\Twins
%PY% gen.py Underworld Underworld_master,Underworld_lose_btl_m1 --model wai --out キャラLoRA確認\Underworld
%PY% gen.py Valkyrie Valkyrie_e1,Valkyrie_lose_btl_e1 --model wai --out キャラLoRA確認\Valkyrie
%PY% gen.py Witch Witch_boss,Witch_lose_btl_boss --model wai --out キャラLoRA確認\Witch
echo.
echo 送信しました。終わったら教えてください。
pause
