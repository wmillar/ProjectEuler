'''
Consider quadratic Diophantine equations of the form:

x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2*2^2 = 1
2^2 - 3*1^2 = 1
9^2 - 5*4^2 = 1
5^2 - 6*2^2 = 1
8^2 - 7*3^2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is
obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest
value of x is obtained.
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


def getPeriod(n):
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
    return period[:periodLength]


def extendPeriodGenerator(period):
    periodLength = len(period)
    while True:
        for i in xrange(periodLength):
            yield period[i]
            

def calcConvergent(a, period):
    num, den = 1, period.pop()
    while period:
        n = period.pop()
        den, num = addFraction(n, 1, num, den)
    return addFraction(a, 1, num, den)


def addFraction(num1, den1, num2, den2):
    common = gcd(den1, den2)
    if common != 1:
        den1 /= common
        den2 /= common
        new_den = den1 * den2 * common
    else:
        new_den = den1 * den2
    new_num = num1 * den2 + num2 * den1
    common = gcd(new_num, new_den)
    return new_num / common, new_den / common


def convergentsGenerator(a, period):
    new_period = []
    periodGenerator = extendPeriodGenerator(period)
    yield a, 1
    while True:
        new_period.append(periodGenerator.next())
        yield calcConvergent(a, new_period[:])

    
def getSolution(D):
    period = getPeriod(D)
    for x, y in convergentsGenerator(int(D**.5), period):
        if pow(x, 2) - D * pow(y, 2) == 1:
            return x, y


maxX = 0
maxD = None
for n in xrange(2, 1001):
    if int(n**.5)**2 == n:
        continue
    x, y = getSolution(n)
    if x > maxX:
        maxX = x
        maxD = n
print maxD
