'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

maxPal = 0
for x in xrange(100,1000):
    for y in xrange(x, 1000):
        product = x*y
        productStr = str(product)
        if productStr == productStr[::-1]:
            if product > maxPal:
                maxPal = product
print maxPal
