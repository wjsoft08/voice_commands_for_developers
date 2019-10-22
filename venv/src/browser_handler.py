# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:19:18 2019

@author: jenny
"""

import webbrowser

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    
def stack_overflow_search(issue):
    urL='https://stackoverflow.com/search?q='+issue
    webbrowser.get('chrome').open_new_tab(urL)

def open_chrome():
    urL='https://www.google.com'
    webbrowser.get('chrome').open_new_tab(urL)

    # https: // www.google.com / search?q =