@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% (
  echo ComfyUI 付属の Python が見つかりません: %PY%
  echo ComfyUI の場所が変わった場合は、この bat の PY の行を書き換えてください。
  pause
  exit /b 1
)
echo ============================================
echo  MOD まとめツール
echo  ブラウザに画面が開きます（開かない時は http://127.0.0.1:8765/ ）
echo  この黒い画面を閉じるとツールが止まります
echo ============================================
%PY% app.py
pause
