'''
The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?
'''

def getPrimes(n):
    '''returns a sorted list of primes [2, n)'''
    pList, pDict = [2], {2: 2}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pList.append(i)
            for i2 in xrange(i * 3, n, i * 2):
                pDict[i2] = False
    return pList


def nextPrimeDict(pList):
    nPrime = {pList[-1]: None}
    i = 1
    for n in pList[:-1]:
        nPrime[n] = pList[i]
        i += 1
    return nPrime


def powerIter(iterable):
    iterSum = 0
    p = 2
    for n in iterable:
        iterSum += pow(n, p)
        p += 1
    return iterSum


def newSet(pSet, limit):
    # try to increase number in positions, resetting prev positions
    if powerIter([nDict[pSet[0]]] + pSet[1:]) < limit:
        return [nDict[pSet[0]]]+ pSet[1:]
    elif powerIter([2] + [nDict[pSet[1]]] + [pSet[2]]) < limit:
        return [2] + [nDict[pSet[1]]] + [pSet[2]]
    elif powerIter([2, 2] + [nDict[pSet[2]]]) < limit:
        return [2, 2] + [nDict[pSet[2]]]
    else:
        return None


limit = 50000000
numSet = set()
pSet = [2, 2, 2]
nDict = nextPrimeDict(getPrimes(int(limit**.5) + 50))

while pSet:
    numSet.add(powerIter(pSet))
    pSet = newSet(pSet, 50000000)

print len(numSet)
