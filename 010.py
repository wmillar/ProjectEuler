'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def getPrimes(n):
    pList, pDict = [2], {}
    for i in xrange(3,n,2):
        if i not in pDict:
            pList.append(i)
            for i2 in xrange(i*3,n,i*2):
                pDict[i2] = None
    return pList

print sum(getPrimes(2000000))
