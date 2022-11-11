# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:54:44 2022

@author: harpreet.singh
"""

from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Serial Communication")
        self.root.geometry("360x120")
        self.root.config(bg="white")
        
        
class ComGui():
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(root, text="Com Manager", padx=5, pady=5, bg ="white" )
    def publish(self):
        self.frame.grid(row=0,column=0, rowspan=3, columnspan=3, padx=5,pady=5)
        
        
        
        
if __name__ == "__main__":
    RootGUI()