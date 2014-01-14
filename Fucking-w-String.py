'''
Created on Dec 30, 2013

@author: Dell
'''

message = raw_input("Enter a word: ")

print "The length of the message is %s" % len(message)
print "The most common letter in the English Language, '%s'," % 'e',
if 'e' in message:
    print "is in your message."
else:
    print "is not in your message"