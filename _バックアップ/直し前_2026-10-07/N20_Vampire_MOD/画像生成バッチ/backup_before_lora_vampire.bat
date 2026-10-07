@echo off
chcp 65001 >nul
cd /d "%~dp0"
rem LoRAで撮り直す前に、今の51枚と候補を「output\Vampire_beforeLoRA」へ控える（1回だけ。すでにあれば何もしない）
if exist "output\Vampire_beforeLoRA\Vampire_master.png" (
  echo すでに控えがあります： output\Vampire_beforeLoRA
) else (
  mkdir "output\Vampire_beforeLoRA" 2>nul
  mkdir "output\Vampire_beforeLoRA\_candidates" 2>nul
  copy /Y "output\Vampire\*.png" "output\Vampire_beforeLoRA\" >nul
  copy /Y "output\Vampire\_candidates\*.png" "output\Vampire_beforeLoRA\_candidates\" >nul
  echo 控えました： output\Vampire_beforeLoRA
)
dir /b "output\Vampire_beforeLoRA\*.png" | find /c ".png"
