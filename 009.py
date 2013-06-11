'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
from math import pow

def triplet():
    for a in xrange(1, 333):
        a2 = pow(a, 2)
        for b in xrange(a+1, 1000):
            if b <= a:
                break
            b2 = pow(b, 2)
            c = 1000-a-b
            c2 = pow(c, 2)

            if a2+b2 == c2:
                return a*b*c

print triplet()
