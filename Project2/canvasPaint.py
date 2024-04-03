#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:43:41 2020

@author: aayog
"""

from tkinter import *

master = Tk()
    second = Tk()
    master.geometry('800x600')
second.geometry('600x600')
w, h = 600, 600

myCanvas = Canvas(master, width=w, height=h)
myCanvas.place(x=0, y=0)
myCanvas.configure(bg="white")

prevX, prevY = -99, -99 
points = []
myCanvas2 = Canvas(second, width=w, height=h)
myCanvas2.pack(expand=YES)
myCanvas2.configure(bg="white")

penColor = 'black'

def changeColor(event=None):
    global penColor
    penColor = event.widget.color

a, b = 0, 0
for i in ["black", "white", "red", "blue", "green", "yellow", "purple", "brown"]:
    button = Button(master, width=5, height=5, bg=i)
    button.place(x=w+a, y=0+b)
    button.bind('<Button>', changeColor)
    button.color = i
    a+=50
    if(a >= 100):
        a %= 50
        b+=100
def clearAll(event=None):
    global myCanvas, myCanvas2, points
    points = []
    myCanvas.delete("all")
    myCanvas2.delete("all")
clearButton = Button(master, text="CLEAR", width=5,height=5)
clearButton.place(x=w+a, y=b)
clearButton.bind('<Button>', clearAll)

def trigger():
    global prevX2, prevY2, points, penColor
    prevX2 = points[0][0]
    prevY2 = points[0][1]
    for x2, y2, col in points:
        myCanvas2.create_line(prevX2, prevY2, x2, y2, fill=col)
        prevX2, prevY2 = x2, y2
        
def paint(event):
    global prevX, prevY, points
    x, y = event.x, event.y
    if (prevX == -99):
        prevX, prevY = x, y
    myCanvas.create_line(prevX, prevY, x, y, fill=penColor)
    points.append((x, y, penColor))
    prevX, prevY = x, y
    trigger()

def trigger2():
    global prevX2, prevY2, points 
    prevX2 = points[0][0]
    prevY2 = points[0][1]
    for x2, y2 in points:
        myCanvas.create_line(prevX2, prevY2, x2, y2, fill=penColor)
        prevX2, prevY2 = x2, y2


def paint2(event):
    global prevX, prevY, points
    x, y = event.x, event.y
    if (prevX == -99):
        prevX, prevY = x, y
    myCanvas2.create_line(prevX, prevY, x, y, fill="black")
    points.append((x, y))
    prevX, prevY = x, y
    trigger2()
    
myCanvas.bind('<B1-Motion>', paint)
myCanvas2.bind('<B1-Motion>', paint2)



master.mainloop()
second.mainloop()