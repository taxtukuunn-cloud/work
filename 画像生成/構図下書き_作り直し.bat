@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  構図の下書きを作り直す（pose_templates.py の骨格 → Blender の 3D 人体で奥行き）
echo  出力: 構図下書き\depth3d_^<下書き^>.png と ComfyUI\input\pose_depth3d_^<下書き^>.png
echo ============================================
%PY% pose_templates.py
"%USERPROFILE%\Downloads\Blender\blender-4.2.23-windows-x64\blender.exe" --background --python depth_blender.py
for %%F in ("%~dp0構図下書き\depth3d_*.png") do copy /y "%%F" "%COMFY_DIR%\ComfyUI\input\pose_%%~nxF" >nul
echo.
echo 完了。
pause
