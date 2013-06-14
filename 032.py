'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

def getDivisorPairs(n):
    divisors = []
    for div in xrange(2, int(n**.5)):
        if n % div == 0:
            divisors.append((div, n / div))
    return divisors


def checkPandigital(num, div1, div2):
    counter = [0] * 10
    for d in map(int, str(num) + str(div1) + str(div2)):
        counter[d] += 1
    return counter == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


pandList = []
for n in xrange(1000, 10000):
    for div1, div2 in getDivisorPairs(n):
        if checkPandigital(n, div1, div2):
            pandList.append(n)
            break

print sum(pandList)
