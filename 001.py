'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sumOfMultiples(n, limit=1000):
    s = 0
    for i in xrange(n, limit, n):
        s += i
    return s

print sumOfMultiples(3) + sumOfMultiples(5) - sumOfMultiples(15)
