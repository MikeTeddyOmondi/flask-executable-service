import winreg
import subprocess

# Define the path to the Flask application's executable file or the bundled .exe file
app_path = r"D:\Projects\experimental-projects\flask_executable\dist\app.exe"

# Define the firewall rule name and description
rule_name = "Flask App"
rule_description = "Allows network access - Flask app"

# Create the firewall rule using netsh
subprocess.run(
    f"netsh advfirewall firewall add rule name='{rule_name}' dir=in action=allow program='{app_path}' enable=yes description='{rule_description}'", shell=True)
