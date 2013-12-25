'''
The binomial coefficient C(10, 3) = 120.
120 = 2**3 * 3 * 5 = 2 * 2 * 2 * 3 * 5, and 2 + 2 + 2 + 3 + 5 = 14.
So the sum of the terms in the prime factorisation of C(10, 3) is 14.

Find the sum of the terms in the prime factorisation of C(20000000, 15000000).
'''


class Range(object):
    def __init__(self, start, end, inc=1):
        '''start <= end, inc >= 1, endpoint inclusive'''
        self.start = start
        self.end = end
        self.inc = inc


class RangeHolder(object):
    def __init__(self, r_obj):
        self.r = [r_obj]    # range container
        self.numbers = {}   # key=base, value=power

    def cancelCommonNumbers(self, other):
        '''ideally other (Range object) should contain more numbers'''
        for n in self.numbers.keys():
            if n in other.numbers:
                p = min((self.numbers[n], other.numbers[n]))
                self.decreaseNumber(n, p)
                other.decreaseNumber(n, p)

    def increaseNumber(self, n, p):
        if n == 1:
            return
        if n in self.numbers:
            self.numbers[n] += p
        else:
            self.numbers[n] = p

    def decreaseNumber(self, n, p):
        '''assumes n in numbers and numbers[n] >= p'''
        if self.numbers[n] == p:
            del self.numbers[n]
        else:
            self.numbers[n] -= p

    def containsRangeInc(self, inc):
        '''returns True if contains a range with given inc'''
        for r_obj in self.r:
            if r_obj.inc == inc:
                return True
        return False

    def getRangeInc(self, inc):
        '''get a Range object with given inc
        assumes Range object exists'''
        for r_obj in self.r:
            if r_obj.inc == inc:
                return r_obj

    def cancellationAppend(self, L):
        '''reinsert ranges/numbers in L back after cancellation'''
        for n in L:
            if isinstance(n, int):
                self.increaseNumber(n, 1)
            else:
                self.r.append(n)


def C_Range(n, k):
    '''returns numerator and denominator Ranges for C(n, k)'''
    return Range(n-k+1, n, 1), Range(1, k, 1)


def reduceRange(r_obj):
    '''reduce Range object (inc 1) to 2**n * oddRange * Range'''
    if r_obj.start == r_obj.end:
        return 0, obj.start, 1
    if r_obj.start % 2 == 0:
        if r_obj.end % 2 == 0:  # Range(even, even)
            pow2 = ((r_obj.end - r_obj.start) / 2) + 1
            oddRange = Range(r_obj.start + 1, r_obj.end - 1, 2)
            newRange = Range(r_obj.start / 2, r_obj.end / 2)
        else:                   # Range(even, odd)
            pow2 = ((r_obj.end - r_obj.start) / 2) + 1
            oddRange = Range(r_obj.start + 1, r_obj.end, 2)
            newRange = Range(r_obj.start / 2, r_obj.end / 2)
    else:
        if r_obj.end % 2 == 0:  # Range(odd, even)
            pow2 = ((r_obj.end - r_obj.start) / 2) + 1
            oddRange = Range(r_obj.start, r_obj.end - 1, 2)
            newRange = Range((r_obj.start / 2) + 1, r_obj.end / 2)
        else:                   # Range(odd, odd)
            pow2 = ((r_obj.end - r_obj.start) / 2)
            oddRange = Range(r_obj.start, r_obj.end, 2)
            newRange = Range((r_obj.start / 2) + 1, r_obj.end / 2)
    return pow2, simplifyRange(oddRange), simplifyRange(newRange)


def simplifyRange(r_obj):
    '''Range(1,3,2) -> 3, Range(1,3,1) -> Range(2,3), Range(3,3,1) -> 3'''
    if r_obj.start == 1:
        if r_obj.start + r_obj.inc <= r_obj.end:
            r_obj = Range(r_obj.start + r_obj.inc, r_obj.end, r_obj.inc)
    if r_obj.start == r_obj.end:
        return r_obj.start
    return r_obj


def cancelRanges(r_obj1, r_obj2):
    '''cancel common ranges in r_obj1 and r_obj2 (Range objects, inc=1)'''
    ro1_reduced, ro2_reduced = [], []
    # check left endpoints
    if r_obj1.start > r_obj2.start:
        ro2_reduced.append(simplifyRange(Range(r_obj2.start, r_obj1.start-1)))
    elif r_obj1.start < r_obj2.start:
        ro1_reduced.append(simplifyRange(Range(r_obj1.start, r_obj2.start-1)))
    # check right endpoints
    if r_obj2.end > r_obj1.end:
        ro2_reduced.append(simplifyRange(Range(r_obj1.end+1, r_obj2.end)))
    elif r_obj1.end > r_obj2.end:
        ro1_reduced.append(simplifyRange(Range(r_obj2.end+1, r_obj1.end)))
    return ro1_reduced, ro2_reduced


