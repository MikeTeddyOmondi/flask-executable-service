# Converting a Flask App to an Executable Binary

## Bundling the app with pyinstaller PyPi package

```sh
pyinstaller --onefile --noconsole --hidden-import=waitress app.py # Add --noconsole flag if you dont want your app not to write on the console
pyinstaller --onefile --hidden-import=waitress app.py 
```

## Install the Windows Service

```sh
sc create FlaskService binPath= "C:\path\to\app.exe" start= auto DisplayName= "Flask Service" 
```

## Start the Windows service

```sh
sc start FlaskService
```

## Use the batch  file to create and start the service

```powershell
.\run.bat
```

## To check for the service

```sh
sc qc FlaskBin # Service name
```
