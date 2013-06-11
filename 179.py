'''
Find the number of integers 1 < n < 10^7, for which n and n + 1 have the same
number of positive divisors. For example, 14 has the positive divisors
1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''

def getDivisors(limit):
    fDict = dict((n, 1) for n in range(4, limit, 2))
    for n in xrange(3, limit):
        for mult in xrange(n * 2, limit, n):
            if mult in fDict:
                fDict[mult] += 1
            else:
                fDict[mult] = 1
    return fDict


def consecDivisors(limit):
    fDict = getDivisors(limit)
    numOfConsec = 0
    prevDivisors = 0
    for n in xrange(3, limit):
        if n in fDict:
            divisors = fDict[n]
        else:
            divisors = 0
        if prevDivisors == divisors:
            numOfConsec += 1
        prevDivisors = divisors
    return numOfConsec
        

limit = 10**7
print consecDivisors(limit + 1)
