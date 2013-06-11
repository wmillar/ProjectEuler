"""
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is
divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible
by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which
produces 80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""
#generates all primes up to limit(included), returns as dict type
def genPrimes(limit):
    limit2 = limit + 1
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

#input current coefficients, return next
def nextCoefficients(a=0,b=0,limit=9):
    if a == 0:
        if b == 0:
            return 0,b+1
        if b > 0:
            return 0,-b
        if b < 0:
            if b == -limit:
                return a+1,0
            return a,-b+1
    if a > 0:
        if b == 0:
            return -a,0
        if b > 0:
            return a,-b
        if b < 0:
            return -a,-b
    if a < 0:
        if b == 0:
            return -a,b+1
        if b > 0:
            return a,-b
        if b < 0:
            if b == -limit:
                if a == -limit:
                    return False
                return -a+1,0
            return -a,-b+1

def nextCoefficients2(a,b,limit=9):
    global smallPrimeList
    aIndex = smallPrimeList.index(a)
    bIndex = smallPrimeList.index(b)
    try:
        return smallPrimeList[aIndex],smallPrimeList[bIndex+1]
    except:
        try:
            return smallPrimeList[aIndex+1],smallPrimeList[0]
        except:
            return False
#generate primes up to 1 million
primeList = []
smallPrimeList = []
i = 2
for j in genPrimes(500000).values():
    if j == True:
        primeList.append(i)
        if i < 1000:
            smallPrimeList.append(i)
    i += 1
print "Primes generated"

maxPrimes = 0
primesFound = 0
c = (0,0)
while True:
    if primesFound > maxPrimes:
        coefficients = (c[0],c[1])
        maxPrimes = primesFound
        print "%s %r" % (maxPrimes,coefficients)
    primesFound = 0
    c = nextCoefficients(c[0],c[1],999)
#    print c
    n = 0
    if c != False:
        while True:
            result = n**2 + n * c[0] + c[1]
            if result > 1:
                try:
                    primeList.index(result)
                    n += 1
                    primesFound += 1
#                    print "(%s) %s is a prime (%s,%s)" % (n,result,c[0],c[1])
                except:
#                    print "(%s) %s is NOT a prime (%s,%s)" % (n,result,c[0],c[1])
                    break
            else:
                break
    else:
        break
print maxPrimes
print coefficients

