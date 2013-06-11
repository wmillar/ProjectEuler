'''
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

def getPrimeFactors(limit):
    fDict = {2: False}
    for n in xrange(4, limit, 2):
        origN = n
        fDict[n] = []
        while n % 2 == 0:
            fDict[origN].append(2)
            n /= 2
    for n in xrange(3, limit, 2):
        if n not in fDict:
            fDict[n] = False
            for n2 in xrange(n * 2, limit, n):
                if n2 not in fDict:
                    fDict[n2] = []
                origN2 = n2
                while n2 % n == 0:
                    fDict[origN2].append(n)
                    n2 /= n
    return fDict


def findMaxPowers(fDict):
    maxDict = {}
    for n, factors in fDict.items():
        if not factors:
            maxDict[n] = 1
            continue
        powers = [(d, factors.count(d)) for d in set(factors)]
        for n, p in powers:
            if p > maxDict[n]:
                maxDict[n] = p
    return maxDict


def multMaxPowers(maxDict):
    result = 1
    for n, p in maxDict.items():
        result *= pow(n, p)
    return result


print multMaxPowers(findMaxPowers(getPrimeFactors(20)))
