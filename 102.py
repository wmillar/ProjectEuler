'''
Three distinct points are plotted at random on a Cartesian plane, for which
-1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

    A(-340,495), B(-153,-910), C(835,-947)

    X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle
XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
file containing the co-ordinates of one thousand "random" triangles, find the
number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the
example given above.
'''

def getPoints():
    points = []
    f = file('triangles.txt', 'r')
    for line in [map(int, line.split(',')) for line in f.readlines()]:
        points.append(map(lambda i: tuple(line[i:i + 2]), range(0, 6, 2)))
    return points


def getB(p1, p2):
    return p1[1] - float(p2[1] - p1[1]) / (p2[0] - p1[0]) * p1[0]


def getSides(points):
    sideDict = {'L':[], 'R':[]} 
    for p in points:
        if p[0] < 0:
            sideDict['L'].append(p)
        else:
            sideDict['R'].append(p)
    return sorted(sideDict.values(), key=lambda x: len(x))


def opposites(L):
    return L[0] > 0 and L[1] < 0 or L[1] > 0 and L[0] < 0


def containsOrigin(points):
    vertex, points = getSides(points)
    if not vertex:
        return 0
    b = [getB(vertex[0], p) for p in points]
    if opposites(b) or 0 in b:
        return 1
    return 0


print sum(map(containsOrigin, getPoints()))
