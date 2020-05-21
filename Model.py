# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:08:04 2019

@author: André Moraes
"""
import pandas as pd

class curve:
    color = "#1559c6"
    
    def __init__(self, Name, curveX, curveY):
        self.curveName = Name
        self.curveX = curveX
        self.curveY = curveY
        
class dpv:
    def __init__(self):
        self.pIni = "-0.6"
        self.pFim = "0.0"
        self.pPas = "0.005"
        self.pPul = "0.01"
        self.tPul = "0.01"
        self.tPas = "0.025"
        self.tEqu = "5"
        self.fEsc = 0
