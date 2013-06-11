'''
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...
             ^
It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

digitNum = (1,10,100,1000,10000,100000,1000000)
num,aSequence,nSeqLen,productValue = 0,"",0,1
for digitValue in digitNum:
    nextRound = False
    while True:
        if nextRound:
            break
        if nSeqLen >= digitValue:
            aSequence += numStr[nSeqLen-digitValue-len(numStr)+1]
            nextRound = True
        num += 1
        numStr = str(num)
        nSeqLen += len(numStr)
for digit in aSequence:
    productValue *= int(digit)
print productValue
