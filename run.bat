@echo off
set FLASK_APP=.\code\hello.py
set /p FLASK_DEBUG="Enable debug? enter 1 to enable"\n
flask run -h 0.0.0.0 -p 80
pause