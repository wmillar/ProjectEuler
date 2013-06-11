spiralSize, spiralSum, currentNum = 1001, 1, 1
for i in xrange(2,spiralSize,2):
    currentNum += i
    spiralSum += currentNum
    currentNum += i
    spiralSum += currentNum
    currentNum += i
    spiralSum += currentNum
    currentNum += i
    spiralSum += currentNum
print spiralSum
