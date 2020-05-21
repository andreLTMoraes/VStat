# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:08:04 2019

@author: Aluno
"""
import sys

import win32com.client as winp

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import savgol_filter


import serial as sr
import time

import glob

import Model as md
import pandas as pd

devicePort = None
vstat = None
receivedCurveName = 0

""" Validation Controller """
class validation:
    global w, rt
    def __init__(self, widget, root):
        global w, rt
        w = widget
        rt = root
    
    @staticmethod
    def updateInfo(pIni, pFim, pPas, tPas):
                
        if (tPas and pPas > 0.0) and hasattr(w, "et_nPontos") :
            #sRate = str(round(pPas/tPas, 2))
            nPnt = str(round(abs(pFim-pIni)/pPas))
            tEst = str(abs(pFim-pIni)/(pPas/tPas))
            
            w.et_sRate.configure(state = "normal")
            w.et_sRate.delete(0, "end")
            w.et_sRate.insert("end", round(pPas/tPas, 2))
            w.et_sRate.configure(state = "disable")
            
            w.et_tEstimado.configure(state = "normal")
            w.et_tEstimado.delete(0, "end")
            w.et_tEstimado.insert("end", tEst)
            w.et_tEstimado.configure(state = "disabled")
            
            w.et_nPontos.configure(state = "normal")
            w.et_nPontos.delete(0, "end")
            w.et_nPontos.insert("end", nPnt)
            w.et_nPontos.configure(state = "disabled")
                    
        
    def entryValidate(self, d, i, P, S, W):
        if len(S) > 1: return False
        # Limita aos caracteres aceitos 47-48(0-9), 46(.) e 45(-)
        if ord(S) > 47 and ord(S) < 58 or ord(S) == 46 or ord(S) == 45:
            
            # Permite apagar acima de qualquer outra condição
            if int(d) == 0: return True
            # Se o sinal de negativo não for o inicial
            if ord(S) == 45 and int(i): return False
            # Se já existe ponto na entrada, se o ponto não vem no inicio ou depois do -
            if ord(S) == 46 and ("." in P[:-1] or int(i) < 1 or P[:-1] == "-"): return False
            
            if w.fr_analise.config()["text"][4] == "DPV":
                wd = rt.nametowidget(W)
                try:
                    pIni = float(w.et_PInicio.get())
                    pFim = float(w.et_PFim.get())
                    pPas = float(w.et_PPasso.get())
                    tPas = float(w.et_tPasso.get())
                    
                    if wd is w.et_PInicio:
                        self.updateInfo(float(P), pFim, pPas, tPas)
                    elif wd is w.et_PFim:
                        self.updateInfo(pIni, float(P), pPas, tPas)
                    elif wd is w.et_PPasso:
                        self.updateInfo(pIni, pFim, float(P), tPas)
                    elif wd is w.et_tPasso:
                        self.updateInfo(pIni, pFim, pPas, float(P))
                except ValueError:
                    pass # Algumdos valores ainda não é considerado float 
                    
            return True
        else:
            return False
        
    def entryInsert(et, value):
        for c in value:
            et.insert("end", c)

""" File Controller """
class file:
    def importCsv(caminho):
        name = caminho.split("/")
        name = name[len(name)-1]
        d = pd.read_csv(caminho, header = None)
        csv = md.curve(name[:-4], d.iloc[:,-2].values, d.iloc[:,-1].values)
        
        return csv
    
    def exportCsv(curve, name):
        pd.DataFrame(curve.curveY, curve.curveX).to_csv(name)
        #curve.curveData.to_csv(name)
        

""" Connection Controller """
class connection:
    def connect():
        global devicePort
        if sys.platform.startswith('win'):
            wmi = winp.GetObject("winmgmts:")
            for serial in wmi.InstancesOf("Win32_SerialPort"):
               if "Silicon Labs CP210x USB to UART Bridge" in serial.Name:
                   # Fazer procedimento adicional pra certificar que é o potenciostato
                   devicePort = serial.DeviceID
                   return devicePort
                   
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        return None
    
    def disconnect():
        global devicePort
        if devicePort:
            comunication = sr.Serial(devicePort)
            comunication.close()
            devicePort = None
            
    def openPort():
        global vstat
        if devicePort:
            vstat = sr.Serial(devicePort, 115200)
            time.sleep(1)
        else:
            return -1
        
    def closePort():
        vstat.close()
        
""" Transmition Controller """
class transmition:
    @staticmethod
    def flush():
        global vstat
        vstat.flushInput()
        vstat.flushOutput()
        
    @staticmethod
    def start_send():
        global vstat
        
        transmition.flush();
        a = vstat.write(bytes("start".encode("UTF-8")))
        print(a)
        print("vai entrar no loop...")
        while(1): #Loop que espera o recebimento do 'start' como confirmação para envio dos parâmetros
            print("loop...")
            data = vstat.readline()[:-2]
            if data:
                print(data)
                if bytes.decode(data).find("start") != -1:
                    print("ACK start OK")
                    break
                
    @staticmethod
    def start_receive():
        global vstat
        while(1): #Loop que espera o recebimento do 'start' como confirmação para envio dos parâmetros
            data = vstat.readline()[:-2]
            if data:
                print(data)
                if bytes.decode(data).find("start") != -1:
                    vstat.write(bytes("start".encode()))
                    print("ACK start OK")
                    break
                
    @staticmethod
    def end_receive():
        global vstat
        while(1): #Loop que espera o recebimento do 'end' como confirmação para envio dos parâmetros
            data = vstat.readline()[:-2]
            if data:
                print(data)
                if bytes.decode(data).find("end") != -1:
                    print("ACK end OK")
                    break
                
    def transmit(fEsc, pIni, pFim, pPul, pPas, tPul, tPas, tEqu):
        global vstat
        
        # Conversão interface -> potenciostato
        pIni = str(-float(pIni))
        pFim = str(-float(pFim))
        pPul = str(int(float(pPul)*1000))
        pPas = str(-int(float(pPas)*1000))
        tPul = str(int(float(tPul)*1000))
        tPas = str(int(float(tPas)*1000))
        
        transmition.start_send()
        
        data_to_send = fEsc+"/"+pIni+"/"+pFim+"/"+pPas+"/"+pPul+"/"+tPul+"/"+tPas+"/"+tEqu+"/e"
        print(data_to_send)
        ret = vstat.write(bytes(data_to_send.encode()))
        print(ret)
        #transmition.end_receive()
    
    def receive(curvePlot, subPlot, canvas, fe, pIni, pPas):
        global vstat, receivedCurveName
        
        y2 = np.array([])#criando array vazio que vai receber o Y2 (ou I2) do ESP
        y1 = np.array([])#criando array vazio que vai receber o Y1 (ou I1) do ESP
        y = np.array([])#criando array vazio que vai receber o Y do ESP
        x = np.array([])#criano array correspondente as coordenadas X
        stData = ""
        
        print("subPlot dentro:")
        print(subPlot)
        
        receivedCurveName += 1
        
        curve = np.take(curvePlot, 1)
        curve.curveName = "Untitle-"+str(receivedCurveName)
        subPlot.set_title(curve.curveName)
        canvas.draw()
        
        transmition.start_receive()
        
        while(1): #Loop que armazena os dados e encerra ao receber o 'end'    
            data = vstat.readline()[:-2] #Coordenada X
            if data:
                if bytes.decode(data).find("end") != -1:
                    vstat.write(bytes("end".encode()))
                    print("ACK end OK")
                    break
                else:
                    stData = bytes.decode(data)
                    
                    x_, y1_, y2_ = stData.split(", ")
                    
                    # Converte o indice do potencial da medição
                    x1 = (int(x_)*pPas)+pIni
                    
                    x = np.concatenate((x,np.array(x1)), axis = None)
                    y1 = np.concatenate((y1,np.array(int(y1_) * fe)),axis = None)
                    y2 = np.concatenate((y2,np.array(int(y2_) * fe)),axis = None)
                    y = np.concatenate((y,np.array((int(y1_) - int(y2_)) * fe)),axis = None)
                    
                    
            
            #---- Live Plot ----#
            curve.curveX = x
            curve.curveY = y
            subPlot.plot(curve.curveX, curve.curveY, color=curve.color)
            canvas.draw()        
        
        #Será retornado um array com três curvas (X, Y1-Y2), (X, Y1) e (X, Y2)
        curves = np.ndarray([])
        
        #curve = md.curve(, x, y)

        curveY1 = md.curve("Untitle-"+str(receivedCurveName)+"_Y1", x, y1)

        curveY2 = md.curve("Untitle-"+str(receivedCurveName)+"_Y2", x, y2)
        
        curves = np.append(curves, curve, axis=None)
        curves = np.append(curves, curveY1, axis=None)
        curves = np.append(curves, curveY2, axis=None)
        
        return curves

class operations:
    '''
    Filter Savitzky Golay
        y --> Array de valores para se aplicar o filtro
        wl --> window_length, tamanho da janela de valores para suavização
        po --> polyorder, ordem do polinomio aplicado
    '''
    def ft_savgol(y, wl, po):
        # Retorna um array com os valores de Y
        
        print(wl)
        print(po)
        return savgol_filter(y, window_length = int(wl), polyorder = int(po))
    
    '''
    ALPS Baseline correction
        y --> Array de valores para se calcular o baseline
        lam --> Lambda que se refere a suavização e costuma ter valores entre 10^2 e 10^9
        p --> Assimetria e costuma ter valores entre 0.1 e 0.001
    '''
    def bl_alps(y, lam, p, niter=10):
        lam = int(lam)
        p = float(p)
        L = len(y)
        D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
        w = np.ones(L)
        for i in range(niter):
            W = sparse.spdiags(w, 0, L, L)
            Z = W + lam * D.dot(D.transpose())
            z = spsolve(Z, w*y)
            w = p * (y > z) + (1-p) * (y < z)
        # z é o baseline
        return np.subtract(y,z)
    
    '''
    FINDPEAKS
        y --> para se procurar os picos, com height igual a 1,
        encontra-se apenas um pico, o global.
    '''
    def findPeak(y):
        N = y.size
        max = y[0]
        i_max = 0
        for i in range (1,N):
            if y[i] > max:
                max = y[i]
                i_max = i
        # Retorna o indice do pico encontrado
        return i_max

    
    