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
from collections import deque


numDict = dict(zip('IVXLCDM', (1, 5, 10, 50, 100, 500, 1000)))
subtracts = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
numDict.update(dict(zip(subtracts, (numDict[c[1]]-numDict[c[0]] for c in subtracts))))
decDict = {value: key for key, value in numDict.items()}
decDescending = sorted(decDict.keys(), reverse=True)


def num2dec(string):
    string = deque(string)
    value = 0
    while string:
        c = string.popleft()
        if string and c + string[0] in subtracts:
            value += numDict[string.popleft()] - numDict[c]
        else:
            value += numDict[c]
    return value


def get_numeral_value(value):
    for v in decDescending:
        if value >= v:
            return v


def dec2num(n):
    result = ''
    while n:
        numeral_value = get_numeral_value(n)
        result += decDict[numeral_value]
        n -= numeral_value
    return result


with open('roman.txt', 'r') as f:
    numerals = f.read().splitlines()

print sum(len(num) - len(dec2num(num2dec(num))) for num in numerals)
