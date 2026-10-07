@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
rem 崩れた画像を、直したプロンプトで3候補ずつ作り直す（output\Heels\_candidates\）
for %%K in (Heels_atk_m1 Heels_atk_m2 Heels_atk_m3 Heels_lose_btl_m1 Heels_lose_onani_m1 Heels_lose_inochi_m1 Heels_lose_btl_m2 Heels_lose_onani_m2 Heels_lose_onedari_m2 Heels_lose_btl_m3 Heels_lose_onani_m3 Heels_lose_inochi_m3 Heels_lose_onedari_m3 Heels_lose_btl_e1 Heels_lose_onani_e1 Heels_lose_inochi_e1 Heels_lose_btl_e2 Heels_lose_onani_e2 Heels_lose_inochi_e2 Heels_lose_onedari_e2) do (
  %PY% comfy_batch.py %%K --random --batch 3
)
echo 作り直し完了
