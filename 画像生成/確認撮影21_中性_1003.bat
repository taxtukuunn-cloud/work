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
echo  確認撮影21：主人公を中性的な見た目にする（9場面 × 主人公LoRAあり／なし＝18枚）
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_女装
%PY% gen.py Perfume Perfume_lose_btl_m3 --model wai --redo --andro all --out 確認21_中性\LoRAあり_女装
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_女装
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_女装
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --andro all --out 確認21_中性\LoRAあり_女装
%PY% gen.py Amazon Amazon_lose_btl_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_ふつう
%PY% gen.py Police Police_atk_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_ふつう
%PY% gen.py Clinic Clinic_lose_btl_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_ふつう
%PY% gen.py Witch Witch_atk_e1 --model wai --redo --andro all --out 確認21_中性\LoRAあり_ふつう
%PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_女装
%PY% gen.py Perfume Perfume_lose_btl_m3 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_女装
%PY% gen.py Revue Revue_atk_m1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_女装
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_女装
%PY% gen.py Casino Casino_atk_m3 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_女装
%PY% gen.py Amazon Amazon_lose_btl_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_ふつう
%PY% gen.py Police Police_atk_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_ふつう
%PY% gen.py Clinic Clinic_lose_btl_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_ふつう
%PY% gen.py Witch Witch_atk_e1 --model wai --redo --andro all --no-hero --out 確認21_中性\LoRAなし_ふつう
echo.
pause
