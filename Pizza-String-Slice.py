'''
Created on Jan 9, 2014

@author: zar
'''
word = "pizza"

print("""
Slicing Pizza 'Cheat Sheet'
   0   1   2   3   4   5
 +---+---+---+---+---+
 | p | i | z | z | a |
 +---+---+---+---+---+
  -5  -4  -3  -2  -1
""")
print("Enter the begining and ending indexes for your slice of 'pizza'")
print("Press the enter key at begining to exit")

begin = None
while begin != "":
    begin = (input("Begin: "))
    if begin:
        begin = int(begin)
        end = int(input("End: "))
        print("Begin: %s \nEnd: %s" % (begin, end))
        print(word[begin:end])