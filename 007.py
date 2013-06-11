'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
'''

def getPrimes(n):
    pList, pDict = [2], {2: 2}
    for i in xrange(3, n, 2):
        if i not in pDict:
            pList.append(i)
            for i2 in xrange(i*3, n, i*2):
                pDict[i2] = False
    return pList

print getPrimes(150000)[10000]
