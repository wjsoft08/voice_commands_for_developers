# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:21:50 2019

@author: jenny
"""

import win32com.client
import win32api

def query_source_code(query):
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("IntelliJ IDEA")
    win32api.Sleep(5000)
    shell.SendKeys("^+f"+query)
    
def build():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("IntelliJ IDEA")
    win32api.Sleep(5000)
    shell.SendKeys("^{F9}")
    
def run():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("IntelliJ IDEA")
    win32api.Sleep(5000)
    shell.SendKeys("+{F10}")

def debug():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("IntelliJ IDEA")
    win32api.Sleep(5000)
    shell.SendKeys("+{F9}")
    
def indent():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("IntelliJ IDEA")
    win32api.Sleep(5000)
    shell.SendKeys("^a"+"^%I")