'''
The following iterative sequence is defined for the set of positive integers:

n => n/2    (n is even)
n => 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
def nextNum(n):
    if n%2==0: return n/2
    return 3*n+1


numDict = {2:1,13:9}
longestChain = -1

for num in xrange(2,1000000):
    origNum,chainLength,chain = num,1,[]
    if numDict.has_key(num):
        chainLength += numDict[num]
    else:
        chain.append(num)
        while True:
            num = nextNum(num)
            chainLength += 1
            if numDict.has_key(num):
                chainLength += numDict[num]
                break
            else:
                chain.append(num)
    if chain:
        i = 1
        for n in chain:
            numDict[n] = chainLength-i
            i += 1
    if chainLength > longestChain:
        longestChain = chainLength
        longestNum = origNum
print longestNum
