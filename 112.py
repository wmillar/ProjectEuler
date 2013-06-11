'''
Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are bouncy. In fact, the least
number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

def bouncyNumber(num):
    increasingNumber,decreasingNumber = True,True
    num = str(num)
    prevNum = int(num[0])
    for d in num[1:]:
        d = int(d)
        if d > prevNum:
            decreasingNumber = False
        if d < prevNum:
            increasingNumber = False
        if decreasingNumber==False and increasingNumber==False:
            return True
        prevNum = d
    return False

totalNum = 9
bouncyNum = 0
percentage = 99.0/100

for x in xrange(10,9999999):
    totalNum += 1
    result = bouncyNumber(x)
    if result:
        bouncyNum += 1
    if bouncyNum >= percentage*totalNum:
        print x
        break
