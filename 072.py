'''
Consider the fraction, n/d, where n and d are positive integers. If n < d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d <= 1,000,000?
'''

def getPrimeFactors2(n):
    pDict = {2: False}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pDict[i] = False
            for i2 in xrange(i*2, n, i):
                if i2 in pDict:
                    if i2 not in pDict[i2]:
                        pDict[i2].append(i)
                else:
                    pDict[i2] = [i]
    for n in xrange(4, n, 2):
        if n in pDict:
            pDict[n] = [2] + pDict[n]
        else:
            pDict[n] = [2]
    return pDict


def totient(n):
    if n == 1:
        return 1
    if not pDict[n]:
        return n - 1
    product = n
    for p in pDict[n]:
        product *= 1 - 1.0/p
    return int(product)


def farey(n):
    fDict = {1: 2}
    for i in xrange(2, n + 1):
        fDict[i] = fDict[i - 1] + totient(i)
    return fDict[n]


pDict = getPrimeFactors2(1000001)
print farey(1000000) - 2
