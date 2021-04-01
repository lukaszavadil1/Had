@ECHO off
    ECHO Vítejte u instalace Hada!
    PAUSE

    ECHO Vytváření virtuálního prostředí...
    call python -m venv env
    cd env/Scripts
    call activate.bat
    cd ../..
    ECHO Instalace requirements...
    call pip install -r requirements.txt
