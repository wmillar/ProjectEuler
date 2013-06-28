'''
The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number
with this property is 614656 = 28^4.

We shall define a_n to be the nth term of this sequence and insist that a
number must contain at least two digits to have a sum.

You are given that a_2 = 512 and a_10 = 614656.

Find a_30.
'''
from itertools import count


def getNumbersInbetween(base, upper, powMinimum):
    include = []
    if base in limitsDict:
        startPow = limitsDict[base]
    else:
        startPow = powMinimum
    current = pow(base, startPow - 1)
    for p in count(startPow):
        current *= base
        if current < upper:
            include.append(current)
        else:
            limitsDict[base] = p
            return include
        
    
limitsDict = {2:4}
aList = []
aFound = 0
upper = 10
powMinimum = 2.0

while aFound < 30:
    powMinimumInt = int(powMinimum)
    upper *= 10
    currentAList = []
    for b in xrange(2, int(pow(upper, 1.0 / powMinimumInt)) + 1):
        for n in getNumbersInbetween(b, upper, powMinimumInt):
            if sum(int(d) for d in str(n)) == b:
                currentAList.append(n)
                aFound += 1
    powMinimum += 0.5
    aList += sorted(currentAList)

print aList[29]
