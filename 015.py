'''
Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''

def fact(n):
    result = 1
    for num in xrange(2, n + 1):
        result *= num
    return result

def choose(n, r):
    return fact(n) / (fact(r) * fact(n - r))


print choose(40, 20)
