'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
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



primeList = genPrimesList(1000)
'''
for num in xrange(10,50):
    tempNum = num
    mult = []
    i = 2
    while True:
        while tempNum%i==0 and tempNum != 1:
            mult.append(i)
            tempNum /= i
        i += 1
        if tempNum == 1:
            break
    print num,mult
'''
consecList = []
for num in xrange(10,200000):
    distinctDiv = 0
    divisors = []
    if num not in primeList:
        tempNum = num
        numLimit = num/2+1
        for prime in primeList:
            if prime > numLimit:
                break
            while tempNum % prime == 0:
                tempNum /= prime
                if prime not in divisors:
                    divisors.append(prime)
                    distinctDiv += 1
            if tempNum == 1:
                break
    if tempNum == 1 and distinctDiv == 4:
        consecList.append(num)
        consecPrimeCount += 1
        if consecPrimeCount == 4:
            print consecList[0]
            break
    else:
        consecList = []
        consecPrimeCount = 0
