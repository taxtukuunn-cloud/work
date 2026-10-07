@echo off
setlocal
cd /d "%~dp0"
set "COMFY_DIR=%USERPROFILE%\Downloads\ComfyUI_windows_portable"
set PY="%COMFY_DIR%\python_embeded\python.exe"
echo ============================================
echo  Š„‚è“–‚Ä‚ª•Ï‚í‚Á‚½ŠG‚ÌŽB‚è’¼‚µi2026-10-04j
echo  ŽB‚èÏ‚Ý‚ÌŠG‚Ì‚¤‚¿A‚¢‚Ü‚ÌŠ„‚è“–‚Ä‚Æˆá‚¤‰º‘‚«‚ÅŽB‚ç‚ê‚Ä‚¢‚éê–Ê‚¾‚¯‚ðŽB‚è’¼‚µ‚Ü‚·
echo  1) ‚¢‚Ü‚ÌŠ„‚è“–‚Ä‚ðo‚·iŽB‚ç‚¸‚É‘SMOD‚ð‘g‚Ý—§‚Ä‚éB2`3•ªj
echo  2) ŽB‚è’¼‚·ê–Ê‚Ìˆê——‚ðo‚·iŠ„‚è“–‚Ä‚ª•Ï‚í‚Á‚½ŠG_ˆê——.csvj
echo  3) ˆê——‚ðŒ©‚ÄA‚æ‚¯‚ê‚ÎƒL[‚ð‰Ÿ‚·‚ÆŽB‚è’¼‚µ‚ªŽn‚Ü‚è‚Ü‚·iŽ~‚ß‚é‚Æ‚«‚Í‚±‚Ì‰æ–Ê‚ð•Â‚¶‚éj
echo  Œ³‚ÌŠG‚ÍÁ‚µ‚Ü‚¹‚ñi”Ô†‚ª‘‚¦‚½V‚µ‚¢ŠG‚ª‚Å‚«‚Ü‚·j
echo ============================================
%PY% gen.py all all --model wai --preview
echo.
%PY% "Š„‚è“–‚Ä‚ª•Ï‚í‚Á‚½ŠG‚ÌŽB‚è’¼‚µ.py" --dry-run
echo.
echo ‚±‚±‚Ü‚Å‚Í‰½‚àŽB‚Á‚Ä‚¢‚Ü‚¹‚ñBŽB‚è’¼‚·‚È‚çƒL[‚ð‰Ÿ‚µ‚Ä‚­‚¾‚³‚¢B‚â‚ß‚é‚È‚ç‚±‚Ì‰æ–Ê‚ð•Â‚¶‚Ä‚­‚¾‚³‚¢B
pause
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI ‚ð‹N“®‚µ‚Ü‚·...
start "ComfyUI" /D "%COMFY_DIR%" cmd /k run_nvidia_gpu.bat
:wait
timeout /t 5 /nobreak >nul
curl -s -o nul http://127.0.0.1:8188/ && goto ready
echo ComfyUI ‚Ì‹N“®‚ð‘Ò‚Á‚Ä‚¢‚Ü‚·...
goto wait
:ready
rem  ˆê•”‚ÌMOD‚¾‚¯ŽB‚è’¼‚·‚Æ‚«‚ÍA‰º‚Ìs‚Ì––”ö‚É MOD–¼‚ðƒJƒ“ƒ}‹æØ‚è‚Å‘«‚·i—á: ... ŽB‚è’¼‚µ.py" Clinic,Candyj
%PY% "Š„‚è“–‚Ä‚ª•Ï‚í‚Á‚½ŠG‚ÌŽB‚è’¼‚µ.py"
echo %date% %time%  Š„‚è“–‚Ä‚ª•Ï‚í‚Á‚½ŠG‚ÌŽB‚è’¼‚µ  I—¹ƒR[ƒh %errorlevel% >> "‘SMODŽB‰e_‹L˜^.txt"
echo.
pause
