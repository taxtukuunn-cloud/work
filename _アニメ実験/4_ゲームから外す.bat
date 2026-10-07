@echo off
set "GAME=D:\GAME\SuccubusDuel本体\RJ01149693\SuccubusDuel_sub\サキュバスデュエル"
echo 実験用に入れた次のファイルだけを消します。
echo   CSV\Card\AnimeTest_master.txt
echo   CSV\EventList\Quest\AnimeTest.txt
echo   Picture\AnimeTest\
pause
if exist "%GAME%\CSV\Card\AnimeTest_master.txt" del /Q "%GAME%\CSV\Card\AnimeTest_master.txt"
if exist "%GAME%\CSV\EventList\Quest\AnimeTest.txt" del /Q "%GAME%\CSV\EventList\Quest\AnimeTest.txt"
if exist "%GAME%\Picture\AnimeTest" rmdir /S /Q "%GAME%\Picture\AnimeTest"
echo 外しました。
pause
exit /b 0
