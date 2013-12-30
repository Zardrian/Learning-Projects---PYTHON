'''
Created on Dec 29, 2013

@author: Melissa
'''
import random

correctNumber = random.randrange(100) + 1
guess = int(input("Make a guess. "))

while guess != correctNumber:
    if guess > correctNumber:
        print("You guessed too high.")
        guess = int(input("Make a guess. "))
    elif guess < correctNumber:
        print("You guessed too low.")
        guess = int(input("Make a guess. "))
    else:
        print("I heard OP is a foggot")
print("Good Job!")
input("Press enter to exit")