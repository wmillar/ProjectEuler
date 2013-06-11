triangleRaw = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#input string of triangle, converts it to a list
def convToTriangle(raw_triangle):
    i, triangle, tempList = 0, list(), list()
    for num in triangleRaw:
        if num == "\n":
            triangle.append(tempList)
            tempList = list()
            i = 0
        if num != " " and num != "\n":
            i += 1
            if i == 1:
                tempNum = num
            if i == 2:
                tempNum += num
                tempList.append(int(tempNum))
                i = 0
    return triangle

triangle = convToTriangle(triangleRaw)

for row in xrange(len(triangle)-1,-1,-1):
    for column in xrange(0,len(triangle[row])-1):
        triangle[row-1][column] += max(triangle[row][column],triangle[row][column+1])
        print triangle
print triangle[0][0]
