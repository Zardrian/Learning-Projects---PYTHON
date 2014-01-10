'''
Created on Jan 9, 2014
'''

import random

WORDS = ("easy", "hard", "python", "jumble", "difficult", "anwser", "xylophone")

word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("""
WELCOME TO WORD JUMBLE!
Unscramble the letters to make a word
(press [enter] at the prompt to quit)
""")
print("The jumble is: %s" % (jumble))

guess = input("Your guess: ")
guess = guess.lower()
while (guess != correct) and (guess != ""):
    print("Sorry that's not it.")
    guess = input("Your guess: ")
    guess = guess.lower()
    
if guess == correct:
    print("Congradulations! You guessed it!")
    
print("Thanks for playing")
input("Press [enter] to exit")