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
echo  全MOD撮影：108個のMODを順に撮ります（撮り終えた絵は飛ばすので、途中で止めても次回は続きから）
rem  ・1つのMODが1行。撮らないMODは行頭に rem を付ける（消さない）。止めるときは Ctrl+C か、この画面を閉じる
rem  ・記録は 全MOD撮影_記録.txt（MODごとの終了時刻。終了コード 0 以外は失敗）
echo %date% %time%  ---- 開始 ---- >> "全MOD撮影_記録.txt"
rem  ==== 1) 女装のないMOD（83個・3230枚） ====
%PY% gen.py Alchemy all --model wai
echo %date% %time%  Alchemy  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Alraune all --model wai
echo %date% %time%  Alraune  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Amazon all --model wai
echo %date% %time%  Amazon  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Android all --model wai
echo %date% %time%  Android  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Angel all --model wai
echo %date% %time%  Angel  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Beach all --model wai
echo %date% %time%  Beach  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Cammy all --model wai
echo %date% %time%  Cammy  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Candy all --model wai
echo %date% %time%  Candy  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Circle all --model wai
echo %date% %time%  Circle  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Circus all --model wai
echo %date% %time%  Circus  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Clinic all --model wai
echo %date% %time%  Clinic  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Clock all --model wai
echo %date% %time%  Clock  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py DarkElf all --model wai
echo %date% %time%  DarkElf  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Dragon all --model wai
echo %date% %time%  Dragon  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Dream all --model wai
echo %date% %time%  Dream  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Eiraira all --model wai
echo %date% %time%  Eiraira  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Eruru all --model wai
echo %date% %time%  Eruru  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Esthe all --model wai
echo %date% %time%  Esthe  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Exam all --model wai
echo %date% %time%  Exam  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Flower all --model wai
echo %date% %time%  Flower  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Fortune all --model wai
echo %date% %time%  Fortune  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Gemini all --model wai
echo %date% %time%  Gemini  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py General all --model wai
echo %date% %time%  General  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Gym all --model wai
echo %date% %time%  Gym  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Hive all --model wai
echo %date% %time%  Hive  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Host all --model wai
echo %date% %time%  Host  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Inma all --model wai
echo %date% %time%  Inma  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Inmon all --model wai
echo %date% %time%  Inmon  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Inn all --model wai
echo %date% %time%  Inn  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Kitsune all --model wai
echo %date% %time%  Kitsune  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Knight all --model wai
echo %date% %time%  Knight  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Konoha all --model wai
echo %date% %time%  Konoha  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Lab all --model wai
echo %date% %time%  Lab  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Labyrinth all --model wai
echo %date% %time%  Labyrinth  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Library all --model wai
echo %date% %time%  Library  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Luna all --model wai
echo %date% %time%  Luna  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Masque all --model wai
echo %date% %time%  Masque  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Medusa all --model wai
echo %date% %time%  Medusa  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Military all --model wai
echo %date% %time%  Military  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Mimic all --model wai
echo %date% %time%  Mimic  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Mirror all --model wai
echo %date% %time%  Mirror  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Moth all --model wai
echo %date% %time%  Moth  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Musashi all --model wai
echo %date% %time%  Musashi  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Necro all --model wai
echo %date% %time%  Necro  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Nekomata all --model wai
echo %date% %time%  Nekomata  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Neneko all --model wai
echo %date% %time%  Neneko  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Ninja all --model wai
echo %date% %time%  Ninja  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Octa all --model wai
echo %date% %time%  Octa  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Office all --model wai
echo %date% %time%  Office  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Oni all --model wai
echo %date% %time%  Oni  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Onsen all --model wai
echo %date% %time%  Onsen  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Patra all --model wai
echo %date% %time%  Patra  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Pawn all --model wai
echo %date% %time%  Pawn  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Police all --model wai
echo %date% %time%  Police  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Prison all --model wai
echo %date% %time%  Prison  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Puppet all --model wai
echo %date% %time%  Puppet  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Queen all --model wai
echo %date% %time%  Queen  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Ranch all --model wai
echo %date% %time%  Ranch  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Rosetta all --model wai
echo %date% %time%  Rosetta  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Ruin all --model wai
echo %date% %time%  Ruin  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py SEruru all --model wai
echo %date% %time%  SEruru  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Salon all --model wai
echo %date% %time%  Salon  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py ShowPub all --model wai
echo %date% %time%  ShowPub  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Sky all --model wai
echo %date% %time%  Sky  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Slime all --model wai
echo %date% %time%  Slime  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Smith all --model wai
echo %date% %time%  Smith  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Snow all --model wai
echo %date% %time%  Snow  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Sphinx all --model wai
echo %date% %time%  Sphinx  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Spirit all --model wai
echo %date% %time%  Spirit  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Starship all --model wai
echo %date% %time%  Starship  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Studio all --model wai
echo %date% %time%  Studio  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Summoner all --model wai
echo %date% %time%  Summoner  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Sylvia all --model wai
echo %date% %time%  Sylvia  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Tea all --model wai
echo %date% %time%  Tea  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Tengu all --model wai
echo %date% %time%  Tengu  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Tutor all --model wai
echo %date% %time%  Tutor  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Twins all --model wai
echo %date% %time%  Twins  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Underworld all --model wai
echo %date% %time%  Underworld  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Valkyrie all --model wai
echo %date% %time%  Valkyrie  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Vampire all --model wai
echo %date% %time%  Vampire  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Werewolf all --model wai
echo %date% %time%  Werewolf  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Witch all --model wai
echo %date% %time%  Witch  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
%PY% gen.py Yakai all --model wai
echo %date% %time%  Yakai  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  ==== 2) 下半身が人でない相手など、下書きが当たらない場面が多いMOD（7個・274枚） ====
rem  Arachne：場面 28 のうち下書きなし 21
%PY% gen.py Arachne all --model wai
echo %date% %time%  Arachne  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Centaur：場面 28 のうち下書きなし 16
%PY% gen.py Centaur all --model wai
echo %date% %time%  Centaur  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  GhostShip：場面 28 のうち下書きなし 12
%PY% gen.py GhostShip all --model wai
echo %date% %time%  GhostShip  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Kiss：場面 28 のうち下書きなし 12
%PY% gen.py Kiss all --model wai
echo %date% %time%  Kiss  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Lamia：場面 28 のうち下書きなし 28
%PY% gen.py Lamia all --model wai
echo %date% %time%  Lamia  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Scylla：場面 28 のうち下書きなし 23
%PY% gen.py Scylla all --model wai
echo %date% %time%  Scylla  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Yatsume：場面 28 のうち下書きなし 12
%PY% gen.py Yatsume all --model wai
echo %date% %time%  Yatsume  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  ==== 3) 女装のあるMOD（18個・717枚）：まず参考なしで撮る。外れた場面はあとで撮り直す ====
rem  Atelier：女装の場面 28（うち主人公の位置が取れない場面 11）
%PY% gen.py Atelier all --model wai
echo %date% %time%  Atelier  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Auction：女装の場面 28（うち主人公の位置が取れない場面 4）
%PY% gen.py Auction all --model wai
echo %date% %time%  Auction  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Bride：女装の場面 27（うち主人公の位置が取れない場面 8）
%PY% gen.py Bride all --model wai
echo %date% %time%  Bride  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Casino：女装の場面 28（うち主人公の位置が取れない場面 6）
%PY% gen.py Casino all --model wai
echo %date% %time%  Casino  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  CrossCafe：女装の場面 28（うち主人公の位置が取れない場面 8）
%PY% gen.py CrossCafe all --model wai
echo %date% %time%  CrossCafe  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Dorm：女装の場面 28（うち主人公の位置が取れない場面 4）
%PY% gen.py Dorm all --model wai
echo %date% %time%  Dorm  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Harem：女装の場面 28（うち主人公の位置が取れない場面 7）
%PY% gen.py Harem all --model wai
echo %date% %time%  Harem  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Heels：女装の場面 28（うち主人公の位置が取れない場面 15）
%PY% gen.py Heels all --model wai
echo %date% %time%  Heels  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Idol：女装の場面 28（うち主人公の位置が取れない場面 7）
%PY% gen.py Idol all --model wai
echo %date% %time%  Idol  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Lingerie：女装の場面 25（うち主人公の位置が取れない場面 3）
%PY% gen.py Lingerie all --model wai
echo %date% %time%  Lingerie  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Maid：女装の場面 28（うち主人公の位置が取れない場面 4）
%PY% gen.py Maid all --model wai
echo %date% %time%  Maid  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Oiran：女装の場面 22（うち主人公の位置が取れない場面 3）
%PY% gen.py Oiran all --model wai
echo %date% %time%  Oiran  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Perfume：女装の場面 26（うち主人公の位置が取れない場面 7）
%PY% gen.py Perfume all --model wai
echo %date% %time%  Perfume  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Revue：女装の場面 28（うち主人公の位置が取れない場面 6）
%PY% gen.py Revue all --model wai
echo %date% %time%  Revue  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Shrine：女装の場面 22（うち主人公の位置が取れない場面 10）
%PY% gen.py Shrine all --model wai
echo %date% %time%  Shrine  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Sister：女装の場面 21（うち主人公の位置が取れない場面 6）
%PY% gen.py Sister all --model wai
echo %date% %time%  Sister  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Tavern：女装の場面 22（うち主人公の位置が取れない場面 3）
%PY% gen.py Tavern all --model wai
echo %date% %time%  Tavern  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
rem  Train：女装の場面 28（うち主人公の位置が取れない場面 3）
%PY% gen.py Train all --model wai
echo %date% %time%  Train  終了コード %errorlevel% >> "全MOD撮影_記録.txt"
echo %date% %time%  ---- 全部終了 ---- >> "全MOD撮影_記録.txt"
echo.
echo  全部終わりました。
pause
