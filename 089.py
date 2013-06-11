'''
The rules for writing Roman numerals allow for many ways of writing each number
(see About Roman Numerals...). However, there is always a "best" way of writing
a particular number.

For example, the following represent all of the legitimate ways of writing
the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey thesubtractive pair rule (see About Roman Numerals...
for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
'''

f = open('roman.txt', 'r')
roman = f.read().splitlines()
f.close()

valueDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
valueOrder = 'IVXLCDM'

def convRomToDec(numerals):
    global valueDict, valueOrder
    value = 0
    while numerals:
        cNum,cNumConsec = numerals[0],1
        for c in numerals[1:]:
            if c == cNum:
                cNumConsec += 1
            else:
                break
        if cNumConsec > 1:
            value += valueDict[cNum]*cNumConsec
            numerals = numerals[cNumConsec:]
        else:
            if len(numerals) > 1:
                if valueOrder.index(numerals[1]) > valueOrder.index(cNum):
                    value += valueDict[numerals[1]]-valueDict[cNum]
                    numerals = numerals[2:]
                else:
                    value += valueDict[cNum]
                    numerals = numerals[1:]
            else:
                value += valueDict[cNum]
                numerals = numerals[1:]
    return value

def convDecToRom(num):
    global valueDict, valueOrder
    values,numStr,numerals = [],str(num),''
    numeralDict = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
    while numStr:
        values.append(int(numStr[0]+'0'*(len(numStr)-1)))
        numStr = numStr[1:]
    for n in values:
        if n in numeralDict:
            numerals += numeralDict[n]
        else:
            if n == 0:
                pass
            elif n < 4:     #1-3
                numerals += 'I'*n
            elif n < 10:    #5-9
                numerals += 'V'+'I'*(n-5)
            elif n < 40:    #20-30
                numerals += 'X'*(n/10)
            elif n < 90:    #50-80
                numerals += 'L'+'X'*((n-50)/10)
            elif n < 500:   #200-400
                numerals += 'C'*(n/100)
            elif n < 900:   #600-800
                numerals += 'D'+'C'*((n-500)/100)
            else:           #2000+
                numerals += 'M'*(n/1000)
    return numerals

savedChar = 0
for numerals in roman:
    savedChar += len(numerals)-len(convDecToRom(convRomToDec(numerals)))
print savedChar