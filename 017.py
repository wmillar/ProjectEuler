def genStringLength(tempGenStr):
    tempGenStr = tuple(tempGenStr)
    i = 0
    tempStrLen = len(tempGenStr)
    newStrLen = 0
    while i < tempStrLen:
        tempGenStrRaise = True
        tempGenStrChar = tempGenStr[0+i]
        if tempGenStrChar == " " or tempGenStrChar == "-":
            tempGenStrRaise = False
        if tempGenStrRaise:
            newStrLen += 1
        i += 1
    return newStrLen

def genWords1(genWords1Num):
    if type(genWords1Num) != type(1):
        genWords1Num = int(genWords1Num)
    if genWords1Num == 1:
        return "one"
    if genWords1Num == 2:
        return "two"
    if genWords1Num == 3:
        return "three"
    if genWords1Num == 4:
        return "four"
    if genWords1Num == 5:
        return "five"
    if genWords1Num == 6:
        return "six"
    if genWords1Num == 7:
        return "seven"
    if genWords1Num == 8:
        return "eight"
    if genWords1Num == 9:
        return "nine"
    return ""
def genWords2(genWords2Num):
    if type(genWords2Num) != type(1):
        genWords2Num = int(genWords2Num)
    if genWords2Num == 1:
        return "ten"
    if genWords2Num == 2:
        return "twenty"
    if genWords2Num == 3:
        return "thirty"
    if genWords2Num == 4:
        return "forty"
    if genWords2Num == 5:
        return "fifty"
    if genWords2Num == 6:
        return "sixty"
    if genWords2Num == 7:
        return "seventy"
    if genWords2Num == 8:
        return "eighty"
    if genWords2Num == 9:
        return "ninety"
    return ""
def genWords3(genWords3Num):
    if type(genWords3Num) != type(1):
        genWords3Num = int(genWords3Num)
    if genWords3Num == 11:
        return "eleven"
    if genWords3Num == 12:
        return "twelve"
    if genWords3Num == 13:
        return "thirteen"
    if genWords3Num == 14:
        return "fourteen"
    if genWords3Num == 15:
        return "fifteen"
    if genWords3Num == 16:
        return "sixteen"
    if genWords3Num == 17:
        return "seventeen"
    if genWords3Num == 18:
        return "eighteen"
    if genWords3Num == 19:
        return "nineteen"

def genWords(genWordsNum):
    genWordsStr = str(genWordsNum)
    genWordsLen = len(genWordsStr)
    if genWordsLen == 1:
        return genWords1(genWordsNum)
    if genWordsLen == 2:
        if genWordsNum >= 11 and genWordsNum <= 19:
            return genWords3(genWordsNum)
        genWordsPart1 = genWords2(genWordsStr[0])
        genWordsPart2 = genWords1(genWordsStr[1])
        if genWordsPart2 == "":
            return genWordsPart1
        return genWordsPart1 + "-" + genWordsPart2
    genWordsStr2 = genWordsStr[1] + genWordsStr[2]
    if genWordsLen == 3:
        genWordsPart1 = genWords1(genWordsStr[0])
        genWordsPart1 += " hundred"
        if int(genWordsStr2) >= 11 and int(genWordsStr2) <= 19:
            return genWordsPart1 + " and " + genWords3(genWordsStr2)
        genWordsPart2 = genWords2(genWordsStr[1])
        genWordsPart3 = genWords1(genWordsStr[2])
        if genWordsNum % 100 == 0:
            return genWordsPart1
        if int(genWordsStr2) % 10 == 0:
            return genWordsPart1 + " and " + genWordsPart2
        if int(genWordsStr[1]) == 0 and int(genWordsStr[2]) < 10:
            return genWordsPart1 + " and " + genWordsPart3
        return genWordsPart1 + " and " + genWordsPart2 + "-" + genWordsPart3
    if genWordsLen == 4:
        return "one thousand"
i = 1
totalChars = 0
while i <= 1000:
    chars =  genStringLength(genWords(i))
    totalChars += chars
#    print "%s %s ... %s ... total: %s" % (i,genWords(i),chars,totalChars)
    i += 1
print totalChars
