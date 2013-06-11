'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n!/(r!(nr)!), where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are
greater than one-million?
'''

fDict = {0:1}
product = 1
for n in range(1,101):
    product *= n
    fDict[n] = product

def nCr(n,r,fDict):
    return fDict[n]/(fDict[r]*(fDict[n-r]))

numFound = 0
for n in xrange(23,101):
    for r in xrange(4,n-3):      #begin at 4 because 100 choose 3 < 10^7, end n-3 because 100 choose 97 < 10^7
        if nCr(n,r,fDict) > 1000000:
            numFound += 1
print numFound