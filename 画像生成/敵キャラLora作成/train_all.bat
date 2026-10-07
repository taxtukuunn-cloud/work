@echo off
chcp 65001 >nul
setlocal

rem ===== ここの2行だけ自分の環境に合わせて書き換える =====
set "SD_SCRIPTS=C:\path\to\sd-scripts"
set "BASE_MODEL=C:\path\to\illustrious_or_noobai.safetensors"
rem =======================================================

set "ROOT=%~dp0"
if not exist "%SD_SCRIPTS%\sdxl_train_network.py" (
  echo SD_SCRIPTS の場所が違います: %SD_SCRIPTS%
  pause
  exit /b 1
)
if not exist "%BASE_MODEL%" (
  echo BASE_MODEL が見つかりません: %BASE_MODEL%
  pause
  exit /b 1
)
if exist "%SD_SCRIPTS%\venv\Scripts\activate.bat" call "%SD_SCRIPTS%\venv\Scripts\activate.bat"
cd /d "%SD_SCRIPTS%"

rem train フォルダ内のキャラを順番に学習。学習済み(outputに完成ファイルあり)は飛ばす。
for /d %%C in ("%ROOT%train\*") do (
  if exist "%ROOT%output\%%~nxC_v1.safetensors" (
    echo [skip] %%~nxC は学習済み
  ) else (
    echo [train] %%~nxC
    accelerate launch sdxl_train_network.py --config_file "%ROOT%train_config.toml" --pretrained_model_name_or_path "%BASE_MODEL%" --train_data_dir "%%C\img" --output_dir "%ROOT%output" --output_name "%%~nxC_v1"
  )
)
echo 完了
pause
