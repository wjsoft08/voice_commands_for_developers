# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:31:15 2019

@author: jenny
"""

import subprocess
import win32com.client
import os
import webbrowser
import psutil
import pythoncom

d = {}
    
def close_notepad():
    os.system("taskkill /im notepad++.exe /f")
    
def open_visualStudioCode():
    global d
    path = d['VSCode'].rstrip()
    print(path)
    subprocess.Popen(path)
#    path = 'D:\\Program Files (x86)\\Microsoft VS Code\\Code.exe'
#    subprocess.Popen([path])

def open_chrome():
    urL='https://www.google.com'
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(urL)
    return

def open_eclipse():
    global d
    path = d['Eclipse'].rstrip()
    print(path)
    subprocess.Popen(path)
    #    path = 'C:\\Users\\User\\eclipse\\java-oxygen\\eclipse\\eclipse.exe'
    #    subprocess.Popen([path])
       
def open_intelliJ():
    global d
    path = d['IntelliJ'].rstrip()
    print(path)
    subprocess.Popen(path)
#    path = 'D:\\Program Files (x86)\\JetBrains\\IntelliJ IDEA 2018.2.3\\bin\\idea64.exe'
#    subprocess.Popen([path])

def open_github():
    path = 'C:\\Users\\User\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
    subprocess.Popen([path])
    
def open_program(message):
    
    path_file = open("filePaths.txt", "r")

    global d
    for line in path_file.readlines():
        (key, val) = line.split("=")
        d[key] = val
    
    path_file.close()

    pythoncom.CoInitialize()
    
    if "notepad" in message:
        print(message)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.Run("Notepad++")
    elif message == "visual studio code":
        open_visualStudioCode()
    elif message == "eclipse":
        open_eclipse()
    elif "git" in message or "github" in message or "git hub" in message:
        open_github()
    elif "intellij" in message or "intelli j" in message:
        open_intelliJ()
    elif message == "chrome" or message == "browser":
        open_chrome()

def close_program(message):    
    if message == "notepad":
        program = "notepad++.exe"
    elif message == "visual studio code":
        program = "Code.exe"
    elif message == "chrome" or message == "browser":
        program = "chrome.exe"
    elif message == "I D E" or message == "intelli J" or message == "intelliJ":
        program = "idea64.exe"
    os.system("taskkill /im " + program + " /f")
    
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;