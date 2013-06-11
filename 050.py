'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
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
def genPrimesList(limit):
    primeList = []
    i = 2
    for j in genPrimes(limit).values():
        if j == True:
            primeList.append(i)
        i += 1
    return primeList

maxPrimeAllowed = 1000000
primeList = genPrimesList(maxPrimeAllowed)
offset = 0
maxPrime,maxPrimeInfo = 0,{'offset':0,'r':0}

while True:
    tempNum,tMaxPrime,tMaxPrimeRound = 0,0,0
    r = 0
    for prime in primeList[offset:]:
        tempNum += prime
        r += 1
        if tempNum <= maxPrimeAllowed:
            if tempNum in primeList:
                tMaxPrime = tempNum
                tMaxPrimeRound = r
        else:break
    if tMaxPrimeRound > maxPrimeInfo['r']:
        maxPrime = tMaxPrime
        maxPrimeInfo = {'offset':offset,'r':tMaxPrimeRound}
    offset += 1
    if maxPrimeInfo['r']-15 > tMaxPrimeRound:
        print maxPrime
        break
