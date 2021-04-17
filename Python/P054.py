
"""
High Card: 0 | Needs a Value
One Pair: 1 | Needs a Value
Two Pairs: 2 | Needs a Value
Three of a Kind: 3 | Needs a Value
Straight: 4 | Needs a Value
Flush: 5
Full House: 6 | Needs a Value
Four of a Kind: 7 | Needs a Value
Straight Flush: 8 | Needs a Value
Royal Flush: 9
"""



def GetScore(hand):
    HIGHEST = 0
    VALUE = 0
    RANKS = []
    SUITS = []
    RDICT = {"T":"10", "J":"11", "Q":"12", "K":"13"}


    for i in range(0, len(hand), 3):
        RANKS.append(hand[i])
        SUITS.append(hand[i+1])
    
    for r in range(len(RANKS)):
        for k in RDICT.keys():
            RANKS[r] = RANKS[r].replace(k, RDICT[k])

    RANKS = list(map(int, RANKS))
    
    RANKS, SUITS = zip(*sorted(zip(RANKS, SUITS)))


#   One Pair: 1 
    for i in range(len(RANKS)-1):
        if RANKS[i] == RANKS[i+1]:
            HIGHEST = 1
            VALUE = RANKS[i]
            break


#   Two Pairs: 2
    if HIGHEST == 1:
        for i in range(len(RANKS)-1):
            if RANKS[i] == RANKS[i+1] and RANKS[i] != VALUE:
                HIGHEST = 2
                if RANKS[i] > VALUE:
                    VALUE = RANKS[i]


#   Three of a Kind: 3
    for i in range(len(RANKS)-2):
        if RANKS[i] == RANKS[i+1] and RANKS[i] == RANKS[i+2]:
            HIGHEST = 3
            VALUE = RANKS[i]


#   Straight: 4
        t = 0
        for i in range(1, len(RANKS)):
            if RANKS[i] == RANKS[i-1] + 1:
                continue
            t = 1
        if t == 0:
            HIGHEST = 4
            VALUE = RANKS[-1]


#   Flush: 5
    t = 0
    for i in range(len(SUITS)-1):
        if SUITS[i] == SUITS[i+1]:
            continue
        t = 1
    if t == 0:
        HIGHEST = 5
        VALUE = 0


#   Full House: 6







    print(RANKS, SUITS)

    return HIGHEST, VALUE






input =  "5D 6D 7D 8D 9C"

print(GetScore(input))