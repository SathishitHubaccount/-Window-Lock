# -Window-Lock
**Window Lock** is a Python script that locks and unlocks folders on Windows using `icacls`, restricting access until a password is entered. It also adds a right-click menu option for quick folder security.

# To use these option first add the option to the windows by running the lock.reg file 
  Then you can see a option in your folder menu to lock and unlock 
  You can change the password in the floder_lock.py file

# Window Lock

## **Project Overview**
Window Lock is a Python-based script designed to control access to folders on Windows systems by modifying folder permissions using the `icacls` command. The script allows users to lock and unlock folders with a predefined password, ensuring restricted access to sensitive files.

Additionally, the project includes a Windows Registry file that adds **"Lock/Unlock Folder"** options to the right-click context menu for easier usability.

## **Features**
- Restricts access to a specified folder and its contents.
- Unlocks the folder upon correct password entry.
- Provides a command-line interface for direct execution.
- Adds **"Lock/Unlock Folder"** options to the Windows right-click context menu.
- Uses built-in Windows commands, requiring no external dependencies.

## **System Requirements**
- Windows operating system
- Python 3.x installed
- Administrative privileges to modify folder permissions
- Registry modification permissions (for adding the context menu option)
