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

def rotateNum(num):
    num = str(num)
    rotations = []
    i = 0
    while i < len(num)-1:
        tempChar = num[0]
        num = num[1:] + tempChar
        rotations.append(num)
        i += 1
    return rotations

def goodRotateNum(rotationList):
    rotations = []
    for rotation in rotationList:
        #rotations beginning with a '0' are ignored
        if rotation[0] != "0":
            rotations.append(int(rotation))
    return rotations

def checkPrime(prime):
    prime = str(prime)
    for c in prime:
        if c=="2" or c=="4" or c=="6" or c=="8":
            return False
    return True

bigPrimeList = genPrimesList(999999)
circPrimesFound = 0

for prime in bigPrimeList:
    if checkPrime(prime):
        primeList = goodRotateNum(rotateNum(prime))
        goodPrime = True
        for num in primeList:
            try:
                bigPrimeList.index(num)
            except:
                goodPrime = False
                break
        if goodPrime:
            circPrimesFound += 1
#            print prime
print circPrimesFound+1
