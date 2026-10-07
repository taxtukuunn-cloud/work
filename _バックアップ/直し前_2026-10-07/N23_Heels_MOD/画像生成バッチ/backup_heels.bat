@echo off
cd /d "%~dp0"
rem LoRAで撮り直す前の画像を output\Heels_LoRA前 に残す（すでにあれば何もしない）
if exist "output\Heels_LoRA前\Heels_master.png" (
  echo バックアップは作成済みです： output\Heels_LoRA前
) else (
  xcopy "output\Heels" "output\Heels_LoRA前\" /E /I /Y >nul
  echo バックアップしました： output\Heels_LoRA前
)
