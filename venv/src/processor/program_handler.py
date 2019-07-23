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

#'C:\Users\jenny\AppData\Local\Programs\Microsoft VS Code\Code.exe'
#path = input("Enter the path of your file: ")
#subprocess.call([path])

def open_notepad():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Run("Notepad++")
    
def close_notepad():
    os.system("taskkill /im notepad++.exe /f")
    
def open_visualStudioCode():
    path = 'C:\\Users\\jenny\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    subprocess.Popen([path])

def open_chrome():
    urL='https://www.google.com'
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(urL)
    return
       
def open_intelliJ():
    path = 'C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2018.1.6\\bin\\idea64.exe'
    subprocess.Popen([path])

def open_program(message):
    if message == "notepad":
        open_notepad()
    elif message == "visual studio code":
        open_visualStudioCode()
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