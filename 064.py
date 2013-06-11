'''
All square roots are periodic when written as continued fractions and can be
written in the form:

It can be seen that the sequence is repeating. For conciseness, we use the
notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

2=[1;(2)], period=1
3=[1;(1,2)], period=2
5=[2;(4)], period=1
6=[2;(2,4)], period=2
7=[2;(1,1,1,4)], period=4
8=[2;(1,4)], period=2
10=[3;(6)], period=1
11=[3;(3,6)], period=2
12= [3;(2,6)], period=2
13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
'''

def gcd(n, m):
    while m:
        m, n = n % m, m
    return n


def get_a(num, den_sq, den_n):
    '''input form: num / (den_sq**.5 + den_n)'''
    new_den_n = den_sq + (den_n * den_n * -1)
    div = gcd(num, new_den_n)
    num /= div
    new_den_n /= div
    new_num_n = -1 * den_n
    result = int((den_sq**.5 + new_num_n) / new_den_n)
    new_num_n -= result * new_den_n
    # return reciprocal of new
    return result, new_den_n, den_sq, new_num_n
    

def checkPattern(L, index):
    '''returns True if a pattern is detected'''
    for i in xrange(len(L) - index):
        if L[i] != L[index]:
            return False
        index += 1
    return True


def genContFract(n, length):
    generator = genContFractHelper(n)
    while True:
        result = []
        for count in xrange(length):
            result.append(generator.next())
        yield result


def genContFractHelper(n):
    current = int(n**.5)
    num = 1
    den_sq = n
    den_n = -1 * current
    while True:
        current, num, den_sq, den_n = get_a(num, den_sq, den_n)
        yield current


def getPeriodLength(L):
    next_c = L.index(L[0], 1)
    while next_c != -1:
        if checkPattern(L, next_c):
            return next_c
        else:
            next_c = L.index(L[0], next_c + 1)
    return False


def countOddPeriods(limit):
    total = 0
    for n in xrange(2, limit + 1):
        if int(n**.5)**2 == n:
            continue
        length_inc = 500
        periodGenerator = genContFract(n, length_inc)
        length, period = 0, []
        while True:
            period.extend(periodGenerator.next())
            length += length_inc
            try:
                periodLength = getPeriodLength(period)
                break
            except:
                pass
        if periodLength % 2 == 1:
            total += 1
    return total


print countOddPeriods(10000)
