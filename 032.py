'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''
pandigits = ("1","2","3","4","5","6","7","8","9")

def getDivisors(num):
    divisors = []
    i = 2
    while True:
        if num%i==0:
            tempResult = num/i
            if tempResult >= i:
                divisors.append((i,tempResult))
            else:
                return divisors
        i += 1

def checkPand(num,div1,div2):
    global pandigits
    seq = str(num)+str(div1)+str(div2)
    if seq.count("0") != 0:
        return False
    for dig in pandigits:
        if seq.count(dig) != 1:
            return False
    return True
        
pandList = []
for x in xrange(1000,10000):
    divisors = getDivisors(x)
    for div in divisors:
        if checkPand(x,div[0],div[1]):
            try:
                pandList.index(x)
            except:
#                print x,div[0],div[1]
                pandList.append(x)
                break
pandSum = 0
for n in pandList:
    pandSum += n
print pandSum
