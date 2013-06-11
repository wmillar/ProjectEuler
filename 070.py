# -*- coding: utf-8 -*-
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
'''

def getPrimeFactors(n):
    pDict = {2:False}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pDict[i] = False
            for i2 in xrange(i*2,n,i):
                if i2 in pDict:
                    if i2 not in pDict[i2]:
                        pDict[i2].append(i)
                else:
                    pDict[i2] = [i]
    for n in xrange(4, n, 2):
        if n in pDict:
            pDict[n] = [2]+pDict[n]
        else:
            pDict[n] = [2]
    return pDict

def totient(pDict, n):
    if not pDict[n]:
        return n-1
    product = n
    for p in pDict[n]:
        product *= 1-1.0/p
    return int(product)



limit = 10000000
primeDict = getPrimeFactors(limit)
ratio = 2


for n in xrange(2, limit):
    result = totient(primeDict, n)
    if sorted(str(n)) == sorted(str(result)):
        cRatio = float(n)/result
        if cRatio < ratio:
            ratio, ratio_n = cRatio, n
print ratio_n
