#!/bin/zsh
pyinstaller src/bomber.py -n Bomber --windowed --noconfirm --clean --icon="src/assets/icon/bomber.icns" --add-data="src/assets:assets"