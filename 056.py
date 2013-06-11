'''
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
'''

def addSum(num):
    num = str(num)
    Sum = 0
    for d in num:
        Sum += int(d)
    return Sum

maxSum = 0
for base in xrange(50,100):
    for power in xrange(90,100):
        result = addSum(base**power)
        if result > maxSum:
            maxSum = result
print maxSum
