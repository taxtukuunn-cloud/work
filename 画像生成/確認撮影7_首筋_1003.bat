@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo 脇を嗅ぐ場面を「首筋に鼻先を寄せて息を吹きかける」絵にした確認撮影（5枚）→ output\確認7_首筋
%PY% gen.py Underworld Underworld_atk_e2,Underworld_lose_btl_e2 --model wai --out 確認7_首筋
%PY% gen.py Werewolf Werewolf_atk_e1,Werewolf_lose_inochi_m2,Werewolf_lose_onedari_e1 --model wai --out 確認7_首筋
pause
