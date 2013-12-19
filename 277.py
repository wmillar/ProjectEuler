'''
A modified Collatz sequence of integers is obtained from a starting
value a_1 in the following way:

a_n+1 = a_n / 3 if a_n is divisible by 3.
We shall denote this as a large downward step, "D".

a_n+1 = (4 * a_n + 2) / 3 if a_n divided by 3 gives a remainder of 1.
We shall denote this as an upward step, "U".

a_n+1 = (2 * a_n - 1) / 3 if a_n divided by 3 gives a remainder of 2.
We shall denote this as a small downward step, "d".

The sequence terminates when some a_n = 1.

Given any integer, we can list out the sequence of steps.
For instance if a_1=231, then the sequence {a_n} =
{231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "DdDddUUdDD".

Of course, there are other sequences that begin with that same sequence
"DdDddUUdDD....".
For instance, if a_1=1004064, then the sequence is
DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
In fact, 1004064 is the smallest possible a_1 > 10^6 that begins with
the sequence DdDddUUdDD.

What is the smallest a_1 > 10^15 that begins with the sequence
"UDDDUdddDDUDDddDdDddDDUDDdUUDd"?
'''

def sequenceGenerator(a_0):
    while a_0 != 1:
        mod = a_0 % 3
        if mod == 0:
            yield 'D'
            a_0 /= 3
        elif mod == 1:
            yield 'U'
            a_0 = (4 * a_0 + 2) / 3
        else:
            yield 'd'
            a_0 = (2 * a_0 - 1) / 3


def check(sequence, a_0):
    '''does a_0 satisfy the given sequence?'''
    seqGen = sequenceGenerator(a_0)
    seqLen = len(sequence)
    i = 0
    for c in seqGen:
        if i == seqLen:
            return True
        if c != sequence[i]:
            return False
        i += 1
    return i == seqLen


def aGenerator(start, inc):
    while True:
        yield start
        start += inc


def findMinimumSequence(seq):
    '''returns minimum a_0 and increment that satisfies seq'''
    if seq[0] == 'U':
        prev_a_0, prev_inc = 4, 6
    else:
        prev_a_0, prev_inc = {'D': 3, 'd': 2}[seq[0]], 3
    for i in xrange(2, len(seq) + 1):
        aGen = aGenerator(prev_a_0, prev_inc)
        subSeq = seq[:i]
        for a in aGen:
            if check(subSeq, a):
                break
        prev_a_0 = a
        prev_inc *= 3
    return prev_a_0, prev_inc


def aGreaterThan(sequence, a_min):
    '''returns the minimum a_0 > a_min that satisfies sequence'''
    a_0, inc = findMinimumSequence(sequence)
    mult = (a_min - a_0) / inc
    if a_0 + mult * inc > a_min:
        return a_0 + mult * inc
    else:
        return a_0 + (mult + 1) * inc


print aGreaterThan('UDDDUdddDDUDDddDdDddDDUDDdUUDd', 10**15)
