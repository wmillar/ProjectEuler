'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
factorial = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

totalSum = 0
for n in xrange(3, 50000):
    if n == sum(map(lambda x: factorial[x], map(int, str(n)))):
        totalSum += n
print totalSum
