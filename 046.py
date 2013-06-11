'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
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

primeList = genPrimesList(10000)
for num in xrange(9,10000,2):
    if num not in primeList:
        maxPrime = num-2
        if maxPrime in primeList:
            pass
        else:
            for prime in primeList:
                nextNum = False
                if prime > maxPrime:
                    print num
                    quit()
                    break
                base = 2
                while True:
                    tempResult = prime + 2*(base**2)
                    if tempResult == num:
                        nextNum = True
                        break
                    if tempResult > num:
                        break
                    base += 1
                if nextNum:
                    break
