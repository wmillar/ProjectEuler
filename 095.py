'''
The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496,
we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.
'''

def getDivisors(limit):
    '''return list of sums of divisors for every number as the index'''
    bigList = [1] * limit
    for n in xrange(2, limit):
        for m in xrange(n * 2, limit, n):
            bigList[m] += n
    return bigList


def getChainLength(start):
    '''returns chain length and minimum'''
    chain = set()
    chainLength = 0
    length = 1
    minimum = start
    next = divisors[start]
    while next != 1 and next != start and next <= 1000000:
        if next < minimum:
            minimum = next
        chain.add(next)
        chainLength += 1
        if len(chain) != chainLength:   # infinite loop
            next = 1
            break
        length += 1
        next = divisors[next]
    if next == 1 or next > 1000000:
        return False, False
    else:
        return length, minimum


divisors = getDivisors(10**6)
maxChainLength = 0
maxChainMin = None

for n in xrange(10, 10**6):
    chainLength, minimum = getChainLength(n)
    if chainLength > maxChainLength:
        maxChainLength = chainLength
        maxChainMin = minimum
print maxChainMin
