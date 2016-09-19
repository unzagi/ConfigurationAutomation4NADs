@echo on & setlocal
set "MySearchString='action=edit'"
for /f "delims=" %%i in ('dir /b /s /a-d ^| findstr /i "MySearchString"') do echo del "%%~i"