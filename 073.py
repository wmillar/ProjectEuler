'''
Consider the fraction, n/d, where n and d are positive integers. If nd and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d  8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
proper fractions for d <= 12,000?

Note: The upper limit has been changed recently.
'''

#GorL=0 => returns fraction just greater, 1 returns just less
def getFraction(denominator,limit,GorL=0):
    tempNumerator = limit*denominator
    tempNumeratorInt = int(tempNumerator)
    if GorL == 1:
        if tempNumerator == tempNumeratorInt:
            return tempNumeratorInt-1
        return tempNumeratorInt
    else:
        if tempNumerator == tempNumeratorInt:
            return tempNumeratorInt
        return tempNumeratorInt+1

minLimit = 1.0/3
maxLimit = 1.0/2
decimalsDict = {}

totalDecimals = 0

for denominator in xrange(5,12001):
    denominatorLow = getFraction(denominator,minLimit,0)
    denominatorHigh = getFraction(denominator,maxLimit,1)
    denominator = float(denominator)
    for numerator in xrange(denominatorLow,denominatorHigh+1):
        tempDecimal = numerator/denominator
        if tempDecimal > minLimit and tempDecimal < maxLimit:
            if not decimalsDict.has_key(tempDecimal):
                decimalsDict[tempDecimal] = True
                totalDecimals += 1
print totalDecimals
