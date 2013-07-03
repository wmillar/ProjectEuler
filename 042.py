'''
The nth term of the sequence of triangle numbers is given by, t_n = 1/2n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

def solve_eq(n):
    return -0.5 + pow(0.25 - (2  * n), 0.5)


def t(n):
    return int(0.5 * n * (n + 1))


def isTriangleWord(word):
    wordValue = sum(ord(c) - 64 for c in word)
    return t(int(solve_eq(-wordValue))) == wordValue


wordList = open('words.txt', 'r').read().replace('"', '').split(',')
print map(isTriangleWord, wordList).count(True)
