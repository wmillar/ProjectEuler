'''
A composite is a number containing at least two prime factors. For example,
15 = 3 x 5; 9 = 3 x 3; 12 = 2 x 2 x 3.

There are ten composites below thirty containing precisely two, not
necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 10^8, have precisely two, not necessarily
distinct, prime factors?
'''

def createLimits(limit):
    sieveRootLimit = int(limit**.5) + 1
    if sieveRootLimit % 2 == 1:     # make sure it's even
        sieveRootLimit += 1
    return sieveRootLimit, limit / 2 + 1


def getComposites(limit):
    pList, pSet = [None, 2], set([])
    pLimitIndex = 1
    numOfComposites = 1     # include 2*2
    sieveRootLimit, sieveMaxLimit = createLimits(limit)
    for n in xrange(3, sieveRootLimit, 2):
        if n not in pSet:
            pList.append(n)
            pLimitIndex += 1
            numOfComposites += pLimitIndex
            for mult in xrange(n * 3, sieveMaxLimit, n * 2):
                pSet.add(mult)
    for n in xrange(sieveRootLimit + 1, sieveMaxLimit, 2):
        if n in pSet:
            continue
        if n * pList[pLimitIndex] < limit:
            numOfComposites += pLimitIndex
        else:
            pLimitIndex -= 1
            if pLimitIndex == 0:
                return numOfComposites
            while n * pList[pLimitIndex] >= limit:
                    pLimitIndex -= 1
            numOfComposites += pLimitIndex
        for mult in xrange(n * 3, sieveMaxLimit, n * 2):
            pSet.add(mult)
    return numOfComposites


print getComposites(10**8)
