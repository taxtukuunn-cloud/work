@echo off
cd /d "%~dp0"
set PY="%USERPROFILE%\Downloads\ComfyUI_windows_portable\python_embeded\python.exe"
if not exist %PY% set PY=python
rem 崩れやすい画像を3候補ずつ作り直す（output\Maid\_candidates\ に保存。pick_maid.bat で採用）
rem 必要に応じてキーを増減する
for %%K in (Maid_atk_m3 Maid_atk_boss Maid_lose_btl_m3 Maid_lose_onani_m3 Maid_lose_inochi_m3 Maid_lose_onedari_m3 Maid_lose_btl_boss Maid_lose_onedari_boss Maid_lose_onani_boss Maid_lose_inochi_boss Maid_atk_m2 Maid_atk_e2 Maid_lose_btl_e2 Maid_lose_onedari_e2 Maid_lose_inochi_e3 Maid_onanie_master Maid_onanie_boss) do (
  %PY% comfy_batch.py %%K --random --batch 3
)
echo 作り直し完了
pause
