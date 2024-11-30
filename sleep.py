import os

def sleep_computer():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

sleep_computer()
