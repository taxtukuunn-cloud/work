@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  MODごとの絵柄の割当
echo  絵柄割当.csv の「絵柄」列に、下の一覧の絵柄名を書いて保存してください
echo  （空欄＝今までどおり ／ 本編 と書いても今までどおり）
echo ============================================
%PY% gen.py all --style-list
echo.
set /p OK="絵柄割当.csv を開きますか？（y で開く）: "
if /i "%OK%"=="y" start "" "%~dp0絵柄割当.csv"
pause
