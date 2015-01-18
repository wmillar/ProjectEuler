'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def arithSum(n):
    return n * (n + 1) / 2


def arithSumMult(m, n):
    return arithSum(n // m) * m


def multSum(a, b, n):
    return arithSumMult(a, n) + arithSumMult(b, n) - arithSumMult(a * b, n)


print multSum(3, 5, 999)
