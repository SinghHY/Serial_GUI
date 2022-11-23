# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:33:47 2022

@author: harpreet.singh
"""

import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


import serial
import time

serialcomm = serial.Serial('COM3', 115200)

serialcomm.timeout = 1

while True:

    i = input("Enter Input: ").strip()
    
    if i == "Done":

        print('finished')

        break

    serialcomm.write(i.encode())

    time.sleep(0.5)

    print(serialcomm.readline().decode('ascii'))
    print(serialcomm.readline().decode('ascii'))
    print(serialcomm.readline().decode('ascii'))
    
serialcomm.close()