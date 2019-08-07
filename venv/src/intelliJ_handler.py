# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:21:50 2019

@author: jenny
"""

import win32com.client
import win32api
import pythoncom

def control_intelliJ(message):
    pythoncom.CoInitialize()
    
    if "query" in message or "search" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("IntelliJ IDEA")
        win32api.Sleep(5000)
        shell.SendKeys("^+f"+message.split("search ",1)[1])
    elif "build" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("IntelliJ IDEA")
        win32api.Sleep(5000)
        shell.SendKeys("^{F9}")
    elif "run" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("IntelliJ IDEA")
        win32api.Sleep(5000)
        shell.SendKeys("+{F10}")
    elif "debug" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("IntelliJ IDEA")
        win32api.Sleep(5000)
        shell.SendKeys("+{F9}")
    elif "indent" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("IntelliJ IDEA")
        win32api.Sleep(5000)
        shell.SendKeys("^%L")