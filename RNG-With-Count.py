'''
Created on Dec 29, 2013

@author: Melissa
'''
import random

attempts = int(input("How many attempts would you like? "))
correctNumber = random.randrange(100) + 1
guess = 0

while guess != correctNumber and attempts > 0:
    guess = int(input("Make a guess. "))
    attempts -= 1
    if guess > correctNumber:
        print("You guessed too high.")
    elif guess < correctNumber:
        print("You guessed too low.")
    else:
        print("I heard OP is a foggot")
        
if guess == correctNumber:
    print("Good Job!")
elif attempts < 0:
    print("You couldn't guess it in time.")
else:
    print("This chain may not be working")
input("Press enter to exit")