# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:11:05 2019

@author: jenny
"""

import win32com.client
import win32api
import pythoncom

def control_eclipse(message):
    pythoncom.CoInitialize()
    
    if "query" in message or "search" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Eclipse")
        win32api.Sleep(5000)
        shell.SendKeys("^h"+message.split("search ",1)[1]+"~")
    elif "run" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Eclipse")
        win32api.Sleep(5000)
        shell.SendKeys("^{F11}")
    elif "debug" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Eclipse")
        win32api.Sleep(5000)
        shell.SendKeys("{F11}")
    elif "indent" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Eclipse")
        win32api.Sleep(5000)
        shell.SendKeys("^a^i")
    elif "coverage" in message:
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("Eclipse")
        win32api.Sleep(5000)
        shell.SendKeys("^+{F11}")