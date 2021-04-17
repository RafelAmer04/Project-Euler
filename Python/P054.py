
"""
High Card: 0 | Needs a Value
One Pair: 1 | Needs a Value
Two Pairs: 2 | Needs a Value
Three of a Kind: 3 | Needs a Value
Straight: 4 | Needs a Value
Flush: 5 | Needs a Value
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
    RDICT = {"T":"10", "J":"11", "Q":"12", "K":"13", "A":"14"}
    f = 1

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
            f = i

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
    if f == 0 and RANKS[-1] == RANKS[-2]:
        HIGHEST = 6
        VALUE = RANKS[0]
    if f == 2 and RANKS[0] == RANKS[1]:
        HIGHEST = 6
        VALUE = RANKS[-1]

#   Four of a kind: 7
    for i in range(len(RANKS)-3):
        if RANKS[i] == RANKS[i+1] and RANKS[i] == RANKS[i+2] and RANKS[i] == RANKS[i+3]:
            HIGHEST = 7
            VALUE = RANKS[i]
    
#   Straight Flush: 8
        t = 0
        for i in range(1, len(RANKS)):
            if RANKS[i] == RANKS[i-1] + 1 and SUITS[i] == SUITS[i-1]:
                continue
            t = 1
        if t == 0:
            HIGHEST = 8
            VALUE = RANKS[-1]

#   Royal Flush: 9
    t = 0
    s = 0
    if RANKS == (10,11,12,13,14):
        s = 1
    for i in range(len(RANKS)-1):
        if SUITS[i] == SUITS[i+1]:
            continue
        t = 1
    if t == 0 and s == 1:
        HIGHEST = 9
        VALUE = 0

#   Highest Card: 0
    if HIGHEST == 0:
        VALUE =[RANKS[-1]]

    return HIGHEST, VALUE

sol = 0

f = open("P054.txt", "r")
t = f.read()
hands = t.split("\n")
f.close()

for h in hands:
    if len(h) != 29:
        continue
    P1 = GetScore(h[0:14])
    P2 = GetScore(h[15:])


    if P1[0] > P2[0]:
        sol += 1
    elif P1[0] == P2[0]:
        if P1[1] > P2[1]:
            sol += 1
            


print(sol) 
        

   