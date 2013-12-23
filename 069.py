# -*- coding: utf-8 -*-
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

    n   Relatively Prime  φ(n)  n/φ(n)
    2   1                 1     2
    3   1,2               2     1.5
    4   1,3               2     2
    5   1,2,3,4           4     1.25
    6   1,5               2     3
    7   1,2,3,4,5,6       6     1.1666...
    8   1,3,5,7           4     2
    9   1,2,4,5,7,8       6     1.5
    10  1,3,7,9           4     2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
def genPrimes(limit):
    primeDict = {}
    for i in xrange(2, limit+1):
        primeDict[i] = True
    sieveNum = 1
    while True:
        currentNum = sieveNum + 1
        i = currentNum
        if currentNum == limit:
            return primeDict
        while True:
            if i == limit:
                return primeDict
            if primeDict[i] == True:
                sieveNum = i
                break
            else:
                i += 1
        i = 2
        while True:
            sieveProduct = sieveNum * i
            if sieveProduct <= limit:
                primeDict[sieveProduct] = False
                i += 1
            else:
                break
    return primeDict

#outputs list of primes up to(including) limit
def genPrimesList(limit):
    primeList = []
    i = 2
    for j in genPrimes(limit).values():
        if j == True:
            primeList.append(i)
        i += 1
    return primeList


primeList = genPrimesList(50)

product = 1
for prime in primeList:
    tempResult = product * prime
    if tempResult < 1000000:
        product = tempResult
print product
