'''
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''
def checkDigits(num,multiplier):
    num2 = str(num*multiplier)
    num = str(num)
    for d in num2:
        if d not in num:
            return False
    return True

for num in xrange(1,500000):
    multiplier = 1
    while checkDigits(num,multiplier+1):
        multiplier += 1
    if multiplier == 6:
        print num
        break
