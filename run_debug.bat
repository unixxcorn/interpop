@echo off
set FLASK_APP=.\code\website.py
set FLASK_DEBUG=1
flask run -h 0.0.0.0 -p 80
pause