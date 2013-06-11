# -*- coding: cp1252 -*-
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''
def wordValue(word):
    global alphabet
    value = 0
    for char in word:
        value += alphabet.index(char)+1
    return value

def genTriNumbers(limit):
    numList = []
    i = 1
    while True:
        tempResult = int(.5*i*(i+1))
        if tempResult < limit:
            numList.append(tempResult)
        else:
            return numList
        i += 1

f = open("words.txt","r")
data = f.readline()
f.close()

alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M", \
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z")

wordList = []
index2 = -1
while True:
    index1 = index2 + 1
    try:
        index1 = data.index('"',index1)
        index2 = data.index('"',index1+1)
        word = data[index1+1:index2]
        wordList.append(word)
    except:
        break

wordValues = []
for word in wordList:
    wordValues.append(wordValue(word))
maxWValue = 0
for value in wordValues:
    if value > maxWValue:
        maxWValue = value
triangleList = genTriNumbers(maxWValue)

totalTriWords = 0
for value in wordValues:
    try:
        triangleList.index(value)
        totalTriWords += 1
    except:
        pass
print totalTriWords
