"""
Name: Aayog Koirala
Date: Jan 15, 2020
Desc: Guessing Game: guess numbers from 1 to 100
"""

from random import randint

toGuess = randint(0, 101)

# Message exactly same from the example output
message = """We have randomly selected a number from 0
to 100 inclusive.  Make a guess and we will 
tell you if it is too high or too low.  Keep
guessing until you guess the correct number.
"""

print(message)
count = 0
while True:
    count += 1
    num = input("What is you guess?")   
    try:
        num = int(num)
    except:
        continue
    if toGuess < num:
        print("Too high!")
    elif toGuess > num:
        print("Too low!")
    else:
        print(f"Correct! It took you {count} guesses.")
        break
