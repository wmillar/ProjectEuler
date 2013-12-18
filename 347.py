'''
The largest integer <= 100 that is only divisible by both the primes 2 and 3 is
96, as 96=32*3=25*3. For two distinct primes p and q let M(p,q,N) be the largest
positive integer <= N only divisible by both p and q and M(p,q,N)=0 if such a
positive integer does not exist.

E.g. M(2,3,100)=96.
M(3,5,100)=75 and not 90 because 90 is divisible by 2 ,3 and 5.
Also M(2,73,100)=0 because there does not exist a positive integer <= 100 that
is divisible by both 2 and 73.

Let S(N) be the sum of all distinct M(p,q,N). S(100)=2262.

Find S(10 000 000).
'''

def getPrimes(limit):
    sieve = [True] * limit
    for n in xrange(3, int(limit**.5) + 1, 2):
        if sieve[n]:
            sieve[n*n::n*2] = [False] * ((limit-n*n-1)/(n*2) + 1)
    return [2] + [n for n in xrange(3, limit, 2) if sieve[n]]


def findLargest(p, q, n):
    N = 0   # largest found
    start = p * q
    current = start
    while True:
        while current <= n:
            current *= q
        else:
            if current / q > N:
                N = current / q
        start *= p
        if start > n:
            return N
        else:
            current = start


def pqGenerator(n):
    primes = getPrimes(n / 2)
    indexLimit = len(primes)
    for i in xrange(indexLimit):
        j = i + 1
        while j < indexLimit and primes[i] * primes[j] <= n:
            yield primes[i], primes[j]
            j += 1


def S(n):
    pqGen = pqGenerator(n)
    total = 0
    for p, q in pqGen:
        total += findLargest(p, q, n)
    return total


print S(10**7)
