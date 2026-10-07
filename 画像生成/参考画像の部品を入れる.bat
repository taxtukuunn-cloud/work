@echo off
setlocal
set "COMFY=%USERPROFILE%\Downloads\ComfyUI_windows_portable\ComfyUI"
if not exist "%COMFY%\custom_nodes" (
  echo [中止] ComfyUI のフォルダが見つかりません: %COMFY%
  pause & exit /b 1
)
echo  参考画像（IP-Adapter）の部品を入れます。合計 約3.4GB のダウンロードです。
echo  ※ ComfyUI は閉じてから実行してください。
echo.

echo [1/3] 拡張機能 ComfyUI_IPAdapter_plus
if exist "%COMFY%\custom_nodes\ComfyUI_IPAdapter_plus\__init__.py" (
  echo   もう入っています。飛ばします。
) else (
  curl -L --fail -o "%TEMP%\ipadapter_plus.zip" https://github.com/cubiq/ComfyUI_IPAdapter_plus/archive/refs/heads/main.zip || goto err
  tar -xf "%TEMP%\ipadapter_plus.zip" -C "%COMFY%\custom_nodes" || goto err
  ren "%COMFY%\custom_nodes\ComfyUI_IPAdapter_plus-main" ComfyUI_IPAdapter_plus || goto err
  del "%TEMP%\ipadapter_plus.zip"
)

echo [2/3] 絵を読み取るモデル（約2.5GB）
if not exist "%COMFY%\models\clip_vision" mkdir "%COMFY%\models\clip_vision"
if exist "%COMFY%\models\clip_vision\CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors" (
  echo   もう入っています。飛ばします。
) else (
  curl -L --fail -o "%COMFY%\models\clip_vision\CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors.part" https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/model.safetensors || goto err
  ren "%COMFY%\models\clip_vision\CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors.part" CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors || goto err
)

echo [3/3] 参考画像を効かせるモデル（約0.85GB）
if not exist "%COMFY%\models\ipadapter" mkdir "%COMFY%\models\ipadapter"
if exist "%COMFY%\models\ipadapter\ip-adapter-plus_sdxl_vit-h.safetensors" (
  echo   もう入っています。飛ばします。
) else (
  curl -L --fail -o "%COMFY%\models\ipadapter\ip-adapter-plus_sdxl_vit-h.safetensors.part" https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors || goto err
  ren "%COMFY%\models\ipadapter\ip-adapter-plus_sdxl_vit-h.safetensors.part" ip-adapter-plus_sdxl_vit-h.safetensors || goto err
)

echo.
echo  終わりました。入ったもの：
dir /b "%COMFY%\custom_nodes" | findstr /i IPAdapter
dir "%COMFY%\models\clip_vision\CLIP-ViT-H*" | findstr /i safetensors
dir "%COMFY%\models\ipadapter\ip-adapter*" | findstr /i safetensors
echo.
echo  このあと ComfyUI を起動し直してください。
pause
exit /b 0
:err
echo.
echo [失敗] 途中で止まりました。この画面を写して Claude に見せてください。
pause
exit /b 1
