@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo N31～N60 の場面プロンプト（技CG・敗北CG・オナニーCG の40場面）を
echo N31-N60_場面\scene_data から作り直して prompts\ に書き込みます。
echo （立ち絵・魔法・背景・女装娘はそのまま。最初の元ファイルは prompts_場面追加前\ に保存済み）
set /p MOD="MODコード（例 Onsen ／ 複数は Onsen,Oiran ／ Enterだけ＝30MOD全部）: "
%PY% "N31-N60_場面\build_scenes.py" %MOD%
pause
