'''
We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from itertools import permutations


def isPrime(n):
    if n % 2 == 0:
        return False
    if n < 8:   # 2, 3, 5, 7 are prime
        return True
    if n % 3 == 0:
        return False
    for d in xrange(5, int(pow(n, 0.5)) + 2, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True


def genPermutations(digits):
    for perm in permutations(digits):
        yield int(''.join(perm))


def findPandPrimes(length):
    found = []
    for n in genPermutations(map(str, range(1, length + 1))):
        if isPrime(n):
            found.append(n)
    return found


def findMaxPandPrime():
    for n in xrange(9, 4, -1):
        results = findPandPrimes(n)
        if results:
            return max(results)


print findMaxPandPrime()
