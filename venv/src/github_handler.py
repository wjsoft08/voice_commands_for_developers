# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:47:00 2019

@author: jenny
"""

import win32com.client
import win32api
import subprocess
import pythoncom

def open_github():
    path = 'C:\\Users\\jenny\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
    subprocess.Popen([path])

def control_github(message):
    pythoncom.CoInitialize()
    
    if "on" in message:
        open_github()
    elif "pull" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(5000)
        shell.SendKeys("^+p")
    elif "push" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(5000)
        shell.SendKeys("^p")
    elif "pull request" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(5000)
        shell.SendKeys("^r")
    elif "view" in message and "git hub" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(5000)
        shell.SendKeys("^+g")
    elif "update" in message and "master" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(5000)
        shell.SendKeys("^+u")
    elif "commit" in message:
        m = message.split("commit ",1)[1]
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("GitHub Desktop")
        win32api.Sleep(500)
        shell.SendKeys("^,")
        win32api.Sleep(500)
        shell.SendKeys("{ESC}")
        win32api.Sleep(1000)
        shell.SendKeys("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}"+m)
        win32api.Sleep(1000)
        shell.SendKeys("{TAB}{TAB}" + "{ENTER}")
        win32api.Sleep(1000)
    elif "show" in message:
        if "repository" in message:
            print(message)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.AppActivate("GitHub Desktop")
            win32api.Sleep(5000)
            shell.SendKeys("^t")
        elif "commit history" in message:
            print(message)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.AppActivate("GitHub Desktop")
            win32api.Sleep(5000)
            shell.SendKeys("^2")
        elif "branches" in message:
            print(message)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.AppActivate("GitHub Desktop")
            win32api.Sleep(5000)
            shell.SendKeys("^b")
        