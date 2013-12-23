'''
The points P(x1, y1) and Q(x2, y2) are plotted at integer co-ordinates
and are joined to the origin, O(0,0), to form OPQ.


There are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 <= x1, y1, x2, y2 <= 2.


Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?
'''


def checkRightTriangle(P, Q):
    '''OPQ form a right triangle only if P.Q, (P-Q).Q, or (P-Q).P = 0'''
    # if P, Q are not valid, then it is impossible to form a triangle
    if not verifyCoordinates(P, Q):
        return False
    for P, Q in genNewCoordinates(P, Q):
        if dot(P, Q) == 0:
            return True
    return False


def genNewCoordinates(P, Q):
    yield P, Q
    R = subtract(P, Q)
    yield R, Q
    yield R, P


def sortCoordinate(P, Q):
    '''basic coordinate pair sorting'''
    if P[0] > Q[0]:
        return Q, P
    if P[0] < Q[0]:
        return P, Q
    if P[1] > Q[1]:
        return Q, P
    return P, Q


def verifyCoordinates(P, Q):
    '''verify that given coordinates form a triangle OPQ'''
    # points cannot be the same
    if P == Q:
        return False
    # slopes cannot be the same or be multiples of each other
    if slope(P) == slope(Q):
        return False
    return True


def subtract(A, B, size=2):
    C = []
    for i in xrange(size):
        C.append(A[i] - B[i])
    return tuple(C)


def slope(A):
    if A[0] == 0:
        return None
    return float(A[1]) / A[0]


def dot(A, B, size=2):
    result = 0
    for i in xrange(size):
        result += A[i] * B[i]
    return result


def genCoordinates(X, Y):
    '''X,Y = size in dimension, excludes (0,0)'''
    generator = genCoordinatesHelper(X, Y)
    generator.next()
    for coordinate in generator:
        yield coordinate


def genCoordinatesHelper(X, Y):
    for x in xrange(X + 1):
        for y in xrange(Y + 1):
            yield (x, y)


def genAllCoordinatePairs(X, Y):
    for coord1 in genCoordinates(X, Y):
        for coord2 in genCoordinates(X, Y):
            yield coord1, coord2


def countRightTriangles(X, Y):
    coordinates = set()
    for P, Q in genAllCoordinatePairs(X, Y):
        if checkRightTriangle(P, Q):
            coordinates.add(sortCoordinate(P, Q))
    return len(coordinates)


print countRightTriangles(50, 50)
