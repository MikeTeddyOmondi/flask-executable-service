@echo off
:: Run the script to configure the Windows Firewall with administrative privileges
echo Configuring Windows Firewall...
powershell -Command "Start-Process -Verb runAs python net_access.py"

:: Install the Flask application as a Windows service using sc
echo Installing app as a service...
sc create FlaskBin binPath="%cd%\dist\app.exe" start=auto
sc description FlaskBin "Flask Windows service"

echo Starting service...
sc start FlaskBin

echo Done!