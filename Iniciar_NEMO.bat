@echo off
title N.E.M.O. - Assistente Proelium

echo ==============================
echo   INICIANDO N.E.M.O.
echo   Assistente Proelium
echo ==============================
echo.

cd /d G:\NEMO

echo Ativando ambiente virtual...
call Sistema\venv\Scripts\activate

echo.
echo Iniciando memoria operacional...
echo.

python Sistema\nemo.py

pause