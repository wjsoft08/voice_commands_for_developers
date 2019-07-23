# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:47:00 2019

@author: jenny
"""

import win32com.client
import win32api
import subprocess

def open_github():
    path = 'C:\\Users\\jenny\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe'
    subprocess.Popen([path])

def pull():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^+p")
    
def push():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^p")
    
def view_on_github():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^+g")
    
def update_from_master():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^+u")

def pull_request():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^r")
    
def show_repository():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^t")
    
def show_commit_history():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^2")
    
def show_branches():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("GitHub Desktop")
    win32api.Sleep(5000)
    shell.SendKeys("^b")
    
def control_github(message):
    if "on" in message:
        open_github()
    elif "pull" in message:
        pull()
    elif "push" in message:
        push()
    elif "pull request" in message:
        pull_request()
    elif "view" in message and "git hub" in message:
        view_on_github()
    elif "update" in message and "master" in message:
        update_from_master()
    elif "show" in message:
        if "repository" in message:
            show_repository()
        elif "commit history" in message:
            show_commit_history()
        elif "branches" in message:
            show_branches()
        