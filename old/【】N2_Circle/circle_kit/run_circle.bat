@echo off
chcp 65001 >nul
rem ComfyUI 同梱の python を使う。場所が違う場合はここを書き換える
set PY=..\python_embeded\python.exe
if not exist "%PY%" set PY=python
"%PY%" "%~dp0run_circle_batch.py" %*
pause
