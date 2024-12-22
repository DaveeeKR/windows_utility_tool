import subprocess
import sys
import ctypes
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
        logging.info("Opened as admin")
        sys.exit(0)
    except:
        logging.error("Failed to open as admin")
        sys.exit(1)
    

def set_execution_policy():
    try:
        command = "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
        subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Execution policy set to RemoteSigned")
    except:
        logging.error("Failed to set execution policy")
        sys.exit(1)

def activate_windows():
    try:
        commands = [
            "slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
            "slmgr /skms kms8.msguides.com",
            "slmgr /ato"
        ]   

        for command in commands:
            subprocess.Popen(["powershell", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Executing command: {command}")
            time.sleep(3)
    except:
        logging.error("Failed to activate Windows")
        sys.exit(1)

def remove_bloatware():
    try:
        commands = [
            "Get-AppxPackage *Cortana* | Remove-AppxPackage",
            "Get-AppxPackage *Family* | Remove-AppxPackage",
            "Get-AppxPackage *Copilot* | Remove-AppxPackage",
            "Get-AppxPackage *Mail* | Remove-AppxPackage",
            "Get-AppxPackage *DevHome* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsAlarms* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsCamera* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsCommunicationApps* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsFeedbackHub* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsMaps* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsSoundRecorder* | Remove-AppxPackage",
            "Get-Appxpackage *WindowsContacts* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsFeedback* | Remove-AppxPackage",
            "Get-AppxPackage *WindowsPhone* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftTeams* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftOneNote* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftStickyNotes* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftWhiteboard* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftSolitaireCollection* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftSkypeApp* | Remove-AppxPackage",
            "Get-AppxPackage *MicrosoftPeople* | Remove-AppxPackage",
            "Get-AppxPackage *Clipchamp* | Remove-AppxPackage",
            "Get-AppxPackage *Bing* | Remove-AppxPackage",
            "Get-AppxPackage *PowerAutomate* | Remove-AppxPackage",
            "Get-AppxPackage *LinkedIn* | Remove-AppxPackage",
            "Get-AppxPackage *Todo* | Remove-AppxPackage",
            "Get-AppxPackage *YourPhone* | Remove-AppxPackage",
            "Get-AppxPackage *Outlook* | Remove-AppxPackage",
            "winget uninstall Microsoft.OneDrive"
            "winget uninstall cortana"
        ]

        for command in commands:
            subprocess.Popen(["powershell", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info(f"Executing command: {command}")
            time.sleep(3)
    except:
        logging.error("Failed to remove bloatware")
        sys.exit(1)


if __name__ == "__main__":
    if not is_admin():
        run_as_admin()

    set_execution_policy()
    time.sleep(3)
    activate_windows()
    time.sleep(3)
    remove_bloatware()


