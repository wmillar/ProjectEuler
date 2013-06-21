'''
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''
import collections
import itertools
from operator import mul


def getPF(limit):
    sieve = [False] * limit
    for n in xrange(4, limit, 2):
        original_n = n
        sieve[n] = [2]
        n /= 2
        while n % 2 == 0:
            sieve[original_n].append(2)
            n /= 2
    for n in xrange(3, limit / 2 + 1, 2):
        if not sieve[n]:
            for m in xrange(n * 2, limit, n):
                original_m = m
                if not sieve[m]:
                    sieve[m] = [n]
                    m /= n
                else:
                    sieve[m].append(n)
                    m /= n
                while m % n == 0:
                    sieve[original_m].append(n)
                    m /= n
    return sieve


def minDiv(limit):
    factorization = getPF(limit + 1)[2:]
    primes = itertools.imap(lambda i, f: f if f else [i],
                            xrange(2, limit + 1), factorization)
    powers = collections.defaultdict(int)
    for factors in primes:
        for n, p in collections.Counter(factors).iteritems():
            if p > powers[n]:
                powers[n] = p
    return reduce(mul, itertools.starmap(pow, powers.iteritems()))


print minDiv(20)
