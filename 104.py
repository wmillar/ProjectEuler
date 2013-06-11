'''
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n1 + F_n2, where F_1 = 1 and F_2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F2749, which contains 575
digits, is the first Fibonacci number for which the first nine digits are
1-9 pandigital.

Given that F_k is the first Fibonacci number for which the first nine digits
AND the last nine digits are 1-9 pandigital, find k.
'''

def genFib():
    a = 1
    b = 1
    while True:
        c = a + b
        yield c
        a, b = b, c


def checkNum(n, sizePower):
    if not checkPandigital(n % 1000000000):
        return False
    if sizePower > 11:
        if not checkPandigital(n / pow(10, sizePower - 9)):
            return False
    else:
        return False
    return True


def checkPandigital(n):
    expected = 1
    for n in sorted([int(c) for c in str(n)]):
        if n != expected:
            return False
        expected += 1
    if expected == 10:
        return True
    else:
        return False


fibGenerator = genFib()
size = 1
sizePower = 0
k = 2
while True:
    n = fibGenerator.next()
    k += 1
    if n > size:
        size *= 10
        sizePower += 1
    if checkNum(n, sizePower):
        print k
        break
