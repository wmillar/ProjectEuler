'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def concatNum(num):
    result = ""
    i = 0
    totalRounds = 1
    while i < 9:
        tempResult = str(num*totalRounds)
        result += tempResult
        totalRounds += 1
        i += len(tempResult)
    if i == 9:
        return result
    else:
        return False

def checkPandigital(numStr):
    if numStr.count("0") > 0:
        return False
    for r in xrange(1,10):
        tempResult = numStr.count(str(r))
        if tempResult != 1:
            return False
    return True

maxNum = 0
for num in xrange(1,100000):
    result = concatNum(num)
    if result:
        if checkPandigital(result):
            if result > maxNum:
                maxNum = result
print maxNum

