'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''
import random


def getPrimes(n):
    # returns sorted list of primes [3, n)
    pList, pSet = [], set()
    for i in xrange(3, n, 2):
        if i not in pSet:
            pList.append(i)
            for i2 in xrange(i*3, n, i*2):
                pSet.add(i2)
    return pList


def fermatPrimeTest(n):
    if pow(random.randint(2, n - 1), n - 1, n) != 1:
        return False
    return True


def checkPrimeSet(primes, n):
    for p in primes:
        if not fermatPrimeTest(int(p + n)):
            return False
        if not fermatPrimeTest(int(n + p)):
            return False
    return True


def getSets(cSets, cLength, tLength, limit, pList, pListIndex):
    newSets = []
    while cSets:
        s = cSets.pop(0)
        sStr = [str(n) for n in s]
        cNewSets = []
        for prime in pList[pListIndex[s[-1]] + 1:]:
            if checkPrimeSet(sStr, str(prime)):
                cNewSets.append(s + [prime])
        newSets.extend(cNewSets)
    if not newSets:
        return False        # cannot find any more sets
    cLength += 1
    if cLength == tLength:
        return newSets[0]   # returns first set with desired length
    else:
        return getSets(newSets, cLength, tLength, limit, pList, pListIndex)


def findLowestSet(length, limit):
    pList = getPrimes(limit)
    pList.remove(5)
    pListIndex = dict(zip(pList, range(len(pList))))
    for n in pList:
        result = getSets([[n]], 1, length, limit, pList, pListIndex)
        if result:
            return sum(result)


print findLowestSet(5, 10000)
