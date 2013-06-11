'''
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest
prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
'''
from itertools import combinations

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

def getCombinations(comboHelper,comboLength):
    comboList = []
    for combo in combinations(comboHelper,comboLength):
        comboList.append(combo)
    return comboList

def convListToInt(numList):
    tempNum = ""
    for n in numList:
        tempNum += n
    return int(tempNum)

primeDict = genPrimes(1000000)
primeDict[1] = False
primesChecked = {}

for number in xrange(56003,9999999,2):
    try:primesChecked[number]
    except:
        numberStr = str(number)
        minLimit = 10**(len(numberStr)-1)
        for comboLength in xrange(1,len(numberStr)):
            comboHelper = ""
            for d in xrange(len(numberStr)-1):
                comboHelper += str(d)
            comboList = getCombinations(comboHelper,comboLength)
            for combo in comboList:
                tempNumList,primeCombos = list(numberStr),0
                primesList = []
                for i in xrange(10):
                    replacement = str(i)
                    for index in combo:
                        tempNumList[int(index)] = replacement
                    tempNum = convListToInt(tempNumList)
                    if tempNum >= minLimit:
                        if primeDict[tempNum]:
                            primesChecked[tempNum] = True
                            primesList.append(tempNum)
                            primeCombos += 1
                            if primeCombos >= 8:
                                primesList.sort()
                                print primesList[0]
                                quit()

