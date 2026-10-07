@echo off
cd /d "%~dp0"
set "GAME=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル"
if not exist "%GAME%\CSV\Card" goto nogame
if not exist "%GAME%\CSV\EventList\Quest" goto nogame
if not exist "out\CSV\Card\AnimeTest_master.txt" goto noout
echo 次の3か所に、実験用のファイルだけをコピーします。ほかのファイルには触りません。
echo   CSV\Card\AnimeTest_master.txt
echo   CSV\EventList\Quest\AnimeTest.txt
echo   Picture\AnimeTest\anime\
pause
copy /Y "out\CSV\Card\AnimeTest_master.txt" "%GAME%\CSV\Card\"
copy /Y "out\CSV\EventList\Quest\AnimeTest.txt" "%GAME%\CSV\EventList\Quest\"
if not exist "%GAME%\Picture\AnimeTest\anime" mkdir "%GAME%\Picture\AnimeTest\anime"
del /Q "%GAME%\Picture\AnimeTest\anime\AnimeTest (*).png" 2>nul
copy /Y "out\Picture\AnimeTest\anime\*.png" "%GAME%\Picture\AnimeTest\anime\"
echo.
echo 入れました。ゲームを起動して、クエスト一覧の「【実験】アニメ再生テスト」を選んでください。
pause
exit /b 0
:nogame
echo ゲームのフォルダが見つかりません。
echo %GAME%
pause
exit /b 1
:noout
echo 先に「2_コマを作る.bat」を実行してください。
pause
exit /b 1
