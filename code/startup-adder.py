import os, getpass
from win32com.client import Dispatch
def createShortcut(path, target='', wDir=''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.save()

if __name__ == "__main__":
    try:
        user_name = getpass.getuser()
        current_directory = os.getcwd()
        source = current_directory + r"\programs\web-shortcut.exe"
        destination = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\web-shortcut.lnk".format(user_name) 
        createShortcut(
            path = destination,
            target = source,
            wDir = current_directory
        )
        print("The program has been added to startups successfully.\n")
        input("Press [ENTER] to exit...")
    except Exception as error:
        print("[ERROR]: An exception occured.")
        print("Please report this to the developer: {}\n".format(error))
        input("Press [ENTER] to exit...")