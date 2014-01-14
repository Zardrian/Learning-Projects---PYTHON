'''

Created on Dec 31, 2013

@author: Dell
'''

numberRows = int(raw_input("Enter how long the Christmas Tree will be: "))
numberColumns = ((numberRows * 2) - 1)
blankSpaceForTrunkLength = (numberColumns / 2)
print "There are %s rows and %s columns" % (numberRows, numberColumns)

for i in range(1, (numberRows + 1)):
    printSpotLength = ((i * 2) - 1)
    blankSpotLength = ((numberColumns - printSpotLength) / 2)
    print "%s%s" % ((" " * blankSpotLength), ("*" * printSpotLength))
print "%s*" % (" " * blankSpaceForTrunkLength)
raw_input("press enter to exit")