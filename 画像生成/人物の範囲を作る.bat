@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  人物ごとの範囲を作る（領域指定・2026-10-02）
echo  構図下書き元 の元絵の顔を見つけ、男＝主人公（青）・女＝相手（赤）の「頭～胸」の範囲を作ります（第2版）
echo  確認: 構図下書き\_人物の範囲一覧_*.png ／ 構図下書き\_人物の範囲.csv
echo  前回の範囲は作り直されます
echo ============================================
%PY% make_region_masks.py %*
echo.
pause
