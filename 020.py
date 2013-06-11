'''
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is
3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

product,digitSum = 1,0
for x in xrange(2,101):
    product *= x
for d in str(product):
    digitSum += int(d)
print digitSum
