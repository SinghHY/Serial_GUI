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
            self.frame, text="Availabel Port(s) : ", bg = "white", width=15, anchor="w")
        self.label_bd = Label(
            self.frame, text="Baud Rate : ", bg = "white", width=15, anchor="w")
        self.ComOptionMenu()
        self.BaudOptionMenu()
        
        self.padx = 20
        self.pady = 5  
        self.publish()
        
    def ComOptionMenu(self):
        coms = ["-", "COM3", "COM2", "COM6"]
        self.clicked_com = StringVar()
        self.clicked_com.set(coms[0])
        self.drop_com = OptionMenu(
            self.frame, self.clicked_com, *coms)
        self.drop_com.config(width=10)
        
    def BaudOptionMenu(self):
        self.clicked_bd = StringVar()
        bds = ["-",
              "300",
              "600",
              "1200",
              "2400",
              "4800",
              "9600",
              "14400",
              "19200",
              "28800",
              "38400",
              "56000",
              "57600",
              "115200",
              "128000",
              "256000"]
        self.clicked_bd.set(bds[0])
        self.drop_baud = OptionMenu(
            self.frame, self.clicked_bd, *bds)
        self.drop_baud.config(width=10)

    def publish(self):
        self.frame.grid(row=0,column=0, rowspan=3, columnspan=3, padx=5,pady=5)
        self.label_com.grid(column=1, row=2)
        self.drop_com.grid(column=2, row=2, padx=self.padx, pady=self.pady)
        self.label_bd.grid(column=1, row=3)
        self.drop_baud.grid(column=2, row=3)
        
if __name__ == "__main__":
    RootGUI()