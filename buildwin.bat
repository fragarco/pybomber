@echo off
rmdir /S /Q build
rmdir /S /Q dist
pyinstaller -F --icon=".\src\assets\icon\bomber.ico" -w src\bomber.py
xcopy /Y /S .\src\assets .\dist\assets\
@echo on