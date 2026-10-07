@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ささやきの場面のうち、寝ている場面 7枚を、寝姿の下書きに替えて撮り直します。
echo 保存先：ComfyUI\output\ささやき確認2
%PY% gen.py Cammy Cammy_lose_inochi_m3 --model wai --out ささやき確認2
%PY% gen.py Dream Dream_lose_btl_m1 --model wai --out ささやき確認2
%PY% gen.py Konoha Konoha_lose_btl_e1 --model wai --out ささやき確認2
%PY% gen.py Luna Luna_lose_inochi_e2 --model wai --out ささやき確認2
%PY% gen.py Necro Necro_lose_inochi_m3 --model wai --out ささやき確認2
%PY% gen.py Tengu Tengu_atk_e3,Tengu_lose_btl_e3 --model wai --out ささやき確認2
pause
