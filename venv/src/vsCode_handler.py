# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:19:54 2019

@author: jenny
"""

import win32com.client
import win32api
import pythoncom

def control_VScode(message):
    pythoncom.CoInitialize()
    
    if "query" in message or "search" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Visual Studio Code")
        win32api.Sleep(5000)
        shell.SendKeys("^+f"+message.split("search ",1)[1]+"~")
    elif "run" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Visual Studio Code")
        win32api.Sleep(5000)
        shell.SendKeys("^{F5}")
    elif "debug" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Visual Studio Code")
        win32api.Sleep(5000)
        shell.SendKeys("{F5}")