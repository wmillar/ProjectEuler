'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
'''

def divisorSum(num):
    divisors,limit = [],int(num**.5)+1
    for i in xrange(2,limit):
        if not num%i:
            if i not in divisors: divisors.append(i)
            if num/i not in divisors: divisors.append(num/i)
    if not divisors:return num+1    #num is prime
    else: return sum(divisors)+1+num

def P(num):
    PDict,divisorsSum = {0:1},{1:1}
    for x in xrange(2,num+1):       #get divisor sums
        divisorsSum[x] = divisorSum(x)
    if PDict.has_key(num):return PDict[num]
    for n in xrange(1,num+1):
        pSum = 0
        for k in xrange(1,n+1):
            pSum += divisorsSum[k]*PDict[n-k]
        PDict[n] = pSum/n
    return PDict[num]

#subtract 1 because [100] does not count
print P(100)-1
