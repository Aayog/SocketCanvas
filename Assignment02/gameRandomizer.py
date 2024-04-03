#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Aayog Koirala
Desc: Project 1 - CSCI-420: Game Randomizer
Date: Feb 3, 2020
Bias: Picks user based on two randomly highest repeating characters in their name
    i.e. Java has a repeating character with count of 2 which so has a bias of 
         two, compared to python which has no repeating character
"""

from tkinter import *
from tkinter import messagebox
from collections import Counter
from random import choice, randint

master = Tk()
master.geometry("400x300")

# master.resizable(0,0)
Label(master, text="Picking a random user game", font="none 16 bold").grid(row=0, column=0, columnspan=2)
master.title("Pick User")

Label(master, text="Enter a list of names.").grid(row=1, column=0)

inputUserList = Text(master, height=10, width=30)
inputUserList.grid(row=2, column=0)

prevChoice = ""

def addBias(nameList):
    returnList = []
    for name in nameList:
        name = name.strip()
        if name == "":
            continue
        temp = Counter(name.lower())
        # randomly based on highest or second highest, so it's not readily apparent
        if temp.most_common()[0][1] == 1:
            returnList += [name] #dealing with the bias if no repeating characters
        elif len(temp.most_common()) == 1:
            returnList += [name]
        else:
            returnList += [name] * temp.most_common()[randint(0,1)][1]
    # to debug if probability is actuallly bias
    # print(Counter([choice(returnList) for i in range(100)]))
    
    return returnList

outputLabel = Label(master, text="", font="none 14 bold", fg="blue")
outputLabel.grid(row=3, column=0)
def inputError():
    messagebox.showerror(title="Invalid Input", message="Enter at least two name to pick a player")
    
    
def getInputList(event=None):
    global outputLabel
    global prevChoice
    try:
        names = inputUserList.get("1.0", END)
        namesList = addBias(names.split("\n"))
        if len(namesList) < 2:
            raise Exception
        newChoice = choice(namesList)
        # making sure new choice is different from previous choice
        while newChoice == prevChoice:
            newChoice = choice(namesList)
        outputLabel.configure(text="Picked User : " + newChoice)
        prevChoice = newChoice
    except:
        inputError()
    
submitButton = Button(master, text="Pick Player",height=10)
submitButton.grid(row=2, column = 1)
submitButton.bind('<Button>', getInputList)


mainloop()