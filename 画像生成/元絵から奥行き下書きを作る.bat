@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  選んだ構図の元絵から 奥行き下書き を作る
echo  1) output\構図候補\構図名\ に残っている画像を 構図下書き元 に取り込む
echo  2) 構図下書き\depthref_構図名.png を作る（作ってあるものは飛ばす）
echo  3) 構図下書き\_元絵奥行き一覧.png で確認
echo  初回だけ推定モデル（約100MB）を自動ダウンロードします
echo ============================================
%PY% depth_from_ref.py %*
echo.
pause
