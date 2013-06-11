'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

def convBin(num):
    maxPower = 0
    while True:
        if 2**maxPower > num:
            maxPower -= 1
            break
        maxPower += 1
    binary = ""
    while maxPower > -1:
        tempResult = 2**maxPower
        if tempResult <= num:
            binary += "1"
            num -= tempResult
        else:
            binary += "0"
        maxPower -= 1
    return binary

totalSum = 0
for num in xrange(1,1000000):
    numStr = str(num)
    if numStr == numStr[::-1]:
        tempResult = convBin(num)
        if tempResult == tempResult[::-1]:
            totalSum += num
print totalSum
