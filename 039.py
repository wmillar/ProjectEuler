'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p  1000, is the number of solutions maximised?
'''

def checkTriangle(a,b,c):
    if a**2+b**2==c**2:
        return True
    return False

p = 8
a = 1
aLimit = p/3
tempSolutions,maxSolutions = 0,0    #default values

while True:
    if p > 1000:
        break
    if a == aLimit:
        a = 1
        p += 1
        aLimit = p/3
        if tempSolutions > maxSolutions:
            maxSolutions,mSP = tempSolutions,p-1
        tempSolutions = 0
    b = a+1
    c = p-b-a
    while True:
        if c <= b:
            a += 1
            break
        if checkTriangle(a,b,c):
            tempSolutions += 1
#            print a,b,c,p
        b += 1
        c -= 1
print mSP
