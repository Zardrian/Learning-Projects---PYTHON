'''
Created on Dec 29, 2013

@author: Melissa
'''
import random
if __name__ == '__main__':
    die1 = random.randrange(6) + 1
    die2 = random.randrange(6) + 1
    total = die1 + die2
    print("You rolled a %s and a %s for a total of %s" %  (die1, die2, total))
    input("Press enter to exit")
    pass