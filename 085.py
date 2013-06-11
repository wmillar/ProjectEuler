'''
By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.

solved while on OYOT so that is why its ugly code
'''

def countRectangles(x, y):
	x, y = x+1, y+1
	totalCombos = 0
	for cX in xrange(1, x):
		for cY in xrange(1, y):
			totalCombos += (x-cX)*(y-cY)
	return totalCombos

target = 2000000
difference = target
diffX, diffY = -1, -1

for x in xrange(1,100):
        y = x
        if countRectangles(x,x) > target:
                break
        while True:
                combos = countRectangles(x, y)
                if combos < target:
                        prevCombos = combos
                        prevCombosY = y
                else:
                        break
                y += 1
        difference1 = combos-target
        difference2 = target-prevCombos
        if difference1 < difference2:
                if difference1 < difference:
                        difference = difference1
                        diffX, diffY = x, y
        else:
                if difference2 < difference:
                        difference = difference2
                        diffX, diffY = x, prevCombosY
print diffX*diffY