def commonOddRanges(r_obj1, r_obj2):
    '''do these odd ranges have any numbers in common?'''
    if r_obj1.start > r_obj2.start:
        return r_obj2.end >= r_obj1.start
    elif r_obj1.start < r_obj2.start:
        return r_obj1.end >= r_obj2.start
    return True


def cancelOddRanges(r_obj1, r_obj2):
    '''cancel common odd ranges'''
    ro1_r, ro2_r = [], []
    if r_obj1.start > r_obj2.start:
        ro2_r.append(simplifyRange(Range(r_obj2.start, r_obj1.start-2, 2)))
    elif r_obj1.start < r_obj2.start:
        ro1_r.append(simplifyRange(Range(r_obj1.start, r_obj2.start-2, 2)))
    if r_obj2.end > r_obj1.end:
        ro2_r.append(simplifyRange(Range(r_obj1.end+2, r_obj2.end, 2)))
    elif r_obj2.end < r_obj1.end:
        ro1_r.append(simplifyRange(Range(r_obj2.end+2, r_obj1.end, 2)))
    return ro1_r, ro2_r


def rangeHolderReduce(rh_obj, r_obj):
    '''applies reduction of r_obj (inc 1) to rh_obj'''
    pow2, oddRange, newRange = reduceRange(r_obj)
    if pow2:
        rh_obj.increaseNumber(2, pow2)
    if isinstance(oddRange, Range):
        rh_obj.r.append(oddRange)
    else:
        rh_obj.increaseNumber(oddRange, 1)
    if isinstance(newRange, Range):
        rh_obj.r.append(newRange)
    else:
        rh_obj.increaseNumber(newRange, 1)


def C_Reduced(n, k):
    '''returns simplified numerator/denominator RangeHolder of C(n, k)'''
    num, den = map(RangeHolder, C_Range(n, k))
    # initial reduction
    rangeHolderReduce(num, num.r.pop())
    if num.containsRangeInc(1):
        r_obj1 = num.getRangeInc(1)
        num.r.remove(r_obj1)
        r_obj2 = den.getRangeInc(1)
        den.r.remove(r_obj2)
        ro1_reduced, ro2_reduced = cancelRanges(r_obj1, r_obj2)
        num.cancellationAppend(ro1_reduced)
        den.cancellationAppend(ro2_reduced)
    # reduce to odd ranges
    for rh_obj in (num, den):
        while rh_obj.containsRangeInc(1):
            r_obj = rh_obj.getRangeInc(1)
            rh_obj.r.remove(r_obj)
            rangeHolderReduce(rh_obj, r_obj)
    den.cancelCommonNumbers(num)
    # cancel common odd ranges
    den_no_cancel = []
    while den.r:
        den_r_obj = den.r.pop(0)
        for num_r_obj in num.r:
            if not commonOddRanges(den_r_obj, num_r_obj):
                continue
            num.r.remove(num_r_obj)
            num_rr, den_rr = cancelOddRanges(num_r_obj, den_r_obj)
            num.cancellationAppend(num_rr)
            den.cancellationAppend(den_rr)
            break
        else:
            den_no_cancel.append(den_r_obj)
    den.r.extend(den_no_cancel)
    return num, den


def getPrimes(limit):
    sieve = [True] * limit
    for n in xrange(3, int(limit**.5) + 1, 2):
        if sieve[n]:
            sieve[n*n::n*2] = [False] * ((limit-n*n-1)/(n*2) + 1)
    return [n for n in xrange(3, limit, 2) if sieve[n]]


def factorSumOddRange(start, end):
    '''sum of prime factorization of an odd range'''
    def getMinNumber(n):
        '''get min num in range(start,end+1,2) which has a factor of n'''
        mult = start / n
        if mult % 2 == 0:
            return (mult + 1) * n
        elif mult * n < start:
            return (mult + 2) * n
        else:
            return mult * n

    L = range(start, end + 1, 2)
    total = 0
    for n in getPrimes(int(end**.5) + 1):
        for i in xrange((getMinNumber(n) - start) / 2, len(L), n):
            while L[i] % n == 0:
                L[i] /= n
                total += n
    for n in L:
        if n != 1:
            total += n
    return total


def pfSumChoose(n, k):
    num, den = C_Reduced(n, k)
    total = sum(factorSumOddRange(r_obj.start, r_obj.end) for r_obj in num.r)
    total -= sum(factorSumOddRange(r_obj.start, r_obj.end) for r_obj in den.r)
    total += sum(b * p for b, p in num.numbers.items())
    total -= sum(b * p for b, p in den.numbers.items())
    return total


print pfSumChoose(20 * 10**6, 15 * 10**6)
