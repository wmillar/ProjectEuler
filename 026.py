"""
A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
def pattern(tempStr):
    if type(tempStr) != type(str()):    #makes sure its a string
        tempStr = str(tempStr)
    tempStr = tempStr[2:]   #shortens str to exclude 0.

    numMaxCount = tempStr.count(tempStr[0])     #counts how many of first char
    prevIndex = 0                               #default value
    numOfRuns = 0
    patternFound = False
    
    while patternFound == False:
        numOfRuns += 1
        if numOfRuns > numMaxCount:
            print "Pattern could not be found"
            return False
        numIndex = tempStr.index(tempStr[0], prevIndex + 1)
        numLimitIndex = numIndex - 1
        i = 0

        while tempStr[0+i] == tempStr[numIndex+i]:
#            print "%s == %s" % (tempStr[0+i],tempStr[numIndex+i])
            
            # checks if at index limit, if True: pattern found
            if i == numLimitIndex and i > 1:
#                print "Pattern found...",
#                print "(%s)" % i,
#                print "Pattern length: %s" % (int(numLimitIndex + 1))
                return int(numLimitIndex + 1)

            i += 1
            prevIndex = numIndex

#        print "%s != %s" % (tempStr[0+i],tempStr[numIndex+i])

from decimal import *
getcontext().prec = 2000
maxPattern = 0

i = 7
while i < 1000:
    while i % 11 == 0 or i % 2 == 0 or i % 5 == 0 or i % 3 == 0:
        i += 1
    num = str(Decimal(1)/Decimal(i))
    numPattern = pattern(num)
    if numPattern > maxPattern:
        maxPatternNumber = i
        maxPattern = numPattern
    i += 1
print maxPatternNumber
