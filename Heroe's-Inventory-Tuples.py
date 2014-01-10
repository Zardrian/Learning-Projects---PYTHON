'''
Created on Jan 9, 2014

@author: zar
'''

inventory = ()

if not inventory:
    print("You are empty-handed")
    
input("You have found a treasure chest. Press enter to open it")

inventory = ("sword","armor", "shield", "healing potion")

print("You have found some useful items")
print("Your items: ")
for item in inventory:
    print(item)

input("Press enter to exit")