'''
We shall define a square lamina to be a square outline with a square "hole" so
that the shape possesses vertical and horizontal symmetry. For example, using
exactly thirty-two square tiles we can form two different square laminae:


With one-hundred tiles, and not necessarily using all of the tiles at one time,
it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
'''


def getWays(emptyDim, tileLimit):
    emptyTiles = emptyDim * emptyDim
    tileDim = emptyDim + 2
    ways = 0
    while tileDim * tileDim - emptyTiles <= tileLimit:
        ways += 1
        tileDim += 2
    return ways


def sqLaminaeCount(tileLimit):
    emptyDim = 1
    totalWays = 0
    while True:
        ways = getWays(emptyDim, tileLimit)
        if ways == 0:
            return totalWays
        totalWays += ways
        emptyDim += 1


print sqLaminaeCount(10**6)
