'''
It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots is
infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of
the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums
of the first one hundred decimal digits for all the irrational square roots.
'''
from decimal import *
getcontext().prec = 102

def checkIrrational(num):
    tempNum = int(num**.5)
    if tempNum**2 == num:
        return False
    return True

decimalSum = 0

for num in xrange(2,100):
    if checkIrrational(num):
        decimals = str(Decimal(num).sqrt())
        decimals = decimals[:decimals.index('.')] + \
                   decimals[decimals.index('.')+1:]
        amountRemove = len(decimals)%100
        if amountRemove > 0:decimals = decimals[:-amountRemove]
        for d in decimals:
            decimalSum += int(d)
print decimalSum
