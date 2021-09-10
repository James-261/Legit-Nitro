import psutil
import time
from pynput import keyboard
import os

folder = os.path.dirname(os.path.abspath(__file__))

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

os.system("pythonw nitro.py")

while True:
    if checkIfProcessRunning('pythonw'):
        pass
    else:
        os.system("pythonw nitro.py")
