"""
Name: Aayog Koirala
Date: Jan 14, 2020
Desc: Box Maker: makes box of witdh w and height h using character c
"""

from math import floor

width = floor(float(input("Enter the width:")))
height = floor(float(input("Enter the height:")))
character = input("Enter the character to print:")

# We don't need for-loops to repeat the same thing in python
print(f"{character*width}\n"*height, end="")
