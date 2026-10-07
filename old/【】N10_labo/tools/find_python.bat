@echo off
rem ComfyUI の Python を探して PY に入れる（run_lab / gen_Lab_all / install_lab から呼ばれる）
set PY=
set CFG=%~dp0comfy_path.txt

rem 1) 前回保存した場所
if exist "%CFG%" (
  set /p SAVED=<"%CFG%"
)
if defined SAVED call :try "%SAVED%"
if defined PY goto :eof

rem 2) よくある場所
for %%D in (
  "%~dp0..\.."
  "%~dp0..\..\.."
  "C:\ComfyUI_windows_portable"
  "D:\ComfyUI_windows_portable"
  "E:\ComfyUI_windows_portable"
  "C:\ComfyUI"
  "D:\ComfyUI"
  "%USERPROFILE%\ComfyUI_windows_portable"
  "%USERPROFILE%\Desktop\ComfyUI_windows_portable"
  "%USERPROFILE%\Downloads\ComfyUI_windows_portable"
  "%USERPROFILE%\Documents\ComfyUI"
) do (
  if not defined PY call :try %%D
)
if defined PY goto :save

rem 3) 見つからなければ聞く
echo.
echo ComfyUI のフォルダが見つかりませんでした。
echo ComfyUI のフォルダ（run_nvidia_gpu.bat がある場所）をこの画面にドラッグして Enter を押してください。
set IN=
set /p IN=^> 
if not defined IN goto :notfound
set IN=%IN:"=%
call :try "%IN%"
if defined PY goto :save
:notfound
echo.
echo その場所に python が見つかりませんでした。
echo   ポータブル版: フォルダ内に python_embeded\python.exe があるか確認してください。
echo   デスクトップ版: フォルダ内に .venv\Scripts\python.exe があるか確認してください。
goto :eof

:save
>"%CFG%" echo %FOUND%
echo Python: %PY%
goto :eof

:try
set D=%~1
if "%D%"=="" goto :eof
if exist "%D%\python_embeded\python.exe" (set PY=%D%\python_embeded\python.exe& set FOUND=%D%& goto :eof)
if exist "%D%\.venv\Scripts\python.exe" (set PY=%D%\.venv\Scripts\python.exe& set FOUND=%D%& goto :eof)
if exist "%D%\venv\Scripts\python.exe" (set PY=%D%\venv\Scripts\python.exe& set FOUND=%D%& goto :eof)
if exist "%D%\ComfyUI_windows_portable\python_embeded\python.exe" (set PY=%D%\ComfyUI_windows_portable\python_embeded\python.exe& set FOUND=%D%\ComfyUI_windows_portable& goto :eof)
goto :eof
