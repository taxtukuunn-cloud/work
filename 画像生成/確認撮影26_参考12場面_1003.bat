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
echo  確認撮影26：衣装の参考画像を12場面で試す（参考12枚 → Claude が確認 → 参考あり12枚＋参考なし12枚）
echo  [1/2] 参考の絵を撮る
%PY% "衣装の参考を撮る.py" --out 確認26_参考\参考の絵 Atelier:Atelier_atk_m1 Auction:Auction_atk_e3 Bride:Bride_atk_m3 CrossCafe:CrossCafe_atk_m1 Harem:Harem_atk_m1 Heels:Heels_atk_e2 Idol:Idol_atk_m2 Oiran:Oiran_atk_e1 Perfume:Perfume_atk_e3 Shrine:Shrine_atk_e2 Sister:Sister_lose_onedari_m1 Tavern:Tavern_atk_e3
if errorlevel 1 goto end
echo.
echo  ここで止めて、Claude に「参考できた」と伝えてください。OK が出たら何かキーを押して続きへ。
pause
echo  [2/2] 2人の場面を撮る
%PY% gen.py Atelier Atelier_atk_m1 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Auction Auction_atk_e3 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Bride Bride_atk_m3 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py CrossCafe CrossCafe_atk_m1 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Harem Harem_atk_m1 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Heels Heels_atk_e2 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Idol Idol_atk_m2 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Oiran Oiran_atk_e1 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Perfume Perfume_atk_e3 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Shrine Shrine_atk_e2 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Sister Sister_lose_onedari_m1 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Tavern Tavern_atk_e3 --model wai --redo --outfit-ref 0.5 --out 確認26_参考\参考あり
%PY% gen.py Atelier Atelier_atk_m1 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Auction Auction_atk_e3 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Bride Bride_atk_m3 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py CrossCafe CrossCafe_atk_m1 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Harem Harem_atk_m1 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Heels Heels_atk_e2 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Idol Idol_atk_m2 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Oiran Oiran_atk_e1 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Perfume Perfume_atk_e3 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Shrine Shrine_atk_e2 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Sister Sister_lose_onedari_m1 --model wai --redo --out 確認26_参考\参考なし
%PY% gen.py Tavern Tavern_atk_e3 --model wai --redo --out 確認26_参考\参考なし
:end
echo.
pause
