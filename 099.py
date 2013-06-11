'''
Comparing two numbers written in index form like 211 and 37 is not
difficult, as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
'''

f = open("base_exp.txt","r")
dataList = []
while True:
    line = f.readline()
    if not line:break
    dataList.append((int(line[0:line.index(",")]),\
                     int(line[line.index(",")+1:len(line)-1])))
f.close()

maxNum,maxNumLine,i = 0,0,1
for x in dataList:
    tempNum = x[0]**(float(x[1])/10**5)
    if tempNum > maxNum:
        maxNum = tempNum
        maxNumLine = i
    i += 1
print maxNumLine
