@echo off
setlocal
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
echo ============================================
echo  人物の範囲の直し（2026-10-04 追加した元絵の分だけ）
echo  ・peg_stand_behind_b_3 … 主人公と相手が逆 → 入れ替え
echo  ・two_ で始まる6枚 … 相手が2人の構図 → 範囲を使わない
echo ============================================
%PY% make_region_masks.py --only peg_stand_behind_b_3,two_stand_sandwich,two_seated_sides,two_seated_sides_2,two_lying_above,two_low_close,two_pov_lying
echo.
pause
