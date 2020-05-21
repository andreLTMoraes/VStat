# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:06:50 2019

@author: André Moraes
"""

font9 = "-family {Segoe UI} -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

def btnStyle(btn):
    btn.configure(activebackground="#ececec")
    btn.configure(activeforeground="#000000")
    btn.configure(background="#00cccc")
    btn.configure(disabledforeground="#a3a3a3")
    btn.configure(font=font9)
    btn.configure(foreground="#ffffff")
    btn.configure(highlightbackground="#d9d9d9")
    btn.configure(highlightcolor="black")
    btn.configure(pady="0")
    
def frStyle(fr):
    fr.configure(relief='groove')
    fr.configure(borderwidth="2")
    fr.configure(relief='groove')
    fr.configure(background="#f9f9f9")
    fr.configure(highlightbackground="#d9d9d9")
    fr.configure(highlightcolor="black")
    
def mnStyle(mn):
    mn.configure(activebackground="#ececec")
    mn.configure(activeforeground="#000000")
    mn.configure(background="#d9d9d9")
    mn.configure(font="TkMenuFont")
    mn.configure(foreground="#000000")
                 
def etStyle(et):
    et.configure(background="white")
    et.configure(disabledforeground="#a3a3a3")
    et.configure(font="TkFixedFont")
    et.configure(foreground="#000000")
    et.configure(highlightbackground="#d9d9d9")
    et.configure(highlightcolor="black")
    et.configure(insertbackground="black")
    et.configure(selectbackground="#c4c4c4")
    et.configure(selectforeground="black")
    
def lbStyle(lb):
    lb.configure(activebackground="#f9f9f9")
    lb.configure(activeforeground="black")
    lb.configure(background="#f9f9f9")
    lb.configure(disabledforeground="#a3a3a3")
    lb.configure(foreground="#000000")
    lb.configure(highlightbackground="#d9d9d9")
    lb.configure(highlightcolor="black")
    lb.configure(justify='left')
