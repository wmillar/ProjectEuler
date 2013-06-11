'''
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg
'''


def getTotalCombinations(L):
    return sum(n[1] for n in L)


def getAllRolls(dice, sides):
    rollsDict = {}
    for roll in getCombinations(dice, sides):
        rollSum = sum(roll)
        if rollSum in rollsDict:
            rollsDict[rollSum] += 1
        else:
            rollsDict[rollSum] = 1
    return rollsDict


def printAllRolls(dice, sides):
    rollsDict = getAllRolls(dice, sides)
    rolls = sorted(rollsDict.items(), key=lambda x: x[0])
    totalCombinations = getTotalCombinations(rolls)
    print "Total combinations for %s dice with %s sides: %s" % (dice, sides,
                                                                totalCombinations)
    print "Sum\tCombinations\tProbability"
    for rollSum, combinations in rolls:
        print "%s\t%s\t\t%s" % (rollSum, combinations,
                             float(combinations) / totalCombinations)



def getCombinations(dice, sides):
    allRolls = []
    roll = [1] * dice
    while roll:
        allRolls.append(tuple(roll))
        roll = getCombinationsHelper(roll, dice, sides)
    return allRolls


def getCombinationsHelper(roll, dice, sides):
    i = 0
    newRoll = None
    while i < dice:
        if roll[i] < sides:
            newRoll = roll[:]
            newRoll[i] += 1
            break
        i += 1
    if newRoll == None:
        return None
    if i == 0:
        return newRoll
    for new_i in xrange(i-1, -1, -1):
        newRoll[new_i] = 1
    return newRoll


def winsCombinations(prob1, prob2):
    '''Returns the number of cases where prob1 beats prob2'''
    totalWins = 0
    for rollSum1, combinations1 in prob1:
        for rollSum2, combinations2 in prob2:
            if rollSum1 > rollSum2:
                totalWins += combinations1 * combinations2
            else:
                break
    return totalWins



peterRolls = sorted(getAllRolls(9, 4).items(), key=lambda x: x[0])
peterCombinations = getTotalCombinations(peterRolls)
colinRolls = sorted(getAllRolls(6, 6).items(), key=lambda x: x[0])
colinCombinations = getTotalCombinations(colinRolls)


peterWins = winsCombinations(peterRolls, colinRolls)
print round(float(peterWins) / (peterCombinations * colinCombinations), 7)
