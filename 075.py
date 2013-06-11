'''
It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000
can exactly one integer sided right angle triangle be formed?
'''

def genTriplets(mLimit):
    for m in xrange(2, mLimit):
        for n in xrange(1, m):
            if coprime(m, n) and (m - n) % 2 != 0:
                yield calcTrip(m, n)


def coprime(a, b):
    aFactors = fDict[a]
    bFactors = fDict[b]
    # if a is prime and a > b, a and b must be coprime
    if not aFactors:
        return True
    # a is composite, b is prime, coprime if b not in a
    if not bFactors:
        return not b in aFactors
    # both composite, compare intersection of factors
    return len(aFactors.intersection(bFactors)) == 0

    
def calcTrip(m, n):
    return tuple(sorted([m * m - n * n, 2 * m * n, m * m + n * n]))


def uniquePrimeFactors(limit):
    pDict = {1: False, 2: False}
    for n in xrange(4, limit, 2):
        pDict[n] = set([2])
    for n in xrange(3, limit, 2):
        if n not in pDict:
            pDict[n] = False
            for n2 in xrange(n * 2, limit, n):
                if n2 not in pDict:
                    pDict[n2] = set([n])
                else:
                    pDict[n2].add(n)
    return pDict


def multTriplets(trip, limit):
    i = 2
    newTrip = [n*i for n in trip]
    while sum(newTrip) <= limit:
        yield tuple(newTrip)
        i += 1
        newTrip = [n*i for n in trip]


def multN(n, limit):
    c = n * 2
    while c <= limit:
        yield c
        c += n


targetLength = 1500000


tripDict = {}
generator = genTriplets(int(((targetLength*2 + 1)**.5) / 2) + 1)
fDict = uniquePrimeFactors(int(((targetLength*2 + 1)**.5) / 2) + 1)

for triplet in generator:
    tripSum = sum(triplet)
    if tripSum <= targetLength:
        if tripSum in tripDict:
            tripDict[tripSum].add(triplet)
        else:
            tripDict[tripSum] = set([triplet])

multiples = {}
for s in tripDict:
    for n in multN(s, targetLength):
        if n in multiples:
            multiples[n] += 1
        else:
            multiples[n] = 1

found = 0
for k, v in tripDict.items():
    if len(v) == 1 and k not in multiples:
        found += 1
for k,v in multiples.items():
    if v == 1 and k not in tripDict:
        found += 1

print found
