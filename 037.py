'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
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

#outputs list of primes up to(including) limit
def genPrimesList(limit):
    primeList = []
    i = 2
    for j in genPrimes(limit).values():
        if j == True:
            primeList.append(i)
        i += 1
    return primeList

def truncLR(num):
    truncList = []
    i = 0
    limit = len(num)-1
    while i < limit:
        num = num[1:]
        yield num
        i += 1

def truncRL(num):
    truncList = []
    i = 0
    limit = len(num)-1
    while i < limit:
        num = num[:-1]
        yield num
        i += 1

def checkPrime(num):
    if num=="23":
        return True
    for c in num:
        if c=="0" or c=="2" or c=="4" or c=="6" or c=="8":
            return False
    return True
    

bigPrimeList = genPrimesList(999999)
totalSum = 0

for prime in bigPrimeList:
    primeStr = str(prime)
    if checkPrime(primeStr):
        allPrimes = True
        for num in truncLR(primeStr):
            try:
                bigPrimeList.index(int(num))
            except:
                allPrimes = False
                break
        if allPrimes:
            for num in truncRL(primeStr):
                try:
                    bigPrimeList.index(int(num))
                except:
                    allPrimes = False
                    break
            if allPrimes:
                totalSum += prime
                print prime

#remove 3,5,7 from sum
print totalSum-15
