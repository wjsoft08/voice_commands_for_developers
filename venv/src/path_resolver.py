# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:31:37 2019

@author: jenny
"""
import subprocess

path_file = open("path.txt", "r")

d = {}
for line in path_file.readlines():
    (key, val) = line.split("=")
    d[key] = val

path_file.close()

subprocess.call([d['Visual Studio Code']])