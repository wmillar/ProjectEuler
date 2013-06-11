'''
In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example
1 below). But if two ranks tie, for example, both players have a pair of
queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	    5H 5C 6S 7S KD          2C 3S 8S 8D TD              Player 2
            Pair of Fives           Pair of Eights

2	    5D 8C 9S JS AC          2C 5C 7D 8S QH              Player 1
            Highest card Ace        Highest card Queen

3	    2D 9C AS AH AC          3D 6D 7D TD QD              Player 2
            Three Aces              Flush with Diamonds

4	    4D 6S 9H QH QC          3D 6D 7H QD QS              Player 1
            Pair of Queens          Pair of Queens
            Highest card Nine       Highest card Seven

5	    2H 2D 4C 4D 4S          3C 3D 3S 9S 9D       	Player 1
            Full House              Full House
            With Three Fours        with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a
clear winner.

How many hands does Player 1 win?
'''

f = open('poker.txt','r')
hands1,hands2 = [],[]
while True:
    data = f.readline()
    if not data:break
    tHand,tCard = [],""
    tData = data[0:14]+' '
    for c in tData:
        if c == ' ' or c == '\n':
            tHand.append(tCard)
            tCard = ""
        else:
            tCard += c
    hands1.append(tHand)
    tData,tHand = data[15:],[]
    for c in tData:
        if c == ' ' or c == '\n':
            tHand.append(tCard)
            tCard = ""
        else:
            tCard += c
    hands2.append(tHand)
f.close()

def scanHand(handList):
    values = ('2','3','4','5','6','7','8','9','T','J','Q','K','A')
    valueList = []
    valueDict = {}
    suitDict = {}
    suitTypes = 0
    valueTypes = 0
    for hand in handList:
        cardValue = hand[0]
        cardSuit = hand[1]
        if valueDict.has_key(cardValue):
            valueDict[cardValue].append(cardSuit)
        else:
            valueDict[cardValue] = [cardSuit]
            valueTypes += 1
        if suitDict.has_key(cardSuit):
            suitDict[cardSuit].append(cardValue)
        else:
            suitDict[cardSuit] = [cardValue]
            suitTypes += 1
        valueList.append(values.index(cardValue)+2)
    valueListSorted = valueList[:]
    valueListSorted.sort()
    if suitTypes == 1:  #possible flush
        if valueTypes == 5:
            straightFlush = True
            if valueListSorted[0] == 10:    #possible royal flush
                royalFlush = True
            else:royalFlush = False
            if royalFlush:
                for x in xrange(10,15):
                    if x not in valueList:
                        royalFlush = False
                        break
                if royalFlush:return 10000  #royal flush
            for x in xrange(valueListSorted[0]+1,valueListSorted[0]+5):
                if x not in valueList:
                    straightFlush = False
                    break
                if straightFlush:return 9000 #straight flush
        return 6000      #if not royal/straight flush, must be normal flush
    valueSet = set(valueList)
    if valueTypes == 2:
        for x in valueSet:
            if valueList.count(x) == 4:     #four of a kind
                return 8000
        return 7000     #if not four of a kind, has to be full house
    if valueTypes == 5:
        straight = True
        for x in xrange(valueListSorted[0]+1,valueListSorted[0]+5):
            if x not in valueList:
                straight = False
                break
        if straight:return 5000     #straight
    if valueTypes == 3:     #either two pair of three of a kind
        threeOfKind = False
        for x in valueSet:
            if valueList.count(x) == 3:
                threeOfKind = True
        if threeOfKind:return 4000  #three of a kind
        else:       #must be two pair
            return 3000             #two pairs
    if valueTypes == 4:             #one pair
        for x in valueSet:
            if valueList.count(x) == 2:
                return 2000+x
    return 1000+max(valueList)      #high card

wins = 0
for i in xrange(1000):
    value1 = scanHand(hands1[i])
    value2 = scanHand(hands2[i])
    if value1 > value2:
        wins += 1
print wins
