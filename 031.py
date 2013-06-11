'''
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can £2 be made using any number of coins?
'''

def getSum(vList, seq):
    value = 0
    for n in xrange(len(seq)):
        value += seq[n]*vList[n]
    return value


def genNext(value, vList, seq):
    nSeq = dict()
    seqLen = len(vList)
    iMax = seqLen-1
    totalTypes = 0
    i = 1
    for d in xrange(seqLen):
        nSeq[d] = 0
    for n in seq[::-1]:
        if n > 0:
            totalTypes += 1
            if totalTypes == 2:
                lowIndex2 = seqLen-i
            if totalTypes == 1:
                lowIndex = seqLen-i
        i += 1
    if lowIndex < iMax:
        for d in xrange(lowIndex):
            nSeq[d] = seq[d]
        nSeq[lowIndex] = seq[lowIndex]-1
        i = lowIndex+1
    elif totalTypes == 1:
        for d in xrange(lowIndex):
            nSeq[d] = seq[d]
        nSeq[lowIndex] = seq[lowIndex]-1
        i = lowIndex+1
    else:
        for d in xrange(lowIndex2):
            nSeq[d] = seq[d]
        nSeq[lowIndex2] = seq[lowIndex2]-1
        i = lowIndex2+1
    cValue = getSum(vList, nSeq)
    while cValue < value:
        if cValue+vList[i] <= value:
            nSeq[i] += 1
            cValue += vList[i]
        else:
            i += 1
            if i > iMax:
                return False # unable to complete combo
    return [nSeq[d] for d in range(seqLen)]



value = 200
vList = (200,100,50,20,10,5,2,1)
sequence = [1,0,0,0,0,0,0,0]
total = 1   #include starting sequence


while sequence:
    sequence = genNext(value, vList, sequence)
    if sequence[-1] == value:
        total += 1
        break
    total += 1
print total
