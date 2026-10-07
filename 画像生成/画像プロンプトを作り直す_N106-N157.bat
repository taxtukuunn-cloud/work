@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  N106-N157_場面\scene_data を直したあとに実行します（prompts\コード.json を作り直す）
echo  キャラの見た目を直すときは、scene_data\コード.py の chars の tags を書き換えてから実行
echo ============================================
set /p MOD="作り直すMODコード（Enterだけ＝全部 ／ 例 Genji,Tensho）: "
%PY% N106-N157_場面\build_new.py %MOD% --check
echo.
set /p OK="書き込みますか？（y）: "
if /i not "%OK%"=="y" goto end
%PY% N106-N157_場面\build_new.py %MOD%
:end
pause
