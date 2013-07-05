'''
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def getPrimes(limit):
    sieve = [True] * limit
    for n in xrange(3, int(limit**.5) + 1, 2):
        if sieve[n]:
            sieve[n*n::n*2] = [False] * ((limit-n*n-1)/(n*2) + 1)
    return [2] + [n for n in xrange(3, limit, 2) if sieve[n]], sieve


def rotate(n):
    current = n
    for i in xrange(len(n)):
        current = current[-1] + current[:-1]
        yield int(current)
        

def onlyOddDigits(n):
    return all(d % 2 == 1 for d in map(int, n))


def isCircular(rotations, sieve):
    return all(sieve[circ] for circ in rotations)


def getCircularPrimes(limit):
    primes, sieve = getPrimes(limit)
    primes = map(str, primes)
    circularPrimes = set(['2'])
    for n in filter(onlyOddDigits, primes):
        rotations = set(rotate(n))
        if isCircular(rotations, sieve):
            circularPrimes = circularPrimes.union(rotations)
    return circularPrimes


print len(getCircularPrimes(10**6))
