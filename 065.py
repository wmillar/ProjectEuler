'''
The infinite continued fraction can be written, 2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, 23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for
square roots provide the best rational approximations. Let us consider the
convergents for 2.

Hence the sequence of the first ten convergents for 2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the
continued fraction for e.
'''

#create the actual sequence
def createSequence(sequence,seqLength,indexMult,multiplier,limit):
    tempSeq, i = list(sequence), 1
    indexMultMod = indexMult - 1
    totalIndex = seqLength
    while totalIndex < limit:
        tempIndex = totalIndex % seqLength
        if tempIndex == indexMultMod:
            tempSeq.append(indexMult + multiplier*i)
            i += 1
        else:
            tempSeq.append(sequence[tempIndex])
        totalIndex += 1
    return tempSeq


seqInit        = 2          #initial number (not part of sequence)
sequence       = 1,2,1      #infite continued fraction sequence
seqIndexDouble = 2          #index of which number to double thru each pass


convergenceLimit = 99

seq = createSequence(sequence,len(sequence),seqIndexDouble,2,convergenceLimit)
numerator,denominator = 1,seq[-1]
index = 1
while index < convergenceLimit:
    addNum = seq[-(index+1)]
    numerator = denominator * addNum + numerator
    tempNum = numerator
    numerator = denominator
    denominator = tempNum
    index += 1
numerator += denominator*2

numeratorSum = 0
for d in str(numerator):
    numeratorSum += int(d)
print numeratorSum

