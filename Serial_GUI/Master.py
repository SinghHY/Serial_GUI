# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:55:17 2022

@author: harpreet.singh
"""
from GUI_Master import RootGUI, ComGui

RootMaster = RootGUI()
ComMaster = ComGui(RootMaster.root)
RootMaster.root.mainloop()
