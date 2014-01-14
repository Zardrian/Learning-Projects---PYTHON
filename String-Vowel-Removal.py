'''
Created on Jan 1, 2014

@author: Dell
'''

message = raw_input("Enter a message, and i'll remove the vowels: ")
newMessage = ""
VOWELS = "aeiou"

for letter in message:
    if letter.lower() not in VOWELS:
        newMessage += letter
print "Your new message is %s" % newMessage