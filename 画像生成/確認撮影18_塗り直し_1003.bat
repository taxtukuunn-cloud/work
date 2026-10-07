@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo  確認撮影18：女装の場面の「主人公の服だけ塗り直す」試作（5場面×2通り）
echo  ※ ComfyUI を起動しておいてください
%PY% "服の塗り直し.py" --out 確認18_塗り直し --denoise 0.7,0.85 Lingerie:Lingerie_lose_inochi_e1:確認16_女装\Lingerie_lose_inochi_e1_00001_.png Perfume:Perfume_lose_btl_m3:確認16_女装\Perfume_lose_btl_m3_00001_.png Revue:Revue_atk_m1:確認16_女装\Revue_atk_m1_00001_.png Maid:Maid_lose_btl_e1:確認16_女装\Maid_lose_btl_e1_00001_.png Casino:Casino_atk_m3:確認12_女装\Casino_atk_m3_00001_.png
echo.
pause
