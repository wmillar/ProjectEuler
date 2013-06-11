'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over
five thousand different ways?
'''

def getPrimes(n):
    pList, pDict = [2], {2: None}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pList.append(i)
            for i2 in xrange(i * 3, n, i * 2):
                pDict[i2] = None
    return pList


def nextPrime(pList):
    nDict = {1:2, pList[-1]:None}
    for i in xrange(len(pList) - 1):
        nDict[pList[i]] = pList[i + 1]
    return nDict


def combineWays(nWaysNum, nNew, waysDict):
    '''returns a list of sorted tuples of the ways to writes nWaysNum
       with nNew added to every tuple'''
    ways = set([])
    for w in waysDict[nWaysNum]:
        ways.add(tuple(sorted(list(w) + [nNew])))
    return ways


def getWays(num, nextDict, pSet, waysDict):
    ways = set([])
    n, p = num - 1, 1
    while n > p:
        p = nextDict[p]
        n = num - p
        if n in pSet:
            ways.add((p,n))
        ways.update(combineWays(n, p, waysDict))
    return list(ways)


def waysSum(target):
    pSet = getPrimes(target)
    nextDict = nextPrime(pSet)
    pSet = set(pSet)
    waysDict = {2:[(2,)], 3:[(3,)]}
    for n in xrange(4, 5000):
        result = getWays(n, nextDict, pSet, waysDict)
        waysDict[n] = result
        if len(result) > target:
            return n


print waysSum(5000)
