#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Feb 20, 2019 02:41:59 PM -0300  platform: Windows NT
"""
Created on Mon Feb 18 10:08:04 2019

@author: André Moraes
"""
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import VStat_support
import Controller as ctrl
import Estilos as es

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    VStat_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    VStat_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    ctrl.connection.disconnect()
    ctrl.connection.closePort()
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
#        font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
#            "-underline 0 -overstrike 0"
            
        self.fr_miniaturas = tk.Frame(top)
        self.fr_mainView = tk.Frame(top)
        self.fr_values = tk.Frame(top)
        
        def resize(e):
            self.fr_miniaturas.place(relx=272/top.winfo_width())
            self.fr_mainView.place(relx = 272/top.winfo_width(), width=top.winfo_width()-476)
            self.fr_values.place(x=top.winfo_width()-200)
            
        root.iconbitmap('VStat.ico')
        
        top.geometry("1223x666+16+1")
        top.title("VStat")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind("<Configure>", lambda e: resize(e))
        top.update()
        #top.minsize()
        
        self.fr_FastOptions = tk.Frame(top)
        self.fr_FastOptions.place(relx=0.0, rely=0.0, relheight=1.0
                , width=268)
        es.frStyle(self.fr_FastOptions)
        self.fr_FastOptions.configure(width=205)

        self.btn_import = tk.Button(self.fr_FastOptions)
        self.btn_import.place(relx=0.049, rely=0.028, height=24, relwidth=0.88)
        es.btnStyle(self.btn_import)
        self.btn_import.configure(text='''Importar CSV''')
        self.btn_import.bind('<ButtonRelease-1>',lambda e:VStat_support.btn_import(e))

        self.btn_export = tk.Button(self.fr_FastOptions)
        self.btn_export.place(relx=0.049, rely=0.084, height=24, relwidth=0.88)
        es.btnStyle(self.btn_export)
        self.btn_export.configure(text='''Exportar CSV''')
        self.btn_export.bind('<ButtonRelease-1>', lambda e:VStat_support.btn_export(e))
        
        self.btn_connect = tk.Button(self.fr_FastOptions)
        self.btn_connect.place(relx=0.049, rely=0.14, height=24, relwidth=0.88)
        es.btnStyle(self.btn_connect)
        self.btn_connect.configure(background="#738c8c")
        self.btn_connect.configure(text='''Conectar''')
        self.btn_connect.bind('<ButtonRelease-1>',lambda e:VStat_support.btn_connect(e))
        
        self.fr_analise = tk.LabelFrame(self.fr_FastOptions)
        self.fr_analise.place(relx=0.049, rely=0.196, height=360
                , relwidth=0.88)
        self.fr_analise.configure(relief='groove')
        self.fr_analise.configure(foreground="black")
        self.fr_analise.configure(background="#f9f9f9")
        self.fr_analise.configure(width=190)
        
        self.fr_miniaturas.place(relx=272/top.winfo_width(), rely=0.766, relheight=0.308
                , relwidth=1.0)
        es.frStyle(self.fr_miniaturas)
        self.fr_miniaturas.configure(width=1015)

        self.fr_mainView.place(relx = 272/top.winfo_width(), rely=0.0, relheight=0.758
                , width=top.winfo_width()-476)
        es.frStyle(self.fr_mainView)
        self.fr_mainView.configure(width=845)

        self.fr_values.place(x=top.winfo_width()-200, rely=0.0, relheight=0.758
                , width=200)
        es.frStyle(self.fr_values)
        self.fr_values.configure(width=165)
        
        self.fr_info = tk.LabelFrame(self.fr_values)
        self.fr_info.place(relx=0.061, rely=0.02, relheight=0.96, relwidth=0.909)

        self.fr_info.configure(relief='groove')
        self.fr_info.configure(foreground="black")
        self.fr_info.configure(text='''Informações''')
        self.fr_info.configure(background="#f9f9f9")
        self.fr_info.configure(highlightbackground="#d9d9d9")
        self.fr_info.configure(highlightcolor="black")
        self.fr_info.configure(width=150)
        
        self.lb_ConnInfo = tk.Label(self.fr_info)
        self.lb_ConnInfo.place(relx=0.067, rely=0.7, height=441, width=131
                , bordermode='ignore')
        self.lb_ConnInfo.configure(activebackground="#f9f9f9")
        self.lb_ConnInfo.configure(activeforeground="black")
        self.lb_ConnInfo.configure(background="#f9f9f9")
        self.lb_ConnInfo.configure(disabledforeground="#a3a3a3")
        self.lb_ConnInfo.configure(foreground="#000000")
        self.lb_ConnInfo.configure(highlightbackground="#d9d9d9")
        self.lb_ConnInfo.configure(highlightcolor="black")
        self.lb_ConnInfo.configure(width=131)
        self.lb_ConnInfo.pack()

        #---- BARRA DE MENU ----#
        
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        es.mnStyle(self.sub_menu)
        self.menubar.add_cascade(menu=self.sub_menu,                
                label="Arquivo")
        
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Importar CSV",
                command=lambda:VStat_support.btn_import(self.sub_menu._name))
        
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Exportar CSV",
                command=lambda:VStat_support.btn_export(self.sub_menu._name))
        #self.sub_menu.bind()
        
        self.menuVoltammetry = tk.Menu(top, tearoff=0)
        es.mnStyle(self.menuVoltammetry)
        
        self.menubar.add_cascade(menu=self.menuVoltammetry,
                label="Voltametria")
        
        self.menuVoltammetry.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Pulso Diferencial (DPV)",
                command= VStat_support.painelDPV)
        
        self.curveMenu = tk.Menu(top,tearoff=0)
        es.mnStyle(self.curveMenu)
        
        self.menubar.add_cascade(menu=self.curveMenu,
                label="Curvas")
        
        self.curveMenu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Unir",
                command= VStat_support.curvesJoin)
        self.curveMenu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Excluir",
                command= VStat_support.removeCurve)
        
        self.sMenuBaseline = tk.Menu(top, tearoff=0)
        self.curveMenu.add_cascade(menu=self.sMenuBaseline,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Baseline")
        
        self.sMenuBaseline.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="ALSS",
                command= lambda:VStat_support.op_frame2param("Baseline ALSS",
                                                               "Suavização",
                                                               "3000",
                                                               "Assimetria",
                                                               "0.0001",
                                                               ctrl.operations.bl_alps))
        
        self.sMenuSuavizacao = tk.Menu(top, tearoff=0)
        self.curveMenu.add_cascade(menu=self.sMenuSuavizacao,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Suavização")
        
        self.sMenuSuavizacao.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Savitzky Golay",
                command= lambda:VStat_support.op_frame2param("Filtro Savitzky Golay",
                                                               "Janela",
                                                               "11",
                                                               "Ordem pol.",
                                                               "2",
                                                               ctrl.operations.ft_savgol))
        
        self.curveMenu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Encontrar pico",
                command= VStat_support.fd_PEAK)
        
    
        
if __name__ == '__main__':
    vp_start_gui()




