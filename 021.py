'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from collections import deque


def getDivisors(n):
    lowerDivisors = [1]
    upperDivisors = deque()
    sqrt = int(n**.5)
    for div in xrange(2, sqrt + 1):
        if n % div == 0:
            lowerDivisors.append(div)
            upperDivisors.appendleft(n / div)
    if sqrt**2 == n and upperDivisors:
        upperDivisors.popleft()
    return lowerDivisors + list(upperDivisors)


def getAmicableUnder(limit):
    amicable = []
    divisors = {n:sum(getDivisors(n)) for n in xrange(2, limit)}
    for k, v in divisors.iteritems():
        if v != 1 and v < limit and divisors[v] == k and k < v:
            amicable += [k, v]
    return amicable


print sum(getAmicableUnder(10**4))
