'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
'''

cubeDict = {}
for base in xrange(300,1000000000):
    sortedCube = ''.join(sorted(str(base**3)))
    if cubeDict.has_key(sortedCube):
        cubeDict[sortedCube].append(base)
        if len(cubeDict[sortedCube]) >= 5:
            print cubeDict[sortedCube][0]**3
            break
    else:cubeDict[sortedCube] = [base]

