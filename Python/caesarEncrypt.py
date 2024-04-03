#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:36:28 2020

@author: aayog
"""
from tkinter import *
master = Tk()
Label(master, text="Text to encrypt").grid(row=0)

e1 = Entry(master)
e1.grid(row=0, column=1)



alpha = [chr(i) for i in range(97,123)]

def caeser_encrypt(string, key=-2):
    toReturn = ""
    for char in string:
        flagUpper = 0
        if char.lower() not in alpha:
            toReturn += char
            continue
        if char.upper() == char:
            flagUpper = 1
            char = char.lower()
            
        encrypted = chr((((ord(char) - ord('a')) + key) % 26)+ord('a'))
        if flagUpper == 1:
            encrypted = encrypted.upper()
        toReturn += encrypted
    return toReturn
        
def encrypt(event=None):
    print(caeser_encrypt(e1.get()))
    Label(master, text=caeser_encrypt(e1.get())).grid(row=1)
    
button = Button(master, text="Encrypt")
button.grid(row=3, column=0)
button.bind('<Button>', encrypt)

            
# print(caeser_encrypt("Hello!!", 2))

master.mainloop()
