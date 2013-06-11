def checkPrime(num):
    if num < 2:return False
    if num == 2 or num == 3:return True
    if num%2 == 0 or num%3 == 0:return False
    if num < 10:return True
    limit,i = int(num**.5),5
    while i <= limit:
        if num%i==0 or num%(i+2)==0:return False
        i += 6
    return True

currentNum,spiralSize,totalCorners,totalPrimes,i = 1,1,1.0,0,2
while True:
    spiralSize += 2
    totalCorners += 4
    for r in xrange(1,4):
        if checkPrime(currentNum+i*r):
            totalPrimes += 1
    currentNum += i*4
    if totalPrimes/totalCorners*100 < 10:
        print spiralSize
        break
    i += 2
