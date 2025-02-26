import os
import sys

# Folder to lock/unlock (passed as an argument)
folder_path = sys.argv[1] if len(sys.argv) > 1 else ""

# Predefined password (Change it as needed)
PASSWORD = "12345"

def lock_folder():
    """Locks the folder and all its contents by denying access to all users."""
    os.system(f'icacls "{folder_path}" /deny Everyone:F')
    os.system(f'icacls "{folder_path}\\*" /deny Everyone:F')
    print("Folder and all files locked! Access Denied.")

def unlock_folder():
    """Unlocks the folder and all files after password verification."""
    entered_password = input("Enter Password to Unlock: ")
    if entered_password == PASSWORD:
        os.system(f'icacls "{folder_path}" /grant Everyone:F')
        os.system(f'icacls "{folder_path}\\*" /grant Everyone:F')
        print("Folder and all files unlocked! Full Access Restored.")
    else:
        print("Incorrect Password! Access Denied.")

# Check if the folder is locked
if os.system(f'icacls "{folder_path}" | findstr /C:"Everyone:(N)"') == 0:
    unlock_folder()
else:
    lock_folder()
