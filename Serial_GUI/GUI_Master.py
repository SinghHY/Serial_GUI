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
        self.label_com = Label(
            self.frame, text="Availabel Port(s): ", bg = "white", width=15, anchor="w")
        self.label_bd = Label(
            self.frame, text="Baud Rate: ", bg = "white", width=15, anchor="w")
        
        self.publish()
        
    def publish(self):
        self.frame.grid(row=0,column=0, rowspan=3, columnspan=3, padx=5,pady=5)
        self.label_com.grid(column=1, row=2)
        self.label_bd.grid(column=1, row=3)
        
        
if __name__ == "__main__":
    RootGUI()