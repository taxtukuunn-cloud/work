@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo キャラLoRA 追加その7（75人）の立ち絵を確認撮影します → output\キャラLoRA確認5
echo ※LoRAを足したあと ComfyUI を再起動していないと、LoRAが見つからず撮れません。
%PY% gen.py Lamia Lamia_boss --model wai --out キャラLoRA確認5
%PY% gen.py Arachne Arachne_master --model wai --out キャラLoRA確認5
%PY% gen.py Yatsume Yatsume_boss --model wai --out キャラLoRA確認5
%PY% gen.py Slime Slime_master,Slime_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Tengu Tengu_boss --model wai --out キャラLoRA確認5
%PY% gen.py Eiraira Eiraira_boss --model wai --out キャラLoRA確認5
%PY% gen.py Angel Angel_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Oni Oni_boss --model wai --out キャラLoRA確認5
%PY% gen.py Queen Queen_master --model wai --out キャラLoRA確認5
%PY% gen.py Flower Flower_master --model wai --out キャラLoRA確認5
%PY% gen.py Cammy Cammy_boss --model wai --out キャラLoRA確認5
%PY% gen.py Vampire Vampire_boss --model wai --out キャラLoRA確認5
%PY% gen.py Nekomata Nekomata_master --model wai --out キャラLoRA確認5
%PY% gen.py Neneko Neneko_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Moth Moth_boss --model wai --out キャラLoRA確認5
%PY% gen.py Snow Snow_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Sphinx Sphinx_master --model wai --out キャラLoRA確認5
%PY% gen.py Patra Patra_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Train Train_boss --model wai --out キャラLoRA確認5
%PY% gen.py Circus Circus_e2,Circus_master --model wai --out キャラLoRA確認5
%PY% gen.py GhostShip GhostShip_e2,GhostShip_master --model wai --out キャラLoRA確認5
%PY% gen.py Puppet Puppet_boss --model wai --out キャラLoRA確認5
%PY% gen.py Atelier Atelier_boss --model wai --out キャラLoRA確認5
%PY% gen.py CrossCafe CrossCafe_master,CrossCafe_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Shrine Shrine_e1,Shrine_master,Shrine_boss --model wai --out キャラLoRA確認5
%PY% gen.py Luna Luna_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Fortune Fortune_master --model wai --out キャラLoRA確認5
%PY% gen.py Witch Witch_e3,Witch_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Clock Clock_master --model wai --out キャラLoRA確認5
%PY% gen.py Labyrinth Labyrinth_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Spirit Spirit_boss --model wai --out キャラLoRA確認5
%PY% gen.py Sylvia Sylvia_e1,Sylvia_boss --model wai --out キャラLoRA確認5
%PY% gen.py Studio Studio_master --model wai --out キャラLoRA確認5
%PY% gen.py Idol Idol_boss,Idol_e2,Idol_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Gemini Gemini_master --model wai --out キャラLoRA確認5
%PY% gen.py Salon Salon_master,Salon_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Mirror Mirror_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Bride Bride_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Masque Masque_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Perfume Perfume_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Sister Sister_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Prison Prison_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Esthe Esthe_boss,Esthe_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Lingerie Lingerie_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Harem Harem_boss --model wai --out キャラLoRA確認5
%PY% gen.py Onsen Onsen_boss --model wai --out キャラLoRA確認5
%PY% gen.py Dorm Dorm_e2,Dorm_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Inmon Inmon_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Police Police_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Office Office_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Smith Smith_boss --model wai --out キャラLoRA確認5
%PY% gen.py Inn Inn_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Musashi Musashi_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Underworld Underworld_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Exam Exam_e3 --model wai --out キャラLoRA確認5
%PY% gen.py Kiss Kiss_e3 --model wai --out キャラLoRA確認5
%PY% gen.py General General_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Beach Beach_boss,Beach_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Octa Octa_e2 --model wai --out キャラLoRA確認5
%PY% gen.py Candy Candy_e1 --model wai --out キャラLoRA確認5
%PY% gen.py Alchemy Alchemy_e2 --model wai --out キャラLoRA確認5
pause
