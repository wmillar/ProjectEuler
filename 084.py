'''
In the game, Monopoly, the standard board is set up in the following way:

GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL
H2                              C1
T2                              U1
H1                              C2
CH3                             C3
R4                              R2
G3                              D1
CC3                             CC2
G2                              D2
G1                              D3
G2J F3 U2 F2 F1 R3 E3 E2 CH2 E1 FP

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH
(chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we
are only concerned with cards that order a movement; any instruction not
concerned with movement will be ignored and the player will remain on the
CC/CH square.

Community Chest (2/16 cards):
    1. Advance to GO
    2. Go to JAIL
Chance (10/16 cards):
    1. Advance to GO
    2. Go to JAIL
    3. Go to C1
    4. Go to E3
    5. Go to H2
    6. Go to R1
    7. Go to next R (railway company)
    8. Go to next R
    9. Go to next U (utility company)
    10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and
we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with
sets of squares.

Statistically it can be shown that the three most popular squares, in order,
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24,
and GO (3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the
six-digit modal string.
'''
from random import randint, shuffle

IDtoNumDict = {'GO':0, 'A1':1, 'CC1': 2, 'A2':3, 'T1':4, 'R1':5, 'B1':6,
               'CH1':7, 'B2':8, 'B3':9, 'JAIL':10, 'C1':11, 'U1':12, 'C2':13,
               'C3': 14, 'R2':15, 'D1':16, 'CC2':17, 'D2':18, 'D3':19, 'FP':20,
               'E1':21, 'CH2':22, 'E2':23, 'E3':24, 'R3':25, 'F1':26, 'F2':27,
               'U2':28, 'F3':29, 'G2J':30, 'G1':31, 'G2':32, 'CC3':33, 'G3':34,
               'R4':35, 'CH3':36, 'H1':37, 'T2':38, 'H2':39}


def rollDice(numDice=2, sides=4):
    return [randint(1, sides) for r in xrange(numDice)]

def checkSameRoll(roll):
    roll = roll[:]
    check = roll.pop()
    for n in roll:
        if n != check:
            return False
    return True


# assumes L is sorted and len(L) > 1, helper for nextR/nextU
def nextNum(L, current):
    lowL = L[0]
    highL = L[-1]
    if current in L:
        if current == highL:
            return lowL
        else:
            return L[L.index(current) + 1]
    elif current > highL:
        return lowL
    elif current < lowL:
        return lowL
    else:
        L.append(current)
        L.sort()
        return L[L.index(current) + 1]

# approach for nextR/nextU was to be able to work with custom nums
def nextR(squareNum):
    return nextNum([5, 15, 25, 35], squareNum)

def nextU(squareNum):
    return nextNum([12, 28], squareNum)


# current = current square number
def move(current, distance):
    tmpNew = current + distance
    if distance > 0:
        if tmpNew < 40:
            return tmpNew
        else:
            return tmpNew - 40
    else:
        if tmpNew >= 0:
            return tmpNew
        else:
            return tmpNew + 40

def moveBack3(squareNum):
    return move(squareNum, -3)


def createChanceChest():
    chChest = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', nextR, nextR, nextU,
               moveBack3] + [None] * 6
    shuffle(chChest)
    return chChest

def createCommunityChest():
    coChest = ['GO', 'JAIL'] + [None] * 14
    shuffle(coChest)
    return coChest

# returns card in index 0
def nextChChest(chChest):
    card = chChest.pop(0)
    chChest.append(card)
    return card

def nextCoChest(coChest):
    card = coChest.pop(0)
    coChest.append(card)
    return card


def executeCard(card, squareNum):
    if not card:
        return squareNum
    elif isinstance(card, str):
        return IDtoNumDict[card]
    else:   # must be a function
        return card(squareNum)


# checks to see if current square num is on special tile, returns new tile num
def specialCase(squareNum, coChest, chChest):
    if squareNum == 30:
        return 10
    elif squareNum in (2, 17, 33):  # community chest
        return executeCard(nextCoChest(coChest), squareNum)
    elif squareNum in (7, 22, 36):  # chance
        return executeCard(nextChChest(chChest), squareNum)
    else:
        return squareNum


def checkFrequency(freqDict):
    freqList = sorted([(k, v) for k, v in freqDict.items()],
                      key=lambda x: x[1], reverse=True)
    return ''.join(str(freqList[i][0]).rjust(2, '0') for i in xrange(3))


# returns dict of num of landings on each tile
def monopolySim(rounds):
    frequencyDict = dict((n, 0) for n in xrange(40))
    chChest = createChanceChest()
    coChest = createCommunityChest()
    current = 0         # num of current square
    consecRolls = 0     # num of consecutive double rolls
    for r in xrange(rounds):
        roll = rollDice()
        if checkSameRoll(roll):
            consecRolls += 1
        else:
            consecRolls = 0
        if consecRolls == 3:    # go to jail
            current = 10
            consecRolls = 0
        else:
            current = move(current, sum(roll))
            current = specialCase(current, coChest, chChest)
        frequencyDict[current] += 1
    return checkFrequency(frequencyDict)

def runSim(trials, rounds):
    resultDict = {}
    for t in xrange(trials):
        tResult = monopolySim(rounds)
        if tResult not in resultDict:
            resultDict[tResult] = 0
        resultDict[tResult] += 1
    return sorted([(k, v) for k, v in resultDict.items()],
                  key=lambda x: x[1], reverse=True)[0][0]


# small chance that it produces wrong answer
print runSim(7, 200000)
