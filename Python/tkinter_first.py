#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:49:51 2020

@author: aayog
"""

from tkinter import *
import random

master = Tk()

label = Label(master, text="Calculator")
label.grid(column = 1, row = 0)

textLabelVar = StringVar()
textLabel = Label(master, text=textLabelVar)
textLabel.grid(column = 0, row=1)
count = 1
computation = ""
def calculate(event=None):
    global computation
    if event.widget.mynumber is "=":
        textLabelVar = str(eval(computation))
        computation = ""
        return 
    computation += str(event.widget.mynumber)
    textLabelVar = computation

def changeColor():
    colors = ["red", "green", "blue"]
    random.shuffle(colors)
    master.configure(background=colors[0])
    master.after(100, changeColor)
    
for i in range(3):
    for j in range(3):
        button = Button(master, text=count)
        button.mynumber = count
        count += 1
        button.grid(column=i, row=j + 2)
        button.bind('<Button>', calculate)

equal = Button(master, text ="=")
equal.grid(column = 3, row = 5)
equal.bind('<Button>', calculate)
equal.mynumber = "=" 

plus = Button(master, text ="+")
plus.grid(column = 4, row = 2)
plus.bind('<Button>', calculate)
plus.mynumber = "+"

minus = Button(master, text ="-")
minus.grid(column = 4, row = 3)
minus.bind('<Button>', calculate)
minus.mynumber = "-"


divide = Button(master, text ="/")
divide.grid(column = 4, row = 4)
divide.bind('<Button>', calculate)
divide.mynumber = "/"

multiply = Button(master, text ="*")
multiply.grid(column = 4, row = 5)
multiply.bind('<Button>', calculate)
multiply.mynumber = "*"
master.after(100, changeColor)
mainloop()