"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def findDivisors(tempNum):
    tempList = [1,]
    iMax = tempNum**.5
    i = 2
    while i <= iMax:
        if tempNum % i == 0:
            tempList.append(i)
            tempList.append(tempNum/i)
        i += 1
    return tempList

def addList(tempList):
    tempListLen = len(tempList)
    tempSum = 0
    i = 0
    while i < tempListLen:
        tempSum += tempList[i]
        i += 1
    return tempSum

amicableSum = 0
amicableList = list()
num1 = 2
while num1 < 10000:
    while amicableList.count(num1) != 0:
        num1 += 1
    num1Sum = addList(findDivisors(num1))
    if num1Sum != 1 and num1Sum != num1:
        num2Sum = addList(findDivisors(num1Sum))
        if num2Sum == num1:
 #           print "Amicable pair: %s %s" % (num1,num1Sum)
            amicableList.extend([num1,num1Sum])
            amicableSum += num1 + num1Sum   
    num1 += 1
print amicableSum
