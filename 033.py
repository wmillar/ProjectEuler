'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

def checkFraction(numerator,denominator):
    if numerator == denominator:
        return False
    numeratorStr = str(numerator)
    denominatorStr = str(denominator)
    for char in "123456789":
        if numeratorStr.count(char) == denominatorStr.count(char) and \
           numeratorStr.count(char) == 1:
            if numeratorStr.index(char) == 0:
                tempNum = int(numeratorStr[1])
            else:
                tempNum = int(numeratorStr[0])
            if denominatorStr.index(char) == 0:
                tempDen = int(denominatorStr[1])
            else:
                tempDen = int(denominatorStr[0])
            if tempDen == 0:
                return False
            if float(numerator)/denominator == float(tempNum)/tempDen:
                return tempNum,tempDen,float(tempNum)/tempDen
    return False

def convertDec(decimal):
    decimalStr = str(decimal)
    if int(decimalStr[0]) == 0:
        decimalStr = decimalStr[decimalStr.index(".")+1:]
        numerator = decimal
        denominator = 1
        i = 0
        while i < len(decimalStr):
            numerator *= 10
            denominator *= 10
            i += 1
        return numerator,denominator
        
fractionMult = 1
for numerator in xrange(12,100):
    if numerator % 10 != 0:
        for denominator in xrange(12,100):
            if numerator % 10 != 0:
                if denominator > numerator:
                    result = checkFraction(numerator,denominator)
                    if result != False:
                        fractionMult *= result[2]
print convertDec(fractionMult)[1]
