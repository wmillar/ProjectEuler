'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

factorial = [1] + map(lambda x: reduce(lambda x,y: x*y,
                                       range(1, x+1)), range(1, 10))
totalSum = 0
n = 2
while True:
    for n in xrange(n + 1, n + 50000):
        if n == sum(factorial[d] for d in map(int, str(n))):
            totalSum += n
            break
    else:
        break

print totalSum
