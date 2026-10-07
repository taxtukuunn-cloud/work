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
echo  確認撮影28：光のにじみ対策（参考の絵の背景を中間色に・効かせる時間を短く・強さ40）
rem  ※撮らない場面は消さずに rem で残してあります。撮るときは行頭の rem を外してください（参考の絵と2人の場面の両方）。
echo  [1/2] 参考の絵を撮り直す
%PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 CrossCafe:CrossCafe_atk_m1
if errorlevel 1 goto end
%PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Tavern:Tavern_atk_e3
if errorlevel 1 goto end
%PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Maid:Maid_lose_btl_e1
if errorlevel 1 goto end
%PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Train:Train_atk_e1
if errorlevel 1 goto end
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Atelier:Atelier_atk_m1   （女神のドレス：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Auction:Auction_atk_e3   （シフォンのドレス：今回は対象外）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Bride:Bride_atk_m3   （ウェディングドレス：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Harem:Harem_atk_m1   （踊り子：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Heels:Heels_atk_e2   （ひざ丈のメイド服：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Oiran:Oiran_atk_e1   （振袖：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Perfume:Perfume_atk_e3   （ブラウスとスカート：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Sister:Sister_lose_onedari_m1   （修道服：参考なしで乗る）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Revue:Revue_atk_m1   （ドレス：今回は対象外）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Lingerie:Lingerie_lose_inochi_e1   （下着：参考ありでも乗らない）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Casino:Casino_atk_m3   （バニー：主人公が小さく出るので撮らない）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Idol:Idol_atk_m2   （アイドル衣装：参考の絵が幼く見えるので撮らない）
rem %PY% "衣装の参考を撮る.py" --out 確認28_にじみ\参考の絵 Shrine:Shrine_atk_e2   （巫女装束：参考の絵に別の人物が写り込むので撮らない）
rem  （Dorm 寮の制服は、学生服に見えやすいのでこの方式では撮らない。主人公の体が写らない構図に回す）
echo.
echo  ここで止めて、Claude に「参考できた」と伝えてください。OK が出たら何かキーを押して続きへ。
pause
echo  [2/2] 2人の場面を撮る
%PY% gen.py CrossCafe CrossCafe_atk_m1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40
%PY% gen.py Tavern Tavern_atk_e3 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40
%PY% gen.py Maid Maid_lose_btl_e1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40
%PY% gen.py Train Train_atk_e1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40
rem %PY% gen.py Atelier Atelier_atk_m1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （女神のドレス：参考なしで乗る）
rem %PY% gen.py Auction Auction_atk_e3 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （シフォンのドレス：今回は対象外）
rem %PY% gen.py Bride Bride_atk_m3 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （ウェディングドレス：参考なしで乗る）
rem %PY% gen.py Harem Harem_atk_m1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （踊り子：参考なしで乗る）
rem %PY% gen.py Heels Heels_atk_e2 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （ひざ丈のメイド服：参考なしで乗る）
rem %PY% gen.py Oiran Oiran_atk_e1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （振袖：参考なしで乗る）
rem %PY% gen.py Perfume Perfume_atk_e3 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （ブラウスとスカート：参考なしで乗る）
rem %PY% gen.py Sister Sister_lose_onedari_m1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （修道服：参考なしで乗る）
rem %PY% gen.py Revue Revue_atk_m1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （ドレス：今回は対象外）
rem %PY% gen.py Lingerie Lingerie_lose_inochi_e1 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （下着：参考ありでも乗らない）
rem %PY% gen.py Casino Casino_atk_m3 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （バニー：主人公が小さく出るので撮らない）
rem %PY% gen.py Idol Idol_atk_m2 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （アイドル衣装：参考の絵が幼く見えるので撮らない）
rem %PY% gen.py Shrine Shrine_atk_e2 --model wai --redo --outfit-ref 0.4 --out 確認28_にじみ\強さ40   （巫女装束：参考の絵に別の人物が写り込むので撮らない）
:end
echo.
pause
