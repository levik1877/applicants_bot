@echo off

call %~dp0application_bot\venv\Scripts\activate

cd %~dp0application_bot

python main.py

pause