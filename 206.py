'''
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
'''

form = '1_2_3_4_5_6_7_8_9_0'
low  = int(form.replace('_','0'))
high = int(form.replace('_','9'))

def findFirstBase(low=low, base=2, increment=5000):
    while True:
        if base*base >= low:
            break
        base += increment
    for base in xrange(base-increment, base+1):
        if base*base >= low:
            break
    if base%10 == 0:
        return base
    else:
        return base+(10-base%10)    #makes sure base ends in 0

def findLastBase(high=high, base=2, increment=6500):
    while True:
        if base*base >= high:
            break
        base += increment
    for base in xrange(base-increment, base+1):
        if base*base >= high:
            break
    if base%10 == 1:
        return base-1
    else:
        return base-base%10         #makes sure base ends in 0

def checkNum(numStr):
    n = 1
    for d in numStr[:18:2]:
        if int(d) != n:
            return False
        n += 1
    return True



baseLow  = findFirstBase()
baseHigh = findLastBase()

for base in xrange(baseLow, baseHigh+1, 10):
    if checkNum(str(base*base)):
        print base
        break

