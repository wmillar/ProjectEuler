'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import itertools


def getPrimes(limit):
    primes, sieve = ['2'], [True] * limit
    sq_limit = int(limit**.5) + 1
    if sq_limit % 2 == 0:
        sq_limit += 1
    for n in xrange(3, sq_limit, 2):
        if sieve[n]:
            primes.append(str(n))
            for m in xrange(n * n, limit, n * 2):
                sieve[m] = False
    return (primes + [str(n) for n in xrange(sq_limit, limit, 2) if sieve[n]],
            sieve)


def truncLeft(nStr):
    current = nStr[1:]
    while current:
        yield current
        current = current[1:]


def truncRight(nStr):
    current = nStr[:-1]
    while current:
        yield current
        current = current[:-1]


def truncGenerator(nStr):
    return itertools.chain(truncLeft(nStr), truncRight(nStr))


def filterEnds(nStr):
    return not (nStr[0] in '468019' or nStr[-1] in '24680159')


def onlyOdds(nStr):
    return all(iter(int(n) % 2 == 1 for n in nStr))


def check(nStr):
    if not (filterEnds(nStr) and onlyOdds(nStr[1:])):
        return False
    if not all(sieve[int(truncated)] for truncated in truncGenerator(nStr)):
        return False
    return True


primes, sieve = getPrimes(10**6)
primes = primes[4:]     # remove 2, 3, 5, 7


print sum(int(prime) for prime in primes if check(prime))
