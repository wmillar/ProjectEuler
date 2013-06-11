'''
A number chain is created by continuously adding the square of the digits in
a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
def addSquares(num):
    numSum = 0
    num = str(num)
    for d in num:
        numSum += int(d)**2
    return numSum

numDict = {1:False,89:True}

totalNum = 0
for num in xrange(2,10000000):
    sqSum = addSquares(num)
    if numDict.has_key(sqSum):
        if numDict[sqSum]:
            totalNum += 1
    else:
        num1,num89 = False,False
        seq = []
        while True:
            sqSum = addSquares(sqSum)
            try:
#            if numDict.has_key(sqSum):
                if numDict[sqSum]:
                    totalNum += 1
                    num89 = True
                    break
                else:
                    num1 = True
                    break
            except:
#            else:
                seq.append(sqSum)
        if seq:
            if num89:
                for s in seq:
                    numDict[s] = True
            else:
                if num1:
                    for s in seq:
                        numDict[s] = False
        
print totalNum
