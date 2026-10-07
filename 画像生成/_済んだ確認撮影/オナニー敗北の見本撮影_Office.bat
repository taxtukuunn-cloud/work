@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo Office のオナニー敗北 7場面（見つかったあと相手に責められている絵）を試し撮りします。
echo 保存先：ComfyUI\output\オナニー敗北_見本_Office
%PY% gen.py Office lose_onani --model wai --redo --out オナニー敗北_見本_Office
pause
