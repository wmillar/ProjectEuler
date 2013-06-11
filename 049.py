'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
'''
from itertools import permutations

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

def genPermutations(num):
    global primeList,numBlock
    numStr = str(num)
    permList,tempNum = [],""
    for p in permutations(numStr,len(numStr)):
        if p[0] != "0" and p[-1] not in numBlock:
            for c in p:
                tempNum += c
            permList.append(int(tempNum))
            tempNum = ""
    permList.sort()
    return permList

def testPermutations(permList):
    global primeList
    i = 0
    while i < len(permList)-2:
        if permList[i] in primeList:
            tempResult = [permList[i]]
            for j in xrange(1,3):
                tempNum = permList[i]+3330*j
                if tempNum in permList and tempNum in primeList:
                    tempResult.append(tempNum)
            if len(tempResult)==3:
                return tempResult
        i += 1
    return False

primeList = genPrimesList(9999)
numBlock = ('0','2','4','6','8')

for num in xrange(1000,3340):
    permList = genPermutations(num)
    if permList:
        tempResult = testPermutations(permList)
        if tempResult:
            if tempResult != [1487,4817,8147]:
                print str(tempResult[0])+str(tempResult[1])+str(tempResult[2])
                break

